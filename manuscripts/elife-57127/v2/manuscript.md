# Structure of substrate-bound SMG1-8-9 kinase complex reveals molecular basis for phosphorylation specificity

## Authors

- Lukas M Langer<sup>1</sup> ([ORCID: 0000-0002-9977-2427](https://orcid.org/0000-0002-9977-2427))
- Yair Gat<sup>1</sup> ([ORCID: 0000-0002-2338-9384](https://orcid.org/0000-0002-2338-9384))
- Fabien Bonneau<sup>1</sup> ([ORCID: 0000-0001-8787-7662](https://orcid.org/0000-0001-8787-7662))
- Elena Conti<sup>1</sup> ([ORCID: 0000-0003-1254-5588](https://orcid.org/0000-0003-1254-5588)) †

### Affiliations

1. Department of Structural Cell Biology, Max Planck Institute of Biochemistry Martinsried Germany

† Corresponding author

## Abstract

PI3K-related kinases (PIKKs) are large Serine/Threonine (Ser/Thr)-protein kinases central to the regulation of many fundamental cellular processes. PIKK family member SMG1 orchestrates progression of an RNA quality control pathway, termed nonsense-mediated mRNA decay (NMD), by phosphorylating the NMD factor UPF1. Phosphorylation of UPF1 occurs in its unstructured N- and C-terminal regions at Serine/Threonine-Glutamine (SQ) motifs. How SMG1 and other PIKKs specifically recognize SQ motifs has remained unclear. Here, we present a cryo-electron microscopy (cryo-EM) reconstruction of a human SMG1-8-9 kinase complex bound to a UPF1 phosphorylation site at an overall resolution of 2.9 Å. This structure provides the first snapshot of a human PIKK with a substrate-bound active site. Together with biochemical assays, it rationalizes how SMG1 and perhaps other PIKKs specifically phosphorylate Ser/Thr-containing motifs with a glutamine residue at position +1 and a hydrophobic residue at position -1, thus elucidating the molecular basis for phosphorylation site recognition.

## Introduction

Family members of phosphatidylinositol 3-kinase-related kinases (PIKKs) activate distinct signaling pathways that promote cellular survival in different environmental and endogenous stress conditions (Baretić and Williams, 2014; Imseng et al., 2018; Lempiäinen and Halazonetis, 2009). Specifically, PIKKs oversee translation machinery in the cytoplasm (mTOR, SMG1), or regulate DNA damage repair in the nucleus (ATM, ATR and DNA-PK) (Shimobayashi and Hall, 2014; Saxton and Sabatini, 2017; Yamashita, 2013; Yamashita et al., 2001; Blackford and Jackson, 2017; Elías-Villalobos et al., 2019). With the exception of the enzymatically inactive TRAPP/Tra1, which serves as a scaffold in chromatin modification complexes, all other members of the PIKK family are Ser/Thr-protein kinases, and are among the largest proteins in the eukaryotic kinome. Recent publications have revealed the organization of PIKK active sites at better than 4 Å resolution (Gat et al., 2019; Zhu et al., 2019; Yang et al., 2013; Jansma et al., 2020; Yates et al., 2020), but the key question of how members of this kinase family recognize their substrates remains unanswered.

Human SMG1 is one of the largest PIKK family members (~410 kDa) and plays a crucial role in nonsense-mediated mRNA decay (NMD), a conserved pathway that regulates mRNA stability in the cytoplasm of eukaryotic cells (Kurosaki and Maquat, 2016; Karousis and Mühlemann, 2019). In its canonical surveillance function, the NMD pathway recognizes and degrades aberrant mRNAs containing premature translation termination codons, thus preventing the accumulation of truncated protein products. In addition, NMD also regulates the levels of a subset of normal, physiological transcripts, amounting to 5–10% of the transcriptome. In metazoans, SMG1 forms a stable complex with two additional proteins, SMG8 and SMG9, and specifically phosphorylates the RNA helicase UPF1. Phosphorylation of UPF1 is a crucial event in this pathway as it enables the recruitment of downstream NMD factors SMG5, SMG6 and SMG7, leading to ribonucleolytic cleavage of the RNA. SMG1 phosphorylates UPF1 specifically at Ser/Thr - Gln (SQ) motifs present in the unstructured N- and C-terminal regions that flank the helicase core (Yamashita et al., 2001; Denning et al., 2001). Specificity for a glutamine residue at the +1 position is shared by other PIKK family members, namely, ATM, ATR and DNA-PK kinases (Kim et al., 1999; Bannister et al., 1993). However, there is an additional layer of phosphorylation site specification. Among the 20 possible SQ motifs in UPF1, studies in vitro and in vivo have shown that only a selected few are effectively phosphorylated, including Ser1073, Ser1078, Ser1096 and Ser1116 (Yamashita et al., 2001; Ohnishi et al., 2003; Durand et al., 2016). Interestingly, these UPF1 phosphorylation sites share a Leu-Ser-Gln (LSQ) consensus sequence identical to the LSQ consensus motif identified in substrates of the ATM kinase (O'Neill et al., 2000; Kim et al., 1999). In this work, we studied the interaction between recombinant human SMG1-SMG8-SMG9 with UPF1 peptides using cryo-EM and mass spectrometry to identify the molecular basis with which SMG1, and potentially other PIKKs, recognizes specific phosphorylation sites in its substrate.

## Results and discussion

### Cryo-EM structure of the human SMG1-8-9 kinase complex bound to a UPF1 peptide

We used stably transfected HEK293T cells to express and purify a human wild-type SMG1-8-9 complex, as previously reported (Gat et al., 2019). The complex phosphorylated full-length recombinant UPF1 in a radioactive kinase assay (Figure 1—figure supplement 1A), confirming the enzymatic activity of purified SMG1 towards its physiological substrate. We selected a frequently phosphorylated site within UPF1 (Yamashita et al., 2001), Ser1078, and used a peptide spanning residues 1074–1084 (hereby defined as UPF1-LSQ) for subsequent structural and biochemical analysis (Figure 1—figure supplement 1B). We confirmed the ability of SMG1-8-9 to specifically phosphorylate UPF1-LSQ using a mass spectrometry-based phosphorylation assay (Figure 1—figure supplement 1C and D). This assay allowed us to monitor the relative amount of phosphorylation of a specific peptide over time. As a control, phosphorylation was abolished when Ser1078 was changed to Asp (Figure 1—figure supplement 1C and D). Hence, the reconstitutions used in this study recapitulate specific phosphorylation site selection.

For structure determination, we incubated SMG1-8-9 with UPF1-LSQ and AMPPNP, a non-hydrolyzable ATP analogue, and subjected the sample to cryo-EM single particle analysis. The final reconstruction reached an overall resolution of 2.9 Å (Figure 1—figure supplements 2 and 3), and allowed us to further complete and refine the published model for SMG1-8-9 (Supplementary file 1; Gat et al., 2019). Briefly, SMG1 consists of an N-terminal solenoid 'arch' and a compact C-terminal 'head' region (Figure 1A and B). The C-terminal 'head' is formed by the tight interaction between the catalytic module, typical of Ser/Thr-kinases, and the so-called FAT and FATC domains (Imseng et al., 2018; Baretić and Williams, 2014; Bosotti et al., 2000). The N-terminal ‘arch’ provides binding sites for both SMG8 and SMG9 (Figure 1A and B). As we had previously reported, SMG9 contains an unusual G-fold domain that binds ATP rather than GTP or GDP (Gat et al., 2019). The local resolution of around 3 Å allowed us to model SMG9-bound ATP in the reconstructed density, revealing the molecular basis for how the adenosine nucleotide is recognized by this unusual G-fold domain (Figure 1B and D, Figure 1—figure supplement 4). Briefly, the G4 and G5 motifs responsible for the recognition of the base have rearranged to preferentially bind an adenine base rather than a guanine (Figure 1—figure supplement 4).

![Figure 1.](https://cdn.elifesciences.org/articles/57127/elife-57127-fig1-v2.jpg)

**Figure 1.:** (A) Domain organization of SMG1, SMG8, SMG9 and UPF1. White parts are not resolved in the reconstruction. The sequence and location of UPF1-LSQ is indicated with blue text and dotted lines. (B) Segmented cryo-EM reconstruction of substrate-bound SMG1-8-9. Two different views are shown; proteins and domains are colored as in A. (C) A zoomed-in view of SMG1 showing the kinase active site with bound AMPPNP and UPF1-LSQ. Reconstructed density for UPF1-LSQ is shown as a blue mesh. (D) Zoom-in showing ATP bound to SMG9 with reconstructed density displayed as a blue mesh.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/57127/elife-57127-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Radioactive phosphorylation assay using SMG1-8-9 and full-length UPF1. Coomassie-stained SDS-PAGE showing a change in migration behavior for UPF1 over time as phosphorylation proceeds. The corresponding radioactive signal is shown in the lower panel indicating an increase of UPF1 phosphorylation over time. (B) Alignment showing all SQ motifs present in UPF1 N- and C-terminus including positions −2 to +3. Note the high variance amongst position −1 residues. (C) Mass spectrometry-based phosphorylation assay with UPF1-LSQ and the indicated position 0 variations. The peptide sequence is indicated with the varying position marked as ‘X’. Error bars representing standard deviations calculated from independent experimental triplicates are shown. Phosphorylation was abolished when the phospho-acceptor residue was changed from Ser to Asp. This shows Ser1081 was not recognized for phosphorylation and confirms specificity toward the SQ motif. In addition, phosphorylation was decreased when Ser was changed to Thr, consistent with previous data for ATM, ATR and DNA-PK (Kim et al., 1999; O'Neill et al., 2000). (D). M/z spectra for representative single measurements at indicated time points of the experiment shown in C. The inset lists the expected sizes for the three peptides used in this experiment. Peaks corresponding to unphosphorylated and phosphorylated peptides are highlighted. Note the appearance and increase of intensity of peaks corresponding to phosphorylated peptides over time.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/57127/elife-57127-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Coomassie-stained SDS-PAGE showing purified SMG1-8-9. The asterisk indicates contaminants. (B) Representative micrograph of the collected data set with some SMG1-8-9 particles indicated by blue circles. Scale bar ≈ 500 Å. (C) Representative 2D averages of picked particles. Scale bar ≈ 100 Å. (D) Spherical angular distribution of particles contributing to the final reconstruction with larger red rods indicating more prominent particle views and smaller blue rods indicating rarer particle views. (E) Map of SMG1-8-9 colored according to estimated local resolution shown in two different views as in Figure 1B. Large parts of the complex including the kinase domain and the bound UPF1 peptide are resolved to around 3 Å. Important features of the map are indicated. (F) Three-dimensional FSC plot and further analysis of orientation bias. The red line represents the estimated global masked half-map FSC curve indicating a nominal overall resolution of 2.97 Å according to the gold standard FSC cut off of 0.143 (Rosenthal and Henderson, 2003). The spread of directional resolution values is defined as ± 1σ (shown as dashed grey lines). Overall isotropy of the map is confirmed by a sphericity of 0.957 (out of 1) (Tan et al., 2017). (G) Model vs. map FSC plot for the real spaced refined model. (H) Model vs. map FSC plots for half map 1 ("work") used for real space refinement after displacing atoms of the final model (σ = 0.5 Å) and half map 2 not used for refinement ("free"). The good agreement of the two curves indicates that no substantial overfitting took place.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/57127/elife-57127-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** Processing steps are indicated in blue; particle numbers of classes used for downstream processing steps (in brackets: percentage with respect to initial candidate particles) and resolutions are in black. The class selected for the 3D refinement after the last step of 3D classification is indicated by a red rectangle. Density for the unmodelled, C-terminal part of SMG8 appearing in two other 3D classes not used for the final reconstruction is highlighted in magenta. This part of SMG8 has been suggested to contribute to kinase regulation (Zhu et al., 2019).

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/57127/elife-57127-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** (A) Detailed view of ATP purine ring recognition by SMG9 with important residues highlighted and reconstructed density indicated. (B) Two-dimensional sketch of adenine base recognition by SMG9 shown in panel A with G motifs, key residues and distances indicated. (C) Detailed view of GTP recognition by the GTPase RAS with important residues highlighted (PDB ID 1ZVQ). (D) Two-dimensional sketch of guanine base recognition shown in panel C by RAS with G motifs, key residues and distances indicated for comparison with panel B (based on PDB ID 1ZVQ). (E) Two-dimensional sketch of the overall recognition of ATP by SMG9. The G1-G3 motifs of SMG9 coordinate the phosphate moieties of ATP, similarly to the corresponding motifs of canonical GTPases, but with an important exception, in that they lack the typical residues crucial for catalysis. Another difference with canonical G-fold is that the G4 and G5 motifs responsible for the recognition of the base have rearranged to preferentially bind an adenine base rather than a guanine. (F) Sequence alignment of G motifs of RHEB and RAS GTPases with SMG9. Residues highlighted in A are indicated by a black dot. In the G4 motif, the aspartic acid that specifically engages the guanine moiety in GTPases has diverged to an arginine residue. Instead, Asn372 in the SMG9 G4 motif has shifted so that it engages the side-chain carbonyl group to interact with the adenine amino group (compare panels A and B with C and D). In the G5 motif, the SAK consensus sequence in RAS and RHEB has diverged in SMG9, with the main-chain carbonyl and amine groups of the upstream residues, Pro432 and Met434, forming adenine-specific interactions (compare panels A and B with C and D). (G) Three-dimensional sketches of SMG9 (top) and RAS/RHEB (bottom) highlighting similarities in their overall topology. Positions of the G motifs are highlighted.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/57127/elife-57127-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** (A) Active site density reported in this study. Densities attributed to either AMPPNP or UPF1 peptide are indicated. (B) Active site density of the apo SMG1-8-9 reconstruction reported previously (EMDB 10347). (C) Overlay of the active site densities shown in A and B with the active site density reported in this study shown in transparent grey and density of apo SMG1-8-9 (EMDB 10347) shown in blue. Densities attributed to either AMPPNP or UPF-LSQ are indicated. (D) Model of IP6 and UPF1-LSQ with the corresponding density shown as a blue mesh. Colors of the model as in Figure 1. (E) Additional parts of the model with the corresponding density shown as in B.

Importantly, compared to the previously published apo-SMG1-8-9 structure (Gat et al., 2019), the current reconstruction revealed extra density in the kinase active site accounting for both AMPPNP and UPF1-LSQ (Figure 1B and C, Figure 1—figure supplement 5A,B and C).

### Positioning of UPF1 Ser1078 in the SMG1 active site for phosphoryl transfer

The active site of SMG1 shows excellent density for residues 1075–1081 of UPF1-LSQ (Figure 1C, Figure 1—figure supplement 5). The directionality of the bound substrate peptide is consistent with that of other kinase structures, such as CDK2, and the arrangement of key active site residues is well conserved (Figure 2—figure supplement 1; Bao et al., 2011). The geometry of the catalytic loop (residues 2332 to 2340) and of the activation segment (residues 2352 to 2375) in the SMG1 kinase domain as well as orientation of important active site residues are very similar to those observed in mTOR (Figure 2—figure supplement 1B), indicative of an active kinase state (Yang et al., 2013). Specific recognition of the phosphorylation site is achieved via conserved residues contributed by the activation segment and the catalytic loop as well as by the FATC domain (Figure 2). The hydroxyl group of Ser1078, the phospho-acceptor residue in UPF1-LSQ, is positioned by residues of the catalytic loop, in particular Asp2335 and His2337 (Figure 2B and C, Figure 2—figure supplement 2A and B). Consistent with the structural observations, mutation of either of the corresponding residues in SMG1, mTOR and other protein kinases results in catalytically inactive enzyme (Bao et al., 2011; Madhusudan et al., 2002; Yang et al., 2013; Brown et al., 1995; Yamashita et al., 2001; Denning et al., 2001). Therefore, the overall architecture of the substrate-bound SMG1 catalytic module corroborates the structural conservation among PIKK active sites and reveals that positioning of the substrate phospho-acceptor is achieved by residues that are shared between a wide range of protein kinases.

![Figure 2.](https://cdn.elifesciences.org/articles/57127/elife-57127-fig2-v2.jpg)

**Figure 2.:** (A) The structure of the entire complex is shown overlayed with transparent reconstructed density. The black box indicates the location of the kinase active site. (B) SMG1 active site with important residues shown as sticks. Activation segment and catalytic loop as indicated; the p-loop was omitted for clarity. UPF1-LSQ is shown in blue with positions of important residues highlighted. (C) Two-dimensional sketch of the SMG1 active site with key kinase-substrate interactions indicated. (D) Activation segment (pink) and catalytic loop (magenta) regions of a SMG1 sequence alignment are shown, indicating a high level of conservation across Homo sapiens, Bos taurus, Mus musculus, Gallus gallus, Xenopus laevis, Danio rerio and Caenorhabditis elegans. Key residues shown in B are highlighted by a black dot and activation segment and catalytic loop are indicated.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/57127/elife-57127-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Superposition of substrate-bound SMG1 active site with substrate-bound CDK2 active site (PDB ID, 3QHW). SMG1 catalytic loop is colored in magenta, SMG1 activation segment is in pink, CDK2 is shown in salmon and the CDK2 substrate peptide is in orange. Directionality of the substrates and important catalytic residues are indicated and colored as described above. P-loops were omitted for clarity. The SMG1 kinase contains features that have previously been associated with a model preferring the presence of a ‘dissociative’ transition state, such as a positive charge closely involved in β-phosphate coordination, namely K2155 (residue not shown) (Wang and Cole, 2014). (B) Superposition of substrate-bound SMG1 active site with nucleotide-bound mTOR active site (PDB ID, 4JSP). SMG1 active site is colored as described in panel A and mTOR is in green. Important active site residues are indicated. P-loops were omitted for clarity. (C) Close-up of the active site hydrophobic cage after superposing the model of the substrate-bound SMG1 active site with Chaetomium thermophilum Tel1ATM (PDB ID, 6SKY). SMG1 active site is colored as described in panel A and CtTel1ATM is colored in light orange. Key residues are indicated. (D) Close-up of the active site hydrophobic cage based on the superposition of SMG1 and mTOR shown in B. Color scheme as in B and important residues are indicated. View is similar to C.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/57127/elife-57127-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Close-up showing how residues of the SMG1 catalytic loop coordinate Ser1078 of UPF1-LSQ. (B) Alignment of catalytic loop sequences from Homo sapiens and Xenopus laevis for all PIKKs colored according to conservation. PIKKs are grouped by phosphorylation site specificity and residues highlighted in subfigure C are indicated by a black dot.

### Crucial recognition of a glutamine residue at +1 position of the UPF1 consensus motif

A glutamine residue following the phospho-acceptor site is the minimal requirement for UPF1 phosphorylation by SMG1 (Figure 3A; Yamashita et al., 2001). To validate the importance of this residue, we performed a mass spectrometry-based phosphorylation assay using a series of peptides based on UPF1-LSQ. We changed the residue at position +1 in the UPF1-LSQ peptide to test the effect of different side chain properties on phosphorylation. Only wildtype UPF1-LSQ was efficiently phosphorylated by SMG1 (Figure 3B and Figure 1—figure supplement 1C). In our structure, the glutamine at position +1 of UPF1-LSQ reaches into a hydrophobic cage formed by the SMG1 activation segment and FATC domain (Figure 3C). In particular, UPF1 Gln1079 stacks against Tyr3654 and Leu2365 and forms hydrogen bonds with the backbone of Val2367 (Figure 3C). The hydrophobic cage is highly conserved in other PIKKs that recognize SQ motifs (ATM, ATR and DNA-PK) but is different in mTOR (where Glu2369 is found at the equivalent position of SMG1 Leu2365) (Figure 3D). This difference is also apparent from the superposition of SMG1 with the 2.8 Å resolution structure of the ATM orthologue Chaetomium thermophilum (Ct) Tel1ATM and with mTOR (Figure 2—figure supplement 1C and D; Jansma et al., 2020; Yang et al., 2013). While the geometry of the hydrophobic cage is highly similar between SMG1 and CtTel1ATM, it deviates in mTOR due to the described Leu to Glu substitution. Indeed, mTOR has been found to prefer small or non-polar residues at position +1 of its phosphorylation consensus motif (Hsu et al., 2011). Taken together, these observations provide a rationale for the difference in phosphorylation site specificity between SMG1, ATM, ATR, DNA-PK and mTOR. Intriguingly, the structural superposition with CtTel1ATM shows that its PIKK regulatory domain (PRD) places a Gln residue in the corresponding hydrophobic cage, effectively occupying the substrate Gln binding site (Figure 2—figure supplement 1C). This explains the autoinhibitory function of the ATM PRD domain (Jansma et al., 2020; Yates et al., 2020). The corresponding PRD domain in SMG1 is a ~ 1100 amino-acid long insertion (Figure 1A) that negatively impacts its kinase activity (Deniaud et al., 2015). However, there is no ordered density for this region in neither the previous apo-structure (Gat et al., 2019) nor in the current substrate-bound structure (Figure 1A and B).

![Figure 3.](https://cdn.elifesciences.org/articles/57127/elife-57127-fig3-v2.jpg)

**Figure 3.:** (A) Sequence logo derived from an alignment of all SQ motifs present in human UPF1 with the respective residue positions indicated. The heights of single letters correspond to the observed frequency at that position and the overall height of a stack of letters indicates the level of conservation (Figure 1—figure supplement 1B and Figure 4—figure supplement 2; Crooks et al., 2004). (B) Mass spectrometry-based phosphorylation assay comprising UPF1-LSQ and the indicated position +1 variations. The peptide sequence is indicated in the upper left with the varied position marked as ‘X’. Error bars representing standard deviations calculated from independent experimental triplicates are shown. (C) Zoom-in of the SMG1 active site showing the recognition of UPF1 position +1 glutamine by SMG1 residues located in the activation segment and FATC domain. Residues of interest are shown as sticks. Colors as in Figure 2. (D) Alignment of PIKK sequences from Homo sapiens and Xenopus laevis with the activation segment and FATC domain sequences shown and colored according to conservation. PIKKs are grouped by phosphorylation site specificity and residues highlighted in subfigure C are indicated by a black dot.

### Preferred recognition of a leucine residue at −1 position of the UPF1 consensus motif

Previous results have indicated that SQ motifs preceded by a hydrophobic residue in position −1 are preferentially phosphorylated by SMG1 (Yamashita et al., 2001). In our model, the Leu residue at position −1 in the substrate forms a C-H⋅⋅⋅π-interaction with SMG1 Phe2215 and is further stabilized by hydrophobic interactions with SMG1 Pro2249 and Gly3656. The binding pocket is also restricted by the catalytic loop residues His2337 and Asp2339 (Figure 4A). To biochemically characterize the importance of position −1, we assayed a peptide library based on UPF1-LSQ, in which we varied the residue in position −1 to represent all those found in the 20 different SQ motifs of human UPF1. Following phosphorylation of the peptides over time, we could observe that SQ motifs carrying a hydrophobic residue in position −1 were more efficiently phosphorylated. Notably, a Leu elicited the highest phosphorylation rate (Figure 4B). An end-point measurement experiment using single peptides confirmed these observations (Figure 4—figure supplement 1). We conclude that a Leu at position −1 is optimal for the interaction with SMG1 at the structural level. This is reflected at the biochemical level, whereby decreasing hydrophobicity of the residue at the −1 position negatively affects phosphorylation efficiency.

![Figure 4.](https://cdn.elifesciences.org/articles/57127/elife-57127-fig4-v2.jpg)

**Figure 4.:** (A) Recognition of position -1 residue of UPF1-LSQ by SMG1. Important residues are shown as sticks and colored as in Figure 2. (B) Mass spectrometry-based phosphorylation assay with UPF1-LSQ and derivatives varied in position -1. The peptide sequence is indicated in the upper left with the varying position marked as “X”. Error bars representing standard deviations calculated from independent experimental triplicates are shown and curves are colored according to hydrophobicity of the position -1 residue (Eisenberg et al., 1984). The most hydrophobic peptides are in blue while non-hydrophobics are in red. (C) Final time points of experiment shown in B. Peptides grouped and colored according to the location of the respective position -1 residue in UPF1 N- or C-terminus. Individual data points are shown as circles and error bars representing standard deviations are indicated. (D) Mass spectrometry-based phosphorylation assay with UPF1 N-terminus phosphorylation site 28 and the indicated position -1 variation. The peptide sequence is shown in the upper left with the varied position marked as “X”. Error bars represent standard deviations resulting from independent experimental triplicates. A tyrosine residue was added to the C-terminal end of the wildtype sequence to increase absorbance at $\lambda$ = 280 nm.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/57127/elife-57127-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Mass spectrometry-based end-point measurements of single peptides combined with a control. Data points corresponding to one experiment are shown in the same color. One preferred (LSQ) and two suboptimal (DSQ, KSQ) motifs were chosen to evaluate how the absence of more optimal, competing motifs affects phosphorylation efficiency toward single peptides. The results indicate that decreased phosphorylation of peptides with non-hydrophobic position −1 residues is not only caused by competition with more optimal substrates (compare assay shown in Figure 4B). A peptide with the sequence QPELDQDSYLG was used as a control in all three experiments. Reactions were quenched and analyzed after 80 min. The peptide sequence is shown with the varied position marked as ‘X’ (B) Mass spectrometry-based phosphorylation assay with UPF1-LSQ and derivatives varying in position +2. The peptide sequence is indicated with the varying position marked as ‘X’. Error bars representing standard deviations calculated from independent experimental triplicates are shown.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/57127/elife-57127-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** The alignment is colored according to conservation. (A) Sequence alignment of UPF1 N-terminus. SQ motifs are highlighted by orange boxes with the phosphorylation site position indicated on top. (B) As in A, but for UPF1 C-terminus and using red color to indicate SQ motifs. Location and range of UPF1-LSQ are indicated.

Interestingly, further analysis of the final time points in the time course phosphorylation experiment showed that the SQ motifs that carry rather hydrophobic residues at the −1 position (and are therefore more efficiently phosphorylated) reside exclusively in the UPF1 C-terminus (Figure 4C, Figure 4—figure supplement 2). To validate our hypothesis on the importance of position −1 hydrophobicity, we turned to a known phosphorylation site in the N-terminus, Thr28. We tested whether SMG1-8-9 phosphorylation activity toward this motif could be enhanced by changing the residue at position −1 from the naturally occurring Asp to a Leu. Indeed, mutating the residue upstream of this SQ motif (Asp27Leu) resulted in a gain-of-function effect in the phosphorylation assay (Figure 4D). These findings are in agreement with data for ATM and ATR (Kim et al., 1999), although the residues involved in the recognition of UPF1 Leu1077 have diverged, suggesting that the details of −1 recognition will differ in other PIKKs. Finally, we do not observe extensive interactions between SMG1 and the peptide residues preceding or following the LSQ motif in our structure. Consistently, we did not detect a marked effect on phosphorylation in a time course experiment where we changed the residue at position +2 of UPF1-LSQ (Figure 4—figure supplement 1B).

### Conclusions

In this manuscript, we report the first structure of a substrate-bound PIKK active site, thereby revealing the basis for phosphorylation site selection by SMG1 and other PIKK family members. The results elucidate the mechanism of phospho-acceptor recognition, and explain the specificity for Ser-containing substrates with a glutamine downstream residue at position +1 and an upstream hydrophobic residue at position −1 (particularly Leu). These findings can be extrapolated to other PIKK members, such as ATM and ATR, and suggest a specific mechanism for PRD function by acting as a pseudosubstrate. Our results provide molecular insights into a key step of the NMD pathway. Whether phosphorylation of full-length UPF1 by SMG1 involves additional elements of recognition and/or additional levels of regulation will be a subject for future studies.

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
      <td>Gene (Homo sapiens)</td>
      <td>SMG1</td>
      <td>Shigeo Ohno lab</td>
      <td>Uniprot Q96Q15</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>SMG8</td>
      <td>Shigeo Ohno lab</td>
      <td>Uniprot Q8ND04</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>SMG9</td>
      <td>Shigeo Ohno lab</td>
      <td>Uniprot Q9H0W8</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>HEK293T</td>
      <td>ATCC</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BL21 Star (DE3) pRARE</td>
      <td>EMBL Heidelberg Core Facility</td>
      <td></td>
      <td>Electrocompetent cells</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>UPF1- LSQ (peptide 1078) and derivatives, UPF1- peptide 28 and derivatives</td>
      <td>in-house as described in the Materials and methods section</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>AMPPNP</td>
      <td>Sigma-Aldrich</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>ATP</td>
      <td>Sigma-Aldrich</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RELION</td>
      <td>doi: 10.7554/eLife.42166</td>
      <td>RELION 3.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cryosparc</td>
      <td>doi: 10.1038/nmeth.4169</td>
      <td>Cryosparc2</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CtfFind</td>
      <td>doi: 10.1016/j.jsb.2015.08.008</td>
      <td>CtfFind4.1.9</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cryosparc</td>
      <td>doi: 10.1038/nmeth.4169</td>
      <td>Cryosparc2</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>UCSF Chimera</td>
      <td>UCSF, https://www.cgl.ucsf.edu/chimera/</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>UCSF ChimeraX</td>
      <td>UCSF, https://www.rbvi.ucsf.edu/chimerax/</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>COOT</td>
      <td>http://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PHENIX</td>
      <td>https://www.phenix-online.org/</td>
      <td>PHENIX 1.17</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PyMOL</td>
      <td>PyMOL Molecular Graphics System, Schrodinger LLC</td>
      <td>PyMOL 2.3.2</td>
      <td>https://www.pymol.org/</td>
    </tr>
  </tbody>
</table>

### Protein expression and purification

The SMG1-SMG8-SMG9 complex was expressed and purified as previously described (Gat et al., 2019). Briefly, a pool of HEK293T cells (obtained from ATCC) stably expressing full length SMG1 (N-terminally fused to a TwinStrep-tag and a 3C protease cleavage site), SMG8 and SMG9 was established using the piggybac method by initially transfecting the cells using polyethylenimine (Yusa et al., 2011; Li et al., 2013). The source cells were authenticated by genotyping (Eurofins) and tested negative for mycoplasma contamination (LookOut Mycoplasma PCR Detection Kit, Sigma-Aldrich). For SMG1-SMG8-SMG9 expression, cultures were adjusted to a density of 1 × 106 cells per mL in FreeStyle 293 Expression Medium (Gibco, Thermo Fisher Scientific). The cells were induced by addition of doxycycline and were harvested 48 hr after induction. After lysis by douncing the cells in 1xPBS, 1 mM MgCl2 and 1 mM DTT supplemented with DNase I, Benzonase and EDTA-free cOmplete Protease Inhibitor Cocktail (Roche) the cleared lysate was applied to a StrepTrap HP column (Sigma-Aldrich) and the complex affinity purified using the N-terminal TwinStrep-tag on SMG1. After washing with 50 column volumes of 1xPBS, 1 mM MgCl2 and 1 mM DTT the complex was eluted using wash buffer supplemented with 2.5 mM desthiobiotin. SMG1-8-9 was further purified by size-exclusion chromatography using a Superose 6 Increase 10/300 GL column (Sigma-Aldrich) equilibrated with 1xPBS, 1 mM MgCl2 and 1 mM DTT (Aekta purifier FPLC system, GE Healthcare). Purified SMG1-8-9 was concentrated up to 6 μM and stored in gel filtration buffer. To obtain full-length unphosphorylated human UPF1, the protein was expressed in Escherichia coli BL21 STAR (DE3) pRARE fused to a C-terminal 6xHis-tag cleavable with Tobacco etch virus (TEV) protease, as described before (Chakrabarti et al., 2011; Chakrabarti et al., 2014). Bacteria were grown at 37°C in TB medium shaking at 180 rpm and induced using IPTG at an OD of 2 for overnight expression at 18°C. Harvested bacteria (6000 rpm, 10 min) were lysed by sonication in lysis buffer (50 mM Tris-Cl pH 7.5, 500 mM NaCl, 10 mM Imidazole, 1 mM β-mercaptoethanol, 10% (v/v) glycerol, 2 mM MgCl2 and 0.2% (v/v) NP-40) supplemented with DNase I and EDTA-free cOmplete Protease Inhibitor Cocktail (Roche). The lysate was cleared by centrifugation (25.000 rpm, 30 min), filtered and combined with TALON resin (Takara) equilibrated with lysis buffer for gravity-flow affinity purification. After washing with 70 column volumes of lysis buffer, the protein was eluted with lysis buffer supplemented with 300 mM imidazole pH 7.5 and the eluate was combined with His-tagged TEV protease and dialyzed overnight against 20 mM HEPES pH 7.5, 85 mM KCl, 1 mM MgCl2, 10% (v/v) glycerol and 2 mM DTT. The dialyzed sample was passed over another TALON column by gravity-flow, in order to separate cleaved protein from the cleaved-off His-tag, the His-tagged TEV protease and uncleaved UPF1 protein. The flow-through of this column contained cleaved UPF1 and was loaded on a HiTrap Heparin HP column (GE Healthcare). Following binding and washing with Heparin buffer A (as for dialysis), UPF1 was eluted by a gradient increasing salt concentration from 85 mM to 500 mM over 50 column volumes (Aekta prime FPLC system, GE Healthcare). The peak corresponding to full-length UPF1 was pooled and concentrated before a final sizing step using a Superdex 200 Increase 10/300 GL column (Sigma-Aldrich) equilibrated with Heparin buffer A (Aekta purifier FPLC system, GE Healthcare). Purified full-length UPF1 was pooled and concentrated up to 30 μM using an Amicon Ultra Centrifugal Filter (50 kDa MWCO, Merck). All described protein purification steps were carried out at 4°C and all purified proteins were flash frozen in size-exclusion buffer using liquid nitrogen and stored at −80°C until further usage.

### Cryo-EM sample preparation and data collection

A sample of 0.5 μM (final concentration) purified SMG1-SMG8-SMG9 was mixed with 0.5 mM of UPF1-LSQ, 1 mM AMPPNP, 2 mM MgCl2, 2 mM DTT and 0.04% (v/v) n-octyl-beta-D-glucoside in 1xPBS and incubated for 30 min on ice. The UPF1-LSQ peptide (sequence: QPELSQDSYLG) was synthesized in-house as described for the mass spectrometry-based phosphorylation assay. A 4 μL sample was applied to a glow-discharged Quantifoil R1.2/1.3, Cu 200 mesh grid and incubated for 30 s at 4°C and approximately 100% humidity. Grids were subsequently plunge frozen directly after blotting using a liquid ethane/propane (37% ethane, temperature range when plunging: −170°C to −180°C) mixture and a ThermoFisher FEI Vitrobot IV set to a blot time of 3.5 s and a blot force of 4. Cryo-EM data were collected using a ThermoFisher FEI Titan Krios microscope operated at 300 kV equipped with a post-column GIF (energy width 20 eV) and a Gatan K3 camera operated in counting mode, the SerialEM software suite, and a beam-tilt based multi-shot acquisition scheme. Movies were recorded at a nominal magnification of 81.000x corresponding to a pixel size of 1.094 Å at the specimen level. The sample was imaged with a total exposure of 68.75 e-/Å2 evenly spread over 5.5 s and 79 frames. The target defocus during data collection ranged between −0.8 and −2.9 μm.

### Cryo-EM data processing

Data processing was carried out using RELION 3.0 (Zivanov et al., 2018) unless stated otherwise. Beam-induced sample motions were corrected and dose-weighting was carried out using the RELION implementation of MotionCor2 (Zheng et al., 2017). Particles were picked using Gautomatch (https://www.mrc-lmb.cam.ac.uk/kzhang/Gautomatch/) and CTF estimation was done using the RELION wrapper for CtfFind4.1 (Rohou and Grigorieff, 2015). After extraction (box size: 320 pix, 1.094 Å/pix) and downsampling (box size: 80 pix, 4.376 Å/pix), 4,368,586 particles were submitted to two rounds of reference-free 2D classification. A subset of the cleaned candidate particles was used to generate an initial model using CryoSPARC v2 (Punjani et al., 2017). 1,524,355 selected particles were 3D classified before re-extracting 886,714 particles with original sampling followed by two additional rounds of 3D classification resulting in 481,754 final particles. All classification steps were carried out with the total amount of particles being distributed over multiple batches. After 3D auto-refinement, sharpening (b-factor = −119.5) and Ctf refinement in RELION 3.0, the final refined map (3D auto-refinement) was again submitted to RELIONs’ post-processing routine for automatic B-factor weighting and high-resolution noise substitution (b-factor = −102.6). The final reconstruction (EMD-11063) reached an overall resolution of 2.9 Å with local resolution ranging from 2.8 Å to 4.5 Å as estimated by RELION 3.0.

### Model building and refinement

The reconstructed density was interpreted using COOT (version 1.0) and our previously published model of SMG1-8-9 (PDB: 6SYT) (Emsley et al., 2010). Model building was iteratively interrupted by real-space refinements using PHENIX (version 1.17) (Adams et al., 2010; Liebschner et al., 2019). Statistics assessing the quality of the final model (PDB ID 6Z3R) were generated using Molprobity (Chen et al., 2010; Supplementary file 1). FSC curves were calculated using PHENIX and the 3D FSC online application (Tan et al., 2017). Images of the calculated density and the built model were prepared using UCSF Chimera (Pettersen et al., 2004), UCSF ChimeraX (Goddard et al., 2018) and PyMOL (version 2.3.2).

### Radioactive in vitro kinase assay

In vitro kinase assays were essentially carried out as before (Gat et al., 2019). 1 μM of full-length UPF1 was mixed with 50 nM SMG1-8-9, 10mM MgCl2 and 2mM DTT in 1xPBS. The reaction was started by adding 0.5mM ATP and 0.06 μM of $\gamma$-32P-labeled ATP. The reaction was incubated at 30°C and samples were taken at different time points to follow phosphorylation over time. The samples were immediately quenched by adding SDS-containing sample buffer and initially analyzed by SDS gel electrophoresis followed by Coomassie-staining. Phosphoproteins were subsequently detected using autoradiography and a Typhoon FLA7000 imager (GE Healthcare).

### Mass spectrometry-based in vitro kinase assay

All peptides were synthesized in-house using solid-phase peptide synthesis and the quality of the product was assessed by electrospray ionization mass spectrometry (ESI MS). For the purpose of this study, peptides were dissolved in 1xPBS supplemented with 500 mM HEPES pH 7.4. Two types of experiments were carried out. Firstly, several peptides (typically comprising a library) and a control were mixed, and their individual phosphorylation ratios were determined at several time points (0, 10, 20, 40 and 80 min). Secondly, one end-point measurement experiment was carried out. In this setup, a single peptide was mixed with a control and the relative phosphorylation ratio was determined at a single, final time point (80 min). This type of experiment was used to assess whether effects on phosphorylation ratios observed in time course assays are caused by competition between several peptides for SMG1 binding. In both cases, 0.5 μM of kinase complex was combined with 0.1 mM of each peptide, 0.5 mM ATP, 20 mM MgCl2 and 2 mM DTT in 1xPBS. The reaction was started by addition of kinase and incubated at 30°C. Samples were taken at desired time points and immediately quenched after collection by adding EDTA to a final concentration of 50 mM on ice.

In order to remove kinase complex and transfer the peptides into a compatible buffer, we made use of home-made StageTips (Rappsilber et al., 2007). Poly(styrenedivinylbenzene)copolymer (SDB-XC) was washed with methanol by centrifugation before being washed again with buffer B (0.1% (v/v) formic acid, 80% (v/v) acetonitrile). Buffer A (0.1% (v/v) formic acid) was used for equilibration of the SDB-XC material. Following sorbent equilibration, the sample was applied and the tips were washed using buffer A. Finally, the sample was eluted using buffer B. Using an Agilent 1290 HPLC, typically about 5 μL of the sample in 70% (v/v) acetonitrile and 0.05% (v/v) trifluoroacetic acid were flow-injected (250 μL/min) into a Bruker maXis II ETD mass spectrometer for ESI MS time-of-flight analysis. Peptides were ionized at a capillary voltage of 4500 V and an end plate offset of 500 V. Full scan MS spectra (200–1600 m/z) were acquired at a spectra rate of 1 Hz and a collision energy of 10 eV. All experiments were carried out as independent experimental triplicates. Raw data files were processed using Bruker Compass DataAnalysis software. The m/z spectra were deconvoluted by maximum entropy with an instrument resolving power of 10,000. The 12C peaks corresponding to individual peptides were identified in the resulting neutral spectra and integrated, both for masses accounting for unphosphorylated and phosphorylated peptides. To calculate a relative phosphorylation ratio, the area for phosphorylated peptide was divided by the sum of phosphorylated and unphosphorylated peptide. All time points were normalized to time point 0. Means of independent experimental triplicates and error bars indicating standard deviations were visualized using Prism (GraphPad).

# The carboxyl-terminal sequence of PUMA binds to both anti-apoptotic proteins and membranes

## Authors

- James M Pemberton<sup>1</sup> ([ORCID: 0000-0001-8386-1081](https://orcid.org/0000-0001-8386-1081))
- Dang Nguyen<sup>1</sup> ([ORCID: 0000-0002-3000-2053](https://orcid.org/0000-0002-3000-2053))
- Elizabeth J Osterlund<sup>2</sup> ([ORCID: 0000-0003-0941-7630](https://orcid.org/0000-0003-0941-7630))
- Wiebke Schormann<sup>2</sup> ([ORCID: 0000-0003-3055-2706](https://orcid.org/0000-0003-3055-2706))
- Justin P Pogmore<sup>2</sup> ([ORCID: 0000-0003-4198-2779](https://orcid.org/0000-0003-4198-2779))
- Nehad Hirmiz<sup>2</sup>
- Brian Leber<sup>5</sup>
- David W Andrews<sup>1</sup> ([ORCID: 0000-0002-9266-7157](https://orcid.org/0000-0002-9266-7157)) †

### Affiliations

1. Department of Medical Biophysics, Faculty of Medicine, University of Toronto Toronto Canada ([ROR:03dbr7087](https://ror.org/03dbr7087))
2. Biological Sciences Platform, Sunnybrook Research Institute Toronto Canada
3. Department of Biochemistry, Faculty of Medicine, University of Toronto Toronto Canada ([ROR:03dbr7087](https://ror.org/03dbr7087))
4. Department of Biomedical Engineering, McMaster University Hamilton Canada ([ROR:02fa3aq29](https://ror.org/02fa3aq29))
5. Department of Medicine, McMaster University Hamilton Canada ([ROR:02fa3aq29](https://ror.org/02fa3aq29))

† Corresponding author

## Abstract

Anti-apoptotic proteins such as BCL-XL promote cell survival by sequestering pro-apoptotic BCL-2 family members, an activity that frequently contributes to tumorigenesis. Thus, the development of small-molecule inhibitors for anti-apoptotic proteins, termed BH3-mimetics, is revolutionizing how we treat cancer. BH3 mimetics kill cells by displacing sequestered pro-apoptotic proteins to initiate tumor-cell death. Recent evidence has demonstrated that in live cells the BH3-only proteins PUMA and BIM resist displacement by BH3-mimetics, while others like tBID do not. Analysis of the molecular mechanism by which PUMA resists BH3-mimetic mediated displacement from full-length anti-apoptotic proteins (BCL-XL, BCL-2, BCL-W, and MCL-1) reveals that both the BH3-motif and a novel binding site within the carboxyl-terminal sequence (CTS) of PUMA contribute to binding. Together these sequences bind to anti-apoptotic proteins, which effectively ‘double-bolt locks’ the proteins to resist BH3-mimetic displacement. The pro-apoptotic protein BIM has also been shown to double-bolt lock to anti-apoptotic proteins however, the novel binding sequence in PUMA is unrelated to that in the CTS of BIM and functions independent of PUMA binding to membranes. Moreover, contrary to previous reports, we find that when exogenously expressed, the CTS of PUMA directs the protein primarily to the endoplasmic reticulum (ER) rather than mitochondria and that residues I175 and P180 within the CTS are required for both ER localization and BH3-mimetic resistance. Understanding how PUMA resists BH3-mimetic displacement will be useful in designing more efficacious small-molecule inhibitors of anti-apoptotic BCL-2 proteins.

## Introduction

Apoptosis, a form of programmed cell death, is an essential physiological process responsible for the elimination and disposal of malignant or excessive cells in multicellular organisms (Fuchs and Steller, 2011). The loss of outer-mitochondrial membrane integrity, known as mitochondrial outer-membrane (MOM) permeabilization (MOMP), is regarded as an irreversible event, resulting in the release of cytochrome c and apoptotic factors from the mitochondria that leads to the activation of caspases and cell death (Kale et al., 2018). MOMP is tightly regulated by BCL-2 protein family proteins, including both pro- and anti-apoptotic regulators that share from one to four homology motifs (BH1 to BH4). BCL-2 and its anti-apoptotic homologs possess all four BH motifs and keep the effector pore-forming multi-BH domain pro-apoptotic proteins, BAX and BAK, from inducing MOMP through direct binary protein-protein interactions (Kale et al., 2018; Bogner et al., 2020). Anti-apoptotic proteins can also prevent MOMP by binding BH3-only proteins, which are pro-apoptotic proteins that share only the BH3 region with other BCL-2 family proteins. The interaction of pro-apoptotic proteins with anti-apoptotic proteins, which is often but not always binary, results in a mutual sequestration that inhibits both proteins. BH3-only ‘activator’ proteins, like BIM and BID, bind to and activate BAX and BAK. BH3-only ‘sensitizer’ proteins, like BAD and HRK, bind to and inhibit anti-apoptotic proteins but do not activate BAX or BAK. Unlike the other BH3-proteins where there is a clear distinction, whether the BH3-protein PUMA functions primarily as an inhibitor of anti-apoptotic proteins (sensitizer) or as an activator of BAX and BAK remains unclear and may depend on the cell type analyzed. Although first identified as a p53 transcriptional target (Yu et al., 2001; Nakano and Vousden, 2001), PUMA has been characterized as a mediator of cell death induced by DNA damage, endoplasmic reticulum (ER) stress and oxidative damage. All these stresses are induced by common chemotherapeutics and ionizing radiation (Jeffers et al., 2003; Jiang et al., 2006) suggesting that PUMA may play a role in chemotherapy responses. As the overexpression of pro-survival BCL-2 proteins is not only a hallmark of cancer progression but also critical for tumor cells to sustain a high proliferative rate and survive genomic instability, apoptosis modulation has been proposed as a therapeutic approach to selectively target cancer cells for elimination (Hanahan and Weinberg, 2011; Delbridge et al., 2016).

The development of small molecule inhibitors that mimic the BH3-motif of pro-apoptotic BCL-2 family proteins and function as competitive inhibitors for BH3-protein binding to anti-apoptotic proteins (BH3-mimetics) is an area of active academic and pharmaceutical research. BH3-mimetics result in the death of cancer cells that depend on anti-apoptotic proteins for survival (Delbridge et al., 2016). Among BH3-mimetics, the selective BCL-2 inhibitor, Venetoclax (ABT-199) is leading advancement to the clinic, and is FDA approved for the treatment of relapsed chronic lymphocytic leukemia and acute myeloid leukemia in patients not fit for standard induction chemotherapy (Delbridge et al., 2016; Roberts et al., 2016). Navitoclax (ABT-263), a BH3-mimetic that inhibits BCL-2, BCL-XL, and BCL-W results in undesirable but manageable on-target thrombocytopenia due to the dependence of platelets on BCL-XL (Tse et al., 2008). Unexpectedly complexes of anti-apoptotic proteins bound to PUMA and BIM, are highly resistant to all known BH3-mimetics (Aranovich et al., 2012; Liu et al., 2019). Resistance can be partly attributed to membrane binding by both the BH3-protein and its anti-apoptotic target increasing the local concentrations and therefore binding interactions (Liu et al., 2019; Pécot et al., 2016). However, we recently demonstrated that in addition to the BH3-sequence, there is a second anti-apoptotic protein binding motif in the carboxyl-terminal sequence (CTS) of BIM (Liu et al., 2019). Together the two binding sequences enable BIM to ‘double-bolt lock’ to anti-apoptotic proteins. The increased avidity that results from two independent binding sequences is presumed to confer resistance to displacement by BH3 mimetics.

Similar to BIM, PUMA is an intrinsically disordered protein containing a BH3 motif important for binding other BCL-2 family proteins and a CTS reported to function as a tail-anchor that integrates the protein in the MOM (Rogers et al., 2014; Wilfling et al., 2012). However, unlike conventional tail-anchor sequences and the CTS of BIM, the CTS of PUMA contains multiple prolines and charged residues, and an unusually short span of hydrophobic amino acids (Borgese et al., 2003; Mehlhorn et al., 2021). Therefore, we investigated whether the unusual CTS of PUMA contributes to resistance to BH3-mimetics. Our results suggest that similar to BIM, PUMA ‘double-bolt locks’ the anti-apoptotic proteins BCL-XL, BCL-2 and BCL-W. Unexpectedly, in multiple cell types, exogenously expressed PUMA is primarily localized at the ER and not the mitochondrial outer membrane (MOM). Furthermore, replacing the PUMA CTS with ER-specific tail-anchor sequences from other proteins resulted in PUMA mutants that bound specifically to ER membranes, retained pro-apoptotic function as a sensitizer binding to anti-apoptotic protein(s) but were not resistant to BH3-mimetics, suggesting that the sequence of the PUMA CTS rather than membrane binding is responsible for BH3-mimetic resistance. Mutagenesis and live cell experiments identified PUMA CTS residues I175 and P180 as required for both ER localization and resistance to BH3-mimetics. Our data indicate that inhibition of both BH3 and CTS binding to anti-apoptotic proteins may be required to mobilize PUMA for the treatment of cancer.

## Results

### The PUMA CTS contributes to BH3-mimetic resistance independent of membranes in vitro

To understand how PUMA resists BH3-mimetic displacement from BCL-XL, full-length recombinant BCL-XL (CAA80661) and full-length PUMA (AAB51243) were purified, and their interaction was measured in vitro using Förster resonance energy transfer (FRET) (Pogmore et al., 2016). Previously, it was shown that PUMA and BCL-XL complexes are highly resistant to BH3-mimetic displacement when bound to membranes (Pécot et al., 2016), and that mutations in the BCL-XL CTS abolished both membrane binding and BH3-mimetic resistance (Pécot et al., 2016). However, PUMA also contains a CTS that binds the protein to membranes (Wilfling et al., 2012; Yee and Vousden, 2008) and it remains unclear whether it contributes to BH3-mimetic resistance (Liu et al., 2019). Therefore, PUMA with a deletion of the last 26 amino acids (PUMA-d26) that encompasses the CTS was also purified. To measure function, purified PUMA protein was added to a 'SMAC-mCherry MOMP assay', as previously described (Chi et al., 2020). In brief, mitochondria were isolated from baby mouse kidney (BMK) cells deficient for Bax and Bak (BMK-dko cells) expressing a fluorescent protein (FP), mCherry, fused to the N-terminal sequence of SMAC (SMAC-mCherry). SMAC-mCherry localizes to the intermembrane space of mitochondria, and is released upon MOMP. Isolated SMAC-mCherry containing mitochondria were reconstituted with recombinant BCL-2 family protein(s), and % SMAC-mCherry release (MOMP) was measured by monitoring SMAC-mCherry fluorescence in the supernatant after pelleting mitochondria, relative to the detergent-induced full permeabilization.

As expected, the addition of each BH3-protein alone was insufficient to induce MOMP as indicated by the low % Smac-mCherry Release (≈20%) (Figure 1A, columns 2,3,9,10). However, the combination of recombinant tBID [4 nM] and BAX [20 nM] was sufficient to induce MOMP at ≈60% release (column 4), which was inhibited by [10 nM] of BCL-XL (column 5). Addition of the BCL-XL inhibitor BAD [50 nM] (column 6), recombinant PUMA (column 7) or PUMA-d26 (column 8) was sufficient to functionally inhibit BCL-XL, thereby inducing SMAC-mCherry release (MOMP) in a BAX-dependent manner (Figure 1A). This confirms that recombinant PUMA and PUMA-d26 function as sensitizers by inhibiting BCL-XL to indirectly activate BAX.

![Figure 1.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig1-v2.jpg)

**Figure 1.:** (A) Left panel, legend indicating the combinations of recombinant proteins incubated with purified mitochondria encapsulating SMAC-mCherry. Right panel, release of SMAC-mCherry from mitochondria by the combination of recombinant proteins indicated by the legend numbers below. Each point represents a single technical replicate. The horizontal bar indicates the average of all three technical replicates per group. A one-way ANOVA and Dunnett’s multiple comparisons test resulted in the indicated p-values. (B–E) Alexa*568 labelled PUMA [5 nM] (black line) or PUMA-d26 [5 nM] (grey line) were incubated with Alexa*647 labelled BCL-XL [40 nM] in the presence of the indicated concentration of the BH3-mimetics (B and C) A-1155463 or (D and E) ABT-263. Each graph includes datapoints from three independent replicates. Total data were fit to a one phase exponential decay (grey and black lines as indicated). (B,D) Incubations of contained mitochondrial-like liposomes (0.2 mg/mL). (C,E) Solution indicates incubations that did not contain liposomes.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Transient transfection of HEK293, HCT116 and BMK cell lines to express exogenous BH3-only protein: BIM, PUMA, BIMdCTS, PUMAdCTS as well as PUMA-4E in which the 4 key hydrophobic residues in the BH3 motif of PUMA were changed to glutamic acid to disrupt the pro-apoptotic function of PUMA (I137E, L141E, M144E, and L148E). Cell death was scored using Annexin V staining to quantify cells that were both Venus and Annexin V positive out of the total Venus-positive cell population. (B) Two-way titration of two BH3-mimetics S63845 (MCL-1 inhibitor) and ABT-263 (BCL-XL, BCL-2, and BCL-W inhibitor) confirmed that HEK293 cells cannot be killed by inhibiting anti-apoptotic proteins (are unprimed) whereas BMK and HCT116 cells are primed for apoptosis and were killed by both BH3-mimetics. Annexin V positivity was scored as in (A) for cells that were incubated overnight with the indicated concentrations of S63845 and ABT-263. Results are displayed in a heatmap colored as indicated in the scale at the left, the values within each square indicate the average % Annexin V positive (dead cells) from three independent biological replicates.

We next tested PUMA pro-apoptotic function in live cells by transient transfection of HEK293, Baby mouse kidney (BMK) and HCT116 cell lines and assessed cell death in the transfected cells by Annexin V staining (Figure 1—figure supplement 1A). Here we use a Venus-fused to the N-terminus of the BH3-only protein BIM (VBim) or PUMA (VPUMA) to identify the transfected cells expressing the BH3-proteins by fluorescence intensity. As we previously published (Chi et al., 2020), HEK293 cell lines are unprimed and can only be killed efficiently by an activator protein such as BIM (60% Annexin V positive), whereas PUMA and the previously established sensitizer-only BIM mutant (BIM-dCTS) did not induce cell death in HEK293. On the other hand, BIM, PUMA and PUMA-d26 killed BMK and HCT116, which are primed cells that can be killed by a sensitizer protein (Chi et al., 2020). Similar to sensitizer proteins, BH3-mimetics are designed to target anti-apoptotic proteins and do not activate BAX or BAK. Thus, we used a combination of two BH3-mimetics S63845 (MCL-1 inhibitor) and ABT-263 (BCL-XL, BCL-2, and BCL-W inhibitor) to validate the apoptotic priming of these stable cell lines by doing a two-way titration of the two drugs (Figure 1—figure supplement 1B). Upon BH3-mimetics treatment, activator proteins and/or active BAX/BAK are displaced from the antiapoptotic proteins in the primed cells resulting in cell death. The combination of these drugs at 10 µM resulted in 47% and 73% Annexin V positivity in HCT116 and BMK, respectively, but did not increase Annexin V positivity in HEK293, confirming that HEK293 is the only unprimed cell line among the three. Taken together, the data show that PUMA acts as a sensitizer and that its CTS is not required for sensitizer function, as truncated PUMA without its CTS can still bind to and inhibit BCL-XL.

Binding of recombinant Alexafluor 647 (A*647) labeled BCL-XL to Alexafluor 568 (A*568) PUMA and PUMA-d26 was measured directly by FRET in the presence of liposomes with a phospholipid composition similar to that of mitochondria (Figure 1B–E). In the absence of BH3-mimetics, (indicated as Concentration, 0 nM) the FRET efficiency was ~40% between the donor PUMA*A568 and the acceptor BCL-XL*A647. The addition of the selective BCL-XL BH3-mimetic, A-1155463, did not result in a significant decrease in FRET efficiency, demonstrating that binding of PUMA*A568 to BCL-XL*A647 remains unchanged (Figure 1B, black line). A FRET efficiency of ~40% was also measured with the same concentrations of PUMA-d26*A568 incubated with BCL-XL*A647, indicating similar protein binding (Figure 1B, grey line). However, the addition of low concentrations of A-1155463 reduced FRET efficiency to less than 10%, demonstrating BH3-mimetic mediated displacement of PUMA-d26*A568 from BCL-XL*A647 (Figure 1B). Thus, removing the PUMA CTS increases PUMA susceptibility to BH3-mimetic displacement from BCL-XL.

When the same experiment was performed in solution, full length PUMA*A568 was more resistant to BH3-mimetic displacement than PUMA-d26*A568 suggesting that the CTS of PUMA contributes to BH3-mimetic resistance by binding to BCL-XL even in the absence of membranes (Figure 1C). To corroborate the result the experiment was repeated using the less potent but better studied BCL-XL inhibitor ABT-263. In the presence of liposomes, both PUMA*A568 and PUMA-d26*A568 resisted displacement from BCL-XL*A647 by ABT-263 (Tao et al., 2014; Figure 1D) but in solution, PUMA-d26*A568 was displaced from BCL-XL*A647 (Figure 1E), consistent with the CTS of PUMA contributing to BH3-mimetic resistance by binding to BCL-XL independent of binding PUMA to membranes.

### The PUMA CTS contributes to BH3-mimetic resistance in live cells

To determine if our findings with purified proteins replicate what occurs in live cells, we used quantitative fast fluorescence lifetime imaging microscopy – Förster resonance energy transfer (qF3) to measure PUMA binding to anti-apoptotic proteins (Osterlund et al., 2022). For these measurements, the donor fluorescent protein mCerulean3 was stably expressed as a fusion to the N-terminus of the indicated anti-apoptotic protein in BMK-dko cells in which the Bax and Bak genes are deleted. The acceptor protein of the FRET pair - Venus (V) fused to the N-terminus of PUMA (VPUMA) was expressed in the cells by transient transfection. Four hours later the media was exchanged to add the indicated BH3-mimetic or DMSO as a solvent control. Twenty hr later, the cells were analyzed by qF3. To assess the effect of mutations in PUMA on binding to the anti-apoptotic proteins, BMK-dko cell lines expressing either CBCL-XL, CBCL-2, or CBCL-W were transfected with plasmids encoding variants of VPUMA as previously described (Pemberton et al., 2019). In these assays, binding of both VPUMA and VPUMA-d26 to CBCL-XL, CBCL-2 and CBCL-W was established with approximately equal apparent dissociation constants (6–9 μM) by ensuring that in the cell images analyzed the expression level of the donor exceeded the absolute dissociation constant (Figure 2A, DMSO lanes) (Osterlund et al., 2022). In these experiments, the non-binding mutants with a 4E mutation within the BH3 motif (BH3-4E) of VPUMA and VPUMA-d26 were used to control for collisions as opposed to binding interactions (Figure 2A, bottom panel of heatmap).

![Figure 2.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig2-v2.jpg)

**Figure 2.:** Quantitative Fast FLIM-FRET (qF3) was used to measure binding of PUMA and PUMA-d26 to the anti-apoptotic proteins: CBCL-XL, CBCL-W, and CBCL-2 in live BMK-dko cells. (A) Calculated apparent dissociation constants (Kd’s) for VPUMA and VPUMA-d26 binding to the indicated anti-apoptotic proteins are presented in a heatmap according to the scale at the right, with the calculated values specified inside the heatmap cells. VPUMA-d26 was displaced from CBCL-XL by all of the mimetics, as indicated by the increased apparent Kd in response to addition of BH3-mimetic. The protein pairs are indicated to the left and at the top. Final drug concentrations added to cells are indicated at the left. DMSO is the solvent control. BH3-4E below the panels indicates mutation of the BH3 protein listed at the top. Data is averages of three independent biological replicates. (B) Representative qF3 micrographs of BMK-dko cells stably expressing CBCL-XL, and transiently transfected with the plasmid to express VPUMA. Regions of interest identified automatically (ROI Selection) were assigned arbitrary colors to permit visualization. The FLIM image indicates the subcellular localization of VPUMA- CBCL-XL protein complexes (red, decreased mCerulean3 fluorescence lifetime) compared to unbound CBCL-XL (blue). (C–E) The effect of BH3 mimetics on the binding of PUMA-d26V to the anti-apoptotic proteins indicated above the graphs as measured by qF3. Binding data (Δω,from phasor plots)at different concentrations of unbound PUMA-d26V (means, symbols; error bars, SE) was fit to a Hill equation. Data points are averages from independent experiments. Line was fit to the data points from all three independent experiments. Lines with shaded areas indicate 90% confidence interval for the best fit. The results demonstrate displacement in (C) from BCL-XL, but not in (D) from BCL-W and to an intermediate extent in (E) from BCL-2 when incubated with the drugs indicated by the legend. DMSO is the solvent control and BH3-4E indicates the non-binding PUMA-d26V mutant used to control for collisions.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Binding curves generated from qF3 data demonstrate that both VPUMA and VPUMA-d26 bind to CBCL-XL, CBCL-2, and CBCL-W (blue lines) in a BH3-dependent manner as the corresponding BH3-4E mutant has dramatically reduced Δω values best fit with a straight-line indicating collisions rather than binding (grey lines). Addition of the specific BCL-XL inhibitor, A-1331852, only marginally affected Δω for VPUMA binding with CBCL-XL (left column, third panel down, compare blue and red lines) but reduced Δω for VPUMA-d26 (left column, sixth panel down) to a straight-line indicating addition of A-1331852 reduced binding of VPUMA-d26 with CBCL-XL to primarily collisions. For BCL-W at low concentrations of free VPUMA and VPUMA-d26 the data do not fit well to a Hill equation with a Hill slope of 1 suggesting binding of PUMA to BCL-W may be more complicated than a simple binary interaction. Data points are averages from independent experiments. The line was fit to the data points from the 3 independent experiments. Shaded areas indicate the 95% confidence interval for the best fit of the Hill equation to the data. In all Figures, where the lines overlapped completely only the red shaded area is visible as typically the 95% confidence interval is at least as great as for assays without the BH3 mimetic.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Increased Δω translates to a larger dynamic range in assaying protein binding. Data points are averages from independent experiments. Line was fit to the data points from the 3 independent experiments. Shaded areas indicate the 95% confidence interval for the best fit of the Hill equation with a Hill slope of 1 to the data.

Regions of interest (ROIs) in the qF3 images were identified automatically and fluorescence lifetimes were calculated as previously (Osterlund et al., 2022). The decrease in the 3.8ns fluorescence lifetime in CBCL-XL expressing cells (blue) to less than 3.4 ns in cells expressing VPUMA is indicative of a binding interaction (Figure 2B, red cells). However, to clearly differentiate binding from collisions that can occur at high frequency for colocalized proteins it is necessary to demonstrate that the qF3 data can be better fit to Hill equation than to a straight line. For this purpose, values that are directly related to the fraction of donor molecules in the bound state, the fractional change in angular frequency (Δω) obtained from polar plots of the data, were plotted as a function of the concentrations of the unbound donor (Free Venus) and fit to a Hill equation to enable calculating apparent dissociation constants for each binding curve (Osterlund et al., 2022).

Addition of the dual BCL-2/BCL-XL inhibitors ABT-263 [30 μM], AZD-4320 [20 μM] or a newer BCL-XL inhibitor related to A-1155463, A-1331852 [2.5 μM] caused increases in the apparent dissociation constants that were more pronounced for VPUMA-d26 than for VPUMA binding to CBCL-XL (Figure 2A). This result demonstrates that these BH3-mimetics displaced truncated PUMA (PUMA-d26), to a much greater extent than full-length PUMA. The most dramatic change in apparent Kd was for A-1331852 which severely reduced the affinity for VPUMA-d26 binding to CBCL-XL resulting in an apparent Kd increase from ~9 to~37 μM. In contrast, measurements of the effect of the same inhibitor on binding of full-length VPUMA to CBCL-XL revealed much less but detectable displacement (the apparent Kd increased from ~6 to~13 μM) (Figure 2A). Consistent with these results, in live cells, A-1331852 is more selective and more potent than either AZD-4320 or ABT-263 (Osterlund et al., 2022).

The inhibitors ABT-263 and AZD-4320 are BH3-mimetics reported to target BCL-XL, BCL-2 and BCL-W (Tse et al., 2008; Leverson et al., 2015) and BCL-XL and BCL-2, (Leverson et al., 2015) respectively. When these drugs were used to probe PUMA binding to BCL-2, surprisingly ABT-263 had no effect and AZD-4320 only partially reduced the binding of VPUMA-d26 with CBCL-2, indicating that deletion of the PUMA CTS alone is not sufficient to make PUMA susceptible to displacement from BCL-2 (Figure 2—figure supplement 1). None of the inhibitors reduced binding of VPUMA-d26 to BCL-W (Figure 2—figure supplement 1), however that might be due to poor binding of the inhibitors to the anti-apoptotic protein rather than to the binding affinity of PUMA for BCL-W (Osterlund et al., 2022).

Unexpectedly, fusing Venus to the C-terminus of PUMA (PUMAV) resulted in a higher FRET efficiency with anti-apoptotic proteins (indicated by the increase in Δω), likely due to increased proximity between the donor and acceptor fluorescence proteins in the complex and inconsistent with the PUMA CTS spanning a membrane (Figure 2—figure supplement 2). A larger change in Δω results in a greater dynamic range in the assay and therefore the possibility of detecting smaller changes in binding. Both PUMAV and PUMA-d26V bound to anti-apoptotic proteins in a BH3-dependent manner (Figure 2—figure supplement 2). Similar to the results obtained above, when binding to CBCL-XL was measured, PUMAV resisted BH3-mimetic displacement, while PUMA-d26V was displaced (Figure 2C-E, Figure 3). Indeed, binding was reduced to the point where the change in Δω did not return to the level seen for the bound state even at 45 μM free PUMAV (Figure 2C, blue line). Similar to the results with Venus fused to the amino terminus, none of the mimetics displaced PUMA-d26V from BCL-W (Figure 2D) consistent with relatively poor binding of the mimetics to BCL-W. However, for BCL-2 visual inspection of the binding curves revealed that the mimetics, particularly AZD-4320, partially displaced PUMA-d26V (Figure 2E). Taken together our data indicate that the PUMA CTS contributes to PUMA binding to BCL-XL and BCL-2 in live cells.

![Figure 3.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig3-v2.jpg)

**Figure 3.:** (A) Linear depictions of the PUMAV mutants analyzed. Lock 1 indicates the BH3-motif, Lock 2 indicates the CTS. (B) Mutation of either the PUMA CTS or the BH3 region is sufficient to relieve resistance to a subset of the drugs resulting in apparent Kd values similar to those obtained for the BH3 mimetic sensitive control VtBID. Mutation of both sequences in PUMA results in a protein (PUMA(BID-BH3)-d26V) that can be displaced by the BH3 mimetic AZD-4320 from the three anti-apoptotic proteins, CBCL-XL, CBCL-2, and CBCL-W. Heatmaps displaying Kd values calculated from fitting qF3 binding curves and represented by color (scale to the right) to highlight changes in these binding affinities (binding (blue) to non-binding (red)) within the heatmap cells. The interacting protein pairs are indicated to the left and at the top. Final drug concentrations added are indicated at the left. DMSO is the solvent control. BH3-4E below the panels indicates mutation of the BH3 protein listed at the top. Binding by the BH3-mimetic sensitive control VtBID to the anti-apoptotic proteins was inhibited by the cognate BH3-mimetics, as expected. In the assay conditions used, inhibition of VtBID indicated that BCL-XL was inhibited primarily by AZD-4320 and A-1331852; BCL-2 was inhibited by ABT-263 and AZD-4320; CBCL-W was inhibited by only AZD-4320. Data is averages from three independent experiments.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Binding curves generated from qF3 data demonstrate that both VPUMA and VPUMA-d26 bind to CBCL-XL, CBCL-2, and CBCL-W (blue lines) in a BH3-dependent manner as binding of the corresponding BH3-4E mutant was dramatically reduced resulting in lower Δω values that are best fit with a straight-line, indicating collisions rather than binding (grey lines). VPUMA binding with CBCL-XL was slightly reduced by the specific BCL-XL inhibitor, A-1331852, (left column, third panel down, compare blue and red lines). Reduced binding of VPUMA-d26 (Δω, left column, sixth panel down) resulted in data best fit to a straight-line indicating only collisions were detected. Binding between VPUMA-d26 and CBCL-2 was disrupted by AZD-4320, while no BH3-mimetic disrupted the interaction between VPUMA-d26 and CBCL-W. Moreover, at low concentrations of free VPUMA and VPUMA-d26 the data do not fit well to a Hill equation suggesting binding of PUMA to BCL-W may be more complicated than simple 1:1 binding described by a Hill equation. Data points are averages from independent experiments. Line was fit to the data points from the three independent experiments. Shaded areas indicate the 95% confidence interval for the best fit of the data to a Hill equation.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Addition of the specific BCL-XL inhibitor, A-1331852, reduced Δω for both VPUMA(BID-BH3) and VPUMA(BID-BH3)-d26 binding to CBCL-XL (left column, third and sixth panel down, compare blue and red lines). Addition of ABT-263 and AZD-4320 displaced VPUMA(BID-BH3)-d26 from CBCL-XL and CBCL-2 (left and middle columns, fourth and fifth panels down). Only AZD-4320 reduced binding of VPUMA(BID-BH3)-d26 to CBCL-W (right column, fifth panel down). Moreover, for BCL-W and low concentrations of free VPUMA(BID-BH3) and VPUMA(BID-BH3)-d26 the data do not fit well to a Hill equation suggesting binding of PUMA to BCL-W may be more complicated. Data points are averages from independent experiments. Line was fit to the data points from the three independent experiments. Shaded areas indicate the 95% confidence interval for the best fit of the Hill equation to the data.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** The addition of A-1331852 and AZD-4320 reduced the affinity of VtBID binding to CBCL-XL (Left column, second and third panels down, compare blue and red lines) while AZD-4320 and ABT-263 reduced the binding affinity for VtBID binding with CBCL-2 (middle column, first and second panels down). VtBID binding with CBCL-W was disrupted by AZD-4320 (right column, second panel down). Data points are averages from independent experiments. Line was fit to the data points from the three independent experiments. Shaded areas indicate the 95% confidence interval for the best fit of the Hill equation with a slope of 1 to the data.

### In cells PUMA resists BH3-mimetic displacement by double-bolt locking to BCL-2 family anti-apoptotic proteins

The resistance of PUMA to displacement from anti-apoptotic proteins by BH3-mimetics is similar to recently published results for the BH3-protein BIM (Aranovich et al., 2012; Liu et al., 2019; Pécot et al., 2016) yet the CTS of PUMA is very different than the CTS of BIM. To determine whether PUMA is also ‘double-bolt locked’ to anti-apoptotic proteins by the BH3-motif and CTS we constructed new mutants of PUMA. These mutants have the BH3-motif mutated (Lock 1), the CTS deleted (Lock 2), or both (Lock 1 and 2) mutated (Figure 3A). To disable the PUMA BH3 region sufficiently to measure the importance of the CTS separately but without abolishing the interaction entirely we replaced PUMA (residues 133–151) with the BH3 region from the protein BID. Unlike PUMA, BID is a pro-apoptotic BH3-protein that is easily displaced from anti-apoptotic proteins by BH3-mimetics (Aranovich et al., 2012; Pécot et al., 2016). The resulting protein, PUMA(BID-BH3)V has a compromised BH3-motif, but an intact CTS (Figure 3A). To disable both Lock 1 and 2 the CTS was deleted from PUMA(BID-BH3)V. The resulting mutant, PUMA(BID-BH3)-d26V, has a compromised BH3-motif and is missing the PUMA CTS (Figure 3A).

Constructs encoding these proteins were transfected into BMK-dko cells expressing one of CBCL-XL, CBCL-2 or CBCL-W, and after ~20 hr, binding interactions at equilibrium in live cells were measured by qF3. In the DMSO controls, PUMAV bound with Kds of ~4–6 μM to all three anti-apoptotic proteins while the mutants bound with Kds of ~5–10 μM (Figure 3B). As expected, addition of BH3-mimetic did not increase the dissociation constants for PUMAV substantially, although there was detectable inhibition of BCL-XL by A-1331852 and BCL-2 by AZD-4320 (Figure 3B). Also as anticipated, deletion of the PUMA CTS (PUMA-d26V) resulted in increased BH3-mimetic mediated displacement from BCL-XL, but not for BCL-2 and BCL-W as reported above (compare Figure 2A and Figure 3B). As a positive control for BH3-mimetic mediated displacement, we included Venus fused to the N-terminus of truncated BID (VtBID). This protein was displaced from CBCL-XL, CBCL-2 and CBCL-W by the cognate BH3-mimetic to a similar extent as PUMA-d26V (Figure 3B, far-right column). Replacing the BH3 region of PUMA with that of BID (PUMA(BID-BH3)V) was sufficient to result displacement similar to that of VtBID from CBCL-XL with the inhibitor A-1331852 and from BCL-2 with AZD-4320. However, in some cases, PUMA(BID-BH3)V was more resistant than VtBID to displacement by the cognate BH3-mimetics (e.g. CBCL-2 with ABT-263 and CBCL-W with AZD-4320). In contrast, resistance to displacement from CBCL-XL and CBCL-2 was abolished by mutation of Lock 1 and Lock 2 (PUMA(BID-BH3)-d26V). While resistance to AZD-4320 was reduced for PUMA(BID-BH3)-d26V for binding to CBCL-W the apparent Kd remained substantially lower than for VtBID. Overall, these data suggest that both the PUMA BH3 and CTS regions contribute to the high affinity interaction of PUMA with anti-apoptotic proteins, and that the primary mechanism of resistance to BH3-mimetics is a ‘double-bolt lock’, similar to BIM (Liu et al., 2019).

### The CTS of PUMA localizes the protein to the endoplasmic reticulum

The data above demonstrate a previously unrecognized function of the PUMA CTS in double-bolt locking to BCL-XL and BCL-2 and that PUMA-BCL-XL complexes can form in the absence of membranes. Although, BCL-XL is found in both the cytoplasm and bound to intracellular membranes, previous reports suggest that PUMA is localized in a CTS dependent manner primarily to mitochondria (Yu et al., 2001; Nakano and Vousden, 2001; Wilfling et al., 2012; Yee and Vousden, 2008). However, in these reports, localization was interpreted by visual inspection and was not rigorously analyzed. To our surprise, although the spatial resolution of FLIM-FRET images is limited, VPUMA-CBCL-XL complexes in FLIM-FRET images were not obviously localized only at mitochondria (Figure 2B). This could be due to complexes forming and remaining cytoplasmic; however, previous reports suggest that binding to membranes increases the stability of the complexes and contributes to the resistance we observed to displacement by BH3 mimetics (Pécot et al., 2016). Therefore, we re-examined PUMA localization using confocal microscopy and created mutants to identify the CTS residues that mediate binding to subcellular membranes.

To assign the localization of PUMA in live cells using an unbiased quantitative approach we made use of a previously described random forests classifier built from a reference library of 789,011 optically validated landmark-based localization images (Schormann et al., 2020). Briefly, NMuMG (normal murine mammary gland) cells were infected with lentivirus to express a fusion protein consisting of EGFP fused to the N-terminus of a BH3-4E mutant PUMA to visualize the fusion protein (EGFPPUMA-4E) without it binding to anti-apoptotic proteins or killing the cells. Using automated-confocal microscopy, 2225 images of individual cells expressing EGFPPUMA-4E were classified as the landmark from the reference library they most resemble. To our surprise, 55% of EGFPPUMA-4E cell micrographs were classified as most similar to one of the resident endoplasmic reticulum (ER) markers (blue bars), indicating ER localization (Figure 4A). In contrast, smaller fractions of the cells were classified as patterns resembling that of a protein that recycles between the ER and Golgi (Calr-KDEL) or that is resident at mitochondria (MAO, monoamine oxidase). For images of other cells classification was to one of a variety of other locations particularly transport vesicles, a phenomenon not uncommon for over-expressed proteins (Schormann et al., 2020). As a positive control for correct classification of an ER localized EGFP-fused BH3-protein, we infected NMuMG cells with lentivirus to express EGFPBIK-L61G a mutant of the tail-anchored ER protein BIK containing the BH3 mutation L61G previously shown to abrogate apoptotic activity (Mathai et al., 2002). As expected, 79% of the images of EGFPBIK-L61G expressing cells were classified as showing ER localization (yellow bars) compared to 55% for EGFPPUMA-4E (Figure 4A).

![Figure 4.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig4-v2.jpg)

**Figure 4.:** (A) Lentiviral infected NMuMG cells expressing EGFP fused BH3-proteins with mutated BH3-motifs to prevent cell death, were imaged using confocal fluorescence microscopy. Images of individual cells were classified as one of the previously defined landmarks as described in Schormann et al., 2020. Most cells expressing EGFPPUMA-4E (blue) or the ER localized control EGFPBIK-L61G (yellow) were classified as most closely resembling ER landmarks with a small fraction of cells expressing EGFPPUMA-4E resembling localization in a variety of transport vesicles (RAB5A, RAB7A) or secretory pathway vesicles and plasma membrane (VAMP5). The landmarks tested included ER (3 resident endoplasmic reticulum membrane markers), Calr-KDEL (recycling between ER and Golgi), ERGIC (ER-Golgi intermediate compartment), GalT (trans-Golgi), Golgin84 (cis-Golgi), MAO (outer mitochondrial membrane), CCO (inner mitochondrial membrane), MAM (mitochondrial associated ER membrane), Rab5A, Rab7A, VAMP2 (transport and secretory vesicles), VAMP5 (Secretory pathway to the plasma membrane), ΔTMD-VAMP1 (cytoplasm), Lamin A (nuclear envelope), PTS1 (peroxisomes), LAMP1 (Lysosomes) (Schormann et al., 2020). (B) Quantification of fluorescence colocalization in BMK-dko cells indicates PUMA primarily localizes in a CTS-dependent manner to the ER (upper panel) and not Mitochondria (lower panel). Pearson’s correlation coefficients from three independent experiments are reported for the indicated proteins with the ER marker BODIPY FL thapsigargin (upper panel) or the mitochondrial marker Mitotracker Red (mRed, lower panel). The horizontal bars indicate the medians and mGreen indicates the stain Mitotracker Green. CBIK is an ER marker composed of mCerulean3 fused to the ER localized protein BIK. Data from three independent experiments are shown with horizontal bars indicating the medians. Each data point represents the average from a minimum of 50 cells. (C) Fusion of Venus to the C-terminus of PUMA (PUMAV) does not prevent localization at the ER, suggesting that the PUMA CTS is not a conventional TA that spans the bilayer. Top row: Micrographs of the Venus fluorescence from cells expressing VPUMA, VPUMA-d26, and PUMAV by transient transfection, as indicated above. Middle row: Micrographs of the ER marker. Bottom row: MitoTracker Red staining for the same cells. White scale bar is 5 μm. (D) Quantification of the extent to which the distribution of the various mutant proteins (indicated below) correlated with the distribution of the ER marker (cBIK) in BMK-dko cells. Data from three independent experiments are shown with horizontal bars indicating the medians. Each data point represents the average from a minimum of 50 cells.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Pearson’s correlation coefficients from three independent experiments are reported for the proteins indicated at the bottom with the ER marker CBIK (left panel) or the mitochondrial marker Mitotracker Red (mRed, right panel). The horizontal bars indicate the means.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Images of mCerulean3 and mCherry in MCF-7 cells expressing donor CBCL-XL and either ChActA or ChCb5(indicated above), with corresponding segmentation maps selected based on each channel below. ROIs obtained by segmentation of the total cell CBCL-XL (mCerulean3 signal) and ROIs identified from organelle marker-based segmentation maps are shown below the corresponding images. (B) FLIM–FRET binding curves for VPUMA binding to CBCL-XL were generated from ROIs identified from images of MCF-7 cells by organelle marker-based segmentation as indicated above each panel (n=3).

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A) Fluorescence images of MCF-7 cells expressing either mCherry-ActA (ChActA) (Top panels) or mCherry-Cb5 (ChCb5) (Bottom panels) were fixed and immunostained for PUMA (A488). Cells were treated with the drugs and concentrations indicated at the top of the panels for 24 hr before fixation and immunostaining. DMSO treated control cells were labeled as 0 µM drug. (B) Drug treatment increased the level of endogenous PUMA as shown by immunostaining in MCF-7 cells. Fluorescence intensity of Alexa-488 conjugated to the secondary antibody that recognizes the anti-PUMA (human) primary antibody were reported for individual cells and plotted as a box and whisker plot. ETOP, Etoposide; TN, Tunicamycin; TG, Thapsigargin. (C) Table containing Pearson correlation coefficient values from confocal micrographs for co-localization of endogenous PUMA with either ChActA for mitochondria or ChCb5 for ER in MCF-7 cells treated with the indicated concentrations of Thapsigargin or Tunicamycin or Etoposide. Three technical replicates (a, b, c and d, e, f) are represented as rows in the table. The values are color-coded to show the modest drug treatment induced increase in Pearson correlation coefficient from ≈0.4 to ≈0.5 for the co-localization of PUMA to the ER marker and from ≈0.6 to ≈0.7 for the co-localization of PUMA to mitochondria marker. The increase is largest at the highest concentration of the drugs compared to the baseline at 0 µM or 0 µg/mL.

As an orthogonal approach to examine localization in the BMK-dko cell line used for FLIM-FRET experiments, co-localization with ER and mitochondrial markers was examined by calculating Pearson’s correlation coefficients. Because it lacks both BAX and BAK, the BMK-dko cell line will not undergo apoptosis in response to expression of PUMA or BIK. Therefore, inactivating mutations that might affect localization are not required. To calculate correlation values between PUMA and landmarks for two locations in the same cell, the fluorescent protein mCerulean3 was fused to the N-terminus of PUMA (CPUMA). The ER membrane and mitochondria were visualized using the dyes BODIPY FL thapsigargin (green) and MitoTracker Red, respectively. Individual cells were identified using far red nuclear stain DRAQ5. Images of cells were obtained by automated confocal microscopy (Opera Phenix, PerkinElmer) and analyzed with Harmony software (V4.9). To assess localization to the ER membrane, Pearson’s correlation coefficients were calculated between BODIPY FL thapsigargin and mCerulean3 fluorescence intensity for each cell. As seen in Figure 4B, the expression of the negative control mCerulean3 alone resulted in a median coefficient close to zero, indicating no correlation. The positive control for ER localization, mCerulean3 fused to the N-terminus of BIK (CBIK), resulted in a median coefficient close to 0.75, suggesting this value represents localization at the ER membrane. Both CPUMA and CPUMA-4E have Pearson’s coefficient values with BODIPY FL thapsigargin of ~0.6 similar to what was seen for CBIK. In contrast, the Pearson’s correlation coefficient for CPUMA-d26 with BODIPY FL thapsigargin was similar to the negative control (Figure 4B) suggesting CPUMA-d26 is located in the cytoplasm. Overall, this data indicates that exogenously expressed PUMA localizes to the ER in a BH3-independent, CTS-dependent manner.

The same approach was used to assess protein localization at the mitochondria. As expected, the Pearson’s correlation coefficients calculated between mCerulean3 alone and MitoTracker Red resulted in a median coefficient close to zero, indicating no correlation. As a positive control for perfect mitochondrial localization, the calculated median coefficient between the dyes MitoTracker Green and MitoTracker Red was close to 0.85 (Figure 4B). As expected, the median Pearson’s coefficient for the ER localized control CBIK with MitoTracker Red was only slightly higher than the cytoplasmic control mCerulean3 alone. The Pearson’s correlation coefficients for both CPUMA and CPUMA-4E with MitoTracker Red were less than 0.2, much lower than those calculated for these proteins with the ER marker BIK (Figure 3B, compare the bottom and top panels), but slightly higher than values obtained for the cytoplasmic protein mCerulean3. Indeed, the Pearson’s correlation coefficients for CPUMA and CPUMA-4E with MitoTracker Red were similar to the values obtained for the ER marker CBIK and MitoTracker Red. Consistent with these observations, the Pearson’s correlation coefficients for CPUMA-d26 (lacking the CTS) and mCerulean3 with mitochondria were both close to zero (Figure 4B, lower panel). Finally, images of CBCL-XL, a protein known to be both cytoplasmic and localized to multiple membranes resulted in intermediate Pearson’s correlation coefficients. Together, this data suggests that when exogenously expressed the PUMA CTS localizes the protein primarily to the ER.

To further dissect the PUMA CTS and identify the region responsible for directing PUMA localization additional mutants were generated. Incremental deletions of the PUMA CTS decreased the Pearson’s correlation coefficient of the mutant proteins with ER localization suggesting that deleting as few as the last 11 amino acids (VPUMA-d11) impacts ER localization (Figure 4D). As progressive deletion of the CTS correlated with decreasing ER localization, this suggests that the entire CTS contributes to PUMA localization. Unexpectedly, the fusion protein with Venus at the C-terminus of PUMA (PUMAV) retained ER localization (Figure 4C and D), suggesting that unlike CTS of BIK which fully inserts into the ER (Wilfling et al., 2012) the CTS of PUMA is not a conventional tail-anchor that spans the membrane bilayer. This conclusion is also congruent with the data indicating that the PUMA CTS sequence is too short to span the ER membrane.

Our data showed that exogenously expressed PUMA mostly localizes to the ER while BCL-XL localized to both mitochondria and ER (Figure 4B; Osterlund et al., 2022; Kaufmann et al., 2003; Osterlund et al., 2023). Despite this, in BMK cells, PUMA bound to BCL-XL with an apparent Kd of 5.5 µM (Figure 2). To further investigate the subcellular localization of PUMA:BCL-XL heterodimers, FLIM-FRET experiments with VPUMA were done using MCF-7 cells stably expressing CBCL-XL and as a localization marker, mCherry fused to the tail anchor sequence of ActA (ChActA) or of Cytochrome-b5 (ChCb5). This enables the differentiation of the mitochondrial (ChActA) and ER (ChCb5) subcellular regions within the cells where VPUMA could interact with CBCL-XL facilitating localization of complexes. The mCherry channel was used to generate a mitochondrial or ER ‘mask’ and select ROIs for which the mCerulean3 fluorescence lifetime and % FRET were calculated. The plateau observed for the data indicate that both PUMA and PUMA-d26 bind to BCL-XL at both the ER and the mitochondria. In contrast, the FLIM data for the BH3-4E negative controls (VPUMA-4E and VPUMA-d26-4E) can be fit to a straight-line, indicating collisions (Figure 4—figure supplement 2B). The simplest explanation for exogenously expressed VPUMA binding to BCL-XL at mitochondria is that BH3-dependent binding of PUMA to mitochondrial localized BCL-XL results in localization of VPUMA at or close to mitochondria. Supporting this hypothesis, immunofluorescence staining in MCF-7 cells for endogenous PUMA which is expressed at levels more similar to that of BCL-XL and BCL-2 in these cells (Antony et al., 2012; Mukherjee et al., 2015) revealed that endogenous PUMA co-localized more with the mitochondrial landmark (ChActA) (Pearson correlation coefficient ≈ 0.6) than the ER landmark (ChCb5) (Pearson correlation coefficient ≈ 0.4; Figure 4—figure supplement 3C, column 4, 8, and 12).

Given the relatively lower co-localization of endogenous PUMA to the ER marker in MCF-7 cells, we examined localization of endogenous PUMA after the induction of PUMA expression by ER stress (Reimertz et al., 2003; Yu and Zhang, 2008) or genotoxic stress (Meyerkord et al., 2008; Jamil et al., 2015). Previous results suggest that a P53-dependent response to genotoxic stress results in the extension of peripheral tubular ER and promotes the formation of ER-mitochondrial contact sites (Wang et al., 2007) which may be binding sites for PUMA. Therefore, to test this hypothesis, immunofluorescence staining for endogenous PUMA was done in ChActA (mitochondria marker) or ChCb5 expressing (ER marker) MCF-7 cells treated with Thapsigargin (TG) or Tunicamycin (TN) to induce ER stress and Etoposide (ETOP) to induce genotoxic stress (Figure 4—figure supplement 3A). As expected, we observed an increase in the intensity of the Alexa-488 immunofluorescence signal for PUMA in cells treated with the drugs compared to the DMSO-treated cells (Figure 4—figure supplement 3B). Intriguingly, we saw an increase in Pearson correlation coefficients for PUMA to both the ER and the mitochondria, most notably at the highest concentrations of the 3 drugs (Figure 4—figure supplement 3C). As genotoxic stressors can also induce expression of the anti-apoptotic BCL-XL (Jamil et al., 2015) which is both ER and mitochondria-localized (Figure 4B), we speculate that binding to BCL-XL contributes to increased localization of PUMA with the mitochondrial marker ChActA. Moreover, stress induced changes in ER structure and increased MAMs would also result in apparent localization at mitochondria. Taken together, these data suggest that PUMA subcellular localization in living cells is dynamic and dependent not only on the inherent specificity of the PUMA CTS but also on the abundance and localization of its binding partners. This phenomenon has been observed with another BH3-only protein, BIK whereby the predominantly-ER localized BIK can localized to the mitochondria in BMK-dko upon expression of a mitochondria-localized BCL-XL mutant (Osterlund et al., 2023).

### Restoring ER localization to PUMA-d26 does not result in BH3-mimetic resistance

Together the data in Figures 1—3 demonstrate that the CTS of PUMA is required for the protein to resist BH3-mimetic-mediated displacement from BCL-XL in vitro and in live cells. For purified proteins resistance to BH3-mimetic displacement is independent of binding of the proteins to membranes. However, it remains possible that in live cells, PUMA-d26 no longer resists BH3-mimetic displacement because the protein no longer binds subcellular membranes. To test this hypothesis, we constructed two mutants in which the CTS of PUMA was replaced by the tail-anchor sequences of the two proteins used as ER localized controls: BIK (VPUMA-d26-ER1) or cytochrome b5 (CB5) (VPUMA-d26-ER2) (Figure 5A, Figure 5—figure supplement 1A).

![Figure 5.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig5-v2.jpg)

**Figure 5.:** (A) Cartoon depiction of fusion proteins created. (B,C) Fusion of the canonical tail-anchors from BIK and CB5 to VPUMA-d26 restored ER localization when expressed in BMK-dko cells. (B) Pearson’s correlation with the ER marker protein CBIK in BMK-dko cells. Data points are averages from independent experiments. A one-way ANOVA and Dunnett’s multiple comparisons test were used to calculate the indicated p-values. (C) Micrographs illustrating subcellular localization by confocal microscopy of the indicated Venus fusion proteins co-expressed with the ER marker protein CBIK. The scale bar indicates 5 μm. (D) Heatmaps generated from qF3 data display calculated apparent Kd’s for binding of the indicated mutants to CBCL-XL and CMCL-1 in live BMK-dko cells. Restoring ER localization to PUMA-d26 (VPUMA-d26-ER1 and VPUMA-d26-ER2) did not restore resistance to BH3-mimetic displacement as indicated by increased dissociation constants in the presence of BH3-mimetic.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Single letter amino-acid code depiction of the PUMA CTS and the canonical tail-anchors (BIK CTS and CB5 CTS) fused to PUMA-d26. Color depicts amino acid chemical properties (yellow = hydrophobic, purple = helix breaking residue, blue = positively charged, green = negatively charged). One construct (VPUMA-d26-ER1) has the BIK CTS sequence (amino acids 126–160, uniprot: Q13323) and the other (VPUMA-d26-ER2) the CB5 CTS sequence (amino acids 97–132 uniprot: P00167). (B) Fusion proteins VPUMA-d26-ER1 and VPUMA-d26-ER2 are functional as expression kills BMK-wt cells in a BH3-dependent manner as shown by lack of cell death due to expression of proteins containing the 4E mutation. Cell death was measured by Annexin V staining of BMK-wt cells scored by automated confocal microscopy.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** The addition of ABT-263 or A-1331852 (red lines) is sufficient to displace VPUMA-d26, VPUMA-d26-ER1, and VPUMA-d26-ER2 but not VPUMA. As expected, ABT-263 was less effective than A-13311852. Data points are averages from independent experiments. Line was fit to the data points from the three independent experiments.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** The addition of AZD-4320 (red lines) is sufficient to displace VPUMA-d26, VPUMA-d26-ER1, and VPUMA-d26-ER2 but not VPUMA. Data points are averages from independent experiments. Line was fit to the data points from the three independent experiments.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig5-figsupp4-v2.jpg)

**Figure 5—figure supplement 4.:** The maximum values of ∆ω are lower for CMCL-1 due to the increased distance between the fluorescence proteins that results from the extended amino terminus of MCL-1. The addition of either S63845 or S64315 (red lines) resulted in a slight decrease in ∆ω and a change in the shape of the curve that results in a higher calculated Kd in drug treated cells for VPUMA-d26-ER1 (middle column) and VPUMA-d26-ER2 (right column) binding to CMCL-1 in comparison to VPUMA binding to CMCL-1 (Left column), indicating protein displacement. Data points are averages from independent experiments. Line was fit to the data points from the 3 independent experiments.

To determine if these fusion proteins correctly localize to the ER, they were expressed by transient transfection of the corresponding constructs into BMK-dko cells stably expressing CBIK as an ER localization marker (labelled as ER Marker in Figure 5C). The cells were stained with the nuclear dye DRAQ5, imaged by automated confocal microscopy and co-localization was assessed using Pearson’s correlation coefficients, as described above. Both VPUMA-d26-ER1 and VPUMA-d26-ER2 generated Pearson’s correlation coefficients with the ER localization marker that were substantially greater than those for either VPUMA-d26 or Venus alone with the same ER marker (Figure 5B and C). In addition to correct localization, exogenous expression of both fusion proteins induced apoptosis in BMK-wt cells, in a BH3-dependent manner, as measured by Annexin V positivity using confocal microscopy (Figure 5—figure supplement 1B). Given that the fusion proteins are both functional and correctly localized at ER membranes, we used qF3 to measure binding with CBCL-XL in live cells. As seen in Figure 5C, both VPUMA-d26-ER1 and VPUMA-d26-ER2 bound to CBCL-XL (DMSO column) in a BH3-dependent manner in BMK-dko cells. However, neither complex was resistant to displacement by the addition of ABT-263, A-1331852 or AZD-4320. Addition of any of these drugs resulted in significantly higher dissociation constants for binding to CBCL-XL for VPUMA-d26-ER1 and VPUMA-d26-ER2 compared to VPUMA. In addition to binding to CBCL-XL, VPUMA, VPUMA-d26-ER1 and VPUMA-d26-ER2 also bound to CMCL-1 in live BMK-dko cells. Similar to the results obtained for binding to CBCL-XL, the addition of MCL-1 specific BH3-mimetics; S63845 and S64315, resulted in higher dissociation constants for binding to MCL-1 by both mutant proteins compared to VPUMA (Figure 5C). However, these data also demonstrate that the MCL-1 inhibitors only partially displaced VPUMA-d26-ER1 and VPUMA-d26-ER2 compared to mutation of the PUMA BH3 sequence. Thus, similar to BCL-2 and BCL-W the BH3 sequence of PUMA is sufficient to confer partial resistance of binding to MCL-1 to the drugs.

Thus, these data indicate that reintroducing ER membrane localization to VPUMA-d26 does not restore resistance to BH3-mimetic displacement, suggesting that specific residues or sequences within the PUMA CTS contribute to BH3-mimetic resistance.

### Residues I175 and P180 in the PUMA CTS contribute to both ER localization and BH3-mimetic resistance

Data with the CTS substitutions above indicated that localization at the ER is not sufficient to confer resistance to BH3 mimetics. Thus, we sought to identify which regions and residues within the CTS of PUMA are required to confer resistance to BH3 mimetics and if such regions/residues are also required for membrane binding. To this end, mutants were generated containing serial deletions of the PUMA CTS sequence. These mutants were then used to measure binding to membranes and to CBCL-XL in live cells using qF3. Deletion of the last 11 residues (VPUMA-d11) had no effect on localization, binding to BCL-XL or resistance of the complex to BH3-mimetic inhibition (apparent Kd’s: DMSO = 6 μM, plus 2.5 mM A-1331852=14 μM) (Figure 6A–C). Deletion of the last 20 residues (VPUMA-d20) negatively impacted localization (Figure 4D) and substantially altered binding (∆ω). However, the data still resemble a binding curve and although there is substantial noise at low free Venus concentrations where there was no clear change in resistance to addition of BH3-mimetic (apparent Kd’s: DMSO = 2 μM, plus 2.5 mM A-1331852=13 μM) (Figure 6B). The observed change in ∆ω could be due to a conformational change in the protein that increased the distance or altered the dipole orientations between the FRET donor (CBCL-XL) and acceptor (VPUMA-d20) rather than a change in binding affinity. In contrast, deletion of the last 26 amino acids of PUMA (VPUMA-d26) eliminated both ER localization and BH3 mimetic resistant binding to CBCL-XL (apparent Kd’s: DMSO = 8 μM, plus 2.5 mM A-1331852=38 μM). Therefore, the residues between VPUMA-d11 and VPUMA-d20 affect localization and ∆ω, but the effect on BH3 mimetic resistance is less certain. Moreover, this region of the PUMA CTS is the most hydrophobic and contains two proline residues which are unusual for a membrane binding region. Therefore, to probe this region of the protein, nine mutants of PUMAV were generated in which individual residues were replaced with glutamic acid (E). Although replacement with E is a non-conservative mutation, for the DMSO controls similar dissociation constants were measured for all the mutants of PUMAV for binding to CBCL-XL (Figure 6C). Therefore, none of the mutations abolished binding of PUMA to BCL-XL. Addition of the potent BCL-XL inhibitor A-1331852 resulted in an increase in the apparent Kd’s for all the mutants. However, for I175E and P180E, the Kd’s increased substantially, indicating displacement from BCL-XL equivalent to that observed for PUMA-d26V (Figure 6C).

![Figure 6.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig6-v2.jpg)

**Figure 6.:** (A) Amino acid composition of the PUMA CTS. Color depicts amino acid chemical properties (yellow = hydrophobic, purple = alpha-helix breaking residue, blue = positively charged, green = negatively charged). Lines indicate deletion points. Residue numbers are indicated below the sequence. (B) Binding curves generated by qF3 for the indicated mutants. VPUMA and VPUMA-d11 resisted BH3-mimetic displacement from BCL-XL while VPUMA-d26 was displaced (higher Kd value). VPUMA-d20 binding was at least altered such that the distance between the donor and acceptor was increased, as shown by the dramatically reduced values for ∆ω,a measure directly related to FRET efficiency and bound fraction. (C) Calculated Kd values determined by qF3 for PUMAV mutants containing a single-glutamic acid substitution in the PUMA CTS displayed as a heat map with calculated values in the heatmap cells. Averages from 3 biological replicates are shown and suggest that residues I175 and P180 are required for resistance to BH3-mimetics. The color scale was changed for this figure to visually differentiate the effect of the point mutations I175E and P180E from the change in binding that resulted from substituting residues at other locations with a glutamic acid residue. (D) Pearson’s correlation coefficients calculated from confocal micrographs for co-localization of PUMAV and the indicated PUMAV mutants with the ER localization marker CBIK suggest that residues I175 and P180 are most important for PUMA localization at the ER. (E) Pearson’s correlation coefficients calculated from confocal micrographs for co-localization indicate a more conservative mutation to alanine at position I175 (PUMAV I175A) results in increased localization to the ER, while PUMAV P180A was not localized at membranes. (F) Mutation of residues I175 and P180 abrogated resistance to displacement by the BH3-mimetic A1331852 equivalent to deletion of the entire CTS. % Resistance to displacement of PUMAV mutants (indicated below) from CBCL-XL calculated from FLIM-FRET binding curves. Data points are averages from independent experiments. Line indicates the mean of the data points shown. P values in panels (D,E,F) were calculated using an ordinary one-way ANOVA method GraphPad Prism 9.5.0 to examine the differences in the mean Pearson Correlation Coefficient values between the tested group and the reference groups (PUMAV for panels D and E, PUMA-d26V for panel F).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** The addition of BH3-mimetic A-1331852 (red points) most effectively displaced PUMA-d26V and PUMAV mutant I175E. Data from 4 independent experiments (data points) were fit to a Hill equation (lines) with shaded areas representing the 95% confidence interval for the best fit.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** The addition of BH3-mimetic A-1331852 (red points) displaced PUMAV mutants from CBCL-XL but was most effective for PUMAV mutant P180E. Data from 4 independent experiments (data points) were fit to a Hill equation with a slope of 1 (lines) with shaded areas representing the 95% confidence interval for the best fit.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/88329/elife-88329-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** Proteins were expressed by transient transfection. White scale bar indicates 5 μm. Note cytoplasmic expression pattern for the PUMAV mutants I175E, P180E, P180A and the double mutant I715A, P180A.

Visual inspection supported by Pearson’s correlation coefficients revealed that PUMAV mutants I175E and P180E were not localized to membranes but were located primarily in the cytoplasm (Figure 6D and Figure 6—figure supplement 3). In contrast, and consistent with the effects seen on binding to CBCL-XL, the other point mutations reduced PUMA localization at ER to a similar minor extent (Figure 6D). Therefore, in live cells residues I175 and P180 in the PUMA CTS appear to be required for both binding to membranes and resisting BH3-mimetic displacement. For the mutations with minor effects, there is also a correlation between membrane binding and BH3-mimetic resistance.

Substitution of amino acids in the PUMA CTS with negatively charged E residues are more likely to influence PUMA binding to membranes than more conservative substitutions such as alanine. Therefore, to determine if more conservative mutations would separate membrane binding from resistance to BH3-mimetic, additional PUMAV mutants I175A and P180A were analyzed for binding to CBCL-XL by FLIM-FRET and for localization by Pearson’s correlation with an ER marker in live BMK-dko cells. PUMAV mutant P180A appeared cytoplasmic, and resulted in a Pearson’s coefficient with the ER-localized control that was similar to that of the Venus cytoplasmic control (Figure 6E and Figure 6—figure supplement 3). This indicates residue P180 is required for PUMA binding to membranes in live cells. In contrast, mutant I175A appears membrane localized upon visual inspection, and generated a calculated Pearson’s coefficient with the ER-localized control that was higher than that of either PUMAV I175E or Venus (Figure 6E and Figure 6—figure supplement 3), but that was lower than the correlation between the ER-localized control and wildtype PUMAV (Figure 6E).

To compare the extent to which these mutants resist BH3-mimetic displacement from BCL-XL in live cells, FLIM-FRET measurements were made and % Resistance was calculated as previously described Liu et al., 2019; Pemberton et al., 2019. Briefly, the FLIM-FRET efficiency at the acceptor/donor ratio of two was calculated from the fitted Hill-slope equation for expression of the proteins alone and in the presence of the BH3-mimetic, and the change in these values was used to calculate the % Resistance (ie the % of complexes that remain intact). Therefore, a low % Resistance is indicative of protein displacement by BH3-mimetic treatment. In the presence of 2.5 μM A-1331852, PUMAV has a high calculated % Resistance (~90%), while PUMA-d26V has a lower % Resistance (~50%) (Figure 6F). PUMAV mutants I175E, I175A, P180E and P180A all have low % Resistance values similar to PUMA-d26V, suggesting that all of the mutant PUMAV proteins were displaced from BCL-XL similarly to PUMA-d26V. Even PUMAV I175A that localized partially to the ER (P=0.04) did not resist displacement (Figure 6E–F). Overall, this data suggests that PUMA CTS residues I175 and P180 are required for both PUMAV binding to membranes and for resisting BH3-mimetic induced displacement from CBCL-XL.

## Discussion

The availability of small-molecule inhibitors for anti-apoptotic proteins has generated new insights into the mechanisms underlying programmed cell death in a number of cell types, and has positively impacted the treatment of cancer (Delbridge et al., 2016). The development of the first true BH3-mimetic, ABT-737, was based on the structure of the BH3 sequence of BAD bound to BCL-XL and efficacy defined by displacement of BAD BH3-peptides from truncated BCL-XL in solution (Oltersdorf et al., 2005). The other BH3-mimetics currently under pharmaceutical development were all derived based on the structures of BH3-peptides and their corresponding binding sites in the different anti-apoptotic proteins. However, other factors that contribute to BCL-2 family interactions have been discovered. For instance, the MOM and the ER membrane act as both the platform and an active participant in BCL-2 family interactions (Pécot et al., 2016; Lovell et al., 2008; Bleicken et al., 2017). Not surprisingly, full-length proteins have different affinities than truncated proteins binding to BH3 peptides (Kale et al., 2018). This is most dramatically shown for the BH3 protein BIM binding to BCL-XL (Liu et al., 2019; Chi et al., 2020). Studies with truncated protein and BH3 peptides showed binding affinities in the micromolar to millimolar range while studies with full length proteins in the presence of membranes revealed a nanomolar affinity between BIM and BCL-XL (see also Figure 1). In the latter studies, both BH3 regions and the CTS previously thought exclusively involved in binding of BIM to membranes were discovered to contribute to BIM function. Moreover, both the BH3 sequence and the CTS are required for BIM to bind BCL-XL, forming a “double-bolt lock”, in a manner that is resistant to inhibition by BH3-mimetics (Liu et al., 2019).

Collectively the data presented here demonstrate that like BIM, the PUMA CTS functions in binding the protein to membranes and together with the BH3 sequence is required for BH3-mimetic resistant binding to anti-apoptotic proteins. However, unlike BIM, the CTS of PUMA localizes primarily at ER instead of mitochondria (Figure 4) and together with the PUMA BH3 region results in almost complete resistance to all currently known BH3 mimetics (Figure 5D). Endogenous PUMA was observed predominantly at mitochondria in MCF-7 cells (Figure 4—figure supplement 3), suggesting other factors besides the CTS may influence PUMA localization, such as the presence of PUMA-binding partners including the anti-apoptotic protein BCL-XL at both the ER and mitochondria (Figure 4B and Figure 4—figure supplement 2).

Unexpectedly, when analyzed using purified proteins the CTS of PUMA conferred resistance to BH3 mimetics in the absence of membranes, demonstrating that inhibition of anti-apoptotic proteins by PUMA does not require binding to membranes (Figure 1) and suggesting the PUMA CTS binds to BCL-XL. Furthermore, when the PUMA CTS sequence was replaced with classical tail-anchor sequences from each of two other proteins, the mutant proteins were localized at the ER in live cells but remained sensitive to displacement from BCL-XL by BH3 mimetics (Figure 5). Thus, we conclude that membrane binding is not sufficient for the PUMA CTS to confer resistance to displacement from BCL-XL by BH3 mimetics. Instead binding of both the BH3 region and CTS of PUMA to BCL-XL increases both the affinity and avidity of the interaction.

To our surprise delineating the specific residues involved in resistance to BH3 mimetics and localization of PUMA at membranes by mutagenesis revealed that residues I175 and P180 are required for both localization and resistance to BH3-mimetics. This suggests that, at least in live cells, binding to membranes and resistance to BH3-mimetics may not be separable. This is very different from the CTS of BIM in which separate regions of the CTS are involved in binding BIM to mitochondria and binding it to BCL-XL (Liu et al., 2019). It remains to be determined how residues I175 and P180 are involved in PUMA binding to both membranes and anti-apoptotic proteins. We speculate that for P180E or P180A mutation, the diminished membrane binding and resistance to BH3-mimetic displacement might be due to disruption of the structure of the PUMA CTS. As the CTS sequence contains 4 prolines in the last 14 amino acids and there are 6 prolines in the last 30 amino acids of PUMA the structure of this region is expected to be very unlike other tail-anchor sequences that localize proteins at the ER or mitochondria (Figure 5—figure supplement 1).

Unexpectedly, we find using two different quantitative approaches that the PUMA CTS localizes the protein primarily to the ER, and not the MOM as previously claimed (Wilfling et al., 2012). Random forest image classification is an unbiased approach to assess the localization of EGFPPUMA-4E in live NMuMG cells (Figure 4A). A caveat of this approach is that it assumes that the 4E mutation that disrupts the BH3 region and abrogated pro-apoptotic function has no effect on PUMA subcellular localization. Therefore, since binding to anti-apoptotic proteins such as BCL-XL and MCL-1 requires an intact BH3 region, localization due to binding these proteins would not be observed using EGFPPUMA-4E. For this reason, we also calculated Pearson’s Correlation values for the overlap between exogenously expressed CPUMA or VPUMA, with ER membrane and mitochondrial markers in live BMK-dko cells (Figure 4B, C and D). Moreover, fusion of the PUMA CTS (residues 167–193 of PUMA) to the carboxyl-terminus of the fluorescent protein Venus (VPUMA-CTS) and expression of this mutant in BMK-dko cells results primarily in ER localization (Figure 4—figure supplement 1), indicating that the CTS of PUMA alone is sufficient to direct ER localization. Although we have shown that PUMA with an N-terminal fluorescence protein for visualization is functional as a sensitizer and can activate BAX or BAK indirectly to kill cells, it remains possible that the absence of available pro-apoptotic protein binding partners (BAX and BAK) may alter PUMA localization. Nevertheless, taken together the two approaches provide strong evidence that in epithelial cells, in the absence of cellular stress, the majority of exogenously expressed PUMA is located at the ER. In contrast, endogenous PUMA was located primarily at mitochondria and when expression increased in response to stress agonists, PUMA localization was increased at both ER and mitochondria. We speculate that the localization of PUMA may be determined by the availability and localization of anti-apoptotic binding partners such as BCL-XL. It is also possible that the protein localizes at ER-mitochondrial contact sites similar to the BH3-protein BIK (Osterlund et al., 2023) or that localization at the ER may be required for a non-apoptotic function of the protein, sometimes referred to as a ‘day job’.

Our data demonstrate that PUMA residues I175 and P180 are required for BH3-mimetic resistance of PUMAV binding to CBCL-XL. However, in the absence of a BH3-mimetic, the entire CTS region is dispensable for binding of the two proteins as shown by binding of PUMA-d26V to CBCL-XL (Figure 6C). In contrast, disabling the BH3 region of PUMAV (BH3-4E mutation) resulted in no binding to anti-apoptotic proteins (Figure 6—figure supplement 1). This may suggest that a conformational change in either PUMA or the anti-apoptotic proteins that results from binding of the PUMA BH3 sequence increases the affinity of the interaction with the PUMA CTS. Further delineation of the molecular mechanism may require high resolution structure determination. Nevertheless, our data using purified proteins clearly demonstrate that high affinity binding of PUMA conferred by the CTS occurs in solution and strongly suggests direct binding of the PUMA CTS to BCL-XL is distinct from the BH3-binding site. Thus, PUMA CTS binding would increase both the affinity and avidity of the interaction via a mechanism that does not require PUMA binding to membranes (Figure 1). That BH3-mimetic resistant binding requires only PUMA and CBCL-XL in solution suggests that future structural studies may be possible.

Finally, our demonstration that PUMA-d26 binding to BCL-2 is more resistant to inhibition by BCL-2 specific BH3-mimetics suggests that the BH3 sequence of PUMA makes unique contacts with BCL-2 not seen with other BH3-proteins. Only when the BH3-motif is changed to a susceptible one (BID-BH3) and the CTS is deleted (PUMA(BID-BH3)-d26V) can BH3-mimetic treatment fully inhibit PUMA binding to BCL-2 (Figure 3B). Thus, it may be possible to design BH3-mimetics selective for inhibition of PUMA binding to specific anti-apoptotic proteins. PUMA(BID-BH3)V that contains the BH3-mimetic displaceable BH3 sequence and the PUMA CTS was more resistant than VtBID, to displacement by the cognate BH3-mimetics (e.g. CBCL-2 with ABT-263 and CBCL-W with AZD-4320). Together these results suggest a role for the PUMA CTS in binding to anti-apoptotic proteins that depends on BH3 sequence binding but is independent of the specific BH3 sequence. We speculate that binding of a BH3 sequence may lead to a conformational change in the anti-apoptotic protein that facilitates binding of the PUMA CTS. Finally, the unique amino acid sequence of the PUMA CTS argues that generating an efficient specific inhibitor of PUMA binding to anti-apoptotic proteins may require inhibiting binding of both the PUMA BH3-motif and its CTS.

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
      <td>Antibody</td>
      <td>Antibody to PUMA (polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat. #: 4976 S; RRID: AB_2064551</td>
      <td>Dilution (1:400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa-488 anti-Rabbit IgG secondary antibody (polyclonal)</td>
      <td>Abcam</td>
      <td>Cat: # ab150077; RRID: AB_2630356</td>
      <td>Dilution (1:1000)</td>
    </tr>
    <tr>
      <td>Cell line (M. musculus)</td>
      <td>Baby Mouse Kidney (BMK)- WT</td>
      <td>PMID:11836241</td>
      <td></td>
      <td>Dr. Eileen White (Rutgers University)</td>
    </tr>
    <tr>
      <td>Cell line (M. musculus)</td>
      <td>Baby Mouse Kidney (BMK)- DKO</td>
      <td>PMID:11836241</td>
      <td></td>
      <td>Dr. Eileen White (Rutgers University)</td>
    </tr>
    <tr>
      <td>Cell line (M. musculus)</td>
      <td>NMuMG</td>
      <td></td>
      <td>RRID: CVCL_0075</td>
      <td>Dr. Jeff Wrana (University of Toronto)</td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>HEK293</td>
      <td>Other (Graham et al., 1977)</td>
      <td>RRID: CVCL_0045</td>
      <td>Provided by Dr. Frank Graham (McMaster University).</td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>HCT-116</td>
      <td>Other (Polyak et al., 1996)</td>
      <td>RRID: CVCL_0291</td>
      <td>Provided by Dr. Bert Vogelstein (John Hopkins University).</td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>MCF-7</td>
      <td>PMID:3790748</td>
      <td>RRID: CVCL_0031</td>
      <td>Provided by Dr. Ronald N. Buick (University of Toronto)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DRAQ5</td>
      <td>ThermoFisher Scientific, Molecular probes</td>
      <td>Cat. #62251</td>
      <td>Far red nucleic acid specific fluorescent dye for cell imaging</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>MitoTracker Red</td>
      <td>ThermoFisher Scientific, Molecular probes</td>
      <td>Cat. #: M22425</td>
      <td>Mitochodria specific fluorescent dye</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>BODIPY FL thapsigargin</td>
      <td>MedChemExpress</td>
      <td>Cat. #: HY-D1608</td>
      <td>ER specific fluorescent dye</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Alexa 647-maleimide</td>
      <td>ThermoFisher Scientific, Molecular probes</td>
      <td>Cat. #: A20347</td>
      <td>Thiol reactive fluorescent dye</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Alexa568-maleimide</td>
      <td>ThermoFisher Scientific, Molecular probes</td>
      <td>Cat. #. A20341</td>
      <td>Thiol reactive fluorescent dye</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>PC (L-α-phosphatidylcholine)</td>
      <td>Avanti Polar Lipids</td>
      <td>Cat. #:840051 C</td>
      <td>for making liposomes, used 48% PC</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DOPS (1,2-dioleoyl-sn-glycero-3-phospho-L-serine)</td>
      <td>Avanti Polar Lipids</td>
      <td>Cat. #: 840035 C</td>
      <td>for making liposomes, used 10% DOPS</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>PI (L-α-phosphatidylinositol)</td>
      <td>Avanti Polar Lipids</td>
      <td>Cat. #:840042 C</td>
      <td>for making liposomes, used 10% PI</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>PE (L-α-phosphatidylethanolamine)</td>
      <td>Avanti Polar Lipids</td>
      <td>Cat. #: 841118 C</td>
      <td>for making liposomes, used 28% PE</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TOCL, (18:1 Cardiolipin)</td>
      <td>Avanti Polar Lipids</td>
      <td>Cat. #: 710335 C</td>
      <td>for making liposomes, used 4% TOCL</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>A-1331852</td>
      <td>Chemietek</td>
      <td>Cat. #: CT-A115</td>
      <td>in DMSO</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>S-63845</td>
      <td>Chemietek</td>
      <td>Cat. #: 1799633-27-4</td>
      <td>in DMSO</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>S-64315 also named “MIK665”</td>
      <td>ChemieTek</td>
      <td>Cat. # CT-MIK665</td>
      <td>in DMSO</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Navitoclax; ABT-263</td>
      <td>Selleckchem</td>
      <td>Cat. #: S1001</td>
      <td>in DMSO</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>AZD4320</td>
      <td>ChemieTek</td>
      <td>Cat. #: CT-A4320</td>
      <td>in DMSO</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Thapsigargin</td>
      <td>Sigma-Aldrich</td>
      <td>Cat. #:T9033</td>
      <td>in DMSO</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Etoposide</td>
      <td>Sigma-Aldrich</td>
      <td>Cat. #: 33419-42-0</td>
      <td>in DMSO</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tunicamycin</td>
      <td>Sigma-Aldrich</td>
      <td>Cat. #: T7765</td>
      <td>in DMSO</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TransIT-X2</td>
      <td>Mirus</td>
      <td>Cat. #: Mir 6003</td>
      <td>Transfection reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Cell Carrier-384, Ultra</td>
      <td>PerkinElmer</td>
      <td>Cat. #: 6057300</td>
      <td>for live cell imaging</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Non-binding surface, 96-well plate, black with clear bottom</td>
      <td>Corning</td>
      <td>Cat. #: 3881</td>
      <td>For recombinant protein and liposome assays critical to use non-binding plate</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Opera Phenix</td>
      <td>PerkinElmer</td>
      <td>Cat. #: HH14000000</td>
      <td>Automated spinning disc confocal microscope</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>INO-FHS microscope</td>
      <td>PMID:35442739</td>
      <td></td>
      <td>Custom built by INO for Dr. David Andrews' lab</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>The Infinite M1000</td>
      <td>Tecan</td>
      <td></td>
      <td>Platereader for in vitro assays with recombinant proteins and liposome assays</td>
    </tr>
    <tr>
      <td>Gene (H. sapiens)</td>
      <td>Bax</td>
      <td>PMID:14522999,</td>
      <td>GI: L22473.1</td>
      <td>For recombinant protein</td>
    </tr>
    <tr>
      <td>Gene (H. sapiens)</td>
      <td>Bcl-XL</td>
      <td>PMID:18547146</td>
      <td>GI: Z23115.1</td>
      <td>For recombinant protein</td>
    </tr>
    <tr>
      <td>Gene (H. sapiens)</td>
      <td>PUMA</td>
      <td>PMID:35442739</td>
      <td>GI: 27113Addgene plasmid# 166739</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. musculus)</td>
      <td>BimL</td>
      <td>PMID:30860026</td>
      <td>GI: AAD26594.1</td>
      <td>For recombinant BimL purification</td>
    </tr>
    <tr>
      <td>Gene (M. musculus)</td>
      <td>tBid</td>
      <td>PMID:22464442</td>
      <td>GI: NM_007544.4</td>
      <td>for expression of VtBid in cells</td>
    </tr>
    <tr>
      <td>Gene (M. musculus)</td>
      <td>Bid</td>
      <td>PMID:19062087</td>
      <td>GI: NM_007544.4</td>
      <td>Jean-Claude Martinou, SeronoPharmaceutical InstitutteFor purification of Bid</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism, version 6</td>
      <td>San Diego, California</td>
      <td>RRID: SCR_002798</td>
      <td>Scientific graphing program, used to perform statistical analysis</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB with toolboxes: Signal Processing, CurveFitting, Image Processing, Version R2020a</td>
      <td>https://doi.org/10.5683/SP3/ZKXQW8</td>
      <td>RRID:SCR_00162</td>
      <td>https://www.mathworks.com/products/matlab.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>INO software package including INO-FHS Acquisition,INO_FHS_Analysis, and INO_FHS_Batch Analysis</td>
      <td></td>
      <td>INO Client Release_r10357 package</td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected Construct</td>
      <td>mVenus-pEGFP-C1</td>
      <td>other</td>
      <td>GI: KU341334.1</td>
      <td>Dr. Ray Truant (McMaster University). Backbone EGFP-C1 (Clonetech)</td>
    </tr>
  </tbody>
</table>

### Purification of proteins

Full length human BCL-XL and human BAX were purified as previously described (Pogmore et al., 2016). Full length PUMA(α isoform) was expressed in Bl21-AI Escherichia coli purchased from New England Biolabs, pelleted using centrifugation, then lysed with the following buffer: PUMA Lysis Buffer – pH 8.5, 20 mM HEPES, 50 mM NaCl, 0.2% w/v CHAPS, 20% w/v Glycerol, 50 mM Imidazole, 10 μg/mL DNase, 1 mM PMSF. The lysate was then centrifuged to pellet debris. The supernatant was loaded onto a chitin resin column, 2 mL total volume (New England Biolabs) pre-equilibrated with PUMA Lysis Buffer. The column was then washed with PUMA Chitin Wash Buffer - pH 8.5, 20 mM HEPES, 50 mM NaCl, 0.6% w/v CHAPS, 20% w/v Glycerol, 50 mM Imidazole. After washing, 10 mL of PUMA Chitin Cleavage Buffer was poured on top the resin allowing ~8 mL to flow through. PUMA Chitin Cleavage Buffer - pH 8.5, 20 mM HEPES, 10 mM NaCl, 1% w/v Triton-X-100, 20% w/v Glycerol, 50 mM Imidazole, 300 mM Hydroxylamine. The column was capped retaining ~2 mL of the cleavage buffer on top of the chitin resin and left at 4 °C for 48–72 hours.

For labelling PUMA with a fluorescent dye,~2 mL was eluted from the chitin column, and the hydroxylamine was removed by gel filtration on a 10 mL Sephadex G25 medium column (GE Healthcare life science) equilibrated with PUMA Chitin Cleavage Buffer without hydroxylamine. The concentration of the eluted PUMA (~0.5 mL) was determined by spectrophometry and then labeled by adding urea to a final concentration of 3 M, 4 x molar excess relative to total protein of TCEP and 20 x molar excess of AlexaFluor 568 C5 Maleimide (ThermoFisher Scientific). The labelling reaction was adjusted to pH 7.2 using 12 M HCl, and rotated at 37 °C for 3 hours. The ~0.5 mL labelling reaction or chitin column elution (for unlabeled protein) was diluted in 30 mL of PUMA Ni-Binding Buffer - pH 7.2, 20 mM HEPES, 100 mM NaCl, 1% w/v CHAPS, 20% w/v Glycerol, 15 mM Imidazole and loaded onto a 0.5 mL HisPur Ni-NTA resin column (ThermoFisher Scientific). After washing the Ni-NTA resin with PUMA Ni-Wash Buffer 1 pH 7.2, 20 mM HEPES, 50 mM NaCl, 0.4% w/v CHAPS, 20% w/v Glycerol, 20 mM Imidazole and then with PUMA Ni-Wash Buffer 2 pH 7.2, 20 mM HEPES, 50 mM NaCl, 20% w/v Glycerol, 20 mM Imidazole, 0.5 M guanidine hydrochloride (GdnHCl) PUMA protein was eluted from the Ni-NTA resin with PUMA Ni-Elute Buffer - pH 7.2, 20 mM HEPES, 10 mM NaCl, 20% w/v Glycerol, 300 mM Imidazole, 1 M GdnHCl. Protein was quantified using a Bradford assay, flash frozen and stored at minus 80 °C until use.

### SMAC-mCherry Mitochondria Release Assay

SMAC-mCherry release assays were carried out as previously described (Niu et al., 2017). Briefly, BAX-/-/BAK-/- baby mouse kidney (BMK) cells stably expressing a fusion protein comprised of the mitochondrial import peptide of SMAC (amino acids 1–58) fused to the amino-terminus of the fluorescent protein mCherry were lysed by nitrogen cavitation at 150 psi for 10 min on ice in buffer containing 20 mM HEPES (pH 7.2), 250 mM sucrose, 150 mM potassium chloride, 1 mM EDTA, 1 X protease inhibitor cocktail. Nuclei and cell debris were removed by centrifugation of the lystate at 2000 g for 4 min at 4 °C. Heavy membranes containing mitochondria were obtained by centrifuging the supernatant at 13,000 g for 10 min at 4 °C and washing the pellet once in lysis buffer. Membrane fractions (0.2 mg/ml protein) were incubated with desired BCL-2 family proteins in 250 μL volume and incubated for 30 min at 37 °C. Mitochondria were then pelleted by centrifugation at 13,000 g for 10 min. The release of SMAC-mCherry was measured as fluorescence intensity using a Tecan M1000 microplate reader and comparing fluorescence intensity between the supernatant and pellet fractions. The percentage release of SMAC-mCherry was calculated as [Fsupernatant /(Fsupernatant +Fpellet)] x 100.

### In vitro FRET Assays

FRET experiments were carried out as previously described either in the presence or absence of liposomes (Pogmore et al., 2016; Kale et al., 2014). Briefly, using the same assay buffer that was used to make the liposomes, 100 uL reaction volumes were prepared in a 96-well half-area non-binding surface plate (Corning). Fluorescence intensity of the background was recorded for 30 minutes at 37 °C (back). Next, donor labelled protein (e.g., PUMA*A568) was added to each well, and the fluorescence intensity measured for 30 minutes at 37 °C (FD). Finally, acceptor labelled protein, (e.g. BCL-XL*A647) was added at the desired concentrations to each well, and the fluorescence intensity of the donor was measured for 60 minutes at 37 °C (FDA). The FRET efficiency expressed as a percentage was calculated using the following formula:

$$
% FRET E=(1−(\frac{F_{DA}−back}{F_{D }−back}))∗100
$$

As a control the fluorescence intensity of the donor (FD) was recorded in the presence of unlabeled acceptor. Therefore, for each concentration of labelled acceptor protein tested (FDA), a separate reaction containing the same concentration of unlabeled acceptor protein was measured (FD).

### Cell Lines and Culture

Baby mouse kidney (BMK) cells (wildtype and dko) were cultured in DMEM supplemented with 10% fetal bovine serum (Gibco) and 5% non-essential amino acids (NEAA, ThermoFisher). The BMK-dko cell line was a kind gift from the originator Eileen White, Rutgers Cancer Institute of New Jersey. NMuMG cells (a generous gift of J. Wrana, Lunenfeld-Tanenbaum Research Institute, Toronto, Canada) were cultured in DMEM, containing 10 µg/ml bovine insulin (Sigma), 10% fetal bovine serum (Gibco), and penicillin/streptomycin (Wisent). NMuMG cells expressing fluorescent landmark proteins were generated as previously described (Schormann et al., 2020). The originating cell lines used in the studies reported here (BMK-wt, BMK-dko, NMuMG) and all stably transfected clones were shown to be free of mycoplasma using a PCR based test (Hopert et al., 1993). All cell lines were maintained in a 5% CO2 atmosphere at 37 °C.

### Immunofluorescence

For immunofluorescence experiments to visualize the localization of endogenous PUMA, MCF-7 cells expressing either mCherry-ActA (mitochondrial marker) or mCherry-CB5 (ER marker) were seeded into 384-well plates, at a density of 7000 cells/well. The next day, cells were treated with indicated drugs and concentrations for 24 hours. On the third day, the cells were stained with DNA stain (DRAQ5) plus MitoTracker Green, or DRAQ5 plus Bodipy-thapsigargin for a total of 30 minutes. Subsequently, all cells were fixed using 4% formaldehyde diluted in Dulbecco’s Phosphate Buffered Saline (DPBS). Blocking solution (normal goat serum 5% v/v, Tiriton-X-100 0.3% v/v, diluted in DPBS) was then applied for 1 hour, followed by overnight incubation with primary anti-PUMA antibody. The next day, cells were washed with DPBS, then incubated with secondary anti-rabbit (Alexa Fluor(R) 488) antibody for 2 hours.

### Quantitative Fast FLIM-FRET (qF3)

Detecting protein interactions in live cells was carried out as previously described (Osterlund et al., 2022). Briefly, BMK-dko cells stably expressing a mCerulean3-fused anti-apoptotic protein were seeded at 4000 cells/well into a CellCarrier-384 Ultra Microplate (PerkinElmer). 24 hours later, individual wells were transfected with plasmids encoding Venus fused BH3- proteins using TransIT-X2 reagent (Mirus). Non-transfected wells were treated with transfection reagent alone (no DNA added). Media was changed after 3–5 hours. At this time, selected wells were treated with BH3 mimetic or DMSO. Sample plates were incubated 12–18 hours prior to imaging. Immediately before imaging, fluorescence protein standards were added to empty wells. Fluorescein (10 nM in 0.1 M NaOH) and quenched fluorescein (30 μM Fluorescein in 8.3 M NaI and 100 mM Na2HPO4 (pH 10)) were also added to the plate for instrument calibration. Data acquisition was performed on the INO-FHS microscope as previously described (Osterlund et al., 2019).

Data from each replicate was analyzed to generate binned binding curves. All biological replicates (3 or more) were combined and fit to a Hill equation to generate binding curves and calculate dissociation constants. A 1:1 binding between donor (mCerulean3) fused protein and acceptor (Venus) fused protein was assumed for all protein pairs. Regions of interest (ROIs) were automatically identified within images via a watershed algorithm applied to the TCSPC channel. Pixels within each ROI were combined and used to calculate the fluorescence lifetime. Change in angular frequency is then calculated from corresponding phasor analysis as described in Osterlund et al., 2022. The intensity of mCerulean3 and Venus per ROI was measured and then converted to concentration values based on measured standard curves prepared using recombinant fluorescent proteins and imaged on the same plate. We applied a narrow physiologically relevant range of mCerulean3 expression (1–3 µM) for our binding curves, and 0–50 µM range for Venus. In the 10–20 µM VenusFree range, the difference in angular frequency between positive control (Venus-BH3) and negative (Venus-BH3-4E mutant) must be greater than 0.05 to be considered as sufficient dynamic range in the assay to reliably detect changes. For each curve, the Bmax (saturation parameter) was estimated from the median of the points in the far right of each binding curve (30–50 µM VenusFree). The minimum sRatio, a threshold value representing the curvature of the binding data used to differentiate binding from collisions, was set to 1.5 based on previous analyses and theoretical modelling (Osterlund et al., 2022). For each protein pair data were combined from independent replicates (n≥3), and the average Kd reported. In heatmaps, ‘binding’ was represented in blue and ‘no binding’ in red. However, the colors are strictly to enable easy visual comparison of the data. In addition, the numerical value of the apparent Kd values are provided in each cell of the heatmaps.

### FLIM–FRET with ER or mitochondrial segmentation

In all other experiments in this paper, to extract FLIM-FRET binding curves ROIs were selected by applying a watershed segmentation algorithm to the TCSPC image of mCerulean3 (e.g. CBCL-XL). Our standard segmentation approach was run on all data as a positive control for detection of binding throughout the cell (see Figure 4—figure supplement 2 “mC3 total cell”). BCL-XL is found at the ER, mitochondria and in the cytoplasm (Kaufmann et al., 2003; Osterlund et al., 2023).

The purpose of this experiment was to express mCherry-tagged landmarks for ER or mitochondria in the same cells as PUMA and BCL-XL, then use the expression of the mCherry landmark to define the boundaries of ROI segmentation. This modification in ROI selection allows us to examine interactions in the ER verses mitochondria. MCF-7 cells stably expressing both CBCL-XL and mCherry (red channel)- tagged markers for ER (mCherry-Cb5) or mitochondria (mCherry-ActA) (Osterlund et al., 2023) were transiently transfected with constructs to express VPUMA, VPUMA-4E, VPUMAd26 orVPUMAd26-4E. Data were collected using two imaging configurations as we recently described (Osterlund et al., 2023). The two imaging configurations are rapidly exchanged to acquire signal from mCerulean3 and Venus (fluorescent proteins) by time correlated single photon counting (TCSPC) FLIM, and Venus and mCherry by using a 64-channel hyperspectral detector. Altogether, the Venus protein expression was captured in both configurations and may be used to confirm alignment images acquired in configurations 1 and 2. In contrast to our previous publication (Osterlund et al., 2022), we observed low transient expression of Venus. As a result, we modified our analysis pipeline to calculate relative Venus expression as a measure of intensity (arbitrary units) from the TCSPC FLIM image, rather than use the hyperspectral data, which requires background subtraction.

In detail, the intensity of signal from mCherry was determined by summing the hyperspectral counts at wavelengths 592–660 nm. The same parameters were used to segment all images of mCherry expression (Red Channel): background threshold (1000), Laplacian of a Gaussian kernel size (Delbridge et al., 2016) with sigma (0.13), structural element size (Wilfling et al., 2012), minimum ROI size (Chi et al., 2020), erode factor (0). Nevertheless, the resulting ROIs selected by the Watershed Algorithm were distinct (example images given in Figure 4—figure supplement 2A compare ChActA Mitochondria to ChCb5 ER). As expected, ROIs selected based on the mCherry-Cb5 expression appear more elongated and mesh-like compared to the more punctate ROIs selected based on mCherry-ActA (mitochondria). We provide the MATLAB analysis package on DataVerse (https://doi.org/10.5683/SP3/ZKXQW8).

The ROIs selected from mCherry-marker expression, were directly applied to extract for each ROI the average intensity and lifetime of mCerulean3 (donor) and the average intensity of Venus (acceptor). These data were used to generate FLIM-FRET binding curves in Figure 4—figure supplement 2B for ER- versus mitochondria-segmented ROIs as described (Osterlund et al., 2023). The % FRET efficiency was calculated using the phasor approach (Osterlund et al., 2022; Ranjit et al., 2018) and “Acceptor:Donor intensity ratio” represents the ratio of the average intensity per ROI of Venus to mCerulean3 both recorded by TCSPC. During acquisition, a 10 nM fluorescein sample in 0.1 M NaOH was used to standardize the instrument response for the three biological replicates to enable combining the binding curve data.

### Image Colocalization

Analyses of colocalization by image classification were carried out as previously described (Schormann et al., 2020). Conventional colocalization studies to measure Pearson’s correlation coefficients were carried out in BMK-dko cells. We utilized multiple fluorescent proteins and dyes to validate protein localization. To identify the endoplasmic reticulum, we either used a dye (BODIPY FL thapsigargin, ThermoFisher Scientific) or an overexpressed ER resident protein composed of EGFP fused to the ER specific tail anchor of BIK (CBIK). To identify mitochondria, the dyes MitoTracker Red and MitoTracker Green (ThermoFisher Scientific) were used. The cells were also stained with the nuclear stain, DRAQ5 to permit segmentation and quality control (Oltersdorf et al., 2005). Query proteins fused to the fluorescent proteins mCerulean3 or Venus were expressed by transfection of BMK-dko cells with gene encoding plasmids. Images were acquired using a 63 X water immersion objective, on the Opera Phenix microscope (PerkinElmer) and colocalization analyzed using an analysis pipeline created in Harmony software. In this pipeline, the DRAQ5 fluorescence signal was used to identify images of individual cells and create a mask for the nuclear and cytoplasmic areas. A low-intensity fluorescence threshold was applied to all cells in order to select for those successfully transfected and expressing the query protein (i.e. Venus or mCerulean3 fused BH3 only protein). Background was subtracted for each image and a Pearson’s correlation coefficient between fluorescent protein-fused query protein and fluorescently labelled organelle was calculated for all remaining objects within the cytoplasmic area. The median Pearson’s correlation coefficient for each replicate is plotted in Graphpad Prism software with a line indicating the average between all three replicates.

### Cell death assay

Cell death in response to exogenous expression of vBH3-only proteins in HEK293, BMK, and HCT116 cells, was measured as described (Chi et al., 2020). Briefly, cells were trypsinized and seeded in CellCarrier-Ultra 384-well plates. One day later, cells were transfected with plasmids encoding vBimL or vPuma (or the mutant proteins) using Mirus TransIT-X2 transfecting reagent. The media was aspirated prior to the addition of the transfection mix into each well. Four hr after transfection, the media was exchanged to remove the transfection mix. To measure cell death in response to BH3 mimetic treatments, cells were seeded as described above and the BH3 mimetics were added the next day as described (Chi et al., 2020). After 24 hr of transfection or drug treatment, cells nuclei were stained with Hoechst 33342 and Alexa 647 labelled Annexin V was added to detect externalized phosphatidylserine on the outer leaflet of the plasma membrane in dead or dying cells. Stained cells were imaged by automated confocal microscopy (Opera Phenix, PerkinElmer) and analyzed with Harmony software (V4.9) to obtain %Annexin V positivity for the population of cells in each treatment. Cell death due to vBimL or vPuma expression was quantified as percentage of Venus positive, Annexin V positive cells out of all Venus positive cells. Background Venus intensities in the un-transfected cells were used to determine the threshold for Venus positivity (2 standard deviations above the mean Venus intensity in the un-transfected wells).

### Image-based analysis of subcellular localization by machine learning

NMuMG cells expressing either EGFP-BIK-L61G or EGFP-PUMA4E were seeded (3000 cells per well) in multiple wells (at least 3) of a 384-well microplate (CellCarrier-384 ultra, B128 SRI/160; Perkin Elmer) and allowed to grow for 24 hr before staining with the nuclear dye DRAQ5 (5 nM; Biostatus). Cells were imaged (>15 field of views) on a spinning disk automated confocal microscope (PerkinElmer) with a 40 x water objective (NA = 0.9) in a defined temperature (37 °C) and CO2 (5%) environment. Images were collected using 3-Peltier cooled 12-bit CCD cameras (Type sensiCam, camera resolution 1.3 megapixels; PCO.imaging), unbinned. Segmentation and feature extraction were carried out as described in Schormann et al., 2020. Subcellular localization of cell images was determined by using a Random Forests classifier. Landmarks were expressed as EGFP fusion proteins in NMuMG cells for cell organelles shown in Figure 4: ER, (Cytochrome b5, BIK) and Calr-KDEL (ER targeting sequence of calreticulin fused to the N-terminus of EGFP and the ER retention sequence KDEL at the C-terminus of EGFP); ERGIC,ERGIC53; Golgi, GalT (N-terminal 81 amino acids of human beta 1,4-galactosyltransferase) and Golgin84; Mitochondria, MAO (sequence encoding the TA region of Monoamine oxidase A) and CCO (Cytochrome c oxidase, subunit VIII); MAM, Phosphatidylserine synthase 1; RAB5A and RAB7A vesicular compartments, Ras-related protein Rab5A and Rab7A; secretory pathway, VAMP2 and VAMP5 (Vesicle-associated membrane protein 2 and Vesicle-associated membrane protein 5); cytoplasm, Vesicle-associated membrane protein 1 A without TMD (delta-TMD-VAMP1); nuclear membrane, Lamin A; lysosomes, LAMP1 and peroxisomes, PTS1 (Peroxisome targeting signal 1).

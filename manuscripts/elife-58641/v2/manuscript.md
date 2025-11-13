# Optogenetic investigation of BMP target gene expression diversity

## Authors

- Katherine W Rogers<sup>1</sup> ([ORCID: 0000-0001-5700-2662](https://orcid.org/0000-0001-5700-2662))
- Mohammad ElGamacy<sup>1</sup>
- Benjamin M Jordan<sup>4</sup>
- Patrick Müller<sup>1</sup> ([ORCID: 0000-0002-0702-6209](https://orcid.org/0000-0002-0702-6209)) †

### Affiliations

1. Systems Biology of Development Group, Friedrich Miescher Laboratory of the Max Planck Society Tübingen Germany
2. Modeling Tumorigenesis Group, Translational Oncology Division, Eberhard Karls University Tübingen Tübingen Germany
3. Heliopolis Biotechnology Ltd London United Kingdom
4. Department of Organismic and Evolutionary Biology, Harvard University Cambridge United States

† Corresponding author

## Abstract

Signaling molecules activate distinct patterns of gene expression to coordinate embryogenesis, but how spatiotemporal expression diversity is generated is an open question. In zebrafish, a BMP signaling gradient patterns the dorsal-ventral axis. We systematically identified target genes responding to BMP and found that they have diverse spatiotemporal expression patterns. Transcriptional responses to optogenetically delivered high- and low-amplitude BMP signaling pulses indicate that spatiotemporal expression is not fully defined by different BMP signaling activation thresholds. Additionally, we observed negligible correlations between spatiotemporal expression and transcription kinetics for the majority of analyzed genes in response to BMP signaling pulses. In contrast, spatial differences between BMP target genes largely collapsed when FGF and Nodal signaling were inhibited. Our results suggest that, similar to other patterning systems, combinatorial signaling is likely to be a major driver of spatial diversity in BMP-dependent gene expression in zebrafish.

## Introduction

Embryogenesis is orchestrated by signaling pathways that activate spatiotemporally diverse patterns of gene expression. A prominent theory relating signaling to gene expression diversity is the gradient threshold model, in which a signaling gradient across a tissue defines unique spatial gene expression domains by activating target genes at different signaling thresholds (Figure 1A; Sharpe, 2019; Briscoe and Small, 2015; Dubrulle et al., 2015; Rogers and Schier, 2011; Barkai and Shilo, 2009; Ashe and Briscoe, 2006). Gene expression patterns can also be influenced by signaling dynamics and expression kinetics (Sagner and Briscoe, 2017) as well as interactions with other signaling pathways (Briscoe and Small, 2015). However, in many patterning systems the factors leading to diverse developmental gene expression profiles are incompletely characterized. Here, we investigate how signaling levels, target gene expression kinetics, and combinatorial signaling contribute to gene expression diversity during dorsal-ventral patterning in zebrafish.

![Figure 1.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig1-v2.jpg)

**Figure 1.:** (A) The gradient threshold model states that a signaling gradient activates genes (blue, white, red) at different thresholds (dashed gray lines). (B) BMP binding induces receptor complex formation, phosphorylation of Smad1/5/9, and activation of target genes. (C) Schematic of shield-stage zebrafish embryos with BMP signaling gradients (magenta) along the dorsal-ventral axis. (D-E) Representative images (D) of pSmad1/5/9 immunofluorescence in embryos at the indicated time post-fertilization and quantification (E). (F-O’) Fluorescence in situ hybridization (FISH) showing spatial expression of the indicated high-confidence BMP target genes at shield stage (~6.75 h post-fertilization (hpf)). (F,G,H,I,J,K,L,M,N,O) are animal views, dorsal to the right. (F’,G’,H’,I’,J’,K’,L’,M’,N’,O’) are ventral views. Vertical white bars indicate regions where expression is excluded from the margin. (P-Y) Quantification of FISH signal along the dorsal-ventral axis for the indicated BMP target genes at shield stage (ventral on the left, dorsal on the right as in (E)). Normalized intensities are shown; error bars represent standard error. The Gaussian function $Ae^{-\frac{x-\mu^{2}}{ς}}$ was fitted to each profile (gray lines), and gene expression range was defined as $r=\mu+2\sqrt{ς/2}$ (gray bars). Some BMP target genes could not be reliably quantified due to weak FISH signal (bmp4, id2a, smad6a, smad7, and znfl2b) or inability to reliably identify the ventral side in all assays (crabp2b). See the Figure 1—source data 1 file for source data.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Transcript levels in uninjected shield-stage (~6.75 hpf) embryos and siblings injected with 10 pg bmp2b or 100 pg chordin (Chd, BMP inhibitor) mRNA were assessed by RNA-sequencing (Supplementary file 1). (B) 16 high-confidence BMP target genes were both upregulated in bmp-overexpressing embryos and downregulated in chordin-overexpressing embryos. All RNA-seq data shown here is classified as significantly differentially regulated by edgeR, DESeq, and Cuff diff. (C) Embryos treated as in (A) were fixed at shield stage and BMP target gene expression assessed by in situ hybridization. (D) Opto-BMP (Figure 3—figure supplement 1A) and uninjected embryos were exposed to DMSO or 50 μg/ml of the translation inhibitor cycloheximide (CHX) at 6.25 hpf, illuminated with blue light from 6.75 to 7.25 hpf, and fixed 20 min post-exposure. A subset of BMP target genes was assessed by in situ hybridization. (E) Embryos were imaged using selective plane illumination microscopy to assess BMP signaling (pSmad1/5/9 immunofluorescence) or BMP target gene expression (fluorescence in situ hybridization). Average intensities along vertical lines from the ventral to dorsal side were calculated. ROIs excluded the embryo center for quantification of margin-restricted genes. See the Figure 1—figure supplement 1—source data 1 file for source data.

We focused on patterning mediated by BMP, a TGF-β superfamily member with important developmental roles across the animal kingdom (reviewed in Zinski et al., 2018). BMP ligands bind and assemble complexes of type I and II receptor serine/threonine kinases, resulting in the phosphorylation of the signal transducers Smad1/5/9 and activation of BMP target genes (Figure 1B; Derynck and Budi, 2019). The regulation of BMP gradient formation during early development has been analyzed in a variety of organisms including Drosophila, Nematostella, and Xenopus (Genikhovich et al., 2015; Iber and Gaglia, 2007; Mizutani et al., 2005; Plouhinec et al., 2013) as well as zebrafish. During late blastula and early gastrulation stages in zebrafish embryos, graded transcription and subsequent diffusion of BMP ligands, together with dorsally secreted BMP inhibitors such as Chordin, generate a ventrally-peaking gradient of BMP signaling that patterns the dorsal-ventral axis (Figure 1C; Pomreinke et al., 2017; Zinski et al., 2017). Loss of BMP signaling results in dorsalization, whereas excess BMP signaling produces ventralized embryos (Zinski et al., 2018). The degree of dorsalization or ventralization can be modulated by mutations in BMP pathway components with different strengths (Mintzer et al., 2001; Barth et al., 1999; Nguyen et al., 1998; Mullins et al., 1996) or by injecting different amounts of mRNA encoding pathway activators or inhibitors (Schumacher et al., 2011; Dick et al., 2000; Kishimoto et al., 1997; Neave et al., 1997).

These observations have led to the suggestion that BMP functions as a morphogen to pattern the dorsal-ventral axis by activating different target genes at different signaling level thresholds (Figure 1A; Zinski et al., 2018; Tuazon and Mullins, 2015; Schumacher et al., 2011; Barth et al., 1999; Nguyen et al., 1998; Neave et al., 1997; Mullins et al., 1996). However, overexpression and genetic manipulations can affect the duration of signal exposure, dysregulate other signaling pathways, and modify earlier aspects of development such as morphogenetic movements, complicating the interpretation of these experiments. Moreover, patterning of the dorsal-ventral axis by BMP and the germ layers by FGF and Nodal occurs simultaneously in zebrafish (Zinski et al., 2018), and although these pathways are known to interact, how FGF and Nodal influence the spatiotemporal expression of BMP target genes has not been systematically assessed.

To identify the factors that contribute to differences in BMP target gene expression and rule out factors that do not contribute, we first identified BMP targets in early zebrafish embryos and quantified their diverse spatial (Figure 1) and temporal (Figure 2) expression patterns. We then used an optogenetic approach to generate acute BMP signaling pulses (Figure 3) and found that while most target genes can respond to early BMP signaling (Figure 4), differential transcription kinetics do not fully account for the observed expression differences (Figure 5). Further, target gene responses to high- and low-amplitude signaling pulses suggest that not all spatiotemporal target gene expression differences are due to different signaling activation thresholds (Figure 6). In contrast, inhibition of FGF and Nodal signaling homogenized the spatial expression patterns of BMP targets, suggesting that combinatorial regulation by BMP, FGF, and Nodal is a major driver of BMP target gene spatial diversity (Figure 7).

![Figure 2.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig2-v2.jpg)

**Figure 2.:** (A–N) Embryos were collected every 30 min from 2.75 to 7.25 hpf, and transcript levels were quantified using NanoString technology. Error bars represent standard error. Temporal profiles were fit with the cumulative distribution function of the normal distribution (gray lines), and activation time (arrowheads) was defined as the average time point at which the curves reached about two mean average deviations (i.e., $1.5∙\tau$) from the inflection point $ν$ (excluding the maternally deposited genes id2a [Chong et al., 2005] and smad6a [White et al., 2017]). NanoString probes for two high-confidence activated BMP target genes (apoc1l and znfl2b) were not functional. (O) Average gene expression spatial range is plotted against average activation time. See the Figure 2—source data 1 file for source data.

![Figure 3.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig3-v2.jpg)

**Figure 3.:** (A) Schematic of Opto-BMP strategy. Blue light-dimerizable VfLOV domains were fused to zebrafish BMP receptor kinase domains. Blue light exposure activates BMP signaling. (B) Embryos injected with mRNA encoding Opto-BMP at the one-cell stage and their uninjected siblings were reared in the dark or exposed to blue light for 10 h starting 70–80 min post-fertilization. Ventralization phenotypes V1-V4 (indicating excess BMP signaling) were scored at 1 day post-fertilization. Number of embryos: uninjected dark = 59, Opto-BMP dark = 53, uninjected light = 55, Opto-BMP light = 60. (C-E) Uninjected and Opto-BMP-injected embryos were exposed to blue light (2300 lux) for 30 min starting at high stage (3.5 hpf) or shield stage (6.75 hpf) and fixed during and after exposure. pSmad1/5/9 immunofluorescence was quantified and plotted in (C) as Opto-BMP minus uninjected signal with piecewise linear interpolation between timepoints; error bars represent standard error (see Materials and methods for statistical analysis). Blue background represents light exposure. Representative embryos from the high-stage (D) and shield-stage (E) experiments quantified in (C). pSmad1/5/9 signal is shown in magenta, DAPI in cyan. See the Figure 3—source data 1 file for source data.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Embryos injected with Opto-BMP-encoding mRNA at the one-cell stage were reared in the dark or exposed to white light, and phenotypes were scored at 1 day post-fertilization (dpf). Number of embryos analyzed is indicated on top of each bar. A combination of Opto-Alk3, Opto-Alk8, and Opto-BMPR2a (arrowheads) was used in subsequent experiments. Equimolar amounts of mRNA were injected: Opto-Alk3: 5.2 pg, Opto-Alk8: 5.2 pg, Opto-BMPR2a: 8.9 pg, Opto-BMPR2b: 5 pg. (B) Blue LEDs were embedded into the lid of a six-well dish. (C) LED intensity was measured three times with a luxmeter at different voltages. Averages are shown with piecewise linear interpolation; error bars represent standard error. (D) Circuit schematic for the LED array. A program-generated square wave on a single-board computer acts as a signal source (S1) controlling an amplifier to time the operation and intensity of an LED array (D1-6) run on a constant-voltage power supply (V1). S1: Square wave signal source. C1-3: 1000 μF, 10 V electrolytic capacitor, V1: Constant-voltage regulated power supply, D1-6: 470 nm blue light diode, R1: 200 Ω resistor, R2: 68 Ω, 2W choke resistor, R3: 70 Ω resistor, R4: 7 kΩ resistor, R5: 20 kΩ resistor. (E-H) Opto-BMP embryos were exposed to a 5–12 μm-thick sheet of 405 nm light at the indicated laser power for 3 min using SPIM. BMP signaling was assessed using pSmad1/5/9 immunofluorescence (animal views). Opto-BMP embryos exhibit localized BMP activation compared to uninjected (E) and mock-exposed Opto-BMP embryos (F). (I-J) Uninjected and Opto-BMP-injected embryos were exposed to blue light (2300 lux) for 30 min starting at high stage (3.5 hpf, I) or shield stage (6.75 hpf, J). pSmad1/5/9 immunofluorescence was quantified and plotted with piecewise linear interpolation between timepoints; error bars represent standard error (Materials and methods). Blue background represents light exposure. This data is shown in Figure 3C as Opto-BMP - uninjected intensity. (K) Uninjected and Opto-BMP embryos were reared in the dark or exposed transiently to blue light (2300 lux) for 30 min or 10 h at the indicated developmental stages. (L) Phenotypes were scored at 1 dpf; number of embryos analyzed is indicated to the right of each bar. See the Figure 3—figure supplement 1—source data 1 file for source data.

![Figure 4.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig4-v2.jpg)

**Figure 4.:** (A) Schematic of competence model: Late-activated genes should respond to a late (shield stage, solid line), but not early (high stage, dashed line) BMP signaling pulse. (B-O) High-confidence BMP target gene responses after an early (high stage,~3.5 hpf, dashed line) or late (shield stage,~6.75 hpf, solid line) BMP signaling pulse delivered by exposing uninjected and Opto-BMP-injected embryos to 30 min blue light (Figure 3C–E and Figure 3—figure supplement 1I,J). To assess induced transcription, NanoString transcript counts from uninjected embryos were subtracted from Opto-BMP transcript counts and are plotted here with piecewise linear interpolation between timepoints; error bars represent standard error (see Materials and methods for statistical analysis). See the Figure 4—source data 1 file for source data.

![Figure 5.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig5-v2.jpg)

**Figure 5.:** (A) Different transcription kinetics may lead to differences in apparent activation times (arrowheads) based on assay detection thresholds (gray line). Assuming similar degradation kinetics, transcripts with faster induction rates should accumulate to higher levels in response to BMP. (B-E) Uninjected and Opto-BMP-injected embryos were exposed to blue light for 30 min at high (~3.5 hpf, B,C) or shield stage (~6.75 hpf, D,E), and target gene expression in response to the resulting BMP signaling pulses (Figure 3C–E and Figure 3—figure supplement 1I,J) was quantified using NanoString technology (Figure 4). Maximum average transcript counts were determined, and are plotted against activation time (B,D) (Figure 2) or spatial range (C,E). Error bars represent standard error, gray lines represent linear fits, ρs = Spearman correlation coefficient, ρp = Pearson correlation coefficient. crabp2b is not included due to lack of significant induction. (F-L) All three target gene response repeats were fitted with a model of induction and decay (Materials and methods). The average induction constant (σ) is plotted against activation time (F), spatial range (G), or maximum transcript count (J). The average decay constant (λ) is plotted against activation time (H), range (I), or maximum transcript count (K). Error bars represent standard error, ρs = Spearman correlation coefficient, ρp = Pearson correlation coefficient. crabp2b is not included due to lack of significant induction. pSmad1/5/9 immunofluorescence (Figure 3) was fitted with a polynomial (gray line, L) and used as signaling input. (M-Z) Individual fits of transcriptional responses (Figure 4); closed circles represent averages of three data points, open circles represent individual data points, and gray lines represent individual fits of each repeat. See the Figure 5—source data 1 source data file for source data.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A–F) Opto-BMP and uninjected embryos were exposed to blue light (2300 lux) for 30 min at shield stage (~6.75 hpf), and BMP target gene expression was assessed using colorimetric in situ hybridization in response to the BMP signaling pulse (Figure 3C and Figure 3—figure supplement 1J). Animal pole views. (G-H) Transcript levels in embryos treated as described in A-F were quantified using NanoString technology (Figure 4). BMP target gene induction (σ) and decay constants (λ) were determined by fitting the data using two approaches (Materials and methods): In Method 1 (main text and Figure 5), individual Opto-BMP – uninjected subtracted data series were fitted with a model of induction and decay for each transcript; in Method 2, all raw data points from the Opto-BMP and uninjected data sets were fitted simultaneously for each transcript. Both approaches produced similar σ (G) and λ (H) values (gray lines represent linear fits, ρs = Spearman correlation coefficient, ρp = Pearson correlation coefficient, Method one median shown). (I-W) In Method 2, pSmad1/5/9 immunofluorescence (Figure 3C and Figure 3—figure supplement 1J) was fitted with a model of induction and decay (gray line, I) and used as signaling input to model the transcript time series. Fits of uninjected (black) and Opto-BMP (blue) transcript data using Method two are shown in J-W. See the Figure 5—figure supplement 1—source data 1 file for source data.

![Figure 6.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig6-v2.jpg)

**Figure 6.:** (A) The activation threshold model predicts that broadly expressed genes will be activated by lower amplitude signaling. (B) pSmad1/5/9 immunofluorescence in uninjected and Opto-BMP-injected embryos exposed to 10 (triangle, dashed line) or 20 (diamond, solid line) min of 70 (light pink) or 3900 (magenta) lux blue light starting at shield stage. Immunofluorescence was quantified and plotted as Opto-BMP signal - uninjected with piecewise linear interpolation between timepoints; error bars represent standard error (see Materials and methods for statistical analysis). Embryos for the transcriptional response experiment were collected 30 (x), 40 (square), or 50 (circle) min after the start of light exposure. (C-F) Transcriptional responses in Opto-BMP embryos exposed to conditions shown in (B) were quantified using NanoString technology and are plotted against spatial range (C,E) or activation time (D,F). Embryos were collected 30 (x), 40 (square), or 50 (circle) min after the start of light exposure. Responses that are not statistically significant are anchored to the x-axis (N.S.; see Materials and methods for statistical analysis). See the Figure 6—source data 1 file for source data.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A–N) High-confidence BMP target gene responses were measured in zebrafish embryos by NanoString technology after exposure to optogenetically generated BMP signaling pulses with different amplitudes and durations (see Figure 6B for BMP signaling pulse profiles). Uninjected and Opto-BMP-injected embryos were exposed to 10 (triangle, dashed line) or 20 (diamond, solid line) min of 70 (lilac) or 3900 (dark purple) lux blue light starting at shield stage (~6.75 hpf), and collected 30, 40, and 50 min after the beginning of light exposure. To assess induced transcription, average NanoString transcript counts from uninjected embryos were subtracted from Opto-BMP transcript counts and are plotted here with piecewise linear interpolation between timepoints; large symbols represent averages of three data points, small symbols represent individual data points, and error bars represent standard error (see Materials and methods for statistical analysis). See the Figure 6—source data 1 file for source data.

![Figure 7.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig7-v2.jpg)

**Figure 7.:** (A) pSmad1/5/9 immunofluorescence in untreated embryos at the indicated times (data also shown in Figure 1E). (B-E) Embryos were treated with 10 μM FGF inhibitor SU-5402 (B), 50 μM Nodal inhibitor SB-505124 (C), or both (D) starting at 2 hpf, or injected with 0.5 pg bmp2b mRNA at the one-cell stage (E). The BMP signaling gradient was quantified along the dorsal-ventral axis at shield stage using pSmad1/5/9 immunofluorescence; error bars represent standard error. Note that the embryos in panels B-E came from different experiments and were processed and imaged on different days, but untreated controls were always siblings of treated embryos and processed and imaged simultaneously. (F-J) BMP target gene expression along the dorsal-ventral axis at shield stage in untreated (F), SU-5402-treated (G), SB-505124-treated (H), SB-505124 + SU-5402-treated (I), and bmp-overexpressing (J) embryos quantified using fluorescence in situ hybridization (untreated data from Figure 1). (K) FGF and Nodal block expression of a subset of BMP target genes at the margin, and restrict BMP signaling in part by activating the BMP inhibitor Chordin. (L) Ventral views of margin-excluded BMP target gene expression at shield stage assessed by FISH in untreated embryos (top row), bmp-overexpressing embryos (0.5 pg bmp2b mRNA, middle row), and embryos treated with SU-5402 + SB-505124 (bottom row). Vertical white bars indicate regions where expression is excluded from the margin. (M) Expression levels at the margin quantified by calculating the average normalized intensity from 5–10% embryo length in untreated versus bmp-overexpressing embryos (left) or untreated versus SU-5402+SB-505124-treated embryos (right). Lines connect treated and untreated conditions to visualize shifts, error bars represent standard error. Lower numbers indicate less expression at the margin. (N) Spatial coefficient of variation for the 10 BMP target genes assessed here in untreated (black), SU-5402-treated (yellow), SB-505124-treated (red), SU-5402+SB-505124-treated (salmon), and bmp-overexpressing (magenta) embryos. Lower numbers indicate less spatial diversity. See the Figure 7—source data 1 file for source data.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A–J’) BMP, FGF, and Nodal signaling were assessed at shield stage (~6.75 hpf) using pSmad1/5/9, pErk, or pSmad2/3 immunofluorescence, respectively, in untreated embryos and siblings injected with 0.5 pg bmp2b mRNA (A-C’), or exposed to 10 μM FGF inhibitor SU-5402 (D-E’), 50 μM Nodal inhibitor SB-505124 (F-G’), or both (H-J’) starting at 2 h post-fertilization (hpf). pSmad1/5/9: animal views, pErk: lateral views, pSmad2/3: dorsal views. Quantification is shown in Figure 7B–E. (K-O) Fluorescence in situ hybridization for the indicated 10 high-confidence BMP target genes in shield-stage embryos treated as described in A-J’. Untreated images are also shown in Figure 1; Left columns are animal views (dorsal to the right), and right columns are ventral views. Vertical white bars indicate regions where expression is excluded from the margin. (P-S) Expression levels at the margin quantified by calculating the average normalized intensity from 5–10% embryo length in embryos treated as described in A-J’. P and S are also shown in Figure 7. Lines connect treated and untreated conditions to visualize shifts; error bars represent standard error. See the Figure 7—figure supplement 1—source data 1 file for source data.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** Embryos were treated with 10 μM FGF inhibitor SU-5402 and 50 μM Nodal inhibitor SB-505124 starting at 2 hpf. (A-K) BMP signaling was assessed from 2.75 to 7.25 h post-fertilization (hpf) in treated and untreated embryos using pSmad1/5/9 immunofluorescence. Spatial BMP signaling gradients along the ventral-to-dorsal axis were quantified (B-K). Error bars represent standard error; data from untreated embryos also shown in Figures 1E and 7A. (L-ZA) BMP target gene transcript levels (L-Y) were assessed using NanoString technology in embryos treated as described above from 2.75 to 7.25 hpf. Temporal profiles were fit with the cumulative distribution function of the normal distribution (gray and light salmon lines), and activation time (black arrowhead = untreated, salmon arrowhead = drug-treated) was defined as the average time point at which the curves reached about two mean average deviations (i.e., $1.5∙\tau$) from the inflection point $ν$ (excluding the maternally deposited genes id2a [Chong et al., 2005] and smad6a [White et al., 2017]). Expression of bmp2b (Z) and chordin (ZA) was also assessed. Error bars represent standard error (see Materials and methods for statistical analysis). See the Figure 7—figure supplement 2—source data 1 file for source data.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig7-figsupp3-v2.jpg)

**Figure 7—figure supplement 3.:** Spatial quantification of fluorescence in situ hybridization signal along the dorsal-ventral axis for BMP target genes at shield stage in embryos treated as indicated, compared to untreated spatial distributions (black). Normalized intensities are shown, error bars represent standard error. (A) Embryos were injected with 0.5 pg bmp2b mRNA at the one-cell stage. (B-D) Embryos were treated with 10 μM FGF inhibitor SU-5402 (B), 50 μM Nodal inhibitor SB-505124 (C), or both (D) starting at 2 hpf. See the Figure 7—figure supplement 3—source data 1 file for source data.

## Results

### BMP target genes have diverse spatiotemporal expression patterns

We used RNA-sequencing to systematically identify genes activated by BMP during early zebrafish gastrulation, when BMP is engaged in dorsal-ventral patterning (shield stage,~6.75 h post-fertilization (hpf)) (Zinski et al., 2018). We identified 16 high-confidence target genes that are significantly upregulated in bmp-overexpressing embryos and downregulated in embryos overexpressing the BMP inhibitor chordin (Figure 1—figure supplement 1A–D and Supplementary file 1). 14 of these genes (apoc1l, bambia, bmp4, cdx4, eve1, foxi1, gata2a, id2a, klf2b, smad6a, smad7, sizzled, tfap2c, and ved) are known to be positively regulated by BMP in zebrafish (Kashiwada et al., 2015; Wang et al., 2015; Kotkamp et al., 2014; Wang et al., 2013; Das and Crump, 2012; de Pater et al., 2012; Kwon et al., 2010; Li and Cornell, 2007; Poulain et al., 2006; Chong et al., 2005; Davidson et al., 2003; Martyn and Schulte-Merker, 2003; Nissen et al., 2003; Solomon et al., 2003; Yabe et al., 2003; Pogoda and Meyer, 2002; Shimizu et al., 2002; Oates et al., 2001; Tsang et al., 2000; Chin et al., 1997; Nikaido et al., 1997; Hammerschmidt et al., 1996a; Hammerschmidt et al., 1996b; Mullins et al., 1996; Detrich et al., 1995; Joly et al., 1993; Joly et al., 1992), whereas crabp2b (Sharma et al., 2005) and znfl2b (Hogan et al., 2006) have not previously been implicated as BMP targets. Four of the 16 target genes encode repressors of BMP signaling (bambia, sizzled, smad6a, and smad7) and one encodes bmp4, consistent with roles for negative and positive feedbacks in TGF-β-mediated patterning (Zinski et al., 2018).

According to the gradient threshold model, target genes are activated by distinct signaling levels, leading to different spatial domains of target gene expression in the presence of a signaling gradient (Figure 1A). To determine whether the BMP patterning system fits this paradigm, we first sought to characterize both BMP signaling distribution and spatial target gene expression. We assessed spatial BMP signaling from 2.75 to 7.25 hpf (256-cell stage – 60% epiboly) using immunofluorescent stainings to detect the BMP signal transducer pSmad1/5/9. We imaged embryos using selective plane illumination microscopy (SPIM) and quantified fluorescence along the dorsal-ventral axis (Figure 1—figure supplement 1E, Materials and methods). Similar to previous studies (Pomreinke et al., 2017; Zinski et al., 2017; Ramel and Hill, 2013; Tucker et al., 2008), we observed a ventrally-peaking BMP signaling gradient that increases in amplitude over time (Figure 1D,E).

We then used fluorescence in situ hybridization and SPIM to quantify the spatial expression profiles of BMP target genes along the dorsal-ventral axis at shield stage (~6.75 hpf) and found that target genes have different expression profiles along this axis (Figure 1F–Y, Figure 1—figure supplement 1E, Materials and methods; some genes could not be quantified due to weak signal or inability to reliably identify the ventral side). The shape of the expression profiles can be well described by bell curves. We therefore used regression analysis with the Gaussian function

$$
Ae^{-\frac{x-\mu^{2}}{ς}}
$$

and defined the range of each target gene as

$$
r=\mu+2\sqrt{ς/2}
$$

Using this definition, spatial gene expression broadness ranges from 40–100% dorsal-ventral embryo length (Figure 1F–Y). Strikingly, pronounced differences along the orthogonal animal-vegetal axis were also evident: Genes were either uniformly expressed along this axis on the ventral side (sizzled, ved, apoc1l, and bambia), restricted to the margin (cdx4 and eve1), or excluded from the margin (foxi1, klf2b, gata2a, and tfap2c) (Figure 1C,F–O’). Margin exclusion resulted in distinct dorsal-ventral profiles in which mRNA levels peak around 30% embryo length (Figure 1R,T,W,X), compared to non-excluded genes that peaked more ventrally (Figure 1P,Q,S,U,V,Y). Therefore, some of the spatial diversity in BMP target gene expression arises from differences along the animal-vegetal axis, orthogonal to the dorsal-ventral BMP signaling gradient.

The gradient threshold paradigm (Figure 1A) implies that genes with broad ranges should be activated by lower signaling levels. Since signaling levels increase over time (Figure 1D,E; Pomreinke et al., 2017; Zinski et al., 2017; Ramel and Hill, 2013; Tucker et al., 2008), we sought to determine whether more broadly expressed targets were activated earlier. To assess temporal expression of BMP targets, we used NanoString molecular barcoding (Kulkarni, 2011) to measure transcript levels from 2.75 to 7.25 hpf (256-cell stage – 60% epiboly) (Figure 2A–N). The shape of the temporal expression profiles can be well approximated by the modified cumulative distribution function of the normal distribution

$$
\frac{1}{2}A1+erf⁡\frac{x-ν}{\tau\sqrt{2}}+b
$$

We used this function for regression analysis of the temporal expression profiles and defined activation times as the average time point at which the curves reached about two mean average deviations (i.e., $1.5∙\tau$) from the inflection point $ν$. BMP target gene activation times defined in this way ranged from 3.4 to 6.3 hpf (Figure 2).

The gradient threshold model predicts a monotonic decrease when comparing range and activation time. While this relationship is not observed for the entire dataset (Figure 2O), there is a decreasing monotonic trend when foxi1, eve1, and cdx4 are excluded (note that in contrast to the other genes, the expression of eve1 and cdx4 was only quantified in the embryonic margin [Figure 1—figure supplement 1E, Materials and methods]). This suggests the possibility that subsets of BMP target genes may behave consistently with the gradient threshold model. We therefore sought to investigate the relationship between BMP signaling and target gene expression further using an optogenetic strategy.

### Reversible optogenetic activation of BMP signaling in vivo using Opto-BMP

To assess how BMP target genes respond to BMP signaling, we developed a method to optogenetically manipulate BMP signaling in vivo. We fused zebrafish BMP receptor kinase domains to an algal blue light-homodimerizable LOV domain (Rogers and Müller, 2020; Takahashi et al., 2007) and targeted the fusions to the membrane using a myristoylation motif (Figure 3A), similar to previous approaches (Ramachandran et al., 2018; Vopalensky et al., 2018; Sako et al., 2016). Blue light (~450 nm) exposure should lead to dimerization of the LOV domains and interaction of the BMP kinase domains, activating BMP signaling (Figure 3A).

Injection of mRNA encoding Opto-BMP into zebrafish embryos at the one-cell stage resulted in strong ventralization in light-reared embryos, consistent with excess BMP signaling, whereas dark-reared siblings were mostly aphenotypic (Figure 3B and Figure 3—figure supplement 1A,K,L). Spatially localized activation of BMP signaling was also possible using SPIM, further demonstrating light-dependent signaling activation (Figure 3—figure supplement 1E–H).

To facilitate optogenetic experiments, we developed a light exposure device by embedding blue LEDs into the lid of a standard six-well plate and controlling light intensity and dynamics with a single-board computer (Figure 3—figure supplement 1B–D, Materials and methods). Using the LED array, we exposed uninjected and Opto-BMP-injected embryos to blue light for 30 min during high (3.5–4 hpf) or shield (6.75–7.25 hpf) stages, fixed embryos during and after exposure, and quantified BMP signaling using pSmad1/5/9 immunofluorescence (Figure 3C–E and Figure 3—figure supplement 1I,J). At both stages, Opto-BMP embryos showed a dramatic increase in BMP signaling within 10 min of light exposure, and signaling levels returned to normal after light removal. These experiments demonstrate that Opto-BMP reversibly activates BMP signaling in zebrafish embryos in response to light.

### Most BMP target genes are competent to respond to BMP at early stages

BMP target genes are activated over a range of developmental stages, from 3.4 to 6.3 hpf (Figure 2). Time-dependent differences in competence – a gene’s ability to respond to signaling – may underlie the diversity in activation timing (Figure 4A). To test this, we quantified BMP target gene expression in uninjected and Opto-BMP-injected embryos exposed to 30 min blue light during either high (3.5–4 hpf) or shield stage (6.75–7.25 hpf) (Figure 4 and Figure 5—figure supplement 1A–F).

In response to a strong BMP signaling pulse at high or shield stage (Figure 3C–E and Figure 3—figure supplement 1I,J), we observed corresponding significant pulses of BMP target gene expression for all genes except crapb2b and cdx4 (Figure 4K,L). While cdx4 is not competent to respond to an early BMP signaling pulse and crabp2b did not clearly respond to either an early or late signaling pulse, all other tested high-confidence BMP target genes responded at high stage. Therefore, differences in competence to respond to BMP signaling at early stages do not explain the majority of diversity in activation timing.

### Transcription kinetics in response to BMP do not fully explain spatiotemporal expression

Target gene transcription kinetics can play important roles in defining spatial expression domains. For example, it has been suggested that Nodal target genes with faster transcript accumulation rates have broader spatial expression domains (Dubrulle et al., 2015). To investigate how the transcription kinetics of BMP target genes may influence their spatiotemporal expression patterns, we assessed the dynamics of target gene responses (Figure 4) to optogenetically generated BMP signaling pulses (Figure 3C–E and Figure 3—figure supplement 1I,J). We reasoned that the early activation timing and broad spatial range of some BMP targets might be explained by more rapid transcription in response to BMP. In this paradigm, early BMP signaling activates expression of all target genes at the same time, but transcripts of more slowly transcribed genes only accumulate to detectable levels at later stages, causing them to appear to be ‘late-activated’ (Figure 5A). Similarly, broader spatial ranges could be caused by faster accumulation of rapidly produced transcripts that would therefore be detectable farther from the ventral side than more slowly produced transcripts.

To determine whether higher transcript accumulation rates correlate with broader spatial ranges or earlier activation times, we first assessed maximum transcript counts in response to BMP signaling pulses at high or shield stage (Figure 4). Assuming similar transcript degradation kinetics, transcripts with faster production rates should accumulate to higher levels in response to a BMP signaling pulse (Figure 5A). However, we observed a weak negative correlation (Figure 5B) or no correlation (Figure 5D) between maximum transcript counts and activation time, and found similar results for range (Figure 5C,E). This suggests that differences in transcript accumulation rates in response to BMP do not fully account for differences in activation timing and spatial broadness.

We then used a second approach to assess transcript accumulation kinetics that does not require the assumption of similar transcript degradation rates (Figure 5F–Z). We fitted the transcription data from the shield-stage BMP signaling pulse with a model involving the known pSmad1/5/9 input (Figure 3C, Figure 5L, and Figure 3—figure supplement 1J) and parameters reflecting transcript induction (σ) and decay (λ) (Figure 5M–Z, Materials and methods). Each of the three experimental repeats was fitted individually, and average σ and λ values were calculated for each gene. We found a weak negative correlation between σ and activation time (Figure 5F), and no correlation between σ and range (Figure 5G). We also observed a weak negative correlation between λ and activation time (Figure 5H), and no obvious correlation between λ and spatial broadness (Figure 5I). These results are consistent with the maximum transcript count analysis (Figure 5B–E) and with an alternative fitting approach (Figure 5—figure supplement 1G–W, Materials and methods). In addition, we observed a strong positive correlation between maximum transcript count and σ (Figure 5J), and no correlation between maximum transcript count and λ (Figure 5K), suggesting that production dominates transcription kinetics, and supporting the use of maximum transcript count as a proxy for induction rate.

Together, our analyses indicate that differential transcription kinetics in response to BMP signaling play a minor role in generating the distinct spatiotemporal expression patterns of BMP target genes.

### Differential activation thresholds do not fully explain spatiotemporal expression

In the gradient threshold paradigm, target genes are activated by distinct signaling thresholds that define gene expression ranges (Figure 1A). This model therefore predicts that broadly expressed genes, but not narrowly expressed genes, should be activated by low levels of signaling (Figure 6A).

To test this idea, we exposed uninjected and Opto-BMP-injected embryos to high- (3900 lux) or low-intensity (70 lux) blue light for 10 or 20 min at shield stage – resulting in high- or low-amplitude BMP signaling pulses, respectively (Figure 6B) – and then quantified BMP target gene responses using NanoString technology. As expected, target activation was generally stronger following higher amplitude, longer duration pulses (Figure 6C–F and Figure 6—figure supplement 1). However, after a 10 min low-amplitude exposure, the third most narrowly expressed gene, foxi1, was significantly activated, whereas the broader genes were not robustly induced (Figure 6C). A longer 20 min low-amplitude pulse significantly activated both narrowly and broadly expressed genes (Figure 6E). A 10 min low-amplitude pulse significantly activated two of the top 50% earliest expressed genes (foxi1 and smad7), whereas a 20 min low-amplitude pulse significantly activated both early and late-expressed genes (Figure 6D,F). High-amplitude pulses activated genes of all ranges and activation times (Figure 6C–F).

Our experiments exposing embryos to different amplitude BMP signaling pulses therefore suggest that not all spatiotemporal target gene expression differences are due to different signaling activation thresholds, although a subset may be (see Discussion).

### FGF and Nodal modify BMP signaling and target gene expression

We noted that BMP target genes have unique expression patterns along the animal-vegetal axis that contribute to differences in their dorsal-ventral expression profiles (Figure 1F–Y). Specifically, 6 out of the 10 spatially quantified high-confidence BMP target genes are either restricted to (cdx4, eve1) or excluded from (foxi1, klf2b, gata2a, tfap2c) the margin. We wondered how regulation by additional signaling pathways active at the margin might contribute to these differences. We focused on the FGF and Nodal pathways, which regulate mesoderm and mesendoderm specification, respectively, and are known to influence BMP signaling (Figure 7; Rogers and Müller, 2019).

To assess the effects of FGF and Nodal signaling on BMP target gene expression, we inhibited these pathways using the small molecule inhibitors SU-5402 (Mohammadi et al., 1997) and SB-505124 (DaCosta Byfield et al., 2004), respectively (Figure 7—figure supplement 1A–J’). At shield stage, Nodal inhibition did not observably affect BMP signaling (Figure 7C and Figure 7—figure supplement 1F–G’), whereas FGF inhibition increased the amplitude of the BMP signaling gradient (Figure 7B and Figure 7—figure supplement 1D–E’). Simultaneous inhibition of both FGF and Nodal signaling increased both the amplitude and spatial broadness of the BMP signaling gradient (Figure 7D, Figure 7—figure supplement 1H–J’, and Figure 7—figure supplement 2A–K). Consistent with enhanced BMP signaling, in the absence of FGF/Nodal several BMP-activated genes were upregulated (Figure 7—figure supplement 2L–Y). Reduced levels of the secreted BMP inhibitor Chordin in embryos lacking FGF/Nodal signaling (Figure 7—figure supplement 2ZA) are likely to contribute to this BMP signaling expansion (Varga et al., 2007; Londin et al., 2005; Koshida et al., 2002). Additionally, FGF restricts the expression of bmp (Londin et al., 2005; Fürthauer et al., 2004; Fürthauer et al., 1997), and we detected increased bmp2b expression in FGF/Nodal-inhibited embryos (Figure 7—figure supplement 2Z).

Loss of FGF, Nodal, or both simultaneously affected BMP target gene dorsal-ventral spatial expression profiles differently (Figure 7F–I, Figure 7—figure supplement 1, and Figure 7—figure supplement 3). To determine whether FGF and Nodal are responsible for the margin restriction or exclusion of some BMP target genes (Figure 1F–O’), we assessed target expression along the animal-vegetal axis in inhibitor-treated embryos. In embryos lacking both FGF and Nodal signaling, margin-restricted genes were still expressed and restricted to the margin, whereas the expression of margin-excluded genes shifted into the margin (Figure 7I,L,M, and Figure 7—figure supplement 1).

We reasoned that the shift of margin-excluded genes into the margin could either be due to loss of FGF/Nodal activity, or due to enhanced BMP signaling at the margin (Figure 7D, Figure 7—figure supplement 1A–J’, and Figure 7—figure supplement 2A–K). We therefore assessed the animal-vegetal expression of margin-excluded genes in bmp-overexpressing embryos, which have dramatically elevated levels of BMP signaling at the ventral margin (Figure 7E) but intact Nodal and FGF signaling (Figure 7—figure supplement 1A–C’; Fürthauer et al., 1997). Margin-excluded genes were still clearly excluded from the margin in bmp-overexpressing embryos, suggesting that direct inhibition by FGF and Nodal normally prevents expression of these genes at the margin (Figure 7J,L,M).

To determine whether FGF and Nodal contribute to diversity in BMP target gene activation timing, we quantified the temporal expression of BMP targets in embryos lacking FGF and Nodal signaling from 2.75 to 7.25 hpf (256-cell stage – 60% epiboly) (Figure 7—figure supplement 2L–Y). Although transcript levels of several BMP targets were higher in treated compared to untreated embryos at later stages, their activation times were still diverse, suggesting that inputs other than FGF and Nodal are responsible for differences in activation times.

Finally, we noticed that much of the spatial diversity in BMP target gene expression along the dorsal-ventral axis collapsed in embryos lacking both FGF and Nodal signaling (Figure 7F,I). To quantify the decrease in spatial diversity, we calculated the spatial coefficient of variation in untreated and treated embryos (see Materials and methods). Strikingly, embryos lacking both FGF and Nodal had lower coefficients of variation at almost all positions along the dorsal-ventral axis compared to untreated embryos (Figure 7N). Together, our results identify combinatorial FGF and Nodal signaling as a major driver of spatial diversity in BMP target gene expression.

## Discussion

### Minor roles for differential responses to BMP in generating spatiotemporal diversity

Signaling gradients are frequently observed in developing tissues, including the embryonic axes of gastrulating zebrafish, the neural tube in mice, and the wing precursor in Drosophila (Briscoe and Small, 2015; Schier and Talbot, 2005). However, how gradients are interpreted by cells is complex to ascertain. The gradient threshold model proposes that gene-specific activation thresholds are responsible for differences in the spatial expression of target genes (Sharpe, 2019; Briscoe and Small, 2015; Dubrulle et al., 2015; Rogers and Schier, 2011; Barkai and Shilo, 2009; Ashe and Briscoe, 2006). Can gradients be reliably generated and signaling thresholds accurately interpreted with high sensitivity, or do gradients simply provide a ‘rough framework’ for patterning that is refined over time by other mechanisms such as target gene cross-talk (Briscoe and Small, 2015; Chen et al., 2012) or cell sorting (Akieda et al., 2019; Xiong et al., 2013)? In the former case, is such precision actually required for patterning?

In the context of zebrafish dorsal-ventral patterning, our data suggest minor roles for gene-specific activation thresholds in generating BMP target gene expression diversity. We did not find a clear monotonically decreasing relationship between activation time and gene expression range (Figure 2O), suggesting that more broadly expressed genes are not consistently more likely to be activated by the low levels of BMP present early (Figure 1D–E). We were also unable to detect an unambiguous correlation between range and the levels of signaling required for activation (Figure 6C,E). This suggests that not all BMP target expression boundaries are positioned by gene-specific BMP signaling thresholds (Figure 1A).

An alternative model proposes that diversity in spatiotemporal target gene expression is due to differences in expression kinetics. For example, it was shown that Nodal targets with higher transcript accumulation rates in response to Nodal signaling have broader spatial expression domains (Dubrulle et al., 2015). To determine whether the BMP patterning system might function similarly, we examined the transcriptional responses of BMP target genes (Figures 4 and 5, and Figure 5—figure supplement 1) to optogenetically generated pulses of BMP signaling (Figure 3C–D and Figure 3—figure supplement 1I,J). We did not detect a strong correlation between transcript induction rates and activation time or spatial range (Figure 5 and Figure 5—figure supplement 1G–W). Therefore, differential transcription kinetics in response to BMP are unlikely to account for spatiotemporal expression diversity.

Our results do not rule out the possibility that a different subset of BMP target genes may behave more consistently with these models. We focused on a set of high-confidence BMP targets (Figure 1—figure supplement 1), but other known targets were excluded from our analyses (Supplementary file 1). For example, the BMP target gene tp63 (Bakkers et al., 2002) is not expressed at shield stage, and was therefore excluded since it was not downregulated by chordin overexpression in our RNA-sequencing experiment (Supplementary file 1). We note that a subset of three genes (sizzled, ved, and bambia) that are neither restricted to nor excluded from the margin do show a monotonically decreasing relationship between range and activation time (Figure 2O) as well as activation dynamics that could be roughly commensurate with signaling input (Figure 6C and Figure 6—figure supplement 1), consistent with the gradient threshold model. However, it remains to be determined to what extent this subset of genes (or others) quantitatively follows the input-output relationships predicted by the gradient threshold model.

Our results also do not rule out other mechanisms of BMP signaling interpretation. For example, the graded distribution of many genes (Figure 1P–Y) could be consistent with a model in which gene expression is roughly proportional to the level of BMP signaling. In addition, BMP signaling duration may encode specific responses in vivo. Future work is needed to better define the relationship between BMP signaling levels and gene expression and to determine how BMP signaling dynamics are interpreted in embryos. Our study highlights the promise of optogenetic approaches in such investigations (Rogers and Müller, 2020). In contrast to pharmacological or genetic methods, optogenetic strategies can provide fast, tunable, and reversible spatiotemporal manipulation of signaling in vivo (Figure 3, Figure 6B, and Figure 3—figure supplement 1E–H), allowing more thorough characterization of input/output relationships.

In addition, our observations indicate that BMP signaling precision may not be required for proper patterning, or that the system is robustly buffered. For example, most embryos experiencing transient activation of BMP signaling lack gross morphological defects (Figure 3C–E, Figure 4, Figure 3—figure supplement 1A,K,L, and Figure 5—figure supplement 1). How patterning recovers from such insults will be an interesting avenue for future study. Together with previous work (reviewed in Zinski et al., 2018), several of our observations indicate that feedback is an important feature of the BMP patterning system: Five out of 16 high-confidence BMP target genes affect BMP signaling (Figure 1—figure supplement 1), and embryos can experience a dip in signaling levels after a signaling pulse (Figure 3C and Figure 3—figure supplement 1J). Cell sorting strategies that sharpen gene expression boundaries may also contribute to the observed recovery from BMP signaling manipulation (Akieda et al., 2019; Xiong et al., 2013).

### Margin restriction and competence of BMP target genes

One unresolved question from our study is the restriction of the BMP target genes eve1 and cdx4 to the margin (Figure 1I,I’,L,L’ and Figure 7—figure supplement 1). Consistent with previous work (Swanhart et al., 2010; Ota et al., 2009; Bennett et al., 2007; Ho et al., 2006; Londin et al., 2005; Shimizu et al., 2005; Rentzsch et al., 2004), in the absence of FGF or Nodal, eve1 and cdx4 were still expressed at the ventral margin (Figure 7—figure supplement 1; we note, however, conflicting reports with dominant-negative FGF receptors [Ota et al., 2009; Kudoh et al., 2004; Griffin et al., 1995]). Inhibition by animal pole factors or a requirement for signaling pathways at the margin such as Wnt or retinoic acid might play a role in their margin restriction.

Both eve1 and cdx4 are also activated relatively late in development (Figure 2F,J), and cdx4 is not competent to respond to an early BMP signaling pulse (Figure 4K). FGF and Nodal have no obvious roles in regulating their activation timing or competence since their temporal expression was not significantly affected by loss of FGF/Nodal signaling (Figure 7—figure supplement 2Q,U). Understanding how the activation timing of all BMP target genes including eve1 and cdx4 is regulated is an important future goal.

### FGF and Nodal are major contributors to BMP target gene spatial diversity

Inhibition of FGF, Nodal, or both together had distinct effects on BMP signaling (Figure 7B–D, Figure 7—figure supplement 1A–J’, and Figure 7—figure supplement 2A–K). The increase in BMP signaling in the absence of FGF is likely explained by several factors including the known role of FGF in activating chordin and inhibiting bmp transcription (Figure 7—figure supplement 2Z,ZA) (Varga et al., 2007; Maegawa et al., 2006; Londin et al., 2005; Fürthauer et al., 2004; Kudoh et al., 2004; Koshida et al., 2002; Fürthauer et al., 1997), as well as inactivating Smad1 (Sapkota et al., 2007; Pera et al., 2003; Kretzschmar et al., 1997). Loss of Nodal did not detectably alter BMP signaling at shield stage. This is surprising because early expression of fgf is thought to depend on Nodal (van Boxtel et al., 2015; Maegawa et al., 2006; Mathieu et al., 2004; Gritsman et al., 1999; Rodaway et al., 1999), although low levels of fgf3 appear to be present at late blastula stages in Nodal signaling mutants (Mathieu et al., 2004), and weak FGF activity is detectable in Nodal inhibitor-treated embryos (van Boxtel et al., 2015). Nodal can activate chordin expression independently of FGF (Varga et al., 2007), and chordin is detectable albeit reduced in Nodal signaling mutants (Gritsman et al., 1999), suggesting that the reduction in chordin caused by Nodal loss is not sufficient to affect BMP signaling during early gastrulation. Future work is needed to explain why FGF, but not Nodal loss enhances BMP signaling at early gastrulation, and why simultaneous loss increases not only the amplitude but the broadness of the BMP signaling gradient.

Inhibition of FGF, Nodal, or both together also had distinct effects on BMP target gene expression (Figure 7F–I, Figure 7—figure supplements 1, 2 and 3). Although Nodal loss did not detectably alter the BMP signaling gradient (Figure 7C and Figure 7—figure supplement 1F–G’), the spatial distributions of several BMP target genes were affected (Figure 7H, Figure 7—figure supplement 1N,R, and Figure 7—figure supplement 3C). Nodal is also responsible for the dorsal expression of the BMP target gene apoc1l (Figure 1O,O’,Y), which is lost in the absence of Nodal (Figure 7H, Figure 7—figure supplement 1N, and Figure 7—figure supplement 3C). Although our study defines individual target gene responses at the phenomenological level, uncovering the DNA-level mechanisms (e.g., promoter regulation and chromatin status) that lead to the observed responses to BMP, FGF, and Nodal is an important future challenge.

The margin exclusion of the BMP target genes foxi1, klf2b, gata2a, and tfap2c can be explained by FGF/Nodal-mediated inhibition (Figure 7K). Loss of either FGF or Nodal signaling shifted the expression of margin-excluded genes toward the margin, although the shifts were most dramatic in the absence of both (Figure 7F–I,L,M, Figure 7—figure supplement 1, and Figure 7—figure supplement 3), with the exception of tfap2c, which was completely margin-shifted in FGF-inhibited embryos (Figure 7G, Figure 7—figure supplement 1M,Q, and Figure 7—figure supplement 3B). Excess BMP signaling at the margin in embryos lacking FGF and Nodal (Figure 7D, Figure 7—figure supplement 1H–J’, and Figure 7—figure supplement 2A–K) does not explain the observed gene expression shifts because no shifts were evident in bmp-overexpressing embryos (Figure 7J,L,M, Figure 7—figure supplement 1L,P, and Figure 7—figure supplement 3A). The FGF/Nodal-mediated margin exclusion of a subset of BMP targets contributes to the diversity in BMP target gene expression (Figure 7F,I,K,N), creating distinct dorsal-ventral profiles for margin-excluded genes (Figure 1R,T,W,X) compared to non-excluded genes (Figure 1P,Q,S,U,V,Y).

Our results suggest that much of the spatial diversity in BMP target gene expression arises from combinatorial signaling. A similar strategy is thought to regulate Bicoid target genes during Drosophila embryogenesis: Gene expression boundary shifts in response to Bicoid manipulation are often inconsistent with the gradient threshold model (Chen et al., 2012; Ochoa-Espinosa et al., 2009), and activation thresholds do not appear to explain target gene expression profiles at the DNA level (Ochoa-Espinosa et al., 2005). Rather, Bicoid is thought to act within a system of repressive pathways that regulate Bicoid target gene expression (Chen et al., 2012). During zebrafish dorsal-ventral patterning, FGF and Nodal affect BMP target gene expression in two ways: by restricting BMP signaling (Figure 7B–D, Figure 7—figure supplement 1D–E’,H–J’, and Figure 7—figure supplement 2A–K), and by inhibiting a subset of BMP target genes at the margin (Figure 7F–I,L,M, Figure 7—figure supplement 1, and Figure 7—figure supplement 3). These interactions sculpt the spatial expression profiles of BMP target genes and contribute to the patterning of the dorsal-ventral axis.

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
      <td>Strain, strain background (E. coli)</td>
      <td>One Shot TOP10</td>
      <td>Life Technologies</td>
      <td>C4040</td>
      <td>Chemically competent</td>
    </tr>
    <tr>
      <td>Strain, strain background (Danio rerio)</td>
      <td>TE zebrafish</td>
      <td>Pomreinke et al., 2017 Donovan et al., 2017</td>
      <td></td>
      <td>Wild type</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-phospho- Smad1/Smad5/Smad9 (Rabbit monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>13820, RRID:AB_2493181</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-rabbit Alexa Fluor 488-conjugated secondary (Goat polyclonal)</td>
      <td>Life Technologies</td>
      <td>A11008, RRID:AB_143165</td>
      <td>IF (1:5000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-phospho-Smad2/Smad3 (Rabbit monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>8828, RRID:AB_2631089</td>
      <td>IF (1:5000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-rabbit horseradish peroxidase (Goat polyclonal)</td>
      <td>Jackson ImmunoResearch</td>
      <td>111-035-003, RRID:AB_2313567</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-pErk (Mouse monoclonal)</td>
      <td>Sigma</td>
      <td>M8159, RRID:AB_477245</td>
      <td>IF (1:5000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-mouse horseradish peroxidase (Donkey polyclonal)</td>
      <td>Jackson ImmunoResearch</td>
      <td>715-035-150, RRID:AB_2340770</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-digoxigenin horseradish peroxidase Fab fragments (Sheep polyclonal)</td>
      <td>Roche</td>
      <td>11207733910, RRID:AB_514500</td>
      <td>FISH (1:150)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCS2-Opto-Alk3</td>
      <td>Generated in this study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCS2-Opto-Alk8</td>
      <td>Generated in this study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCS2-Opto-BMPR2a</td>
      <td>Generated in this study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCS2-Opto-BMPR2b</td>
      <td>Generated in this study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TRIzol reagent</td>
      <td>Invitrogen</td>
      <td>5596026</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Co-Precipitant Pink</td>
      <td>Bioline</td>
      <td>BIO-37075</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cycloheximide</td>
      <td>Sigma</td>
      <td>C4859</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Pronase</td>
      <td>Roche</td>
      <td>11459643001</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DMSO</td>
      <td>Roth</td>
      <td>A994.2</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>FBS</td>
      <td>Biochrom</td>
      <td>S0415</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DAPI</td>
      <td>Life Technologies</td>
      <td>D1306</td>
      <td>1:5000</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Blocking reagent</td>
      <td>Roche</td>
      <td>11096176001</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Low melting temperature agarose</td>
      <td>Lonza</td>
      <td>50080</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Nodal inhibitor SB-505124</td>
      <td>Sigma</td>
      <td>S4696-5MG</td>
      <td>50 μM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>FGF inhibitor SU-5402</td>
      <td>Sigma</td>
      <td>SML0443-5MG</td>
      <td>10 μM</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TSA plus cyanine three system</td>
      <td>Perkin Elmer</td>
      <td>NEL744001KT</td>
      <td>FISH/IF (1:75)</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNeasy kit</td>
      <td>QIAGEN</td>
      <td>74104</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Wizard SV Gel and PCR Clean-up System</td>
      <td>Promega</td>
      <td>A9282</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>pCR-bluntII TOPO kit</td>
      <td>Thermo Fisher Scientific</td>
      <td>450245</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>SP6 mMessage mMachine transcription kit</td>
      <td>Thermo Fisher Scientific</td>
      <td>AM1340</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>DIG RNA labeling mix</td>
      <td>Sigma-Aldrich</td>
      <td>11277073910</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji</td>
      <td>Schindelin et al., 2012</td>
      <td>https://fiji.sc/ RRID:SCR_002285</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Prism</td>
      <td>GraphPad Software</td>
      <td>https://www.graphpad.com/scientific-software/prism RRID:SCR_002798</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>COMSOL Multiphysics 3.5a</td>
      <td>COMSOL, Inc</td>
      <td>https://www.comsol.com/ RRID:SCR_014767</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Matlab</td>
      <td>Mathworks</td>
      <td>http://mathworks.com RRID:SCR_001622</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>edgeR 3.2.3</td>
      <td>Robinson et al., 2010</td>
      <td>RRID:SCR_012802</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DESeq 1.12.0</td>
      <td>Anders and Huber, 2010</td>
      <td>RRID:SCR_000154</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cuff diff 2.1.1</td>
      <td>Trapnell et al., 2010</td>
      <td>https://github.com/cole-trapnell-lab/cufflinks</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PWM code for controlling LED array</td>
      <td>Generated in this study</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>nSolver 4.0 software</td>
      <td>NanoString</td>
      <td>RRID:SCR_003420</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Excel</td>
      <td>Microsoft</td>
      <td>RRID:SCR_016137</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Maple</td>
      <td>Waterloo Maple Inc</td>
      <td>RRID:SCR_014449</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>RNA-sequencing data</td>
      <td>Generated in this study</td>
      <td>GEO: GSE135100</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>TIP122 complementary power NPN Darlington</td>
      <td>STMicroelectronics</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Regulated power supply</td>
      <td>Disrelec Group AG</td>
      <td>RND 320-KD3000D</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>6-well plates</td>
      <td>Greiner Bio-One</td>
      <td>657160</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Blue LEDs</td>
      <td>Nichia</td>
      <td>NSPB510AS</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Blue LEDs</td>
      <td>Everlight</td>
      <td>1363-2SUBC/C470/S400-A4</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Temperature- controlled incubator, Heratherm IMC 18</td>
      <td>ThermoScientific</td>
      <td>50125882</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Raspberry Pi model B</td>
      <td>Raspberry Pi Foundation</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>LM37 luxmeter</td>
      <td>DOSTMANN electronic GmbH</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>White worklight</td>
      <td>REV Ritter GmbH</td>
      <td>90910</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Red color filters</td>
      <td>Rosco</td>
      <td>E106 Primary Red</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Zebrafish husbandry

Zebrafish husbandry was executed in accordance with the guidelines of the State of Baden-Württemberg (Germany) and approved by the Regierungspräsidium Tübingen (35/9185.46–5, 35/9185.81–5). Wild type TE adult zebrafish were maintained under standard conditions. Embryos were incubated at 28°C in embryo medium (250 mg/l Instant Ocean salt, 1 mg/l methylene blue in reverse osmosis water adjusted to pH 7 with NaHCO3 [Müller et al., 2012]) unless otherwise noted.

### mRNA in vitro synthesis

pCS2+-based plasmids encoding Bmp2b, Chordin (Pomreinke et al., 2017), and Opto-BMP (this work, Figure 3—figure supplement 1, see below for cloning details) were linearized with NotI-HF (NEB, R3189). Capped mRNA was generated using a mMessage mMachine SP6 kit (ThermoFisher, AM1340). mRNA was purified using an RNeasy Mini kit (Qiagen, 74104) and quantified using a NanoDrop spectrophotometer (ThermoScientific).

### RNA-sequencing

Wild type TE zebrafish embryos were dechorionated with Pronase (Roche, 11459643001) and injected at the one-cell stage with 10 pg mRNA encoding zebrafish Bmp2b, 100 pg mRNA encoding zebrafish Chordin, or left uninjected (Pomreinke et al., 2017). When uninjected siblings reached shield stage (~6.75 hpf), embryos were snap-frozen in liquid nitrogen. 10 embryos were collected per sample, three samples per condition.

To prepare total RNA, the TRIzol reagent (Invitrogen, 15596026) manufacturer’s protocol was followed until aqueous phase recovery, then 6.25 μl Co-Precipitant Pink (Bioline, BIO-37075) was added to 250 μl aqueous phase, followed by 375 μl 100% EtOH. After vortexing briefly, samples were transferred to RNeasy Mini kit (Qiagen, 74104) spin columns and centrifuged at 13600 rpm at 4°C for 1 min. Flow-through was discarded and columns were washed twice with RPE buffer (Qiagen). RNA was eluted in 50 μl H2O. Total RNA concentration was measured using a NanoDrop spectrophotometer (ThermoScientific). 3–5 μg total RNA per sample were provided to LCG Genomics GmbH (Berlin, Germany) for sequencing and differential expression analysis. Sequences were aligned against the reference genome Danio rerio GRCz10 with STAR 2.4.1b, and differential expression analysis was carried out with edgeR 3.2.3, DESeq 1.12.0, and Cuff diff 2.1.1. The p-value threshold for differentially expressed genes was set to 0.05.

Note that endogenous bmp2b and chordin were not distinguishable from injected mRNAs in bmp2b- or chordin-injected embryos, respectively, and were therefore excluded from consideration as BMP target genes.

### Opto-BMP constructs

Opto-BMP constructs are based on Opto-Acvr constructs (Sako et al., 2016). These pCS2+-based Opto-Acvr constructs encode proteins that are tethered to the plasma membrane by an N-terminal myristoylation motif. Next to the membrane is a Nodal receptor kinase domain, followed by the light-oxygen-voltage (VfLOV) domain Aureochrome1 from Vaucheria frigida (Takahashi et al., 2007), and finally a C-terminal HA tag. Using splicing by overlap extension (SOE) PCR (Horton et al., 2013), Nodal receptor kinase domains in Opto-Acvr were swapped with putative kinase domains from the type I zebrafish BMP receptors Alk3 (NM_131621, bp 691–1566) (Nikaido et al., 1999) and Alk8 (NM_131345, bp 622–1497) (Mintzer et al., 2001; Yelick et al., 1998), and the type II zebrafish receptors BMPR2a (NM_001039817, bp 571–3009) and BMPR2b (NM_001039807, bp 598–1536) (Monteiro et al., 2008). In all cases except for Opto-BMPR2a, all residues after the transmembrane domain until the end of the kinase domain were included. Opto-BMPR2a contains all residues after the transmembrane domain until the end of the protein; the kinase domain-only construct was inactive.

An equimolar combination of mRNA encoding Opto-Alk3 (5.2 pg), Opto-Alk8 (5.2 pg), and Opto-BMPR2a (8.9 pg) was found to optimally induce BMP signaling in the light but not in the dark (Figure 3B, Figure 3—figure supplement 1A,K,L), and was used in all Opto-BMP experiments described here.

### LED array

To facilitate optogenetic experiments requiring control of light intensity and exposure duration, an embedded system-based controller was developed (Figure 3—figure supplement 1B–D). To maximize the versatility of the setup for different applications, a single-board computer was deployed (Raspberry Pi 3 model B, running under a Linux kernel, version 4.9). The controller was programmed to generate signals that modulate the duration and intensity of light. The generated signal was further amplified to drive the load of the LED array. A two-stage Darlington amplifier was used (TIP122 complementary power NPN Darlington - STMicroelectronics) to raise the ceiling of the current of amplification. The Darlington pair was used in a common emitter configuration in order to achieve a large power gain. The loads were operated on a constant voltage source provided by a regulated power supply (Disrelec Group AG, RND 320-KD3000D). During initial trials, brief, weak signal spikes could be detected, and an RC filter was subsequently used across the load to dampen any sporadic light flashes. The LED array constituted the circuit load; these LEDs were glued into the plastic cover of 6-well plates (Greiner Bio-One, 657160) (Figure 3—figure supplement 1B). Blue Nichia (NSPB510AS) or Everlight (1363-2SUBC/C470/S400-A4) LEDs were used in the array. Both LEDs emitted maximal spectral intensity at 470 nm, with the Nichia LEDs having a broader radiation angle, tighter spectral distribution, and less variable performance. During experiments, the LED array was placed inside a temperature-controlled incubator (Thermo Scientific Heratherum IMC 18, 50125882) set to 28°C. Dark fabric was taped to the interior of the incubator door to prevent outside light from entering.

The circuit schematic (Figure 3—figure supplement 1D) shows how the generated square wave was used to drive the LED array. One of the Raspberry Pi’s GPIO pins was used as a pulse-width modulation (PWM) output to produce signal. The raspberry-gpio-python module (https://sourceforge.net/projects/raspberry-gpio-python) was used to interface the GPIO. A pulse program was written in Python, which allows for variable parameter settings: GPIO pin number, modulation frequency (10 kHz is the NPN Darlington amplifier linear limit), pulse duration, and duty cycle.

Light intensities were measured using an LM37 luxmeter (DOSTMANN electronic GmbH).

LED array settings used in optogenetic experiments:

<table>
  <thead>
    <tr>
      <th>Fig.</th>
      <th>Experiment</th>
      <th>LED</th>
      <th>Voltage (V)</th>
      <th>Frequency (Hz)</th>
      <th>Intensity (lux)</th>
      <th>Duration (min)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">3, 3.1I,J</td>
      <td>Shield stage</td>
      <td>Everlight</td>
      <td>24</td>
      <td>200</td>
      <td>2300</td>
      <td>30</td>
    </tr>
    <tr>
      <td>High stage</td>
      <td>Everlight</td>
      <td>25–28</td>
      <td>2</td>
      <td>2300</td>
      <td>30</td>
    </tr>
    <tr>
      <td rowspan="2">4, 5, 5.1 G-W</td>
      <td>Shield stage</td>
      <td>Everlight</td>
      <td>24</td>
      <td>200</td>
      <td>2300</td>
      <td>30</td>
    </tr>
    <tr>
      <td>High stage</td>
      <td>Everlight</td>
      <td>25–28</td>
      <td>2</td>
      <td>2300</td>
      <td>30</td>
    </tr>
    <tr>
      <td rowspan="2">6, 6.1</td>
      <td>70 lux</td>
      <td>Nichia</td>
      <td>15</td>
      <td>200</td>
      <td>70</td>
      <td>10 or 20</td>
    </tr>
    <tr>
      <td>3900 lux</td>
      <td>Nichia</td>
      <td>21</td>
      <td>200</td>
      <td>3900</td>
      <td>10 or 20</td>
    </tr>
    <tr>
      <td rowspan="2">1.1D</td>
      <td>bambia, klf2b, sizzled, smad6a, smad7, ved</td>
      <td>Everlight</td>
      <td>25–28</td>
      <td>2</td>
      <td>2300</td>
      <td>30</td>
    </tr>
    <tr>
      <td>apoc1l, bmp4, cdx4, crabp2b, eve1, foxi1, gata2a, id2a, tfap2c, znfl2b</td>
      <td>Nichia</td>
      <td>21</td>
      <td>200</td>
      <td>3900</td>
      <td>30</td>
    </tr>
    <tr>
      <td rowspan="2">3.1K,L</td>
      <td>Shield stage</td>
      <td>Everlight</td>
      <td>24</td>
      <td>200</td>
      <td>2300</td>
      <td>30</td>
    </tr>
    <tr>
      <td>All except shield</td>
      <td>Everlight</td>
      <td>25–28</td>
      <td>2</td>
      <td>2300</td>
      <td>30 or 600</td>
    </tr>
    <tr>
      <td>5.1A-F</td>
      <td>All</td>
      <td>Everlight</td>
      <td>24</td>
      <td>200</td>
      <td>2300</td>
      <td>30</td>
    </tr>
  </tbody>
</table>

For all experiments above, the duty cycle was 100%, and the GPIO pin was 32.

A white worklight (REV Ritter GmbH, 90910) was used in experiments described in Figure 3—figure supplement 1A. For all exposure conditions described in this work, no phototoxicity was evident.

PWM code for controlling the LED array (sqr_pls_v01.py):#!/usr/bin/python
import sys
import time
import getopt
import RPi.GPIO as GPIO

def usage():
  hlp_str = """Basic square pulse programme

input:
-p output BOARD pin number <int>
-f PWM frequency in Hz <int>
-d duty cycle (in percentage terms) <int>
-t length of the pulse in seconds <float>

example usage:
./sqr_pls_v01.py -p 32 -f 200 -d 100 -t 50.0
"""
  print(hlp_str)

def init_out_chan(pin_num, mod_frq):

  """###################
# initiate output #
#-----------------##################################################
# input:
# - output PWM pin number (12, 32 or 33) <int>
# - PWM frequency in Hz <int>
# output:
# - pin object
# BOARD numbering mode
# only BOARD channels 12, 32 and 33 are PWModulable
####################################################################
  """

  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(pin_num, GPIO.OUT)
  pin = GPIO.PWM(pin_num, mod_frq)

  return pin

def sqr_pls(pin_num, mod_frq, dc, span):

  """###################
# generate output #
#-----------------##################################################
# input:
# - output PWM pin number (12, 32 or 33) <int>
# - PWM frequency in Hz <int>
# - duty cycle (in percentage terms) <int>
# - length of the pulse in seconds <float>
# output:
# - 0: completion; 1: interruption <int>
####################################################################
  """

  p = init_out_chan(pin_num, mod_frq)
  t_strt = time.time()
  p.start(dc)
  p.ChangeDutyCycle(dc)
  try:
    while (time.time() - t_strt) < span:
      time.sleep(1)
      print("seconds remaining: " + str(round(span - (time.time()-t_strt))))
  except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
    return 1
  p.stop()
  GPIO.cleanup()

  return 0

def main():

  try:
    opts, args = getopt.getopt(sys.argv[1:],"p:f:d:t:")
  except getopt.GetoptError as e:
    print(str(e))
    usage()
    sys.exit(2)

  for o, a in opts:
    if o == '-p':
      pin_num=int(a)
      if pin_num not in [12, 32, 33]:
        print("--USAGE ERROR\n--PIN NUMBER UNACCEPTABLE\n")
        usage()
        sys.exit(2)
    elif o == '-f':
      mod_frq=int(a)
      if (mod_frq > 10000) or (mod_frq < 0):
        print("--USAGE ERROR\n--MODULATION FREQUENCY VALUE OUTSIDE 0-10000 RANGE\n")
        usage()
        sys.exit(2)
    elif o == '-d':
      dc=int(a)
      if (dc > 100) or (dc < 0):
        print("--USAGE ERROR\n--DUTY CYCLE VALUE OUTSIDE 0-100 RANGE\n")
        usage()
        sys.exit(2)
    elif o == '-t':
      t=float(a)
      if (t < 0):
        print("--USAGE ERROR\n--PASSING NEGATIVE TIME")
        usage()
        sys.exit(2)
  #sqr_pls(pin_num, frq, dc, t)
  try:
    print("--commencing square pulse at pin %d modulated at %d Hz at %d%% power for %.3f seconds" % (pin_num, mod_frq, dc, t))
    print("--starting at %s" % time.ctime())
  except Exception as e:
    print(str(e))
    print("--MISSING ARGUMENT(S) - REVISE USAGE")
    usage()
    sys.exit(2)

  exec_val = sqr_pls(pin_num, mod_frq, dc, t)
  if exec_val:
    print("--Terminating\n--SEQUENCE INTERRUPTED at %s" % time.ctime())
  else:
    print("--Terminating\n--sequence completed at %s" % time.ctime())
  return exec_val

if __name__ == "__main__":
  main()

To guard against inadvertent photoactivation, plates containing embryos were wrapped in aluminum foil starting from ~70 min post-injection until light exposure. Where applicable (e.g. Figure 1—figure supplement 1 and Figure 3—figure supplement 1), red color filters (Rosco, E106 Primary Red) were used to cover light sources such as dissecting microscope stages to prevent transmission of VfLOV-dimerizing wavelengths.

### Cycloheximide experiment

For the cycloheximide (Sigma, C4859) experiment in Figure 1—figure supplement 1D, embryos from wild type TE incrosses were dechorionated using Pronase (Roche, 11459643001) and injected at the one-cell stage with 5.2 pg opto-Alk3 + 5.2 pg opto-Alk8 + 8.9 pg opto-BMPR2a mRNA (Figure 3—figure supplement 1A). Control siblings were left uninjected, and embryos were sorted into agarose-coated 6-well plates and incubated at 28°C. 70–90 min post-fertilization at the 4–16 cell stage, unfertilized and damaged embryos were removed, and plates were individually wrapped in aluminum foil to prevent light exposure and incubated at 28°C. At 6.25 h post-fertilization (hpf), embryos were transferred into new agarose-coated 6-well dishes containing either 50 μg/ml cycloheximide (Bennett et al., 2007; Poulain and Lepage, 2002) or an equivalent volume of DMSO (Roth, A994.2) diluted in embryo medium that had been incubated at 28°C prior to transfer. Red color filters (Rosco, E106 Primary Red) were used to cover the dissecting microscope light source during the transfer to prevent transmission of VfLOV-dimerizing wavelengths and minimize BMP activation, and plates were wrapped in aluminum foil after transfer. At 6.75 hpf (~shield stage, 30 min after cycloheximide exposure), plates were transferred to a small 28°C incubator containing the LED array (Figure 3—figure supplement 1B) and exposed to blue light for 30 min (6.75–7.25 hpf). 20 min after light exposure, when most BMP target genes are maximally induced (Figure 4), embryos were fixed and colorimetric in situ hybridization was carried out as described in the Fluorescence and colorimetric in situ hybridization section below.

### pSmad1/5/9, pSmad2/3, and pErk immunofluorescence staining

For pSmad1/5/9, pSmad2/3, and pErk immunofluorescence staining, embryos were fixed in 4% formaldehyde in PBS at 4°C overnight, then transferred to MeOH and stored at −20°C for at least 2 h. See below and Figure 1—figure supplement 1E for imaging and quantification details.

#### pSmad1/5/9

Embryos were washed at least three times with PBST (phosphate buffered saline + 0.1% Tween-20), then blocked for at least 1 h at room temperature in blocking buffer (10% FBS (Biochrom, S0415), 1% DMSO, 0.1% Tween-20 in PBS). Embryos were incubated in 1:100 rabbit anti-phosphoSmad1/5/9 antibody (Cell Signaling Technology, 13820) in blocking buffer at 4°C overnight. One wash with blocking buffer followed by 3–5 washes with PBST were carried out at room temperature, then embryos were blocked again with blocking buffer for at least 1 h. Embryos were incubated in 1:5000 goat anti-rabbit Alexa Fluor 488-conjugated secondary antibody (Life Technologies, A11008) in blocking buffer at 4°C overnight. Embryos were then incubated in 1:5000 DAPI (Life Technologies, D1306; stock concentration: 5 mg/ml) in blocking buffer at room temperature for at least 1 h, then washed at least five times with PBST. Stained embryos were wrapped in aluminum foil and stored at 4°C overnight before SPIM imaging.

#### pSmad2/3

Embryos were incubated in ice-cold acetone (Roth, 5025.5) for 7 min, then washed at least three times with PBST, blocked for at least 1 h in 10% FBS in PBST and incubated in 1:5000 rabbit anti-pSmad2/3 (Cell Signaling Technology, 8828) in 10% FBS in PBST at 4°C overnight. Embryos were then washed at least five times in PBST, blocked again for at least 1 h in 10% FBS in PBST, and incubated in 1:500 goat anti-rabbit HRP secondary antibody (Jackson ImmunoResearch, 111-035-003) in 10% FBS in PBST at 4°C overnight. Next, embryos were washed at least five times in PBST, then once in TSA 1x amplification buffer (TSA Plus Cyanine 3 System, Perkin Elmer, NEL744001KT). For staining, embryos were incubated in 75 μl 1:75 Cy3-TSA in 1x amplification buffer in the dark at room temperature for 45 min. After washing at least six times with PBST, embryos were incubated in 1:5000 DAPI (Life Technologies, D1306; stock concentration: 5 mg/ml) in PBST at room temperature for at least 1 h, then washed at least four times with PBST. Finally, embryos were wrapped in aluminum foil and stored at 4°C overnight before SPIM imaging.

#### pErk

Embryos were washed at least three times with PBST, then transferred to ice-cold acetone for 20 min and washed at least three times with PBST. After blocking in 10% FBS in PBST for at least 1 h, embryos were incubated in 1:5000 mouse anti-pErk antibody (Sigma, M8159) in 10% FBS in PBST at 4°C overnight. Embryos were then washed at least five times in PBST, blocked again for at least 1 h in 10% FBS in PBST, and incubated in 1:500 donkey anti-mouse HRP secondary antibody (Jackson ImmunoResearch, 715-035-150) in 10% FBS in PBST at 4°C overnight. Embryos were washed at least five times with PBST, then once in TSA 1x amplification buffer. Next, embryos were incubated in 75 μl 1:75 Cy3-TSA in 1x amplification buffer in the dark at room temperature for 45 min. After washing at least six times with PBST, embryos were incubated in 1:5000 DAPI (Life Technologies, D1306; stock concentration: 5 mg/ml) in PBST at room temperature for at least 1 h, then washed at least four times with PBST. Stained embryos were wrapped in aluminum foil and stored at 4°C overnight before SPIM imaging.

### Fluorescence and colorimetric in situ hybridization

BMP target gene probes were generated by amplifying full or partial coding sequences (CDS) from wild type TE zebrafish cDNA and cloning into pCS2+ or pCR-bluntII TOPO (ThermoFisher, 450245) vectors. Plasmids were linearized with the indicated restriction enzymes, column purified (Promega, A9282), and DIG-labeled probes were generated using the indicated polymerase (Roche, 11175025910).

High-confidence BMP target gene in situ hybridization probes:

<table>
  <thead>
    <tr>
      <th>Gene</th>
      <th>Vector</th>
      <th>Sequence</th>
      <th>Enzyme</th>
      <th>Polymerase</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>apoc1l</td>
      <td>pCS2+</td>
      <td>entire CDS</td>
      <td>ClaI</td>
      <td>T7</td>
    </tr>
    <tr>
      <td>bambia</td>
      <td>pCR-bluntII TOPO</td>
      <td>partial CDS; bp 47–425</td>
      <td>BamHI</td>
      <td>T7</td>
    </tr>
    <tr>
      <td>bmp4</td>
      <td>pCR-bluntII TOPO</td>
      <td>partial CDS; bp 103–558</td>
      <td>EcoRV</td>
      <td>SP6</td>
    </tr>
    <tr>
      <td>cdx4</td>
      <td>pCR-bluntII TOPO</td>
      <td>partial CDS; bp 132–810</td>
      <td>EcoRV</td>
      <td>SP6</td>
    </tr>
    <tr>
      <td>crabp2b</td>
      <td>pCR-bluntII TOPO</td>
      <td>partial CDS; bp 14–436</td>
      <td>EcoRV</td>
      <td>SP6</td>
    </tr>
    <tr>
      <td>eve1</td>
      <td>pCR-bluntII TOPO</td>
      <td>partial CDS; bp 42–665</td>
      <td>BamHI</td>
      <td>T7</td>
    </tr>
    <tr>
      <td>foxi1</td>
      <td>pCS2+</td>
      <td>entire CDS</td>
      <td>ClaI</td>
      <td>T7</td>
    </tr>
    <tr>
      <td>gata2a</td>
      <td>pCR-bluntII TOPO</td>
      <td>partial CDS; bp 40–1141</td>
      <td>SpeI</td>
      <td>T7</td>
    </tr>
    <tr>
      <td>id2a</td>
      <td>pCR-bluntII TOPO</td>
      <td>partial CDS; bp 6–401</td>
      <td>BamHI</td>
      <td>T7</td>
    </tr>
    <tr>
      <td>klf2b</td>
      <td>pCS2+</td>
      <td>entire CDS</td>
      <td>ClaI</td>
      <td>T7</td>
    </tr>
    <tr>
      <td>smad6a</td>
      <td>pCR-bluntII TOPO</td>
      <td>partial CDS; bp 8–880</td>
      <td>BamHI</td>
      <td>T7</td>
    </tr>
    <tr>
      <td>smad7</td>
      <td>pCR-bluntII TOPO</td>
      <td>partial CDS; bp 23–1024</td>
      <td>BamHI</td>
      <td>T7</td>
    </tr>
    <tr>
      <td>sizzled</td>
      <td>pCS2+</td>
      <td>entire CDS</td>
      <td>ClaI</td>
      <td>T7</td>
    </tr>
    <tr>
      <td>tfap2c</td>
      <td>pCS2+</td>
      <td>entire CDS</td>
      <td>ClaI</td>
      <td>T7</td>
    </tr>
    <tr>
      <td>ved</td>
      <td>pCR-bluntII TOPO</td>
      <td>partial CDS; bp 7–825</td>
      <td>EcoRV</td>
      <td>SP6</td>
    </tr>
    <tr>
      <td>znfl2b</td>
      <td>pCR-bluntII TOPO</td>
      <td>partial CDS; bp 25–435</td>
      <td>BamHI</td>
      <td>T7</td>
    </tr>
  </tbody>
</table>

Note that the znfl2b in situ probe contained 47 SNPs compared to the reference genome (Danio rerio GRCz11).

The same DIG-labeled probes were used for both fluorescence (Figures 1F–Y and 7F–J, Figure 7—figure supplement 1K–O, and Figure 7—figure supplement 3) and colorimetric (Figure 1—figure supplement 1C–D and Figure 5—figure supplement 1A–F) in situ hybridization at a concentration of 1 ng/μl.

Whole-mount colorimetric in situ hybridization was carried out as described previously (Thisse and Thisse, 2008). Embryos were fixed in 4% formaldehyde in PBS, incubated at 4°C overnight, then transferred to MeOH and stored at −20°C for at least 2 h. Stained embryos were imaged in 2:1 benzyl benzoate:benzyl alcohol with an Axio Zoom.V16 microscope (ZEISS).

For fluorescence in situ hybridization (FISH), the same protocol was used until the blocking step, at which point embryos were blocked in FISH blocking buffer (2% blocking reagent (Roche, 11096176001) in 1x maleic acid buffer (100 mM maleic acid, 150 mM NaCl, 180 mM NaOH, 0.1% Tween)) for at least 2 h at room temperature with gentle rocking, then incubated at 4°C overnight in 1:150 anti-DIG-POD (Roche, 11207733910). The following day embryos were washed at least five times with PBST. To develop signal, embryos were incubated in 75 μl 1:75 Cy3-TSA in 1x amplification buffer (TSA Plus Cyanine 3 System, Perkin Elmer, NEL744001KT) for 30 min at room temperature in the dark. Embryos were then washed at least five times with PBST, incubated in 1:5000 DAPI (Life Technologies, D1306; stock concentration: 5 mg/ml) with agitation at room temperature for at least 1 h (or overnight at 4°C), then washed at least five times with PBST. One day after Cy3 incubation, embryos were imaged on a ZEISS Lightsheet Z.1 (see below and Figure 1—figure supplement 1E for imaging and quantification details). All FISH embryos shown in Figure 1F–Y were fertilized and fixed on the same day.

### SPIM imaging of immunofluorescence staining and fluorescence in situ hybridization

Fixed embryos were mounted in 1% low melting temperature agarose (Lonza, 50080) using a glass capillary and imaged with a ZEISS Lightsheet Z.1 selective plane illumination microscope (SPIM). The imaging chamber was filled with water, and filters and light sheets were auto-aligned prior to imaging. For fluorescence in situ hybridization (FISH) and pSmad1/5/9 immunofluorescence (IF) experiments, embryos were positioned using the DAPI signal with the animal pole pointing toward the imaging objective to produce animal views; for ventral views, embryos in the correct orientation were rotated 90°. For animal views, 50–90 z-slices with 7 μm between each slice were acquired per embryo, covering the entire blastoderm over a distance of 350–630 μm depending on embryo size. For ventral views, ~70 z-slices with 7 μm between each slice were acquired per embryo, spanning roughly half of the embryo.

For pSmad2/3 and pErk IF, embryos were mounted in the orthogonal orientation compared to pSmad1/5/9 and FISH experiments, and three lateral images were acquired per embryo: one at the brightest region, a second rotated 120°, and a third rotated 240°.

All images were acquired with dual light sheet illumination using a W Plan-Apochromat 20x objective at 0.5x zoom and the imaging conditions described below.

SPIM imaging conditions:

<table>
  <thead>
    <tr>
      <th>Experiment</th>
      <th>Signal</th>
      <th>Fluorophore</th>
      <th>Laser wavelength (nm)</th>
      <th>Laser intensity</th>
      <th>Filter</th>
      <th>Exposure (ms)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">pErk IF</td>
      <td>pErk</td>
      <td>Cy3</td>
      <td>561</td>
      <td>1.5%</td>
      <td>BP 575–615</td>
      <td>100</td>
    </tr>
    <tr>
      <td>Nuclei</td>
      <td>DAPI</td>
      <td>405</td>
      <td>1.5%</td>
      <td>BP 420–470</td>
      <td>100</td>
    </tr>
    <tr>
      <td rowspan="2">pSmad2/3 IF</td>
      <td>pSmad2/3</td>
      <td>Cy3</td>
      <td>561</td>
      <td>1%</td>
      <td>BP 575–615</td>
      <td>100</td>
    </tr>
    <tr>
      <td>Nuclei</td>
      <td>DAPI</td>
      <td>405</td>
      <td>1.1%</td>
      <td>BP 420–470</td>
      <td>100</td>
    </tr>
    <tr>
      <td rowspan="2">pSmad1/5/9 IF</td>
      <td>pSmad 1/5/9</td>
      <td>Alexa488</td>
      <td>488</td>
      <td>2%</td>
      <td>BP 505–545</td>
      <td>200</td>
    </tr>
    <tr>
      <td>Nuclei</td>
      <td>DAPI</td>
      <td>405</td>
      <td>1.3%</td>
      <td>BP 420–470</td>
      <td>200</td>
    </tr>
    <tr>
      <td rowspan="2">All FISH except SB-treated</td>
      <td>FISH</td>
      <td>Cy3</td>
      <td>561</td>
      <td>1.5%</td>
      <td>BP 575–615</td>
      <td>100</td>
    </tr>
    <tr>
      <td>Nuclei</td>
      <td>DAPI</td>
      <td>405</td>
      <td>1.5%</td>
      <td>BP 420–470</td>
      <td>100</td>
    </tr>
    <tr>
      <td rowspan="2">SB-treated FISH</td>
      <td>FISH</td>
      <td>Cy3</td>
      <td>561</td>
      <td>1%</td>
      <td>BP 575–615</td>
      <td>100</td>
    </tr>
    <tr>
      <td>Nuclei</td>
      <td>DAPI</td>
      <td>405</td>
      <td>1.1%</td>
      <td>BP 420–470</td>
      <td>100</td>
    </tr>
  </tbody>
</table>

Maximum intensity projections were generated using the software ZEN (2014 SP1, black edition) and used for the analyses described below.

### Mathematical modeling of target gene induction and decay kinetics

To estimate induction and decay of transcripts from the NanoString data (Figure 4), time-dependent pSmad1/5/9 and transcript changes were modeled mathematically. The change in the amount of endogenous (Pe) and optogenetically induced (Po) pSmad1/5/9 levels can be described by the following general differential equations:

$$
\frac{dP_{e}}{dt}=G˙(t)
$$



$$
\frac{dP_{o}}{dt}=H˙(t)
$$

The observed pSmad1/5/9 levels in uninjected embryos correspond to G(t), whereas the observed pSmad1/5/9 levels (Ps) in light-exposed Opto-BMP embryos correspond to the sum of G(t) and H(t). Therefore, the change in the amount of Ps over time can be described by:

$$
\frac{dP_{s}}{dt}=G˙(t)+H˙(t)=I˙(t)
$$

Thus, the levels of optogenetically induced pSmad1/5/9 can be calculated by subtracting the pSmad1/5/9 levels in uninjected embryos from the pSmad1/5/9 levels in light-exposed Opto-BMP embryos:

$$
It-Gt=H(t)
$$

Similarly, changes in the endogenous transcript levels (Te) and optogenetically induced transcript levels (To) over time can be described by the following general differential equations:

$$
\frac{dT_{e}}{dt}=K˙(t)
$$



$$
\frac{dT_{o}}{dt}=L˙(t)
$$

The observed transcript levels in uninjected embryos correspond to K(t), whereas the observed transcript levels (Ts) in light-exposed Opto-BMP embryos correspond to the sum of K(t) and L(t). The change in the amount of Ts over time can therefore be described by:

$$
\frac{dT_{s}}{dt}=K˙(t)+L˙(t)=M˙(t)
$$

Thus, the levels of optogenetically induced transcripts can be calculated by subtracting the transcript levels in uninjected embryos from the transcript levels in light-exposed Opto-BMP embryos:

$$
Mt-Kt=L(t)
$$

#### Modeling method 1

The NanoString transcription data was first analyzed using the simplest model of induction and decay (Figure 5):

$$
\frac{dT_{o}}{dt}=\sigmaP_{o}−\lambdaT_{o}
$$

where Po represents the optogenetically induced pSmad1/5/9 input, To the pSmad1/5/9-dependent target gene, σ the induction rate constant, and λ the decay rate constant of the induced gene. Po was obtained by fitting the measured pSmad1/5/9 immunofluorescence data H(t) (Figure 3C, Figure 5L, and Figure 3—figure supplement 1J) with a polynomial of degree five using the function polyfit in MATLAB 7.10.0 (R2010a). The induction-decay model was simulated in COMSOL Multiphysics 3.5a in a 10 μm domain (representing approximately one cell) with no-flux boundary conditions and an initial concentration To(0).

For each experiment, the combination of parameters To(0), σ, and λ was found that minimizes the sum of squared differences (SSD)

$$
SSD=\sumn(Lt_{n}-T_{o}t_{n})^{2}
$$

between the simulations of the induction-decay model To(tn) and the data L(tn) for all measured time points n.

The minimization was performed numerically using a constrained optimization algorithm (Nelder-Mead, MATLAB 7.10.0) with zero for the initial guesses of To(0), σ, and λ, and a maximum of 500 iterations. σ and λ were constrained between biologically plausible values of 0.00001/s and 0.1/s, and To(0) was bounded between −100 a.u. and 100 a.u. R2 values were calculated from the minimizing SSD (SSDmin) to assess the goodness of the fits by

$$
R^{2}=1−\frac{SSD_{min}}{\sumn(L(t_{n})−\frac{1}{n}\sumnL(t_{n}))^{2}}
$$

Fitted values for high-confidence BMP target genes, experimental repeat 1:

<table>
  <thead>
    <tr>
      <th>Target gene</th>
      <th>σ (1/s)</th>
      <th>λ (1/s)</th>
      <th>To(0) (a.u.)</th>
      <th>R2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>bambia</td>
      <td>0.000414</td>
      <td>0.000879</td>
      <td>−95.84</td>
      <td>0.9125</td>
    </tr>
    <tr>
      <td>bmp4</td>
      <td>0.000076</td>
      <td>0.000452</td>
      <td>−42.71</td>
      <td>0.7060</td>
    </tr>
    <tr>
      <td>cdx4</td>
      <td>0.000220</td>
      <td>0.000434</td>
      <td>−81.48</td>
      <td>0.6871</td>
    </tr>
    <tr>
      <td>crabp2b</td>
      <td>0.000041</td>
      <td>0.000010</td>
      <td>10.27</td>
      <td>0.0951</td>
    </tr>
    <tr>
      <td>eve1</td>
      <td>0.000233</td>
      <td>0.000514</td>
      <td>−20.49</td>
      <td>0.7132</td>
    </tr>
    <tr>
      <td>foxi1</td>
      <td>0.000371</td>
      <td>0.000835</td>
      <td>−91.10</td>
      <td>0.7821</td>
    </tr>
    <tr>
      <td>gata2a</td>
      <td>0.000105</td>
      <td>0.000336</td>
      <td>−46.01</td>
      <td>0.6056</td>
    </tr>
    <tr>
      <td>id2a</td>
      <td>0.000111</td>
      <td>0.000539</td>
      <td>−20.54</td>
      <td>0.7354</td>
    </tr>
    <tr>
      <td>klf2b</td>
      <td>0.000394</td>
      <td>0.001262</td>
      <td>5.369</td>
      <td>0.6880</td>
    </tr>
    <tr>
      <td>smad6a</td>
      <td>0.000016</td>
      <td>0.000670</td>
      <td>1.606</td>
      <td>0.1780</td>
    </tr>
    <tr>
      <td>smad7</td>
      <td>0.000116</td>
      <td>0.000765</td>
      <td>−65.54</td>
      <td>0.8043</td>
    </tr>
    <tr>
      <td>sizzled</td>
      <td>0.000222</td>
      <td>0.000605</td>
      <td>−82.09</td>
      <td>0.6470</td>
    </tr>
    <tr>
      <td>tfap2c</td>
      <td>0.000041</td>
      <td>0.000153</td>
      <td>−15.90</td>
      <td>0.1922</td>
    </tr>
    <tr>
      <td>ved</td>
      <td>0.000590</td>
      <td>0.000590</td>
      <td>−100.0</td>
      <td>0.8072</td>
    </tr>
  </tbody>
</table>

Fitted values for high-confidence BMP target genes, experimental repeat 2:

<table>
  <thead>
    <tr>
      <th>Target gene</th>
      <th>σ (1/s)</th>
      <th>λ (1/s)</th>
      <th>To(0) (a.u.)</th>
      <th>R2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>bambia</td>
      <td>0.000344</td>
      <td>0.000564</td>
      <td>90.73</td>
      <td>0.6248</td>
    </tr>
    <tr>
      <td>bmp4</td>
      <td>0.000066</td>
      <td>0.000474</td>
      <td>−17.10</td>
      <td>0.6114</td>
    </tr>
    <tr>
      <td>cdx4</td>
      <td>0.000169</td>
      <td>0.000170</td>
      <td>−26.84</td>
      <td>0.2825</td>
    </tr>
    <tr>
      <td>crabp2b</td>
      <td>0.000056</td>
      <td>0.000010</td>
      <td>−43.72</td>
      <td>0.2517</td>
    </tr>
    <tr>
      <td>eve1</td>
      <td>0.000158</td>
      <td>0.000394</td>
      <td>7.77</td>
      <td>0.6689</td>
    </tr>
    <tr>
      <td>foxi1</td>
      <td>0.000413</td>
      <td>0.001217</td>
      <td>−14.67</td>
      <td>0.7806</td>
    </tr>
    <tr>
      <td>gata2a</td>
      <td>0.000111</td>
      <td>0.000399</td>
      <td>−71.03</td>
      <td>0.5647</td>
    </tr>
    <tr>
      <td>id2a</td>
      <td>0.000141</td>
      <td>0.000522</td>
      <td>−35.84</td>
      <td>0.6967</td>
    </tr>
    <tr>
      <td>klf2b</td>
      <td>0.000708</td>
      <td>0.003101</td>
      <td>−62.70</td>
      <td>0.6394</td>
    </tr>
    <tr>
      <td>smad6a</td>
      <td>0.000029</td>
      <td>0.000340</td>
      <td>−6.326</td>
      <td>0.3140</td>
    </tr>
    <tr>
      <td>smad7</td>
      <td>0.000112</td>
      <td>0.000613</td>
      <td>−54.51</td>
      <td>0.7397</td>
    </tr>
    <tr>
      <td>sizzled</td>
      <td>0.000217</td>
      <td>0.000692</td>
      <td>−99.99</td>
      <td>0.6918</td>
    </tr>
    <tr>
      <td>tfap2c</td>
      <td>0.000056</td>
      <td>0.000160</td>
      <td>−27.15</td>
      <td>0.4203</td>
    </tr>
    <tr>
      <td>ved</td>
      <td>0.000588</td>
      <td>0.000554</td>
      <td>−100.0</td>
      <td>0.7354</td>
    </tr>
  </tbody>
</table>

Fitted values for high-confidence BMP target genes, experimental repeat 3:

<table>
  <thead>
    <tr>
      <th>Target gene</th>
      <th>σ (1/s)</th>
      <th>λ (1/s)</th>
      <th>To(0) (a.u.)</th>
      <th>R2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>bambia</td>
      <td>0.000640</td>
      <td>0.001045</td>
      <td>−99.99</td>
      <td>0.9362</td>
    </tr>
    <tr>
      <td>bmp4</td>
      <td>0.000094</td>
      <td>0.000455</td>
      <td>−73.00</td>
      <td>0.7986</td>
    </tr>
    <tr>
      <td>cdx4</td>
      <td>0.000181</td>
      <td>0.000468</td>
      <td>−99.81</td>
      <td>0.5390</td>
    </tr>
    <tr>
      <td>crabp2b</td>
      <td>0.000087</td>
      <td>0.000010</td>
      <td>−87.63</td>
      <td>0.4399</td>
    </tr>
    <tr>
      <td>eve1</td>
      <td>0.000334</td>
      <td>0.000568</td>
      <td>−100.0</td>
      <td>0.7789</td>
    </tr>
    <tr>
      <td>foxi1</td>
      <td>0.000505</td>
      <td>0.001174</td>
      <td>−6.052</td>
      <td>0.8502</td>
    </tr>
    <tr>
      <td>gata2a</td>
      <td>0.000148</td>
      <td>0.000491</td>
      <td>−65.45</td>
      <td>0.8464</td>
    </tr>
    <tr>
      <td>id2a</td>
      <td>0.000126</td>
      <td>0.000579</td>
      <td>9.476</td>
      <td>0.8000</td>
    </tr>
    <tr>
      <td>klf2b</td>
      <td>0.000505</td>
      <td>0.001407</td>
      <td>−100.0</td>
      <td>0.6530</td>
    </tr>
    <tr>
      <td>smad6a</td>
      <td>0.000051</td>
      <td>0.000563</td>
      <td>−25.92</td>
      <td>0.8935</td>
    </tr>
    <tr>
      <td>smad7</td>
      <td>0.000095</td>
      <td>0.000553</td>
      <td>−19.75</td>
      <td>0.5364</td>
    </tr>
    <tr>
      <td>sizzled</td>
      <td>0.000290</td>
      <td>0.000721</td>
      <td>−100.0</td>
      <td>0.7169</td>
    </tr>
    <tr>
      <td>tfap2c</td>
      <td>0.000045</td>
      <td>0.000378</td>
      <td>−38.42</td>
      <td>0.4709</td>
    </tr>
    <tr>
      <td>ved</td>
      <td>0.000602</td>
      <td>0.000489</td>
      <td>−100.0</td>
      <td>0.6802</td>
    </tr>
  </tbody>
</table>

Average fitted values for high-confidence BMP target genes:

<table>
  <thead>
    <tr>
      <th rowspan="2">Target gene</th>
      <th colspan="2">σ (1/s)</th>
      <th colspan="2">λ (1/s)</th>
      <th colspan="2">To(0) (a.u.)</th>
    </tr>
    <tr>
      <th>Mean</th>
      <th>Stdev</th>
      <th>Mean</th>
      <th>Stdev</th>
      <th>Mean</th>
      <th>Stdev</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>bambia</td>
      <td>0.00047</td>
      <td>0.00015</td>
      <td>0.00083</td>
      <td>0.00024</td>
      <td>−35.04</td>
      <td>108.9</td>
    </tr>
    <tr>
      <td>bmp4</td>
      <td>0.00008</td>
      <td>0.00001</td>
      <td>0.00046</td>
      <td>0.00001</td>
      <td>−44.27</td>
      <td>27.98</td>
    </tr>
    <tr>
      <td>cdx4</td>
      <td>0.00019</td>
      <td>0.00003</td>
      <td>0.00036</td>
      <td>0.00016</td>
      <td>−69.38</td>
      <td>37.96</td>
    </tr>
    <tr>
      <td>crabp2b</td>
      <td>0.00006</td>
      <td>0.00002</td>
      <td>0.00001</td>
      <td>0.00000</td>
      <td>−40.36</td>
      <td>49.04</td>
    </tr>
    <tr>
      <td>eve1</td>
      <td>0.00024</td>
      <td>0.00009</td>
      <td>0.00049</td>
      <td>0.00009</td>
      <td>−37.57</td>
      <td>55.88</td>
    </tr>
    <tr>
      <td>foxi1</td>
      <td>0.00043</td>
      <td>0.00007</td>
      <td>0.00108</td>
      <td>0.00021</td>
      <td>−37.27</td>
      <td>46.81</td>
    </tr>
    <tr>
      <td>gata2a</td>
      <td>0.00012</td>
      <td>0.00002</td>
      <td>0.00041</td>
      <td>0.00008</td>
      <td>−60.83</td>
      <td>13.13</td>
    </tr>
    <tr>
      <td>id2a</td>
      <td>0.00013</td>
      <td>0.00002</td>
      <td>0.00055</td>
      <td>0.00003</td>
      <td>−15.63</td>
      <td>23.05</td>
    </tr>
    <tr>
      <td>klf2b</td>
      <td>0.00054</td>
      <td>0.00016</td>
      <td>0.00192</td>
      <td>0.00102</td>
      <td>−52.44</td>
      <td>53.43</td>
    </tr>
    <tr>
      <td>smad6a</td>
      <td>0.00003</td>
      <td>0.00002</td>
      <td>0.00052</td>
      <td>0.00017</td>
      <td>−10.21</td>
      <td>14.17</td>
    </tr>
    <tr>
      <td>smad7</td>
      <td>0.00011</td>
      <td>0.00001</td>
      <td>0.00064</td>
      <td>0.00011</td>
      <td>−46.60</td>
      <td>23.90</td>
    </tr>
    <tr>
      <td>sizzled</td>
      <td>0.00024</td>
      <td>0.00004</td>
      <td>0.00067</td>
      <td>0.00006</td>
      <td>−94.03</td>
      <td>10.34</td>
    </tr>
    <tr>
      <td>tfap2c</td>
      <td>0.00005</td>
      <td>0.00001</td>
      <td>0.00023</td>
      <td>0.00013</td>
      <td>−27.15</td>
      <td>11.26</td>
    </tr>
    <tr>
      <td>ved</td>
      <td>0.00059</td>
      <td>0.00001</td>
      <td>0.00054</td>
      <td>0.00005</td>
      <td>−100.0</td>
      <td>0.000</td>
    </tr>
  </tbody>
</table>

#### Modeling method 2

In a second approach (Figure 5—figure supplement 1G–W), the NanoString transcription data was fitted with the analytical solutions to the differential equation system

$$
\frac{dP_{e}}{dt}=k_{1}-k_{2}P_{e}
$$



$$
\frac{dP_{o}}{dt}=k_{3}\thetat-\thetat-t_{L}-k_{2}P_{o}
$$



$$
\frac{dT_{e}}{dt}=k_{4}P_{e}-k_{5}T_{e}
$$



$$
\frac{dT_{o}}{dt}=\sigmaP_{o}−\lambdaT_{o}
$$

which describes the changes in endogenous as well as optogenetically induced pSmad1/5/9 and transcript levels based on the simplest model of induction and decay after an optogenetic pulse of length tL (i.e., 30 min = 1800 s for all experiments). k1 represents the activation rate of endogenous pSmad1/5/9, k2 the decay rate constant of pSmad1/5/9, and k3 the activation rate of optogenetically induced pSmad1/5/9. Optogenetic switch-like activation was modeled with the Heaviside step function θ. k4 and k5 represent the activation rate and decay rate constants of endogenously induced BMP-dependent transcripts, and σ and λ are the induction rate and decay rate constants of the induced gene.

The analytical solutions to this equation system are:

$$
P_{e}t=e^{-k_{2}t}\delta_{P_{e}}+\frac{k_{1}}{k_{2}}
$$



$$
P_{o}(t)=\frac{1}{k_{2}}(k_{3}(\theta(t_{L})−\theta(t_{L}−t))e^{−k_{2}(t−t_{L})}+k_{3}\theta(t_{L}−t)+(−k_{3}\theta(t)−\theta(t_{L})k_{3}+\delta_{P_{o}}k_{2}+k_{3})e^{−k_{2}t}+k_{3}(\theta(t)−1))
$$



$$
T_{e}=\frac{1}{k_{2}k_{5}(k_{2}−k_{5})}(k_{2}k_{5}(\delta_{P_{e}}k_{4}+\delta_{T_{e}}k_{2}−\delta_{T_{e}}k_{5})e^{−k_{5}t}+(−k_{2}k_{5}\delta_{P_{e}}e^{−k_{2}t}+k_{1}(k_{2}−k_{5}))k_{4})
$$



$$
T_{o}=\frac{1}{(k_{2}−\lambda)k_{2}\lambda}(−\sigmak_{3}\lambda(\theta(t_{L})−\theta(t_{L}−t))e^{−k_{2}(t−t_{L})}+ \sigmak_{2}k_{3}(\theta(t_{L})−\theta(t_{L}−t))e^{−\lambda(t−t_{L})}+\sigmak_{3}(k_{2}−\lambda)\theta(t_{L}−t)−k_{2}(\theta(t_{L})k_{3}\sigma+\sigmak_{3}\theta(t)+(−\delta_{P_{o}}\lambda−k_{3})\sigma−\lambda\delta_{T_{o}}(k_{2}−\lambda))e^{−\lambdat}+\sigma(\lambda(\theta(t_{L})k_{3}+k_{3}\theta(t)−\delta_{P_{o}}k_{2}−k_{3})e^{−k_{2}t}+k_{3}(\theta(t)−1)(k_{2}−\lambda)))
$$

with

$$
P_{e}0=\delta_{P_{e}}+\frac{k_{1}}{k_{2}}
$$



$$
P_{o}0=\delta_{P_{o}}
$$



$$
T_{e}0=\delta_{T_{e}}+\frac{k_{1}k_{4}}{k_{2}k_{5}}
$$



$$
T_{o}0=\delta_{T_{o}}
$$

The pSmad1/5/9 data was fitted with the computer algebra system Maple (Waterloo Maple Inc) using the function LSSolve to minimize the difference between the pSmad1/5/9 data in uninjected embryos and Pe(t), as well as the difference between the pSmad1/5/9 data in light-exposed Opto-BMP embryos and Pe(t) + Po(t) with the initial guesses $\delta_{P_{e}}=0 a.u.$, $\delta_{P_{o}}=0 a.u.$, $k_{1}=0/s$, $k_{2}=0.00167/s$, $k_{3}=0/s$, $k_{4}=00167/s$ and a maximum of 20000 iterations and an optimality tolerance of 0.3981071706 × 10−14. The best fitting parameters $\delta_{P_{e}}=-76.19a.u$, $\delta_{P_{o}}=264.1a.u.,$ $k_{1}=0.1429 a.u./s,$ $k_{2}=0.000900/s,$ and $k_{3}=0.954a.u./s$ were then used for the simulation of the gene induction dynamics in the NanoString data.

The NanoString data was fitted in Maple using the function LSSolve to simultaneously minimize the difference between the NanoString data in uninjected embryos and Te(t), as well as the difference between the NanoString data in light-exposed Opto-BMP embryos and Te(t) + To(t) with the initial guesses $\delta_{T_{e}}=0 a.u.$, $\delta_{T_{o}}=0 a.u.$, $k_{4}=0/s$, $k_{5}=0.00167/s$, $\sigma=0/s$, $\lambda=0.00167/s$ and a maximum of 10000 iterations and an optimality tolerance of 0.3981071706 × 10−14.

Fitted values for high-confidence BMP target genes:

<table>
  <thead>
    <tr>
      <th>Target gene</th>
      <th>σ (1/s)</th>
      <th>λ (1/s)</th>
      <th>δTe (a.u.)</th>
      <th>δTo (a.u.)</th>
      <th>R2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>bambia</td>
      <td>0.000327</td>
      <td>0.000671</td>
      <td>520.4</td>
      <td>16.01</td>
      <td>0.7509</td>
    </tr>
    <tr>
      <td>bmp4</td>
      <td>0.000070</td>
      <td>0.000362</td>
      <td>171.2</td>
      <td>−41.52</td>
      <td>0.7912</td>
    </tr>
    <tr>
      <td>cdx4</td>
      <td>0.000238</td>
      <td>0.000550</td>
      <td>−1331</td>
      <td>−29.22</td>
      <td>0.8682</td>
    </tr>
    <tr>
      <td>crabp2b</td>
      <td>0.000048</td>
      <td>−0.000191</td>
      <td>−310.9</td>
      <td>−40.27</td>
      <td>0.8111</td>
    </tr>
    <tr>
      <td>eve1</td>
      <td>0.000177</td>
      <td>0.000313</td>
      <td>950.7</td>
      <td>−52.74</td>
      <td>0.8599</td>
    </tr>
    <tr>
      <td>foxi1</td>
      <td>0.000401</td>
      <td>0.000094</td>
      <td>47.34</td>
      <td>−72.26</td>
      <td>0.5592</td>
    </tr>
    <tr>
      <td>gata2a</td>
      <td>0.000144</td>
      <td>0.000427</td>
      <td>62.39</td>
      <td>−77.72</td>
      <td>0.4272</td>
    </tr>
    <tr>
      <td>id2a</td>
      <td>0.000143</td>
      <td>0.000449</td>
      <td>231.3</td>
      <td>−21.14</td>
      <td>0.7586</td>
    </tr>
    <tr>
      <td>klf2b</td>
      <td>0.000419</td>
      <td>0.001114</td>
      <td>9.959</td>
      <td>−97.86</td>
      <td>0.5082</td>
    </tr>
    <tr>
      <td>smad6a</td>
      <td>0.000030</td>
      <td>0.000318</td>
      <td>49.62</td>
      <td>−15.67</td>
      <td>0.3307</td>
    </tr>
    <tr>
      <td>smad7</td>
      <td>0.000125</td>
      <td>0.000626</td>
      <td>122.9</td>
      <td>−54.50</td>
      <td>0.7043</td>
    </tr>
    <tr>
      <td>sizzled</td>
      <td>0.000274</td>
      <td>0.000758</td>
      <td>238.9</td>
      <td>−120.7</td>
      <td>0.5116</td>
    </tr>
    <tr>
      <td>tfap2c</td>
      <td>0.000062</td>
      <td>0.000316</td>
      <td>44.54</td>
      <td>−31.75</td>
      <td>0.1597</td>
    </tr>
    <tr>
      <td>ved</td>
      <td>0.000732</td>
      <td>0.000531</td>
      <td>1200</td>
      <td>−403.0</td>
      <td>0.8063</td>
    </tr>
  </tbody>
</table>

### Inhibition of Nodal and FGF signaling with small molecule inhibitors

The Nodal inhibitor SB-505124 (Sigma, S4696-5MG) (Soh et al., 2020; Almuedo-Castillo et al., 2018; Rogers et al., 2017; van Boxtel et al., 2015; Vogt et al., 2011; Fan et al., 2007; Hagos and Dougan, 2007; Hagos et al., 2007; DaCosta Byfield et al., 2004) and the FGF inhibitor SU-5402 (Sigma SML0443-5MG) (van Boxtel et al., 2015; Poulain et al., 2006; Londin et al., 2005; Fürthauer et al., 2004; Kudoh et al., 2004; Mathieu et al., 2004; Mohammadi et al., 1997) were diluted to 10 mM in DMSO (Roth, A994.2), aliquoted, and stored at −20°C. Aliquots were thawed the same day that experiments were carried out and were not re-used. 10 mM stocks of SB-505124 and SU-5402 were diluted to 50 and 10 μM, respectively, in embryo medium the day of each experiment. 5 ml diluted inhibitors were then dispensed into each well of agarose-coated (Sigma, A9539) 6-well plates (Greiner Bio-One, 657160), and plates were incubated at 28°C at least 30 min before embryos were added.

### Quantification of pSmad1/5/9 immunofluorescence staining and fluorescence in situ hybridization

To measure spatial intensity profiles along the dorsal-ventral axis (Figure 1—figure supplement 1E) from pSmad1/5/9 immunofluorescence experiments (IF) (Figures 1D–E and 7A–E, Figure 7—figure supplement 1A–J’, and Figure 7—figure supplement 2A–K) and BMP target gene fluorescence in situ hybridization (FISH) (Figure 1P–Y, Figure 7F–J, and Figure 7—figure supplement 3), maximum intensity projections of animal views were manually rotated in Fiji (Schindelin et al., 2012) with ventral to the left (brightest signal) and dorsal to the right (dimmest signal; for the very early pSmad1/5/9 images prior to clear onset of BMP signaling, embryos were oriented with the brightest side on the left and the dimmest on the right where obvious, but correspondence with ventral-dorsal is not clear in those early cases). A polygonal region of interest (ROI) was then manually drawn around the embryo and used to create a mask in order to remove image background (for FISH experiments, the Cy3 signal was used to draw the mask; for IF experiments the DAPI signal was used). The average pixel intensity in each column of pixels from ventral to dorsal was then acquired (pixel area: 0.46 μm × 0.46 μm). For genes that are restricted to the margin (cdx4 and eve1), a second manually positioned circular ROI was used to exclude the non-margin region of the embryo (Figure 1—figure supplement 1E).

For FISH experiments, non-probe-exposed control embryos for background subtraction were imaged and intensity profiles acquired as described above. The orientation of these background subtraction embryos was random. Images for background subtraction controls were acquired in the same imaging session as experimental FISH images.

After intensity profiles were acquired, absolute distance was converted into percent embryo length to account for embryo-to-embryo variability in size, and intensity measurements were averaged into bins of 0.5% embryo length using an automated routine (0 < bin 1 < 0.5%, 0.5 < bin 2 < 1%, etc.).

For FISH experiments, the average intensity at each position in all 10 non-probe-exposed background embryos was calculated. This spatial background average was subtracted from each experimental FISH raw intensity profile, and data from the first and last 5% embryo length was excluded because the averages at the most ventral and dorsal regions are composed of relatively few pixels and are therefore less reliable.

The profiles of individual embryos were normalized following the procedure in Gregor et al., 2007 using the model

$$
I_{n}(x)=A_{n}c-x+b_{n}
$$

which relates the mean intensity profile $c-x$ of all data points for a given target gene to the intensity profile $I_{n}(x)$ for an embryo n through the embryo-specific proportionality constant $A_{n}$ and the nonspecific background $b_{n}$. $A_{n}$ and $b_{n}$ were determined by minimizing the objective function

$$
\sumi(I_{n}(x_{i})−(A_{n}c−(x_{i})+b_{n}))^{2}
$$

for the data points at all positions xi with the Nelder-Mead algorithm using the function fminsearch in MATLAB 7.10.0, the initial guesses 1 and 0 for $A_{n}$ and $b_{n}$, a maximum of 10000 function evaluations, and a maximum of 5000 iterations. For display, each average profile was then divided by its maximum intensity (Figure 1P-Y, Figure 7F-J, and Figure 7—figure supplement 3).

The Gaussian function $Ae^{-\frac{x-\mu^{2}}{ς}}$ was fitted to each profile using a constrained Nelder-Mead algorithm in MATLAB 7.10.0 with a maximum of 10000 function evaluations, a maximum of 5000 iterations, the initial guesses 300, 20, and 10000, the lower bounds 300, -50, and 100, and the upper bounds 100000, 50, and 100000 for A, µ, and ς, respectively. Gene expression range was defined as $r=\mu+2\sqrt{ς/2}$. The resulting ranges from 9-10 embryos were averaged to define each gene’s mean range.

For pSmad1/5/9 IF spatial quantification experiments, the average image background intensity was determined for each image using a small ROI in the corner outside of the embryo, and subtracted from each IF raw intensity profile. Since the averages at the most ventral and dorsal regions are composed of relatively few pixels and are therefore less reliable, data from the first and last 5% embryo length was not considered. The mean of the dorsal-most 5% at 2.75 hpf was then subtracted from all profiles. These profiles were then normalized as described above for the FISH data, assuming embryo-specific constant nonspecific background and proportionality constants that relate immunofluorescent staining intensity to protein concentration.

Number of embryos assessed in spatial quantification experiments:

<table>
  <thead>
    <tr>
      <th colspan="2">Experiment</th>
      <th>Fig.</th>
      <th>Number of embryos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">FISH</td>
      <td>All except apoc1l in bmp-overexpressing embryos</td>
      <td>1P-Y, 7 F-J, 7.3</td>
      <td>10</td>
    </tr>
    <tr>
      <td>apoc1l in bmp-overexpressing embryos</td>
      <td>7J, 7.3A</td>
      <td>9</td>
    </tr>
    <tr>
      <td rowspan="5">pSmad 1/5/9 IF</td>
      <td>Time course in untreated and SU-5402/SB-505124-treated embryos</td>
      <td>1E,7A, 7.2A-K</td>
      <td>8–9</td>
    </tr>
    <tr>
      <td>Untreated and bmp-overexpressing embryos</td>
      <td>7E, 7.1A-A’</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Untreated and SU-5420-treated embryos</td>
      <td>7B, 7.1D-D’</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Untreated and SB-505124-treated embryos</td>
      <td>7C, 7.1 F-F’</td>
      <td>9–10</td>
    </tr>
    <tr>
      <td>Untreated and SU-5402/SB-505124-treated embryos</td>
      <td>7D, 7.1 H-H’</td>
      <td>10</td>
    </tr>
  </tbody>
</table>

To quantify total pSmad1/5/9 IF intensity (Figures 3C–E and 6B, and Figure 3—figure supplement 1I,J), an ROI was manually drawn around the embryo in Fiji based on DAPI signal and used to create a mask in order to remove image background as described above. The average intensity within the ROI was then calculated.

For experiments shown in Figure 3C–D and Figure 3—figure supplement 1I, image background intensity was measured using a small ROI in the corner of each image outside of the embryo. The average image background was then subtracted from the embryo intensity measurements to generate background-subtracted intensities.

For shield-stage experiments shown in Figure 3C,E, Figure 5L, Figure 6B, and Figure 3—figure supplement 1J, the average intensity within a small ROI on the dorsal side was measured in uninjected embryos; for each time point, these values were averaged and subtracted from the embryo intensity measurements to generate background-subtracted intensities.

Number of embryos assessed in total pSmad1/5/9 IF quantification time course experiments:

<table>
  <thead>
    <tr>
      <th>Experiment</th>
      <th>Fig.</th>
      <th>Number of embryos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>High-stage BMP signaling pulse</td>
      <td>3C, 3.1I</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Shield-stage BMP signaling pulse</td>
      <td>3C, 5L, 3.1J</td>
      <td>5</td>
    </tr>
    <tr>
      <td rowspan="2">Low- and high-amplitude BMP signaling pulse</td>
      <td rowspan="2">6B</td>
      <td>5 uninjected</td>
    </tr>
    <tr>
      <td>7 Opto-BMP</td>
    </tr>
  </tbody>
</table>

### NanoString RNA quantification

For the NanoString time course experiment in untreated (Figure 2) and FGF/Nodal-inhibitor-treated embryos (Figure 7—figure supplement 2L-ZA), embryos from wild type TE incrosses were collected ~15 min after mating commenced. Embryos were incubated at 28°C, dechorionated using Pronase (Roche, 11459643001) at ~1.5 hpf, and sorted into 10 agarose-coated 6-well plates, one plate per time point. Each plate had one well containing embryo medium and one well containing FGF/Nodal inhibitor. To keep temperature and therefore development steady, plates were only removed from the 28°C incubator immediately prior to embryo collection. Every 30 min from 2.75 to 7.25 hpf, treated and untreated embryos were snap-frozen in liquid nitrogen.

For NanoString experiments quantifying responses to BMP signaling pulses using Opto-BMP (Figures 4, 5 and 6, Figure 5—figure supplement 1J–W, and Figure 6—figure supplement 1), embryos from TE incrosses were dechorionated using Pronase and injected at the one-cell stage with 5.2 pg opto-Alk3 + 5.2 pg opto-Alk8 + 8.9 pg opto-BMPR2a mRNA (Figure 3—figure supplement 1A). Control siblings were left uninjected, and embryos were sorted into agarose-coated 6-well plates and incubated at 28°C. 70–90 min post-fertilization at the 4–16 cell stage, unfertilized and damaged embryos were removed, and plates were individually wrapped in aluminum foil and incubated at 28°C. At the appropriate time, individual plates were transferred to a small 28°C incubator containing the LED array, exposed to light for the appropriate duration, and embryos were either snap-frozen in liquid nitrogen immediately (e.g., for the 10 min during exposure time point), or re-wrapped in aluminum foil and returned to 28°C incubation in the dark (e.g., for the 80 min post-exposure time point).

RNA was prepared as described for the RNA-sequencing experiment. 30 μl aliquots at 20 ng/μl were provided to Proteros GmbH (Planegg-Martinsried, Germany) for analysis using a custom-designed NanoString nCounter Elements TagSet with probes targeting high-confidence BMP target genes identified by RNA-sequencing, and housekeeping genes for normalization. Samples were measured using an nCounter SPRINT according to the standard protocol with a 24–30 h hybridization length.

nSolver 4.0 software (https://www.nanostring.com/products/analysis-software/nsolver) was used to subtract background and normalize the RNA count data using the geometric means of the positive spike-in controls and the housekeeping genes eef1a1l1 and act2b, respectively. Lanes that failed quality control were repeated.

Number of embryos assessed in NanoString experiments:

<table>
  <thead>
    <tr>
      <th colspan="2">Experiment</th>
      <th>Fig.</th>
      <th>Number of embryos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Time course from 2.75 to 7.25 hpf</td>
      <td>Untreated embryos</td>
      <td>2, 7.2L-ZA</td>
      <td>25</td>
    </tr>
    <tr>
      <td>SU-5402/SB-505124-treated embryos</td>
      <td>7.2L-ZA</td>
      <td>20–25</td>
    </tr>
    <tr>
      <td colspan="2">High-stage BMP signaling pulse</td>
      <td>4</td>
      <td>21–25</td>
    </tr>
    <tr>
      <td colspan="2">Shield-stage BMP signaling pulse</td>
      <td>4, 5, 5.1I-W</td>
      <td>19–25</td>
    </tr>
    <tr>
      <td colspan="2">Low- and high-amplitude BMP signaling pulse</td>
      <td>6 C-F, 6.1</td>
      <td>25</td>
    </tr>
  </tbody>
</table>

Each of the experiments described in the table above was repeated three times.

For experiments in which transcriptional responses to BMP signaling pulses are assessed (Figures 4, 5 and 6C–F, and Figure 6—figure supplement 1), it is necessary to determine changes in transcript levels compared to uninduced embryos. Because each of the three sets of Opto-BMP embryos had uninjected control siblings collected at the same time, average induction was calculated by first subtracting the uninjected transcript count from its corresponding injected sibling count, then by averaging the three subtracted counts (also see the section Mathematical modeling of target gene induction and decay kinetics above for a formal description of this procedure).

### Calculation of spatial coefficients of variation

The spatial coefficient of variation (Figure 7N) for each condition (untreated, bmp-overexpressing, +SB-505124, + SU-5402, and +SB-505124 and SU-5402) was calculated as follows: First, at each position x, the average normalized intensity

$$
\mu(x)=\frac{1}{n}\sumi=1nI_{i}(x)
$$

and standard deviation

$$
\sigmax=\sqrt{\frac{1}{n-1}\sumi=1nI_{i}x-\mu(x)^{2}}
$$

for all n genes quantified by FISH were determined (Figure 7F–J). Next, the standard deviation was divided by the average normalized intensity at that position

$$
c_{v}(x)=\frac{\sigma(x)}{\mu(x)}
$$

This was repeated for every position along the dorsal-ventral axis for all five conditions to calculate the spatial coefficients of variation for the 10 measured genes.

### Statistical analyses

In the following experiments, significance was defined as a p-value≤0.05 using an unpaired two-tailed Student’s t-test assuming equal variance in Excel.

To determine how light exposure at different developmental stages affects BMP signaling in Opto-BMP embryos, total pSmad1/5/9 immunofluorescence intensity was quantified in uninjected and Opto-BMP-injected embryos exposed to light at high (3.5–4 hpf) or shield (6.75–7.25 hpf) stage (Figure 3C–D and Figure 3—figure supplement 1I,J).

Early and late light exposure, Opto-BMP versus uninjected p-values (Figure 3C–D and Figure 3—figure supplement 1I,J):

<table>
  <thead>
    <tr>
      <th>Time post-exposure (min)</th>
      <th>High stage (early)</th>
      <th>Shield stage (late)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>−30</td>
      <td>0.065</td>
      <td>0.003</td>
    </tr>
    <tr>
      <td>−20</td>
      <td>0.029</td>
      <td>1.422 × 10−5</td>
    </tr>
    <tr>
      <td>−10</td>
      <td>0.001</td>
      <td>7.732 × 10−7</td>
    </tr>
    <tr>
      <td>0</td>
      <td>1.189 × 10−5</td>
      <td>1.610 × 10−6</td>
    </tr>
    <tr>
      <td>10</td>
      <td>2.052 × 10−6</td>
      <td>1.181 × 10−5</td>
    </tr>
    <tr>
      <td>20</td>
      <td>0.002</td>
      <td>6.800 × 10−6</td>
    </tr>
    <tr>
      <td>35</td>
      <td>0.077</td>
      <td>0.407</td>
    </tr>
    <tr>
      <td>55</td>
      <td>0.021</td>
      <td>0.016</td>
    </tr>
    <tr>
      <td>80</td>
      <td>0.455</td>
      <td>0.025</td>
    </tr>
    <tr>
      <td>110</td>
      <td>0.948</td>
      <td>0.135</td>
    </tr>
  </tbody>
</table>

To determine how different light intensities affect BMP signaling in Opto-BMP embryos, total pSmad1/5/9 immunofluorescence intensity was quantified in uninjected and Opto-BMP-injected embryos exposed to low (70 lux) or high (3900 lux) intensity light for 10 or 20 min (Figure 6B).

Low- and high-intensity light, Opto-BMP versus uninjected p-values (Figure 6B):

<table>
  <thead>
    <tr>
      <th>Time post-exposure (min)</th>
      <th>70 lux, 10 min</th>
      <th>3900 lux, 10 min</th>
      <th>70 lux, 20 min</th>
      <th>3900 lux, 20 min</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0.419</td>
      <td>0.020</td>
      <td>0.013</td>
      <td>0.975</td>
    </tr>
    <tr>
      <td>5</td>
      <td>0.782</td>
      <td>0.782</td>
      <td>ND</td>
      <td>ND</td>
    </tr>
    <tr>
      <td>10</td>
      <td>0.328</td>
      <td>0.003</td>
      <td>0.493</td>
      <td>0.001</td>
    </tr>
    <tr>
      <td>15</td>
      <td>0.001</td>
      <td>0.0004</td>
      <td>ND</td>
      <td>ND</td>
    </tr>
    <tr>
      <td>20</td>
      <td>0.097</td>
      <td>0.0004</td>
      <td>0.009</td>
      <td>0.001</td>
    </tr>
    <tr>
      <td>30</td>
      <td>0.583</td>
      <td>0.012</td>
      <td>0.0002</td>
      <td>0.00003</td>
    </tr>
    <tr>
      <td>40</td>
      <td>0.059</td>
      <td>0.018</td>
      <td>0.367</td>
      <td>8.656 × 10−7</td>
    </tr>
    <tr>
      <td>50</td>
      <td>ND</td>
      <td>ND</td>
      <td>0.367</td>
      <td>0.729</td>
    </tr>
  </tbody>
</table>

To determine whether BMP target gene expression domain boundaries differ significantly in untreated embryos, range was defined in individual embryos as described in the section Quantification of pSmad1/5/9 immunofluorescence staining and fluorescence in situ hybridization. Ranges were then averaged.

BMP target gene range comparison p-values (Figure 1P–Y):

<table>
  <thead>
    <tr>
      <th></th>
      <th>bambia</th>
      <th>cdx4</th>
      <th>eve1</th>
      <th>foxi1</th>
      <th>gata2a</th>
      <th>klf2b</th>
      <th>sizzled</th>
      <th>tfap2c</th>
      <th>ved</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>apoc1l</td>
      <td>0.0122</td>
      <td>0.136</td>
      <td>3.27 × 10−4</td>
      <td>9.47 × 10−5</td>
      <td>0.682</td>
      <td>0.371</td>
      <td>1.06 × 10−6</td>
      <td>0.003</td>
      <td>6.79 × 10−5</td>
    </tr>
    <tr>
      <td>bambia</td>
      <td></td>
      <td>4.44 × 10−6</td>
      <td>1.06 × 10−5</td>
      <td>1.2 × 10−9</td>
      <td>0.129</td>
      <td>9.95 × 10−5</td>
      <td>1.12 × 10−18</td>
      <td>2.70 × 10−5</td>
      <td>1.58 × 10−8</td>
    </tr>
    <tr>
      <td>cdx4</td>
      <td></td>
      <td></td>
      <td>3.38 × 10−8</td>
      <td>2.70 × 10−11</td>
      <td>0.511</td>
      <td>0.138</td>
      <td>3.67 × 10−17</td>
      <td>5.59 × 10−9</td>
      <td>2.15 × 10−10</td>
    </tr>
    <tr>
      <td>eve1</td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.182</td>
      <td>0.010</td>
      <td>2.64 × 10−7</td>
      <td>5.40 × 10−8</td>
      <td>0.001</td>
      <td>0.081</td>
    </tr>
    <tr>
      <td>foxi1</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.004</td>
      <td>5.70 × 10−9</td>
      <td>1.66 × 10−9</td>
      <td>2.09 × 10−7</td>
      <td>0.466</td>
    </tr>
    <tr>
      <td>gata2a</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.838</td>
      <td>1.07 × 10−4</td>
      <td>0.049</td>
      <td>0.003</td>
    </tr>
    <tr>
      <td>klf2b</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.26 × 10−12</td>
      <td>2.01 × 10–6</td>
      <td>8.46 × 10−9</td>
    </tr>
    <tr>
      <td>sizzled</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>7.92 × 10−18</td>
      <td>5.19 × 10−7</td>
    </tr>
    <tr>
      <td>tfap2c</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.33 × 10−6</td>
    </tr>
  </tbody>
</table>

The shape of the temporal BMP target gene expression profiles assessed by NanoString in untreated and SU-5402/SB-505124-treated embryos can be well approximated by the modified cumulative distribution function of the normal distribution

$$
\frac{1}{2}A1+erf⁡\frac{x-ν}{\tau\sqrt{2}}+b
$$

which was used for regression analysis using a constrained Nelder-Mead algorithm in MATLAB 7.10.0 with a maximum of 10000 function evaluations, a maximum of 5000 iterations, the initial guesses 1000, 5 h, 1 h, and 100, the lower bounds 100, 3 h, 0.05 h, and 0, and the upper bounds 10000, 7 h, 3 h, and 1000 for A, $ν$, $\tau$, and b, respectively. The activation time of each BMP target gene was defined as the average time point at which the curves reached about two mean average deviations (i.e., $1.5∙\tau$) from the inflection point $ν$ (Figure 2 and Figure 7—figure supplement 2L-Y). id2a (Chong et al., 2005) and smad6a (White et al., 2017) were excluded from this analysis because they are maternally contributed.

To determine whether FGF/Nodal loss affects the timing of gene activation, activation times in untreated versus SU-5402/SB-505124-treated samples were compared (Figure 7—figure supplement 2L–Y).

SU-5402/SB-505124-treated versus untreated activation time p-values (Figure 7—figure supplement 2L–Y):

<table>
  <thead>
    <tr>
      <th>bambia</th>
      <th>bmp4</th>
      <th>cdx4</th>
      <th>crabp 2b</th>
      <th>eve1</th>
      <th>foxi1</th>
      <th>gata 2a</th>
      <th>klf2b</th>
      <th>smad7</th>
      <th>sizzled</th>
      <th>tfap2c</th>
      <th>ved</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.446</td>
      <td>0.248</td>
      <td>0.551</td>
      <td>0.346</td>
      <td>0.450</td>
      <td>0.184</td>
      <td>0.043</td>
      <td>0.760</td>
      <td>0.571</td>
      <td>0.201</td>
      <td>0.082</td>
      <td>0.333</td>
    </tr>
  </tbody>
</table>

To identify differences in BMP target gene expression in the absence of FGF/Nodal signaling, transcript counts from SU-5402/SB-505124-treated embryos were compared to counts from untreated embryos (Figure 7—figure supplement 2L–Y).

SU-5402/SB-505124-treated versus untreated p-values (Figure 7—figure supplement 2L–Y):

<table>
  <thead>
    <tr>
      <th>hpf</th>
      <th>bambia</th>
      <th>bmp4</th>
      <th>cdx4</th>
      <th>crabp 2b</th>
      <th>eve1</th>
      <th>foxi1</th>
      <th>gata 2a</th>
      <th>id2a</th>
      <th>klf2b</th>
      <th>smad 6a</th>
      <th>smad7</th>
      <th>sizzled</th>
      <th>tfap 2c</th>
      <th>ved</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2.75</td>
      <td>0.796</td>
      <td>0.677</td>
      <td>0.770</td>
      <td>0.389</td>
      <td>0.835</td>
      <td>0.654</td>
      <td>0.675</td>
      <td>0.961</td>
      <td>0.652</td>
      <td>0.578</td>
      <td>0.826</td>
      <td>0.824</td>
      <td>0.897</td>
      <td>0.968</td>
    </tr>
    <tr>
      <td>3.25</td>
      <td>0.757</td>
      <td>0.590</td>
      <td>0.855</td>
      <td>0.905</td>
      <td>0.573</td>
      <td>0.790</td>
      <td>0.386</td>
      <td>0.946</td>
      <td>0.341</td>
      <td>0.918</td>
      <td>0.704</td>
      <td>0.497</td>
      <td>0.514</td>
      <td>0.682</td>
    </tr>
    <tr>
      <td>3.75</td>
      <td>0.695</td>
      <td>0.749</td>
      <td>0.941</td>
      <td>0.951</td>
      <td>0.593</td>
      <td>0.791</td>
      <td>0.804</td>
      <td>0.700</td>
      <td>0.729</td>
      <td>0.159</td>
      <td>0.816</td>
      <td>0.854</td>
      <td>0.245</td>
      <td>0.818</td>
    </tr>
    <tr>
      <td>4.25</td>
      <td>0.565</td>
      <td>0.954</td>
      <td>0.650</td>
      <td>0.434</td>
      <td>0.561</td>
      <td>0.661</td>
      <td>0.590</td>
      <td>0.720</td>
      <td>0.855</td>
      <td>0.785</td>
      <td>0.358</td>
      <td>0.258</td>
      <td>0.521</td>
      <td>0.751</td>
    </tr>
    <tr>
      <td>4.75</td>
      <td>0.988</td>
      <td>0.943</td>
      <td>0.996</td>
      <td>0.655</td>
      <td>0.645</td>
      <td>0.751</td>
      <td>0.919</td>
      <td>0.965</td>
      <td>0.820</td>
      <td>0.460</td>
      <td>0.643</td>
      <td>0.224</td>
      <td>0.630</td>
      <td>0.947</td>
    </tr>
    <tr>
      <td>5.25</td>
      <td>0.910</td>
      <td>0.477</td>
      <td>0.554</td>
      <td>0.996</td>
      <td>0.927</td>
      <td>0.874</td>
      <td>0.759</td>
      <td>0.733</td>
      <td>0.877</td>
      <td>0.511</td>
      <td>0.561</td>
      <td>0.095</td>
      <td>0.489</td>
      <td>0.800</td>
    </tr>
    <tr>
      <td>5.75</td>
      <td>0.877</td>
      <td>0.323</td>
      <td>0.622</td>
      <td>0.405</td>
      <td>0.237</td>
      <td>0.324</td>
      <td>0.083</td>
      <td>0.589</td>
      <td>0.108</td>
      <td>0.739</td>
      <td>0.615</td>
      <td>0.122</td>
      <td>0.319</td>
      <td>0.926</td>
    </tr>
    <tr>
      <td>6.25</td>
      <td>0.443</td>
      <td>0.509</td>
      <td>0.731</td>
      <td>0.399</td>
      <td>0.450</td>
      <td>0.149</td>
      <td>0.091</td>
      <td>0.767</td>
      <td>0.085</td>
      <td>0.938</td>
      <td>0.966</td>
      <td>0.077</td>
      <td>0.105</td>
      <td>0.483</td>
    </tr>
    <tr>
      <td>6.75</td>
      <td>0.493</td>
      <td>0.596</td>
      <td>0.713</td>
      <td>0.325</td>
      <td>0.723</td>
      <td>0.041</td>
      <td>0.038</td>
      <td>0.163</td>
      <td>0.022</td>
      <td>0.415</td>
      <td>0.120</td>
      <td>0.006</td>
      <td>0.023</td>
      <td>0.103</td>
    </tr>
    <tr>
      <td>7.25</td>
      <td>0.346</td>
      <td>0.078</td>
      <td>0.657</td>
      <td>0.262</td>
      <td>0.874</td>
      <td>0.021</td>
      <td>0.014</td>
      <td>0.256</td>
      <td>0.011</td>
      <td>0.067</td>
      <td>0.055</td>
      <td>0.008</td>
      <td>0.019</td>
      <td>0.020</td>
    </tr>
  </tbody>
</table>

For experiments in which transcriptional responses to BMP signaling pulses at high or shield stage were measured using NanoString (Figures 4 and 5M–Z), mRNA counts in Opto-BMP-injected embryos were compared to uninjected embryos.

High-stage BMP signaling pulse, Opto-BMP versus uninjected p-values (Figure 4):

<table>
  <thead>
    <tr>
      <th>Time post-exposure (min)</th>
      <th>bambia</th>
      <th>bmp4</th>
      <th>cdx4</th>
      <th>crabp2b</th>
      <th>eve1</th>
      <th>foxi1</th>
      <th>gata 2a</th>
      <th>id2a</th>
      <th>klf2b</th>
      <th>smad6a</th>
      <th>smad7</th>
      <th>sizzled</th>
      <th>tfap2c</th>
      <th>ved</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>−30</td>
      <td>0.274</td>
      <td>0.381</td>
      <td>0.279</td>
      <td>0.362</td>
      <td>0.428</td>
      <td>0.610</td>
      <td>0.401</td>
      <td>0.315</td>
      <td>0.573</td>
      <td>0.173</td>
      <td>0.983</td>
      <td>0.295</td>
      <td>0.283</td>
      <td>0.312</td>
    </tr>
    <tr>
      <td>−20</td>
      <td>0.270</td>
      <td>0.419</td>
      <td>0.225</td>
      <td>0.144</td>
      <td>0.386</td>
      <td>0.051</td>
      <td>0.354</td>
      <td>0.275</td>
      <td>0.364</td>
      <td>0.301</td>
      <td>0.897</td>
      <td>0.456</td>
      <td>0.171</td>
      <td>0.124</td>
    </tr>
    <tr>
      <td>−10</td>
      <td>0.232</td>
      <td>0.273</td>
      <td>0.799</td>
      <td>0.501</td>
      <td>0.563</td>
      <td>0.019</td>
      <td>0.874</td>
      <td>0.570</td>
      <td>0.359</td>
      <td>0.398</td>
      <td>0.711</td>
      <td>0.249</td>
      <td>0.900</td>
      <td>0.527</td>
    </tr>
    <tr>
      <td>0</td>
      <td>0.019</td>
      <td>0.181</td>
      <td>0.053</td>
      <td>0.483</td>
      <td>0.004</td>
      <td>0.071</td>
      <td>0.152</td>
      <td>0.459</td>
      <td>0.053</td>
      <td>0.732</td>
      <td>0.167</td>
      <td>0.016</td>
      <td>0.001</td>
      <td>0.169</td>
    </tr>
    <tr>
      <td>10</td>
      <td>0.005</td>
      <td>0.539</td>
      <td>0.760</td>
      <td>0.136</td>
      <td>0.031</td>
      <td>0.002</td>
      <td>0.168</td>
      <td>0.040</td>
      <td>0.043</td>
      <td>0.793</td>
      <td>0.124</td>
      <td>0.0001</td>
      <td>0.012</td>
      <td>0.017</td>
    </tr>
    <tr>
      <td>20</td>
      <td>0.002</td>
      <td>0.034</td>
      <td>0.190</td>
      <td>0.902</td>
      <td>0.002</td>
      <td>0.083</td>
      <td>0.021</td>
      <td>0.001</td>
      <td>0.067</td>
      <td>0.156</td>
      <td>0.007</td>
      <td>0.001</td>
      <td>0.019</td>
      <td>0.060</td>
    </tr>
    <tr>
      <td>35</td>
      <td>0.002</td>
      <td>0.002</td>
      <td>0.458</td>
      <td>0.726</td>
      <td>0.006</td>
      <td>0.0002</td>
      <td>0.002</td>
      <td>0.017</td>
      <td>0.098</td>
      <td>0.897</td>
      <td>0.0003</td>
      <td>0.0004</td>
      <td>0.0001</td>
      <td>0.001</td>
    </tr>
    <tr>
      <td>55</td>
      <td>0.113</td>
      <td>0.139</td>
      <td>0.912</td>
      <td>0.566</td>
      <td>0.033</td>
      <td>0.242</td>
      <td>0.043</td>
      <td>0.004</td>
      <td>0.182</td>
      <td>0.214</td>
      <td>0.097</td>
      <td>0.083</td>
      <td>0.043</td>
      <td>0.138</td>
    </tr>
    <tr>
      <td>80</td>
      <td>0.175</td>
      <td>0.069</td>
      <td>0.497</td>
      <td>0.061</td>
      <td>0.166</td>
      <td>0.310</td>
      <td>0.003</td>
      <td>0.008</td>
      <td>0.807</td>
      <td>0.279</td>
      <td>0.287</td>
      <td>0.804</td>
      <td>0.079</td>
      <td>0.623</td>
    </tr>
    <tr>
      <td>110</td>
      <td>0.056</td>
      <td>0.449</td>
      <td>0.793</td>
      <td>0.356</td>
      <td>0.209</td>
      <td>0.440</td>
      <td>0.463</td>
      <td>0.402</td>
      <td>0.226</td>
      <td>0.760</td>
      <td>0.084</td>
      <td>0.006</td>
      <td>0.357</td>
      <td>0.214</td>
    </tr>
  </tbody>
</table>

Shield-stage BMP signaling pulse, Opto-BMP versus uninjected p-values (Figures 4 and 5M–Z, and Figure 5—figure supplement 1J–W):

<table>
  <thead>
    <tr>
      <th>Time post-exposure (min)</th>
      <th>bambia</th>
      <th>bmp4</th>
      <th>cdx4</th>
      <th>crabp2b</th>
      <th>eve1</th>
      <th>foxi1</th>
      <th>gata 2a</th>
      <th>id2a</th>
      <th>klf2b</th>
      <th>smad6a</th>
      <th>smad7</th>
      <th>sizzled</th>
      <th>tfap2c</th>
      <th>ved</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>−30</td>
      <td>0.544</td>
      <td>0.401</td>
      <td>0.983</td>
      <td>0.522</td>
      <td>0.869</td>
      <td>0.423</td>
      <td>0.382</td>
      <td>0.909</td>
      <td>0.278</td>
      <td>0.828</td>
      <td>0.168</td>
      <td>0.154</td>
      <td>0.667</td>
      <td>0.003</td>
    </tr>
    <tr>
      <td>−20</td>
      <td>0.111</td>
      <td>0.069</td>
      <td>0.727</td>
      <td>0.440</td>
      <td>0.686</td>
      <td>0.474</td>
      <td>0.116</td>
      <td>0.242</td>
      <td>0.084</td>
      <td>0.731</td>
      <td>0.509</td>
      <td>0.983</td>
      <td>0.631</td>
      <td>0.483</td>
    </tr>
    <tr>
      <td>−10</td>
      <td>0.166</td>
      <td>0.667</td>
      <td>0.698</td>
      <td>0.098</td>
      <td>0.634</td>
      <td>0.013</td>
      <td>0.522</td>
      <td>0.489</td>
      <td>0.197</td>
      <td>0.881</td>
      <td>0.834</td>
      <td>0.820</td>
      <td>0.492</td>
      <td>0.680</td>
    </tr>
    <tr>
      <td>0</td>
      <td>0.032</td>
      <td>0.071</td>
      <td>0.599</td>
      <td>0.627</td>
      <td>0.041</td>
      <td>0.005</td>
      <td>0.280</td>
      <td>0.004</td>
      <td>0.046</td>
      <td>0.136</td>
      <td>0.002</td>
      <td>0.056</td>
      <td>0.781</td>
      <td>0.004</td>
    </tr>
    <tr>
      <td>10</td>
      <td>0.013</td>
      <td>0.001</td>
      <td>0.084</td>
      <td>0.658</td>
      <td>0.082</td>
      <td>0.000</td>
      <td>0.006</td>
      <td>0.013</td>
      <td>0.0001</td>
      <td>0.242</td>
      <td>0.003</td>
      <td>0.005</td>
      <td>0.151</td>
      <td>0.002</td>
    </tr>
    <tr>
      <td>20</td>
      <td>0.003</td>
      <td>0.002</td>
      <td>0.020</td>
      <td>0.201</td>
      <td>0.001</td>
      <td>0.000</td>
      <td>0.0001</td>
      <td>0.012</td>
      <td>0.007</td>
      <td>0.045</td>
      <td>0.006</td>
      <td>0.004</td>
      <td>0.006</td>
      <td>0.002</td>
    </tr>
    <tr>
      <td>35</td>
      <td>0.006</td>
      <td>0.012</td>
      <td>0.031</td>
      <td>0.254</td>
      <td>0.088</td>
      <td>0.015</td>
      <td>0.005</td>
      <td>0.002</td>
      <td>0.222</td>
      <td>0.067</td>
      <td>0.013</td>
      <td>0.075</td>
      <td>0.034</td>
      <td>0.020</td>
    </tr>
    <tr>
      <td>55</td>
      <td>0.415</td>
      <td>0.001</td>
      <td>0.139</td>
      <td>0.408</td>
      <td>0.158</td>
      <td>0.011</td>
      <td>0.460</td>
      <td>0.024</td>
      <td>0.038</td>
      <td>0.044</td>
      <td>0.766</td>
      <td>0.563</td>
      <td>0.051</td>
      <td>0.162</td>
    </tr>
    <tr>
      <td>80</td>
      <td>0.237</td>
      <td>0.067</td>
      <td>0.726</td>
      <td>0.231</td>
      <td>0.101</td>
      <td>0.067</td>
      <td>0.695</td>
      <td>0.089</td>
      <td>0.067</td>
      <td>0.336</td>
      <td>0.374</td>
      <td>0.031</td>
      <td>0.710</td>
      <td>0.011</td>
    </tr>
    <tr>
      <td>110</td>
      <td>0.673</td>
      <td>0.009</td>
      <td>0.828</td>
      <td>0.050</td>
      <td>0.079</td>
      <td>0.568</td>
      <td>0.783</td>
      <td>0.410</td>
      <td>0.094</td>
      <td>0.222</td>
      <td>0.214</td>
      <td>0.005</td>
      <td>0.537</td>
      <td>0.049</td>
    </tr>
  </tbody>
</table>

For experiments in which transcriptional responses to low- and high-amplitude BMP signaling pulses of different durations were measured using NanoString (Figure 6C–F and Figure 6—figure supplement 1), mRNA counts from uninjected embryos were first subtracted from Opto-BMP-injected siblings. Then the subtracted counts from light-exposed embryos were compared to subtracted counts from unexposed control embryos.

Low- and high-amplitude BMP pulses, exposed versus unexposed p-values (Figure 6C–F, Figure 6—figure supplement 1):

<table>
  <thead>
    <tr>
      <th>Exp.</th>
      <th>Time into exposure (min)</th>
      <th>bambia</th>
      <th>bmp4</th>
      <th>cdx4</th>
      <th>crabp 2b</th>
      <th>eve1</th>
      <th>foxi1</th>
      <th>gata 2a</th>
      <th>id2a</th>
      <th>klf 2b</th>
      <th>smad 6a</th>
      <th>smad 7</th>
      <th>szl</th>
      <th>tfap 2c</th>
      <th>ved</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">70 lux, 10 min</td>
      <td>30</td>
      <td>0.083</td>
      <td>0.597</td>
      <td>0.390</td>
      <td>0.967</td>
      <td>0.487</td>
      <td>0.021</td>
      <td>0.856</td>
      <td>0.703</td>
      <td>0.271</td>
      <td>0.894</td>
      <td>0.071</td>
      <td>0.405</td>
      <td>0.816</td>
      <td>0.603</td>
    </tr>
    <tr>
      <td>40</td>
      <td>0.945</td>
      <td>0.917</td>
      <td>0.247</td>
      <td>0.928</td>
      <td>0.467</td>
      <td>0.020</td>
      <td>0.700</td>
      <td>0.436</td>
      <td>0.586</td>
      <td>0.263</td>
      <td>0.045</td>
      <td>0.309</td>
      <td>0.230</td>
      <td>0.291</td>
    </tr>
    <tr>
      <td>50</td>
      <td>0.078</td>
      <td>0.234</td>
      <td>0.659</td>
      <td>0.358</td>
      <td>0.104</td>
      <td>0.046</td>
      <td>0.067</td>
      <td>0.050</td>
      <td>0.341</td>
      <td>0.081</td>
      <td>0.084</td>
      <td>0.205</td>
      <td>0.070</td>
      <td>0.079</td>
    </tr>
    <tr>
      <td rowspan="3">3900 lux, 10 min</td>
      <td>30</td>
      <td>0.122</td>
      <td>0.967</td>
      <td>0.758</td>
      <td>0.998</td>
      <td>0.317</td>
      <td>0.020</td>
      <td>0.456</td>
      <td>0.085</td>
      <td>0.155</td>
      <td>0.343</td>
      <td>0.355</td>
      <td>0.475</td>
      <td>0.583</td>
      <td>0.425</td>
    </tr>
    <tr>
      <td>40</td>
      <td>0.013</td>
      <td>0.367</td>
      <td>0.008</td>
      <td>0.296</td>
      <td>0.085</td>
      <td>0.056</td>
      <td>0.171</td>
      <td>0.154</td>
      <td>0.027</td>
      <td>0.572</td>
      <td>0.037</td>
      <td>0.261</td>
      <td>0.019</td>
      <td>0.062</td>
    </tr>
    <tr>
      <td>50</td>
      <td>0.029</td>
      <td>0.013</td>
      <td>0.169</td>
      <td>0.805</td>
      <td>0.517</td>
      <td>0.030</td>
      <td>0.011</td>
      <td>0.015</td>
      <td>0.163</td>
      <td>0.332</td>
      <td>0.005</td>
      <td>0.051</td>
      <td>0.190</td>
      <td>0.206</td>
    </tr>
    <tr>
      <td rowspan="3">70 lux, 20 min</td>
      <td>30</td>
      <td>0.001</td>
      <td>0.635</td>
      <td>0.176</td>
      <td>0.660</td>
      <td>0.037</td>
      <td>0.001</td>
      <td>0.062</td>
      <td>0.019</td>
      <td>0.002</td>
      <td>0.304</td>
      <td>0.056</td>
      <td>0.087</td>
      <td>0.321</td>
      <td>0.031</td>
    </tr>
    <tr>
      <td>40</td>
      <td>0.120</td>
      <td>0.348</td>
      <td>0.217</td>
      <td>0.126</td>
      <td>0.479</td>
      <td>0.011</td>
      <td>0.172</td>
      <td>0.104</td>
      <td>0.031</td>
      <td>0.270</td>
      <td>0.181</td>
      <td>0.136</td>
      <td>0.102</td>
      <td>0.250</td>
    </tr>
    <tr>
      <td>50</td>
      <td>0.121</td>
      <td>0.103</td>
      <td>0.273</td>
      <td>0.173</td>
      <td>0.075</td>
      <td>0.075</td>
      <td>0.068</td>
      <td>0.033</td>
      <td>0.042</td>
      <td>0.216</td>
      <td>0.064</td>
      <td>0.085</td>
      <td>0.031</td>
      <td>0.047</td>
    </tr>
    <tr>
      <td rowspan="3">3900 lux, 20 min</td>
      <td>30</td>
      <td>0.178</td>
      <td>0.448</td>
      <td>0.201</td>
      <td>0.233</td>
      <td>0.061</td>
      <td>0.160</td>
      <td>0.061</td>
      <td>0.035</td>
      <td>0.154</td>
      <td>0.491</td>
      <td>0.166</td>
      <td>0.232</td>
      <td>0.122</td>
      <td>0.189</td>
    </tr>
    <tr>
      <td>40</td>
      <td>0.005</td>
      <td>0.123</td>
      <td>0.934</td>
      <td>0.761</td>
      <td>0.083</td>
      <td>0.003</td>
      <td>0.075</td>
      <td>0.028</td>
      <td>0.077</td>
      <td>0.020</td>
      <td>0.001</td>
      <td>0.028</td>
      <td>0.324</td>
      <td>0.033</td>
    </tr>
    <tr>
      <td>50</td>
      <td>0.324</td>
      <td>0.271</td>
      <td>0.006</td>
      <td>0.615</td>
      <td>0.077</td>
      <td>0.540</td>
      <td>0.144</td>
      <td>0.382</td>
      <td>0.062</td>
      <td>0.929</td>
      <td>0.238</td>
      <td>0.160</td>
      <td>0.225</td>
      <td>0.237</td>
    </tr>
  </tbody>
</table>

### Data and code availability

The raw images, data, and source code for custom scripts used in this work are available from the corresponding author upon request. Image quantification data and differential gene expression analyses are available in the accompanying source data files and Supplementary file 1, respectively. The RNA-sequencing data has been deposited at the GEO repository (accession number: GSE135100).

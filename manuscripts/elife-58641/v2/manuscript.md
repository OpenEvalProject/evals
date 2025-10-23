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

We focused on patterning mediated by BMP, a TGF-β superfamily member with important developmental roles across the animal kingdom (reviewed in Zinski et al., 2018). BMP ligands bind and assemble complexes of type I and II receptor serine/threonine kinases, resulting in the phosphorylation of the signal transducers Smad1/5/9 and activation of BMP target genes (Figure 1B; Derynck and Budi, 2019). The regulation of BMP gradient formation during early development has been analyzed in a variety of organisms including Drosophila, Nematostella, and Xenopus (Genikhovich et al., 2015; Iber and Gaglia, 2007; Mizutani et al., 2005; Plouhinec et al., 2013) as well as zebrafish. During late blastula and early gastrulation stages in zebrafish embryos, graded transcription and subsequent diffusion of BMP ligands, together with dorsally secreted BMP inhibitors such as Chordin, generate a ventrally-peaking gradient of BMP signaling that patterns the dorsal-ventral axis (Figure 1C; Pomreinke et al., 2017; Zinski et al., 2017). Loss of BMP signaling results in dorsalization, whereas excess BMP signaling produces ventralized embryos (Zinski et al., 2018). The degree of dorsalization or ventralization can be modulated by mutations in BMP pathway components with different strengths (Mintzer et al., 2001; Barth et al., 1999; Nguyen et al., 1998; Mullins et al., 1996) or by injecting different amounts of mRNA encoding pathway activators or inhibitors (Schumacher et al., 2011; Dick et al., 2000; Kishimoto et al., 1997; Neave et al., 1997).

These observations have led to the suggestion that BMP functions as a morphogen to pattern the dorsal-ventral axis by activating different target genes at different signaling level thresholds (Figure 1A; Zinski et al., 2018; Tuazon and Mullins, 2015; Schumacher et al., 2011; Barth et al., 1999; Nguyen et al., 1998; Neave et al., 1997; Mullins et al., 1996). However, overexpression and genetic manipulations can affect the duration of signal exposure, dysregulate other signaling pathways, and modify earlier aspects of development such as morphogenetic movements, complicating the interpretation of these experiments. Moreover, patterning of the dorsal-ventral axis by BMP and the germ layers by FGF and Nodal occurs simultaneously in zebrafish (Zinski et al., 2018), and although these pathways are known to interact, how FGF and Nodal influence the spatiotemporal expression of BMP target genes has not been systematically assessed.

To identify the factors that contribute to differences in BMP target gene expression and rule out factors that do not contribute, we first identified BMP targets in early zebrafish embryos and quantified their diverse spatial (Figure 1) and temporal (Figure 2) expression patterns. We then used an optogenetic approach to generate acute BMP signaling pulses (Figure 3) and found that while most target genes can respond to early BMP signaling (Figure 4), differential transcription kinetics do not fully account for the observed expression differences (Figure 5). Further, target gene responses to high- and low-amplitude signaling pulses suggest that not all spatiotemporal target gene expression differences are due to different signaling activation thresholds (Figure 6). In contrast, inhibition of FGF and Nodal signaling homogenized the spatial expression patterns of BMP targets, suggesting that combinatorial regulation by BMP, FGF, and Nodal is a major driver of BMP target gene spatial diversity (Figure 7).

![Figure 2.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig2-v2.jpg)

**Figure 2.:** (A–N) Embryos were collected every 30 min from 2.75 to 7.25 hpf, and transcript levels were quantified using NanoString technology. Error bars represent standard error. Temporal profiles were fit with the cumulative distribution function of the normal distribution (gray lines), and activation time (arrowheads) was defined as the average time point at which the curves reached about two mean average deviations (i.e., ) from the inflection point 1.5∙τ (excluding the maternally deposited genes νid2a [Chong et al., 2005] and smad6a [White et al., 2017]). NanoString probes for two high-confidence activated BMP target genes (apoc1l and znfl2b) were not functional. (O) Average gene expression spatial range is plotted against average activation time. See the Figure 2—source data 1 file for source data.Figure 2—source data 1.Figure 2.

![Figure 4.](https://cdn.elifesciences.org/articles/58641/elife-58641-fig4-v2.jpg)

**Figure 4.:** (A) Schematic of competence model: Late-activated genes should respond to a late (shield stage, solid line), but not early (high stage, dashed line) BMP signaling pulse. (B-O) High-confidence BMP target gene responses after an early (high stage,~3.5 hpf, dashed line) or late (shield stage,~6.75 hpf, solid line) BMP signaling pulse delivered by exposing uninjected and Opto-BMP-injected embryos to 30 min blue light (Figure 3C–E and Figure 3—figure supplement 1I,J). To assess induced transcription, NanoString transcript counts from uninjected embryos were subtracted from Opto-BMP transcript counts and are plotted here with piecewise linear interpolation between timepoints; error bars represent standard error (see Materials and methods for statistical analysis). See the Figure 4—source data 1 file for source data.Figure 4—source data 1.Figure 4.

## Results

## BMP target genes have diverse spatiotemporal expression patterns

We used RNA-sequencing to systematically identify genes activated by BMP during early zebrafish gastrulation, when BMP is engaged in dorsal-ventral patterning (shield stage,~6.75 h post-fertilization (hpf)) (Zinski et al., 2018). We identified 16 high-confidence target genes that are significantly upregulated in bmp-overexpressing embryos and downregulated in embryos overexpressing the BMP inhibitor chordin (Figure 1—figure supplement 1A–D and Supplementary file 1). 14 of these genes (apoc1l, bambia, bmp4, cdx4, eve1, foxi1, gata2a, id2a, klf2b, smad6a, smad7, sizzled, tfap2c, and ved) are known to be positively regulated by BMP in zebrafish (Kashiwada et al., 2015; Wang et al., 2015; Kotkamp et al., 2014; Wang et al., 2013; Das and Crump, 2012; de Pater et al., 2012; Kwon et al., 2010; Li and Cornell, 2007; Poulain et al., 2006; Chong et al., 2005; Davidson et al., 2003; Martyn and Schulte-Merker, 2003; Nissen et al., 2003; Solomon et al., 2003; Yabe et al., 2003; Pogoda and Meyer, 2002; Shimizu et al., 2002; Oates et al., 2001; Tsang et al., 2000; Chin et al., 1997; Nikaido et al., 1997; Hammerschmidt et al., 1996a; Hammerschmidt et al., 1996b; Mullins et al., 1996; Detrich et al., 1995; Joly et al., 1993; Joly et al., 1992), whereas crabp2b (Sharma et al., 2005) and znfl2b (Hogan et al., 2006) have not previously been implicated as BMP targets. Four of the 16 target genes encode repressors of BMP signaling (bambia, sizzled, smad6a, and smad7) and one encodes bmp4, consistent with roles for negative and positive feedbacks in TGF-β-mediated patterning (Zinski et al., 2018).

According to the gradient threshold model, target genes are activated by distinct signaling levels, leading to different spatial domains of target gene expression in the presence of a signaling gradient (Figure 1A). To determine whether the BMP patterning system fits this paradigm, we first sought to characterize both BMP signaling distribution and spatial target gene expression. We assessed spatial BMP signaling from 2.75 to 7.25 hpf (256-cell stage – 60% epiboly) using immunofluorescent stainings to detect the BMP signal transducer pSmad1/5/9. We imaged embryos using selective plane illumination microscopy (SPIM) and quantified fluorescence along the dorsal-ventral axis (Figure 1—figure supplement 1E, Materials and methods). Similar to previous studies (Pomreinke et al., 2017; Zinski et al., 2017; Ramel and Hill, 2013; Tucker et al., 2008), we observed a ventrally-peaking BMP signaling gradient that increases in amplitude over time (Figure 1D,E).

We then used fluorescence in situ hybridization and SPIM to quantify the spatial expression profiles of BMP target genes along the dorsal-ventral axis at shield stage (~6.75 hpf) and found that target genes have different expression profiles along this axis (Figure 1F–Y, Figure 1—figure supplement 1E, Materials and methods; some genes could not be quantified due to weak signal or inability to reliably identify the ventral side). The shape of the expression profiles can be well described by bell curves. We therefore used regression analysis with the Gaussian functionAe-x-μ2ςand defined the range of each target gene asr=μ+2ς/2

Using this definition, spatial gene expression broadness ranges from 40–100% dorsal-ventral embryo length (Figure 1F–Y). Strikingly, pronounced differences along the orthogonal animal-vegetal axis were also evident: Genes were either uniformly expressed along this axis on the ventral side (sizzled, ved, apoc1l, and bambia), restricted to the margin (cdx4 and eve1), or excluded from the margin (foxi1, klf2b, gata2a, and tfap2c) (Figure 1C,F–O’). Margin exclusion resulted in distinct dorsal-ventral profiles in which mRNA levels peak around 30% embryo length (Figure 1R,T,W,X), compared to non-excluded genes that peaked more ventrally (Figure 1P,Q,S,U,V,Y). Therefore, some of the spatial diversity in BMP target gene expression arises from differences along the animal-vegetal axis, orthogonal to the dorsal-ventral BMP signaling gradient.

The gradient threshold paradigm (Figure 1A) implies that genes with broad ranges should be activated by lower signaling levels. Since signaling levels increase over time (Figure 1D,E; Pomreinke et al., 2017; Zinski et al., 2017; Ramel and Hill, 2013; Tucker et al., 2008), we sought to determine whether more broadly expressed targets were activated earlier. To assess temporal expression of BMP targets, we used NanoString molecular barcoding (Kulkarni, 2011) to measure transcript levels from 2.75 to 7.25 hpf (256-cell stage – 60% epiboly) (Figure 2A–N). The shape of the temporal expression profiles can be well approximated by the modified cumulative distribution function of the normal distribution12A1+erf⁡x-ντ2+b

We used this function for regression analysis of the temporal expression profiles and defined activation times as the average time point at which the curves reached about two mean average deviations (i.e., 1.5∙τ) from the inflection point ν. BMP target gene activation times defined in this way ranged from 3.4 to 6.3 hpf (Figure 2).

The gradient threshold model predicts a monotonic decrease when comparing range and activation time. While this relationship is not observed for the entire dataset (Figure 2O), there is a decreasing monotonic trend when foxi1, eve1, and cdx4 are excluded (note that in contrast to the other genes, the expression of eve1 and cdx4 was only quantified in the embryonic margin [Figure 1—figure supplement 1E, Materials and methods]). This suggests the possibility that subsets of BMP target genes may behave consistently with the gradient threshold model. We therefore sought to investigate the relationship between BMP signaling and target gene expression further using an optogenetic strategy.

## Reversible optogenetic activation of BMP signaling in vivo using Opto-BMP

To assess how BMP target genes respond to BMP signaling, we developed a method to optogenetically manipulate BMP signaling in vivo. We fused zebrafish BMP receptor kinase domains to an algal blue light-homodimerizable LOV domain (Rogers and Müller, 2020; Takahashi et al., 2007) and targeted the fusions to the membrane using a myristoylation motif (Figure 3A), similar to previous approaches (Ramachandran et al., 2018; Vopalensky et al., 2018; Sako et al., 2016). Blue light (~450 nm) exposure should lead to dimerization of the LOV domains and interaction of the BMP kinase domains, activating BMP signaling (Figure 3A).

Injection of mRNA encoding Opto-BMP into zebrafish embryos at the one-cell stage resulted in strong ventralization in light-reared embryos, consistent with excess BMP signaling, whereas dark-reared siblings were mostly aphenotypic (Figure 3B and Figure 3—figure supplement 1A,K,L). Spatially localized activation of BMP signaling was also possible using SPIM, further demonstrating light-dependent signaling activation (Figure 3—figure supplement 1E–H).

To facilitate optogenetic experiments, we developed a light exposure device by embedding blue LEDs into the lid of a standard six-well plate and controlling light intensity and dynamics with a single-board computer (Figure 3—figure supplement 1B–D, Materials and methods). Using the LED array, we exposed uninjected and Opto-BMP-injected embryos to blue light for 30 min during high (3.5–4 hpf) or shield (6.75–7.25 hpf) stages, fixed embryos during and after exposure, and quantified BMP signaling using pSmad1/5/9 immunofluorescence (Figure 3C–E and Figure 3—figure supplement 1I,J). At both stages, Opto-BMP embryos showed a dramatic increase in BMP signaling within 10 min of light exposure, and signaling levels returned to normal after light removal. These experiments demonstrate that Opto-BMP reversibly activates BMP signaling in zebrafish embryos in response to light.

## Most BMP target genes are competent to respond to BMP at early stages

BMP target genes are activated over a range of developmental stages, from 3.4 to 6.3 hpf (Figure 2). Time-dependent differences in competence – a gene’s ability to respond to signaling – may underlie the diversity in activation timing (Figure 4A). To test this, we quantified BMP target gene expression in uninjected and Opto-BMP-injected embryos exposed to 30 min blue light during either high (3.5–4 hpf) or shield stage (6.75–7.25 hpf) (Figure 4 and Figure 5—figure supplement 1A–F).

In response to a strong BMP signaling pulse at high or shield stage (Figure 3C–E and Figure 3—figure supplement 1I,J), we observed corresponding significant pulses of BMP target gene expression for all genes except crapb2b and cdx4 (Figure 4K,L). While cdx4 is not competent to respond to an early BMP signaling pulse and crabp2b did not clearly respond to either an early or late signaling pulse, all other tested high-confidence BMP target genes responded at high stage. Therefore, differences in competence to respond to BMP signaling at early stages do not explain the majority of diversity in activation timing.

## Transcription kinetics in response to BMP do not fully explain spatiotemporal expression

Target gene transcription kinetics can play important roles in defining spatial expression domains. For example, it has been suggested that Nodal target genes with faster transcript accumulation rates have broader spatial expression domains (Dubrulle et al., 2015). To investigate how the transcription kinetics of BMP target genes may influence their spatiotemporal expression patterns, we assessed the dynamics of target gene responses (Figure 4) to optogenetically generated BMP signaling pulses (Figure 3C–E and Figure 3—figure supplement 1I,J). We reasoned that the early activation timing and broad spatial range of some BMP targets might be explained by more rapid transcription in response to BMP. In this paradigm, early BMP signaling activates expression of all target genes at the same time, but transcripts of more slowly transcribed genes only accumulate to detectable levels at later stages, causing them to appear to be ‘late-activated’ (Figure 5A). Similarly, broader spatial ranges could be caused by faster accumulation of rapidly produced transcripts that would therefore be detectable farther from the ventral side than more slowly produced transcripts.

To determine whether higher transcript accumulation rates correlate with broader spatial ranges or earlier activation times, we first assessed maximum transcript counts in response to BMP signaling pulses at high or shield stage (Figure 4). Assuming similar transcript degradation kinetics, transcripts with faster production rates should accumulate to higher levels in response to a BMP signaling pulse (Figure 5A). However, we observed a weak negative correlation (Figure 5B) or no correlation (Figure 5D) between maximum transcript counts and activation time, and found similar results for range (Figure 5C,E). This suggests that differences in transcript accumulation rates in response to BMP do not fully account for differences in activation timing and spatial broadness.

We then used a second approach to assess transcript accumulation kinetics that does not require the assumption of similar transcript degradation rates (Figure 5F–Z). We fitted the transcription data from the shield-stage BMP signaling pulse with a model involving the known pSmad1/5/9 input (Figure 3C, Figure 5L, and Figure 3—figure supplement 1J) and parameters reflecting transcript induction (σ) and decay (λ) (Figure 5M–Z, Materials and methods). Each of the three experimental repeats was fitted individually, and average σ and λ values were calculated for each gene. We found a weak negative correlation between σ and activation time (Figure 5F), and no correlation between σ and range (Figure 5G). We also observed a weak negative correlation between λ and activation time (Figure 5H), and no obvious correlation between λ and spatial broadness (Figure 5I). These results are consistent with the maximum transcript count analysis (Figure 5B–E) and with an alternative fitting approach (Figure 5—figure supplement 1G–W, Materials and methods). In addition, we observed a strong positive correlation between maximum transcript count and σ (Figure 5J), and no correlation between maximum transcript count and λ (Figure 5K), suggesting that production dominates transcription kinetics, and supporting the use of maximum transcript count as a proxy for induction rate.

Together, our analyses indicate that differential transcription kinetics in response to BMP signaling play a minor role in generating the distinct spatiotemporal expression patterns of BMP target genes.

## Differential activation thresholds do not fully explain spatiotemporal expression

In the gradient threshold paradigm, target genes are activated by distinct signaling thresholds that define gene expression ranges (Figure 1A). This model therefore predicts that broadly expressed genes, but not narrowly expressed genes, should be activated by low levels of signaling (Figure 6A).

To test this idea, we exposed uninjected and Opto-BMP-injected embryos to high- (3900 lux) or low-intensity (70 lux) blue light for 10 or 20 min at shield stage – resulting in high- or low-amplitude BMP signaling pulses, respectively (Figure 6B) – and then quantified BMP target gene responses using NanoString technology. As expected, target activation was generally stronger following higher amplitude, longer duration pulses (Figure 6C–F and Figure 6—figure supplement 1). However, after a 10 min low-amplitude exposure, the third most narrowly expressed gene, foxi1, was significantly activated, whereas the broader genes were not robustly induced (Figure 6C). A longer 20 min low-amplitude pulse significantly activated both narrowly and broadly expressed genes (Figure 6E). A 10 min low-amplitude pulse significantly activated two of the top 50% earliest expressed genes (foxi1 and smad7), whereas a 20 min low-amplitude pulse significantly activated both early and late-expressed genes (Figure 6D,F). High-amplitude pulses activated genes of all ranges and activation times (Figure 6C–F).

Our experiments exposing embryos to different amplitude BMP signaling pulses therefore suggest that not all spatiotemporal target gene expression differences are due to different signaling activation thresholds, although a subset may be (see Discussion).

## FGF and Nodal modify BMP signaling and target gene expression

We noted that BMP target genes have unique expression patterns along the animal-vegetal axis that contribute to differences in their dorsal-ventral expression profiles (Figure 1F–Y). Specifically, 6 out of the 10 spatially quantified high-confidence BMP target genes are either restricted to (cdx4, eve1) or excluded from (foxi1, klf2b, gata2a, tfap2c) the margin. We wondered how regulation by additional signaling pathways active at the margin might contribute to these differences. We focused on the FGF and Nodal pathways, which regulate mesoderm and mesendoderm specification, respectively, and are known to influence BMP signaling (Figure 7; Rogers and Müller, 2019).

To assess the effects of FGF and Nodal signaling on BMP target gene expression, we inhibited these pathways using the small molecule inhibitors SU-5402 (Mohammadi et al., 1997) and SB-505124 (DaCosta Byfield et al., 2004), respectively (Figure 7—figure supplement 1A–J’). At shield stage, Nodal inhibition did not observably affect BMP signaling (Figure 7C and Figure 7—figure supplement 1F–G’), whereas FGF inhibition increased the amplitude of the BMP signaling gradient (Figure 7B and Figure 7—figure supplement 1D–E’). Simultaneous inhibition of both FGF and Nodal signaling increased both the amplitude and spatial broadness of the BMP signaling gradient (Figure 7D, Figure 7—figure supplement 1H–J’, and Figure 7—figure supplement 2A–K). Consistent with enhanced BMP signaling, in the absence of FGF/Nodal several BMP-activated genes were upregulated (Figure 7—figure supplement 2L–Y). Reduced levels of the secreted BMP inhibitor Chordin in embryos lacking FGF/Nodal signaling (Figure 7—figure supplement 2ZA) are likely to contribute to this BMP signaling expansion (Varga et al., 2007; Londin et al., 2005; Koshida et al., 2002). Additionally, FGF restricts the expression of bmp (Londin et al., 2005; Fürthauer et al., 2004; Fürthauer et al., 1997), and we detected increased bmp2b expression in FGF/Nodal-inhibited embryos (Figure 7—figure supplement 2Z).

Loss of FGF, Nodal, or both simultaneously affected BMP target gene dorsal-ventral spatial expression profiles differently (Figure 7F–I, Figure 7—figure supplement 1, and Figure 7—figure supplement 3). To determine whether FGF and Nodal are responsible for the margin restriction or exclusion of some BMP target genes (Figure 1F–O’), we assessed target expression along the animal-vegetal axis in inhibitor-treated embryos. In embryos lacking both FGF and Nodal signaling, margin-restricted genes were still expressed and restricted to the margin, whereas the expression of margin-excluded genes shifted into the margin (Figure 7I,L,M, and Figure 7—figure supplement 1).

We reasoned that the shift of margin-excluded genes into the margin could either be due to loss of FGF/Nodal activity, or due to enhanced BMP signaling at the margin (Figure 7D, Figure 7—figure supplement 1A–J’, and Figure 7—figure supplement 2A–K). We therefore assessed the animal-vegetal expression of margin-excluded genes in bmp-overexpressing embryos, which have dramatically elevated levels of BMP signaling at the ventral margin (Figure 7E) but intact Nodal and FGF signaling (Figure 7—figure supplement 1A–C’; Fürthauer et al., 1997). Margin-excluded genes were still clearly excluded from the margin in bmp-overexpressing embryos, suggesting that direct inhibition by FGF and Nodal normally prevents expression of these genes at the margin (Figure 7J,L,M).

To determine whether FGF and Nodal contribute to diversity in BMP target gene activation timing, we quantified the temporal expression of BMP targets in embryos lacking FGF and Nodal signaling from 2.75 to 7.25 hpf (256-cell stage – 60% epiboly) (Figure 7—figure supplement 2L–Y). Although transcript levels of several BMP targets were higher in treated compared to untreated embryos at later stages, their activation times were still diverse, suggesting that inputs other than FGF and Nodal are responsible for differences in activation times.

Finally, we noticed that much of the spatial diversity in BMP target gene expression along the dorsal-ventral axis collapsed in embryos lacking both FGF and Nodal signaling (Figure 7F,I). To quantify the decrease in spatial diversity, we calculated the spatial coefficient of variation in untreated and treated embryos (see Materials and methods). Strikingly, embryos lacking both FGF and Nodal had lower coefficients of variation at almost all positions along the dorsal-ventral axis compared to untreated embryos (Figure 7N). Together, our results identify combinatorial FGF and Nodal signaling as a major driver of spatial diversity in BMP target gene expression.

## Discussion

## Minor roles for differential responses to BMP in generating spatiotemporal diversity

Signaling gradients are frequently observed in developing tissues, including the embryonic axes of gastrulating zebrafish, the neural tube in mice, and the wing precursor in Drosophila (Briscoe and Small, 2015; Schier and Talbot, 2005). However, how gradients are interpreted by cells is complex to ascertain. The gradient threshold model proposes that gene-specific activation thresholds are responsible for differences in the spatial expression of target genes (Sharpe, 2019; Briscoe and Small, 2015; Dubrulle et al., 2015; Rogers and Schier, 2011; Barkai and Shilo, 2009; Ashe and Briscoe, 2006). Can gradients be reliably generated and signaling thresholds accurately interpreted with high sensitivity, or do gradients simply provide a ‘rough framework’ for patterning that is refined over time by other mechanisms such as target gene cross-talk (Briscoe and Small, 2015; Chen et al., 2012) or cell sorting (Akieda et al., 2019; Xiong et al., 2013)? In the former case, is such precision actually required for patterning?

In the context of zebrafish dorsal-ventral patterning, our data suggest minor roles for gene-specific activation thresholds in generating BMP target gene expression diversity. We did not find a clear monotonically decreasing relationship between activation time and gene expression range (Figure 2O), suggesting that more broadly expressed genes are not consistently more likely to be activated by the low levels of BMP present early (Figure 1D–E). We were also unable to detect an unambiguous correlation between range and the levels of signaling required for activation (Figure 6C,E). This suggests that not all BMP target expression boundaries are positioned by gene-specific BMP signaling thresholds (Figure 1A).

An alternative model proposes that diversity in spatiotemporal target gene expression is due to differences in expression kinetics. For example, it was shown that Nodal targets with higher transcript accumulation rates in response to Nodal signaling have broader spatial expression domains (Dubrulle et al., 2015). To determine whether the BMP patterning system might function similarly, we examined the transcriptional responses of BMP target genes (Figures 4 and 5, and Figure 5—figure supplement 1) to optogenetically generated pulses of BMP signaling (Figure 3C–D and Figure 3—figure supplement 1I,J). We did not detect a strong correlation between transcript induction rates and activation time or spatial range (Figure 5 and Figure 5—figure supplement 1G–W). Therefore, differential transcription kinetics in response to BMP are unlikely to account for spatiotemporal expression diversity.

Our results do not rule out the possibility that a different subset of BMP target genes may behave more consistently with these models. We focused on a set of high-confidence BMP targets (Figure 1—figure supplement 1), but other known targets were excluded from our analyses (Supplementary file 1). For example, the BMP target gene tp63 (Bakkers et al., 2002) is not expressed at shield stage, and was therefore excluded since it was not downregulated by chordin overexpression in our RNA-sequencing experiment (Supplementary file 1). We note that a subset of three genes (sizzled, ved, and bambia) that are neither restricted to nor excluded from the margin do show a monotonically decreasing relationship between range and activation time (Figure 2O) as well as activation dynamics that could be roughly commensurate with signaling input (Figure 6C and Figure 6—figure supplement 1), consistent with the gradient threshold model. However, it remains to be determined to what extent this subset of genes (or others) quantitatively follows the input-output relationships predicted by the gradient threshold model.

Our results also do not rule out other mechanisms of BMP signaling interpretation. For example, the graded distribution of many genes (Figure 1P–Y) could be consistent with a model in which gene expression is roughly proportional to the level of BMP signaling. In addition, BMP signaling duration may encode specific responses in vivo. Future work is needed to better define the relationship between BMP signaling levels and gene expression and to determine how BMP signaling dynamics are interpreted in embryos. Our study highlights the promise of optogenetic approaches in such investigations (Rogers and Müller, 2020). In contrast to pharmacological or genetic methods, optogenetic strategies can provide fast, tunable, and reversible spatiotemporal manipulation of signaling in vivo (Figure 3, Figure 6B, and Figure 3—figure supplement 1E–H), allowing more thorough characterization of input/output relationships.

In addition, our observations indicate that BMP signaling precision may not be required for proper patterning, or that the system is robustly buffered. For example, most embryos experiencing transient activation of BMP signaling lack gross morphological defects (Figure 3C–E, Figure 4, Figure 3—figure supplement 1A,K,L, and Figure 5—figure supplement 1). How patterning recovers from such insults will be an interesting avenue for future study. Together with previous work (reviewed in Zinski et al., 2018), several of our observations indicate that feedback is an important feature of the BMP patterning system: Five out of 16 high-confidence BMP target genes affect BMP signaling (Figure 1—figure supplement 1), and embryos can experience a dip in signaling levels after a signaling pulse (Figure 3C and Figure 3—figure supplement 1J). Cell sorting strategies that sharpen gene expression boundaries may also contribute to the observed recovery from BMP signaling manipulation (Akieda et al., 2019; Xiong et al., 2013).

## Margin restriction and competence of BMP target genes

One unresolved question from our study is the restriction of the BMP target genes eve1 and cdx4 to the margin (Figure 1I,I’,L,L’ and Figure 7—figure supplement 1). Consistent with previous work (Swanhart et al., 2010; Ota et al., 2009; Bennett et al., 2007; Ho et al., 2006; Londin et al., 2005; Shimizu et al., 2005; Rentzsch et al., 2004), in the absence of FGF or Nodal, eve1 and cdx4 were still expressed at the ventral margin (Figure 7—figure supplement 1; we note, however, conflicting reports with dominant-negative FGF receptors [Ota et al., 2009; Kudoh et al., 2004; Griffin et al., 1995]). Inhibition by animal pole factors or a requirement for signaling pathways at the margin such as Wnt or retinoic acid might play a role in their margin restriction.

Both eve1 and cdx4 are also activated relatively late in development (Figure 2F,J), and cdx4 is not competent to respond to an early BMP signaling pulse (Figure 4K). FGF and Nodal have no obvious roles in regulating their activation timing or competence since their temporal expression was not significantly affected by loss of FGF/Nodal signaling (Figure 7—figure supplement 2Q,U). Understanding how the activation timing of all BMP target genes including eve1 and cdx4 is regulated is an important future goal.

## FGF and Nodal are major contributors to BMP target gene spatial diversity

Inhibition of FGF, Nodal, or both together had distinct effects on BMP signaling (Figure 7B–D, Figure 7—figure supplement 1A–J’, and Figure 7—figure supplement 2A–K). The increase in BMP signaling in the absence of FGF is likely explained by several factors including the known role of FGF in activating chordin and inhibiting bmp transcription (Figure 7—figure supplement 2Z,ZA) (Varga et al., 2007; Maegawa et al., 2006; Londin et al., 2005; Fürthauer et al., 2004; Kudoh et al., 2004; Koshida et al., 2002; Fürthauer et al., 1997), as well as inactivating Smad1 (Sapkota et al., 2007; Pera et al., 2003; Kretzschmar et al., 1997). Loss of Nodal did not detectably alter BMP signaling at shield stage. This is surprising because early expression of fgf is thought to depend on Nodal (van Boxtel et al., 2015; Maegawa et al., 2006; Mathieu et al., 2004; Gritsman et al., 1999; Rodaway et al., 1999), although low levels of fgf3 appear to be present at late blastula stages in Nodal signaling mutants (Mathieu et al., 2004), and weak FGF activity is detectable in Nodal inhibitor-treated embryos (van Boxtel et al., 2015). Nodal can activate chordin expression independently of FGF (Varga et al., 2007), and chordin is detectable albeit reduced in Nodal signaling mutants (Gritsman et al., 1999), suggesting that the reduction in chordin caused by Nodal loss is not sufficient to affect BMP signaling during early gastrulation. Future work is needed to explain why FGF, but not Nodal loss enhances BMP signaling at early gastrulation, and why simultaneous loss increases not only the amplitude but the broadness of the BMP signaling gradient.

Inhibition of FGF, Nodal, or both together also had distinct effects on BMP target gene expression (Figure 7F–I, Figure 7—figure supplements 1, 2 and 3). Although Nodal loss did not detectably alter the BMP signaling gradient (Figure 7C and Figure 7—figure supplement 1F–G’), the spatial distributions of several BMP target genes were affected (Figure 7H, Figure 7—figure supplement 1N,R, and Figure 7—figure supplement 3C). Nodal is also responsible for the dorsal expression of the BMP target gene apoc1l (Figure 1O,O’,Y), which is lost in the absence of Nodal (Figure 7H, Figure 7—figure supplement 1N, and Figure 7—figure supplement 3C). Although our study defines individual target gene responses at the phenomenological level, uncovering the DNA-level mechanisms (e.g., promoter regulation and chromatin status) that lead to the observed responses to BMP, FGF, and Nodal is an important future challenge.

The margin exclusion of the BMP target genes foxi1, klf2b, gata2a, and tfap2c can be explained by FGF/Nodal-mediated inhibition (Figure 7K). Loss of either FGF or Nodal signaling shifted the expression of margin-excluded genes toward the margin, although the shifts were most dramatic in the absence of both (Figure 7F–I,L,M, Figure 7—figure supplement 1, and Figure 7—figure supplement 3), with the exception of tfap2c, which was completely margin-shifted in FGF-inhibited embryos (Figure 7G, Figure 7—figure supplement 1M,Q, and Figure 7—figure supplement 3B). Excess BMP signaling at the margin in embryos lacking FGF and Nodal (Figure 7D, Figure 7—figure supplement 1H–J’, and Figure 7—figure supplement 2A–K) does not explain the observed gene expression shifts because no shifts were evident in bmp-overexpressing embryos (Figure 7J,L,M, Figure 7—figure supplement 1L,P, and Figure 7—figure supplement 3A). The FGF/Nodal-mediated margin exclusion of a subset of BMP targets contributes to the diversity in BMP target gene expression (Figure 7F,I,K,N), creating distinct dorsal-ventral profiles for margin-excluded genes (Figure 1R,T,W,X) compared to non-excluded genes (Figure 1P,Q,S,U,V,Y).

Our results suggest that much of the spatial diversity in BMP target gene expression arises from combinatorial signaling. A similar strategy is thought to regulate Bicoid target genes during Drosophila embryogenesis: Gene expression boundary shifts in response to Bicoid manipulation are often inconsistent with the gradient threshold model (Chen et al., 2012; Ochoa-Espinosa et al., 2009), and activation thresholds do not appear to explain target gene expression profiles at the DNA level (Ochoa-Espinosa et al., 2005). Rather, Bicoid is thought to act within a system of repressive pathways that regulate Bicoid target gene expression (Chen et al., 2012). During zebrafish dorsal-ventral patterning, FGF and Nodal affect BMP target gene expression in two ways: by restricting BMP signaling (Figure 7B–D, Figure 7—figure supplement 1D–E’,H–J’, and Figure 7—figure supplement 2A–K), and by inhibiting a subset of BMP target genes at the margin (Figure 7F–I,L,M, Figure 7—figure supplement 1, and Figure 7—figure supplement 3). These interactions sculpt the spatial expression profiles of BMP target genes and contribute to the patterning of the dorsal-ventral axis.

## Materials and methods

## Zebrafish husbandry

Zebrafish husbandry was executed in accordance with the guidelines of the State of Baden-Württemberg (Germany) and approved by the Regierungspräsidium Tübingen (35/9185.46–5, 35/9185.81–5). Wild type TE adult zebrafish were maintained under standard conditions. Embryos were incubated at 28°C in embryo medium (250 mg/l Instant Ocean salt, 1 mg/l methylene blue in reverse osmosis water adjusted to pH 7 with NaHCO3 [Müller et al., 2012]) unless otherwise noted.

## mRNA in vitro synthesis

pCS2+-based plasmids encoding Bmp2b, Chordin (Pomreinke et al., 2017), and Opto-BMP (this work, Figure 3—figure supplement 1, see below for cloning details) were linearized with NotI-HF (NEB, R3189). Capped mRNA was generated using a mMessage mMachine SP6 kit (ThermoFisher, AM1340). mRNA was purified using an RNeasy Mini kit (Qiagen, 74104) and quantified using a NanoDrop spectrophotometer (ThermoScientific).

## RNA-sequencing

Wild type TE zebrafish embryos were dechorionated with Pronase (Roche, 11459643001) and injected at the one-cell stage with 10 pg mRNA encoding zebrafish Bmp2b, 100 pg mRNA encoding zebrafish Chordin, or left uninjected (Pomreinke et al., 2017). When uninjected siblings reached shield stage (~6.75 hpf), embryos were snap-frozen in liquid nitrogen. 10 embryos were collected per sample, three samples per condition.

To prepare total RNA, the TRIzol reagent (Invitrogen, 15596026) manufacturer’s protocol was followed until aqueous phase recovery, then 6.25 μl Co-Precipitant Pink (Bioline, BIO-37075) was added to 250 μl aqueous phase, followed by 375 μl 100% EtOH. After vortexing briefly, samples were transferred to RNeasy Mini kit (Qiagen, 74104) spin columns and centrifuged at 13600 rpm at 4°C for 1 min. Flow-through was discarded and columns were washed twice with RPE buffer (Qiagen). RNA was eluted in 50 μl H2O. Total RNA concentration was measured using a NanoDrop spectrophotometer (ThermoScientific). 3–5 μg total RNA per sample were provided to LCG Genomics GmbH (Berlin, Germany) for sequencing and differential expression analysis. Sequences were aligned against the reference genome Danio rerio GRCz10 with STAR 2.4.1b, and differential expression analysis was carried out with edgeR 3.2.3, DESeq 1.12.0, and Cuff diff 2.1.1. The p-value threshold for differentially expressed genes was set to 0.05.

Note that endogenous bmp2b and chordin were not distinguishable from injected mRNAs in bmp2b- or chordin-injected embryos, respectively, and were therefore excluded from consideration as BMP target genes.

## Opto-BMP constructs

Opto-BMP constructs are based on Opto-Acvr constructs (Sako et al., 2016). These pCS2+-based Opto-Acvr constructs encode proteins that are tethered to the plasma membrane by an N-terminal myristoylation motif. Next to the membrane is a Nodal receptor kinase domain, followed by the light-oxygen-voltage (VfLOV) domain Aureochrome1 from Vaucheria frigida (Takahashi et al., 2007), and finally a C-terminal HA tag. Using splicing by overlap extension (SOE) PCR (Horton et al., 2013), Nodal receptor kinase domains in Opto-Acvr were swapped with putative kinase domains from the type I zebrafish BMP receptors Alk3 (NM_131621, bp 691–1566) (Nikaido et al., 1999) and Alk8 (NM_131345, bp 622–1497) (Mintzer et al., 2001; Yelick et al., 1998), and the type II zebrafish receptors BMPR2a (NM_001039817, bp 571–3009) and BMPR2b (NM_001039807, bp 598–1536) (Monteiro et al., 2008). In all cases except for Opto-BMPR2a, all residues after the transmembrane domain until the end of the kinase domain were included. Opto-BMPR2a contains all residues after the transmembrane domain until the end of the protein; the kinase domain-only construct was inactive.

An equimolar combination of mRNA encoding Opto-Alk3 (5.2 pg), Opto-Alk8 (5.2 pg), and Opto-BMPR2a (8.9 pg) was found to optimally induce BMP signaling in the light but not in the dark (Figure 3B, Figure 3—figure supplement 1A,K,L), and was used in all Opto-BMP experiments described here.

## LED array

To facilitate optogenetic experiments requiring control of light intensity and exposure duration, an embedded system-based controller was developed (Figure 3—figure supplement 1B–D). To maximize the versatility of the setup for different applications, a single-board computer was deployed (Raspberry Pi 3 model B, running under a Linux kernel, version 4.9). The controller was programmed to generate signals that modulate the duration and intensity of light. The generated signal was further amplified to drive the load of the LED array. A two-stage Darlington amplifier was used (TIP122 complementary power NPN Darlington - STMicroelectronics) to raise the ceiling of the current of amplification. The Darlington pair was used in a common emitter configuration in order to achieve a large power gain. The loads were operated on a constant voltage source provided by a regulated power supply (Disrelec Group AG, RND 320-KD3000D). During initial trials, brief, weak signal spikes could be detected, and an RC filter was subsequently used across the load to dampen any sporadic light flashes. The LED array constituted the circuit load; these LEDs were glued into the plastic cover of 6-well plates (Greiner Bio-One, 657160) (Figure 3—figure supplement 1B). Blue Nichia (NSPB510AS) or Everlight (1363-2SUBC/C470/S400-A4) LEDs were used in the array. Both LEDs emitted maximal spectral intensity at 470 nm, with the Nichia LEDs having a broader radiation angle, tighter spectral distribution, and less variable performance. During experiments, the LED array was placed inside a temperature-controlled incubator (Thermo Scientific Heratherum IMC 18, 50125882) set to 28°C. Dark fabric was taped to the interior of the incubator door to prevent outside light from entering.

The circuit schematic (Figure 3—figure supplement 1D) shows how the generated square wave was used to drive the LED array. One of the Raspberry Pi’s GPIO pins was used as a pulse-width modulation (PWM) output to produce signal. The raspberry-gpio-python module (https://sourceforge.net/projects/raspberry-gpio-python) was used to interface the GPIO. A pulse program was written in Python, which allows for variable parameter settings: GPIO pin number, modulation frequency (10 kHz is the NPN Darlington amplifier linear limit), pulse duration, and duty cycle.

Light intensities were measured using an LM37 luxmeter (DOSTMANN electronic GmbH).

LED array settings used in optogenetic experiments:

Fig.ExperimentLEDVoltage (V)Frequency (Hz)Intensity (lux)Duration (min)3, 3.1I,JShield stageEverlight24200230030High stageEverlight25–2822300304, 5, 5.1 G-WShield stageEverlight24200230030High stageEverlight25–2822300306, 6.170 luxNichia152007010 or 203900 luxNichia21200390010 or 201.1Dbambia, klf2b, sizzled, smad6a, smad7, vedEverlight25–282230030apoc1l, bmp4, cdx4, crabp2b, eve1, foxi1, gata2a, id2a, tfap2c, znfl2bNichia212003900303.1K,LShield stageEverlight24200230030All except shieldEverlight25–282230030 or 6005.1A-FAllEverlight24200230030

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

## Cycloheximide experiment

For the cycloheximide (Sigma, C4859) experiment in Figure 1—figure supplement 1D, embryos from wild type TE incrosses were dechorionated using Pronase (Roche, 11459643001) and injected at the one-cell stage with 5.2 pg opto-Alk3 + 5.2 pg opto-Alk8 + 8.9 pg opto-BMPR2a mRNA (Figure 3—figure supplement 1A). Control siblings were left uninjected, and embryos were sorted into agarose-coated 6-well plates and incubated at 28°C. 70–90 min post-fertilization at the 4–16 cell stage, unfertilized and damaged embryos were removed, and plates were individually wrapped in aluminum foil to prevent light exposure and incubated at 28°C. At 6.25 h post-fertilization (hpf), embryos were transferred into new agarose-coated 6-well dishes containing either 50 μg/ml cycloheximide (Bennett et al., 2007; Poulain and Lepage, 2002) or an equivalent volume of DMSO (Roth, A994.2) diluted in embryo medium that had been incubated at 28°C prior to transfer. Red color filters (Rosco, E106 Primary Red) were used to cover the dissecting microscope light source during the transfer to prevent transmission of VfLOV-dimerizing wavelengths and minimize BMP activation, and plates were wrapped in aluminum foil after transfer. At 6.75 hpf (~shield stage, 30 min after cycloheximide exposure), plates were transferred to a small 28°C incubator containing the LED array (Figure 3—figure supplement 1B) and exposed to blue light for 30 min (6.75–7.25 hpf). 20 min after light exposure, when most BMP target genes are maximally induced (Figure 4), embryos were fixed and colorimetric in situ hybridization was carried out as described in the Fluorescence and colorimetric in situ hybridization section below.

## pSmad1/5/9, pSmad2/3, and pErk immunofluorescence staining

For pSmad1/5/9, pSmad2/3, and pErk immunofluorescence staining, embryos were fixed in 4% formaldehyde in PBS at 4°C overnight, then transferred to MeOH and stored at −20°C for at least 2 h. See below and Figure 1—figure supplement 1E for imaging and quantification details.

## pSmad1/5/9

Embryos were washed at least three times with PBST (phosphate buffered saline + 0.1% Tween-20), then blocked for at least 1 h at room temperature in blocking buffer (10% FBS (Biochrom, S0415), 1% DMSO, 0.1% Tween-20 in PBS). Embryos were incubated in 1:100 rabbit anti-phosphoSmad1/5/9 antibody (Cell Signaling Technology, 13820) in blocking buffer at 4°C overnight. One wash with blocking buffer followed by 3–5 washes with PBST were carried out at room temperature, then embryos were blocked again with blocking buffer for at least 1 h. Embryos were incubated in 1:5000 goat anti-rabbit Alexa Fluor 488-conjugated secondary antibody (Life Technologies, A11008) in blocking buffer at 4°C overnight. Embryos were then incubated in 1:5000 DAPI (Life Technologies, D1306; stock concentration: 5 mg/ml) in blocking buffer at room temperature for at least 1 h, then washed at least five times with PBST. Stained embryos were wrapped in aluminum foil and stored at 4°C overnight before SPIM imaging.

## pSmad2/3

Embryos were incubated in ice-cold acetone (Roth, 5025.5) for 7 min, then washed at least three times with PBST, blocked for at least 1 h in 10% FBS in PBST and incubated in 1:5000 rabbit anti-pSmad2/3 (Cell Signaling Technology, 8828) in 10% FBS in PBST at 4°C overnight. Embryos were then washed at least five times in PBST, blocked again for at least 1 h in 10% FBS in PBST, and incubated in 1:500 goat anti-rabbit HRP secondary antibody (Jackson ImmunoResearch, 111-035-003) in 10% FBS in PBST at 4°C overnight. Next, embryos were washed at least five times in PBST, then once in TSA 1x amplification buffer (TSA Plus Cyanine 3 System, Perkin Elmer, NEL744001KT). For staining, embryos were incubated in 75 μl 1:75 Cy3-TSA in 1x amplification buffer in the dark at room temperature for 45 min. After washing at least six times with PBST, embryos were incubated in 1:5000 DAPI (Life Technologies, D1306; stock concentration: 5 mg/ml) in PBST at room temperature for at least 1 h, then washed at least four times with PBST. Finally, embryos were wrapped in aluminum foil and stored at 4°C overnight before SPIM imaging.

## pErk

Embryos were washed at least three times with PBST, then transferred to ice-cold acetone for 20 min and washed at least three times with PBST. After blocking in 10% FBS in PBST for at least 1 h, embryos were incubated in 1:5000 mouse anti-pErk antibody (Sigma, M8159) in 10% FBS in PBST at 4°C overnight. Embryos were then washed at least five times in PBST, blocked again for at least 1 h in 10% FBS in PBST, and incubated in 1:500 donkey anti-mouse HRP secondary antibody (Jackson ImmunoResearch, 715-035-150) in 10% FBS in PBST at 4°C overnight. Embryos were washed at least five times with PBST, then once in TSA 1x amplification buffer. Next, embryos were incubated in 75 μl 1:75 Cy3-TSA in 1x amplification buffer in the dark at room temperature for 45 min. After washing at least six times with PBST, embryos were incubated in 1:5000 DAPI (Life Technologies, D1306; stock concentration: 5 mg/ml) in PBST at room temperature for at least 1 h, then washed at least four times with PBST. Stained embryos were wrapped in aluminum foil and stored at 4°C overnight before SPIM imaging.

## Fluorescence and colorimetric in situ hybridization

BMP target gene probes were generated by amplifying full or partial coding sequences (CDS) from wild type TE zebrafish cDNA and cloning into pCS2+ or pCR-bluntII TOPO (ThermoFisher, 450245) vectors. Plasmids were linearized with the indicated restriction enzymes, column purified (Promega, A9282), and DIG-labeled probes were generated using the indicated polymerase (Roche, 11175025910).

High-confidence BMP target gene in situ hybridization probes:

GeneVectorSequenceEnzymePolymeraseapoc1lpCS2+entire CDSClaIT7bambiapCR-bluntII TOPOpartial CDS; bp 47–425BamHIT7bmp4pCR-bluntII TOPOpartial CDS; bp 103–558EcoRVSP6cdx4pCR-bluntII TOPOpartial CDS; bp 132–810EcoRVSP6crabp2bpCR-bluntII TOPOpartial CDS; bp 14–436EcoRVSP6eve1pCR-bluntII TOPOpartial CDS; bp 42–665BamHIT7foxi1pCS2+entire CDSClaIT7gata2apCR-bluntII TOPOpartial CDS; bp 40–1141SpeIT7id2apCR-bluntII TOPOpartial CDS; bp 6–401BamHIT7klf2bpCS2+entire CDSClaIT7smad6apCR-bluntII TOPOpartial CDS; bp 8–880BamHIT7smad7pCR-bluntII TOPOpartial CDS; bp 23–1024BamHIT7sizzledpCS2+entire CDSClaIT7tfap2cpCS2+entire CDSClaIT7vedpCR-bluntII TOPOpartial CDS; bp 7–825EcoRVSP6znfl2bpCR-bluntII TOPOpartial CDS; bp 25–435BamHIT7

Note that the znfl2b in situ probe contained 47 SNPs compared to the reference genome (Danio rerio GRCz11).

The same DIG-labeled probes were used for both fluorescence (Figures 1F–Y and 7F–J, Figure 7—figure supplement 1K–O, and Figure 7—figure supplement 3) and colorimetric (Figure 1—figure supplement 1C–D and Figure 5—figure supplement 1A–F) in situ hybridization at a concentration of 1 ng/μl.

Whole-mount colorimetric in situ hybridization was carried out as described previously (Thisse and Thisse, 2008). Embryos were fixed in 4% formaldehyde in PBS, incubated at 4°C overnight, then transferred to MeOH and stored at −20°C for at least 2 h. Stained embryos were imaged in 2:1 benzyl benzoate:benzyl alcohol with an Axio Zoom.V16 microscope (ZEISS).

For fluorescence in situ hybridization (FISH), the same protocol was used until the blocking step, at which point embryos were blocked in FISH blocking buffer (2% blocking reagent (Roche, 11096176001) in 1x maleic acid buffer (100 mM maleic acid, 150 mM NaCl, 180 mM NaOH, 0.1% Tween)) for at least 2 h at room temperature with gentle rocking, then incubated at 4°C overnight in 1:150 anti-DIG-POD (Roche, 11207733910). The following day embryos were washed at least five times with PBST. To develop signal, embryos were incubated in 75 μl 1:75 Cy3-TSA in 1x amplification buffer (TSA Plus Cyanine 3 System, Perkin Elmer, NEL744001KT) for 30 min at room temperature in the dark. Embryos were then washed at least five times with PBST, incubated in 1:5000 DAPI (Life Technologies, D1306; stock concentration: 5 mg/ml) with agitation at room temperature for at least 1 h (or overnight at 4°C), then washed at least five times with PBST. One day after Cy3 incubation, embryos were imaged on a ZEISS Lightsheet Z.1 (see below and Figure 1—figure supplement 1E for imaging and quantification details). All FISH embryos shown in Figure 1F–Y were fertilized and fixed on the same day.

## SPIM imaging of immunofluorescence staining and fluorescence in situ hybridization

Fixed embryos were mounted in 1% low melting temperature agarose (Lonza, 50080) using a glass capillary and imaged with a ZEISS Lightsheet Z.1 selective plane illumination microscope (SPIM). The imaging chamber was filled with water, and filters and light sheets were auto-aligned prior to imaging. For fluorescence in situ hybridization (FISH) and pSmad1/5/9 immunofluorescence (IF) experiments, embryos were positioned using the DAPI signal with the animal pole pointing toward the imaging objective to produce animal views; for ventral views, embryos in the correct orientation were rotated 90°. For animal views, 50–90 z-slices with 7 μm between each slice were acquired per embryo, covering the entire blastoderm over a distance of 350–630 μm depending on embryo size. For ventral views, ~70 z-slices with 7 μm between each slice were acquired per embryo, spanning roughly half of the embryo.

For pSmad2/3 and pErk IF, embryos were mounted in the orthogonal orientation compared to pSmad1/5/9 and FISH experiments, and three lateral images were acquired per embryo: one at the brightest region, a second rotated 120°, and a third rotated 240°.

All images were acquired with dual light sheet illumination using a W Plan-Apochromat 20x objective at 0.5x zoom and the imaging conditions described below.

SPIM imaging conditions:

ExperimentSignalFluorophoreLaser wavelength (nm)Laser intensityFilterExposure (ms)pErk IFpErkCy35611.5%BP 575–615100NucleiDAPI4051.5%BP 420–470100pSmad2/3 IFpSmad2/3Cy35611%BP 575–615100NucleiDAPI4051.1%BP 420–470100pSmad1/5/9 IFpSmad 1/5/9Alexa4884882%BP 505–545200NucleiDAPI4051.3%BP 420–470200All FISH except SB-treatedFISHCy35611.5%BP 575–615100NucleiDAPI4051.5%BP 420–470100SB-treated FISHFISHCy35611%BP 575–615100NucleiDAPI4051.1%BP 420–470100

Maximum intensity projections were generated using the software ZEN (2014 SP1, black edition) and used for the analyses described below.

## Mathematical modeling of target gene induction and decay kinetics

To estimate induction and decay of transcripts from the NanoString data (Figure 4), time-dependent pSmad1/5/9 and transcript changes were modeled mathematically. The change in the amount of endogenous (Pe) and optogenetically induced (Po) pSmad1/5/9 levels can be described by the following general differential equations:dPedt=G˙(t)dPodt=H˙(t)

The observed pSmad1/5/9 levels in uninjected embryos correspond to G(t), whereas the observed pSmad1/5/9 levels (Ps) in light-exposed Opto-BMP embryos correspond to the sum of G(t) and H(t). Therefore, the change in the amount of Ps over time can be described by:dPsdt=G˙(t)+H˙(t)=I˙(t)

Thus, the levels of optogenetically induced pSmad1/5/9 can be calculated by subtracting the pSmad1/5/9 levels in uninjected embryos from the pSmad1/5/9 levels in light-exposed Opto-BMP embryos:It-Gt=H(t)

Similarly, changes in the endogenous transcript levels (Te) and optogenetically induced transcript levels (To) over time can be described by the following general differential equations:dTedt=K˙(t)dTodt=L˙(t)

The observed transcript levels in uninjected embryos correspond to K(t), whereas the observed transcript levels (Ts) in light-exposed Opto-BMP embryos correspond to the sum of K(t) and L(t). The change in the amount of Ts over time can therefore be described by:dTsdt=K˙(t)+L˙(t)=M˙(t)

Thus, the levels of optogenetically induced transcripts can be calculated by subtracting the transcript levels in uninjected embryos from the transcript levels in light-exposed Opto-BMP embryos:Mt-Kt=L(t)

## Modeling method 1

The NanoString transcription data was first analyzed using the simplest model of induction and decay (Figure 5):dTodt=σPo−λTowhere Po represents the optogenetically induced pSmad1/5/9 input, To the pSmad1/5/9-dependent target gene, σ the induction rate constant, and λ the decay rate constant of the induced gene. Po was obtained by fitting the measured pSmad1/5/9 immunofluorescence data H(t) (Figure 3C, Figure 5L, and Figure 3—figure supplement 1J) with a polynomial of degree five using the function polyfit in MATLAB 7.10.0 (R2010a). The induction-decay model was simulated in COMSOL Multiphysics 3.5a in a 10 μm domain (representing approximately one cell) with no-flux boundary conditions and an initial concentration To(0).

For each experiment, the combination of parameters To(0), σ, and λ was found that minimizes the sum of squared differences (SSD)SSD=∑n(Ltn-Totn)2between the simulations of the induction-decay model To(tn) and the data L(tn) for all measured time points n.

The minimization was performed numerically using a constrained optimization algorithm (Nelder-Mead, MATLAB 7.10.0) with zero for the initial guesses of To(0), σ, and λ, and a maximum of 500 iterations. σ and λ were constrained between biologically plausible values of 0.00001/s and 0.1/s, and To(0) was bounded between −100 a.u. and 100 a.u. R2 values were calculated from the minimizing SSD (SSDmin) to assess the goodness of the fits byR2=1−SSDmin∑n(L(tn)−1n∑nL(tn))2

Fitted values for high-confidence BMP target genes, experimental repeat 1:

Target geneσ (1/s)λ (1/s)To(0) (a.u.)R2bambia0.0004140.000879−95.840.9125bmp40.0000760.000452−42.710.7060cdx40.0002200.000434−81.480.6871crabp2b0.0000410.00001010.270.0951eve10.0002330.000514−20.490.7132foxi10.0003710.000835−91.100.7821gata2a0.0001050.000336−46.010.6056id2a0.0001110.000539−20.540.7354klf2b0.0003940.0012625.3690.6880smad6a0.0000160.0006701.6060.1780smad70.0001160.000765−65.540.8043sizzled0.0002220.000605−82.090.6470tfap2c0.0000410.000153−15.900.1922ved0.0005900.000590−100.00.8072

Fitted values for high-confidence BMP target genes, experimental repeat 2:

Target geneσ (1/s)λ (1/s)To(0) (a.u.)R2bambia0.0003440.00056490.730.6248bmp40.0000660.000474−17.100.6114cdx40.0001690.000170−26.840.2825crabp2b0.0000560.000010−43.720.2517eve10.0001580.0003947.770.6689foxi10.0004130.001217−14.670.7806gata2a0.0001110.000399−71.030.5647id2a0.0001410.000522−35.840.6967klf2b0.0007080.003101−62.700.6394smad6a0.0000290.000340−6.3260.3140smad70.0001120.000613−54.510.7397sizzled0.0002170.000692−99.990.6918tfap2c0.0000560.000160−27.150.4203ved0.0005880.000554−100.00.7354

Fitted values for high-confidence BMP target genes, experimental repeat 3:

Target geneσ (1/s)λ (1/s)To(0) (a.u.)R2bambia0.0006400.001045−99.990.9362bmp40.0000940.000455−73.000.7986cdx40.0001810.000468−99.810.5390crabp2b0.0000870.000010−87.630.4399eve10.0003340.000568−100.00.7789foxi10.0005050.001174−6.0520.8502gata2a0.0001480.000491−65.450.8464id2a0.0001260.0005799.4760.8000klf2b0.0005050.001407−100.00.6530smad6a0.0000510.000563−25.920.8935smad70.0000950.000553−19.750.5364sizzled0.0002900.000721−100.00.7169tfap2c0.0000450.000378−38.420.4709ved0.0006020.000489−100.00.6802

Average fitted values for high-confidence BMP target genes:

Target geneσ (1/s)λ (1/s)To(0) (a.u.)MeanStdevMeanStdevMeanStdevbambia0.000470.000150.000830.00024−35.04108.9bmp40.000080.000010.000460.00001−44.2727.98cdx40.000190.000030.000360.00016−69.3837.96crabp2b0.000060.000020.000010.00000−40.3649.04eve10.000240.000090.000490.00009−37.5755.88foxi10.000430.000070.001080.00021−37.2746.81gata2a0.000120.000020.000410.00008−60.8313.13id2a0.000130.000020.000550.00003−15.6323.05klf2b0.000540.000160.001920.00102−52.4453.43smad6a0.000030.000020.000520.00017−10.2114.17smad70.000110.000010.000640.00011−46.6023.90sizzled0.000240.000040.000670.00006−94.0310.34tfap2c0.000050.000010.000230.00013−27.1511.26ved0.000590.000010.000540.00005−100.00.000

## Modeling method 2

In a second approach (Figure 5—figure supplement 1G–W), the NanoString transcription data was fitted with the analytical solutions to the differential equation systemdPedt=k1-k2PedPodt=k3θt-θt-tL-k2PodTedt=k4Pe-k5TedTodt=σPo−λTowhich describes the changes in endogenous as well as optogenetically induced pSmad1/5/9 and transcript levels based on the simplest model of induction and decay after an optogenetic pulse of length tL (i.e., 30 min = 1800 s for all experiments). k1 represents the activation rate of endogenous pSmad1/5/9, k2 the decay rate constant of pSmad1/5/9, and k3 the activation rate of optogenetically induced pSmad1/5/9. Optogenetic switch-like activation was modeled with the Heaviside step function θ. k4 and k5 represent the activation rate and decay rate constants of endogenously induced BMP-dependent transcripts, and σ and λ are the induction rate and decay rate constants of the induced gene.

The analytical solutions to this equation system are:Pet=e-k2tδPe+k1k2Po(t)=1k2(k3(θ(tL)−θ(tL−t))e−k2(t−tL)+k3θ(tL−t)+(−k3θ(t)−θ(tL)k3+δPok2+k3)e−k2t+k3(θ(t)−1))Te=1k2k5(k2−k5)(k2k5(δPek4+δTek2−δTek5)e−k5t+(−k2k5δPee−k2t+k1(k2−k5))k4)To=1(k2−λ)k2λ(−σk3λ(θ(tL)−θ(tL−t))e−k2(t−tL)+ σk2k3(θ(tL)−θ(tL−t))e−λ(t−tL)+σk3(k2−λ)θ(tL−t)−k2(θ(tL)k3σ+σk3θ(t)+(−δPoλ−k3)σ−λδTo(k2−λ))e−λt+σ(λ(θ(tL)k3+k3θ(t)−δPok2−k3)e−k2t+k3(θ(t)−1)(k2−λ)))withPe0=δPe+k1k2Po0=δPoTe0=δTe+k1k4k2k5To0=δTo

The pSmad1/5/9 data was fitted with the computer algebra system Maple (Waterloo Maple Inc) using the function LSSolve to minimize the difference between the pSmad1/5/9 data in uninjected embryos and Pe(t), as well as the difference between the pSmad1/5/9 data in light-exposed Opto-BMP embryos and Pe(t) + Po(t) with the initial guesses δPe=0 a.u., δPo=0 a.u., k1=0/s, k2=0.00167/s, k3=0/s, k4=00167/s and a maximum of 20000 iterations and an optimality tolerance of 0.3981071706 × 10−14. The best fitting parameters δPe=-76.19 a.u, δPo=264.1 a.u., k1=0.1429 a.u./s, k2=0.000900/s, and  k3=0.954 a.u./s were then used for the simulation of the gene induction dynamics in the NanoString data.

The NanoString data was fitted in Maple using the function LSSolve to simultaneously minimize the difference between the NanoString data in uninjected embryos and Te(t), as well as the difference between the NanoString data in light-exposed Opto-BMP embryos and Te(t) + To(t) with the initial guesses δTe=0 a.u., δTo=0 a.u., k4=0/s, k5=0.00167/s, σ=0/s, λ=0.00167/s and a maximum of 10000 iterations and an optimality tolerance of 0.3981071706 × 10−14.

Fitted values for high-confidence BMP target genes:

Target geneσ (1/s)λ (1/s)δTe (a.u.)δTo (a.u.)R2bambia0.0003270.000671520.416.010.7509bmp40.0000700.000362171.2−41.520.7912cdx40.0002380.000550−1331−29.220.8682crabp2b0.000048−0.000191−310.9−40.270.8111eve10.0001770.000313950.7−52.740.8599foxi10.0004010.00009447.34−72.260.5592gata2a0.0001440.00042762.39−77.720.4272id2a0.0001430.000449231.3−21.140.7586klf2b0.0004190.0011149.959−97.860.5082smad6a0.0000300.00031849.62−15.670.3307smad70.0001250.000626122.9−54.500.7043sizzled0.0002740.000758238.9−120.70.5116tfap2c0.0000620.00031644.54−31.750.1597ved0.0007320.0005311200−403.00.8063

## Inhibition of Nodal and FGF signaling with small molecule inhibitors

The Nodal inhibitor SB-505124 (Sigma, S4696-5MG) (Soh et al., 2020; Almuedo-Castillo et al., 2018; Rogers et al., 2017; van Boxtel et al., 2015; Vogt et al., 2011; Fan et al., 2007; Hagos and Dougan, 2007; Hagos et al., 2007; DaCosta Byfield et al., 2004) and the FGF inhibitor SU-5402 (Sigma SML0443-5MG) (van Boxtel et al., 2015; Poulain et al., 2006; Londin et al., 2005; Fürthauer et al., 2004; Kudoh et al., 2004; Mathieu et al., 2004; Mohammadi et al., 1997) were diluted to 10 mM in DMSO (Roth, A994.2), aliquoted, and stored at −20°C. Aliquots were thawed the same day that experiments were carried out and were not re-used. 10 mM stocks of SB-505124 and SU-5402 were diluted to 50 and 10 μM, respectively, in embryo medium the day of each experiment. 5 ml diluted inhibitors were then dispensed into each well of agarose-coated (Sigma, A9539) 6-well plates (Greiner Bio-One, 657160), and plates were incubated at 28°C at least 30 min before embryos were added.

## Quantification of pSmad1/5/9 immunofluorescence staining and fluorescence in situ hybridization

To measure spatial intensity profiles along the dorsal-ventral axis (Figure 1—figure supplement 1E) from pSmad1/5/9 immunofluorescence experiments (IF) (Figures 1D–E and 7A–E, Figure 7—figure supplement 1A–J’, and Figure 7—figure supplement 2A–K) and BMP target gene fluorescence in situ hybridization (FISH) (Figure 1P–Y, Figure 7F–J, and Figure 7—figure supplement 3), maximum intensity projections of animal views were manually rotated in Fiji (Schindelin et al., 2012) with ventral to the left (brightest signal) and dorsal to the right (dimmest signal; for the very early pSmad1/5/9 images prior to clear onset of BMP signaling, embryos were oriented with the brightest side on the left and the dimmest on the right where obvious, but correspondence with ventral-dorsal is not clear in those early cases). A polygonal region of interest (ROI) was then manually drawn around the embryo and used to create a mask in order to remove image background (for FISH experiments, the Cy3 signal was used to draw the mask; for IF experiments the DAPI signal was used). The average pixel intensity in each column of pixels from ventral to dorsal was then acquired (pixel area: 0.46 μm × 0.46 μm). For genes that are restricted to the margin (cdx4 and eve1), a second manually positioned circular ROI was used to exclude the non-margin region of the embryo (Figure 1—figure supplement 1E).

For FISH experiments, non-probe-exposed control embryos for background subtraction were imaged and intensity profiles acquired as described above. The orientation of these background subtraction embryos was random. Images for background subtraction controls were acquired in the same imaging session as experimental FISH images.

After intensity profiles were acquired, absolute distance was converted into percent embryo length to account for embryo-to-embryo variability in size, and intensity measurements were averaged into bins of 0.5% embryo length using an automated routine (0 < bin 1 < 0.5%, 0.5 < bin 2 < 1%, etc.).

For FISH experiments, the average intensity at each position in all 10 non-probe-exposed background embryos was calculated. This spatial background average was subtracted from each experimental FISH raw intensity profile, and data from the first and last 5% embryo length was excluded because the averages at the most ventral and dorsal regions are composed of relatively few pixels and are therefore less reliable.

The profiles of individual embryos were normalized following the procedure in Gregor et al., 2007 using the modelIn(x)=Anc-x+bnwhich relates the mean intensity profile c-x of all data points for a given target gene to the intensity profile In(x) for an embryo n through the embryo-specific proportionality constant An and the nonspecific background bn. An and bn were determined by minimizing the objective function∑i(In(xi)−(Anc−(xi)+bn))2for the data points at all positions xi with the Nelder-Mead algorithm using the function fminsearch in MATLAB 7.10.0, the initial guesses 1 and 0 for An and bn, a maximum of 10000 function evaluations, and a maximum of 5000 iterations. For display, each average profile was then divided by its maximum intensity (Figure 1P-Y, Figure 7F-J, and Figure 7—figure supplement 3).

The Gaussian function Ae-x-μ2ς was fitted to each profile using a constrained Nelder-Mead algorithm in MATLAB 7.10.0 with a maximum of 10000 function evaluations, a maximum of 5000 iterations, the initial guesses 300, 20, and 10000, the lower bounds 300, -50, and 100, and the upper bounds 100000, 50, and 100000 for A, µ, and ς, respectively. Gene expression range was defined as r=μ+2ς/2. The resulting ranges from 9-10 embryos were averaged to define each gene’s mean range.

For pSmad1/5/9 IF spatial quantification experiments, the average image background intensity was determined for each image using a small ROI in the corner outside of the embryo, and subtracted from each IF raw intensity profile. Since the averages at the most ventral and dorsal regions are composed of relatively few pixels and are therefore less reliable, data from the first and last 5% embryo length was not considered. The mean of the dorsal-most 5% at 2.75 hpf was then subtracted from all profiles. These profiles were then normalized as described above for the FISH data, assuming embryo-specific constant nonspecific background and proportionality constants that relate immunofluorescent staining intensity to protein concentration.

Number of embryos assessed in spatial quantification experiments:

ExperimentFig.Number of embryosFISHAll except apoc1l in bmp-overexpressing embryos1P-Y, 7 F-J, 7.310apoc1l in bmp-overexpressing embryos7J, 7.3A9pSmad 1/5/9 IFTime course in untreated and SU-5402/SB-505124-treated embryos1E,7A, 7.2A-K8–9Untreated and bmp-overexpressing embryos7E, 7.1A-A’10Untreated and SU-5420-treated embryos7B, 7.1D-D’10Untreated and SB-505124-treated embryos7C, 7.1 F-F’9–10Untreated and SU-5402/SB-505124-treated embryos7D, 7.1 H-H’10

To quantify total pSmad1/5/9 IF intensity (Figures 3C–E and 6B, and Figure 3—figure supplement 1I,J), an ROI was manually drawn around the embryo in Fiji based on DAPI signal and used to create a mask in order to remove image background as described above. The average intensity within the ROI was then calculated.

For experiments shown in Figure 3C–D and Figure 3—figure supplement 1I, image background intensity was measured using a small ROI in the corner of each image outside of the embryo. The average image background was then subtracted from the embryo intensity measurements to generate background-subtracted intensities.

For shield-stage experiments shown in Figure 3C,E, Figure 5L, Figure 6B, and Figure 3—figure supplement 1J, the average intensity within a small ROI on the dorsal side was measured in uninjected embryos; for each time point, these values were averaged and subtracted from the embryo intensity measurements to generate background-subtracted intensities.

Number of embryos assessed in total pSmad1/5/9 IF quantification time course experiments:

ExperimentFig.Number of embryosHigh-stage BMP signaling pulse3C, 3.1I5Shield-stage BMP signaling pulse3C, 5L, 3.1J5Low- and high-amplitude BMP signaling pulse6B5 uninjected7 Opto-BMP

## NanoString RNA quantification

For the NanoString time course experiment in untreated (Figure 2) and FGF/Nodal-inhibitor-treated embryos (Figure 7—figure supplement 2L-ZA), embryos from wild type TE incrosses were collected ~15 min after mating commenced. Embryos were incubated at 28°C, dechorionated using Pronase (Roche, 11459643001) at ~1.5 hpf, and sorted into 10 agarose-coated 6-well plates, one plate per time point. Each plate had one well containing embryo medium and one well containing FGF/Nodal inhibitor. To keep temperature and therefore development steady, plates were only removed from the 28°C incubator immediately prior to embryo collection. Every 30 min from 2.75 to 7.25 hpf, treated and untreated embryos were snap-frozen in liquid nitrogen.

For NanoString experiments quantifying responses to BMP signaling pulses using Opto-BMP (Figures 4, 5 and 6, Figure 5—figure supplement 1J–W, and Figure 6—figure supplement 1), embryos from TE incrosses were dechorionated using Pronase and injected at the one-cell stage with 5.2 pg opto-Alk3 + 5.2 pg opto-Alk8 + 8.9 pg opto-BMPR2a mRNA (Figure 3—figure supplement 1A). Control siblings were left uninjected, and embryos were sorted into agarose-coated 6-well plates and incubated at 28°C. 70–90 min post-fertilization at the 4–16 cell stage, unfertilized and damaged embryos were removed, and plates were individually wrapped in aluminum foil and incubated at 28°C. At the appropriate time, individual plates were transferred to a small 28°C incubator containing the LED array, exposed to light for the appropriate duration, and embryos were either snap-frozen in liquid nitrogen immediately (e.g., for the 10 min during exposure time point), or re-wrapped in aluminum foil and returned to 28°C incubation in the dark (e.g., for the 80 min post-exposure time point).

RNA was prepared as described for the RNA-sequencing experiment. 30 μl aliquots at 20 ng/μl were provided to Proteros GmbH (Planegg-Martinsried, Germany) for analysis using a custom-designed NanoString nCounter Elements TagSet with probes targeting high-confidence BMP target genes identified by RNA-sequencing, and housekeeping genes for normalization. Samples were measured using an nCounter SPRINT according to the standard protocol with a 24–30 h hybridization length.

nSolver 4.0 software (https://www.nanostring.com/products/analysis-software/nsolver) was used to subtract background and normalize the RNA count data using the geometric means of the positive spike-in controls and the housekeeping genes eef1a1l1 and act2b, respectively. Lanes that failed quality control were repeated.

Number of embryos assessed in NanoString experiments:

ExperimentFig.Number of embryosTime course from 2.75 to 7.25 hpfUntreated embryos2, 7.2L-ZA25SU-5402/SB-505124-treated embryos7.2L-ZA20–25High-stage BMP signaling pulse421–25Shield-stage BMP signaling pulse4, 5, 5.1I-W19–25Low- and high-amplitude BMP signaling pulse6 C-F, 6.125

Each of the experiments described in the table above was repeated three times.

For experiments in which transcriptional responses to BMP signaling pulses are assessed (Figures 4, 5 and 6C–F, and Figure 6—figure supplement 1), it is necessary to determine changes in transcript levels compared to uninduced embryos. Because each of the three sets of Opto-BMP embryos had uninjected control siblings collected at the same time, average induction was calculated by first subtracting the uninjected transcript count from its corresponding injected sibling count, then by averaging the three subtracted counts (also see the section Mathematical modeling of target gene induction and decay kinetics above for a formal description of this procedure).

## Calculation of spatial coefficients of variation

The spatial coefficient of variation (Figure 7N) for each condition (untreated, bmp-overexpressing, +SB-505124, + SU-5402, and +SB-505124 and SU-5402) was calculated as follows: First, at each position x, the average normalized intensityμ(x)=1n∑i=1nIi(x)and standard deviationσx=1n-1∑i=1nIix-μ(x)2for all n genes quantified by FISH were determined (Figure 7F–J). Next, the standard deviation was divided by the average normalized intensity at that positioncv(x)=σ(x)μ(x)

This was repeated for every position along the dorsal-ventral axis for all five conditions to calculate the spatial coefficients of variation for the 10 measured genes.

## Statistical analyses

In the following experiments, significance was defined as a p-value≤0.05 using an unpaired two-tailed Student’s t-test assuming equal variance in Excel.

To determine how light exposure at different developmental stages affects BMP signaling in Opto-BMP embryos, total pSmad1/5/9 immunofluorescence intensity was quantified in uninjected and Opto-BMP-injected embryos exposed to light at high (3.5–4 hpf) or shield (6.75–7.25 hpf) stage (Figure 3C–D and Figure 3—figure supplement 1I,J).

Early and late light exposure, Opto-BMP versus uninjected p-values (Figure 3C–D and Figure 3—figure supplement 1I,J):

Time post-exposure (min)High stage (early)Shield stage (late)−300.0650.003−200.0291.422 × 10−5−100.0017.732 × 10−701.189 × 10−51.610 × 10−6102.052 × 10−61.181 × 10−5200.0026.800 × 10−6350.0770.407550.0210.016800.4550.0251100.9480.135

To determine how different light intensities affect BMP signaling in Opto-BMP embryos, total pSmad1/5/9 immunofluorescence intensity was quantified in uninjected and Opto-BMP-injected embryos exposed to low (70 lux) or high (3900 lux) intensity light for 10 or 20 min (Figure 6B).

Low- and high-intensity light, Opto-BMP versus uninjected p-values (Figure 6B):

Time post-exposure (min)70 lux, 10 min3900 lux, 10 min70 lux, 20 min3900 lux, 20 min00.4190.0200.0130.97550.7820.782NDND100.3280.0030.4930.001150.0010.0004NDND200.0970.00040.0090.001300.5830.0120.00020.00003400.0590.0180.3678.656 × 10−750NDND0.3670.729

To determine whether BMP target gene expression domain boundaries differ significantly in untreated embryos, range was defined in individual embryos as described in the section Quantification of pSmad1/5/9 immunofluorescence staining and fluorescence in situ hybridization. Ranges were then averaged.

BMP target gene range comparison p-values (Figure 1P–Y):

bambiacdx4eve1foxi1gata2aklf2bsizzledtfap2cvedapoc1l0.01220.1363.27 × 10−49.47 × 10−50.6820.3711.06 × 10−60.0036.79 × 10−5bambia4.44 × 10−61.06 × 10−51.2 × 10−90.1299.95 × 10−51.12 × 10−182.70 × 10−51.58 × 10−8cdx43.38 × 10−82.70 × 10−110.5110.1383.67 × 10−175.59 × 10−92.15 × 10−10eve10.1820.0102.64 × 10−75.40 × 10−80.0010.081foxi10.0045.70 × 10−91.66 × 10−92.09 × 10−70.466gata2a0.8381.07 × 10−40.0490.003klf2b1.26 × 10−122.01 × 10–68.46 × 10−9sizzled7.92 × 10−185.19 × 10−7tfap2c1.33 × 10−6

The shape of the temporal BMP target gene expression profiles assessed by NanoString in untreated and SU-5402/SB-505124-treated embryos can be well approximated by the modified cumulative distribution function of the normal distribution12A1+erf⁡x-ντ2+bwhich was used for regression analysis using a constrained Nelder-Mead algorithm in MATLAB 7.10.0 with a maximum of 10000 function evaluations, a maximum of 5000 iterations, the initial guesses 1000, 5 h, 1 h, and 100, the lower bounds 100, 3 h, 0.05 h, and 0, and the upper bounds 10000, 7 h, 3 h, and 1000 for A, ν, τ, and b, respectively. The activation time of each BMP target gene was defined as the average time point at which the curves reached about two mean average deviations (i.e., 1.5∙τ) from the inflection point ν (Figure 2 and Figure 7—figure supplement 2L-Y). id2a (Chong et al., 2005) and smad6a (White et al., 2017) were excluded from this analysis because they are maternally contributed.

To determine whether FGF/Nodal loss affects the timing of gene activation, activation times in untreated versus SU-5402/SB-505124-treated samples were compared (Figure 7—figure supplement 2L–Y).

SU-5402/SB-505124-treated versus untreated activation time p-values (Figure 7—figure supplement 2L–Y):

bambiabmp4cdx4crabp 2beve1foxi1gata 2aklf2bsmad7sizzledtfap2cved0.4460.2480.5510.3460.4500.1840.0430.7600.5710.2010.0820.333

To identify differences in BMP target gene expression in the absence of FGF/Nodal signaling, transcript counts from SU-5402/SB-505124-treated embryos were compared to counts from untreated embryos (Figure 7—figure supplement 2L–Y).

SU-5402/SB-505124-treated versus untreated p-values (Figure 7—figure supplement 2L–Y):

hpfbambiabmp4cdx4crabp 2beve1foxi1gata 2aid2aklf2bsmad 6asmad7sizzledtfap 2cved2.750.7960.6770.7700.3890.8350.6540.6750.9610.6520.5780.8260.8240.8970.9683.250.7570.5900.8550.9050.5730.7900.3860.9460.3410.9180.7040.4970.5140.6823.750.6950.7490.9410.9510.5930.7910.8040.7000.7290.1590.8160.8540.2450.8184.250.5650.9540.6500.4340.5610.6610.5900.7200.8550.7850.3580.2580.5210.7514.750.9880.9430.9960.6550.6450.7510.9190.9650.8200.4600.6430.2240.6300.9475.250.9100.4770.5540.9960.9270.8740.7590.7330.8770.5110.5610.0950.4890.8005.750.8770.3230.6220.4050.2370.3240.0830.5890.1080.7390.6150.1220.3190.9266.250.4430.5090.7310.3990.4500.1490.0910.7670.0850.9380.9660.0770.1050.4836.750.4930.5960.7130.3250.7230.0410.0380.1630.0220.4150.1200.0060.0230.1037.250.3460.0780.6570.2620.8740.0210.0140.2560.0110.0670.0550.0080.0190.020

For experiments in which transcriptional responses to BMP signaling pulses at high or shield stage were measured using NanoString (Figures 4 and 5M–Z), mRNA counts in Opto-BMP-injected embryos were compared to uninjected embryos.

High-stage BMP signaling pulse, Opto-BMP versus uninjected p-values (Figure 4):

Time post-exposure (min)bambiabmp4cdx4crabp2beve1foxi1gata 2aid2aklf2bsmad6asmad7sizzledtfap2cved−300.2740.3810.2790.3620.4280.6100.4010.3150.5730.1730.9830.2950.2830.312−200.2700.4190.2250.1440.3860.0510.3540.2750.3640.3010.8970.4560.1710.124−100.2320.2730.7990.5010.5630.0190.8740.5700.3590.3980.7110.2490.9000.52700.0190.1810.0530.4830.0040.0710.1520.4590.0530.7320.1670.0160.0010.169100.0050.5390.7600.1360.0310.0020.1680.0400.0430.7930.1240.00010.0120.017200.0020.0340.1900.9020.0020.0830.0210.0010.0670.1560.0070.0010.0190.060350.0020.0020.4580.7260.0060.00020.0020.0170.0980.8970.00030.00040.00010.001550.1130.1390.9120.5660.0330.2420.0430.0040.1820.2140.0970.0830.0430.138800.1750.0690.4970.0610.1660.3100.0030.0080.8070.2790.2870.8040.0790.6231100.0560.4490.7930.3560.2090.4400.4630.4020.2260.7600.0840.0060.3570.214

Shield-stage BMP signaling pulse, Opto-BMP versus uninjected p-values (Figures 4 and 5M–Z, and Figure 5—figure supplement 1J–W):

Time post-exposure (min)bambiabmp4cdx4crabp2beve1foxi1gata 2aid2aklf2bsmad6asmad7sizzledtfap2cved−300.5440.4010.9830.5220.8690.4230.3820.9090.2780.8280.1680.1540.6670.003−200.1110.0690.7270.4400.6860.4740.1160.2420.0840.7310.5090.9830.6310.483−100.1660.6670.6980.0980.6340.0130.5220.4890.1970.8810.8340.8200.4920.68000.0320.0710.5990.6270.0410.0050.2800.0040.0460.1360.0020.0560.7810.004100.0130.0010.0840.6580.0820.0000.0060.0130.00010.2420.0030.0050.1510.002200.0030.0020.0200.2010.0010.0000.00010.0120.0070.0450.0060.0040.0060.002350.0060.0120.0310.2540.0880.0150.0050.0020.2220.0670.0130.0750.0340.020550.4150.0010.1390.4080.1580.0110.4600.0240.0380.0440.7660.5630.0510.162800.2370.0670.7260.2310.1010.0670.6950.0890.0670.3360.3740.0310.7100.0111100.6730.0090.8280.0500.0790.5680.7830.4100.0940.2220.2140.0050.5370.049

For experiments in which transcriptional responses to low- and high-amplitude BMP signaling pulses of different durations were measured using NanoString (Figure 6C–F and Figure 6—figure supplement 1), mRNA counts from uninjected embryos were first subtracted from Opto-BMP-injected siblings. Then the subtracted counts from light-exposed embryos were compared to subtracted counts from unexposed control embryos.

Low- and high-amplitude BMP pulses, exposed versus unexposed p-values (Figure 6C–F, Figure 6—figure supplement 1):

Exp.Time into exposure (min)bambiabmp4cdx4crabp 2beve1foxi1gata 2aid2aklf 2bsmad 6asmad 7szltfap 2cved70 lux, 10 min300.0830.5970.3900.9670.4870.0210.8560.7030.2710.8940.0710.4050.8160.603400.9450.9170.2470.9280.4670.0200.7000.4360.5860.2630.0450.3090.2300.291500.0780.2340.6590.3580.1040.0460.0670.0500.3410.0810.0840.2050.0700.0793900 lux, 10 min300.1220.9670.7580.9980.3170.0200.4560.0850.1550.3430.3550.4750.5830.425400.0130.3670.0080.2960.0850.0560.1710.1540.0270.5720.0370.2610.0190.062500.0290.0130.1690.8050.5170.0300.0110.0150.1630.3320.0050.0510.1900.20670 lux, 20 min300.0010.6350.1760.6600.0370.0010.0620.0190.0020.3040.0560.0870.3210.031400.1200.3480.2170.1260.4790.0110.1720.1040.0310.2700.1810.1360.1020.250500.1210.1030.2730.1730.0750.0750.0680.0330.0420.2160.0640.0850.0310.0473900 lux, 20 min300.1780.4480.2010.2330.0610.1600.0610.0350.1540.4910.1660.2320.1220.189400.0050.1230.9340.7610.0830.0030.0750.0280.0770.0200.0010.0280.3240.033500.3240.2710.0060.6150.0770.5400.1440.3820.0620.9290.2380.1600.2250.237

## Data and code availability

The raw images, data, and source code for custom scripts used in this work are available from the corresponding author upon request. Image quantification data and differential gene expression analyses are available in the accompanying source data files and Supplementary file 1, respectively. The RNA-sequencing data has been deposited at the GEO repository (accession number: GSE135100).

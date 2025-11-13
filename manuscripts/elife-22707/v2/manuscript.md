# Global analysis of gene expression reveals mRNA superinduction is required for the inducible immune response to a bacterial pathogen

## Authors

- Kevin C Barry<sup>1</sup> ([ORCID: 0000-0003-1064-5964](https://orcid.org/0000-0003-1064-5964))
- Nicholas T Ingolia<sup>2</sup> ([ORCID: 0000-0002-3395-1545](https://orcid.org/0000-0002-3395-1545)) †
- Russell E Vance<sup>1</sup> ([ORCID: 0000-0002-6686-3912](https://orcid.org/0000-0002-6686-3912)) †

### Affiliations

1. Division of Immunology and Pathogenesis, Department of Molecular and Cell Biology University of California, Berkeley Berkeley United States
2. Division of Biochemistry, Biophysics and Structural Biology, Department of Molecular and Cell Biology University of California, Berkeley Berkeley United States
3. Cancer Research Laboratory University of California, Berkeley Berkeley United States
4. Howard Hughes Medical Institute, University of California, Berkeley Berkeley United States

† Corresponding author

## Abstract

The inducible innate immune response to infection requires a concerted process of gene expression that is regulated at multiple levels. Most global analyses of the innate immune response have focused on transcription induced by defined immunostimulatory ligands, such as lipopolysaccharide. However, the response to pathogens involves additional complexity, as pathogens interfere with virtually every step of gene expression. How cells respond to pathogen-mediated disruption of gene expression to nevertheless initiate protective responses remains unclear. We previously discovered that a pathogen-mediated blockade of host protein synthesis provokes the production of specific pro-inflammatory cytokines. It remains unclear how these cytokines are produced despite the global pathogen-induced block of translation. We addressed this question by using parallel RNAseq and ribosome profiling to characterize the response of macrophages to infection with the intracellular bacterial pathogen Legionella pneumophila. Our results reveal that mRNA superinduction is required for the inducible immune response to a bacterial pathogen.

## Introduction

Gene expression is a concerted process that is regulated at multiple steps, including transcription, mRNA degradation, translation, and protein degradation. Most global studies of gene expression have focused on the transcriptional response, but the relative importance of transcription in determining protein levels remains debated (Li et al., 2014; Schwanhäusser et al., 2011; Breker and Schuldiner, 2014; Maier et al., 2009; Vogel and Marcotte, 2012; de Sousa Abreu et al., 2009). One recent study analyzed the response of dendritic cells to lipopolysaccharide (LPS) and found that changes in mRNA levels accounted for ~90% of observed alterations in protein levels (Jovanovic et al., 2015). However, the response to infection with a virulent pathogen is certainly more complicated than the response to a purified immunostimulatory ligand such as LPS. Indeed, pathogens have evolved to disrupt or manipulate almost every cellular process involved in gene expression (Finlay and McFadden, 2006). An effective innate immune response to infection therefore requires that host cells be able to induce appropriate responses in the face of pathogen manipulation.

Inhibition of host protein synthesis is a common strategy used by many viral and bacterial pathogens to disrupt host gene expression (Mohr and Sonenberg, 2012; Lemaitre and Girardin, 2013). For example, the intracellular bacterial pathogen L. pneumophila uses its Dot/Icm type IV secretion system (T4SS) to translocate into host cells several effector proteins that block host protein synthesis, including at least four effectors that target the elongation factor eEF1A (Lemaitre and Girardin, 2013; Barry et al., 2013; Belyi et al., 2008; Fontana et al., 2011; Shen et al., 2009). Similarly, the bacterial pathogen Pseudomonas aeruginosa blocks host translation elongation by secretion of exotoxin A (Lemaitre and Girardin, 2013; Dunbar et al., 2012; Iglewski et al., 1977). Interestingly, we previously discovered that host cells respond to protein synthesis inhibition — whether by Legionella, exotoxin A, or by pharmacological agents that block translation initiation or elongation — by initiating a specific host response characterized by production of specific pro-inflammatory cytokines, including interleukin-23 (Il23a), granulocyte macrophage colony-stimulating factor (Csf2) and interleukin-1α (Il1a) (Barry et al., 2013; Fontana et al., 2011). The mechanism by which infected host cells are able to produce certain cytokines despite a global (>90%) block in protein synthesis remains unclear, but at least two distinct models have been proposed (Mohr and Sonenberg, 2012; Lemaitre and Girardin, 2013; Barry et al., 2013; Fontana et al., 2011; Dunbar et al., 2012; Fontana and Vance, 2011; McEwan et al., 2012; Chakrabarti et al., 2012). One model posits that the block in protein synthesis leads to superinduction of cytokine mRNAs that is sufficient to overcome the partial block in host protein synthesis (Barry et al., 2013; Fontana et al., 2011). Alternatively, it has been proposed that host cells may circumvent the global block in protein synthesis by selective translation of specific cytokine transcripts (Dunbar et al., 2012; Asrat et al., 2014).

To determine how host cells mount an inflammatory response when protein synthesis is disrupted, we performed parallel RNAseq and ribosome profiling (Ingolia et al., 2012, 2009, 2011) of Legionella-infected mouse primary bone-marrow-derived macrophages (BMMs). The results reveal the relative contributions of translational regulation and mRNA induction in controlling immune responses to pathogenic L. pneumophila, and support a model in which the majority of gene induction in response to pathogenic infections occurs at the level of mRNA induction. We were able to identify a subset of mRNAs that display higher-than-average ribosome occupancy, but the elevated occupancy of these mRNAs was observed in uninfected cells as well as in cells infected with L. pneumophila. We propose that mRNA superinduction provides a robust mechanism for host cells to initiate a response to infection despite pathogen-mediated disruption of host gene expression.

## Results

### mRNA superinduction mediates the host response to virulent L. pneumophila

The relative role of transcription versus translation in mediating the inducible response to an infection with a virulent bacterial pathogen remains unclear. Thus, we performed ribosome profiling (Ingolia et al., 2012, 2009, 2011) and total (rRNA-depleted) RNA sequencing of BMMs infected with L. pneumophila. BMMs were infected with a virulent ΔflaA strain, an avirulent T4SS-deficient ΔdotAΔflaA strain, or a Δ7ΔflaA strain that lacks the seven effectors associated with inhibition of host protein synthesis. RNA was isolated at 6 hr post-infection, which was the earliest we could detect significant L. pneumophila-induced translation inhibition without marked cytotoxicity (data not shown). L. pneumophila strains on the ΔflaA background were used to reduce cell cytotoxicity by avoiding the effects of NAIP5/NLRC4 inflammasome activation by flagellin (Molofsky et al., 2006; Ren et al., 2006) and we previously showed loss of flagellin does not affect blockade of host translation or the transcriptional induction of inflammatory cytokines (Barry et al., 2013). Control experiments demonstrated that ~90% of macrophages were infected with at least one bacterium under our infection conditions (Figure 1—figure supplement 1A–B).

Lysates from infected macrophages were split and used to generate ribosome profiling libraries and RNAseq libraries, thereby allowing us to compare directly the mRNA levels and ribosome occupancy of those mRNAs from the same cells. As a confirmation of the quality of the ribosome profiling libraries, ribosome footprints were found to map preferentially to the exonic regions of infection-induced genes (Figure 1), and showed a strong bias toward 27–28 nucleotide fragment lengths (Figure 1—figure supplement 2), consistent with the known size of ribosome-protected footprints. In accord with previous studies, induction of ribosome footprints on Gem, Csf2, and Il23a required the seven-bacterial effectors associated with the block in host protein synthesis, while induction of ribosome footprints corresponding to Il1a and Il1b required the bacterial T4SS (Figure 1A–F).

![Figure 1.](https://cdn.elifesciences.org/articles/22707/elife-22707-fig1-v2.jpg)

**Figure 1.:** (A–F) Ribosome footprint reads were mapped to the genome and the number of footprints on the mRNAs for Gapdh (A), Csf2 (B), Gem (C), Il23a (D), Il1a (E), and Il1b (F) was visualized. Numbers in parentheses show the total read count of ribosome footprints found on the indicated transcript. Bracketed numbers represent read count data range. Gray, uninfected BMMs. Red, ΔflaA-infected BMMs. Green, ΔdotAΔflaA-infected BMMs. Blue, Δ7ΔflaA-infected BMMs.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/22707/elife-22707-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A–B) ΔflaA or ΔdotAΔflaA L. pneumophila-infected BMMs were stained to mark extracellular (blue) and all bacteria (red). (A) Representative image of ΔflaA L. pneumophila-infected BMMs showing extracellular (blue and red stain, blue arrow) and intracellular (red stain only, yellow arrow) bacteria. (B) Individual BMMs (n = 1375) were analyzed for the presence of at least one intracellular ΔflaA or ΔdotAΔflaA L. pneumophila bacterium. Image is the same as in A with yellow circles marking infected cells and blue circles marking uninfected cells. The average combined infectivity in these conditions is ~90%. See supplemental methods for more details on counting.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/22707/elife-22707-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** The fraction of total reads with a size of 26–34 nucleotides was plotted for each ribosome profiling library used in this study. These graphs clearly show that the ribosome profiling libraries used in this study have a strong bias for 27–28 nucleotide fragments, consistent with the size of the footprint of the ribosome. Columns indicate infection condition. Rows indicate BMM genotype and/or drug treatment.

We first analyzed WT BMMs for T4SS-dependent gene induction, defined as the ratio of normalized read counts in the virulent ΔflaA to avirulent ΔdotAΔflaA L. pneumophila-infected conditions (see Materials and methods). We found that the majority of T4SS-dependent increases in ribosome footprints could be explained at the level of mRNA induction, as there was nearly a perfect linear correlation between the extent of mRNA induction and ribosome footprints for all T4SS-induced genes (Figure 2A). This correlation held for numerous known pathogen-induced mRNAs, including Il23a, Gem, Csf2, Il6, Tnf, Cxcl1, Cxcl2, Dusp1, and Dusp2, as well as for the cytokines Il1a and Il1b that were previously proposed to be preferentially translated (Asrat et al., 2014). To confirm that cytokine protein levels correlate with mRNA levels, we infected BMMs with ΔflaA or ΔdotAΔflaA L. pneumophila and measured the levels of 42 cytokines or immune-related proteins in the supernatants or cell lysates of these BMMs at 6 hr, using commercially available bead arrays. Of the cytokines assayed, 18 cytokines/proteins were measured above the limit of detection in lysates, and 22 cytokines/proteins were measured above the limit of detection in supernatants. The T4SS-dependent fold-induction of these protein levels was plotted versus the T4SS-dependent fold-induction of mRNA levels (Figure 2B–C). We observed a robust correlation between the extent of mRNA induction and the extent of protein induction, particularly in lysates (Figure 2B). The correlation seems to apply for the most highly induced proteins/mRNAs (e.g. IL-10 (Il10) and GM-CSF (Csf2)) but also for more modestly induced cytokines (Il1a, Il1b, Cxcl10). The less robust correlation between mRNA levels and protein levels in the cell supernatant (Figure 2C) may reflect differing rates of secretion, accumulation in the supernatant over time, re-binding to cell surface receptors, and stability in the supernatant. Taken together, these results suggest that the inducible immune response to L. pneumophila is controlled primarily at the level of mRNA superinduction (Figure 2).

![Figure 2.](https://cdn.elifesciences.org/articles/22707/elife-22707-fig2-v2.jpg)

**Figure 2.:** (A) The ratio of ribosome footprint and RNAseq read counts for well-expressed transcripts (read count ≥100) in ΔflaA-infected versus ΔdotAΔflaA-infected B6 BMMs was calculated for each annotated transcript (open circles) in the dataset and plotted. (B–C) B6 BMMs were infected with ΔflaA or ΔdotAΔflaA L. pneumophila and at 6 hr post-infection proteins were measured in cell lysates (B) or supernatants (C) by bead array. The T4SS-induction (ΔflaA/ΔdotAΔflaA) of protein in supernatants (B) or lysates (C) and the T4SS-induction of mRNA (ΔflaA/ΔdotAΔflaA) was plotted. Proteins were normalized to total protein levels measured by BCA and RNAseq read counts was normalized to transcript length and the sum of their respective mitochondrial protein coding genes. Data are averaged from four (A) or two independent experiments (B–C). Orange circle, Il1a. Green circle, Il1b. Blue circle, subset of inducible genes. Grey dotted line, y = x. Blue dotted line, linear regression model. r2, coefficient of determination. See also Figure 2—source data 1.

### mRNA induction accounts for effector-induced gene expression

L. pneumophila uses multiple mechanisms to block host protein synthesis. It has been shown that up to seven bacterial effectors secreted into the host cytosol can block translation (Barry et al., 2013; Fontana et al., 2011). Interestingly, the ∆7 strain that lacks these effectors is still able to partially suppress host protein synthesis by a mechanism that remains to be fully characterized (Barry et al., 2013; Fontana et al., 2011; Ivanov and Roy, 2013). It has been proposed that T4SS-competent L. pneumophila damages host cell membranes, resulting in ubiquitylation-dependent downregulation of mTOR activity and a block in cap-dependent translation (Ivanov and Roy, 2013). Consistent with its ability to partially suppress protein synthesis, the ∆7 strain still provokes IL-1α production, although its ability to stimulate Il23a and Csf2 expression is diminished (Barry et al., 2013; Fontana et al., 2011).

To determine the mechanism of effector-triggered cytokine induction, we performed parallel RNAseq and ribosome profiling of BMMs infected either with ∆flaA or ∆7∆flaA L. pneumophila. As expected, induction of Gem, Il23a, and Csf2 is highly dependent on the seven bacterial effectors, but again, similar to the total T4SS-dependent gene induction (Figure 2), the seven effector-dependent induction of ribosome footprints on these genes could be explained at the level of mRNA induction (Figure 3A). While the seven effector-dependent induction of the genes Dusp1, Dusp2, Cxcl1, Cxcl2, Tnf, Il1a, Il1b, and Il6 was low, all changes in ribosome footprint reads could again be explained by changes in mRNA levels (Figure 3A). These data suggest that T4SS-dependent and seven bacterial effector-dependent induction of inflammatory cytokines occurs by the induction of mRNA transcripts rather than through a mechanism of selective ribosome loading of mRNAs.

![Figure 3.](https://cdn.elifesciences.org/articles/22707/elife-22707-fig3-v2.jpg)

**Figure 3.:** (A–B) Ribosome footprint and RNAseq read counts were sorted for well-expressed transcripts (read count ≥100) and normalized to the sum of their respective mitochondrial protein coding genes. The ratio of ribosome footprint and RNAseq read counts in (A) ΔflaA-infected and Δ7ΔflaA-infected B6 BMMs or (B) B6 or Myd88–/– BMMs infected with ΔflaA L. pneumophila was calculated for each annotated transcript (open circles) in the dataset and plotted. Data are averaged from two independent experiments. Orange circle, Il1a. Green circle, Il1b. Blue circle, subset of inducible genes. Grey dotted line, y = x. Blue dotted line, linear regression model. r2, coefficient of determination. See also Figure 3—source data 1.

### MyD88 signaling in response to L. pneumophila is required for mRNA induction

It was previously proposed that specific transcripts, such as Il1a and Il1b, can be preferentially translated via a mechanism that requires signaling through the adaptor protein MyD88 (Asrat et al., 2014). Thus, we performed ribosome profiling and RNAseq on WT and Myd88–/– BMMs infected with ΔflaA L. pneumophila. For all MyD88-induced genes, including Il1a and Il1b, we observed a linear correlation between the induction of ribosome footprints and RNAseq reads (Figure 3B). This implies that MyD88-dependent induction of Il1a and Il1b ribosome footprints is controlled primarily at the level of mRNA induction, rather than at the level of selective ribosome loading of the mRNA. A similar pattern was also observed for other MyD88-induced genes, including Cxcl1, Csf2, Tnf, and Il6 (Figure 3B). Taken together, our results argue that the ability of host cells to overcome a pathogen-induced block in protein synthesis, and produce inflammatory cytokines such as IL-1α and IL-1β, requires a T4SS- and MyD88-dependent increase in mRNA levels rather than preferential loading of these cytokine mRNAs with ribosomes.

### Ribosome occupancy of mRNAs varies but is independent of infection

The above analyses sought to determine whether T4SS-dependent or MyD88-dependent gene induction was due to increased mRNA levels or increased ribosome loading of mRNAs. However, the analyses did not reveal whether there is differential ribosome occupancy of constitutively expressed (i.e. non-induced) mRNAs. We thus analyzed the ratio of ribosome footprint reads to RNAseq reads for all (induced and non-induced) transcripts in uninfected BMMs, and in BMMs infected with ΔflaA, ΔdotAΔflaA, or Δ7ΔflaA L. pneumophila. This analysis revealed a wide range of ribosome occupancies across different transcripts (Figure 4A–D). As might be anticipated, many of the mRNAs with the highest ribosome occupancy encoded abundant ‘housekeeping’ proteins, including Acta1 and histone mRNAs (e.g. Hist1h2ba, H2afj, and Hist3h2ba) (Figure 4A; Table 1). Importantly, most mRNAs that exhibit increased ribosome occupancy in uninfected BMMs also exhibit increased ribosome occupancy in ΔflaA, ΔdotAΔflaA, or Δ7ΔflaA L. pneumophila-infected BMMs (Figure 4B–D; Table 1), implying that the increased ribosome occupancy of these mRNAs is constitutive and not induced in response to infection. A few mRNAs of immunological interest, namely Lyz1, S100a11, and Cxcl3 exhibited elevated ribosome occupancy in all infection conditions (Figure 4B–D; Table 1). In contrast, Ftl1 mRNA exhibited very low ribosome occupancy (Figure 4A), consistent with a previous report showing that Ftl1 translation can be strongly repressed (Cairo et al., 1989). Atf4 is another gene known to be regulated at the level of translation (Pavitt and Ron, 2012), and in ΔflaA and ΔdotAΔflaA L. pneumophila-infected BMMs, Atf4 exhibited low ribosome occupancy (Figure 4B–C). Atf4 was not expressed at high enough levels to be called as detected in uninfected or Δ7ΔflaA L. pneumophila-infected BMMs (Figure 4A and D). Taken together, our results reveal that several mRNAs exhibit constitutive increased or decreased ribosome occupancy, as expected. Despite this, ribosome occupancy of mRNAs was not markedly affected by L. pneumophila infection (Figure 4A–D).

![Figure 4.](https://cdn.elifesciences.org/articles/22707/elife-22707-fig4-v2.jpg)

**Figure 4.:** (A–D) Ribosome footprint and RNAseq read counts were sorted for well-expressed transcripts (read counts ≥ 100) and normalized to CDS length and the sum of their respective mitochondrial protein coding genes. The normalized read counts for ribosome footprints and RNAseq for all well-expressed annotated transcripts were plotted for (A) uninfected, (B) ΔflaA, (C) ΔdotAΔflaA, or (D) Δ7ΔflaA L. pneumophila-infected B6 BMMs. Red dots represent transcripts with low translation efficiency. Purple dots represent a number of transcripts common to all conditions that appear to have significantly higher ribosome occupancy. Data are averaged from three (A), four (B–C), or two independent experiments (D). Orange circle, Il1a. Green circle, Il1b. Blue circles, subset of inducible transcripts. Blue dotted line, linear regression model. Grey lines, 99% prediction interval. r2, coefficient of determination. See also Table 1 and Figure 4—source data 1.

**Table 1.**
 Transcripts with ribosome occupancy eight times greater than the condition average. Bolded, transcripts found in all conditions. Orange, transcripts found in three conditions. Purple, transcripts found in two conditions. Data are averaged from two independent experiments.


<table>
  <thead>
    <tr>
      <th colspan="2">Uninfected</th>
      <th colspan="2">ΔflaA</th>
      <th colspan="2">ΔdotAΔflaA</th>
      <th colspan="2">Δ7ΔflaA</th>
    </tr>
    <tr>
      <th>Gene</th>
      <th>Riobosome occupancy</th>
      <th>Gene</th>
      <th>Riobosome occupancy</th>
      <th>Gene</th>
      <th>Riobosome occupancy</th>
      <th>Gene</th>
      <th>Riobosome occupancy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Acta1</td>
      <td>7105.62</td>
      <td>Acta1</td>
      <td>3137.40</td>
      <td>Acta1</td>
      <td>2489.70</td>
      <td>Acta1</td>
      <td>1633.44</td>
    </tr>
    <tr>
      <td>H2-Q7</td>
      <td>3130.45</td>
      <td>Hist1h4f</td>
      <td>1177.90</td>
      <td>S100a11</td>
      <td>1115.36</td>
      <td>Hist1h4f</td>
      <td>943.87</td>
    </tr>
    <tr>
      <td>Hist1h4f</td>
      <td>2195.70</td>
      <td>S100a11</td>
      <td>870.51</td>
      <td>Hist1h4f</td>
      <td>1069.93</td>
      <td>Rpl31</td>
      <td>893.93</td>
    </tr>
    <tr>
      <td>Hist3h2ba</td>
      <td>1715.98</td>
      <td>Hist1h2aa</td>
      <td>844.87</td>
      <td>Rpl31</td>
      <td>873.61</td>
      <td>Hist1h2aa</td>
      <td>822.96</td>
    </tr>
    <tr>
      <td>H2afj</td>
      <td>1524.09</td>
      <td>Hist3h2bb-ps</td>
      <td>699.92</td>
      <td>Hist1h2ba</td>
      <td>707.62</td>
      <td>Hist3h2ba</td>
      <td>625.90</td>
    </tr>
    <tr>
      <td>Hist3h2bb-ps</td>
      <td>1470.88</td>
      <td>Hist1h2ba</td>
      <td>692.19</td>
      <td>Hist3h2ba</td>
      <td>670.32</td>
      <td>S100a11</td>
      <td>565.91</td>
    </tr>
    <tr>
      <td>Lyz1</td>
      <td>1260.16</td>
      <td>H2afj</td>
      <td>686.47</td>
      <td>Lyz1</td>
      <td>533.22</td>
      <td>Fus</td>
      <td>532.18</td>
    </tr>
    <tr>
      <td>Hist1h2ba</td>
      <td>1174.16</td>
      <td>Cxcl3</td>
      <td>675.23</td>
      <td>Hist3h2bb-ps</td>
      <td>524.22</td>
      <td>Hist1h2ba</td>
      <td>519.60</td>
    </tr>
    <tr>
      <td>Cd52</td>
      <td>1170.22</td>
      <td>H2-T24</td>
      <td>557.88</td>
      <td>Fus</td>
      <td>405.23</td>
      <td>Lyz1</td>
      <td>498.70</td>
    </tr>
    <tr>
      <td>Fus</td>
      <td>1102.13</td>
      <td>Lyz1</td>
      <td>551.76</td>
      <td>H2-T24</td>
      <td>374.06</td>
      <td>H2-Q7</td>
      <td>371.10</td>
    </tr>
    <tr>
      <td>H2-Q4</td>
      <td>1022.17</td>
      <td>Hist3h2ba</td>
      <td>509.95</td>
      <td>Gm5803</td>
      <td>345.78</td>
      <td>Gm5803</td>
      <td>368.22</td>
    </tr>
    <tr>
      <td>Rpl38</td>
      <td>1004.74</td>
      <td>Fus</td>
      <td>480.25</td>
      <td>H2-Q7</td>
      <td>337.36</td>
      <td>H2afj</td>
      <td>356.99</td>
    </tr>
    <tr>
      <td>Hist2h2ab</td>
      <td>796.60</td>
      <td>Saa1</td>
      <td>475.25</td>
      <td>Hist1h4i</td>
      <td>302.55</td>
      <td>Hist1h4i</td>
      <td>348.34</td>
    </tr>
    <tr>
      <td>H2-Q6</td>
      <td>752.77</td>
      <td>Gm5803</td>
      <td>436.48</td>
      <td>Cxcl3</td>
      <td>281.86</td>
      <td>Hist1h4k</td>
      <td>318.08</td>
    </tr>
    <tr>
      <td>S100a11</td>
      <td>717.99</td>
      <td>Hist1h4i</td>
      <td>333.72</td>
      <td>Saa1</td>
      <td>265.08</td>
      <td>Rrbp1</td>
      <td>306.19</td>
    </tr>
    <tr>
      <td>Gm5803</td>
      <td>692.32</td>
      <td>Atp5e</td>
      <td>315.00</td>
      <td>Hist1h4n</td>
      <td>244.74</td>
      <td>Hist1h4j</td>
      <td>301.73</td>
    </tr>
    <tr>
      <td>Tmsb10</td>
      <td>679.27</td>
      <td>Rrbp1</td>
      <td>308.68</td>
      <td>Rrbp1</td>
      <td>225.85</td>
      <td>Hist1h4a</td>
      <td>298.67</td>
    </tr>
    <tr>
      <td>H2-Q10</td>
      <td>674.79</td>
      <td>Mt1</td>
      <td>308.36</td>
      <td>Hist1h4j</td>
      <td>218.84</td>
      <td>Hist1h4h</td>
      <td>295.99</td>
    </tr>
    <tr>
      <td>Rpl36</td>
      <td>672.43</td>
      <td>Hist1h4j</td>
      <td>304.87</td>
      <td>Hist1h4k</td>
      <td>217.89</td>
      <td>Hist1h4b</td>
      <td>288.98</td>
    </tr>
    <tr>
      <td>Mt1</td>
      <td>672.29</td>
      <td>Hist1h4k</td>
      <td>303.19</td>
      <td>Atp5e</td>
      <td>217.08</td>
      <td>Hist1h4n</td>
      <td>272.04</td>
    </tr>
    <tr>
      <td>Hist2h2bb</td>
      <td>650.90</td>
      <td>Hist1h4h</td>
      <td>293.11</td>
      <td>H2-Q4</td>
      <td>215.94</td>
      <td>BC094916</td>
      <td>259.08</td>
    </tr>
    <tr>
      <td>H2-Q7</td>
      <td>629.56</td>
      <td>Hist1h4a</td>
      <td>292.51</td>
      <td>Hist1h4h</td>
      <td>215.51</td>
      <td>Hist1h4c</td>
      <td>255.20</td>
    </tr>
    <tr>
      <td>H2-Q7</td>
      <td>618.80</td>
      <td>Hist1h4b</td>
      <td>280.60</td>
      <td>H2afj</td>
      <td>206.14</td>
      <td>Cxcl3</td>
      <td>252.49</td>
    </tr>
    <tr>
      <td>Atp5e</td>
      <td>606.27</td>
      <td>Gm11127</td>
      <td>272.59</td>
      <td>Hist1h4a</td>
      <td>205.64</td>
      <td>Atp5e</td>
      <td>241.23</td>
    </tr>
    <tr>
      <td>H2-T24</td>
      <td>601.41</td>
      <td>Hist1h4n</td>
      <td>265.41</td>
      <td>Hist1h4b</td>
      <td>197.15</td>
      <td>Saa1</td>
      <td>220.10</td>
    </tr>
    <tr>
      <td>Rpl37</td>
      <td>584.88</td>
      <td>Fkbp1a</td>
      <td>264.22</td>
      <td>Hist2h2bb</td>
      <td>191.90</td>
      <td>Myl12b</td>
      <td>210.72</td>
    </tr>
    <tr>
      <td>H2-T10</td>
      <td>545.54</td>
      <td>Hist1h4c</td>
      <td>Hist1h4c</td>
      <td>Hist1h4c</td>
      <td>187.03</td>
      <td>Gm7030</td>
      <td>206.93</td>
    </tr>
    <tr>
      <td>Hist1h4i</td>
      <td>529.15</td>
      <td>Gm7030</td>
      <td>253.47</td>
      <td>Mt1</td>
      <td>185.28</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gm11127</td>
      <td>512.74</td>
      <td>Myl12b</td>
      <td>247.71</td>
      <td>Cd52</td>
      <td>184.14</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Uqcrq</td>
      <td>511.93</td>
      <td>Rps17</td>
      <td>234.41</td>
      <td>Gm11127</td>
      <td>183.08</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Emp1</td>
      <td>494.39</td>
      <td>Cd52</td>
      <td>231.77</td>
      <td>Hist1h2bj</td>
      <td>182.74</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Hist1h2bf</td>
      <td>484.53</td>
      <td></td>
      <td></td>
      <td>Sh3bgrl</td>
      <td>181.81</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gm7030</td>
      <td>481.28</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Npc2</td>
      <td>479.93</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Hist1h2bj</td>
      <td>478.33</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Usmg5</td>
      <td>477.21</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Hmga2</td>
      <td>468.10</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Global analysis of translation inhibition by L. pneumophila

A benefit of ribosome profiling is that it permits the mapping of ribosome footprints with nucleotide resolution. Thus, to characterize the position of ribosomes on mRNAs after infection with L. pneumophila, we generated metagene ribosome footprint profiles from libraries generated from WT BMMs (Figure 5). Metagene profiles were generated by mapping the inferred A site position of ribosome footprint reads relative to the start (Figure 5A,C,E,G,I) or stop (Figure 5B,D,F,H,J) codon on a given transcript. Mapped reads were then summed to produce a global view of the distribution of ribosomes across all transcripts in our dataset. As expected from the known stepwise codon-by-codon movement of the ribosome, all metagene plots demonstrated a characteristic three-nucleotide periodicity (Figure 5). Interestingly, metagene ribosome profiles of uninfected (Figure 5A–B), ΔflaA (Figure 5C–D), ΔdotAΔflaA (Figure 5E–F), or Δ7ΔflaA (Figure 5G–H) infected BMMs appeared grossly similar to each other, even though global translation is blocked only in the ΔflaA and Δ7ΔflaA L. pneumophila-infected conditions (Barry et al., 2013; Fontana et al., 2011; Asrat et al., 2014). This result can be explained by the fact that ribosome metagene profiles do not distinguish whether ribosome footprints arise from stalled or translating ribosomes, unless the stall occurs at a characteristic distance from the start or stop codon. In fact, we did notice a slight increase in the number of ribosomes found at the start site of the transcript in Δ7ΔflaA L. pneumophila-infected BMMs as compared to other conditions (Figure 5I). This may reflect a selective block in translation initiation by this strain (see below). In addition, we noted that in all conditions, ribosomes accumulated at the stop codon, suggesting that, in BMMs, translation termination may be a limiting step in translation (Figure 5J).

![Figure 5.](https://cdn.elifesciences.org/articles/22707/elife-22707-fig5-v2.jpg)

**Figure 5.:** (A–J) Metagene profiles of uninfected (A–B), ΔflaA (C–D), ΔdotAΔflaA (E–F), Δ7ΔflaA (G–H) L. pneumophila-infected B6 BMMs and a merge (I–J). Metagene profiles are depicted relative to the translation start (A, C, E, G, I) and stop site (B, D, F, H, J). Metagene analyses show peaks at every three nucleotides, corresponding to the codon-to-codon shifts of the ribosome. Data are representative of two independent experiments (A–J). Black line, uninfected. Red line, ΔflaA-infected. Green line, ΔdotAΔflaA-infected. Blue line, Δ7ΔflaA-infected.

### L. pneumophila blocks translation at the levels of initiation and elongation

To distinguish whether an observed ribosome footprint arises from a stalled or translating ribosome, we performed ribosome run-off experiments. In these experiments, new translation initiation was blocked by the drug harringtonine 120 s prior to cell lysis. Harringtonine inhibits the first rounds of peptide bond formation following ribosome subunit joining and results in accumulation of ribosomes at the translational start site and run-off of elongating (but not stalled) ribosomes that have already cleared the start codon (Ingolia et al., 2012, 2011; Huang and Harringtonine, 1975; Tscherne and Pestka, 1975; Fresno et al., 1977). Importantly, cells experiencing a block in translation elongation will exhibit less ribosome run-off after harringtonine treatment, and an increased number of reads at the 5ʹ end of mRNAs after drug treatment (Ingolia et al., 2011), compared to cells in which elongation is not blocked.

As expected, uninfected and ΔdotAΔflaA-infected BMMs show an increase in ribosome footprints at the translation start site and a preferential loss of ribosome footprints from the 5ʹ and 3ʹ end of mRNAs, consistent with the expected effects of harringtonine and demonstrating clear ribosome run-off (Figure 6A–B,E–F, Figure 6—figure supplement 1A–B). By contrast, ΔflaA L. pneumophila-infected BMMs treated with harringtonine exhibited little ribosome run-off (Figure 6C–D, Figure 6—figure supplement 1A–B), consistent with the expectation that ΔflaA L. pneumophila blocks host translation elongation. The Δ7ΔflaA L. pneumophila strain, lacking all known bacterial effectors that block host protein synthesis, nevertheless, shuts down host translation (Barry et al., 2013), yet we observed clear evidence of run-off of elongating ribosomes from the 5ʹ and 3ʹ end of mRNAs following harringtonine treatment (Figure 6G–H, Figure 6—figure supplement 1A–B). These data suggest that the residual block in host protein synthesis induced by Δ7ΔflaA L. pneumophila is at the level of translation initiation. Similar results can be seen when analyzing longer stretches of coding sequences (Figure 6—figure supplement 1C–F).

![Figure 6.](https://cdn.elifesciences.org/articles/22707/elife-22707-fig6-v2.jpg)

**Figure 6.:** (A–H) Metagene profiles of B6 BMMs uninfected (A–B) or infected with ΔflaA (C–D), ΔdotAΔflaA (E–F), or Δ7ΔflaA (G–H) L. pneumophila in the presence (solid line) or absence (dashed line) of the drug harringtonine to block translation initiation. Metagene profiles are depicted relative to the translation start (A, C, E, G) and stop site (B, D, F, H). Data are representative of two independent experiments (A–H). Solid line, no drug treatment. Dashed line, harringtonine treatment. Black line, uninfected. Red line, ΔflaA-infected. Green line, ΔdotAΔflaA-infected. Blue line, Δ7ΔflaA-infected.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/22707/elife-22707-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A–B) Metagene profile plot around the translation start (A) or stop (B) site of all harringtonine-treated conditions normalized to mitochondrial read counts of each condition. (C–F) Global weighted averages across transcripts were calculated for BMMs left uninfected (C) or infected with ΔflaA (D), ΔdotAΔflaA (E), or Δ7ΔflaA (F) L. pneumophila. Weighted averages were generated by scaling each transcript’s ribosome occupancy profile according to the average density from codon 250 to codon 349 and then averaging across the entire condition. Transcripts with very low density in the 250–349 codon region (or shorter than 349 codons) are excluded from averaging. If the weighted average is less than 1, this shows that this region has reduced ribosome footprints, while if the weighted average is greater than one this shows that there are more ribosome footprints in this region. Following a brief pulse of cells with harringtonine (red line) there is a change in the distribution of ribosomes from the 5ʹ end of the mRNA to the 3ʹ end of the mRNA (i.e., as the ribosomes continue to move 5ʹ to 3ʹ; C–F) as compared to untreated cells (blue line). This can be seen by an increase in the weighted average at the 3ʹ end of mRNAs (C, E, F) but the lack of this change shows a block in translation elongation (D). We also expect an accumulation of ribosomes at the ATG following harringtonine treatment, which is also seen as a peak in the weighted average at the start site (C–F). Data are representative of two independent experiments (A–F).

It is important to note that there is a small proportion of uninfected bystander cells assayed in our experiments. However, it is unlikely that these uninfected cells are responsible for the ribosome run-off seen in Δ7ΔflaA L. pneumophila-infected BMMs because the conditions used in these experiments led to most (~90%) cells being infected with L. pneumophila (Figure 1—figure supplement 1A–B). Furthermore, if our infection conditions resulted in large numbers of uninfected cells, then a similar run-off should have been observed in the ∆flaA-infected sample, which it was not. Thus, these results suggest that the seven effectors are required to block translation elongation, and that the residual translation inhibition induced by Δ7ΔflaA L. pneumophila is at the level of translation initiation (Figure 6).

### Cytokine transcripts do not escape the pathogen-induced translation block

Although the above results demonstrate a global block in translation elongation in ∆flaA-infected cells, it remains possible that specific transcripts escape this block. We therefore analyzed our translation run-off datasets to assess translation elongation on a per-mRNA basis. We plotted the number of ribosome footprint reads for each transcript in paired untreated and harringtonine treated samples (Figure 7A–D). In this analysis, we expect that an mRNA with actively elongating ribosomes would show a reduction in the number of 5ʹ reads in the harringtonine treated sample, as ribosomes will run off the transcript, compared to the untreated sample. In order to best measure run-off elongation and avoid the expected but confounding effects of harringtonine-induced accumulation of footprints at start codons (which were clearly observed; Figure 6), we excluded the first 25 codons and analyzed ribosome footprint occupancy over the next 300 codons. Consistent with our previous analysis, we find that uninfected, ΔdotAΔflaA, and Δ7ΔflaA-infected BMMs show a clear global signature of ribosome run-off, again suggesting that the block in host protein synthesis induced by Δ7ΔflaA L. pneumophila infection is occurring at the level of translation initiation (Figure 7A–D). Importantly, in ΔflaA-infected BMMs there is no evidence of ribosome run-off, consistent with ΔflaA L. pneumophila inducing a block in host translation elongation (Figure 7B). Interestingly, in all conditions tested, cytokine-related genes fell well within the average of ribosome retention across all transcripts, and if anything, were found to have reduced ribosome run-off compared to a typical gene (Figure 7A–D). A similar trend was seen when we further examined ribosome run-off for specific immune and housekeeping transcripts by plotting the cumulative read counts over the length of the mRNA (Figure 7—figure supplement 1). These results imply that at this time point, cytokine transcripts are not preferentially translated in response to pathogenic infection, but instead are controlled at the level of mRNA induction (Figure 7A–D).

![Figure 7.](https://cdn.elifesciences.org/articles/22707/elife-22707-fig7-v2.jpg)

**Figure 7.:** (A–D) Read counts from paired samples treated with harringtonine or left untreated were plotted for uninfected (A), ΔflaA (B), ΔdotAΔflaA (C), or Δ7ΔflaA-infected (D) BMMs showing where cytokine-related transcripts (pink circles; Csf1, Csf2, Cxcl1, Cxcl2, Dusp1, Dusp2, Ifnb1, Il10, Il12b, Il1a, Il1b, Il23a, Il6, Lyz1, and Tnf) and housekeeping transcripts (blue circles; Gapdh, Rpl31, Rps17, and Tuba1a) fall among all transcripts (black circles). Grey line, y=x. Data shown are representative of two independent experiments. See Figure 7—source data 1 for individual housekeeping and cytokine-related transcripts. Supporting Information Captions.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/22707/elife-22707-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Cumulative read counts across the length of individual transcripts were calculated and normalized to the sum of ribosome footprints of mitochondrial transcripts in each respective library. Red = BMMs treated with harringtonine. Black = BMMs untreated. Numbers in parentheses = total read counts. Rows = individual transcript. Columns = infection condition.

## Discussion

Inducible gene expression is of central importance for the immune response to infection. A recent study showed that in response to innate immune stimulation with purified LPS, dendritic cells almost entirely control the induction of genes at the level of transcription (Jovanovic et al., 2015). However, this conclusion may not apply to cells infected with a virulent pathogen that manipulates gene expression. We thus investigated the relative contributions of mRNA induction and translation during infection with an intracellular bacterial pathogen, L. pneumophila, that blocks host protein synthesis.

Pathogen-induced blockade of host protein synthesis has been shown in a number of infection models to be sensed by the host and induce an inflammatory response (Barry et al., 2013; Fontana et al., 2011; Dunbar et al., 2012; McEwan et al., 2012; Chakrabarti et al., 2012; Fontana et al., 2012). We previously identified IL-1α as a key inflammatory cytokine induced preferentially in response to translation inhibition imposed by L. pneumophila (Barry et al., 2013). However, the mechanism by which cytokine proteins are induced despite a pathogen-induced translation blockade remains unclear. We previously provided evidence for a model in which translation inhibition results in a failure to synthesize negative feedback inhibitors of transcription, for example, IκB or A20 (Fontana et al., 2011). We proposed this results in a massive and sustained production of cytokine transcripts, termed mRNA superinduction, that is sufficient to overcome the partial (~95%) block in translation and allow for production of cytokine proteins (Barry et al., 2013; Fontana et al., 2011). Another report provided data suggesting that IL-1 production is mediated by MyD88-enhanced protein synthesis, although alternative explanations were also entertained (Asrat et al., 2014). A third study proposed that virulent L. pneumophila regulates cap-dependent translation initiation, via manipulation of the mTOR signaling pathway, to regulate the protein levels of highly abundant transcripts in infected macrophages (Ivanov and Roy, 2013). In our present study, we found that the induction of ribosome footprints by L. pneumophila could be explained by an underlying induction of mRNAs. We did not find evidence for selective ribosome loading of abundant cytokine mRNAs. In addition, ribosome run-off experiments confirmed that cytokine mRNAs are not selectively translated during infection (Figure 7). Furthermore, we find that the role of MyD88 signaling in gene expression appears to be primarily at the level of mRNA induction and not translational regulation (Figure 3). Thus, we conclude that preferential translation does not account for the majority of specific gene induction following infection by L. pneumophila.

It remains possible that selective translation initiation mechanisms, for example, via uORFs, might also contribute modestly to the inducible immune response to L. pneumophila, but these subtle effects were not evident in our global analysis. In any case, it is difficult to explain how regulation of translation initiation could overcome a downstream pathogen-induced block in translation elongation such as is observed during L. pneumophila infection. It is also possible that post-translational mechanisms, which are not addressable with the ribosomal profiling techniques used here, may regulate protein production by infected cells. Indeed, inflammasome-dependent caspase-1 processing is known to be an important post-translational regulatory mechanism controlling IL-1β production by infected cells (von Moltke et al., 2013). Lastly, our data do not specifically address the mechanism of mRNA induction, although our prior work suggested mRNA induction involves new transcription rather than increased mRNA stability (Fontana et al., 2011).

Although wild-type L. pneumophila blocks translation elongation via translocated effectors, we found that Δ7ΔflaA L. pneumophila lacking the effectors nevertheless blocks protein synthesis at the level of translation initiation (Figure 6). Thus, in contrast to a previous study that used virus-based translation reporter experiments in L. pneumophila-infected RAW macrophages (Ivanov and Roy, 2013), we were clearly able to dissociate the L. pneumophila-induced block in host protein synthesis into two components: (1) an elongation block that required the seven translocated effectors, and (2) an initiation block that did not require the seven effectors. In addition, our analysis represents an advance over prior studies because we were able to analyze the translation of all endogenous transcripts simultaneously as opposed to measuring translation only of a single exogenous reporter mRNA. Intriguingly, in contrast to the effector-dependent block in translation that we show occurs at the level of elongation, the majority of host-mediated regulation of translation occurs at the level of translation initiation (Hershey et al., 2012). Thus, while it is possible that a novel bacterial effector that directly targets translation initiation could explain the residual inhibition of translation by the Δ7ΔflaA L. pneumophila mutant, we favor the hypothesis that the residual block in host protein synthesis may be a result of the host stress response induced by pathogenic infection, consistent with numerous prior studies (Mohr and Sonenberg, 2012; Lemaitre and Girardin, 2013; Chakrabarti et al., 2012; Ivanov and Roy, 2013; Janssens et al., 2014; Tattoli et al., 2012). Indeed, T4SS-competent L. pneumophila has been suggested to induce membrane damage that inhibits the mTOR pathway and blocks translation initiation (Ivanov and Roy, 2013). Further studies will be required to identify the bacterial and host pathways required for the residual translation inhibition caused by the Δ7ΔflaA L. pneumophila mutant.

The results presented here further support a role for translation inhibition as a signal that the innate immune system uses to recognize and preferentially respond to pathogens (Fontana et al., 2011). Our work provides nucleotide-level analysis of the global block in host protein synthesis induced by L. pneumophila, and demonstrates that L. pneumophila infection results in inhibition of host protein synthesis both at the level of translation initiation and elongation. Importantly, our results also provide insights into the molecular mechanisms by which host cells are able to mount a protective immune response despite a pathogen-induced block in protein synthesis. Using ribosome run-off assays in combination with ribosome profiling and RNAseq, we find that mRNA superinduction, rather than selective mRNA translation, is the strategy by which host cells produce inflammatory cytokines in the face of pathogen-mediated translation inhibition. To be effective, the strategy of mRNA superinduction requires that the magnitude of mRNA superinduction exceeds the magnitude of the block in protein synthesis. Indeed, our data suggest this is the case, as we observe >1000 fold induction of certain mRNAs, whereas we previously estimated the block in protein synthesis to be ~95% (20-fold) (Fontana et al., 2011). One possible advantage of mRNA superinduction as a strategy for overcoming a pathogen-mediated block of protein synthesis is that it does not require specific translation factors, as was previously proposed might mediate selective mRNA translation in L. pneumophila-infected cells (Asrat et al., 2014). In addition, in mammalian cells, selective translation is usually regulated at the level of translation initiation, a strategy that would be easily defeated by pathogens such as L. pneumophila that block the downstream process of translation elongation. Importantly, since numerous viral and bacterial pathogens and toxins interfere with host protein synthesis, we propose that our results may provide general insight into the inducible innate immune response to infection.

## Materials and methods

### Ethics statement

These studies were carried out in strict accordance with the recommendations in the Guide for the Care and Use of Laboratory Animals of the National Institutes of Health under animal protocol AUP-2014-09-6665. The protocol was approved by the Animal Care and Use Committee at the University of California, Berkeley.

### Access to high-throughput sequencing data

The data discussed in this publication have been deposited in NCBI's Gene Expression Omnibus (Edgar et al., 2002) and are accessible through GEO Series accession number GSE89184 (https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE89184).

### Cell culture

Macrophages were derived from the bone marrow of C57BL/6J (Jackson Laboratory, Bar Harbor, ME, USA) and Myd88 –/– (Hou et al., 2008) mice on the B6 background. Macrophages were derived by 8 days of culture in RPMI supplemented with 10% serum, 100 μM streptomycin, 100 U/mL penicillin, 2 mM L-glutamine and 10% supernatant from 3T3-macrophage-colony-stimulating factor cells, with feeding on day 5. Cells were re-plated in antibiotic free media 24 hr prior to infection with L. pneumophila.

### Bacterial strains and infections

All L. pneumophila strains were derived from LP02, a streptomycin-resistant thymidine auxotroph derived from L. pneumophila LP01. The ΔdotAΔflaA, ΔflaA, and Δ7ΔflaA strains were generated on the LP02 background and have been described previously (Barry et al., 2013; Fontana et al., 2011; Ren et al., 2006; Fontana et al., 2012). Twofold dilutions of L. pneumophila strains used for infections were grown overnight in liquid buffered-yeast-extract culture and, at the time of infection, cultures with an optical density (600 nm) greater than 4.0 were selected. BMMs were plated at a density of 1.56 × 105 cells per cm2 (1.5.x106 cells per well of a six-well plate) and infected at an MOI of 3 by centrifugation for 10 min at 400 xg. After 1 hr of infection media was changed. All in vitro L. pneumophila infections were performed in the absence of thymidine to prevent bacterial replication which would otherwise differ between the ∆dotA and Dot+ strains. The lack of thymidine can result in a loss of bacterial viability, although we attempted to mitigate this concern by examining host gene expression at a relatively early 6 hr time point.

### Library preparation and sequencing for ribosome profiling

Ribosome profiling experiments were undertaken as previously described (Ingolia et al., 2012). BMMs were plated in tissue culture treated six-well plates (1.5 × 106 BMMs/well) or 75 cm2 flasks (1.2 × 107 BMMs per flask). At 6 hr post-infection BMMs were lysed by flash freezing and thawed in the presence of lysis buffer (Ingolia et al., 2012). When used, harringtonine (LKT Laboratories, Saint Paul, MN) was added at a final concentration of 2 μg/mL for 120 s at the end of the 6 hr infection. 100 μg/mL of cycloheximide (Sigma-Aldrich, St. Louis, MO) was added to freeze ribosomes after the 120 s harringtonine treatment. Following cycloheximide treatment cells were immediately lysed. Clarified lysates were split and some was used to generate ribosome footprints while some was used to isolate total RNA for RNA sequencing (described below). All RNA and DNA gel extractions were performed overnight as previously described (Ingolia et al., 2012). The Ribo-Zero Gold rRNA Removal Kit (Illumina, San Diego, CA) was used to remove rRNA from ribosome profiling samples before the dephosphorylation and linker ligation steps (Ingolia et al., 2012). Final ribosome profiling libraries were sequenced on a HiSeq2000 System (Illumina) with single read 50 (SR50) read lengths by the Vincent J. Coates Genomics Sequencing Laboratory at UC, Berkeley.

### Generation of RNAseq libraries

Clarified lysate was isolated as described above and 300 μL of lysate was mixed with 900 μL of Trizol LS (Thermo Fisher Scientific, Waltham, MA) and RNA was isolated following the manufacturer’s guidelines. RNA integrity was measured utilizing the RNA Pico method on the Agilent 2100 Bioanalyzer at the University of California, Berkeley Functional Genomics Laboratory. High-quality RNA with a RNA integrity number (RIN) >8 (Agilent Technologies, Santa Clara, CA) was submitted to the QB3-Berkeley Functional Genomics Laboratory and single read 100 base pair read length (SR100) sequencing libraries were generated. Libraries were sequenced on a HiSeq2000 System (Illumina) by the Vincent J. Coates Genomics Sequencing Laboratory at UC, Berkeley.

### Alignment of RNAseq reads and differential expression analysis

RNA sequencing reads were preprocessed using tools from the FASTX-Toolkit (http://hannonlab.cshl.edu/fastx_toolkit/) by trimming the linker sequence from the 3ʹ end of each read and in some cases removing 10–15 nucleotides from the 5ʹ of each read to mitigate a region of overrepresented nucleotides. Alignment and differential expression analysis of RNAseq reads were undertaken as previously described (Trapnell et al., 2012). Briefly, high quality and preprocessed sequencing reads were aligned using the TopHat splicing-aware short-read alignment program to a library of transcripts derived from the UCSC Known Gene data set, and those with no acceptable transcript alignment were then aligned against the Mus musculus genome (mm10).

### Alignment of ribosome footprint sequences

Sequences were processed as described previously (Ingolia et al., 2012). Sequences were preprocessed by trimming the linker sequence from the 3ʹ end of each sequencing read and removing the first nucleotide from the 5ʹ end of each read. Reads were then aligned to a rRNA reference using the Bowtie short-read alignment program. All sequences aligning the rRNA reference were discarded. All non-rRNA sequencing reads were aligned using the TopHat splicing-aware short-read alignment program to a library of transcripts derived from the UCSC Known Genes data set, and those with no acceptable transcript alignment were then aligned against the mouse genome (mm10). Perfect-match alignments were extracted, and these files were used for analyses. For most analyses, footprint alignments were assigned to specific A site nucleotides by using the position and total length of each alignment, calibrated from footprints at the beginning and the end of CDSes, as previously described (Ingolia et al., 2012, 2011).

### Counting of ribosome profiling and RNAseq reads

Counting of reads was performed as previously described (Ingolia et al., 2009, 2011). Reads were mapped to coding sequences and counted, excluding reads that mapped to the first 15 codons or the last 5 codons of a CDS due to accumulation of ribosomes (Ingolia et al., 2011). In order to analyze gene-specific ribosome run-off (Figure 7A–D), we counted reads mapping from codon 26 to codon 325, that is, a 300-codon window excluding the first 25 codons of a gene.

### Ribosome occupancy analysis

For analyses of ribosome occupancy (Figure 4), ribosome footprint and mRNAseq read counts were calculated similarly. Read counts were normalized to CDS length, as longer transcripts inherently have increased read counts, generating a read density (read density = read count ÷ transcript length) for each gene. Read densities were further normalized to the sum of read counts of 12 mitochondrial protein-coding genes (see below) as an estimate of total cells in each condition, allowing for comparison among different conditions and libraries (Iwasaki et al., 2016). For each transcript in the dataset, the average raw ribosome footprint read counts for each infection conditions was calculated and transcripts with an average ribosome footprint or RNAseq read count less than 100 were discarded. Additionally, any transcript that had ribosome footprint reads but 0 RNAseq reads was also discarded. Discarded transcripts were defined as undetectable.

### MyD88-dependent gene induction analysis

Two experiments were used to generate two independent libraries consisting of B6 and Myd88–/– BMMs infected with ΔflaA or ΔdotAΔflaA L. pneumophila. For each gene in the dataset, the average raw ribosome footprint read counts for ΔflaA L. pneumophila-infected B6 BMMs were sorted and genes with an average ribosome footprint or RNAseq read count less than 100 were discarded. Additionally, any gene that had ribosome footprint reads but no detectable RNAseq reads in B6 or Myd88–/– BMMs were discarded. The sorted read counts were then normalized to ribosome footprint or RNAseq read counts of 12 mitochondrial protein-coding genes (see below) as an estimate of total cells in each condition. MyD88-dependent gene induction was calculated using the equation: MyD88-dependent gene induction = average(normalized B6 read count) ÷ average(normalized Myd88–/– read count).

### Type IV secretion system-dependent gene induction analysis

Four independent experiments were used to generate four collections of sequencing libraries consisting of B6 BMMs infected with ΔflaA or ΔdotAΔflaA L. pneumophila. For each gene in the dataset, the average raw ribosome footprint read counts for ΔflaA L. pneumophila infected B6 BMMs were sorted and genes with an average ribosome footprint or RNAseq read count less than 100 were discarded. Additionally, any gene that had ribosome footprint reads but no detectable RNAseq reads in ΔflaA or ΔdotAΔflaA L. pneumophila-infected B6 BMMs were discarded. The sorted read counts were then normalized to ribosome footprint or RNAseq read counts of 12 mitochondrial protein-coding genes (see below) as an estimate of total cells in each condition. T4SS-dependent gene induction was calculated using the equation: T4SS-dependent gene induction = average(normalized ΔflaA-infected read count) ÷ average(normalized ΔdotAΔflaA-infected read count).

### Analysis of cytokine and protein levels in infected BMM lysates and supernatants

B6 BMMs were left uninfected or infected with ΔflaA or ΔdotAΔflaA L. pneumophila at an MOI of 3 in duplicate, as described above. Media was changed 1 hr following infection and at 6 hr post-infection supernatants were collected and BMMs washed with PBS. BMMs were lysed in 400 μL mammalian cell PE lysis buffer (G-Biosciences, St. Louis, MO) following the manufacturers instructions. Lysates and supernatants were cleared by spinning at 20,000 x g for 30 min at 4°C. Cytokine and protein levels were measured using a commercially available cytokine bead array (Rodent MAP 4.0-Mouse Sample Testing, Ampersand Biosciences, Saranac Lake, NY) and total protein levels were measured by bicinchoninic acid (BCA) assay (Ampersand Biosciences, Saranac Lake, NY). Protein and cytokine levels in each infection condition were normalized to total protein levels. Infectivity was confirmed by staining for L. pneumophila (see below). mRNA levels of cytokines were determined by counting (counting method described above) previously acquired RNAseq data of B6 BMMs infected with ΔflaA or ΔdotAΔflaA L. pneumophila at an MOI of 3 for 6 hr. RNAseq read counts were normalized to transcript length and the sum of RNAseq read counts of 12 mitochondrial protein-coding genes (see below) as an estimate of total cells in each condition (RNAseq normalization described above). T4SS-dependent induction was measured by taking the ratio of protein or mRNA levels in the ΔflaA infected condition to protein or mRNA levels in the ΔdotAΔflaA infected condition: T4SS-dependent induction = average(normalized ΔflaA mRNA or protein) divided by average(normalized ΔdotAΔflaA mRNA or protein). T4SS-induction was averaged from two independent experiments and plotted.

### Seven-effector-dependent gene induction analysis

Two independent experiments were used to generate two collections of sequencing libraries consisting of B6 BMMs infected with ΔflaA or Δ7ΔflaA L. pneumophila. For each gene in the dataset the average raw ribosome footprint read counts for ΔflaA L. pneumophila-infected B6 BMMs were sorted and genes with an average ribosome footprint or RNAseq read count less than 100 were discarded. Additionally, any gene that had ribosome footprint reads but no detectable RNAseq reads in ΔflaA or Δ7ΔflaA L. pneumophila-infected B6 BMMs were discarded. The sorted read counts were then normalized to ribosome footprint or RNAseq read counts of 12 mitochondrial protein-coding genes (see below) as an estimate of total cells in each condition. Seven effector-dependent gene induction was calculated using the equation: seven effector-dependent gene induction = average(normalized ΔflaA-infected read count) ÷ average(normalized Δ7ΔflaA-infected read count).

### Metagene profile analysis of ribosome profiling libraries

Metagene profiles were generated as previously described (Ingolia et al., 2009, 2011). These metagene profiles indicate the total number of ribosome footprints whose A site falls at the indicated position relative to the start or stop codon of the coding sequence, and reflect a simple, unweighted sum of the footprint profiles around the beginning and the end of each protein-coding gene. The A site position was estimated for each footprint using a length-dependent offset from the 5ʹ end of the fragment. The distance from this A site position to the start or stop codon of the coding sequence was then computed, taking into account the fact that translation initiation occurs with the second codon in the A site.

### Analysis of ribosome run-off of individual genes

Cumulative ribosome occupancy profiles (Figure 7—figure supplement 1) were computed by taking the cumulative sum of ribosome footprints mapping to each position in the gene, scaled by the normalization factor derived from mitochondrial translation in that sample.

### Mitochondrial genes used for library normalization

<table>
  <thead>
    <tr>
      <th>Gene ID</th>
      <th>Name</th>
      <th>Size (bp)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ENSMUST00000082392</td>
      <td>mt-Nd1</td>
      <td>299</td>
    </tr>
    <tr>
      <td>ENSMUST00000082396</td>
      <td>mt-Nd2</td>
      <td>326</td>
    </tr>
    <tr>
      <td>ENSMUST00000082402</td>
      <td>mt-Co1</td>
      <td>495</td>
    </tr>
    <tr>
      <td>ENSMUST00000082405</td>
      <td>mt-Co2</td>
      <td>208</td>
    </tr>
    <tr>
      <td>ENSMUST00000082407</td>
      <td>mt-Atp8</td>
      <td>48</td>
    </tr>
    <tr>
      <td>ENSMUST00000082408</td>
      <td>mt-Atp6</td>
      <td>207</td>
    </tr>
    <tr>
      <td>ENSMUST00000082409</td>
      <td>mt-Co3</td>
      <td>241</td>
    </tr>
    <tr>
      <td>ENSMUST00000082411</td>
      <td>mt-Nd3</td>
      <td>96</td>
    </tr>
    <tr>
      <td>ENSMUST00000082414</td>
      <td>mt-Nd4</td>
      <td>439</td>
    </tr>
    <tr>
      <td>ENSMUST00000082418</td>
      <td>mt-Nd5</td>
      <td>588</td>
    </tr>
    <tr>
      <td>ENSMUST00000082419</td>
      <td>mt-Nd6</td>
      <td>153</td>
    </tr>
    <tr>
      <td>ENSMUST00000082421</td>
      <td>mt-Cytb</td>
      <td>361</td>
    </tr>
  </tbody>
</table>

### Quantification of infectivity

WT BMMs were plated on a sterile #1.5 coverslip by placing the coverslip in a tissue-culture-treated six-well plates and adding 1.5 × 106 BMMs/well in antibiotic-free media 24 hr prior to infection. Twofold dilutions of L. pneumophila strains used for infections were grown overnight in liquid buffered-yeast-extract culture and, at the time of infection, cultures with an optical density (600 nm) greater than 4.0 were selected. BMMs were infected at an MOI of 3 by centrifugation for 10 min at 400 xg. Media was changed after one hour of infection. At 6 hr post-infection coverslips were collected, washed in PBS, and placed in fixative solution (100 uM sodium periodate, 75 uM Lysine, 2.9 uM NaH2PO4, 3.2% sucrose, and 4% paraformaldehyde) for 1 hr at 37°C. Following fixation BMMs were blocked in 2% goat serum in PBS. To stain extracellular L. pneumophila, blocked BMMs were incubated with a rabbit anti-Legionella antibody (RRID: AB_231859; Fitzgerald Industries International, North Acton, MA, USA 20-LR45), washed in PBS, and stained with a goat-anti-rabbit IgG secondary antibody conjugated to Cascade Blue (RRID: AB_2536453; ThermoFisher Scientific, Waltham, MA, USA, C-2764). In some experiments, mammalian cell membrane was labeled with FITC-labeled wheat germ agglutinin (Sigma-Aldrich, St. Louis, MO, L4895) prior to permeabilization. BMMs were permeabilized by dipping coverslips into ice-cold methanol. Permeabilized BMMs were blocked with 2% goat serum and stained with a rabbit anti-Legionella antibody (Fitzgerald Industries International, North Acton, MA, 20-LR45) followed by incubation with a goat-anti-rabbit IgG secondary antibody conjugated to TexasRed (RRID: AB_2556776; ThermoFisher Scientific, Waltham, MA, T-2767) to mark all (intracellular and extracellular) L. pneumophila. Coverslips were mounted in vectashield antifade mounting medium (Vector Laboratories, Burlingame, CA, H-1000) and visualized on a Nikon TE2000 inverted microscope. All antibody stains were incubated for 30 min at 37°C and all blocking steps were incubated for 60 min at 37°C.

Importantly, the staining method described above results in intracellular bacteria staining positive for TexasRed while extracellular bacteria are double positive for Cascade Blue and TexasRed. Quantification of infectivity was undertaken by two methods using the differential staining of intracellular and extracellular L pneumophila. In experiments where differential contrast (DIC) microscopy, Cascade Blue, and TexasRed were visualized counting of intracellular bacteria in BMMs was done by hand using the image analysis software ImageJ (RRID:SCR_003070; Rasband, W.S., ImageJ, U. S. National Institutes of Health, Bethesda, Maryland, USA, http://imagej.nih.gov/ij/, 1997–2016) and the Cell Counter plugin (https://imagej.nih.gov/ij/plugins/cell-counter.html). Uninfected BMMs were classified as BMMs that were not associated with L. pneumophila or only associated with extracellular (Cascade Blue + TexasRed double positive) bacteria. Infected BMMs were classified as macrophages containing at least one intracellular L. pneumophila (Texas Red only), independent of the number of extracellular bacteria associated with the BMM. In experiments where the cell membrane of BMMs was labeled with FITC-conjugated wheat germ agglutinin along with DIC, Cascade Blue, and TexasRed, analysis of infectivity was undertaken using the imaging software Imaris (RRID:SCR_007370; Bitplane, Zurich, Switzerland). Using Imaris, surfaces of BMMs were drawn on the FITC-conjugated wheat germ agglutinin channel to mark individual BMMs. All extracellular bacteria were removed from analysis by generating a new channel that subtracted the Cascade Blue channel from the TexasRed channel, for example Intracellular Channel = TexasRed Channel – (Scaling Value x Cascade Blue Channel). The scaling value was calculated by measuring the average pixel intensities in each channel for double positive bacteria. As an example, if the TexasRed channel had an average pixel intensity of 350 and the Cascade Blue channel was 3500 then the equation would be: Intracellular Channel = TexasRed Channel – (0.1 x Cascade Blue Channel). The outcome of this calculation is the generation of a channel that removes the TexasRed signal of extracellular bacteria, thus allowing for analysis of bacteria that are only intracellular. Lastly, using the Sortomato utility (http://open.bitplane.com/tabid/235/Default.aspx?id=90) in Imaris, new cell surfaces were drawn for cells that contained a signal in the new Intracellular channel (with double positive bacteria removed), marking cells infected with an intracellular bacterium. Surfaces were also drawn for cells that did not have a signal in the Intracellular channel, marking uninfected BMMs or BMMs only associated with extracellular L. pneumophila. Results were checked by eye to confirm that all surfaces accurately marked uninfected and infected BMMs; the surfaces generated by Sortomato were used to quantify infectivity.

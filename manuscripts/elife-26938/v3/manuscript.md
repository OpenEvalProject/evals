# A broadly distributed toxin family mediates contact-dependent antagonism between gram-positive bacteria

## Authors

- John C Whitney<sup>1</sup> ([ORCID: 0000-0002-4517-8836](https://orcid.org/0000-0002-4517-8836))
- S Brook Peterson<sup>1</sup> ([ORCID: 0000-0003-2648-0965](https://orcid.org/0000-0003-2648-0965))
- Jungyun Kim<sup>1</sup> ([ORCID: 0000-0003-3793-4264](https://orcid.org/0000-0003-3793-4264))
- Manuel Pazos<sup>2</sup>
- Adrian J Verster<sup>3</sup>
- Matthew C Radey<sup>1</sup>
- Hemantha D Kulasekara<sup>1</sup>
- Mary Q Ching<sup>1</sup>
- Nathan P Bullen<sup>4</sup>
- Diane Bryant<sup>6</sup>
- Young Ah Goo<sup>7</sup>
- Michael G Surette<sup>4</sup>
- Elhanan Borenstein<sup>3</sup>
- Waldemar Vollmer<sup>2</sup>
- Joseph D Mougous<sup>1</sup> ([ORCID: 0000-0002-5417-4861](https://orcid.org/0000-0002-5417-4861)) †

### Affiliations

1. Department of Microbiology University of Washington School of Medicine Seattle United States
2. Centre for Bacterial Cell Biology, Institute for Cell and Molecular Biosciences Newcastle University Newcastle United Kingdom
3. Department of Genome Sciences University of Washington Seattle United States
4. Michael DeGroote Institute for Infectious Disease Research McMaster University Hamilton Canada
5. Department of Biochemistry and Biomedical Sciences McMaster University Hamilton Canada
6. Experimental Systems Group Advanced Light Source Berkeley United States
7. Northwestern Proteomics Core Facility Northwestern University Chicago United States
8. Department of Medicine, Farncombe Family Digestive Health Research Institute McMaster University Hamilton Canada
9. Department of Computer Science and Engineering University of Washington Seattle United States
10. Santa Fe Institute Santa Fe United States
11. Howard Hughes Medical Institute, University of Washington School of Medicine Seattle United States

† Corresponding author

## Abstract

The Firmicutes are a phylum of bacteria that dominate numerous polymicrobial habitats of importance to human health and industry. Although these communities are often densely colonized, a broadly distributed contact-dependent mechanism of interbacterial antagonism utilized by Firmicutes has not been elucidated. Here we show that proteins belonging to the LXG polymorphic toxin family present in Streptococcus intermedius mediate cell contact- and Esx secretion pathway-dependent growth inhibition of diverse Firmicute species. The structure of one such toxin revealed a previously unobserved protein fold that we demonstrate directs the degradation of a uniquely bacterial molecule required for cell wall biosynthesis, lipid II. Consistent with our functional data linking LXG toxins to interbacterial interactions in S. intermedius, we show that LXG genes are prevalent in the human gut microbiome, a polymicrobial community dominated by Firmicutes. We speculate that interbacterial antagonism mediated by LXG toxins plays a critical role in shaping Firmicute-rich bacterial communities.

## Introduction

Bacteria in polymicrobial environments must persist in the face of frequent physical encounters with competing organisms. Studies have revealed Gram-negative bacterial species contend with this threat by utilizing pathways that mediate antagonism toward contacting bacterial cells (Konovalova and Søgaard-Andersen, 2011). For instance, Proteobacteria widely employ contact-dependent inhibition (CDI) to intoxicate competitor cells that share a high degree of phylogenetic relatedness (Hayes et al., 2014). Additionally, both Proteobacteria and bacteria belonging to the divergent phylum Bacteroidetes deliver toxins to competitor Gram-negative cells in an indiscriminate fashion through the type VI secretion system (T6SS) (Russell et al., 2014a, 2014b). Although toxin delivery by CDI and the T6SS is mechanistically distinct, cells harboring either pathway share the feature of prohibiting self-intoxication with immunity proteins that selectively inactivate cognate toxins through direct binding.

Few mechanisms that mediate direct antagonism between Gram-positive bacteria have been identified. In Bacillus subtilis, Sec-exported proteins belonging to the YD-repeat family have been shown to potently inhibit the growth of contacting cells belonging to the same strain (Koskiniemi et al., 2013); however, to our knowledge, a pathway that mediates interspecies antagonism between Gram-positive bacteria has not been identified. Given that Gram-positive and Gram-negative bacteria inhabit many of the same densely populated polymicrobial environments (e.g. the human gut), it stands to reason that the former should also possess mechanisms for more indiscriminate targeting of competing cells.

Contact-dependent toxin translocation between bacteria is primarily achieved using specialized secretion systems. Gram-negative export machineries of secretion types IV, V, and VI have each been implicated in this process (Aoki et al., 2005; Hood et al., 2010; Souza et al., 2015). A specialized secretion system widely distributed among Gram-positive bacteria is the Esx pathway (also referred to as type VII secretion) (Abdallah et al., 2007). This pathway was first identified in Mycobacterium tuberculosis, where it plays a critical role in virulence (Stanley et al., 2003). Indeed, attenuation of the vaccine strain M. bovis BCG can be attributed to a deletion inactivating ESX-1 secretion system present in virulence strains (Lewis et al., 2003; Pym et al., 2003). Subsequent genomic studies revealed that the Esx pathway is widely distributed in Actinobacteria, and that a divergent form is present in Firmicutes (Gey Van Pittius et al., 2001; Pallen, 2002). Though they share little genetic similarity, all Esx pathways studied to-date utilize a characteristic FtsK-like AAA+ ATPase referred to as EssC (or EccC) to catalyze the export of one or more substrates belonging to the WXG100 protein family (Ates et al., 2016). Proteins in this family, including ESAT-6 (EsxA) and CFP10 (EsxB) from M. tuberculosis, heterodimerize in order to transit the secretion machinery.

The presence of the Esx secretion system in environmental bacteria as well as commensal and pathogenic bacteria that specialize in colonizing non-sterile sites of their hosts, suggests that the pathway may be functionally pliable. Supporting this notion, ESX-3 of M. tuberculosis is required for mycobactin siderophore-based iron acquisition and the ESX-1 and ESX-4 systems of M. smegmatis are linked to DNA transfer (Gray et al., 2016; Siegrist et al., 2009). In Firmicutes, a Staphylococcus aureus Esx-exported DNase toxin termed EssD (or EsaD) has been linked to virulence and contact-independent intraspecies antibacterial activity (Cao et al., 2016; Ohr et al., 2017).

Aravind and colleagues have noted that Esx secretion system genes are often linked to genes encoding polymorphic toxins belonging to the LXG protein family (Zhang et al., 2012). Analogous to characteristic antimicrobial polymorphic toxins of Gram-negative bacteria, the LXG proteins consist of a conserved N-terminal domain (LXG), a middle domain of variable length, and a C-terminal variable toxin domain. The LXG domain is predicted to adopt a structure resembling WXG100 proteins, thus leading to speculation that these proteins are Esx secretion system substrates (Zhang et al., 2011). Despite the association between LXG proteins and the Esx secretion system, to-date there are no experimental data linking them functionally. However, an intriguing study performed by Hayes and colleagues demonstrated antibacterial properties of B. subtilis LXG RNase toxins via heterologous expression in E. coli (Holberger et al., 2012). This growth inhibition was alleviated by co-expression of immunity determinants encoded adjacent to cognate LXG genes. We show here that LXG proteins transit the Esx secretion system of Streptococcus intermedius (Si) and function as antibacterial toxins that mediate contact-dependent interspecies antagonism.

## Results

### LXG proteins are Esx secretion system substrates

We initiated our investigation into the function of LXG proteins by characterizing the diversity and distribution of genes encoding these proteins across all sequenced genomes from Firmicutes. As noted previously, the C-terminal domains in the LXG family members we identified are highly divergent, exhibiting a wide range of predicted activities (Figure 1a) (Zhang et al., 2012). LXG protein-encoding genes are prevalent and broadly distributed in the classes Clostridiales, Bacillales and Lactobacillales (Figure 1A). Notably, a significant proportion of organisms in these taxa are specifically adapted to the mammalian gut environment. Indeed, we find that LXG genes derived from reference genomes of many of these gut-adapted bacteria are abundant in metagenomic datasets from human gut microbiome samples (Figure 1A and Figure 1—figure supplement 1). An LXG toxin that is predicted to possess ADP-ribosyltransferase activity – previously linked to interbacterial antagonism in Gram-negative organisms – was particularly abundant in a subset of human gut metagenomes (Zhang et al., 2012). Close homologs of this gene are found in Ruminococcus, a dominant taxa in the human gut microbiome, potentially explaining the frequency of this gene (Wu et al., 2011).

![Figure 1.](https://cdn.elifesciences.org/articles/26938/elife-26938-fig1-v3.jpg)

**Figure 1.:** (A) Dendogram depicts LXG-containing genera within Firmicutes, clustered by class and order. Circle size indicates the number of sequenced genomes searched within each genus and circle color represents percentage of those found to contain at least one LXG protein. For classes or orders in which no LXG domain-containing proteins were found, the number of genera evaluated is indicated in parentheses; those consisting of Gram-negative organisms are boxed with dashed lines. Grey boxes contain predicted domain structures for representative divergent LXG proteins. Depicted are LXG-domains (pink), spacer regions (light grey) and C-terminal polymorphic toxin domains (NADase, purple; non-specific nuclease, orange; AHH family nuclease, green; ADP-ribosyltransferase, blue; lipid II phosphatase based on orthology to TelC (defined biochemically herein), yellow; EndoU family nuclease, brown; unknown activity, dark grey). (B) Heatmap depicting the relative abundance (using logarithmic scale) of selected LXG genes detected in the Integrated Gene Catalog (IGC). A complete heatmap is provided in Figure 1—figure supplement 1. Columns represent individual human gut metagenomes from the IGC database and rows correspond to LXG genes. Grey lines link representative LXG toxins in (A) to their corresponding (≥95% identity) IGC group in (B).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/26938/elife-26938-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** Heatmap depicting the relative abundance (using logarithmic scale) of LXG genes detected in the Integrated Gene Catalog (IGC). Columns represent individual human gut metagenomes from the IGC database and rows correspond to LXG genes. Row and column ordering was determined by hierarchical clustering using Euclidian distance and complete linkage.

We next sought to determine whether LXG proteins are secreted via the Esx pathway. The toxin domain of several of the LXG proteins we identified shares homology and predicted catalytic residues with M. tuberculosis TNT, an NAD+-degrading (NADase) enzyme (Figure 2—figure supplement 1A) (Sun et al., 2015). Si, a genetically tractable human commensal and opportunistic pathogen, is among the bacteria we identified that harbor a gene predicted to encode an NADase LXG protein (Claridge et al., 2001); we named this protein TelB (Toxin exported by Esx with LXG domain B). Attempts to clone the C-terminal toxin domain of TelB (TelBtox) were initially unsuccessful, suggesting the protein exhibits a high degree of toxicity. Guided by the TNT structure, we circumvented this by assembling an attenuated variant (H661A) that was tolerated under non-induced conditions (TelBtox*) (Figure 2—figure supplement 1A) (Sun et al., 2015). Induced expression of TelBtox* inhibited E. coli growth and reduced cellular NAD+ levels (Figure 2A, Figure 2—figure supplement 1B). The extent of NAD+ depletion mirrored that catalyzed by expression of a previously characterized interbacterial NADase toxin, Tse6, and importantly, intracellular NAD+ levels were unaffected by an unrelated bacteriostatic toxin, Tse2 (Hood et al., 2010; Whitney et al., 2015). Furthermore, substitution of a second predicted catalytic residue of TelB (R626A), abrogated toxicity of TelBtox* and significantly restored NAD+ levels (Figure 2—figure supplement 1B–C).

![Figure 2.](https://cdn.elifesciences.org/articles/26938/elife-26938-fig2-v3.jpg)

**Figure 2.:** (A) NAD+ levels in E. coli cells expressing a non-NAD+ -degrading toxin (Tse2), the toxin domain of a known NADase (Tse6tox), an inducibly toxic variant of the C-terminal toxin domain of TelB (TelBtox*), a variant of TelBtox* with significantly reduced toxicity (TelBtox*R626A) and TelBtox* co-expressed with its cognate immunity protein TipB. Cellular NAD+ levels were assayed 60 min after induction of protein expression and were normalized to untreated cells. Mean values (n = 3) ± SD are plotted. Asterisks indicate statistically significant differences in NAD+ levels compared to vector control (p<0.05). (B) NAD+ consumption by culture supernatants from the indicated Si strains. Fluorescent images of supernatant droplets supplemented with 2 mM NAD+ for 3 hr; brightness is proportional to NAD+ concentration and was quantified using densitometry. Mean values ± SD (n = 3) are plotted. Asterisks indicate statistically significant differences in NAD+ turnover compared to wild-type SiB196 (p<0.05). (C) Regions of the SiB196 genome encoding Esx-exported substrates. Genes are colored according to functions encoded (secreted Esx structural components, orange; secreted LXG toxins, dark purple; immunity determinants, light purple; WXG100-like proteins, green; other, grey). (D) Western blot analysis of TelC secretion in supernatant (Sup) and cell fractions of wild-type or essC-inactivated SiB196.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/26938/elife-26938-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** (A) Structural model of TelBtox based on TNT toxin from M. tuberculosis. Conserved residues implicated in NAD+ binding are indicated. (B) Viability of E. coli cells grown on solid media harboring inducible plasmids expressing TelBtox*, TelBtox*R626A or an empty vector control. Mean c.f.u. values ± SD (n = 3) are plotted. Asterisk indicates a statistically significant difference in E. coli viability relative to vector control (p<0.05) (C) Growth in liquid media of E. coli cells expressing plasmids shown in (B). Protein expression was induced at the indicated time (arrow). Error bars indicate ± SD (n = 3).

Determination of the biochemical activity of TelB provided a means to test our hypothesis that LXG proteins are substrates of the ESX secretion pathway. Using an assay that exploits fluorescent derivatives of NAD+ that form under strongly alkaline conditions, we found that concentrated cell-free supernatant of an Si strain containing telB (SiB196) possesses elevated levels of NADase activity relative to that of a strain lacking telB (Si27335) (Figure 2B) (Johnson and Morrison, 1970; Olson et al., 2013; Whiley and Beighton, 1991). Furthermore, the NADase activity present in the supernatant of SiB196 was abolished by telB inactivation. Export of Esx substrates relies on EssC, a translocase with ATPase activity (Burts et al., 2005; Rosenberg et al., 2015). Inactivation of essC also abolished NADase activity in the supernatant of SiB196, suggesting that TelB utilizes the Esx pathway for export.

The genome of SiB196 encodes two additional LXG proteins, which we named TelA and TelC (Figure 2C). To determine if these proteins are also secreted in an Esx-dependent fashion, we collected cell-free supernatants from stationary phase cultures of wild-type and essC-deficient SiB196. Extensive dialysis was used to reduce contamination from medium-derived peptides and the remaining extracellular proteins were precipitated and identified using semi-quantitative mass spectrometry (Liu et al., 2004). This technique revealed that each of the LXG proteins predicted by the Si genome is exported in an Esx-dependent manner (Table 1). Western blot analysis of TelC secretion by wild-type and the essC-lacking mutant further validated Esx-dependent export (Figure 2D). Together, these data indicate that LXG proteins are substrates of the Esx secretion system.

**Table 1.**
 The Esx-dependent extracellular proteome of S. intermedius B196.


<table>
  <thead>
    <tr>
      <th>Locus tag</th>
      <th>Wild-type</th>
      <th>ΔessC</th>
      <th>Relative abundance (Wild-type/ΔessC)</th>
      <th>Esx function</th>
      <th>Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SIR_0169*</td>
      <td>19.67†</td>
      <td>0</td>
      <td>Not detected in ΔessC</td>
      <td>LXG protein‡</td>
      <td>TelA</td>
    </tr>
    <tr>
      <td>SIR_0176</td>
      <td>14.67</td>
      <td>0</td>
      <td>Not detected in ΔessC</td>
      <td>Structural component</td>
      <td>EsaA</td>
    </tr>
    <tr>
      <td>SIR_1489</td>
      <td>12.00</td>
      <td>0</td>
      <td>Not detected in ΔessC</td>
      <td>LXG protein</td>
      <td>TelC</td>
    </tr>
    <tr>
      <td>SIR_1516</td>
      <td>9.33</td>
      <td>0</td>
      <td>Not detected in ΔessC</td>
      <td>-</td>
      <td>Trigger Factor</td>
    </tr>
    <tr>
      <td>SIR_0179</td>
      <td>5.33</td>
      <td>0</td>
      <td>Not detected in ΔessC</td>
      <td>LXG protein</td>
      <td>TelB</td>
    </tr>
    <tr>
      <td>SIR_0166</td>
      <td>140.00</td>
      <td>17.48</td>
      <td>8.01</td>
      <td>Structural component</td>
      <td>EsxA</td>
    </tr>
    <tr>
      <td>SIR_0273</td>
      <td>15.33</td>
      <td>2.28</td>
      <td>6.73</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>SIR_1626</td>
      <td>15.00</td>
      <td>2.28</td>
      <td>6.58</td>
      <td>-</td>
      <td>GroEL</td>
    </tr>
    <tr>
      <td>SIR_0832</td>
      <td>12.33</td>
      <td>8.36</td>
      <td>1.48</td>
      <td>-</td>
      <td>Enolase</td>
    </tr>
    <tr>
      <td>SIR_1904</td>
      <td>49.00</td>
      <td>37.24</td>
      <td>1.32</td>
      <td>-</td>
      <td>Putative serine protease</td>
    </tr>
    <tr>
      <td>SIR_1382</td>
      <td>26.00</td>
      <td>19.76</td>
      <td>1.32</td>
      <td>-</td>
      <td>Fructose-bisphosphate aldolase</td>
    </tr>
    <tr>
      <td>SIR_0648</td>
      <td>21.67</td>
      <td>17.48</td>
      <td>1.24</td>
      <td>-</td>
      <td>50S ribosomal protein L7/L12</td>
    </tr>
    <tr>
      <td>SIR_0212</td>
      <td>47.00</td>
      <td>39.52</td>
      <td>1.19</td>
      <td>-</td>
      <td>Elongation Factor G</td>
    </tr>
    <tr>
      <td>SIR_0081</td>
      <td>8.67</td>
      <td>7.60</td>
      <td>1.14</td>
      <td>-</td>
      <td>Putative outer membrane protein</td>
    </tr>
    <tr>
      <td>SIR_1676</td>
      <td>16.33</td>
      <td>14.44</td>
      <td>1.13</td>
      <td>-</td>
      <td>phosphoglycerate kinase</td>
    </tr>
    <tr>
      <td>SIR_1523</td>
      <td>12.67</td>
      <td>12.92</td>
      <td>0.98</td>
      <td>-</td>
      <td>DnaK</td>
    </tr>
    <tr>
      <td>SIR_1154</td>
      <td>10.33</td>
      <td>10.64</td>
      <td>0.97</td>
      <td>-</td>
      <td>Putative bacteriocin accessory protein</td>
    </tr>
    <tr>
      <td>SIR_1027</td>
      <td>63.00</td>
      <td>67.64</td>
      <td>0.93</td>
      <td>-</td>
      <td>Elongation Factor Tu</td>
    </tr>
    <tr>
      <td>SIR_1455</td>
      <td>14.00</td>
      <td>15.96</td>
      <td>0.88</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>SIR_0758</td>
      <td>13.00</td>
      <td>15.20</td>
      <td>0.86</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>SIR_1387</td>
      <td>9.33</td>
      <td>11.40</td>
      <td>0.82</td>
      <td>-</td>
      <td>Putative extracellular solute-binding protein</td>
    </tr>
    <tr>
      <td>SIR_0492</td>
      <td>12.33</td>
      <td>15.20</td>
      <td>0.81</td>
      <td>-</td>
      <td>Putative adhesion protein</td>
    </tr>
    <tr>
      <td>SIR_1033</td>
      <td>17.67</td>
      <td>24.32</td>
      <td>0.73</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>SIR_1359</td>
      <td>14.00</td>
      <td>19.76</td>
      <td>0.71</td>
      <td>-</td>
      <td>Penicillin-binding protein 3</td>
    </tr>
    <tr>
      <td>SIR_0011</td>
      <td>12.33</td>
      <td>17.48</td>
      <td>0.71</td>
      <td>-</td>
      <td>Beta-lactamase class A</td>
    </tr>
    <tr>
      <td>SIR_1546</td>
      <td>8.33</td>
      <td>12.16</td>
      <td>0.69</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>SIR_0040</td>
      <td>101.67</td>
      <td>160.36</td>
      <td>0.63</td>
      <td>-</td>
      <td>Putative stress protein</td>
    </tr>
    <tr>
      <td>SIR_1608</td>
      <td>11.00</td>
      <td>18.24</td>
      <td>0.60</td>
      <td>-</td>
      <td>Putative endopeptidase O</td>
    </tr>
    <tr>
      <td>SIR_1549</td>
      <td>7.33</td>
      <td>12.16</td>
      <td>0.60</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>SIR_1675</td>
      <td>79.00</td>
      <td>132.24</td>
      <td>0.60</td>
      <td>-</td>
      <td>Putative cell-surface antigen I/II</td>
    </tr>
    <tr>
      <td>SIR_1418</td>
      <td>11.33</td>
      <td>21.28</td>
      <td>0.53</td>
      <td>-</td>
      <td>Putative transcriptional regulator LytR</td>
    </tr>
    <tr>
      <td>SIR_0080</td>
      <td>11.00</td>
      <td>21.28</td>
      <td>0.52</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>SIR_1025</td>
      <td>28.33</td>
      <td>63.84</td>
      <td>0.44</td>
      <td>-</td>
      <td>Lysozyme</td>
    </tr>
    <tr>
      <td>SIR_0113</td>
      <td>10.67</td>
      <td>24.32</td>
      <td>0.44</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>SIR_0297</td>
      <td>8.33</td>
      <td>24.32</td>
      <td>0.34</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

_*Rows highlighted in green correspond to proteins linked to the Esx pathway.†Values correspond to average SC (spectral counts) of triplicate biological replicates for each strain.‡Functional link of LXG proteins to Esx secretion pathway defined in the study._

### Contact-dependent interspecies antagonism is mediated by LXG toxins

The export of LXG proteins by the Esx pathway motivated us to investigate their capacity for mediating interbacterial antagonism. The C-terminal domains of TelA (TelAtox) and TelC (TelCtox) bear no homology to characterized proteins, so we first examined the ability of these domains to exhibit toxicity in bacteria. TelAtox and TelBtox* inhibited growth when expressed in the cytoplasm of E. coli, whereas TelCtox did not exhibit toxicity in this cellular compartment (Figure 3A). Given the capacity of some interbacterial toxins to act on extracellular structures, we assessed the viability of Si cells expressing TelCtox targeted to the sec translocon. In contrast to TelCtox production, overexpression of a derivative bearing a signal peptide directing extracellular expression (ss-TelCtox) exhibited significant toxicity (Figure 3B).

![Figure 3.](https://cdn.elifesciences.org/articles/26938/elife-26938-fig3-v3.jpg)

**Figure 3.:** (A) Viability of E. coli cells grown on solid media harboring inducible plasmids expressing the C-terminal toxin domains of the three identified SiB196 LXG proteins or an empty vector control. (B) SiB196 colonies recovered after transformation with equal concentrations of constitutive expression plasmids carrying genes encoding the indicated proteins. ss-TelCtox is targeted to the sec translocon through the addition of the secretion signal sequence from S. pneumoniae LysM (SP_0107). Error bars represent ± SD (n = 3). Asterisk indicates a statistically significant difference in Si transformation efficiency relative to TelCtox (p<0.05). (C) Viability of E. coli cells grown on solid media harboring inducible plasmids co-expressing the indicated proteins. Empty vector controls are indicated by a dash. Mean c.f.u. values ± SD (n = 3) are plotted. Asterisks indicate statistically significant differences in E. coli viability relative to vector control (p<0.05) (D) Intra-species growth competition experiments between the indicated bacterial strains. Competing strains were mixed and incubated in liquid medium or on solid medium for 30 hr and both initial and final populations of each strain were enumerated by plating on selective media. The competitive index was determined by comparing final and initial ratios of the two strains. Asterisks indicate outcomes statistically different between liquid and solid medium (n = 3, p<0.05). (E) Intra-species growth competition experiments performed as in (D) except for the presence of a filter that inhibits cell-cell contact. No contact, filter placed between indicated donor and susceptible recipient (∆telB ∆tipB) strains; Contact, donor and susceptible recipient strains mixed on same side of filter. Asterisks indicate statistically different outcomes (n = 3, p<0.05). Note that recipient cell populations have an Esx-independent fitness advantage in these experiments by virtue of their relative proximity to the growth substrate. (F) Inter-species growth competition experiments performed on solid or in liquid (E. faecalis) medium between Si wild-type and ∆essC donor strains and the indicated recipient organisms. Si23775 lacks tipA and tipB and is therefore potentially susceptible to TelA and TelB delivered by SiB196. Asterisks indicate outcomes where the competitive index of wild-type was significantly higher than an ∆essC donor strain (n = 3, p<0.05). Genetic complementation of the mutant phenotypes presented in this figure was confounded by inherent plasmid fitness costs irrespective of the inserted sequence. As an alternative, we performed whole genome sequencing on strains ∆essC, ∆telB, ∆telC, ∆telB ∆tipB, and ∆telC ∆tipC, which confirmed the respective desired mutation as the only genetic difference between these strains. Sequences of these strains have been deposited to the NCBI Sequence Read Archive (BioProject ID: PRJNA388094).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/26938/elife-26938-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** (A) Bacterial two-hybrid assay for interaction between TelC and TipC. Adenylate cyclase subunit T25 fusions (TipC and Zip control protein) and T18 fusions (TelC and fragments thereof) were coexpressed in the indicated combinations. Successful interaction results in production of blue pigment. (B) ITC analysis indicates TelCtox and mature TipC (TipCΔSS) interact with nanomolar affinity. The top panel displays the heats of injection, whereas the bottom panel shows the normalized integration data as a function of the syringe and cell concentrations.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/26938/elife-26938-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** (A) Intra-species growth competition experiments between the indicated Si B196 strains. Competing strains were mixed at a ratio of 40:1 [donor:recipient] and concentrated to OD600nm = 20. Competition outcomes were determined after 24 hr by enumerating c.f.u. on selective media. (B) Coomassie stained gel of purified TelC-his6. (C) Growth in liquid media of SiB196ΔtelC ΔtipC cells incubated with buffer (Ctrl) or 0.1 mg/mL TelC-his6. Error bars indicate ± SD (n = 3).

We next evaluated whether the Tel proteins, like the substrates of interbacterial toxin delivery systems in Gram-negative bacteria, are inactivated by genetically linked specialized cognate immunity determinants. By co-expressing candidate open reading frames located downstream of each tel gene, we identified a cognate tip (tel immunity protein) for each toxin (Figure 3B–C and Figure 3—figure supplement 1). We then sought to inactivate each of these factors to generate SiB196 strains sensitive to each of the Tel proteins. In SiB196, telA tipA loci are located immediately upstream of conserved esx genes (Figure 2C). We were unable to generate non-polar telA tipA-inactivated strains, and thus focused our efforts on the other two tel tip loci.

We reasoned that if LXG toxins target non-self cells, this process would occur either through diffusion or by facilitated transfer, the latter of which would likely require cell contact. Since we detect TelA-C secretion in liquid medium, we began our attempts to observe intercellular intoxication with wild-type and toxin-sensitive target cell co-culture. These efforts yielded no evidence of target cell killing or growth inhibition, including when co-incubations were performed at cell densities higher than that achievable through growth (Figure 3D, Figure 3—figure supplement 2A). The application of concentrated supernatants or purified TelC (to a final concentration of 0.1 mg/mL) to sensitive strains also did not produce evidence of toxicity (Figure 3—figure supplement 2B–C). This result is perhaps not surprising given the barrier presented by the Gram-positive cell wall (Forster and Marquis, 2012).

Next, we tested conditions that enforce cell contact. In each of these experiments, donor and recipient strains were grown in pure culture before they were mixed at defined ratios and cultured on a solid surface for 30 hr to promote cell-cell interactions. We observed significant growth inhibition of TelB- or TelC-susceptible strains co-cultured with wild-type, but not when co-cultured with strains lacking telB or telC, respectively (Figure 3D). A strain bearing inactivated essC was also unable to intoxicate a sensitive recipient. In competition experiments performed in parallel wherein the bacterial mixtures were grown in liquid culture, TelB and TelC-susceptible strains competed equally with wild type, suggesting that Esx-mediated intoxication requires prolonged cell contact. To further probe this requirement, we conducted related experiments in which wild-type donor cells were segregated from sensitive recipients by a semi-permeable (0.2 μm pore size) membrane (Figure 3E). This physical separation blocked intoxication, which taken together with the results of our liquid co-culture experiments and our finding that purified TelC is not bactericidal, strongly suggests that the mechanism of Esx-dependent intercellular LXG protein delivery requires immediate cell-cell contact.

In Gram-negative bacteria, some antagonistic cell contact-dependent pathways display narrow target range, whereas others act between species, or even between phyla (Hayes et al., 2014; Russell et al., 2014a). To begin to determine the target range of Esx-based LXG protein delivery, we measured its contribution to SiB196 fitness in interbacterial competition experiments with a panel of Gram-positive and -negative bacteria. The Esx pathway conferred fitness to SiB196 in competition with Si23775, S. pyogenes, and Enterococcus faecalis, an organism from a closely related genus (Figure 3F). On the contrary, the pathway did not measurably affect the competitiveness of SiB196 against Gram-negative species belonging to the phyla Proteobacteria (E. coli, Burkholderia thailandensis, Pseudomonas aeruginosa) or Bacteroidetes (Bacteriodes fragilis). These results demonstrate that the Esx pathway can act between species and suggest that its target range may be limited to Gram-positive bacteria.

### TelC targets the bacterial cell wall biosynthetic precursor lipid II

The Esx pathway is best known for its role in mediating pathogen-host cell interactions (Abdallah et al., 2007). Given this precedence, we considered the possibility that the antibacterial activity we observed may not be relevant physiologically. TelB degrades NAD+, a molecule essential for all cellular life, and therefore this toxin is not definitive in this regard. We next turned our attention to TelC, which elicits toxicity from outside of the bacterial cell (Figure 3B). This protein contains a conserved aspartate-rich motif that we hypothesized constitutes its enzymatic active site (Figure 4—figure supplement 1A). To gain further insight into TelC function, we determined the crystal structure of TelCtox to 2.0 Å resolution (Table 2). The structure of TelCtox represents a new fold; it is comprised of distinct and largely α-helical N- and C-terminal lobes (Figure 4A). The single β element of TelCtox is a hairpin that protrudes from the N-terminal lobe. Although TelCtox does not share significant similarity to previously determined structures, we located its putative active site within a shallow groove that separates the N- and C-terminal lobes. This region contains a calcium ion bound to several residues that comprise the conserved aspartate-rich motif. Site-specific mutagenesis of these residues abrogated TelC-based toxicity (Figure 4B,C, Figure 4—figure supplement 1B).

![Figure 4.](https://cdn.elifesciences.org/articles/26938/elife-26938-fig4-v3.jpg)

**Figure 4.:** (A) Space-filling representation of the 2.0 Å resolution TelCtox X-ray crystal structure. Protein lobes (red and blue), active site cleft (white) and Ca2+ (green) are indicated. (B) TelCtox structure rotated as indicated relative to (A) with transparent surface revealing secondary structure. (C) Magnification of the TelC active site showing Ca2+ coordination by conserved aspartate residues and water molecules. (D) Viability of S. aureus cells harboring inducible plasmids expressing the indicated proteins or a vector control. ss-TelCtox is targeted for secretion through the addition of the signal sequence encoded by the 5’ end of the hla gene from S. aureus. Mean c.f.u. values ± SD (n = 3) are plotted. Asterisk indicates a statistically significant difference in S. aureus viability relative to vector control (p<0.05) (E) Representative micrographs of S. aureus expressing ss-TelCtox or a vector control. Frames were acquired eight and 12 hr after spotting cells on inducing growth media. (F) Thin-layer chromotography (TLC) analysis of reaction products from incubation of synthetic Lys-type lipid II with buffer (Ctrl), TelCtox, or TelCtox and its cognate immunity protein TipC. (G) Partial HPLC chromatograms of radiolabeled peptidoglycan (PG) fragments released upon incubation of Lys-type lipid II with the indicated purified proteins. Schematics depict PG fragment structures (pentapeptide, orange; N-acetylmuramic acid, dark green; N-acetylglucosamine, light green; phosphate, black). Known fragment patterns generated by PBP1B + LpoB and colicin M serve as controls. (H) TLC analysis of reaction products generated from incubation of buffer (Ctrl), TelCtox or TelCtox and TipC with undecaprenyl phosphate (C55–P) (left) or undecaprenyl pyrophosphate (C55–PP) (right).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/26938/elife-26938-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** (A) Sequence logo representation of the aspartate-rich motif found among TelC orthologous proteins. Numbers indicate the amino acid positions in TelC from SiB196. (B) Image of SiB196 colonies recovered from transformation with plasmids expressing the indicated TelCtox variants.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/26938/elife-26938-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** (A and B) HPLC analysis of muropeptides generated by incubation of TelCtox, cellosyl muramidase or buffer with either S. aureus peptidoglycan sacculi (A) or lysostaphin endopeptidase treated (non-cross-linked) peptidoglycan sacculi (B). (C and D) HPLC analysis of S. aureus cell wall extracts from cells expressing ss-TelCtox or a vector control. Prior to chromatographic separation, cell walls were treated with either lysostaphin endopeptidase (C) or cellosyl muramidase (D).

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/26938/elife-26938-fig4-figsupp3-v3.jpg)

**Figure 4—figure supplement 3.:** (A) TLC analysis of reaction products from incubation of synthetic Lys-type lipid II with buffer (Ctrl) or TelC. (B) Inter-species growth competition experiments performed on solid medium between the indicated Si donor strains and E. faecalis. Asterisks indicate statistically significant differences in competitive indices (n = 3, p<0.05). (C) Growth of Saccharomyces cerevisiae upon expression of native TelCtox, or a derivative in which an added signal sequence targets the protein to the yeast secretory pathway (ss-TelCtox). Yeast strains carrying the empty vector or a toxic protein (Ctrl) are included for comparison. (D) Western blot analysis of TelCtox and ss-TelCtox in Saccharomyces cerevisiae. Black arrow denotes proteolytically processed ss-TelCtox.

**Table 2.**
 X-ray data collection and refinement statistics.


<table>
  <thead>
    <tr>
      <th></th>
      <th>TelC202-CT (Semet)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data Collection</td>
      <td></td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>0.979</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>C2221</td>
    </tr>
    <tr>
      <td>Cell dimensions</td>
      <td></td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>127.4, 132.7, 58.3</td>
    </tr>
    <tr>
      <td>α, β, γ (°)</td>
      <td>90.0, 90.0, 90.0</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>49.20–1.98 (2.03–1.98)*</td>
    </tr>
    <tr>
      <td>Total observations</td>
      <td>891817</td>
    </tr>
    <tr>
      <td>Unique observations</td>
      <td>34824</td>
    </tr>
    <tr>
      <td>Rpim (%)</td>
      <td>6.6 (138.5)</td>
    </tr>
    <tr>
      <td>I/σI</td>
      <td>11.4 (0.8)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>100.0 (99.9)</td>
    </tr>
    <tr>
      <td>Redundancy</td>
      <td>25.6 (23.4)</td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
    </tr>
    <tr>
      <td>Rwork / Rfree (%)</td>
      <td>22.4/24.6</td>
    </tr>
    <tr>
      <td>Average B-factors (Å2)</td>
      <td>53.8</td>
    </tr>
    <tr>
      <td>No. atoms</td>
      <td></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>2539</td>
    </tr>
    <tr>
      <td>Ligands</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>145</td>
    </tr>
    <tr>
      <td>Rms deviations</td>
      <td></td>
    </tr>
    <tr>
      <td>Bond lengths (Å)</td>
      <td>0.008</td>
    </tr>
    <tr>
      <td>Bond angles (°)</td>
      <td>0.884</td>
    </tr>
    <tr>
      <td>Ramachandran plot (%)</td>
      <td></td>
    </tr>
    <tr>
      <td>Total favored</td>
      <td>96.9</td>
    </tr>
    <tr>
      <td>Total allowed</td>
      <td>99.7</td>
    </tr>
    <tr>
      <td>Coordinate error (Å)</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>PDB code</td>
      <td>5UKH</td>
    </tr>
  </tbody>
</table>

_*Values in parentheses correspond to the highest resolution shell._

We next assessed the morphology of cells undergoing intoxication by TelCtox. Due to the potent toxicity of TelCtox in Si, we employed an inducible expression system in S. aureus as an alternative. S. aureus cells expressing extracellularly-targeted TelCtox exhibited significantly reduced viability (Figure 4D), and when examined microscopically, displayed a cessation of cell growth followed by lysis that was not observed in control cells (Figure 4E, Videos 1–2). Despite eliciting effects consistent with cell wall peptidoglycan disruption, isolated cell walls treated with TelCtox and peptidoglycan recovered from cells undergoing TelC-based intoxication showed no evidence of enzymatic digestion (Figure 4—figure supplement 2A–D). These data prompted us to consider that TelC corrupts peptidoglycan biosynthesis, which could also lead to the lytic phenotype observed (Harkness and Braun, 1989).

![Video 1.](https://cdn.elifesciences.org/articles/26938/elife-26938-media1.mp4.jpg)

**Video 1.:** Cells were imaged every 10 min.

![Video 2.](https://cdn.elifesciences.org/articles/26938/elife-26938-media2.mp4.jpg)

**Video 2.:** Cells were imaged every 10 min.

The immediate precursor of peptidoglycan is lipid II, which consists of the oligopeptide disaccharide repeat unit linked via pyrophosphate to a lipid carrier (Vollmer and Bertsche, 2008). Likely due to its distinctive and conserved structure, lipid II is the target of diverse antibacterial molecules (Breukink and de Kruijff, 2006; Oppedijk et al., 2016). To test activity against lipid II, we incubated the molecule with purified TelCtox. Analysis of the reaction products showed that TelCtox cleaves lipid II – severing the molecule at the phosphoester linkage to undecaprenyl (Figure 4F–G, Figure 4—figure supplement 3A). Reaction products were confirmed by mass spectrometry and inclusion of TipC inhibited their formation. Consumption of lipid II for peptidoglycan assembly generates undecaprenyl pyrophosphate (UPP), which is converted to undecaprenyl phosphate (UP), and transported inside the cell. The UP molecule then reenters peptidoglycan biosynthesis or is utilized as a carrier for another essential cell wall constituent, wall teichoic acid (WTA). Our experiments showed that TelCtox is capable of hydrolyzing cleaved undecaprenyl derivatives but displays a strict requirement for the pyrophosphate group (Figure 4H), indicating the potential for TelC to simultaneously disrupt two critical Gram-positive cell wall polymers. Consistent with its ability to inhibit a conserved step in peptidoglycan biosynthesis, TelC exhibited toxicity towards diverse Gram-positive species including Si (Figure 2B), S. aureus (Figure 4D) and E. faecalis (Figure 4—figure supplement 3B). These data do not explain our observation that cytoplasmic TelC is non-toxic, as the substrates we defined are present in this compartment. The substrates may be inaccessible or TelC could be inactive in the cytoplasm. It is worth noting that TelC contains a calcium ion bound at the interface of its N- and C-terminal lobes. Many secreted proteins that bind calcium utilize the abundance of the free ion in the milieu to catalyze folding. Taken together, our biochemical and phenotypic data strongly suggest that TelC is a toxin directed specifically against bacteria. While we cannot rule out that TelC may have other targets, we find that its expression in the cytoplasm or secretory pathway of yeast does not impact the viability of this model eukaryotic cell (Figure 4—figure supplement 3C–D).

### WXG100-like proteins bind cognate LXG proteins and promote toxin export

The majority of Esx substrates identified to-date belong to the WXG100 protein family. These proteins typically display secretion co-dependency and are essential for apparatus function. M. tuberculosis ESX-1 exports two WXG100 proteins, ESAT-6 and CFP10, and the removal of either inhibits the export of other substrates (Ates et al., 2016; Renshaw et al., 2002). LXG proteins do not belong to the WXG100 family; thus, we sought to determine how the Tel proteins influence Esx function in Si. Using Western blot analysis to measure TelC secretion and extracellular NADase activity as a proxy for TelB secretion, we found that telB- and telC-inactivated strains of Si retain the capacity to secrete TelC and TelB, respectively (Figure 5A–B). These data indicate that TelB and TelC are not required for core apparatus function and do not display secretion co-dependency.

![Figure 5.](https://cdn.elifesciences.org/articles/26938/elife-26938-fig5-v3.jpg)

**Figure 5.:** (A) NAD+ consumption assay of culture supernatants of the indicated SiB196 strains. Mean densitometry values ± SD (n = 3) are plotted. Asterisk indicates statistically significant difference in NAD+ turnover compared to wild-type SiB196 (p<0.05). (B) Western blot analysis of TelC secretion in supernatant (Sup) and cell fractions. (C) Western blot and coomassie stain analysis of CoIP assays of TelC-his6 co-expressed with either WxgB-V or WxgC-V proteins. (D) Bacterial two-hybrid assay for interaction between Tel and WXG100-like proteins. Adenylate cyclase subunit T25 fusions (WXG100-like proteins) and T18 fusions (Tel proteins and fragments thereof) were co-expressed in the indicated combinations. Bait-prey interaction results in blue color production. (E) Model depicting Esx-dependent cell-cell delivery of LXG toxins between bacteria. The schematic shows an Si donor cell containing cognate TelA-C (light shades) and WxgA-C (dark shades) pairs intoxicating a susceptible recipient cell. Molecular targets of LXG toxins identified in this study are depicted in the recipient cell.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/26938/elife-26938-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** The boundaries for the LXG and toxin domains for each protein are based on the protein-protein interaction data and bacterial toxicity assays, respectively, described in this work.

Interestingly, we noted genes encoding WXG100-like proteins upstream of telA-C (wxgA-C) (Figure 2C); however, these proteins were not identified in the extracellular proteome of Si (Table 1). Given the propensity for Esx substrates to function as heterodimers, we hypothesized that the Tel proteins specifically interact with cognate Wxg partners. In support of this, we found that WxgC, but not WxgB co-purified with TelC (Figure 5C). Moreover, using bacterial two-hybrid assays, we determined that this interaction is mediated by the LXG domain of TelC (Figure 5D). To investigate the generality of these findings, we next examined all pairwise interactions between the three Wxg proteins and the LXG domains of the three Tel proteins (TelA-CLXG) (Figure 5—figure supplement 1). We found that WxgA-C interact specifically with the LXG domain of their cognate toxins (Figure 5D). The functional relevance of the LXG–WXG100 interaction was tested by examining substrate secretion in a strain lacking wxgC. We found that wxgC inactivation abrogates TelC secretion, but not that of TelB (Figure 5A–B). In summary, these data suggest that cognate Tel–Wxg interaction facilitates secretion through the Esx pathway of Si (Figure 5E).

## Discussion

We present multiple lines of evidence that Esx-mediated delivery of LXG toxins serves as a physiological mechanism for interbacterial antagonism between Gram-positive bacteria. Our results suggest that like the T6S pathway of Gram-negative bacteria, the Esx system may mediate antagonism against diverse targets, ranging from related strains to species belonging to other genera (Schwarz et al., 2010). This feature of Esx secretion, in conjunction with the frequency by which we detect LXG genes in human gut metagenomes, suggests that the system could have significant ramifications for the composition of human-associated polymicrobial communities. Bacteria harboring LXG toxin genes are also components or pathogenic invaders of polymicrobial communities important in agriculture and food processing. For instance, LXG toxins may assist Listeria in colonizing fermented food communities dominated by Lactobacillus and Lactococcus (Farber and Peterkin, 1991). Of note, the latter genera also possess LXG toxins, which may augment their known antimicrobial properties. Our findings thus provide insights into the forces influencing the formation of diverse communities relevant to human health and industry.

Palmer and colleagues recently reported that the Esx system of Staphylococcus aureus exports EssD, a nuclease capable of inhibiting the growth of target bacteria in co-culture (Cao et al., 2016). The relationship between these findings and those we report herein is currently unclear. S. aureus EssD does not possess an LXG domain and was reported to be active against susceptible bacteria during co-incubation in liquid media, a condition we found not conducive to LXG toxin delivery (Figure 3D). It is evident that the Esx pathway is functionally pliable (Burts et al., 2005; Conrad et al., 2017; Gray et al., 2016; Gröschel et al., 2016; Manzanillo et al., 2012; Siegrist et al., 2009); therefore, it is conceivable that it targets toxins to bacteria through multiple mechanisms. The capacity of EssD to act against bacteria in liquid media could be the result of its over-expression from a plasmid, although we found that the exogenous administration of quantities of TelC far exceeding those likely achievable physiologically had no impact on sensitive recipient cells (Figure 3—figure supplement 2C). A later study of EssD function found no evidence of interbacterial targeting and instead reported that its nuclease activity affects IL-12 accumulation in infected mice (Ohr et al., 2017).

Our data suggest that, like a subset of substrates of the Esx systems of M. tuberculosis, LXG family members require hetero-dimerization with specific WXG100-like partners to be secreted (Ates et al., 2016). Hetero-dimerization is thought to facilitate secretion of these substrates due to the requirement for a bipartite secretion signal consisting of a YxxxD/E motif in the C-terminus of one partner in proximity to the WXG motif present in the turn between helices in the second protein (Champion et al., 2006; Daleke et al., 2012a; Poulsen et al., 2014; Sysoeva et al., 2014). While the canonical secretion signals found in other Esx substrates appear to be lacking in the LXG proteins and their interaction partners, structure prediction algorithms suggest they adopt similar helical hairpin structures, which could facilitate formation of an alternative form of the bipartite signal. Unlike previously characterized Esx substrates, we found that the LXG proteins are not co-dependent for secretion, and we failed to detect secretion of their WXG100-like interaction partners. This suggests that WxgA-C could function analogously to the EspG proteins of M. tuberculosis, which serve as intracellular chaperones facilitating delivery of specific substrates to the secretion machinery (Daleke et al., 2012b; Ekiert and Cox, 2014). Alternatively, Wxg–Lxg complexes could be secreted as heterodimers, but for technical reasons the Wxg member was undetected in our experiments. The paradigm of Lxg-Wxg interaction likely extends beyond S. intermedius, as we observe that LXG proteins from other species are commonly encoded within the same operon as Wxg homologs.

Our study leaves open the question of how Esx-exported LXG proteins reach their targets. In the case of TelC, the target resides on the extracellular face of the plasma membrane, and in the case of TelA and TelB, they are cytoplasmic. Crossing the thick Gram-positive cell wall is the first hurdle that must be overcome to deliver of each of these toxins. The size of LXG toxins exceeds that of molecules capable of free diffusion across the peptidoglycan sacculus (Forster and Marquis, 2012). Donor cell-derived cell wall hydrolytic enzymes may facilitate entry or the LXG proteins could exploit cell surface proteins present on recipient cells. Whether the entry of LXG toxins is directly coordinated by the Esx pathway is not known; our experiments do not rule-out that the requirement for donor-recipient cell contact reflects a step subsequent to secretion by the Esx pathway. Once beyond the sacculus, TelA and TelB must translocate across the plasma membrane. Our study has identified roles for the N- and C-terminal domains of LXG proteins; however, the function of the region between these two domains remains undefined and may participate in entry. Intriguingly, the central domains of TelA and TelB are each over 150 residues, whereas the LXG and toxin domains of TelC, which does not require access to the cytoplasm, appear to directly fuse (Figure 5—figure supplement 1). Based on the entry mechanisms employed by other interbacterial toxins, this central domain – or another part of the protein – could facilitate direct translocation, proteolytic release of the toxin domain, interaction with a recipient membrane protein, or a combination of these activities (Kleanthous, 2010; Willett et al., 2015).

We discovered that TelC, a protein lacking characterized homologs, adopts a previously unobserved fold and catalyzes degradation of the cell wall precursor molecule lipid II. This molecule is the target of the food preservative nisin, as well as the last-line antibiotic vancomycin, which is used to treat a variety of Gram-positive infections (Ng and Chan, 2016). Lipid II is also the target of the recently discovered antibiotic teixobactin, synthesized by the soil bacterium Eleftheria terrae (Ling et al., 2015). A particularly interesting property of this potential therapeutic is the low rate at which resistance is evolved. The apparent challenge of structurally modifying lipid II in order to subvert antimicrobials may explain why interbacterial toxins targeting this molecule have evolved independently in Gram-negative (colicin M) and -positive (TelC) bacteria (El Ghachi et al., 2006). We anticipate that biochemical characterization of additional LXG toxins of unknown function will reveal further Gram-positive cell vulnerabilities that could likewise be exploited in the design of new antibiotics.

## Materials and methods

### Bacterial strains and growth conditions

S. intermedius strains used in this study were derived from the sequenced strains ATCC 27335 and B196 (Supplementary file 1). S. intermedius strains were grown at 37°C in the presence of 5% CO2 in Todd Hewitt broth (THYB) or agar (THYA) supplemented with 0.5% yeast extract. When needed, media contained spectinomycin (75 μg/mL) or kanamycin (250 μg/mL). S. aureus USA300 derived strains were grown at 37°C in tryptic soy broth (TSB) or agar (TSA) supplemented with chloramphenicol (10 μg/mL) and xylose (2% w/v) when needed. E. faecalis OG1RF and S. pyogenes 5005 were grown at 37°C on Brain Heart Infusion (BHI) media. P. aeruginosa PAO1 and B. thailandensis E264 were grown at 37°C on THYA. B. fragilis NCTC9343 was grown anaerobically at 37°C on Brain Heart Infusion-supplemented (BHIS) media. E. coli strains used in this study included DH5α for plasmid maintenance, BL21 for protein expression and toxicity assays and MG1655 for competition experiments. E. coli strains were grown on LB medium supplemented with 150 μg/mL carbenicillin, 50 μg/mL kanamycin, 200 μg/mL trimethoprim, 75 μg/mL spectinomycin, 200 μM IPTG or 0.1% (w/v) rhamnose as needed. For co-culture experiments with S. intermedius strains, E. coli, B. thailandensis, P. aeruginosa, S. aureus, E. faecalis, S. pyogenes were grown on THYA. BHIS agar supplemented with sheep’s blood was used when B. fragilis was grown in co-culture with S. intermedius. S. cerevisiae BY4742 was grown on Synthetic Complete -uracil (SC-ura) medium at 30°C.

S. intermedius mutants were generated by replacing the gene to be deleted with a cassette conferring resistance to spectinomycin (derived from pDL277) or kanamycin (derived from pBAV1K-T5), as previously described (Tomoyasu et al., 2010). Briefly, the antibiotic resistance cassette was cloned between ~800 bp of sequence homologous to the regions flanking the gene to be deleted. The DNA fragment containing the cassette and flanking sequences was then linearized by restriction digest, gel purified, and ~250 ng of the purified fragment was added to 2 mL of log-phase culture pre-treated for two hours with competence peptide (200 ng/ml) to stimulate natural transformation. Cultures were further grown for four hours before plating on the appropriate antibiotic. All deletions were confirmed by PCR.

### DNA manipulation and plasmid construction

All DNA manipulation procedures followed standard molecular biology protocols. Primers were synthesized and purified by Integrated DNA Technologies (IDT). Phusion polymerase, restriction enzymes and T4 DNA ligase were obtained from New England Biolabs (NEB). DNA sequencing was performed by Genewiz Incorporated.

### Informatic analysis of LXG protein distribution

A comprehensive list of all clade names in the Firmicutes phylum was obtained from the List of Prokaryotic names with Standing in Nomenclature (http://www.bacterio.net/; updated 2017-02-02), a database that compiles comprehensive journal citations for every characterized prokaryotic species (Euzéby, 1997). This list was then compared with results obtained from a manually curated Jackhmmer search and LXG-containing Firmicutes were tabulated at the order, family, and genus levels (Finn et al., 2015; Mitchell et al., 2015). These results were binned into three categories based on the number of sequenced species and then further differentiated by the number of LXG-positive species within each genus. For species belonging to orders containing no predicted LXG encoding genes, the number of genera examined was tabulated and included in the dendogram.

### Identification of LXG genes in human gut metagenomes

The 240 nucleotide tags from the toxin domains were mapped using blastn to the Integrated Gene Catalog (Li et al., 2014) – a large dataset of previously identified microbiome genes and their abundances in several extensive microbiome studies (including HMP [Human Microbiome Project Consortium, 2012], MetaHiT [Qin et al., 2010], and a T2D Chinese cohort [Qin et al., 2012]). Genes to which at least one tag was mapped with >95% identity and >50% overlap were labeled as LXG genes. This set of LXG genes was further manually curated to filter out genes that lack the LXG targeting domain. In analyzing the relative abundance of the LXG genes across samples, relative abundances < 10−7 were assumed to represent noise and were set to 0. LXG genes that were not present above this threshold in any sample and samples with no LXG genes were excluded from the analysis.

### Determination of cellular NAD+ levels

Measurement of cellular NAD+ levels was performed as reported previously (Whitney et al., 2015). Briefly, E. coli strains harboring expression plasmids for Tse2, Tse6tox, TelBtox*, TelBtoxR626A, TelBtox*–TipB and a vector control were grown in LB media at 37°C to mid-log phase prior to induction of protein expression with 0.1% (w/v) rhamnose. 1 hr post-induction, cultures were diluted to OD600 = 0.5 and 500 μL of cells were harvested by microcentrifugation. Cells were then lysed in 0.2 M NaOH, 1% (w/v) cetyltrimethylammonium bromide (CTAB) followed by treatment with 0.4 M HCl at 60°C for 15 min. After neutralization with 0.5 M Tris base, samples were then mixed with an equal volume of NAD/NADH-Glo Detection Reagent (Promega) prepared immediately before use as per the instructions of the manufacturer. Luciferin bioluminescence was measured continuously using a Synergy H1 plate reader. The slope of the luciferin signal from the linear range of the assay was used to determine relative NAD+ concentration compared to a vector control strain.

### NADase assay

S. intermedius strains were grown to late-log phase before cells were removed by centrifugation at 3000 g for 15 min. Residual particulates were removed by vacuum filtration through a 0.2 um membrane and the resulting supernatants were concentrated 100-fold by spin filtration (30 kDa MWCO). NADase assays were carried out by mixing 50 μL of concentrated supernatant with 50 μL of PBS containing 2 mM NAD+ followed by incubation at room temperature for 2 hr. Reactions were terminated by the addition of 50 μL of 6M NaOH and incubated in the dark at room temperature for 15 min. Samples were analyzed by UV light at a wavelength of 254 nm and imaged using a FluorChemQ (ProteinSimple). Relative NAD+ consumption was determined using densitometry analysis of each of the indicated strain supernatants using the ImageJ software program (https://imagej.nih.gov/ij/).

### Bacterial toxicity experiments

To assess TelA and TelB toxicity in bacteria, stationary phase cultures of E. coli BL21 pLysS harboring the appropriate plasmids were diluted 106 and each 10-fold dilution was spotted onto 3% LB agar plates containing the appropriate antibiotics. 0.1% (w/v) L-rhamnose and 100 μM IPTG were added to the media to induce expression of toxin and immunity genes, respectively. For TelB, plasmids containing the wild-type toxin domain (under non-inducing conditions) were not tolerated. To circumvent this, SOE pcr was used to assemble a variant (H661A) that was tolerated under non-induced conditions. Based on the similarity of TelBtox to M. tuberculosis TNT toxin, this mutation likely reduces the binding affinity of TelB to NAD+ (Sun et al., 2015). To generate a TelB variant that exhibited significantly reduced toxicity under inducing conditions, a second mutation (R626A) was introduced in the toxin domain of TelB. For examination of TelC toxicity in S. intermedius, the gene fragment encoding TelCtox was fused to the constitutive P96 promoter followed by a start codon and cloned into pDL277 (Lo Sapio et al., 2012). For extracellular targeting of TelCtox in S. intermedius, the gene fragment encoding the sec-secretion signal (residues 1–30) of S. pneumoniae LysM (SP_0107) was fused to the 5’ end of telCtox, each of the telCtox site-specific variants and the telCtox–tipC bicistron. 500 ng of each plasmid was transformed in S. intermedius B196 and toxicity was assessed by counting the number of transformants. For examination of TelC toxicity S. aureus, the gene fragment encoding TelCtox was cloned into the xylose-inducible expression vector pEPSA5. For extracellular targeting, the gene fragment encoding the sec-secretion signal for hla was fused to the 5’ end of telCtox and telCtoxD401A. TelC-based toxicity was assessed in the same manner as was done for the above E. coli toxicity experiments except that xylose (2% w/v) was included in the media to induce protein expression. Detailed plasmid information can be found in Supplementary file 2.

### Time-lapse microscopy

S. aureus USA300 pEPSA5::ss-telC202-CT and S. aureus USA300 pEPSA5 were resuspended in TSB and 1–2 μL of each suspension was spotted onto an 1% (w/v) agarose pad containing typtic soy medium supplemented with 2% (w/v) xylose and sealed.

Microscopy data were acquired using NIS Elements (Nikon) acquisition software on a Nikon Ti-E inverted microscope with a 60× oil objective, automated focusing (Perfect Focus System, Nikon), a xenon light source (Sutter Instruments), and a CCD camera (Clara series, Andor). Time-lapse sequences were acquired at 10 min intervals over 12 hr at room temperature. Movie files included are representative of three biological replicates for each experiment.

### Extracellular proteome

200 mL cultures of S. intermedius B196 wild-type and ΔessC strains were grown to stationary phase in THYB before being pelleted by centrifugation at 2500 × g for 20 min at 4°C. Supernatant fractions containing secreted proteins were collected and spun at 2500 × g for an additional 20 min at 4°C and subsequently filtered through a 0.2 μm pore size membrane to remove residual cells and cell debris. Protease inhibitors (1 mM AEBSF, 10 mM leupeptin, and 1 mM pepstatin) were added to the filtered supernatants prior to dialysis in 4L of PBS using 10 kDa molecular weight cut off tubing at 4°C. After four dialysis buffer changes, the retained proteins were TCA precipitated, pelleted, washed in acetone, dried and resuspended in 1 mL of 100 mM ammonium bicarbonate containing 8 M urea. The denatured protein mixture was then desalted over a PD10 column prior to reduction, alkylation and trypsin digestion as described previously (Eshraghi et al., 2016). The resulting tryptic peptides were desalted and purified using C18 spin columns (Pierce) following the protocol of the manufacturer before being vacuum dried and resuspended in 10 µL of acetonitrile/H2O/formic acid (5/94.9/0.1, v/v/v) for LC-MS/MS analysis.

Peptides were analyzed by LC-MS/MS using a Dionex UltiMate 3000 Rapid Separation nanoLC and a linear ion trap – Orbitrap hybrid mass spectrometer (ThermoFisher Scientific). Peptide samples were loaded onto the trap column, which was 150 µm x 3 cm in-house packed with 3 µm C18 beads, at flow rate of 5 µL/min for 5 min using a loading buffer of acetonitrile/H2O/formic acid (5/94.9/0.1, v/v/v). The analytical column was a 75 µm x 10.5 cm PicoChip column packed with 1.9 µm C18 beads (New Objectives). The flow rate was kept at 300 nL/min. Solvent A was 0.1% formic acid in water and Solvent B was 0.1% formic acid in acetonitrile. The peptide was separated on a 90 min analytical gradient from 5% acetonitrile/0.1% formic acid to 40% acetonitrile/0.1% formic acid.

The mass spectrometer was operated in data-dependent mode. The source voltage was 2.10 kV and the capillary temperature was 275°C. MS1 scans were acquired from 400 to 2000 m/z at 60,000 resolving power and automatic gain control (AGC) set to 1 × 106. The top ten most abundant precursor ions in each MS1 scan were selected for fragmentation. Precursors were selected with an isolation width of 1 Da and fragmented by collision-induced dissociation (CID) at 35% normalized collision energy in the ion trap. Previously selected ions were dynamically excluded from re-selection for 60 s. The MS2 AGC was set to 3 × 105.

Proteins were identified from the MS raw files using Mascot search engine (Matrix Science). MS/MS spectra were searched against the UniprotKB database of S. intermedius B196 (UniProt and UniProt Consortium, 2015). All searches included carbamidomethyl cysteine as a fixed modification and oxidized Met, deamidated Asn and Gln, acetylated N-terminus as variable modifications. Three missed tryptic cleavages were allowed. The MS1 precursor mass tolerance was set to 10 ppm and the MS2 tolerance was set to 0.6 Da. A 1% false discovery rate cutoff was applied at the peptide level. Only proteins with a minimum of two unique peptides above the cutoff were considered for further study. MS/MS spectral counts were extracted by Scaffold 4 (Proteome Software Inc.) and used for statistical analysis of differential expression. Three biological replicates were performed and proteins identified in all three wild-type replicates were included in further analysis. After replicate averaging, low abundance proteins (less than five spectral counts in wild-type) were excluded from the final dataset.

### Secretion assay

Overnight cultures of S. intermedius strains were used to inoculate 2 ml of THYB at a ratio of 1:200. Cultures were grown statically at 37°C, 5% CO2 to mid-log phase, and cell and supernatant fractions were prepared as described previously (Hood et al., 2010).

### Antibody generation and western blot analyses

Full-length TelC protein was expressed and purified as described below (see protein expression and purification) except that PBS buffer was used instead of Tris-HCl for all stages of purification. Ten milligrams of purified TelC protein was sent to GenScript for polyclonal antisera production.

Western blot analyses of protein samples were performed using rabbit α-TelC (diluted 1:2000) or rabbit α-VSV-G (diluted 1:5000, Sigma) and detected with α-rabbit horseradish peroxidase-conjugated secondary antibodies (diluted 1:5000, Sigma). Western blots were developed using chemiluminescent substrate (SuperSignal West Pico Substrate, Thermo Scientific) and imaged with a FluorChemQ (ProteinSimple).

### Bacterial competition experiments

For intraspecific competition experiments donor and recipient strains were diluted in THYB to a starting OD600 of 0.5 and 0.05, respectively. Cell suspensions were then mixed together in a 1:1 ratio and 10 μL of the mixture was spotted on THYA and grown at 37°C, 5% CO2 for 30 hr. The starting ratio of each competition was determined by enumerating donor and recipient c.f.u. Competitions were harvested by excising the agar surrounding the spot of cell growth followed by resuspension of cells in 0.5 mL of THYB. The final donor and recipient ratio was determined by enumerating c.f.u. For all intraspecific experiments, counts of donor and recipient c.f.u. were obtained by dilution plating on THYA containing appropriate antibiotics. To facilitate c.f.u. enumeration of wild-type S. intermedius B196, a spectinomycin resistance cassette was inserted into the intergenic region between SIR_0114 and SIR_0115.

For interspecies competition experiments, donor and recipient strains were diluted in THYB to a starting OD600 of 0.75 and 0.00075, respectively. Cell suspensions were then mixed together in a 1:1 ratio and 10 μL of the mixture was spotted on THYA and grown at 37°C, 5% CO2 for 30 hr. The starting ratio of each competition was determined by enumerating donor and recipient c.f.u. Competitions were harvested by excising the agar surrounding the spot of cell growth followed by resuspension of cells in 0.5 mL of THYB. The final donor and recipient ratio was determined by enumerating c.f.u. Counts of donor and recipient c.f.u. were obtained by dilution plating on THYA containing appropriate antibiotics (S. intermedius), BHI under standard atmospheric conditions (E. coli, E. faecalis and S. pyogenes), LB under standard atmospheric conditions (P. aeruginosa and B. thailandensis) or BHIS supplemented with 60 μg/mL gentamicin under anaerobic conditions (B. fragilis).

Statistically significance was assessed for bacterial competition experiments through pairwise t-tests of competitive index values (n = 3 for each condition).

### Protein expression and purification

Stationary phase overnight cultures of E. coli BL21 pETDuet-1::telC, E. coli BL21 pETDuet-1::telC202-CT (encoding TelCtox) and E. coli BL21 pETDuet-1::tipCΔss were used to inoculate 4L of 2 x YT broth and cultures were grown to mid-log phase in a shaking incubator at 37°C. Upon reaching an OD600 of approximately 0.6, protein expression was induced by the addition of 1 mM IPTG followed by incubation at 18°C for 16 hr. Cells were harvested by centrifugation at 6000 g for 15 min, followed by resuspension in 35 mL of buffer A (50 mM Tris-HCl pH 8.0, 300 mM NaCl, 10 mM imidazole). Resuspended cells were then ruptured by sonication (3 pulses, 50 s each) and cellular debris was removed by centrifugation at 30,000 g for 45 min. Cleared cell lysates were then purified by nickel affinity chromatography using 2 mL of Ni-NTA agarose resin loaded onto a gravity flow column. Lysate was loaded onto the column and unbound proteins were removed using 50 mL of buffer A. Bound proteins were then eluted using 50 mM Tris-HCl pH 8.0, 300 mM NaCl, 400 mM imidazole. The purity of each protein sample was assessed by SDS-PAGE followed by Coomassie Brilliant Blue staining. All protein samples were dialyzed into 20 mM Tris-HCl, 150 mM NaCl.

Selenomethionine-incorporated TelC202-CT was obtained by growing E. coli BL21 pETDuet-1::telC202-CT in SelenoMethionine Medium Complete (Molecular Dimensions) using the expression conditions described above. Cell lysis and nickel affinity purification were also performed as described above except that all buffers contained 1 mM tris(2-carboxyethyl)phosphine.

### Crystallization and structure determination

Purified selenomethionine-incorporated TelC202-CT was concentrated to 12 mg/mL by spin filtration (10 kDa cutoff, Millipore) and screened against commercially available crystallization screens (MCSG screens 1–4, Microlytic). Diffraction quality crystals appeared after 4 days in a solution containing 0.1 M Sodium Acetate pH 4.6, 0.1 M CaCl2, 30% PEG400. X-ray diffraction data were collected using beamline 5.0.2 at the Advanced Light Source (ALS). A single dataset (720 images, 1.0° Δφ oscillation, 1.0 s exposure) was collected on an ADSC Q315r CCD detector with a 200 mm crystal-to-detector distance. Data were indexed and integrated using XDS (Kabsch, 2010) and scaled using AIMLESS (Evans and Murshudov, 2013) (table S2).

The structure of TelC202-CT was solved by Se-SAD using the AutoSol wizard in the Phenix GUI (Adams et al., 2010). Model building was performed using the AutoBuild wizard in the Phenix GUI. The electron density allowed for near-complete building of the model except for N-terminal residues 202–211, two C-terminal residues and an internal segment spanning residues 417–434. Minor model adjustments were made manually in COOT between iterative rounds of refinement, which was carried out using Phenix.refine (Afonine et al., 2012; Emsley et al., 2010). The progress of the refinement was monitored by the reduction of Rwork and Rfree (Table 2).

### Peptidoglycan hydrolase assay

Purified TelCtox was dialyzed against 20 mM sodium acetate pH 4.6, 150 mM NaCl, 10 mM CaCl2. Cross-linked peptidoglycan sacculi and lysostaphin endopeptidase pre-treated (non-cross-linked) sacculi from S. aureus were then incubated with 5 μM TelCtox, 2.5 μg of cellosyl muramidase or buffer at 37°C for 18 hr. Digests were then boiled for 5 min at 100°C and precipitated protein was removed by centrifugation. The resulting muropeptides were reduced by the addition of sodium borohydride and analyzed by HPLC as described previously (de Jonge et al., 1992).

For the analysis of cell walls isolated from TelC-intoxicated cells, 1L of S. aureus USA300 pEPSA5::ss-telCtox and S. aureus USA300 pEPSA5::ss-telCtoxD401A cells were grown to mid-log phase prior to induction of protein expression by the addition of 2% (w/v) xylose. 90 min post-induction, cultures were rapidly cooled in an ice-water bath and cells were harvested by centrifugation. After removal of supernatants, cell pellets were resuspended in 40 mL of ice-cold 50 mM Tris-HCl pH 7.0 and subsequently added dropwise to 120 mL boiling solutions of 5% SDS. PG was isolated as described (de Jonge et al., 1992) and digested with either cellosyl muramidase or lysostaphin endopeptidase and cellosyl, reduced with sodium borohydride and analyzed by HPLC as described above.

### Lipid II phosphatase assay

Purified TelCtox and TelCtox–TipCΔss complex were dialyzed against 20 mM sodium acetate pH 4.6, 150 mM NaCl, 10 mM CaCl2. C14-labelled Lys-type lipid II was solubilized in 5 μL of Triton X-100 before being added to 95 μL of reaction buffer containing 15 mM HEPES pH 7.5, 0.4 mM CaCl2 (excluded from the PBP1B-LpoB reaction), 150 mM NaCl, 0.023% Triton X-100 and either PBP1B–LpoB complex, TelCtox, TelCtox–TipCΔss complex or Colicin M followed by incubation for 1 hr at 37°C. The reaction with PBP1B-LpoB was boiled and reduced with sodium borohydride. All the reactions were quenched by the addition of 1% (v/v) phosphoric acid and analyzed by HPLC as described (Bertsche et al., 2005). Three biological replicates were performed for each reaction. The lipid II degradation products of TelCtox digestion were confirmed by mass spectrometry. Lipid II was kindly provided by Ute Bertsche and was generated as described previously (Bertsche et al., 2005).

For thin-layer chromatography (TLC) analysis of Lys-type lipid II degradation by TelC, TelCtox or TelCtox–TipCΔss, 40 μM lipid II was solubilized in 30 mM HEPES/KOH pH 7.5, 150 mM KCl and 0.1% Triton X-100 before adding either 2 μM TelCtox, 2 μM TelCtox–TipCΔss complex or protein buffer, followed by incubation for 90 min at 37°C. Samples were extracted with n-butanol/pyridine acetate (2:1) pH 4.2 and resolved on silica gel (HPTLC silica gel 60, Millipore) in chloroform/methanol/ammonia/water (88:48:1:10). For the undecaprenyl phosphate reactions 100 μM undecaprenyl phosphate (Larodan) was solubilized in 20 mM HEPES/KOH pH 7.5, 150 mM KCl, 1 mM CaCl2 and 0.1% Triton X-100 before adding 2 μM TelCtox (final concentration), 2 μM TelCtox–TipCΔss or protein buffer, followed by incubation for 5 hr at 25°C and 90 min at 37°C. Samples were extracted and separated by TLC as indicated above. For the undecaprenyl pyrophosphate synthesis reactions coupled to the degradation by TelCtox0.04 mM Farnesyl pyrophosphate and 0.4 mM isopentenyl pyrophosphate were solubilized in 20 mM HEPES/KOH pH 7.5, 50 mM KCl, 0.5 mM MgCl2, 1 mM CaCl2, 0.1% Triton X-100 and incubated with 10 μM UppS and 2 μM TelCtox (final concentrations) or protein buffer for 5 hr at 25°C and 90 min at 37°C. Samples were extracted and separated by TLC as indicated above.

### Yeast toxicity assay

To target TelC to the yeast secretory pathway, telCtox was fused to the gene fragment encoding the leader peptide of Kluyveromyces lactis killer toxin (Baldari et al., 1987), generating ss-telCtox. S. cerevisiae was transformed with pCM190 containing telCtox, ss-telCtox, a known toxin of yeast or empty vector and grown o/n SC-ura +1 ug/mL doxycycline. Cultures were resuspended to OD600 = 1.5 with water and serially diluted 5-fold onto SC-ura agar. Plates were incubated at 30°C for 2 days before being imaged using a Pentax WG-3 digital camera. Images presented are representative of three independent replicate experiments. Proteolytic processing of the leader peptide of ss-TelCtox was confirmed by western blot.

### Isothermal titration calorimetry

Solutions of 25 μM TelC202-CT and 250 μM TipCΔss were degassed prior to experimentation. ITC measurements were performed with a VP-ITC microcalorimeter (MicroCal Inc., Northampton, MA). Titrations consisted of 25 10 μL injections with 180 s intervals between each injection. The ITC data were analyzed using the Origin software package (version 5.0, MicroCal, Inc.) and fit using a single-site binding model.

### Bacterial two-hybrid analyses

E. coli BTH101 cells were co-transformed with plasmids encoding the T18 and T25 fragments of Bordetella pertussis adenylate cyclase fused to the proteins of interest. Stationary phase cells were then plated on LB agar containing 40 mg/mL X-gal, 0.5 mM IPTG, 50 mg/mL kanamycin and 150 mg/mL carbenicillin and grown for 24 hr at 30°C. Plates were imaged using a Pentax WG-3 digital camera. Images representative of at least three independent replicate experiments are presented.

### Immunoprecipitation assay

E. coli BL21 (DE3) pLysS cells were co-transformed with plasmids encoding TelC-his6 and WxgB-V or TelC-his6 and WxgC-V. Cells were grown to an OD600 of 0.6 prior to induction of protein expression with 0.5 mM IPTG for 6 hr at 30°C. Cultures were harvested by centrifugation and cell pellets were resuspended in Buffer A prior to lysis by sonication. Clarified lysates were then incubated with Ni-NTA resin and incubated at 4°C with rotation for 90 min. Ni-NTA resin was then washed four times with Buffer A followed by elution of bound proteins with Buffer B. After the addition of Laemmli sample buffer, proteins were separated by SDS-PAGE using an 8–16% gradient TGX Stain-Free gel (Bio-Rad). TelC-his6 was visualized by UV activation the trihalo compound present in Stain-Free gels whereas WxgB-V and WxgC-V were detected by western blotting.

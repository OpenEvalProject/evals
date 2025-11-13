# Adaptation of hydroxymethylbutenyl diphosphate reductase enables volatile isoprenoid production

## Authors

- Mareike Bongers<sup>1</sup> ([ORCID: 0000-0003-4739-3852](https://orcid.org/0000-0003-4739-3852)) †
- Jordi Perez-Gil<sup>2</sup> ([ORCID: 0000-0002-5632-9556](https://orcid.org/0000-0002-5632-9556))
- Mark P Hodson<sup>2</sup> ([ORCID: 0000-0002-5436-1886](https://orcid.org/0000-0002-5436-1886))
- Lars Schrübbers<sup>1</sup>
- Tune Wulff<sup>1</sup> ([ORCID: 0000-0002-8822-1048](https://orcid.org/0000-0002-8822-1048))
- Morten OA Sommer<sup>1</sup>
- Lars K Nielsen<sup>1</sup> ([ORCID: 0000-0001-8191-3511](https://orcid.org/0000-0001-8191-3511))
- Claudia E Vickers<sup>2</sup> ([ORCID: 0000-0002-0792-050X](https://orcid.org/0000-0002-0792-050X)) †

### Affiliations

1. Novo Nordisk Foundation Center for Biosustainability, Technical University of Denmark Lyngby Denmark
2. Australian Institute for Bioengineering and Nanotechnology, The University of Queensland Brisbane Australia
3. Centre for Research in Agricultural Genomics (CRAG) CSIC-IRTA-UAB-UB, Campus UAB Bellaterra Barcelona Spain
4. Metabolomics Australia, Australian Institute for Bioengineering and Nanotechnology, The University of Queensland Brisbane Australia
5. School of Pharmacy, The University of Queensland Brisbane Australia
6. CSIRO Synthetic Biology Future Science Platform Brisbane Australia

† Corresponding author

## Abstract

Volatile isoprenoids produced by plants are emitted in vast quantities into the atmosphere, with substantial effects on global carbon cycling. Yet, the molecular mechanisms regulating the balance between volatile and non-volatile isoprenoid production remain unknown. Isoprenoids are synthesised via sequential condensation of isopentenyl pyrophosphate (IPP) to dimethylallyl pyrophosphate (DMAPP), with volatile isoprenoids containing fewer isopentenyl subunits. The DMAPP:IPP ratio could affect the balance between volatile and non-volatile isoprenoids, but the plastidic DMAPP:IPP ratio is generally believed to be similar across different species. Here we demonstrate that the ratio of DMAPP:IPP produced by hydroxymethylbutenyl diphosphate reductase (HDR/IspH), the final step of the plastidic isoprenoid production pathway, is not fixed. Instead, this ratio varies greatly across HDRs from phylogenetically distinct plants, correlating with isoprenoid production patterns. Our findings suggest that adaptation of HDR plays a previously unrecognised role in determining in vivo carbon availability for isoprenoid emissions, directly shaping global biosphere-atmosphere interactions.

## Introduction

Biogenic volatile organic compounds (BVOCs) emitted from the biosphere have significant effects on global climate and air quality (Loreto and Fares, 2013). Short-chain isoprenoids such as isoprene, a C5 hydrocarbon, contribute more than 80% of BVOCs, totalling about 650 million tonnes of carbon per year (Sindelarova et al., 2014). The vast quantity and high reactivity of emitted volatile isoprenoids affect the oxidative capacity of the troposphere (Thompson, 1992; Wennberg et al., 2018), impact the residence time of the greenhouse gas methane (Fehsenfeld et al., 1992), and contribute to air pollution through formation of secondary organic aerosols, surface-level ozone and carbon monoxide (Claeys et al., 2004; Poisson et al., 2000; Granier et al., 2000; Figure 1). The effects of isoprenoid emissions may be exacerbated by climate change and shifts in land use (Peñuelas and Staudt, 2010), warranting a better understanding of how plants accomplish and regulate these vast emissions.

![Figure 1.](https://cdn.elifesciences.org/articles/48685/elife-48685-fig1-v1.jpg)

**Figure 1.:** The MEP pathway makes IPP and DMAPP simultaneously through the action of HDR (pink box), and produces the bulk of volatile isoprenoids, contributing >80 % of total BVOCs (Sindelarova et al., 2014) . Non-volatile isoprenoids are essential and synthesised by all organisms, while volatile isoprenoid production is non-essential and highly species-dependent. The cytosolic MVA pathway contributes most sesquiterpenes (<3 % of BVOCs), but is omitted here for clarity. Emitted volatile isoprenoids are rapidly oxidised, resulting in complex atmospheric photochemistry impacting aerosol and cloud condensation nuclei formation, extension of methane residence time, ozonolysis as well as surface-level ozone formation in the presence of mono-nitrogen oxide (NOx) pollutants (Wennberg et al., 2018). BVOCs, biogenic organic volatile compounds; DMAPP, dimethylallyl pyrophosphate; DXS, deoxyxylulose synthase; IDI, isopentenyl diphosphate isomerase; IPP, isopentenyl pyrophosphate; IspS, isoprene synthase; HDR, hydroxymethylbutenyl diphosphate reductase.

All isoprenoids are made from the C5 isomers isopentenyl pyrophosphate (IPP) and dimethylallyl pyrophosphate (DMAPP) (Figure 1). Two non-homologous metabolic pathways produce DMAPP and IPP in plants: the cytosolic mevalonic acid (MVA) and the plastidic methylerythritol phosphate (MEP) pathways, the latter contributing almost all volatile isoprenoids (Pulido et al., 2012). The final step of the MEP pathway is catalyzed by the enzyme hydroxymethylbutenyl diphosphate reductase (HDR/IspH), which produces both IPP and DMAPP (Figure 1). Isoprenoid chain length is initially determined by how many units of IPP are condensed with one molecule of DMAPP, before terpene synthases and other modifying enzymes convert these intermediates into isoprenoids. The resulting compounds are classified by carbon chain length.

In plants, longer-chain isoprenoids (C15 and higher) serve many essential roles, e.g. as membrane components and parts of the photosynthetic apparatus (Pulido et al., 2012; Figure 1). Short-chain isoprenoids (C5, C10, and some C15 compounds) are volatile under physiological conditions, and their functions are generally not essential for plant survival (Vickers et al., 2009). It is currently unknown how plants control carbon allocation between short-chain and long-chain isoprenoids in the chloroplast. While the demand for essential isoprenoids (for example, photosynthetic pigments) is assumed to be relatively similar across plants (Monson et al., 2013), different species produce markedly different amounts of non-essential, short-chain volatile isoprenoids (Wiedinmyer et al., 2020). For example, some oak (Quercus) species produce vast amounts of isoprene, while closely related oaks produce little or none at all (Wiedinmyer et al., 2020). Synthesis of isoprenoids with different chain lengths requires different DMAPP:IPP substrate ratios. Much more IPP than DMAPP is needed for long-chain isoprenoid production, so presumably high relative IPP concentrations are necessary for chain elongation while an excess of DMAPP and insufficient IPP could favour short-chain isoprenoid production. Isoprene synthase (IspS) uses only DMAPP, but not IPP, as a substrate.

Volatile isoprenoid emissions can represent a significant loss of carbon; for example, up to 20% of recently fixed carbon can be emitted as isoprene in high-emitting plants (Sharkey and Loreto, 1993). Isoprene synthase (IspS) has a high Km for its substrate DMAPP (0.5–8 mM; BRENDA, 2020); despite this, it successfully competes with prenyl phosphate synthases, which typically have KM(DMAPP) values 10- to 100-fold lower (BRENDA, 2020). Similarly, monoterpene synthases, which also show lower affinity for the substrates (BRENDA, 2020), compete with downstream prenyl phosphate synthases. Hence, the relative abundance of DMAPP may determine the balance between volatile and non-volatile isoprenoids.

Here we examined HDR as a potential mechanism to provide variability in the DMAPP:IPP ratio. Previous studies in diverse organisms (Escherichia coli, the bacterium Aquifex aeolicus, red pepper chromoplasts, and cultured tobacco cells) all found that HDR produces DMAPP:IPP ratios between 1:4 and 1:6 (Rohdich et al., 2003; Altincicek et al., 2002; Adam et al., 2002; Tritsch et al., 2010). Consequently, it has been assumed that HDR has a fixed product ratio of about 1:5. However, none of these species produce significant amounts of volatile isoprenoids (Wiedinmyer et al., 2020). Isopentenyl diphosphate isomerase (IDI) interconverts DMAPP and IPP, but the reaction is slow (Jonnalagadda et al., 2012) and IDI is rate-limiting for isoprenoid production generally, including isoprene (Vickers et al., 2014). We hypothesised that HDR enzymes from species that emit large amounts of short-chain volatile isoprenoids produce a higher ratio of DMAPP to IPP, which could support production of volatiles like isoprene.

## Results and discussion

We selected HDR genes from the bacterium E. coli, Synechococcus sp. strain PCC 7002 (a photosynthetic prokaryote) and eight species from diverse taxa of the plant kingdom (Table 1). Many plants harbour more than one annotated HDR gene, some of which may be pseudogenes. Therefore, we first identified functional HDR genes by their ability to complement an otherwise lethal knockout of the ispH/HDR gene in E. coli (Altincicek et al., 2001). We found at least one functional gene from each species (Figure 2—figure supplement 1a); however, severe dose-dependent growth defects were observed when overexpressing certain HDR genes, possibly due to toxicity of prenyl phosphates (George et al., 2018; Figure 2—figure supplement 1b). This precluded accurate steady-state metabolite quantification and required alleviating toxicity by the introduction of a metabolic sink for IPP and DMAPP. Here we used a lycopene (C40 isoprenoid) biosynthetic pathway, including expression of a heterologous idi (Cunningham et al., 1994). Deoxyxylulose synthase (DXS), the primary rate-limiting step of the MEP pathway, was also overexpressed in order to achieve intracellular IPP and DMAPP concentrations above quantification limits in E. coli.

**Table 1.**
 Genetic information and volatile isoprenoid emission profiles for species studied in this work.Key: blank cell indicates species has not been tested, or genome sequence (or other information) not available; Y indicates significant emissions of isoprene or isoprenoids have been detected, or gene/transcript has been identified; N indicates significant emissions of isoprene or isoprenoids have NOT been detected, or gene/transcript has NOT been identified; MTs, monoterpenes; IspS, isoprene synthase; TPS, terpene synthase.


<table>
  <thead>
    <tr>
      <th colspan="9"></th>
      <th colspan="2">Emissions</th>
      <th colspan="2">Gene/transcript*</th>
      <th></th>
    </tr>
    <tr>
      <th>Kingdom</th>
      <th>Phylum/Clade</th>
      <th>Clade</th>
      <th>Genus, species</th>
      <th>Common Name</th>
      <th></th>
      <th>HDR protein accession number</th>
      <th>E. coli construct Genbank ID</th>
      <th>Complements?†</th>
      <th>Isoprene (C5)</th>
      <th>MTs (C10)</th>
      <th>IspS</th>
      <th>Short chain TPS</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Plantae</td>
      <td>Angiosperms</td>
      <td>Eudicots</td>
      <td>Ricinus communis</td>
      <td>castor bean plant</td>
      <td></td>
      <td>XP_002519102.1</td>
      <td>MH605331</td>
      <td>yes</td>
      <td>N</td>
      <td>Y</td>
      <td>N</td>
      <td>Y</td>
      <td>Wiedinmyer et al., 2020; Kadri et al., 2011; Xie et al., 2012)</td>
    </tr>
    <tr>
      <td rowspan="2">Plantae</td>
      <td rowspan="2">Angiosperms</td>
      <td rowspan="2">Eudicots</td>
      <td rowspan="2">Populus trichocarpa‡</td>
      <td rowspan="2">black cottonwood</td>
      <td>1</td>
      <td>ACD70402</td>
      <td>MH605329</td>
      <td>yes</td>
      <td rowspan="2">Y</td>
      <td rowspan="2">Y</td>
      <td>Y</td>
      <td rowspan="2">Y</td>
      <td>Wiedinmyer et al., 2020; Tuskan, 2006)</td>
    </tr>
    <tr>
      <td>2</td>
      <td>PNT41333.1</td>
      <td>MH605330</td>
      <td>no</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Plantae</td>
      <td>Angiosperms</td>
      <td>Eudicots</td>
      <td>Prunus persica</td>
      <td>peach</td>
      <td></td>
      <td>XP_007199828.1</td>
      <td>MH605326</td>
      <td>yes</td>
      <td>N</td>
      <td>Y</td>
      <td>N</td>
      <td>Y</td>
      <td>Wiedinmyer et al., 2020; Verde et al., 2013)</td>
    </tr>
    <tr>
      <td rowspan="2">Plantae</td>
      <td rowspan="2">Angiosperms</td>
      <td rowspan="2">Eudicots</td>
      <td rowspan="2">Eucalyptus grandis</td>
      <td rowspan="2">flooded gum</td>
      <td>1</td>
      <td>XP_010028563.1</td>
      <td>MH605323</td>
      <td>yes</td>
      <td rowspan="2">Y</td>
      <td rowspan="2">Y</td>
      <td rowspan="2">Y</td>
      <td rowspan="2">Y</td>
      <td rowspan="2">Wiedinmyer et al., 2020; Myburg et al., 2014</td>
    </tr>
    <tr>
      <td>2</td>
      <td>XP_010047332.1</td>
      <td>MH605324</td>
      <td>no</td>
    </tr>
    <tr>
      <td>Plantae</td>
      <td>Angiosperms</td>
      <td>Eudicots</td>
      <td>Theobroma cacao</td>
      <td>cacao tree</td>
      <td></td>
      <td>XP_007042717.1</td>
      <td>MH605333</td>
      <td>yes</td>
      <td>N</td>
      <td>Y</td>
      <td>N</td>
      <td>Y</td>
      <td>Wiedinmyer et al., 2020; Argout et al., 2008</td>
    </tr>
    <tr>
      <td>Plantae</td>
      <td>Angiosperms</td>
      <td>Eudicots</td>
      <td>Arabidopsis thaliana</td>
      <td>thale cress</td>
      <td></td>
      <td>AEE86362.1</td>
      <td>MH605322</td>
      <td>yes</td>
      <td>N</td>
      <td>Y</td>
      <td>N</td>
      <td>Y</td>
      <td>Sharkey et al., 2005; Chen et al., 2004; Bohlmann et al., 2000</td>
    </tr>
    <tr>
      <td>Plantae</td>
      <td>Angiosperms</td>
      <td>Monocots</td>
      <td>Elaeis guineensis</td>
      <td>oil palm</td>
      <td></td>
      <td>XP_010909277.1</td>
      <td>MH605325</td>
      <td>yes</td>
      <td>Y</td>
      <td></td>
      <td></td>
      <td>Y</td>
      <td>Wiedinmyer et al., 2020; Wilkinson et al., 2006</td>
    </tr>
    <tr>
      <td rowspan="2">Plantae</td>
      <td rowspan="2">Gymnosperms</td>
      <td rowspan="2">Pinophyta</td>
      <td rowspan="2">Picea sitchensis</td>
      <td rowspan="2">Sitka spruce</td>
      <td>1</td>
      <td>ACN40284.1</td>
      <td>MH605327</td>
      <td>yes</td>
      <td rowspan="2">Y</td>
      <td rowspan="2">Y</td>
      <td rowspan="2"></td>
      <td rowspan="2">Y</td>
      <td rowspan="2">Wiedinmyer et al., 2020; Hayward et al., 2004</td>
    </tr>
    <tr>
      <td>2</td>
      <td>ACN39959.1</td>
      <td>MH605328</td>
      <td>yes – toxic</td>
    </tr>
    <tr>
      <td>Bacteria</td>
      <td>Cyanobacteria</td>
      <td></td>
      <td>Synechococcus sp. PCC 7002</td>
      <td>Synechococcus</td>
      <td></td>
      <td>ACA98524.1</td>
      <td>MH605332</td>
      <td>yes</td>
      <td>N</td>
      <td></td>
      <td>N</td>
      <td>N</td>
      <td></td>
    </tr>
  </tbody>
</table>

_* Identified from data/genomes available on NCBI (https://www.ncbi.nlm.nih.gov/) and literature search (references noted).† Whether protein expression was able to functionally complement an E. coli ΔispH knockout in this study.‡ Also known as Populus balsamifera ssp. trichocarpa._

A spectrum of DMAPP:IPP ratios was observed, ranging from almost exclusive IPP production (Picea sitchensis HDR1) to almost exclusive DMAPP production (Populus trichocarpa and Ricinus communis, Figure 2a). A control without HDR overexpression (labelled (-) in Figure 2a) showed a DMAPP:IPP ratio of ~1.5 to 1 in our experimental setup, serving as a reference point. Overexpressing the E. coli HDR shifted the ratio slightly towards IPP, in agreement with previous reports (Rohdich et al., 2002). However, HDR enzymes from species known to emit volatile isoprenoids produced considerably more DMAPP - a noteworthy exception being P. sitchensis HDR1 (PsHDR1, Figure 2a).

![Figure 2.](https://cdn.elifesciences.org/articles/48685/elife-48685-fig2-v1.jpg)

**Figure 2.:** (a) In vivo ratio of DMAPP:IPP measured via LC-MS/MS in E. coli overexpressing HDR genes from different species, in the genetic context of dxs and lycopene biosynthetic pathway overexpression. Filled circles and squares indicate that the HDR source species natively emits C5 or C10 isoprenoids. Open symbols indicate no emission, and no symbol indicates no data or conflicting data. (b) Isoprene production in E. coli when the HDR enzymes shown in panel (a) are overexpressed with dxs and an isoprene synthase. (c) Comparison of DMAPP:IPP ratios between selected HDRs co-expressed with dxs and with expression of either lycopene or isoprene as the metabolic sink. (d) Comparison of DMAPP:IPP ratios in E. coli overexpressing Picea sitchensis (Ps) HDR1 or HDR2 in the context of dxs and lycopene biosynthetic pathway overexpression. (e) Isoprene production in E. coli overexpressing P. sitchensis HDR1 or HDR2 along with dxs and an isoprene synthase. (f) The maximum specific growth rate (µmax) of E. coli expressing selected HDRs in the context of dxs and lycopene biosynthetic pathway overexpression, with or without induction of HDR expression by addition of IPTG. All data shown as mean ± SD from > 3 biological replicates; (-) indicates the control strain without HDR overexpression.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/48685/elife-48685-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (a) An E. coli strain with a ∆ispH knockout and a heterologously expressed lower mevalonate (MVA) pathway depends on mevalonate for survival. When a functional ispH/HDR gene is expressed from a plasmid, growth can be restored in the absence of mevalonate. (-), empty vector negative control; (+), plasmid expressing E. coli ispH as a positive control. E. grandis HDR2 and P. trichocarpa HDR2 did not complement the ∆ispH knockout. MVA, mevalonate. (b) Toxicity of P. sitchensis HDR2 in E. coli ∆ispH. Plasmid-encoded HDR genes are expressed from the trc promoter which can be induced with IPTG or partially repressed with glucose. P. sitchensis HDR2-associated toxicity can be alleviated by adding glucose to repress HDR expression, and is strongest under full IPTG induction. Arabinose, which induces the genomically encoded lower MVA pathway, including a heterologous idi gene, partly alleviates IPTG-induced toxicity. (-), empty vector negative control; (+), plasmid expressing E. coli HDR as a positive control. IPTG, Isopropyl β-D-1-thiogalactopyranoside; MVA, mevalonate.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/48685/elife-48685-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Relative protein abundance in E. coli overexpressing HDR genes from different species, in the genetic context of dxs and lycopene biosynthetic pathway overexpression. Proteins were quantified using untargeted proteomics via LC-MS/MS, and data represent the three most abundant peptide counts from each protein, normalized across all samples. (a) E. coli native Idi shows no significant difference between strains (one-way ANOVA, p = 0.536). (b) E. coli native HDR quantification. Only the EcHDR overexpression strain is significantly different to the ‘no HDR overexpression’ (-) control (Welch’s one-way ANOVA, p = 0.0048), no significant difference were observed between the other strains (p ≥ 0.743). (c) Overexpressed, heterologous HDR proteins. Comparison of protein abundance between different HDR proteins is not possible due to a lack of shared tryptic peptides across all HDRs. Unique peptides for all overexpressed HDR proteins were detected with high abundance in the respective strains. (d) Plasmid-encoded lycopene biosynthetic pathway proteins. No significant differences were detected across strains for CrtI and CrtB (ordinary or Welch’s ANOVA, respectively, p ≥ 0.05). For Idi and CrtE, differences with p < 0.05 were detected between selected strains (e.g. E. grandis vs. R. communis CrtE p = 0.034); however, no significant differences were observed when comparing any of the strains to the negative control (p ≥ 0.78 for Idi, Welch’s one-way ANOVA; p ≥ 0.46 for CrtE, ordinary one-way ANOVA). For Idi and CrtE, a total of only 3 peptides each were detected in our proteomics analysis, indicating low protein abundance and potentially explaining the higher variability between strains. Data represent means +/- SD from n ≥ 3. All p-values were corrected for multiple hypothesis testing using Dunnett’s method.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/48685/elife-48685-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** (a) Absolute quantification of intracellular DMAPP and IPP in E. coli overexpressing HDR genes from different species, in the genetic context of dxs and lycopene biosynthetic pathway overexpression. The difference in product ratio between HDRs at opposite ends of the graph is driven by both an increase in DMAPP and a decrease in IPP concentration. Data represent means +/- SD from n ≥ 3. (b) Representative chromatograms of matrix-matched calibration standards for DMAPP and IPP, including mevalonate-5-phosphate as internal standard (IS). Due to a slow, consistent drift in retention time over the HPLC column lifetime, no fixed retention times are given for DMAPP and IPP; however, with the presented method the analytes remain baseline-separated as shown here.

These values do not represent direct product ratios of the examined HDRs due to the presence of the heterologously expressed lycopene pathway and idi. However, they show that product ratios vary up to 40-fold between HDRs, and that the assumed fixed 1:5 DMAPP to IPP ratio is in fact an exception, rather than the rule. Using LC-MS proteomics, we tested whether the observed phenotypes were influenced by differences in expression of the native E. coli HDR, IDI, or the plasmid-encoded lycopene production pathway. We found no difference in protein levels in any of the HDR overexpression strains compared to the no HDR overexpression control (one-way ANOVA, p>0.05), except for the anticipated increase in E. coli HDR in the respective overexpression strain (Welch’s ANOVA, Dunnett’s post hoc test p<0.005; Figure 2—figure supplement 2). Because no shared proteotypic peptides exist across all heterologous HDRs, quantitative comparison of HDR protein levels across strains is not possible. However, we confirmed that all tested HDRs were strongly overexpressed (Figure 2—figure supplement 2c), and that there was no correlation between HDR abundance and the DMAPP:IPP ratio (rho = −0.488, data not shown). Taken together, these data demonstrate that different HDR enzymes produce vastly different DMAPP:IPP ratios, with some plant HDRs producing a ratio significantly shifted towards more DMAPP than previously recognized.

To test whether an increased in vivo DMAPP:IPP ratio would favour isoprene production, we replaced the lycopene pathway with an overexpressed isoprene synthase (IspS) as a metabolic sink. A high DMAPP:IPP ratio was indeed closely associated with isoprene production (Figure 2b). To confirm that differences in DMAPP:IPP ratios are robust when changing from lycopene (C40) to isoprene (C5) production, we compared selected HDR product ratios with both downstream metabolic sinks (Figure 2c). While the absolute values shifted towards DMAPP (left y-axis; lycopene requires 6 IPP and 2 DMAPP) or IPP (right y-axis; isoprene is made only from DMAPP) depending on downstream requirements, the relative difference between HDRs remained similar, demonstrating that our experimental setup captures representative differences between the enzymes.

Isoprene was not produced in the presence of Theobroma cacao, Arabidopsis thalianaor E. coli HDR (all species that do not emit short-chain isoprenoids), presumably because the available DMAPP was insufficient for IspS to compete with downstream enzymes (Figure 2b). All HDRs from isoprenoid-emitting species enabled isoprene production, supporting our hypothesis. Interestingly, a high DMAPP:IPP ratio and high isoprene production was also observed with HDRs from P. persica and R. communis, species that emit some monoterpenes but not isoprene (Wiedinmyer et al., 2020; Kadri et al., 2011). PpHDR and RcHDR have high (>87%) sequence identity with HDR proteins from high isoprene-emitting species P. trichocarpa and Hevea brasiliensis, respectively (Figure 3), but R. communis and P. persica do not have an isoprene synthase (Table 1).

![Figure 3.](https://cdn.elifesciences.org/articles/48685/elife-48685-fig3-v1.jpg)

**Figure 3.:** Where known, each species’ C5 (isoprene) and C10 (monoterpenes) emission spectra are shown (Wiedinmyer et al., 2020). High DMAPP-producing HDR proteins (from P. trichocarpa, R. communis and P. persica) cluster together based on high sequence similarity. Homologues within species, such as P. trichocarpa, tend to be highly similar; except for in gymnosperms where two separate groups of likely paralogous HDRs exist. Proteins analysed in this study are highlighted in bold. The Asterids clade is collapsed for clarity. Tree generated from BLAST sequence alignment with A. thaliana HDR against all land plants, using maximum likelihood phylogeny. Empty symbol, no volatile emission; filled symbol, volatile emission; no symbol, no or conflicting data available.

Together, these data suggest that HDR from different plant species has adapted to produce differing ratios of DMAPP to IPP, and that an increased DMAPP:IPP ratio is an important prerequisite for production of isoprene and perhaps other non-essential, short-chain isoprenoids. Our data indicate that a high DMAPP:IPP ratio is a necessary, but not a sufficient requirement for volatile isoprenoid emission. This places HDR at a key junction in the evolution of isoprene emission, a trait that appeared and disappeared several times across the plant kingdom (Dani et al., 2014).

Picea sitchensis (Sitka spruce) is a coniferous gymnosperm that emits both isoprene and monoterpenes (Hayward et al., 2004), but contrary to our expectation PsHDR1 produced the highest relative amount of IPP and showed very low isoprene production in E. coli (Figure 2a and b). Recently, the HDR from another gymnosperm, Ginkgo biloba (GbHDR1), was shown to produce an even lower DMAPP to IPP ratio in vitro (Shin et al., 2017). Most sequenced gymnosperms have two or more HDR isoforms which fall into two distinct classes based on sequence similarity (Kim et al., 2008; Figure 3). Interestingly, transcriptional studies (Celedon et al., 2017; Kim et al., 2009) suggest that gymnosperm Type II HDRs are particularly abundant at the site of monoterpene-rich resin formation and are generally expressed at higher levels than Type I HDRs (Celedon et al., 2017) (such as PsHDR1 and GbHDR1). It was therefore tempting to speculate that HDR adaptation in gymnosperms has resulted in paralogues with complementary functions: Type I HDRs, which primarily produce IPP, show basal expression throughout the plant, and are important for long-chain isoprenoid production; and Type II HDRs, which primarily produce DMAPP and are expressed where short-chain isoprenoids are made. This prompted us to investigate the Type II HDR from P. sitchensis (Figure 2d–f).

PsHDR2 failed in our initial complementation assay (data not shown), most likely due to toxicity as no metabolic sink was present for IPP/DMAPP. Indeed, even in the presence of a sink, overexpression of PsHDR2 reduced E. coli growth rate by about 50% (Figure 2f), a level of toxicity exceeding that of other high DMAPP-producing HDRs. Interestingly, PsHDR2 produced a > 10 fold excess of DMAPP over IPP, while PsHDR1 had a ratio shifted towards more IPP (DMAPP:IPP = 0.447 +/- 0.19; Figure 2d). PsHDR2 also enabled higher isoprene production than PsHDR1 (Figure 2e), albeit at a lower yield than the other high DMAPP-producing enzymes, which is most likely an effect of the high toxicity in E. coli. The complementary product ratios of PsHDR1 and PsHDR2 strongly suggest functional specialization of these genes, making them paralogues in P. sitchensis.

While many plants encode more than one HDR gene (Figure 3), these homologues are often closely related and thus likely arose from relatively recent large-scale genome duplications (Saladié et al., 2014). In gymnosperms, the two HDR homologues are phylogenetically more distant (Figure 3) and likely define functionally specialised paralogues. Hence, we propose that two different strategies might have been employed to adapt HDR to isoprenoid production spectra: either using a single HDR and shifting the DMAPP:IPP ratio to allow production of specific isoprenoid profiles (Figure 2a), or having two functionally distinct HDRs each dedicated to the synthesis of one isomer (Figure 2d). Whether adaptation of HDR is a result of a change in the demand for DMAPP, or whether it is a driver of its release as isoprene and other volatile isoprenoids, is a fascinating question that remains to be answered.

The discovery of HDR enzymes with different product ratios has important implications for heterologous production of industrially valuable isoprenoids such as biofuels, fragrances and pharmaceuticals (Vickers, 2015) in engineered microorganisms. We have shown that only certain HDR enzymes enable production of isoprene in our engineered E. coli, and our data indicate that the choice of HDR is important to ensure availability of DMAPP and IPP at appropriate relative concentrations to achieve balanced pathway flux towards the product of interest and to avoid DMAPP toxicity. The presented LC-MS/MS method for separation and absolute quantification of the two isomers (Figure 2—figure supplement 3) proved crucial for our discovery, and will enable a deeper understanding of the processes regulating isoprenoid biosynthesis in nature and biotechnology.

Demands from downstream metabolism may determine IPP and DMAPP requirements, and could form an evolutionary driver for enzymatic activities that impact their ratio. Our data suggest that the adaptation of HDR to generate different DMAPP:IPP ratios allows for the production of large amounts of short-chain isoprenoids in certain species or tissues. Our findings illuminate the molecular mechanism underlying how plants emit isoprene and suggest a central role for HDR in determining the spectrum of isoprenoids produced by plants, including isoprenoid BVOCs. Unravelling the mechanism by which plants distribute carbon between volatile and non-volatile isoprenoids will help resolve the complex interplay between BVOC emissions, land-use management and climate change.

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
      <td>Gene (Escherichia coli)</td>
      <td>ispH/HDR</td>
      <td>NCBI ‘Gene’</td>
      <td>Gene_ID:944777; EcoGene:EG11081; ECK0030; lytB</td>
      <td>hydroxymethylbutenyl diphosphate reductase</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>Escherichia coli W</td>
      <td>ATCC</td>
      <td>ATCC:9637</td>
      <td>obtained from L. Nielsen lab, Australia</td>
    </tr>
    <tr>
      <td>Genetic reagent (Escherichia coli)</td>
      <td>E. coli W∆cscR, lacZ::PtDXS, arsB::PaISPS</td>
      <td>This paper and PMID: 21782859 (Arifin et al., 2011)</td>
      <td></td>
      <td>knockout of cscR, knock-in of PtDXS and PaISPS</td>
    </tr>
    <tr>
      <td>Genetic reagent (Escherichia coli)</td>
      <td>E. coli WΔcscR, lacZ::MVA, ∆ispH</td>
      <td>This paper and PMID: 11115399 (Campos et al., 2001)</td>
      <td></td>
      <td>knock-in of MVA pathway, knockout of ispH</td>
    </tr>
    <tr>
      <td>Genetic reagent (Populus trichocarpa)</td>
      <td>DXS</td>
      <td>NCBI ‘Reference Sequence’</td>
      <td>XP_006378082.1</td>
      <td>Deoxyxylulose phosphate synthase, gene was truncated for expression in E. coli</td>
    </tr>
    <tr>
      <td>Genetic reagent (Populus alba)</td>
      <td>ISPS(del2-52,A3T,L70R,S288C)</td>
      <td>Patent WO2012058494 (Beck et al., 2011)</td>
      <td></td>
      <td>Isoprene synthase (Genbank:EF638224) variant, truncated and mutated</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLacZ-KIKO(cm) plasmid</td>
      <td>PMID: 23799955 (Sabri et al., 2013)</td>
      <td>Addgene:46764</td>
      <td>used to integrate PtDXS into the genome</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pArsBKIKO(cm) plasmid</td>
      <td>PMID: 23799955 (Sabri et al., 2013)</td>
      <td>Addgene:46763</td>
      <td>used to integrate PaISPS into the genome</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pT-HDR plasmids</td>
      <td>This paper</td>
      <td>derived from pTrc99a</td>
      <td>all HDR genes were cloned into this expression vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pAC-LYC04</td>
      <td>PMID: 7919981 (Cunningham et al., 1994)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Ricinus communis HDR expression plasmid</td>
      <td>Genbank</td>
      <td>MH605331</td>
      <td>HDR protein XP_002519102.1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Populus trichocarpa HDR 1 expression plasmid</td>
      <td>Genbank</td>
      <td>MH605329</td>
      <td>HDR protein ACD70402</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Populus trichocarpa HDR 2 expression plasmid</td>
      <td>Genbank</td>
      <td>MH605330</td>
      <td>HDR protein PNT41333.1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Prunus persica HDR expression plasmid</td>
      <td>Genbank</td>
      <td>MH605326</td>
      <td>HDR protein XP_007199828.1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Eucalyptus grandis HDR 1 expression plasmid</td>
      <td>Genbank</td>
      <td>MH605323</td>
      <td>HDR protein XP_010028563.1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Eucalyptus grandis HDR 2 expression plasmid</td>
      <td>Genbank</td>
      <td>MH605324</td>
      <td>HDR protein XP_010047332.1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Theobroma cacao HDR expression plasmid</td>
      <td>Genbank</td>
      <td>MH605333</td>
      <td>HDR protein XP_007042717.1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Arabidopsis thaliana HDR expression plasmid</td>
      <td>Genbank</td>
      <td>MH605322</td>
      <td>HDR protein AEE86362.1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Elaeis guineensis HDR expression plasmid</td>
      <td>Genbank</td>
      <td>MH605325</td>
      <td>HDR protein XP_010909277.1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Picea sitchensis HDR 1 expression plasmid</td>
      <td>Genbank</td>
      <td>MH605327</td>
      <td>HDR protein ACN40284.1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Picea sitchensis HDR 2 expression plasmid</td>
      <td>Genbank</td>
      <td>MH605328</td>
      <td>HDR protein ACN39959.1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Synechococcus sp. PCC 7002 HDR expression plasmid</td>
      <td>Genbank</td>
      <td>MH605332</td>
      <td>HDR protein ACA98524.1</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Astec Cyclobond I2000 chiral HPLC column</td>
      <td>Sigma Aldrich</td>
      <td>20024AST</td>
      <td>HPLC column used for IPP/DMAPP separation</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Isoprene</td>
      <td>Sigma Aldrich</td>
      <td>Cat. # I19551</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Isopentenyl pyrophosphate</td>
      <td>Sigma Aldrich</td>
      <td>Cat. # I0503</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Dimethylallyl pyrophosphate</td>
      <td>Sigma Aldrich</td>
      <td>Cat. # D4287</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>(±)-Mevalonic acid 5-phosphate</td>
      <td>Sigma Aldrich</td>
      <td>Cat. # 79849</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Mevalonolactone</td>
      <td>Sigma Aldrich</td>
      <td>Cat. # M4667</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CLC Main Workbench</td>
      <td>Qiagen</td>
      <td>RRID:SCR_000354</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>iTOL</td>
      <td>PMID: 27095192 (Letunic and Bork, 2016)</td>
      <td>https://itol.embl.de/</td>
      <td>Interactive Tree of Life</td>
    </tr>
  </tbody>
</table>

### Chemicals and reagents

Isoprene (Cat. No I19551), IPP (Ca. No I0503), DMAPP (Ca. No D4287), Isopropyl β-D-thiogalactoside (IPTG, Cat. No I6758), (±)-Mevalonic acid 5-phosphate (MVA-P, Ca. No 79849) were purchased from Sigma Aldrich. Mevalonate (MVA) was prepared from (±)-mevalonolactone (Sigma Aldrich, Cat. No M4667) through base-catalyzed hydrolysis (Campos et al., 2001). Ammonium acetate was purchased from Sigma Aldrich (Ca. No 73594–25 G-F). Acetonitrile hypergrade for LC-MS LiChrosolv (Ca. No 1000292500) and Methanol hypergrade for LC-MS LiChrosolv (Ca. No 1060352500) was purchased from Merck Millipore. Milli-Q water was generated via a Merck Millipore Integral 3 water purification system.

### Gene, plasmid and E. coli strain construction

E. coli Top10 (Cat. No C404050, Thermo Fischer Scientific) was used for cloning. For all other experiments, E. coli W (ATCC 9637) with a knock-out in the csc operon (E. coli W∆cscR Arifin et al., 2011) was used. Plant HDR chloroplast targeting peptides were predicted using the ChloroP 1.1 server (http://www.cbs.dtu.dk/services/ChloroP/). Genes were truncated to remove chloroplast targeting peptides, codon-optimised for E. coli (http://idtdna.com/CodonOpt) and synthesised by Integrated DNA Technologies (Singapore). All plant genes were placed under control of the IPTG-inducible trc promoter in a pTrc99-derived (Amann et al., 1988) vector, generating the pT-HDR series of plasmids. The DXS gene from Populus trichocarpa (Genbank Accession No. XP_006378082.1) was integrated into the genome using the pLacZ-KIKO(cm) vector (Sabri et al., 2013). The chloramphenicol resistance gene was removed from the genome using pCP20 (Datsenko and Wanner, 2000). The resulting strain (E. coli W∆cscR, lacZ::PtDXS) was transformed with each of the pT-HDR plasmids and pAC-LYC04 (Cunningham et al., 1994) for IPP and DMAPP measurements. For isoprene production experiments, an engineered ISPS gene from Populus alba (Genbank Accession No. EF638224) was integrated into the genome of E. coli W∆cscR, lacZ::PtDXS using pArsBKIKO(cm). Apart from removal of the chloroplast-targeting sequence, this gene was also engineered to contain three mutations to enhance specific activity: ISPS(del2-52,A3T,L70R,S288C) (Beck et al., 2011).

### Bacterial growth media

LB medium contained 10 g/L tryptone, 5 g/L yeast extract and 10 g/L NaCl. TB medium contained 12 g/L tryptone, 24 g/L yeast extract, 0.4% (v/v) glycerol, 2 mM MgSO4, 1 mM thiamine, 17 mM KH2PO4, 7.2 mM K2HPO4. Where indicated, media were supplemented with 1 mM mevalonate and 1 mM L-arabinose for induction of the MVA pathway operon, or with 0.2% (w/v) glucose or 0.1 mM IPTG for repression or induction of the trc promoter. All cultures were grown at 37°C with 250 rpm shaking unless stated otherwise.

### Complementation of the ispH/HDR knockout mutant in E. coli

A partial MVA pathway under control of the arabinose-inducible PBAD promoter (Campos et al., 2001) was cloned into a pLacZ-KIKO(cm) vector and integrated into the E. coli WΔcscR genome. This strain (WΔcscR, lacZ::MVA) was used to knock out ispH using recombineering (Datsenko and Wanner, 2000), making growth dependent on supplementation with mevalonate and arabinose. Each pT-HDR plasmid was transformed into this strain and tested for its ability to grow in the absence of mevalonate and arabinose.

### Growth rate measurements

Cells were grown in LB medium; glucose, mevalonate or IPTG were added where indicated. Precultures were grown at 37°C with 250 rpm shaking in 96-well plates (Corning, Cat No. CLS3799) until stationary phase. Cultures were diluted to a starting optical density (OD600) of 0.05 and the growth was monitored in a microplate reader (BioTek ELx808) at 37°C with 700 rpm double-orbital shaking, measuring OD600 every 10 min. All bacterial cultures for quantification of specific growth rates, metabolites and isoprene were grown at least in biological triplicates (from 3 single colonies of the same strain), and means +/- standard deviations are shown.

### Fermentations for metabolite measurements

Strains harbouring the different pT-HDR plasmids and pAC-LYC04 were grown for determination of IPP and DMAPP concentrations. Chloramphenicol (30 mg L−1) and ampicillin (250 mg L−1) were added to the media for plasmid maintenance. Precultures were grown in LB medium as described above. A culture volume of 10 ml of TB medium was inoculated with an overnight preculture in 100 ml baffled flasks to a starting OD600 of 0.05. Protein expression was induced with 0.1 mM IPTG at an OD600 of 0.5. When an OD600 of 5 was reached (exponential growth phase in TB medium), cultures were harvested for metabolite quantification.

### Quantification of IPP and DMAPP

Intracellular metabolites were quenched and extracted using a method adapted from Bongers et al. (2015). To harvest, the equivalent of 1 ml of culture of an optical density of OD600 = 5 was centrifuged at 4°C for 20 s at 13,000 x g, the supernatant was discarded and the pellet snap-frozen in liquid nitrogen. The pellet was resuspended in 95 µl of 90% acetonitrile (v/v) in water and metabolites were extracted by vortexing for 10 min at room temperature. Cell debris was removed by centrifugation at 4°C for 15 min at 13,000 x g. Extracts were transferred into HPLC vials, 5 µl internal standard (MVA-P) was added at a final concentration of 16 µM for analysis using liquid chromatography tandem mass spectrometry (LC-MS/MS).

LC-MS/MS data were acquired on an Advance UHPLC system (Bruker Daltonics, Fremont, CA, USA) equipped with a binary pump, degasser and PAL HTC-xt autosampler (CTC Analytics AG, Switzerland) coupled to an EVOQ Elite triple quadrupole mass spectrometer (Bruker Daltonics, Fremont, CA, USA). Separation of the structural isomers IPP and DMAPP was achieved by adapting a method from Köhling et al. (2014), by injecting 5 μl onto an Astec Cyclobond I2000 chiral HPLC column (250 mm ×4.6 mm; 5 μm particle size) (Sigma Aldrich) with an injection loop size of 2 µL. The column oven temperature was controlled and maintained at 35°C throughout the acquisition and the mobile phases were as follows: 50 mM aqueous ammonium acetate (eluent A) and 90:10 (% v/v) acetonitrile:purified water (eluent B). The mobile phase flow rate was maintained at 600 μL/min and was introduced directly into the mass spectrometer with no split. The mobile phase gradient profile was as follows: Starting condition 100% eluent B, 0.0–1.0 min: 100% B to 25% B, 1.0–22.0 min: 25% B, 22.0–22.5 min: 25% B to 0% B, 22.5–23.0 min: 0% B, 23.0–24.0 min: 0% B to 100% B, 24.0–30.0 min: 100% B. The mass spectrometer was controlled by MS Workstation 8.2.1 software (Bruker Daltonics) using electrospray ionization operated in negative ion mode. The following parameters were used to acquire Multiple Reaction Monitoring (MRM) data: spray voltage: 3.0 kV, cone temperature: 350°C, cone gas flow 20, probe gas flow: 50, nebulizer gas flow: 50, heated probe temperature: 350°C, exhaust gas: on, CID: 1.5 mTorr. The MRM scan time was set to 1000 ms for DMAPP and IPP, and 200 ms for MVA-P with standard resolution for all transitions. The collision energy (CE) was optimised for each transition. The quantifier was m/z 245.0 → 79 (CE: 16 eV) and qualifier m/z 245.0→ 159 (CE: 16 eV) for both DMAPP and IPP. For the internal standard MVA-P the quantifier was m/z 227.0 → 79 (CE: 24 eV) and qualifier m/z 227.0→ 97 (CE: 13 eV). Initial retention times (RT) were 14.1 min (MVA-P) 19.2 min (DMAPP) and 23.6 min (IPP) but shifted to less retention as the column presumably deteriorated during the runs. For quality control (QC) and to ensure correct peak integration a 1 μM standard DMAPP/IPP mix was injected every 12th sample. The RTs decreased in a linear fashion from the first 1 μM QC standard to the last QC standard (n = 52) with 0.024 min, 0.044 min, and 0.061 min per injection for MVA-P, DMAPP, and IPP respectively (R2 = 0.990, R2 = 0.991, R2 = 0.989). Analytes were integrated manually.

To obtain quantitative data, a matrix-matched internal standard calibration was used. Analyte stock solutions were prepared in 90% (v/v) acetonitrile and were diluted with blank matrix extract, extracted with 90:10 (% v/v) acetonitrile:Milli-Q water). The internal standard was added to the final HPLC vial at a concentration of 16 μM. The calibration curve ranged from 0.25 μM to 10 μM with R2 values of 0.968 and 0.981 for DMAPP and IPP, respectively. For both calibration curves a 1/x2 weighting factor was applied. Sample concentrations lower than the lowest standard were obtained through extrapolation of the calibration curve. The limit of quantification (LOQ) was approximated, using the lowest standard as reference (0.25 μM, n = 4), as 10x the signal-to-noise ratio. The LOQ estimate was 0.033 and 0.045 μM for DMAPP and IPP respectively. The 1 μM QC standard (n = 8) recovery was 85.6 (RSD 18.7%) and 93.2 (RSD 15.9%) for DMAPP and IPP respectively. Additionally, five standards with different DMAPP/IPP ratios were injected to verify the ratio accuracy. DMAPP:IPP ratios fortified were 10, 2, 1, 0.5, and 0.1, while ratios found were 11.1, 1.8, 0.96, 0.56, and 0.10 (bias ranging from −9.9 to 12.5% with a mean bias of 1.9%).

### Protein quantification

Cells were harvested for proteomics analyses at the same time point as metabolomics samples. Cell pellets corresponding to 1 ml of cultures of an optical density of OD600 = 5 were processed according to Rennig et al. (2019), both regarding preparation of samples, the applied gradient on the CapLC system and the settings for Orbitrap HF_X mass spectrometer. Here, a total of 1 µg of peptides/sample was injected into the mass spectrometer. After acquisition the raw files were analysed using Proteome Discoverer 2.3 (P.D. 2.3) in order to identify and quantify detected proteins. The following software settings were used: Fixed modification: Carbamidomethyl (C) and Variable modifications: oxidation of methionine residues. First search mass tolerance 10 ppm and a MS/MS tolerance of 0.02 Da., trypsin as proteolytic enzyme and allowing two missed cleavages. FDR was set at 0.1%. For match between runs the ΔRT was set to 0.2 min and the minimum peptide length was set to 7. As database for the searches the E. coli W proteome (UP000008525) was used combined with a contaminant database (cRAP) and the sequences of heterologous HDRs (see Table 1) and lycopene production proteins Idi (Genbank ID AAC32208.1), CrtE (WP026199135.1), CrtI (AAA64981.1), and CrtB (WP020503292.1). Normalization of the data across samples was done with P.D. 2.3. using total peptide amount, meaning all identified peptides in the individual samples are used for normalization, while using one file as master file to which all other counts are normalized. For quantification only unique peptides were used, and for all HDR proteins, hits were manually inspected to ensure correct identification and quantification. HDR overexpression strains were compared by analysing normalized peptide counts using one-way analysis of variance (ANOVA) or Welch’s ANOVA test in case of unequal variances, respectively. Where reported, p-values were adjusted for multiple comparison testing using Dunnett’s method, n ≥ 3 biological replicates.

### Isoprene production

The different pT-HDR plasmids were transformed into E. coli W∆cscR, lacZ::Pt-DXS, arsB::PaISPS(del2-52,A3T,L70R,S288C). All growth media contained 250 mg L−1 ampicillin for plasmid maintenance. Strains were grown in LB medium until stationary phase, then diluted in 0.5 ml TB medium containing 0.1 mM IPTG to a starting OD600 of 0.1, and grown at 30°C, with 250 rpm shaking. Cultures were grown in 20 ml sealed gas chromatography vials and isoprene was quantified after 48 hr as described previously (Vickers et al., 2015).

### Sequence alignments and generation of phylogenetic trees

HDR protein sequences were downloaded from the results of a BLASTP search with A. thaliana HDR against land plants (taxid: 3193), manually removing identical duplicates and obvious pseudogenes (deletions or mutations in highly conserved regions). Sequences were truncated to remove N-terminal chloroplast targeting sequences and aligned using CLC Main Workbench (Qiagen). HDR phylogenetic tree (unrooted) was generated using maximum likelihood phylogeny, neighbour-joining method, WAG protein substitution model, and bootstrap analysis with 100 replicates, also in CLC Main Workbench. Phylogenetic trees were visualised using Interactive Tree of Life (iTOL) v3 (Letunic and Bork, 2016).

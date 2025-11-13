# Phosphoprotein SAK1 is a regulator of acclimation to singlet oxygen in Chlamydomonas reinhardtii

## Authors

- Setsuko Wakao<sup>1</sup>
- Brian L Chin<sup>1</sup>
- Heidi K Ledford<sup>1</sup>
- Rachel M Dent<sup>1</sup>
- David Casero<sup>2</sup>
- Matteo Pellegrini<sup>2</sup>
- Sabeeha S Merchant<sup>3</sup>
- Krishna K Niyogi<sup>1</sup> †

### Affiliations

1. Department of Plant and Microbial Biology University of California, Berkeley Berkeley United States
2. Department of Molecular, Cell and Developmental Biology University of California, Los Angeles Los Angeles United States
3. Institute for Genomics and Proteomics, University of California, Los Angeles Los Angeles United States
4. Department of Chemistry and Biochemistry University of California, Los Angeles Los Angeles United States
5. Howard Hughes Medical Institute, University of California, Berkeley Berkeley United States
6. Physical Biosciences Division Lawrence Berkeley National Laboratory Berkeley United States

† Corresponding author

## Abstract

Singlet oxygen is a highly toxic and inevitable byproduct of oxygenic photosynthesis. The unicellular green alga Chlamydomonas reinhardtii is capable of acclimating specifically to singlet oxygen stress, but the retrograde signaling pathway from the chloroplast to the nucleus mediating this response is unknown. Here we describe a mutant, singlet oxygen acclimation knocked-out 1 (sak1), that lacks the acclimation response to singlet oxygen. Analysis of genome-wide changes in RNA abundance during acclimation to singlet oxygen revealed that SAK1 is a key regulator of the gene expression response during acclimation. The SAK1 gene encodes an uncharacterized protein with a domain conserved among chlorophytes and present in some bZIP transcription factors. The SAK1 protein is located in the cytosol, and it is induced and phosphorylated upon exposure to singlet oxygen, suggesting that it is a critical intermediate component of the retrograde signal transduction pathway leading to singlet oxygen acclimation.

## Introduction

Growth of photosynthetic organisms depends on light energy, which in turn can cause oxidative damage to the cell if not managed properly (Li et al., 2009). Light intensity is highly dynamic in terrestrial and aquatic environments, and the cell must constantly control the dissipation of light energy to avoid photo-oxidative stress while maximizing productivity. In addition to being the site of photosynthesis, the chloroplast houses many essential biochemical reactions such as fatty acid and amino acid biosynthesis, but most of its proteins are encoded in the nucleus and must be imported after translation. Therefore the nucleus must monitor the status of the chloroplast and coordinate gene expression and synthesis of proteins to maintain healthy chloroplast functions.

It is known that signals originating from a stressed or dysfunctional chloroplast modulate nuclear gene expression, a process that is called retrograde signaling (Nott et al., 2006; Chi et al., 2013). In Arabidopsis thaliana the gun mutants have helped to define the field of chloroplast retrograde signaling, leading to the identification of GUN1, a pentatricopeptide repeat protein that is a regulator of this process (Koussevitzky et al., 2007), and pointing to the involvement of the tetrapyrrole biosynthetic pathway (Vinti et al., 2000; Mochizuki et al., 2001; Larkin et al., 2003; Strand et al., 2003; Woodson and Chory, 2008). A role for heme in retrograde signaling has been shown in Chlamydomonas reinhardtii as well (von Gromoff et al., 2008). Many of the gun studies were conducted in context of a dysfunctional chloroplast treated with norflurazon, an inhibitor of carotenoid biosynthesis. More recently a number of exciting advances have shed light on small molecules playing roles in retrograde stress signaling, including methylerythritol cyclodiphosphate, an intermediate of isoprenoid biosynthesis in the chloroplast (Xiao et al., 2012), 3-phosphoadenosine 5-phosphate (PAP) (Estavillo et al., 2011), as well as a chloroplast envelope transcription factor PTM (Sun et al., 2011). Plastid gene expression involving sigma factors has been implicated in affecting nuclear gene expression, although the mechanism is unknown (Coll et al., 2009; Woodson et al., 2012).

Activation of gene expression by reactive oxygen species (ROS) has been well documented (Apel and Hirt, 2004; Mittler et al., 2004; Gadjev et al., 2006; Li et al., 2009). Thus ROS have been proposed as a means for chloroplasts to signal stress to the nucleus and many examples of global gene expression changes in response to ROS have been described (Desikan et al., 2001; Vandenabeele et al., 2004; Vanderauwera et al., 2005). Singlet oxygen (1O2) is a highly toxic form of ROS that can be formed in all aerobic organisms through photosensitization reactions in which excitation energy is transferred from a pigment molecule to O2. For example, porphyria in humans is caused by defects in tetrapyrrole metabolism that can lead to accumulation of photosensitizing intermediates, which generate 1O2 in the light (Straka et al., 1990). In oxygenic photosynthetic organisms, 1O2 is mainly generated at the reaction center of photosystem II, when triplet excited chlorophyll transfers energy to O2 (Krieger-Liszkay, 2005). 1O2 is the predominant cause of lipid oxidation during photo-oxidative stress (Triantaphylidès et al., 2008) and is associated with damage to the reaction center (Trebst et al., 2002). Because of the abundance and proximity of the two elements of 1O2 generation, the photosensitizer chlorophyll and O2, it was hypothesized that oxygenic photosynthetic organisms must have evolved robust means to cope with this ROS (Knox and Dodge, 1985). In Arabidopsis, the EX1 and EX2 proteins in the chloroplast are required for the execution of a 1O2-dependent response: growth arrest in plants and programmed cell death in seedlings, that is distinct from cell damage (op den Camp et al., 2003; Wagner et al., 2004; Lee et al., 2007). Different players in 1O2 signaling have emerged recently, such as β-cyclocitral, an oxidation product of β-carotene in Arabidopsis (Ramel et al., 2012), a bZIP transcription factor (SOR1) responding to reactive electrophiles generated by 1O2 (Fischer et al., 2012), and a cytosolic zinc finger protein conserved in Arabidopsis and Chlamydomonas, MBS (Shao et al., 2013). In the anoxygenic photosynthetic bacterium Rhodobacter sphaeroides, a σE factor is responsible for the elicitation of the gene expression response to 1O2 (Anthony et al., 2005).

The unicellular green alga Chlamydomonas reinhardtii is an excellent model organism for investigation of retrograde 1O2 signaling. Chlamydomonas exhibits an acclimation response to 1O2, in which exposure to a sublethal dose of 1O2 leads to changes in nuclear gene expression that enable cells to resist a subsequent challenge with higher levels of 1O2 (Ledford et al., 2007). We hypothesized that acclimation mutants should include regulatory mutants that are defective in sensing and responding to 1O2. Here we describe the isolation of such a mutant and identification of a cytosolic phosphoprotein SAK1 that is critical for the acclimation and transcriptome response to 1O2.

## Results

### Isolation of a singlet oxygen-sensitive mutant that is defective in acclimation

Chlamydomonas acclimates to singlet oxygen (1O2) generated by the exogenous photosensitizing dye rose bengal (RB) in the light (Ledford et al., 2007). As shown in Figure 1A, wild-type (WT) cells that were pretreated with RB in the light were able to survive a challenge treatment with much higher concentrations of RB, unlike cells pretreated with RB in the dark. By screening an insertional mutant population (Dent et al., 2005) for strains that were sensitive to 1O2, we isolated a mutant called singlet oxygen acclimation knocked-out1 (sak1) that is defective in acclimation to 1O2 (Figure 1A). We have previously shown that Chlamydomonas WT cells can also acclimate to RB following pretreatment with high light (Ledford et al., 2007), indicating that high light and RB induce overlapping responses to 1O2. When subjected to the same conditions (high light pretreatment followed by challenge with RB), sak1 demonstrated less robust cross-acclimation (Figure 1B). We also tested conversely whether pretreatment with RB can acclimate the cells to growth in high light or in the presence of norflurazon. No increase in resistance to high light or norflurazon was induced by pretreatment with RB in either WT or sak1 (Figure 1—figure supplement 1). The viability phenotypes after RB treatment shown in Figure 1A were paralleled by changes in Fv/Fm values, a chlorophyll fluorescence parameter representing photosystem II efficiency (Figure 1C). In both WT and sak1, pretreatment did not cause an inhibition of photosystem II, as demonstrated by unchanged Fv/Fm values after 30 min. However, pretreatment increased resistance of photosystem II to the RB challenge only in WT and not in sak1 cells (Figure 1C). The pretreatment protected the cells only transiently, as by 90 min of challenge treatment both genotypes appeared to have experienced similar inhibition of photosystem II (Figure 1C), consistent with the hypothesis that sak1 is disrupted in early sensing and/or initiation of 1O2 response rather than its direct detoxification.

![Figure 1.](https://cdn.elifesciences.org/articles/02286/elife-02286-fig1-v3.jpg)

**Figure 1.:** (A) Acclimation phenotype of WT and sak1. The cells were pretreated in the dark (−) or under light (+) in the presence of rose bengal (RB), which requires light for generation of 1O2. Pretreatment was followed by a subsequent higher concentration of RB (Challenge) as indicated under light. (B) Cells grown in low light were either kept in low light (−) or transferred to high light (+) for an hour before challenge in the light with increasing RB concentrations. (C) Fv/Fm values were measured after each time point indicated. Pretreatment (PreT) with 0.5 μM RB was applied for 30 min with (+PreT) or without (−PreT) light. After the pretreatment, RB was added to both dark and light samples to a final concentration of 3.75 μM RB (challenge), and Fv/Fm was measured for 90 min at 30 min intervals (total 120 min). First arrow: addition of pretreatment; second arrow: addition of challenge. (D) sak1 has wild-type sensitivity to other photo-oxidative stresses. Serial dilutions of WT and sak1 were spotted onto minimal (HS) plates at the indicated light intensity or on TAP plates containing the indicated inhibitor. DCMU, 3-(3,4-dichlorophenyl)-1,1-dimethylurea; low light (LL), 80 µmol photons m−2 s−1; high light (HL), 450 µmol photons m−2 s−1. (E) Gene expression of a known 1O2-responsive gene, GPX5, is induced during acclimation, while two genes associated with H2O2 response, APX1 and CAT1, are not. WT cells were mock-pretreated without RB (white bars) or pretreated with RB in the light (black bars).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/02286/elife-02286-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** Cells were pretreated with 1 μM RB with (+) or without (−) light, then spotted on minimal plates and grown under high light (HL) or grown photoheterotrophically on TAP plates containing norflurazon (NF) and grown under low light for 4 days. Cells were spotted in serial dilutions.

In contrast to its RB sensitivity, sak1 exhibited wild-type resistance to high light, various photosynthetic inhibitors and generators of other ROS, suggesting its defect is specific to 1O2 (Figure 1D). When tested for the gene expression response of the known 1O2-specific gene GPX5 (Leisinger et al., 2001) during acclimation, WT cells showed a 20- to 30-fold induction, whereas a known H2O2-responsive ascorbate peroxidase gene (APX1) in Chlamydomonas (Urzica et al., 2012) and a catalase gene (CAT1), known to be H2O2 responsive in Arabidopsis (Davletova et al., 2005; Vanderauwera et al., 2005), were unchanged. The mutant sak1 showed attenuated GPX5 induction, as expected for a mutant defective in the 1O2 response (Figure 1E).

### The global gene expression response to 1O2 in Chlamydomonas is distinct from that in Arabidopsis

To obtain insight into the cellular processes and the genes involved in 1O2 acclimation, we used RNA-seq to define the transcriptome of WT cells during acclimation. The sequences were mapped to the Chlamydomonas reinhardtii genome version 4 (v4), and 16476 transcripts corresponding to gene models were detected (Wakao et al., 2014). We validated the data by quantitative reverse transcriptase PCR (qRT-PCR) for some of the differentially expressed genes during acclimation (Figure 2). Basal expression of some of the genes was elevated in sak1 compared to WT (Cre16.g683400 and GST1, Figure 2). Comparisons of the fold change (FC) values obtained by RNA-seq and qRT-PCR for the genes tested in Figure 2 are shown in Figure 2. The FC values are comparable between the two methods, although genes with FC greater than 20 (detected by RNA-seq) showed FC values (estimated by qRT-PCR) that were two to three times higher (Cre06.g281250.t1.1, Cre13.g566850.t1.1, Cre06.g263550.t1.1, Cre14.g623650.t1.2). Some of the genes were also induced by a transition from low light to high light, although not as strongly (Table 1), indicating that the 1O2 response elicited by addition of RB partly overlaps with that caused by increased light intensity. To examine whether the transcriptome changes were specific to 1O2, we examined the expression of several previously identified H2O2-responsive genes (Urzica et al., 2012) (Table 2). Two of the seven genes, VTC2 (3.4-fold) and DHAR1 (twofold) were induced during 1O2 acclimation, whereas the other five genes were not differentially expressed (induced more than twofold) in our data. For these two genes, their magnitude of induction by 1O2 was smaller than that of H2O2-treated cells (both genes were ∼ninefold induced by 1 mM H2O2 treatment for 60 min) (Urzica et al., 2012). These differences suggest that our treatment with 1O2 did not lead to a large-scale induction of H2O2-responsive genes, and it is likely that the two above-mentioned genes involved in ascorbate metabolism respond to both H2O2 and 1O2.

![Figure 2.](https://cdn.elifesciences.org/articles/02286/elife-02286-fig2-v3.jpg)

**Figure 2.:** (A) The error bars indicate standard deviation of biological triplicates. The locus of the transcript (v5) and gene name if annotated, are indicated. *SOUL1 was named gene in v4 but not in v5. (B) Comparison of fold change values from RNA-seq data and qPCR. Fold change values were calculated for RNA-seq as described in ‘Material and methods’, and the values for qPCR are averages obtained from biological triplicates.

**Table 1.**
 Moderate induction of 1O2 genes during high light exposure


<table>
  <thead>
    <tr>
      <th></th>
      <th>Fold change (SD)*</th>
      <th></th>
    </tr>
    <tr>
      <th>Gene name or ID</th>
      <th>WT</th>
      <th>sak1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GPX5</td>
      <td>2.86 (1.06)</td>
      <td>1.08 (0.23)</td>
    </tr>
    <tr>
      <td>CFA1</td>
      <td>3.75 (0.99)</td>
      <td>1.78 (0.52)</td>
    </tr>
    <tr>
      <td>SOUL2</td>
      <td>3.45 (1.25)</td>
      <td>1.82 (0.22)</td>
    </tr>
    <tr>
      <td>MRP3</td>
      <td>3.10 (0.39)</td>
      <td>2.37 (0.32)</td>
    </tr>
    <tr>
      <td>Cre14.g613950</td>
      <td>1.42 (0.53)</td>
      <td>1.57 (0.46)</td>
    </tr>
    <tr>
      <td>LHCSR1†</td>
      <td>14.91 (4.25)</td>
      <td>2.91 (1.35)</td>
    </tr>
  </tbody>
</table>

_*Fold change values are the average of biological triplicates and their standard deviations are indicated in parentheses.†Known to have elevated expression in high light grown cells (Peers et al., 2009)._

**Table 2.**
 Expression of H2O2 response genes during 1O2 acclimation


<table>
  <thead>
    <tr>
      <th></th>
      <th>Gene ID</th>
      <th></th>
      <th>RPKM*</th>
      <th></th>
      <th></th>
      <th></th>
      <th>Fold change†</th>
      <th></th>
    </tr>
    <tr>
      <th>Gene name</th>
      <th>v4</th>
      <th>v5</th>
      <th>WT-mock</th>
      <th>WT-RB</th>
      <th>sak1-mock</th>
      <th>sak1-RB</th>
      <th>WT</th>
      <th>sak1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>APX1</td>
      <td>Cre02.g087700.t1.1</td>
      <td>Cre02.g087700.t1.2</td>
      <td>49.70</td>
      <td>36.22</td>
      <td>79.65</td>
      <td>58.83</td>
      <td>0.73</td>
      <td>0.74</td>
    </tr>
    <tr>
      <td>MSD3</td>
      <td>Cre16.g676150.t1.1</td>
      <td>Cre16.g676150.t1.2</td>
      <td>0.30</td>
      <td>0.18</td>
      <td>0.70</td>
      <td>0.17</td>
      <td>0.60</td>
      <td>0.25</td>
    </tr>
    <tr>
      <td>MDAR1</td>
      <td>Cre17.g712100.t1.1</td>
      <td>Cre17.g712100.t1.2</td>
      <td>35.95</td>
      <td>38.30</td>
      <td>33.53</td>
      <td>51.34</td>
      <td>1.07</td>
      <td>1.53</td>
    </tr>
    <tr>
      <td>DHAR1</td>
      <td>Cre10.g456750.t1.1</td>
      <td>Cre10.g456750.t1.2</td>
      <td>20.40</td>
      <td>40.93</td>
      <td>25.69</td>
      <td>42.18</td>
      <td>2.01</td>
      <td>1.64</td>
    </tr>
    <tr>
      <td>GSH1</td>
      <td>Cre02.g077100.t1.1</td>
      <td>Cre02.g077100.t1.2</td>
      <td>28.27</td>
      <td>26.91</td>
      <td>40.42</td>
      <td>49.95</td>
      <td>0.95</td>
      <td>1.24</td>
    </tr>
    <tr>
      <td>GSHR1</td>
      <td>Cre06.g262100.t1.2</td>
      <td>Cre06.g262100.t1.3</td>
      <td>19.17</td>
      <td>19.02</td>
      <td>19.39</td>
      <td>22.41</td>
      <td>0.99</td>
      <td>1.16</td>
    </tr>
    <tr>
      <td>VTC2</td>
      <td>Cre13.g588150.t1.1</td>
      <td>Cre13.g588150.t1.2</td>
      <td>18.16</td>
      <td>62.53</td>
      <td>35.10</td>
      <td>103.12</td>
      <td>3.44</td>
      <td>2.94</td>
    </tr>
  </tbody>
</table>

_*Average of RPKM obtained from two sequencing lanes as described in ‘Material and methods’.†Calculated as ratio of (RPKM-RB) / (RPKM-mock)._

During acclimation of WT to 1O2, 515 genes were up-regulated at least twofold with a false discovery rate (FDR) smaller than 1% (Supplementary file 1, C1), and 33% of these could be categorized into functional classes based on MapMan (Thimm et al., 2004) using the Algal Functional Annotation Tool (Lopez et al., 2011) (Figure 3A,B). The enriched classes are marked with asterisks, and the genes within those classes are listed in Table 3. Genes involved in sterol/squalene/brassinosteroid metabolism (in the hormone and lipid metabolism functional classes) were notably enriched (Table 3). A sterol methyltransferase was also detected to display differential expression in our previous microarray analysis (Ledford et al., 2007). Brassinosteroids are not known to exist in Chlamydomonas, and in plants increasing evidence indicates sterols have a signaling role independent of brassinosteroids (Lindsey et al., 2003; Boutté and Grebe, 2009). Two cyclopropane fatty acid synthases (CFAs) were among the up-regulated lipid metabolism genes (Table 3). Another function that was notable among up-regulated genes, although they were not grouped to a common functional class by MapMan, were two genes coding for SOUL heme-binding domain proteins that were SAK1-dependent (SOUL2 and Cre06.g299700.t1.1, formerly annotated as SOUL1) (Figure 2). Genes annotated as involved in transport comprised one of the most enriched classes (Figure 3B). These included a number of multidrug-resistant (MDR) and pleiotropic drug-resistant (PDR) type transporters as well as other various transporters for ions, peptides, and lipids (Table 3). The former types of transporters may reflect the cells' response to pump RB out. When the responses to the chemical RB and 1O2 were uncoupled by comparing gene expression in cultures kept in the dark with and without RB, all of the tested 1O2-induced genes and ABC transporters identified from our RNA-seq remained unchanged by RB in the dark in both WT and sak1 (Table 4). This result indicates that the up-regulation of these genes when RB was added in the light was a response to 1O2 rather than to RB itself. Up-regulation of stress genes included those coding for chaperones and some receptor-like proteins (Figure 3B; Table 3), suggesting that the cells do mount a stress response during acclimation though not visible by gross growth phenotype (Figure 1A) or decrease in Fv/Fm (Figure 1C). A smaller number of 219 genes was down-regulated during acclimation in WT (Supplementary file 1, C1), only 21% of which had functional annotation. The most enriched classes of down-regulated genes were nucleotide metabolism and transport, the latter including a distinct type of transporter for small metabolites and ions, different from those found among up-regulated genes that included many MDR- and PDR-type transporters (Figure 3B; Table 3).

![Figure 3.](https://cdn.elifesciences.org/articles/02286/elife-02286-fig3-v3.jpg)

**Figure 3.:** (A) Venn diagram representing differentially expressed genes in WT and sak1. Mapman functional classes distribution of differentially expressed genes (passing criteria of fold change greater than 21 [up] or smaller than 2−1 [down] with FDR <1%) during acclimation in (B) WT and (C) sak1. (D) Differentially expressed genes when comparing WT and sak1 in basal conditions (i.e., before exposure to 1O2). The functional classes represented by the numbers are listed; asterisks indicate classes that were enriched compared to the genome.

**Table 3.**
 Enriched functional classes among differentially expressed genes in WT during 1O2 acclimation


<table>
  <thead>
    <tr>
      <th>Primary MapMan class</th>
      <th>Secondary Mapman class</th>
      <th>Gene ID (v4)</th>
      <th>Gene ID (v5)</th>
      <th>Gene name</th>
      <th>Annotation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="6">Up-regulated genes</td>
    </tr>
    <tr>
      <td>transport</td>
      <td>ABC transporters and multidrug resistance systems</td>
      <td>Cre03.g169300.t1.1</td>
      <td>Cre03.g169300.t2.1</td>
      <td></td>
      <td>ABC transporter (ABC-2 type)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre04.g220850.t1.1</td>
      <td>Cre04.g220850.t1.2</td>
      <td></td>
      <td>ABC transporter (ABC-2 type)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre11.g474600.t1.1§</td>
      <td>Cre02.g095151.t1</td>
      <td></td>
      <td>ABC transporter (ABC-2 type)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g151400.t1.2</td>
      <td>Cre03.g151400.t1.3</td>
      <td></td>
      <td>ABC transporter (subfamilyA member3)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre14.g618400.t1.1§</td>
      <td>Cre14.g618400.t1.2</td>
      <td></td>
      <td>ABC transporter</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre09.g395750.t1.2</td>
      <td>Cre09.g395750.t1.3</td>
      <td></td>
      <td>ABC transporter (plant PDR pleitropic drug resistance)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre14.g613950.t1.1§</td>
      <td>Cre14.g613950.t2.1</td>
      <td></td>
      <td>ABC transporter, Lipid exporter ABCA1 and related proteins</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre17.g725150.t1.1</td>
      <td>Cre17.g725150.t1.2</td>
      <td></td>
      <td>ABC transporter</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre04.g224400.t1.2§</td>
      <td>Cre04.g224400.t1.3</td>
      <td></td>
      <td>ABC transporter (plant PDR pleitropic drug resistance)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre13.g564900.t1.1§</td>
      <td>Cre13.g564900.t1.2</td>
      <td>MRP3</td>
      <td>ABC transporter, Multidrug resistance associated protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre17.g721000.t1.1</td>
      <td>Cre17.g721000.t1.2</td>
      <td></td>
      <td>ABC transporter (ABCA)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre04.g224500.t1.2</td>
      <td>Cre04.g224500.t1.3</td>
      <td></td>
      <td>ABC transporter (plant PDR pleitropic drug resistance)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g007000.t1.1§</td>
      <td>Cre01.g007000.t1.2</td>
      <td></td>
      <td>ABC transporter (ABC-2 type)</td>
    </tr>
    <tr>
      <td></td>
      <td>unspecified anions</td>
      <td>Cre13.g574000.t1.2</td>
      <td>Cre13.g574000.t1.3</td>
      <td></td>
      <td>Chloride channel 7</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre17.g729450.t1.1</td>
      <td>Cre17.g729450.t1.2</td>
      <td></td>
      <td>Chloride channel 7</td>
    </tr>
    <tr>
      <td></td>
      <td>amino acids</td>
      <td>Cre04.g226150.t1.2</td>
      <td>Cre04.g226150.t1.3</td>
      <td>AOC1</td>
      <td>Amino acid carrier 1; belongs to APC (amino acid polyamine organocation) family</td>
    </tr>
    <tr>
      <td></td>
      <td>misc</td>
      <td>Cre16.g683400.t1.1§</td>
      <td>Cre16.g683400.t1.2</td>
      <td></td>
      <td>CRAL/TRIO domain (Retinaldehyde binding protein-related)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre17.g718100.t1.1</td>
      <td>Cre17.g718100.t1.2</td>
      <td></td>
      <td>Phosphatidylinositol transfer protein SEC14 and related proteins (CRAL/TRIO)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g311000.t1.2</td>
      <td>Cre06.g311000.t1.3</td>
      <td>FBT2</td>
      <td>Folate transporte</td>
    </tr>
    <tr>
      <td></td>
      <td>calcium</td>
      <td>Cre09.g410050.t1.1§</td>
      <td>Cre09.g410050.t1.2</td>
      <td></td>
      <td>Ca2+ transporting ATPase</td>
    </tr>
    <tr>
      <td></td>
      <td>potassium</td>
      <td>Cre07.g329882.t1.2</td>
      <td>Cre07.g329882.t1.3</td>
      <td></td>
      <td>Ca2+-activated K+ channel proteins</td>
    </tr>
    <tr>
      <td></td>
      <td>phosphate</td>
      <td>Cre16.g686750.t1.1</td>
      <td>Cre16.g686750.t1.2</td>
      <td>PTA3</td>
      <td>Proton/phosphate symporter</td>
    </tr>
    <tr>
      <td></td>
      <td>metal</td>
      <td>Cre13.g570600.t1.1</td>
      <td>Cre13.g570600.t1.2</td>
      <td>CTR1</td>
      <td>CTR type copper ion transporter</td>
    </tr>
    <tr>
      <td></td>
      <td>metabolite transporters at the mitochondrial membrane</td>
      <td>Cre06.g267800.t1.2</td>
      <td>Cre06.g267800.t2.1</td>
      <td></td>
      <td>Mitochondrial carrier protein</td>
    </tr>
    <tr>
      <td>hormone metabolism*</td>
      <td>brassinosteroid</td>
      <td>Cre16.g663950.t1.1</td>
      <td>Cre16.g663950.t1.2</td>
      <td></td>
      <td>Sterol C5-desaturase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g076800.t1.1</td>
      <td>Cre02.g076800.t1.2</td>
      <td></td>
      <td>delta14-sterol reductase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre12.g557900.t1.1</td>
      <td>Cre12.g557900.t1.1</td>
      <td>CDI1</td>
      <td>C-8,7 sterol isomerase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g092350.t1.1</td>
      <td>Cre02.g092350.t1.2</td>
      <td></td>
      <td>Cytochrome P450, CYP51 Sterol-demethylase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre12.g500500.t1.2</td>
      <td>Cre12.g500500.t2.1</td>
      <td></td>
      <td>SAM-dependent methyltransferases</td>
    </tr>
    <tr>
      <td></td>
      <td>jasmonate</td>
      <td>Cre19.g756100.t1.1</td>
      <td>Cre03.g210513.t1</td>
      <td></td>
      <td>12-oxophytodienoic acid reductase</td>
    </tr>
    <tr>
      <td></td>
      <td>auxin</td>
      <td>Cre14.g609900.t1.1</td>
      <td>Cre14.g609900.t1.1</td>
      <td></td>
      <td>Predicted membrane protein, contains DoH and Cytochrome b-561/ferric reductase transmembrane domains</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g276050.t1.1</td>
      <td>Cre06.g276050.t1.2</td>
      <td></td>
      <td>Aldo/keto reductase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g692800.t1.2</td>
      <td>Cre16.g692800.t1.3</td>
      <td></td>
      <td>Aldo/keto reductase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g185850.t1.2</td>
      <td>Cre03.g185850.t1.2</td>
      <td></td>
      <td>pfkB family, sugar kinase-related</td>
    </tr>
    <tr>
      <td>minor CHO metabolism</td>
      <td>others</td>
      <td>Cre06.g276050.t1.1</td>
      <td>Cre06.g276050.t1.2</td>
      <td></td>
      <td>Aldo/keto reductase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g692800.t1.2</td>
      <td>Cre16.g692800.t1.3</td>
      <td></td>
      <td>Aldo/keto reductase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g185850.t1.2</td>
      <td>Cre03.g185850.t1.2</td>
      <td></td>
      <td>pfkB family, sugar kinase-related</td>
    </tr>
    <tr>
      <td></td>
      <td>callose</td>
      <td>Cre06.g302050.t1.1</td>
      <td>Cre06.g302050.t1.2</td>
      <td></td>
      <td>1,3-beta-glucan synthase</td>
    </tr>
    <tr>
      <td></td>
      <td>myo-inositol</td>
      <td>Cre03.g180250.t1.1</td>
      <td>Cre03.g180250.t1.2</td>
      <td></td>
      <td>Myo-inositol-1-phosphate synthase</td>
    </tr>
    <tr>
      <td>stress</td>
      <td>biotic</td>
      <td>Cre01.g057050.t1.1§</td>
      <td>Cre03.g144324.t1</td>
      <td></td>
      <td>Leucine Rich Repeat</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g016200.t1.2</td>
      <td>Cre01.g016200.t1</td>
      <td></td>
      <td>Mlo Family</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre28.g776450.t1.1§</td>
      <td>Cre08.g358573.t1</td>
      <td>PSMD10</td>
      <td>26S proteasome regulatory complex</td>
    </tr>
    <tr>
      <td></td>
      <td>abiotic</td>
      <td>Cre12.g501500.t1.1</td>
      <td>NF†</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g132300.t1.2</td>
      <td>Cre09.g395732.t1</td>
      <td></td>
      <td>DnaJ domain</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g339650.t1.2</td>
      <td>Cre07.g339650.t1.3</td>
      <td>DNJ20</td>
      <td>DnaJ-like protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g033300.t1.1§</td>
      <td>Cre01.g033300.t2.1</td>
      <td></td>
      <td>No annotation‡</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g677000.t1.1</td>
      <td>Cre16.g677000.t1.2</td>
      <td>HSP70E</td>
      <td>Heat shock protein 70E</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre08.g372100.t1.1</td>
      <td>Cre08.g372100.t1.2</td>
      <td>HSP70A</td>
      <td>Heat shock protein 70A</td>
    </tr>
    <tr>
      <td>lipid metabolism</td>
      <td>phospholipid synthesis</td>
      <td>Cre13.g604700.t1.2</td>
      <td>Cre13.g604700.t1.3</td>
      <td>PCT1</td>
      <td>CDP-alcohol phosphatidyltransferase/Phosphatidylglycerol-phosphate synthase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g281250.t1.1§</td>
      <td>Cre06.g281250.t1.2</td>
      <td>CFA1</td>
      <td>Cyclopropane fatty acid synthase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre09.g398700.t1.1§</td>
      <td>Cre09.g398700.t1.2</td>
      <td>CFA2</td>
      <td>Cyclopropane fatty acid synthase</td>
    </tr>
    <tr>
      <td></td>
      <td>‘exoticsߣ (steroids, squalene etc)</td>
      <td>Cre01.g061750.t1.1</td>
      <td>Cre03.g146507.t1</td>
      <td>SPT2</td>
      <td>Serine palmitoyltransferase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre83.g796250.t1.1</td>
      <td>NF†</td>
      <td>SPT1</td>
      <td>Serine palmitoyltransferase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g137850.t1.1</td>
      <td>Cre09.g400516.t1</td>
      <td></td>
      <td>TRAM (translocating chain-associating membrane) superfamily</td>
    </tr>
    <tr>
      <td></td>
      <td>FA synthesis and FA elongation</td>
      <td>Cre03.g182050.t1.1</td>
      <td>Cre03.g182050.t1</td>
      <td></td>
      <td>Long-chain acyl-CoA synthetases (AMP-forming)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g256750.t1.1</td>
      <td>Cre06.g256750.t1.2</td>
      <td></td>
      <td>Acyl-ACP thioesterase</td>
    </tr>
    <tr>
      <td>misc</td>
      <td>short chain dehydrogenase/reductase (SDR)</td>
      <td>Cre12.g556750.t1.2</td>
      <td>Cre12.g556750.t1.3</td>
      <td></td>
      <td>Short chain dehydrogenase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre27.g775000.t1.1</td>
      <td>Cre12.g549852.t1</td>
      <td></td>
      <td>Short chain dehydrogenase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre17.g731350.t1.2</td>
      <td>Cre17.g731350.t1.2</td>
      <td></td>
      <td>Short chain dehydrogenase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre08.g381510.t1.1§</td>
      <td>NF†</td>
      <td></td>
      <td>Short chain alcohol dehydrogenase</td>
    </tr>
    <tr>
      <td></td>
      <td>UDP glucosyl and glucoronyl transferases</td>
      <td>Cre02.g144050.t1.1</td>
      <td>Cre02.g144050.t2.1</td>
      <td></td>
      <td>Acetylglucosaminyltransferase EXT1/exostosin 1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g659450.t1.1</td>
      <td>Cre16.g659450.t1.2</td>
      <td></td>
      <td>Lactosylceramide 4-alpha-Galactosyltransferase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g173300.t1.1</td>
      <td>Cre03.g173300.t1.2</td>
      <td></td>
      <td>Lactosylceramide 4-alpha-Galactosyltransferase</td>
    </tr>
    <tr>
      <td></td>
      <td>dynamin</td>
      <td>Cre02.g079550.t1.1</td>
      <td>Cre02.g079550.t1.2</td>
      <td></td>
      <td>Dynamin-related GTPase, involved in circadian rhythms</td>
    </tr>
    <tr>
      <td></td>
      <td>misc2</td>
      <td>Cre06.g258600.t1.1§</td>
      <td>Cre06.g258600.t2.1</td>
      <td></td>
      <td>Predicted hydrolase related to dienelactone hydrolase</td>
    </tr>
    <tr>
      <td></td>
      <td>acid and other phosphatases</td>
      <td>Cre06.g249800.t1.1</td>
      <td>Cre06.g249800.t1.2</td>
      <td></td>
      <td>Sphingomyelin synthase</td>
    </tr>
    <tr>
      <td colspan="6">Down-regulated genes</td>
    </tr>
    <tr>
      <td>nucleotide metabolism</td>
      <td>salvage</td>
      <td>Cre13.g573800.t1.1</td>
      <td>Cre13.g573800.t1.2</td>
      <td></td>
      <td>Phosphoribulokinase / Uridine kinase family</td>
    </tr>
    <tr>
      <td></td>
      <td>synthesis</td>
      <td>Cre12.g503300.t1.1</td>
      <td>Cre12.g503300.t1.2</td>
      <td></td>
      <td>Phosphoribosylamidoimidazole-succinocarboxamide synthase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g308500.t1.1</td>
      <td>Cre06.g308500.t1.2</td>
      <td>CMP2</td>
      <td>Carbamoyl phosphate synthase, small subunit</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre14.g614300.t1.1</td>
      <td>Cre14.g614300.t1.2</td>
      <td></td>
      <td>Inosine-5-monophosphate dehydrogenase</td>
    </tr>
    <tr>
      <td>transport</td>
      <td>ABC transporters and multidrug resistance systems</td>
      <td>Cre06.g273750.t1.2</td>
      <td>Cre06.g273750.t1.3</td>
      <td>SUA1</td>
      <td>Chloroplast sulfate transporter</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g083354.t1.1</td>
      <td>Cre02.g083354.t1</td>
      <td></td>
      <td>ATP-binding cassette, subfamily B (MDR/TAP), member 9</td>
    </tr>
    <tr>
      <td></td>
      <td>calcium</td>
      <td>Cre06.g263950.t1.2</td>
      <td>Cre06.g263950.t1.3</td>
      <td></td>
      <td>Na+/K + ATPase, alpha subunit</td>
    </tr>
    <tr>
      <td></td>
      <td>metabolite transporters at the envelope membrane</td>
      <td>Cre08.g363600.t1.1</td>
      <td>Cre08.g363600.t1.2</td>
      <td></td>
      <td>Glucose-6-phosphate, PEP/phosphate antiporter</td>
    </tr>
    <tr>
      <td></td>
      <td>metal</td>
      <td>Cre17.g720400.t1.2</td>
      <td>Cre17.g720400.t1.3</td>
      <td>HMA1</td>
      <td>Heavy metal transporting ATPase</td>
    </tr>
    <tr>
      <td></td>
      <td>P- and V-ATPases</td>
      <td>Cre10.g459200.t1.1</td>
      <td>Cre10.g459200.t1.2</td>
      <td>ACA4</td>
      <td>Plasma membrane H + -transporting ATPase</td>
    </tr>
    <tr>
      <td></td>
      <td>phosphate</td>
      <td>Cre02.g144650.t1.1</td>
      <td>Cre02.g144650.t1.2</td>
      <td>PTB12</td>
      <td>Na+/Pi symporter</td>
    </tr>
    <tr>
      <td></td>
      <td>potassium</td>
      <td>Cre06.g278700.t1.2</td>
      <td>Cre06.g278700.t1.2</td>
      <td></td>
      <td>Myotrophin and similar proteins</td>
    </tr>
  </tbody>
</table>

_*Functional terms are inferred by homology to the annotation set of Arabidopsis thaliana (Lopez et al., 2011).†Corresponding gene model was not found in v5.‡No functional annotations found on v5 but defined by MapMan on Algal Functional Annotation Tool (Lopez et al., 2011).§Induction during 1O2 acclimation dependent on SAK1 (Table 5)._

**Table 4.**
 1O2 response genes are not induced when RB is added in the dark


<table>
  <thead>
    <tr>
      <th></th>
      <th>Fold change +RB/−RB (SD)*</th>
      <th></th>
    </tr>
    <tr>
      <th>Gene name or ID</th>
      <th>WT</th>
      <th>sak1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GPX5</td>
      <td>1.13 (0.33)</td>
      <td>0.87 (0.31)</td>
    </tr>
    <tr>
      <td>SAK1</td>
      <td>1.38 (0.08)</td>
      <td>1.29 (0.19)</td>
    </tr>
    <tr>
      <td>CFA1</td>
      <td>0.90 (0.04)</td>
      <td>1.44 (0.22)</td>
    </tr>
    <tr>
      <td>SOUL2</td>
      <td>1.17 (0.25)</td>
      <td>1.11 (0.19)</td>
    </tr>
    <tr>
      <td>MRP3†,‡</td>
      <td>1.13 (0.12)</td>
      <td>1.07 (0.25)</td>
    </tr>
    <tr>
      <td>Cre12.g503950†,‡</td>
      <td>0.93 (0.06)</td>
      <td>1.20 (0.12)</td>
    </tr>
    <tr>
      <td>Cre14.g613950†,§</td>
      <td>0.65 (0.06)</td>
      <td>0.79 (0.15)</td>
    </tr>
    <tr>
      <td>Cre04.g220850†,‡</td>
      <td>1.00 (0.09)</td>
      <td>1.29 (0.04)</td>
    </tr>
    <tr>
      <td>Cre09.g395750†,‡</td>
      <td>1.05 (0.10)</td>
      <td>1.29 (0.12)</td>
    </tr>
  </tbody>
</table>

_*Average of fold change and standard deviation (SD) of biological triplicates.†Annotated as transport function.‡ABC transporter.§Sec14-like phosphatidylinositol transfer protein._

Although only 33% of the up-regulated genes have a functional annotation (Figure 3B), it is interesting that the 1O2 response in Chlamydomonas involves genes and biological processes that appear to be distinct from those that respond specifically to 1O2 in Arabidopsis (op den Camp et al., 2003). A total of 70 1O2-response genes have been defined using a microarray with the flu mutant in Arabidopsis (op den Camp et al., 2003). These genes include the following classes (number of genes): metabolism (11), transcription (5), protein fate (4), transport (2), cellular communication/signal transduction (17), cell rescue/defense in virulence (4), subcellular localization (2), binding function or cofactor requirement (1), transport facilitation (5) and others (19). From this list of 70 genes we found four similarly annotated genes within our 515 genes induced by 1O2 in Chlamydomonas: a Myb transcription factor, a mitochondrial carrier protein, an amino acid permease, and an ATPase/aminophospholipid translocase. None of these genes in Chlamydomonas was the closest ortholog of the corresponding Arabidopsis gene. Conversely, genes similar to those strongly up-regulated in a SAK1-dependent manner such as CFAs, SOUL proteins, GPX, and sterol biosynthetic enzymes were not found among the Arabidopsis 1O2-specific genes despite having clear counterparts in Arabidopsis. Taken together, these results suggest that these two organisms may deploy distinct mechanisms in their responses to 1O2.

### The sak1 mutant is defective in the global gene expression response during acclimation to 1O2

In the sak1 mutant, 1020 genes were up-regulated, whereas 434 genes were down-regulated during acclimation (Supplementary file 1, C2). 350 of the 515 genes up-regulated in WT overlapped with the set of up-regulated genes in the mutant (Figure 3A). Comparing the fold changes of genes in WT and sak1 during acclimation, we defined 104 genes as SAK1-dependent genes that displayed moderate to strong attenuation in their response (fold change ratio <0.5) (Table 5). Some of the genes that belong to enriched biological classes found among WT up-regulated genes are indicated in Table 3. Interestingly, the most strongly induced genes in WT were found among this group; 37 out of 104 SAK1-dependent genes were among the top 10% most strongly induced genes (Table 5). 33 out of these 37 most strongly induced SAK1-dependent genes displayed strong disruption in their up-regulation; reduced to 0.01–0.25 of magnitude of fold change in sak1 as compared to WT (Table 5). These results indicate SAK1 is required for the induction of the most strongly induced genes during acclimation reflecting its critical role in regulating the cellular acclimation response to 1O2.

**Table 5.**
 Genes that require SAK1 for induction by 1O2


<table>
  <thead>
    <tr>
      <th>Gene ID (v4)</th>
      <th>Gene ID (v5)</th>
      <th>Gene name</th>
      <th>Annotation</th>
      <th>FC WT* (log2)</th>
      <th>FC sak1 (log2)</th>
      <th>Attenuation (FC-sak1/FC-WT)†</th>
      <th>Basal repression in sak1 (log2)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cre02.g137700.t1.1‡</td>
      <td>Cre09.g400404</td>
      <td></td>
      <td></td>
      <td>6.49</td>
      <td>1.80</td>
      <td>0.04</td>
      <td>−3.35</td>
    </tr>
    <tr>
      <td>Cre06.g281250.t1.1‡</td>
      <td>Cre06.g281250</td>
      <td>CFA1</td>
      <td>Cyclopropane fatty acid synthase</td>
      <td>5.92</td>
      <td>1.16</td>
      <td>0.04</td>
      <td>−2.10</td>
    </tr>
    <tr>
      <td>Cre27.g775950.t1.2</td>
      <td>Cre12.g557928</td>
      <td></td>
      <td></td>
      <td>5.83</td>
      <td>0.81</td>
      <td>0.03</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre01.g033300.t1.1</td>
      <td>Cre01.g033300</td>
      <td></td>
      <td></td>
      <td>5.72</td>
      <td>−0.39</td>
      <td>0.01</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre13.g566850.t1.1‡</td>
      <td>Cre13.g566850</td>
      <td>SOUL2</td>
      <td>SOUL heme-binding protein</td>
      <td>5.53</td>
      <td>1.33</td>
      <td>0.05</td>
      <td>−2.60</td>
    </tr>
    <tr>
      <td>Cre14.g623650.t1.1</td>
      <td>Cre14.g623650</td>
      <td></td>
      <td>Alcohol dehydrogenase</td>
      <td>4.89</td>
      <td>1.67</td>
      <td>0.11</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre13.g600650.t1.1</td>
      <td>Cre06.g278245</td>
      <td></td>
      <td>Rieske 2Fe-2S domain</td>
      <td>4.76</td>
      <td>1.64</td>
      <td>0.12</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre06.g263550.t1.1</td>
      <td>Cre06.g263550</td>
      <td>LCI7</td>
      <td>R53.5-related protein</td>
      <td>4.46</td>
      <td>1.77</td>
      <td>0.15</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre07.g342100.t1.1</td>
      <td>Cre07.g342100</td>
      <td></td>
      <td></td>
      <td>4.43</td>
      <td>1.40</td>
      <td>0.12</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre06.g299700.t1.1‡</td>
      <td>Cre06.g299700</td>
      <td>SOUL1</td>
      <td>SOUL heme-binding protein</td>
      <td>4.32</td>
      <td>0.43</td>
      <td>0.07</td>
      <td>−1.13</td>
    </tr>
    <tr>
      <td>Cre09.g398700.t1.1‡</td>
      <td>Cre09.g398700</td>
      <td>CFA2</td>
      <td>Cyclopropane fatty acid synthase</td>
      <td>4.05</td>
      <td>0.18</td>
      <td>0.07</td>
      <td>−1.00</td>
    </tr>
    <tr>
      <td>Cre12.g492650.t1.1‡</td>
      <td>Cre12.g492650</td>
      <td>FAS2</td>
      <td>Fasciclin-like protein</td>
      <td>4.01</td>
      <td>0.07</td>
      <td>0.07</td>
      <td>−1.24</td>
    </tr>
    <tr>
      <td>Cre08.g381510.t1.1</td>
      <td>NF</td>
      <td></td>
      <td></td>
      <td>3.94</td>
      <td>0.73</td>
      <td>0.11</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre10.g458450.t1.2</td>
      <td>Cre10.g458450</td>
      <td>GPX5</td>
      <td>Glutathione peroxidase</td>
      <td>3.91</td>
      <td>2.06</td>
      <td>0.28</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre11.g474600.t1.1</td>
      <td>Cre02.g095151</td>
      <td></td>
      <td>ABC transporter (ABC-2 type)</td>
      <td>3.90</td>
      <td>0.44</td>
      <td>0.09</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre13.g600700.t1.1</td>
      <td>Cre06.g278246</td>
      <td></td>
      <td></td>
      <td>3.78</td>
      <td>1.48</td>
      <td>0.20</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre14.g613950.t1.1</td>
      <td>Cre14.g613950</td>
      <td></td>
      <td></td>
      <td>3.65</td>
      <td>1.38</td>
      <td>0.21</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre06.g269300.t1.1</td>
      <td>Cre06.g269300</td>
      <td></td>
      <td>DUF1365</td>
      <td>3.50</td>
      <td>0.40</td>
      <td>0.12</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre08.g380300.t1.2</td>
      <td>Cre08.g380300</td>
      <td>MSRA3</td>
      <td>Peptide methionine sulfoxide reductase</td>
      <td>3.45</td>
      <td>0.66</td>
      <td>0.14</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre28.g776450.t1.1</td>
      <td>Cre08.g358573</td>
      <td>TRP7</td>
      <td>Transient receptor potential ion channel</td>
      <td>3.31</td>
      <td>−0.79</td>
      <td>0.06</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre01.g031650.t1.2</td>
      <td>Cre01.g031650</td>
      <td>CGLD12</td>
      <td>Potential galactosyl transferase activity</td>
      <td>3.30</td>
      <td>0.67</td>
      <td>0.16</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre14.g629061.t1.1</td>
      <td>NF</td>
      <td></td>
      <td>DUF2177</td>
      <td>3.25</td>
      <td>0.08</td>
      <td>0.11</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre12.g503950.t1.1</td>
      <td>Cre12.g503950</td>
      <td></td>
      <td>CRAL/TRIO domain</td>
      <td>3.24</td>
      <td>0.31</td>
      <td>0.13</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre13.g564900.t1.1</td>
      <td>Cre13.g564900</td>
      <td></td>
      <td>ABC transporter transmembrane region</td>
      <td>3.22</td>
      <td>0.34</td>
      <td>0.14</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre02.g139500.t1.1</td>
      <td>Cre09.g401701</td>
      <td></td>
      <td>DUF1295</td>
      <td>3.04</td>
      <td>−0.16</td>
      <td>0.11</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre14.g618400.t1.1</td>
      <td>Cre14.g618400</td>
      <td></td>
      <td></td>
      <td>2.97</td>
      <td>1.15</td>
      <td>0.28</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre17.g715150.t1.1</td>
      <td>Cre17.g715150</td>
      <td></td>
      <td></td>
      <td>2.89</td>
      <td>0.13</td>
      <td>0.15</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre17.g741300.t1.2‡</td>
      <td>Cre17.g741300</td>
      <td>SAK1</td>
      <td></td>
      <td>2.88</td>
      <td>0.66</td>
      <td>0.21</td>
      <td>−2.77</td>
    </tr>
    <tr>
      <td>Cre01.g007300.t1.1</td>
      <td>Cre01.g007300</td>
      <td></td>
      <td></td>
      <td>2.85</td>
      <td>−1.15</td>
      <td>0.06</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre16.g648700.t1.2‡</td>
      <td>Cre16.g648700</td>
      <td></td>
      <td>ABC transporter (ABC-2 type)</td>
      <td>2.79</td>
      <td>0.26</td>
      <td>0.17</td>
      <td>−1.26</td>
    </tr>
    <tr>
      <td>Cre13.g566900.t1.2</td>
      <td>Cre13.g566900</td>
      <td></td>
      <td></td>
      <td>2.76</td>
      <td>−0.38</td>
      <td>0.11</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre02.g137750.t1.2</td>
      <td>Cre09.g400441</td>
      <td></td>
      <td>JmjC domain</td>
      <td>2.72</td>
      <td>−0.31</td>
      <td>0.12</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre06.g263500.t1.1</td>
      <td>Cre06.g263500</td>
      <td></td>
      <td>Archease protein family (DUF101)</td>
      <td>2.67</td>
      <td>1.02</td>
      <td>0.32</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre01.g016150.t1.1‡</td>
      <td>Cre01.g016150</td>
      <td></td>
      <td>ADP-ribosylglycohydrolase</td>
      <td>2.65</td>
      <td>0.17</td>
      <td>0.18</td>
      <td>−1.26</td>
    </tr>
    <tr>
      <td>Cre08.g380000.t1.1</td>
      <td>Cre08.g380000</td>
      <td></td>
      <td>Formylglycine-generating sulfatase enzyme</td>
      <td>2.59</td>
      <td>1.53</td>
      <td>0.48</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre14.g615600.t1.1</td>
      <td>Cre14.g615600</td>
      <td></td>
      <td>Putative serine esterase (DUF676)</td>
      <td>2.53</td>
      <td>−0.54</td>
      <td>0.12</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre11.g472900.t1.2</td>
      <td>Cre02.g095113</td>
      <td></td>
      <td>CAP-Gly domain</td>
      <td>2.45</td>
      <td>−0.05</td>
      <td>0.18</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre06.g269250.t1.1</td>
      <td>Cre06.g269250</td>
      <td></td>
      <td></td>
      <td>2.44</td>
      <td>0.55</td>
      <td>0.27</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre02.g120600.t1.1</td>
      <td>Cre09.g403071</td>
      <td></td>
      <td></td>
      <td>2.44</td>
      <td>0.94</td>
      <td>0.35</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre06.g261200.t1.1</td>
      <td>Cre06.g261200</td>
      <td>ERG25</td>
      <td>Sterol desaturase</td>
      <td>2.42</td>
      <td>0.64</td>
      <td>0.29</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre16.g683400.t1.1</td>
      <td>Cre16.g683400</td>
      <td></td>
      <td>CRAL/TRIO domain</td>
      <td>2.40</td>
      <td>0.08</td>
      <td>0.20</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre22.g765150.t1.1</td>
      <td>Cre11.g467725</td>
      <td></td>
      <td>hypothetical protein</td>
      <td>2.30</td>
      <td>0.46</td>
      <td>0.28</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre13.g571800.t1.2</td>
      <td>Cre13.g571800</td>
      <td></td>
      <td>DUF1336</td>
      <td>2.27</td>
      <td>0.72</td>
      <td>0.34</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre13.g579450.t1.2</td>
      <td>Cre13.g579450</td>
      <td>CST1</td>
      <td>Membrane transporter</td>
      <td>2.27</td>
      <td>1.23</td>
      <td>0.49</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre08.g380350.t1.1</td>
      <td>Cre08.g380350</td>
      <td></td>
      <td></td>
      <td>2.21</td>
      <td>−0.01</td>
      <td>0.21</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre16.g649250.t1.2</td>
      <td>Cre16.g649250</td>
      <td></td>
      <td></td>
      <td>2.08</td>
      <td>0.58</td>
      <td>0.35</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre11.g476250.t1.1</td>
      <td>Cre11.g476250</td>
      <td></td>
      <td></td>
      <td>2.08</td>
      <td>0.49</td>
      <td>0.33</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre02.g108000.t1.2</td>
      <td>Cre02.g108000</td>
      <td></td>
      <td></td>
      <td>2.08</td>
      <td>1.03</td>
      <td>0.49</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre13.g583300.t1.1</td>
      <td>Cre13.g583300</td>
      <td></td>
      <td></td>
      <td>1.98</td>
      <td>−0.48</td>
      <td>0.18</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre04.g215300.t1.2</td>
      <td>NF</td>
      <td></td>
      <td></td>
      <td>1.97</td>
      <td>0.57</td>
      <td>0.38</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre02.g139450.t1.1</td>
      <td>Cre09.g401663</td>
      <td></td>
      <td>DUF947</td>
      <td>1.95</td>
      <td>−0.62</td>
      <td>0.17</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre03.g194750.t1.2</td>
      <td>Cre03.g194750</td>
      <td></td>
      <td></td>
      <td>1.95</td>
      <td>0.73</td>
      <td>0.43</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre06.g258600.t1.1</td>
      <td>Cre06.g258600</td>
      <td></td>
      <td>Dienelactone hydrolase family</td>
      <td>1.91</td>
      <td>−0.95</td>
      <td>0.14</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre10.g418700.t1.1</td>
      <td>Cre10.g418700</td>
      <td></td>
      <td>Probable N6-adenine methyltransferase</td>
      <td>1.87</td>
      <td>−0.03</td>
      <td>0.27</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre10.g444550.t1.1</td>
      <td>Cre10.g444550</td>
      <td>SPP1A</td>
      <td>Signal peptide peptidase</td>
      <td>1.81</td>
      <td>0.51</td>
      <td>0.41</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre01.g060050.t1.2</td>
      <td>Cre03.g145807</td>
      <td></td>
      <td></td>
      <td>1.78</td>
      <td>−0.11</td>
      <td>0.27</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre09.g410050.t1.1</td>
      <td>Cre09.g410050</td>
      <td></td>
      <td>Calcium transporting ATPase</td>
      <td>1.76</td>
      <td>0.51</td>
      <td>0.42</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre03.g163400.t1.2</td>
      <td>Cre03.g163400</td>
      <td></td>
      <td></td>
      <td>1.76</td>
      <td>−0.17</td>
      <td>0.26</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre01.g008450.t1.1</td>
      <td>Cre01.g008450</td>
      <td></td>
      <td>Nuf2 family</td>
      <td>1.73</td>
      <td>−0.54</td>
      <td>0.21</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre12.g536650.t1.1</td>
      <td>Cre12.g536650</td>
      <td></td>
      <td></td>
      <td>1.72</td>
      <td>0.35</td>
      <td>0.39</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre02.g114900.t1.2</td>
      <td>Cre02.g114900</td>
      <td>ANK23</td>
      <td>predicted protein</td>
      <td>1.71</td>
      <td>0.08</td>
      <td>0.32</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre16.g661850.t1.2</td>
      <td>Cre16.g661850</td>
      <td></td>
      <td>Calcium/calmoduline dependent protein kinase association</td>
      <td>1.69</td>
      <td>0.03</td>
      <td>0.32</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre14.g615500.t1.2</td>
      <td>Cre14.g615500</td>
      <td></td>
      <td>Glycoprotease family</td>
      <td>1.68</td>
      <td>−0.76</td>
      <td>0.18</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre11.g483100.t1.2</td>
      <td>Cre11.g483100</td>
      <td></td>
      <td>Protein kinase</td>
      <td>1.66</td>
      <td>−0.49</td>
      <td>0.22</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre28.g776650.t1.1</td>
      <td>Cre08.g358569</td>
      <td></td>
      <td></td>
      <td>1.64</td>
      <td>0.33</td>
      <td>0.40</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre07.g340250.t1.2</td>
      <td>Cre07.g340250</td>
      <td></td>
      <td>Protein kinase</td>
      <td>1.63</td>
      <td>−0.41</td>
      <td>0.24</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre06.g296250.t1.2</td>
      <td>Cre06.g296250</td>
      <td>SYK1</td>
      <td>tRNA synthetase, class II</td>
      <td>1.60</td>
      <td>0.54</td>
      <td>0.48</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre06.g310500.t1.1</td>
      <td>Cre06.g310500</td>
      <td></td>
      <td></td>
      <td>1.57</td>
      <td>0.18</td>
      <td>0.38</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre07.g342800.t1.2</td>
      <td>Cre07.g342800</td>
      <td>CGL16</td>
      <td>Predicted protein</td>
      <td>1.49</td>
      <td>0.32</td>
      <td>0.44</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre03.g181450.t1.2</td>
      <td>Cre03.g181450</td>
      <td></td>
      <td>DUF1619</td>
      <td>1.47</td>
      <td>0.35</td>
      <td>0.46</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre66.g793601.t1.1</td>
      <td>Cre35.g759497</td>
      <td></td>
      <td></td>
      <td>1.47</td>
      <td>0.03</td>
      <td>0.37</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre14.g614050.t1.2</td>
      <td>Cre14.g614050</td>
      <td>MAP65</td>
      <td>Microtubule associated protein</td>
      <td>1.43</td>
      <td>0.06</td>
      <td>0.39</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre04.g217500.t1.1</td>
      <td>Cre04.g217500</td>
      <td></td>
      <td>Inosine-uridine preferring nucleoside hydrolase</td>
      <td>1.42</td>
      <td>0.19</td>
      <td>0.43</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre06.g292950.t1.1</td>
      <td>Cre06.g292950</td>
      <td></td>
      <td>DNA polymerase delta, subunit 4</td>
      <td>1.38</td>
      <td>−0.12</td>
      <td>0.35</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre16.g661750.t1.1</td>
      <td>Cre16.g661750</td>
      <td></td>
      <td>Calcium/calmoduline dependent protein kinase association</td>
      <td>1.38</td>
      <td>−0.12</td>
      <td>0.35</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre01.g007000.t1.1</td>
      <td>Cre01.g007000</td>
      <td></td>
      <td>ABC transporter (ABC-2 type)</td>
      <td>1.35</td>
      <td>0.21</td>
      <td>0.45</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre04.g224400.t1.2</td>
      <td>Cre04.g224400</td>
      <td></td>
      <td>ABC transporter (ABC-2 type)</td>
      <td>1.34</td>
      <td>−0.13</td>
      <td>0.36</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre01.g068400.t1.2</td>
      <td>Cre16.g680790</td>
      <td></td>
      <td></td>
      <td>1.33</td>
      <td>0.16</td>
      <td>0.45</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre05.g237400.t1.1</td>
      <td>Cre05.g237400</td>
      <td>DAE1</td>
      <td>Diaminopimelate epimerase</td>
      <td>1.32</td>
      <td>0.22</td>
      <td>0.47</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre14.g609600.t1.2</td>
      <td>Cre14.g609600</td>
      <td></td>
      <td></td>
      <td>1.32</td>
      <td>−0.58</td>
      <td>0.27</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre05.g234850.t1.2</td>
      <td>Cre05.g234850</td>
      <td></td>
      <td>Ubiquitin carboxyl-terminal hydrolase</td>
      <td>1.29</td>
      <td>0.16</td>
      <td>0.46</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre03.g179200.t1.1</td>
      <td>Cre03.g179200</td>
      <td></td>
      <td></td>
      <td>1.28</td>
      <td>−0.48</td>
      <td>0.30</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre10.g417730.t1.1</td>
      <td>Cre10.g417730</td>
      <td></td>
      <td></td>
      <td>1.27</td>
      <td>0.17</td>
      <td>0.47</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre03.g159700.t1.2</td>
      <td>Cre03.g159700</td>
      <td></td>
      <td></td>
      <td>1.26</td>
      <td>−0.14</td>
      <td>0.38</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre12.g540150.t1.2</td>
      <td>Cre12.g540150</td>
      <td></td>
      <td></td>
      <td>1.19</td>
      <td>−0.24</td>
      <td>0.37</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre01.g006550.t1.2‡</td>
      <td>Cre01.g006550</td>
      <td></td>
      <td>No annotation</td>
      <td>1.17</td>
      <td>−0.49</td>
      <td>0.32</td>
      <td>−1.60</td>
    </tr>
    <tr>
      <td>Cre03.g159950.t1.2</td>
      <td>Cre03.g159950</td>
      <td></td>
      <td></td>
      <td>1.17</td>
      <td>−0.17</td>
      <td>0.40</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre27.g775900.t1.2</td>
      <td>Cre12.g557503</td>
      <td></td>
      <td></td>
      <td>1.14</td>
      <td>−0.70</td>
      <td>0.28</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre02.g121600.t1.1</td>
      <td>Cre09.g387208</td>
      <td></td>
      <td>Protein kinase</td>
      <td>1.14</td>
      <td>0.00</td>
      <td>0.46</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre14.g609550.t1.1</td>
      <td>NF</td>
      <td></td>
      <td></td>
      <td>1.13</td>
      <td>−0.84</td>
      <td>0.26</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre07.g315050.t1.2</td>
      <td>Cre07.g315050</td>
      <td></td>
      <td></td>
      <td>1.12</td>
      <td>−0.03</td>
      <td>0.45</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre04.g218800.t1.2</td>
      <td>Cre04.g218800</td>
      <td>THB3</td>
      <td>Truncated hemoglobin</td>
      <td>1.11</td>
      <td>−0.50</td>
      <td>0.33</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre02.g133300.t1.1</td>
      <td>Cre09.g396624</td>
      <td></td>
      <td></td>
      <td>1.11</td>
      <td>−0.43</td>
      <td>0.34</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre01.g060650.t1.2</td>
      <td>Cre03.g146067</td>
      <td></td>
      <td></td>
      <td>1.10</td>
      <td>−0.42</td>
      <td>0.35</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre01.g057050.t1.1</td>
      <td>Cre03.g144324</td>
      <td></td>
      <td></td>
      <td>1.10</td>
      <td>0.04</td>
      <td>0.48</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre06.g304950.t1.1</td>
      <td>Cre06.g304950</td>
      <td></td>
      <td></td>
      <td>1.07</td>
      <td>−0.65</td>
      <td>0.30</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre08.g358200.t1.2</td>
      <td>Cre08.g358200</td>
      <td>A4</td>
      <td>Protein kinase</td>
      <td>1.07</td>
      <td>−0.82</td>
      <td>0.27</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre16.g689550.t1.2</td>
      <td>Cre16.g689550</td>
      <td>PTK8</td>
      <td>Putative tyrosine kinase</td>
      <td>1.06</td>
      <td>−0.17</td>
      <td>0.43</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre17.g720950.t1.1</td>
      <td>Cre17.g720950</td>
      <td></td>
      <td>3-oxo-5-alpha-steroid 4-dehydrogenase</td>
      <td>1.05</td>
      <td>−0.26</td>
      <td>0.40</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre02.g090950.t1.2</td>
      <td>Cre02.g090950</td>
      <td></td>
      <td></td>
      <td>1.05</td>
      <td>−0.27</td>
      <td>0.40</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre16.g683350.t1.1</td>
      <td>Cre16.g683350</td>
      <td></td>
      <td></td>
      <td>1.03</td>
      <td>−0.67</td>
      <td>0.31</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre02.g109450.t1.1</td>
      <td>Cre02.g109450</td>
      <td></td>
      <td></td>
      <td>1.01</td>
      <td>−0.03</td>
      <td>0.48</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre16.g652750.t1.1</td>
      <td>Cre16.g652750</td>
      <td></td>
      <td></td>
      <td>1.01</td>
      <td>−0.29</td>
      <td>0.41</td>
      <td></td>
    </tr>
    <tr>
      <td>Cre03.g190000.t1.1</td>
      <td>Cre03.g190000</td>
      <td></td>
      <td></td>
      <td>1.00</td>
      <td>−0.99</td>
      <td>0.25</td>
      <td></td>
    </tr>
  </tbody>
</table>

_*Data were ordered by FC in WT.†Of the 52 most highly induced genes in WT (the top 10%), 37 were SAK1-dependent, and the induction of 33 of these genes was strongly attenuated to only 0.01-0.25 of magnitude of FC found in the WT. Dashed line indicates cutoff of FC for the top 10% most strongly induced genes.‡Genes that are repressed at basal level in sak1.NF, not found in v5._

Classes of up-regulated genes in sak1 were distinct from those of WT and included secondary metabolism of isoprenoids (Figure 3C; Table 6), precursors to photoprotective pigments such as carotenoids and tocopherols (Li et al., 2009). Phenylpropanoids, a group of metabolites associated with defense against stresses such as ultraviolet light and herbivores (Maeda and Dudareva, 2012), also represented a larger part of the response in sak1 as compared to WT (Figure 3C). Another mutant-specific class of genes was cell vesicular transport, suggesting alteration in cell organization in response to the loss of SAK1 (Figure 3C; Table 6). There were 434 genes that were down-regulated by 1O2 in the sak1 mutant (Supplementary file 1, C2), none of which overlapped with the set of down-regulated genes in WT, in contrast to the overlap of up-regulated genes in the two genotypes (Figure 3A). Enriched classes of genes included those involved in DNA, nucleotide metabolism, hormone metabolism (not of brassinosteroid) and tetrapyrrole metabolism (Figure 3C, Table 6).

**Table 6.**
 Enriched functional classes among differentially expressed genes in sak1 during 1O2 acclimation


<table>
  <thead>
    <tr>
      <th>Primary Mapman class</th>
      <th>Secondary Mapman class</th>
      <th>Gene ID (v4)</th>
      <th>Gene name</th>
      <th>Annotation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2">Up-regulated genes</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Secondary metabolism</td>
      <td>isoprenoids</td>
      <td>Cre13.g565650.t1.1</td>
      <td></td>
      <td>Geranylgeranyl pyrophosphate synthase/Polyprenyl synthetase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g267600.t1.1</td>
      <td></td>
      <td>Lycopene epsilon cyclase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre09.g407200.t1.1</td>
      <td></td>
      <td>Phytoene desaturase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g267600.t1.1</td>
      <td></td>
      <td>Lycopene epsilon cyclase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g011100.t1.1</td>
      <td></td>
      <td>Prenyltransferase and squalene oxidase repeat, Oxidosqualene-lanosterol cyclase and related proteins</td>
    </tr>
    <tr>
      <td></td>
      <td>N misc</td>
      <td>Cre08.g381707.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td>phenylpropanoids</td>
      <td>Cre03.g207800.t1.1</td>
      <td></td>
      <td>Alcohol dehydrogenase, class V</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre14.g623650.t1.1</td>
      <td></td>
      <td>Alcohol dehydrogenase, class V (Zinc-binding)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g039350.t1.1</td>
      <td></td>
      <td>Cytochrome P450 reductase, possibly CYP505B family</td>
    </tr>
    <tr>
      <td></td>
      <td>sulfur-containing</td>
      <td>Cre06.g299400.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td>wax</td>
      <td>Cre17.g722150.t1.1</td>
      <td>PKS3</td>
      <td>Type III polyketide synthase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g318500.t1.2</td>
      <td></td>
      <td>FAE1/Type III polyketide synthase-like protein, Chalcone and stilbene synthases</td>
    </tr>
    <tr>
      <td>Lipid metabolism</td>
      <td>‘exotics’ (steroids, squalene etc)</td>
      <td>Cre01.g061750.t1.1</td>
      <td></td>
      <td>serine palmitoyltransferase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g137850.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre83.g796250.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g011100.t1.1</td>
      <td></td>
      <td>Prenyltransferase and squalene oxidase repeat, Oxidosqualene-lanosterol cyclase and related proteins</td>
    </tr>
    <tr>
      <td></td>
      <td>FA synthesis and FA elongation</td>
      <td>Cre06.g256750.t1.1</td>
      <td></td>
      <td>Acyl carrier protein thioesterase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g182050.t1.1</td>
      <td></td>
      <td>Long-chain acyl-CoA synthetases (AMP-forming)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g074650.t1.1</td>
      <td></td>
      <td>Kelch repeat-containing proteins, Acyl-CoA binding protei</td>
    </tr>
    <tr>
      <td></td>
      <td>glycerol metabolism</td>
      <td>Cre01.g053000.t1.1</td>
      <td>GPD2</td>
      <td>Glycerol-3-phosphate dehydrogenase/dihydroxyacetone-3-phosphate reductase</td>
    </tr>
    <tr>
      <td></td>
      <td>glycolipid synthesis</td>
      <td>Cre13.g583600.t1.1</td>
      <td>DGD1</td>
      <td>Digalactosyldiacylglycerol synthase</td>
    </tr>
    <tr>
      <td></td>
      <td>lipid degradation</td>
      <td>Cre01.g057450.t1.2</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g126050.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td>phospholipid synthesis</td>
      <td>Cre06.g281250.t1.1</td>
      <td>CFA1</td>
      <td>Cyclopropane fatty acid synthase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g038250.t1.1</td>
      <td>SDC1</td>
      <td>Serine decarboxylase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre11.g472700.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre13.g604700.t1.2</td>
      <td></td>
      <td>CDP-alcohol phosphatidyltransferase/Phosphatidylglycerol-phosphate synthase</td>
    </tr>
    <tr>
      <td>Cell</td>
      <td>vesicle transport</td>
      <td>Cre18.g744100.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre17.g721900.t1.1</td>
      <td>COG5</td>
      <td>Component of oligomeric golgi complex</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g003050.t1.1</td>
      <td>SEC8</td>
      <td>Component of the Exocyst Complex</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre04.g224800.t1.1</td>
      <td></td>
      <td>Endosomal R-SNARE protein, Vamp7/Nyv1-family</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre17.g728150.t1.1</td>
      <td></td>
      <td>Endosomal R-SNARE protein, Yky6-family</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre12.g507450.t1.1</td>
      <td></td>
      <td>Trans-Golgi network Qa-SNARE protein, Syntaxin16/Syx16/Tlg2/Syp4-family</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g210600.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre04.g225900.t1.1</td>
      <td></td>
      <td>Endosomal R-SNARE protein, Vamp7/Nyv1-family</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g101400.t1.1</td>
      <td>CHC1</td>
      <td>Clathrin Heavy Chain</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre17.g709350.t1.1</td>
      <td></td>
      <td>Late endosomal Qc-SNARE protein, Syx8/Syntaxin8-family</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g342050.t1.1</td>
      <td></td>
      <td>Endosomal Qb-SNARE, Npsn-family</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g692050.t1.1</td>
      <td></td>
      <td>ER-Golgi Qa-SNARE protein, Syntaxin5/Syx5/Sed5/Syp3-family</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g676650.t1.1</td>
      <td>AP1G1</td>
      <td>Gamma1-Adaptin</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g099000.t1.1</td>
      <td></td>
      <td>Late endosomal Qc-SNARE protein, Syx6/Tlg1/Syp5/6-family</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre12.g554200.t1.2</td>
      <td></td>
      <td>ER-Golgi Qb-SNARE, Memb/GS35/Bos1-family</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g310000.t1.1</td>
      <td>AP4E1</td>
      <td>Epsilon4-Adaptin</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre10.g421250.t1.1</td>
      <td>EXO70</td>
      <td>Hypothetical Conserved Protein. Similar to Exo70, a subunit of the exocyst complex</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g330950.t1.1</td>
      <td>AP4S4</td>
      <td>Sigma4-Adaptin</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre12.g488850.t1.2</td>
      <td></td>
      <td>Adaptin, alpha/gamma/epsilon</td>
    </tr>
    <tr>
      <td></td>
      <td>division</td>
      <td>Cre06.g269950.t1.1</td>
      <td>CDC48</td>
      <td>Protein involved in ubiquitin-dependent degradation of ER-bound substrates</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre08.g359200.t1.2</td>
      <td></td>
      <td>Regulator of chromosome condensation (RCC1)</td>
    </tr>
    <tr>
      <td></td>
      <td>organisation</td>
      <td>Cre13.g588600.t1.2</td>
      <td></td>
      <td>Kinesin (SMY1 subfamily)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre12.g513450.t1.1</td>
      <td>TUH1</td>
      <td>Eta-Tubulin</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g010950.t1.2</td>
      <td></td>
      <td>26S proteasome regulatory complex, subunit PSMD10 (Ankyrin repeat)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g679650.t1.2</td>
      <td></td>
      <td>Fimbrin/Plastin</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g261950.t1.1</td>
      <td></td>
      <td>Myotrophin and similar proteins (Ankyrin repeat)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g291700.t1.1</td>
      <td>RSP3</td>
      <td>Radial spoke protein 3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre10.g446700.t1.1</td>
      <td>ANK28</td>
      <td>Ankyrin repeat and DHHC-type Zn-finger domain containing proteins</td>
    </tr>
    <tr>
      <td>Hormone metabolism†</td>
      <td>abscisic acid</td>
      <td>Cre16.g657800.t1.2</td>
      <td>CCD3</td>
      <td>Carotenoid cleavage dioxygenase</td>
    </tr>
    <tr>
      <td></td>
      <td>auxin</td>
      <td>Cre14.g609900.t1.1</td>
      <td></td>
      <td>Predicted membrane protein, contains DoH and Cytochrome b-561/ferric reductase transmembrane domains</td>
    </tr>
    <tr>
      <td></td>
      <td>brassinosteroid</td>
      <td>Cre16.g663950.t1.1</td>
      <td></td>
      <td>Sterol C5 desaturase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g092350.t1.1</td>
      <td></td>
      <td>Cytochrome P450, CYP51 superfamily; sterol 14 desaturase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre12.g557900.t1.1</td>
      <td>CDI1</td>
      <td>C-8,7 sterol isomerase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g076800.t1.1</td>
      <td></td>
      <td>Delta14-sterol reductase, mitochondrial</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre12.g500500.t1.2</td>
      <td></td>
      <td>24-methylenesterol C-methyltransferase</td>
    </tr>
    <tr>
      <td></td>
      <td>ethylene</td>
      <td>Cre02.g108450.t1.1</td>
      <td>FAP280</td>
      <td>Flagellar Associated Protein, transcriptional coactivator-like, putative transcription factor</td>
    </tr>
    <tr>
      <td></td>
      <td>jasmonate</td>
      <td>Cre19.g756100.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td>Misc</td>
      <td>acid and other phosphatases</td>
      <td>Cre09.g396900.t1.1</td>
      <td></td>
      <td>NADH pyrophosphatase I of the Nudix family of hydrolases</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g259650.t1.1</td>
      <td></td>
      <td>Calcineurin-like phosphoesterase, Acid-phosphatase-related</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g249800.t1.1</td>
      <td></td>
      <td>Sphingomyelin synthetase -related</td>
    </tr>
    <tr>
      <td></td>
      <td>cytochrome P450</td>
      <td>Cre05.g234100.t1.1</td>
      <td></td>
      <td>Cytochrome P450, CYP197 superfamily</td>
    </tr>
    <tr>
      <td></td>
      <td>dynamin</td>
      <td>Cre02.g079550.t1.1</td>
      <td>DRP2</td>
      <td>Dynamin-related GTPase, involved in circadian rhythms</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre05.g245950.t1.1</td>
      <td>DRP1</td>
      <td>Dynamin-related GTPase</td>
    </tr>
    <tr>
      <td></td>
      <td>glutathione S transferases</td>
      <td>Cre03.g154950.t1.1</td>
      <td></td>
      <td>Glutathione S-transferase</td>
    </tr>
    <tr>
      <td></td>
      <td>misc2</td>
      <td>Cre12.g538450.t1.1</td>
      <td>EPT1</td>
      <td>CDP-Etn:DAG Ethanolamine phosphotransferase</td>
    </tr>
    <tr>
      <td></td>
      <td>short chain dehydrogenase/reductase (SDR)</td>
      <td>Cre12.g556750.t1.2</td>
      <td></td>
      <td>Short-chain dehydrogenase/reductase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre08.g384864.t1.1</td>
      <td></td>
      <td>SH3 domain, protein binding</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre27.g775000.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre17.g731350.t1.2</td>
      <td></td>
      <td>Short chain dehydrogenase</td>
    </tr>
    <tr>
      <td></td>
      <td>UDP glucosyl and glucoronyl transferases</td>
      <td>Cre02.g111150.t1.2</td>
      <td>ELG26</td>
      <td>Exostosin-like glycosyltransferase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g144050.t1.1</td>
      <td></td>
      <td>Acetylglucosaminyltransferase EXT1/exostosin 1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g204050.t1.2</td>
      <td>ELG6</td>
      <td>Exostosin-like glycosyltransferases</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre11.g474450.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g173300.t1.1</td>
      <td></td>
      <td>Lactosylceramide 4-alpha-galactosyltransferase (alpha- 1,4-galactosyltransferase)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g116600.t1.1</td>
      <td>ELG23</td>
      <td>Exostosin-like glycosyltransferase</td>
    </tr>
    <tr>
      <td colspan="2">Down-regulated genes</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Hormone metabolism†</td>
      <td>cytokinin</td>
      <td>Cre18.g744950.t1.2</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g678900.t1.1</td>
      <td></td>
      <td>Response regulator receiver domain</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g040450.t1.1</td>
      <td>HDT1</td>
      <td>Histidine-aspartic acid phosphotransferase 1 (phosphorylation cascade)</td>
    </tr>
    <tr>
      <td></td>
      <td>ethylene</td>
      <td>Cre09.g403550.t1.1</td>
      <td></td>
      <td>Iron/ascorbate family oxidoreductases</td>
    </tr>
    <tr>
      <td>Nucleotide metabolism</td>
      <td>deoxynucleotide metabolism</td>
      <td>Cre12.g491050.t1.1</td>
      <td>RIR2</td>
      <td>Ribonucleotide reductase (RNR), small subunit</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre12.g492950.t1.1</td>
      <td>RIR1</td>
      <td>Ribonucleotide reductase (RNR), large subunit, class I</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g667850.t1.1</td>
      <td></td>
      <td>dUTP pyrophosphatase</td>
    </tr>
    <tr>
      <td></td>
      <td>synthesis</td>
      <td>Cre14.g614300.t1.1</td>
      <td></td>
      <td>Inosine-5-monophosphate dehydrogenase/GMP reductase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g318750.t1.1</td>
      <td></td>
      <td>Phosphoribosylformylglycinamidine cyclo-ligase</td>
    </tr>
    <tr>
      <td>Tetrapyrrole synthesis</td>
      <td>porphobilinogen deaminase</td>
      <td>Cre16.g663900.t1.1</td>
      <td></td>
      <td>Porphobilinogen deaminase</td>
    </tr>
    <tr>
      <td></td>
      <td>protochlorophyllide reductase</td>
      <td>Cre01.g015350.t1.1</td>
      <td></td>
      <td>Light-dependent protochlorophyllide reductase</td>
    </tr>
    <tr>
      <td></td>
      <td>urogen III methylase</td>
      <td>Cre02.g133050.t1.2</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td>DNA</td>
      <td>repair</td>
      <td>Cre16.g670550.t1.2</td>
      <td></td>
      <td>XP-G/RAD2 DNA repair endonuclease</td>
    </tr>
    <tr>
      <td></td>
      <td>synthesis/chromatin structure</td>
      <td>Cre07.g338000.t1.1</td>
      <td>MCM2</td>
      <td>Minichromosome maintenance protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g314900.t1.2</td>
      <td></td>
      <td>ATP-dependent RNA helicase, DEAD/DEAH helicase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g172950.t1.1</td>
      <td>CBF5</td>
      <td>Centromere/microtubule binding protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g015250.t1.1</td>
      <td></td>
      <td>Eukaryotic DNA polymerase delta</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre27.g774200.t1.2</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g316850.t1.1</td>
      <td>MCM4</td>
      <td>Minichromosome maintenance protein</td>
    </tr>
    <tr>
      <td></td>
      <td>unspecified</td>
      <td>Cre10.g451250.t1.2</td>
      <td></td>
      <td>Adenylate and guanylate cyclase catalytic domain, 3-5 exonuclease</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g059950.t1.2</td>
      <td></td>
      <td>NF*</td>
    </tr>
  </tbody>
</table>

_*Corresponding gene model was not found in v5.†Functional terms are inferred by homology to the annotation set of Arabidopsis thaliana (Lopez et al., 2011)._

To better understand the physiology of sak1, including the primary and secondary effects of lacking SAK1, we also focused on changes in transcript levels at the basal level, that is, without 1O2 treatment. At basal level 699 genes were induced, and 737 genes were repressed in the mutant compared to WT (Supplementary file 1, C3), displaying the genome-wide response to the loss of SAK1 function despite the mutant’s wild-type appearance under normal lab growth conditions (Figure 1D). The enriched classes of genes that are differentially expressed are shown in Figure 3D. Genes induced in the mutant at basal level were enriched for those annotated to be involved in nucleotide metabolism, DNA, and RNA (Figure 3D; Table 7). Interestingly genes involved in tetrapyrrole and photosynthesis were enriched both in elevated and repressed genes at the basal level in sak1. There was no overall trend of these two pathways being up- or down-regulated, since these genes were at different steps of the pathway or encoded a select isoform of an enzyme or a subunit of a complex (Figure 3D; Table 7).

**Table 7.**
 Enriched functional classes among differentially expressed genes in sak1 at basal level


<table>
  <thead>
    <tr>
      <th>Primary Mapman class</th>
      <th>Secondary Mapman class</th>
      <th>Gene ID (v4)</th>
      <th>Gene name</th>
      <th>Annotation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Elevated in sak1</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>nucleotide metabolism</td>
      <td>deoxynucleotide metabolism</td>
      <td>Cre12.g491050.t1.1</td>
      <td>RIR2</td>
      <td>Ribonucleotide reductase (RNR), small subunit</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre12.g492950.t1.1</td>
      <td>RIR1</td>
      <td>Ribonucleotide reductase (RNR), large subunit, class I</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g667850.t1.1</td>
      <td></td>
      <td>dUTP pyrophosphatase</td>
    </tr>
    <tr>
      <td></td>
      <td>phosphotransfer and pyrophosphatases</td>
      <td>Cre02.g122450.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g093950.t1.1</td>
      <td>PYR5</td>
      <td>Uridine 5'- monophosphate synthase/orotate phosphoribosyltransferase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre12.g519950.t1.1</td>
      <td></td>
      <td>Flagellar Associated Protein similar to adenylate/guanylate kinases</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre26.g772450.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td>synthesis</td>
      <td>Cre65.g793400.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g079700.t1.1</td>
      <td>PYR2</td>
      <td>Aspartate carbamoyltransferase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g048950.t1.1</td>
      <td></td>
      <td>dUTP pyrophosphatase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g318750.t1.1</td>
      <td></td>
      <td>Phosphoribosylformylglycinamidine cyclo-ligase.</td>
    </tr>
    <tr>
      <td>DNA</td>
      <td>repair</td>
      <td>Cre07.g314650.t1.1</td>
      <td></td>
      <td>Chloroplast RecA recombination protein</td>
    </tr>
    <tr>
      <td></td>
      <td>synthesis/chromatin structure</td>
      <td>Cre04.g214350.t1.2</td>
      <td></td>
      <td>Eukaryotic DNA polymerase alpha, catalytic subunit</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g314900.t1.2</td>
      <td></td>
      <td>ATP-dependent RNA helicase (DEAD/DEAH)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre04.g223850.t1.1</td>
      <td></td>
      <td>Cytoplasmic DExD/H-box RNA helicase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g015250.t1.1</td>
      <td></td>
      <td>Eukaryotic DNA polymerase delta, catalytic subunit.</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g342506.t1.1</td>
      <td></td>
      <td>Ubiquitin-protein ligase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g338000.t1.1</td>
      <td>MCM2</td>
      <td>Minichromosome maintenance protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g178650.t1.1</td>
      <td>MCM6</td>
      <td>MCM6 DNA replication protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g312350.t1.2</td>
      <td></td>
      <td>DNA polymerase alpha, primase subunit</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g009250.t1.2</td>
      <td>TOP2</td>
      <td>DNA topoisomerase II</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre26.g772150.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g316850.t1.1</td>
      <td>MCM4</td>
      <td>Minichromosome maintenance protein 4</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g263800.t1.2</td>
      <td></td>
      <td>tRNA-splicing endonuclease positive effector (SEN1)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g295700.t1.2</td>
      <td>MCM3</td>
      <td>Minichromosome maintenance protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g251800.t1.1</td>
      <td>RFC4</td>
      <td>DNA replication factor C complex subunit 4</td>
    </tr>
    <tr>
      <td></td>
      <td>unspecified</td>
      <td>Cre07.g322300.t1.2</td>
      <td></td>
      <td>DNA repair helicase of the DEAD superfamily</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre17.g718100.t1.1</td>
      <td></td>
      <td>Phosphatidylinositol transfer protein SEC14 and related proteins (CRAL/TRIO)</td>
    </tr>
    <tr>
      <td>Tetrapyrrole synthesis</td>
      <td>Glu-tRNA reductase</td>
      <td>Cre07.g342150.t1.1</td>
      <td>HEM1</td>
      <td>Glutamyl-tRNA reductase</td>
    </tr>
    <tr>
      <td></td>
      <td>Glu-tRNA synthetase</td>
      <td>Cre44.g788000.t1.1</td>
      <td></td>
      <td>Glutamyl-tRNA reductase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g306300.t1.1</td>
      <td>CHLI1</td>
      <td>Magnesium chelatase subunit I</td>
    </tr>
    <tr>
      <td></td>
      <td>magnesium chelatase</td>
      <td>Cre07.g325500.t1.1</td>
      <td></td>
      <td>Magnesium chelatase subunit H</td>
    </tr>
    <tr>
      <td></td>
      <td>protochlorophyllide reductase</td>
      <td>Cre01.g015350.t1.1</td>
      <td>POR1</td>
      <td>Light-dependent protochlorophyllide reductase</td>
    </tr>
    <tr>
      <td>Photosynthesis</td>
      <td>Calvin-Benson cycle</td>
      <td>Cre05.g234550.t1.1</td>
      <td></td>
      <td>Fructose-biphosphate aldolase</td>
    </tr>
    <tr>
      <td></td>
      <td>light reaction</td>
      <td>Cre07.g330250.t1.1</td>
      <td>PSAH</td>
      <td>Subunit H of photosystem I</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g334550.t1.1</td>
      <td></td>
      <td>Photosystem I subunit PsaO</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g261000.t1.1</td>
      <td>PSBR</td>
      <td>10 kDa photosystem II polypeptide</td>
    </tr>
    <tr>
      <td></td>
      <td>photorespiration</td>
      <td>Cre12.g542300.t1.1</td>
      <td>GYK1</td>
      <td>Glycerate kinase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g253350.t1.1</td>
      <td>GCSH</td>
      <td>Glycine cleavage system, H-protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g293950.t1.1</td>
      <td>SHMT2</td>
      <td>Serine hydroxymethyltransferase 2</td>
    </tr>
    <tr>
      <td>Transport</td>
      <td>ABC transporters and multidrug resistance systems</td>
      <td>Cre04.g222700.t1.1</td>
      <td></td>
      <td>ATPase component of ABC transporters with duplicated ATPase domains/Translation elongation factor EF-3b</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre17.g728400.t1.2</td>
      <td></td>
      <td>ABCtransporter (ABC-2 type)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre05.g241350.t1.2</td>
      <td></td>
      <td>ABCtransporter (ABC-2 type)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g169300.t1.1</td>
      <td></td>
      <td>ABCtransporter (ABC-2 type)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre11.g474600.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td>amino acids</td>
      <td>Cre04.g226150.t1.2</td>
      <td>AOC1</td>
      <td>Amino acid carrier 1; belongs to APC (Amino acid Polyamine organo Cation) family</td>
    </tr>
    <tr>
      <td></td>
      <td>calcium</td>
      <td>Cre09.g388850.t1.1</td>
      <td>ACA1</td>
      <td>P-type ATPase/cation transporter, plasma membrane</td>
    </tr>
    <tr>
      <td></td>
      <td>metabolite transporters at the envelope membrane</td>
      <td>Cre06.g263850.t1.2</td>
      <td>TPT2</td>
      <td>Triose phosphate/phosphate translocator</td>
    </tr>
    <tr>
      <td></td>
      <td>metabolite transporters at the mitochondrial membrane</td>
      <td>Cre10.g449100.t1.1</td>
      <td></td>
      <td>Mitochondrial oxodicarboxylate carrier protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g069350.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre15.g641200.t1.1</td>
      <td></td>
      <td>Mitochondrial fatty acid anion carrier protein/Uncoupling protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre09.g396350.t1.1</td>
      <td></td>
      <td>Mitochondrial carrier protein PET8</td>
    </tr>
    <tr>
      <td></td>
      <td>misc</td>
      <td>Cre06.g311000.t1.2</td>
      <td>FBT2</td>
      <td>Folate transporte</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre17.g718100.t1.1</td>
      <td></td>
      <td>Phosphatidylinositol transfer protein SEC14 and related proteins (CRAL/TRIO)</td>
    </tr>
    <tr>
      <td></td>
      <td>phosphate</td>
      <td>Cre16.g686750.t1.1</td>
      <td>PTA3</td>
      <td>Proton/phosphate symporter</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g675300.t1.2</td>
      <td></td>
      <td>Sodium-dependent phosphate transporter, major facilitator superfamily</td>
    </tr>
    <tr>
      <td></td>
      <td>potassium</td>
      <td>Cre12.g553450.t1.2</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td>sulphate</td>
      <td>Cre17.g723350.t1.1</td>
      <td>SUL2</td>
      <td>Sulfate anion transporter</td>
    </tr>
    <tr>
      <td></td>
      <td>unspecified cations</td>
      <td>Cre13.g573900.t1.1</td>
      <td></td>
      <td>Na+:iodide/myo-inositol/multivitamin symporters</td>
    </tr>
    <tr>
      <td></td>
      <td>sugars</td>
      <td>Cre16.g675300.t1.2</td>
      <td></td>
      <td>Sodium-dependent phosphate transporter, major facilitator superfamily</td>
    </tr>
    <tr>
      <td>RNA</td>
      <td>processing</td>
      <td>Cre10.g427700.t1.1</td>
      <td></td>
      <td>ATP-dependent RNA helicase, DEAD/DEAH box helicase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre12.g538750.t1.1</td>
      <td>LSM1</td>
      <td>U6 snRNA-associated Sm-like protein LSm1, RNA cap binding; (SMP6d)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre10.g433750.t1.2</td>
      <td>PAP1</td>
      <td>Nuclear poly(A) polymerase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g182950.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre08.g375128.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td>regulation of transcription</td>
      <td>Cre17.g728200.t1.2</td>
      <td></td>
      <td>YL-1 protein (transcription factor-like 1)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g275500.t1.1</td>
      <td></td>
      <td>AP2 Transcription factor</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre28.g777500.t1.2</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre13.g572450.t1.1</td>
      <td></td>
      <td>Response regulator receiver domain (sensor histidine kinase-related, regulation of transcription)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre14.g620500.t1.1</td>
      <td></td>
      <td>AP2 Transcription factor</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g673150.t1.1</td>
      <td></td>
      <td>Histone deacetylase complex, catalytic component RPD3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g078700.t1.2</td>
      <td></td>
      <td>DNA damage-responsive repressor GIS1/RPH1, jumonji superfamily</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g198800.t1.1</td>
      <td></td>
      <td>Myb-like DNA-binding domain</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre04.g218050.t1.2</td>
      <td></td>
      <td>RWP-RK domain</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g324400.t1.1</td>
      <td>VPS24</td>
      <td>Subunit of the ESCRT-III complex, vaculoar sortin protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre11.g481050.t1.1</td>
      <td></td>
      <td>SWI/SNF-related chromatin binding protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g101950.t1.1</td>
      <td>TMU2</td>
      <td>tRNA (uracil-5)-methyltransferase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre10.g459600.t1.2</td>
      <td></td>
      <td>CAATT-binding transcription factor/60S ribosomal subunit biogenesis protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g018650.t1.2</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g012200.t1.2</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g129750.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre10.g461750.t1.2</td>
      <td></td>
      <td>DNA (cytosine-5-)-methyltransferase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g004600.t1.2</td>
      <td>RWP12</td>
      <td>Putative RWP-RK domain transcription factor</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre09.g400100.t1.1</td>
      <td></td>
      <td>Predicted Zn-finger protein, zinc and DNA binding domains</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g335150.t1.2</td>
      <td></td>
      <td>SBP domain</td>
    </tr>
    <tr>
      <td></td>
      <td>RNA binding</td>
      <td>Cre16.g662700.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g330300.t1.1</td>
      <td></td>
      <td>RNA-binding protein musashi/mRNA cleavage and polyadenylation factor I complex, subunit HRP1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g275100.t1.1</td>
      <td></td>
      <td>RNA-binding protein musashi/mRNA cleavage and polyadenylation factor I complex, subunit HRP1</td>
    </tr>
    <tr>
      <td></td>
      <td>transcription</td>
      <td>Cre07.g322200.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Repressed in sak1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Transport</td>
      <td>ABC transporters and multidrug resistance systems</td>
      <td>Cre02.g097800.t1.2</td>
      <td></td>
      <td>ABC transporter (MDR)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre17.g725200.t1.1</td>
      <td></td>
      <td>ABC transporter, peptide exporter</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre13.g580300.t1.1</td>
      <td></td>
      <td>ABC transporter family protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre10.g439000.t1.2</td>
      <td></td>
      <td>Long-chain acyl-CoA transporter, ABC superfamily (involved in peroxisome organization and biogenesis)</td>
    </tr>
    <tr>
      <td></td>
      <td>amino acids</td>
      <td>Cre06.g292350.t1.1</td>
      <td>AOC4</td>
      <td>Amino acid carrier</td>
    </tr>
    <tr>
      <td></td>
      <td>calcium</td>
      <td>Cre06.g263950.t1.2</td>
      <td></td>
      <td>Sodium/potassium-transporting ATPase subunit alpha</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g681750.t1.2</td>
      <td></td>
      <td>Calcium transporting ATPase</td>
    </tr>
    <tr>
      <td></td>
      <td>metabolite transporters at the mitochondrial membrane</td>
      <td>Cre03.g172300.t1.1</td>
      <td></td>
      <td>Mitochondrial phosphate carrier protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre09.g394800.t1.2</td>
      <td></td>
      <td>Mitochondrial substrate carrier protein</td>
    </tr>
    <tr>
      <td></td>
      <td>metal</td>
      <td>Cre03.g189550.t1.2</td>
      <td>ZIP3</td>
      <td>Zinc transporter, ZIP family</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre11.g479600.t1.2</td>
      <td></td>
      <td>Sodium/calcium exchanger NCX1 and related proteins</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g281900.t1.1</td>
      <td>ZIP7</td>
      <td>Zinc transporter and related ZIP domain-containing proteins</td>
    </tr>
    <tr>
      <td></td>
      <td>misc</td>
      <td>Cre02.g089900.t1.1</td>
      <td></td>
      <td>Secretory carrier membrane protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre10.g448050.t1.1</td>
      <td></td>
      <td>Retinaldehyde binding protein-related (CRAL/TRIO domain)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g177750.t1.2</td>
      <td></td>
      <td>Multidrug resistance pump</td>
    </tr>
    <tr>
      <td></td>
      <td>NDP-sugars at the ER</td>
      <td>Cre02.g112900.t1.1</td>
      <td></td>
      <td>GDP-fucose transporter (Triose-phosphate transporter family)</td>
    </tr>
    <tr>
      <td></td>
      <td>P- and V-ATPases</td>
      <td>Cre01.g027800.t1.1</td>
      <td>ATPvH</td>
      <td>Vacuolar ATP synthase subunit H</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre10.g446550.t1.1</td>
      <td>ATPvF</td>
      <td>Vacuolar ATP synthase subunit F</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g176250.t1.1</td>
      <td>ATPvD1</td>
      <td>Vacuolar ATP synthase subunit D</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g250250.t1.1</td>
      <td>ATPvC</td>
      <td>Vacuolar ATP synthase subunit C</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre10.g459200.t1.1</td>
      <td>ACA4</td>
      <td>P-type ATPase/cation transporter, plasma membrane (Low CO2 inducible gene)</td>
    </tr>
    <tr>
      <td></td>
      <td>phosphate</td>
      <td>Cre12.g515750.t1.2</td>
      <td></td>
      <td>Sodium-dependent phosphate transporter-related</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre08.g379550.t1.2</td>
      <td></td>
      <td>Sodium-dependent phosphate transporter, major facilitator superfamily</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre12.g489400.t1.1</td>
      <td>PTB7</td>
      <td>Putative phosphate transporter, sodium/phosphate transporter</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g144650.t1.1</td>
      <td>PTB12</td>
      <td>Sodium/phosphate symporter</td>
    </tr>
    <tr>
      <td></td>
      <td>unspecified anions</td>
      <td>Cre09.g404100.t1.1</td>
      <td></td>
      <td>Cl- channel CLC-7 and related proteins (CLC superfamily)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre17.g729450.t1.1</td>
      <td></td>
      <td>Cl- channel CLC-7 and related proteins (CLC superfamily)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g037150.t1.2</td>
      <td></td>
      <td>Voltage-gated chloride channel activity</td>
    </tr>
    <tr>
      <td></td>
      <td>sugars</td>
      <td>Cre03.g206800.t1.2</td>
      <td>HXT1</td>
      <td>Hexose transporter</td>
    </tr>
    <tr>
      <td></td>
      <td>P- and V-ATPases</td>
      <td>Cre03.g176250.t1.1</td>
      <td>ATPvD1</td>
      <td>Vacuolar ATP synthase subunit D</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre10.g446550.t1.1</td>
      <td>ATPvF</td>
      <td>Vacuolar ATP synthase subunit F</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g027800.t1.1</td>
      <td>ATPvH</td>
      <td>Vacuolar ATP synthase subunit H</td>
    </tr>
    <tr>
      <td>Mitochondrial electron transport / ATP synthesis</td>
      <td>cytochrome c reductase</td>
      <td>Cre01.g051900.t1.1</td>
      <td>RIP1</td>
      <td>Rieske iron-sulfur protein of mitochondrial ubiquinol-cytochrome c reductase (complex III)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g262700.t1.2</td>
      <td></td>
      <td>Ubiquinol cytochrome c reductase, subunit 7</td>
    </tr>
    <tr>
      <td></td>
      <td>F1-ATPase</td>
      <td>Cre02.g116750.t1.2</td>
      <td></td>
      <td>F0F1-type ATP synthase, alpha subunit</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g018800.t1.1</td>
      <td>ATP6</td>
      <td>Mitochondrial F1F0 ATP synthase subunit 6</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre10.g420700.t1.1</td>
      <td></td>
      <td>Mitochondrial F1F0-ATP synthase, subunit epsilon/ATP15</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g680000.t1.1</td>
      <td>ATP5</td>
      <td>Mitochondrial ATP synthase subunit 5, OSCP subunit</td>
    </tr>
    <tr>
      <td></td>
      <td>NADH-DH</td>
      <td>Cre10.g434450.t1.1</td>
      <td>NUOA9</td>
      <td>Putative NADH:ubiquinone oxidoreductase (Complex I) 39 kDa subunit</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre08.g378900.t1.1</td>
      <td>NUO3</td>
      <td>NADH:ubiquinone oxidoreductase ND3 subunit</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre10.g450400.t1.1</td>
      <td>NUO5</td>
      <td>NADH:ubiquinone oxidoreductase (Complex I) 24 kD subunit</td>
    </tr>
    <tr>
      <td>Lipid metabolism</td>
      <td>'exotics' (steroids, squalene etc)</td>
      <td>Cre14.g615050.t1.1</td>
      <td></td>
      <td>3-oxo-5-alpha-steroid 4-dehydrogenase, Steroid reductase required for elongation of the VLCFAs (enoyl reductase)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre12.g530550.t1.2</td>
      <td>KDG2</td>
      <td>Diacylglycerol kinase, sphingosine kinase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g137850.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td>FA desaturation</td>
      <td>Cre17.g711150.t1.1</td>
      <td></td>
      <td>Omega-6 fatty acid desaturase (delta-12 desaturase)</td>
    </tr>
    <tr>
      <td></td>
      <td>glyceral metabolism</td>
      <td>Cre13.g577450.t1.2</td>
      <td></td>
      <td>Glycerol-3-phosphate dehydrogenase</td>
    </tr>
    <tr>
      <td></td>
      <td>glycolipid synthesis</td>
      <td>Cre13.g583600.t1.1</td>
      <td>DGD1</td>
      <td>Digalactosyldiacylglycerol synthase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g656400.t1.1</td>
      <td>SQD1</td>
      <td>UDP-sulfoquinovose synthase</td>
    </tr>
    <tr>
      <td></td>
      <td>lipid degradation</td>
      <td>Cre06.g252801.t1.2</td>
      <td></td>
      <td>CGI-141-related/lipase containing protein (TAG lipase)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g164350.t1.2</td>
      <td></td>
      <td>Lysophospholipase, putative drug exporter of the RND superfamily</td>
    </tr>
    <tr>
      <td></td>
      <td>phospholipid synthesis</td>
      <td>Cre06.g281250.t1.1</td>
      <td>CFA1</td>
      <td>Cyclopropane fatty acid synthase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre09.g398700.t1.1</td>
      <td>CFA2</td>
      <td>Cyclopropane fatty acid synthase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre11.g472700.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g262550.t1.1</td>
      <td></td>
      <td>Zinc finger MYND domain containing protein 10</td>
    </tr>
    <tr>
      <td>Photosynthesis</td>
      <td>Calvin-Benson cycle</td>
      <td>Cre12.g511900.t1.1</td>
      <td>RPE1</td>
      <td>Ribulose phosphate-3-epimerase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre02.g120100.t1.1</td>
      <td>RBCS1</td>
      <td>Ribulose-1,5-bisphosphate carboxylase/oxygenase small subunit 1</td>
    </tr>
    <tr>
      <td></td>
      <td>light reaction</td>
      <td>Cre05.g243800.t1.1</td>
      <td>CPLD45</td>
      <td>Photosystem II Psb27 protein</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre10.g420350.t1.1</td>
      <td>PSAE</td>
      <td>Photosystem I reaction center subunit IV</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre01.g071450.t1.2</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g291650.t1.1</td>
      <td></td>
      <td>Ferredoxin</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre05.g242400.t1.1</td>
      <td></td>
      <td>No functional annotation</td>
    </tr>
    <tr>
      <td></td>
      <td>photorespiration</td>
      <td>Cre09.g411900.t1.2</td>
      <td>SHMT3</td>
      <td>Serine hydroxymethyltransferase 3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre06.g295450.t1.1</td>
      <td>HPR1</td>
      <td>Hydroxypyruvate reductase</td>
    </tr>
    <tr>
      <td>Major CHO metabolism</td>
      <td>degradation</td>
      <td>Cre09.g415600.t1.2</td>
      <td></td>
      <td>Starch binding domain</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre11.g473500.t1.2</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre09.g415600.t1.2</td>
      <td></td>
      <td>Starch binding domain</td>
    </tr>
    <tr>
      <td></td>
      <td>synthesis</td>
      <td>Cre06.g289850.t1.2</td>
      <td>SBE1</td>
      <td>Starch Branching Enzyme</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre17.g721500.t1.1</td>
      <td></td>
      <td>Granule-bound starch synthase I</td>
    </tr>
    <tr>
      <td>misc</td>
      <td>acid and other phosphatases</td>
      <td>Cre13.g568600.t1.2</td>
      <td></td>
      <td>Multiple inositol polyphosphate phosphatase-related, Acid phosphatase activity</td>
    </tr>
    <tr>
      <td></td>
      <td>alcohol dehydrogenases</td>
      <td>Cre13.g569350.t1.1</td>
      <td></td>
      <td>Sterol dehydrogenase-related, Flavonol reductase/cinnamoyl-CoA reductase</td>
    </tr>
    <tr>
      <td></td>
      <td>cytochrome P450</td>
      <td>Cre07.g356250.t1.2</td>
      <td></td>
      <td>Cytochrome P450 CYP4/CYP19/CYP26 subfamilies, beta-carotene 15,15'-monooxygenase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre07.g356250.t1.2</td>
      <td></td>
      <td>Cytochrome P450 CYP4/CYP19/CYP26 subfamilies, beta-carotene 15,15'-monooxygenase</td>
    </tr>
    <tr>
      <td></td>
      <td>dynamin</td>
      <td>Cre17.g724150.t1.1</td>
      <td>DRP3</td>
      <td>Dynamin-related GTPase</td>
    </tr>
    <tr>
      <td></td>
      <td>GCN5-related N-acetyltransferase</td>
      <td>Cre16.g657150.t1.2</td>
      <td></td>
      <td>N-acetyltransferase activity (GNAT) family</td>
    </tr>
    <tr>
      <td></td>
      <td>gluco-, galacto- and mannosidases</td>
      <td>Cre03.g171050.t1.2</td>
      <td>GHL1</td>
      <td>Glycosyl hydrolase</td>
    </tr>
    <tr>
      <td></td>
      <td>misc2</td>
      <td>Cre14.g614100.t1.1</td>
      <td>GTR26</td>
      <td>Dolichyl-diphosphooligosaccharide-protein glycosyltransferase</td>
    </tr>
    <tr>
      <td></td>
      <td>rhodanese</td>
      <td>Cre07.g352550.t1.1</td>
      <td>RDP3</td>
      <td>Putative rhodanese domain phosphatase</td>
    </tr>
    <tr>
      <td></td>
      <td>short chain dehydrogenase/reductase (SDR)</td>
      <td>Cre07.g352450.t1.1</td>
      <td></td>
      <td>Corticosteroid 11-beta-dehydrogenase and related short chain-type dehydrogenases, 3-hydroxybutyrate dehydrogenase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre12.g559350.t1.1</td>
      <td></td>
      <td>1-Acyl dihydroxyacetone phosphate reductase and related dehydrogenases</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g191850.t1.1</td>
      <td></td>
      <td>Short chain dehydrogenase</td>
    </tr>
    <tr>
      <td></td>
      <td>UDP glucosyl and glucoronyl transferases</td>
      <td>Cre11.g474450.t1.1</td>
      <td></td>
      <td>NF*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre03.g205250.t1.2</td>
      <td>ELG4</td>
      <td>Exostosin-like glycosyltransferase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre16.g659500.t1.1</td>
      <td></td>
      <td>Lactosylceramide 4-alpha-galactosyltransferase</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cre11.g483400.t1.2</td>
      <td>ELG10</td>
      <td>Exostosin-like glycosyltransferase</td>
    </tr>
    <tr>
      <td>Tetrapyrrole synthesis</td>
      <td>Glu-tRNA synthetase</td>
      <td>Cre12.g510800.t1.1</td>
      <td>CHLI2</td>
      <td>Magnesium-chelatase subunit chlI</td>
    </tr>
    <tr>
      <td></td>
      <td>magnesium protoporphyrin IX methyltransferase</td>
      <td>Cre12.g498550.t1.2</td>
      <td></td>
      <td>Magnesium protoporphyrin IX S-adenosyl methionine O-methyl transferase (Magnesium-protoporphyrin IX methyltransferase) (PPMT)</td>
    </tr>
    <tr>
      <td></td>
      <td>unspecified</td>
      <td>Cre12.g516350.t1.1</td>
      <td>COX10</td>
      <td>Cytochrome c oxidase assembly protein Cox10</td>
    </tr>
    <tr>
      <td></td>
      <td>urogen III methylase</td>
      <td>Cre02.g133050.t1.2</td>
      <td></td>
      <td>NF*</td>
    </tr>
  </tbody>
</table>

_*Corresponding gene model was not found in v5._

We observed that some of the genes more strongly dependent on SAK1 had repressed transcript levels (e.g., CFA1 and SOUL2), indicating that SAK1 is required for their basal expression, while others had elevated basal levels (GPX5), suggesting that expression of these genes is controlled also by other pathways. As is discussed in the following section, SAK1 expression monitored by qRT-PCR followed the latter trend as the 5′UTR of the gene was elevated in the mutant (Figure 4E), which may be a result of response to other factors such as a possible oxidization product of 1O2. The SAK1-dependent genes induced by 1O2 and repressed at basal level in the mutant (i.e., those that require SAK1 for basal expression) are indicated in Table 5.

![Figure 4.](https://cdn.elifesciences.org/articles/02286/elife-02286-fig4-v3.jpg)

**Figure 4.:** (A) The insertion of a zeocin resistance gene and the RB sensitivity phenotype are linked. Twelve complete tetrads from a backcross of sak1 to wild type are shown. Numbers indicate independent tetrads, and letters (a-d) indicate the individual progeny from tetrads. (B) Gene structure of SAK1 and the insertion site. Gray boxes indicate positions of primers used for qPCR. (C) Transformation of sak1 with a genomic fragment containing SAK1 rescues the acclimation phenotype. sak1(gSAK1)-1 and sak1(gSAK1)-2 are two independent transformants. (D) sak1(gSAK1)-1 and sak1(gSAK1)-2 show recovery of 1O2 target gene expression. Y-axis indicates fold change during acclimation to 1O2. (E) qRT-PCR of SAK1 in WT and sak1 mutant using primers for 5′- and 3′-UTR shown in panel B. (F) SAK1 protein is induced in WT and detected as higher molecular weight bands during acclimation to 1O2 generated by RB. (G) SAK1 transcript probed for 5′-UTR in cells transferred from low light to high light for 1 hr. Error bars indicate standard deviation of biological triplicates.

### The sak1 mutant identifies a single nuclear gene that is itself induced during acclimation to 1O2

The sak1 mutant was generated by insertional mutagenesis using a plasmid that confers resistance to zeocin (Dent et al., 2005). Progeny obtained from a backcross of sak1 with WT showed that the mutation causing the RB sensitivity phenotype was linked to zeocin resistance (Figure 4A). The site of insertion was identified by thermal asymmetric interlaced (TAIL)-PCR (Liu et al., 1995) as the second exon of the annotated gene Cre17.g741300 on chromosome 17 (Figure 4B). To test whether this gene is responsible for the mutant phenotype, a genomic fragment containing the gene with an additional ∼500 bp region upstream of the predicted transcription start site was cloned and introduced into the mutant by co-transformation. Among the approximately 300 transformants screened, two clones appeared to have recovered the RB acclimation phenotype (Figure 4C). Furthermore, induction of genes we found attenuated in sak1 (Figure 2) was restored in these transformants (Figure 4D), confirming that Cre17.g741300 is the SAK1 gene required for acclimation and the gene expression response to 1O2.

In WT, the SAK1 gene itself was induced by 6- to 10-fold during acclimation when probed for the 5′-and 3′-UTR of the transcript by qRT-PCR (Figure 4E). The mutant displayed elevated basal level and induction of the 5′-UTR during acclimation, whereas the 3′-UTR of the transcript was undetectable, indicating that the full-length transcript was absent in sak1 (Figure 4E). An antibody raised against an epitope of the SAK1 protein detected a single band in basal conditions, whereas the SAK1 protein appeared as multiple bands with higher molecular weight in acclimated WT cells, all of which were absent in the mutant (Figure 4F). SAK1 transcript was induced when probed for the 5′-UTR during high light exposure in both WT and sak1 (Figure 4G) similarly to other 1O2-response genes identified by RNA-seq (Table 1), indicating that SAK1 itself is part of the endogenous response to high light.

### SAK1 contains an uncharacterized domain conserved in chlorophytes and found in some bZIP transcription factors

The predicted SAK1 protein consists of 1141 amino acid residues and has no domains with functional annotation. Only a ∼150-residue region at the C-terminus, designated the SAK1 domain, has similarity to other proteins. Many predicted proteins within chlorophytes (Volvox carteri [8 proteins], Coccomyxa subellipsoidea [3 proteins], Chlamydomonas [14 proteins], Chlorella variabilis [9 proteins] and Micromonas [3 proteins]) (Table 8) contain this domain as shown in the alignment in Figure 5—figure supplement 1. Among the 37 members of the chlorophyte SAK1 domain family, 13 have possible bZIP transcription factor domains (six were significant Pfam hits and seven were below the threshold for significance but recognizable by Pfam) (Figure 5). One protein contained a mitochondrial (transcription) termination factor (mTERF) domain (Figure 5), defined by its three leucine zipper domains required for DNA binding (Fernandez-Silva et al., 1997). Proteins with more distantly related SAK1 domains were found by PSI-BLAST in plants, many of which were hypothetical or unknown proteins but also included bZIP transcription factors.

**Table 8.**
 SAK1 domain containing proteins in chlorophytes


<table>
  <thead>
    <tr>
      <th>Number in alignment</th>
      <th>Organism</th>
      <th>Transcript/Protein IDaTranscript/Protein IDaTranscript/Protein ID*</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Volvox carteri</td>
      <td>Vocar20009235</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Volvox carteri</td>
      <td>Vocar20002437</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Volvox carteri</td>
      <td>Vocar20002672</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Volvox carteri</td>
      <td>Vocar20004923</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Volvox carteri</td>
      <td>Vocar20012349</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Volvox carteri</td>
      <td>Vocar20005988</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Volvox carteri</td>
      <td>Vocar20007158</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Volvox carteri</td>
      <td>Vocar20007883</td>
    </tr>
    <tr>
      <td>9</td>
      <td>Coccomyxa subellipsoidea</td>
      <td>57405</td>
    </tr>
    <tr>
      <td>10</td>
      <td>Coccomyxa subellipsoidea</td>
      <td>59655</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Coccomyxa subellipsoidea</td>
      <td>57694</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>Cre16.g652650.t1.3</td>
    </tr>
    <tr>
      <td>13</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>Cre06.g271000.t1.2</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>Cre06.g285800.t1.2</td>
    </tr>
    <tr>
      <td>15</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>Cre06.g275600.t1.2</td>
    </tr>
    <tr>
      <td>16</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>Cre06.g285750.t1.3</td>
    </tr>
    <tr>
      <td>17</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>Cre06.g270950.t1.2</td>
    </tr>
    <tr>
      <td>18</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>g9774.t1</td>
    </tr>
    <tr>
      <td>SAK1</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>KF985242</td>
    </tr>
    <tr>
      <td>20</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>Cre03.g179150.t1.2</td>
    </tr>
    <tr>
      <td>21</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>g3701.t1</td>
    </tr>
    <tr>
      <td>22</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>Cre03.g179250.t1.2</td>
    </tr>
    <tr>
      <td>23</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>Cre03.g179200.t1.2</td>
    </tr>
    <tr>
      <td>24</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>Cre01.g004800.t1.2</td>
    </tr>
    <tr>
      <td>25</td>
      <td>Chlamydomonas reinhardtii</td>
      <td>Cre01.g048550.t1.3</td>
    </tr>
    <tr>
      <td>26</td>
      <td>Chlorella variabilis</td>
      <td>EFN51260</td>
    </tr>
    <tr>
      <td>27</td>
      <td>Chlorella variabilis</td>
      <td>EFN53496</td>
    </tr>
    <tr>
      <td>28</td>
      <td>Chlorella variabilis</td>
      <td>EFN55618</td>
    </tr>
    <tr>
      <td>29</td>
      <td>Chlorella variabilis</td>
      <td>EFN57652</td>
    </tr>
    <tr>
      <td>30</td>
      <td>Chlorella variabilis</td>
      <td>EFN55658</td>
    </tr>
    <tr>
      <td>31</td>
      <td>Chlorella variabilis</td>
      <td>EFN54262</td>
    </tr>
    <tr>
      <td>32</td>
      <td>Chlorella variabilis</td>
      <td>EFN54510</td>
    </tr>
    <tr>
      <td>33</td>
      <td>Chlorella variabilis</td>
      <td>EFN55806</td>
    </tr>
    <tr>
      <td>34</td>
      <td>Chlorella variabilis</td>
      <td>EFN53492</td>
    </tr>
    <tr>
      <td>35</td>
      <td>Micromonas sp. RCC299</td>
      <td>ACO61347</td>
    </tr>
    <tr>
      <td>36</td>
      <td>Micromonas pusilla CCMP1545</td>
      <td>EEH57791</td>
    </tr>
    <tr>
      <td>37</td>
      <td>Micromonas sp. RCC299</td>
      <td>ACO65814</td>
    </tr>
  </tbody>
</table>

_*1–25, as defined on phytozome.net; 26–37, CrSAK1, genbank accession numbers._

![Figure 5.](https://cdn.elifesciences.org/articles/02286/elife-02286-fig5-v3.jpg)

**Figure 5.:** Schematic of relative positions of SAK1 and bZIP domains. One protein (Cv28) contains a mitochondrial termination factor (mTERF) domain. The letters and numbers in the abbreviated names represent initials of the species and numbers listed in Table 8. Proteins with italicized names contain bZIP domains that were recognized by Pfam but scored below significance.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/02286/elife-02286-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** The SAK1 domains of 37 chlorophyte proteins were aligned by MUSCLE (phylogeny.fr). Protein identities are as shown in Table 8. Star indicates a relatively conserved residue within the SAK1 domain that was predicted to be a possible phosphorylation site (Figure 5—figure supplement 3).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/02286/elife-02286-fig5-figsupp2-v3.jpg)

**Figure 5—figure supplement 2.:** SAK1 domain modeled against its best-hit nickel cobalt resistance protein cnrr by PHYRE. 44% (coverage) of the SAK1 domain was aligned with 73.6% confidence.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/02286/elife-02286-fig5-figsupp3-v3.jpg)

**Figure 5—figure supplement 3.:** Prediction of phosphorylation sites by NetPhos 2.0. Orange bar indicates the position of SAK1 domain, star indicates a relatively conserved residue among the 37 members containing the SAK1 domain.

Amino acid positions 900 to 1089 of SAK1, corresponding to the region aligned with other proteins in Figure 5—figure supplement 1, were searched for secondary structure using PHYRE, and this region was predicted to consist of mostly alpha helices with some disordered intervals. The top hit was a cobalt/nickel-binding resistance protein cnrr, and 44% of the residues were modeled with 73.6% confidence (Figure 5—figure supplement 2).

### SAK1 resides mainly in the cytosol and is phosphorylated during induction by 1O2

To obtain insight into the function of SAK1, we isolated subcellular fractions enriched for chloroplast, ER, cytosol, and mitochondria from WT cells. The Chlamydomonas cell contains a single large chloroplast that is physically connected to other organelles such as the ER, making it particularly challenging to fractionate. The patterns of markers specific for chloroplast, ER, cytosol, and mitochondria showed that each target fraction was enriched as expected, although with some cross contamination (Figure 6A,B). The distribution of SAK1 in these fractions resembled most closely that of the cytosolic marker NAB1 (Mussgnug et al., 2005), although the SAK1 signal was not as enriched as NAB1 in the cytosolic fraction, possibly due to partial degradation of SAK1 during the fractionation. The localization was the same in cells with and without RB treatment (Figure 6A). Because SAK1 was required for the induction of many genes during acclimation to 1O2 and the list of proteins with similarity to SAK1 included those predicted to be bZIP transcription factors, we tested whether SAK1 protein was dually targeted to the nucleus and cytosol, which would account for the lack of enrichment of SAK1 in the cytosolic fraction (Figure 6A). As shown in Figure 6C although a faint SAK1 signal was detected in nuclear fraction, there was no enrichment as seen for the nuclear marker histone H3 (H3). The distribution of the cytosolic marker NAB1 indicated the contamination of the nuclear fraction by cytosolic proteins (Figure 6C). Therefore we conclude that the low signal of SAK1 in the nuclear fraction is likely to be due to cytosolic contamination. Attempts to detect the protein by immunofluorescence using anti-SAK1 antibodies as well as anti-FLAG and anti-HA antibodies against tagged proteins in transgenic lines were unsuccessful due to a very low signal-to-noise ratio even in bleached cells.

![Figure 6.](https://cdn.elifesciences.org/articles/02286/elife-02286-fig6-v3.jpg)

**Figure 6.:** (A and B) SAK1 is detected in the cytosol and not in other subcellular fractions. (C) SAK1 is not enriched in nuclear extracts. Approximately 30 μg of protein was loaded into each well except for mitochondrial fractions that were loaded approximately 7.5 μg protein due to low protein yield in isolated fractions. Subcellular markers: Chloroplast (CP), PSAD; Endoplasmic reticulum (ER), KDEL; Cytosol, NAB1; Mitochondria (mito), cytochrome c (Cyt c); Nuclear, histone 3 (H3). The arrowhead indicates the band corresponding to Cyt c. (D) Protein extracts from cells treated with increasing concentrations of RB were then treated with phosphatase (+) or only with buffer (−) before detection of SAK1 by immunoblot analysis.

By SDS-PAGE and immunoblot analysis, SAK1 appeared in multiple forms with higher molecular weight during acclimation compared to that observed in control cells (Figures 4F and 6A,C). When the extracted protein samples were treated with phosphatase, the diffuse pattern of multiple forms collapsed into a single band detected by immunoblot analysis that had an even higher mobility that that of untreated cells (Figure 6D). This result indicates that SAK1 is a phosphorylated protein during basal conditions, and it is further phosphorylated upon exposure of cells to 1O2.

## Discussion

### SAK1 is necessary for acclimation of Chlamydomonas cells to 1O2

To understand the retrograde signal transduction pathway involved in the cellular response to 1O2, we focused on the unique ability of Chlamydomonas to acclimate to 1O2 stress (Ledford et al., 2007), and we isolated a regulatory mutant that is unable to acclimate. Several previous genetic screens aimed at dissecting the mechanisms of 1O2 signaling have concentrated on the nuclear gene expression response to 1O2, often relying on the response of a single marker gene (Baruah et al., 2009a; Brzezowski et al., 2012; Fischer et al., 2012; Shao et al., 2013). In contrast, our screen exploited a physiological response to sublethal levels of 1O2, which induces the wild type to survive a subsequent, otherwise lethal treatment with the 1O2 generator RB (Ledford et al., 2007). The sak1 mutant completely lacks this ability to acclimate to 1O2 (Figure 1A). An analogous phenotype is exhibited by the yap1Δ mutant of Saccharomyces cerevisiae, which is unable to acclimate to hydrogen peroxide stress (Stephen et al., 1995).

In contrast to the complete loss of acclimation to RB, sak1 acclimates (but less effectively than WT) when pretreated with high light and challenged with RB (Figure 1B). This result suggests that the high light pretreatment induces a broader response than that elicited by RB and that sak1 is still able to respond to other signals besides 1O2 (e.g., plastoquinone redox state, H2O2, and/or superoxide) that are involved in the response to high light. When tested on TAP agar plates for photoheterotrophic growth in the presence of various photosynthetic inhibitors, the sak1 mutant displayed sensitivity to RB but not to other inhibitors (Figure 1D). In particular, sak1 is not more sensitive than WT to high light or norflurazon (an inhibitor of the biosynthesis of carotenoids, which function as quenchers of 1O2). We speculate that the lack of 1O2-sensitive phenotype in these plate experiments is attributable to the time-scale of the treatments involved. 1O2 generated by RB or during a transfer to higher light intensity is transient, whereas NF requires longer time to exert its effect because it needs to enter the cell, inhibit biosynthesis, and deplete cells of existing carotenoids. During this time, the cell is likely able to acclimate by detoxifying and reducing the generation of 1O2 by various means such as changing the composition of the photosynthetic apparatus. We have previously shown that acclimation to 1O2 is transient and is dissipated by 24 hr post-treatment (Ledford et al., 2007). Consistent with this, pretreatment with RB does not acclimate the cells to stresses such as growth in high light or norflurazon that require a period of days to assess an effect on viability (Figure 1—figure supplement 1). We have also observed that under our experimental conditions, the induction of target gene expression upon exposure to 1O2 lasts up to 90 min and then declines. We conclude that SAK1 functions mainly during transient perturbations that generate 1O2. However, during steady-state growth under high light or norflurazon, the cell is able to cope by other means that do not involve SAK1.

### SAK1 is necessary for a subset of the genome-wide response to 1O2 in Chlamydomonas

A physiological acclimation response that results in such an evident growth phenotype (Figure 1A) likely involves large-scale changes in gene expression, and transcriptome analysis of wild-type cells showed that hundreds of nuclear genes are up- or down-regulated during acclimation to 1O2 (Figure 3A,B; Supplementary file 1, C1). The sak1 mutant is specifically impaired in regulation of a notable subset of these genes, that is, those that are most strongly induced in the wild type (Table 5), suggesting that these genes play a key role in the acclimation response to 1O2.

In particular, many genes involved in sterol and lipid metabolism were induced by 1O2 in Chlamydomonas (Figure 3B; Table 3). For example, two genes encoding putative cyclopropane fatty acid synthase (CFA1 and CFA2) exhibited SAK1-dependent induction (Figure 2). Cyclopropane fatty acids have been found in large amounts in the seeds of Sterculia foetida (Bao et al., 2002), although its biological function is unknown. In bacteria, it has been implicated in oxidative stress responses (Guerzoni et al., 2001; Kim et al., 2005) and particularly in the anoxygenic photosynthetic bacterium Rhodobacter sphaeroides, CFA gene expression is induced during 1O2 stress by a σE factor (Ziegelhoffer and Donohue, 2009). Interestingly CFA mutants of R. sphaeroides are compromised in the induction of genes in response to 1O2, suggesting a regulatory role of the gene, protein, or the product of its enzymatic function (cyclopropane fatty acids, Bao et al., 2002) in gene expression rather than solely a biochemical stress response (Nam et al., 2013).

Another intriguing class of up-regulated genes enriched during 1O2 acclimation in WT and not in sak1 was a group of genes encoding transporters, especially ABC transporters related to the MDR and PDR types. This was not surprising considering that 1O2 exists in aquatic and terrestrial environments, where it is generated by photosensitizing humic substances (Frimmel et al., 1987; Steinberg et al., 2008), which are known to affect microbial populations including phytoplankton (Glaeser et al., 2010, 2014). Assuming that some of these transporters function to export photosensitizing molecules from the cell, our results suggest that removal of photosensitizers is an integral part of the 1O2 response in Chlamydomonas, rather than simply a response to the presence of a xenobiotic compound such as RB (Table 4). It is likely that Chlamydomonas, a soil-dwelling microalga, needs to respond to 1O2 that is generated not only in the chloroplast, but also in other compartments. In this context, it is noteworthy that a recent study has demonstrated light-independent 1O2 generation in multiple organelles other than the chloroplast under various biotic and abiotic stresses in plants (Mor et al., 2014).

Two proteins with SOUL heme-binding domains were among SAK1-dependent up-regulated genes (SOUL2 and Cre06.g299700.t1.1, formerly annotated as SOUL1 in v4). Aside from their ability to bind various porphyrins (Blackmon et al., 2002; Sato et al., 2004), SOUL heme-binding proteins have been described in diverse biological functions in mice, such as in apoptosis by interacting with a mitochondrial anti-apoptotic factor Bcl-xL (Ambrosi et al., 2011) or an isoform-specific role in retina and pineal gland (Zylka and Reppert, 1999). The latter form is suggested to play a role in transporting heme or by binding free heme to prevent oxidative stress (Sato et al., 2004). In Arabidopsis a chloroplast-localized SOUL5 protein has been shown to interact with a heme oxygenase, HY1, and mutation of the gene encoding SOUL5 causes oxidative stress (Lee et al., 2012). Chlamydomonas contains five putative SOUL heme-binding proteins, only one of which contains an amino-terminal chloroplast transit peptide. The two SOUL protein genes induced by 1O2 in our study do not seem to be targeted to the chloroplast, and they may function in the cytosol where SAK1 resides. It would be interesting to test whether these proteins bind porphyrins and are required for 1O2 acclimation.

A recent study reported the role of bilins in retrograde signaling in Chlamydomonas through characterization of heme oxygenase mutants disrupted in bilin biosynthesis and transcriptome analyses during dark to light transitions (Duanmu et al., 2013). The transcriptome changes indicated that much of the cell’s response during a dark-to-light transition (DL) involves photo-oxidative stress. Interestingly, among the 515 genes up-regulated in WT during 1O2 acclimation, 144 genes overlapped with those that are induced during DL (Table 9). Focusing on the 104 genes that we defined as SAK1-dependent (Table 5), 31 genes overlapped (Table 9). CFA1, CFA2, and SOUL2 were among these genes, suggesting that a part of the gene expression response to DL in Chlamydomonas is a response to 1O2. SAK1 itself was also up-regulated during DL as was SOR1, which encodes a more broadly oxidative stress-responsive bZIP transcription factor (Fischer et al., 2012). We found that 64 of the genes induced during acclimation to 1O2 were also up-regulated in the gain-of-function sor1 mutant (Fischer et al., 2012). However, the most strongly induced SAK1-dependent genes were not among these genes, except for GPX5, consistent with the idea that SAK1 and SOR1 function in different pathways.

**Table 9.**
 Genes up-regulated during both 1O2 acclimation and dark to light transition


<table>
  <thead>
    <tr>
      <th>Gene ID (v4)</th>
      <th>Gene name</th>
      <th>Annotation</th>
      <th>RB (log2)</th>
      <th>DL (log2) (Duanmu et al., 2013)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cre02.g137700.t1.1*</td>
      <td></td>
      <td></td>
      <td>6.49</td>
      <td>2.34</td>
    </tr>
    <tr>
      <td>Cre06.g281250.t1.1*</td>
      <td>CFA1</td>
      <td>cyclopropane fatty acid synthase</td>
      <td>5.92</td>
      <td>4.49</td>
    </tr>
    <tr>
      <td>Cre01.g033300.t1.1*</td>
      <td></td>
      <td></td>
      <td>5.72</td>
      <td>3.62</td>
    </tr>
    <tr>
      <td>Cre13.g566850.t1.1*</td>
      <td>SOUL2</td>
      <td>SOUL heme-binding protein</td>
      <td>5.53</td>
      <td>2.25</td>
    </tr>
    <tr>
      <td>Cre13.g600650.t1.1*</td>
      <td></td>
      <td></td>
      <td>4.76</td>
      <td>3.26</td>
    </tr>
    <tr>
      <td>Cre06.g263550.t1.1*</td>
      <td>LCI7</td>
      <td>R53.5-related protein</td>
      <td>4.46</td>
      <td>5.27</td>
    </tr>
    <tr>
      <td>Cre07.g342100.t1.1*</td>
      <td></td>
      <td></td>
      <td>4.43</td>
      <td>1.84</td>
    </tr>
    <tr>
      <td>Cre09.g398700.t1.1*</td>
      <td>CPLD27</td>
      <td>coclaurine N-methyltransferase</td>
      <td>4.05</td>
      <td>1.36</td>
    </tr>
    <tr>
      <td>Cre12.g492650.t1.1*</td>
      <td>FAS2</td>
      <td>fasciclin-like protein</td>
      <td>4.01</td>
      <td>9.24</td>
    </tr>
    <tr>
      <td>Cre08.g381510.t1.1*</td>
      <td></td>
      <td></td>
      <td>3.94</td>
      <td>3.27</td>
    </tr>
    <tr>
      <td>Cre10.g458450.t1.2*</td>
      <td>GPX5</td>
      <td>glutathione peroxidase</td>
      <td>3.91</td>
      <td>3.08</td>
    </tr>
    <tr>
      <td>Cre11.g474600.t1.1*</td>
      <td></td>
      <td></td>
      <td>3.90</td>
      <td>1.99</td>
    </tr>
    <tr>
      <td>Cre13.g600700.t1.1*</td>
      <td></td>
      <td></td>
      <td>3.78</td>
      <td>5.79</td>
    </tr>
    <tr>
      <td>Cre14.g613950.t1.1*</td>
      <td></td>
      <td></td>
      <td>3.65</td>
      <td>2.68</td>
    </tr>
    <tr>
      <td>Cre06.g269300.t1.1*</td>
      <td></td>
      <td></td>
      <td>3.50</td>
      <td>1.99</td>
    </tr>
    <tr>
      <td>Cre08.g380300.t1.2*</td>
      <td>MSRA3</td>
      <td>peptide methionine sulfoxide reductase</td>
      <td>3.45</td>
      <td>1.79</td>
    </tr>
    <tr>
      <td>Cre01.g031650.t1.2*</td>
      <td>CGLD12</td>
      <td>protein with potential galactosyl transferase activity</td>
      <td>3.30</td>
      <td>4.90</td>
    </tr>
    <tr>
      <td>Cre14.g629061.t1.1*</td>
      <td></td>
      <td></td>
      <td>3.25</td>
      <td>1.88</td>
    </tr>
    <tr>
      <td>Cre13.g564900.t1.1*</td>
      <td></td>
      <td></td>
      <td>3.22</td>
      <td>3.38</td>
    </tr>
    <tr>
      <td>Cre13.g586450.t1.1</td>
      <td></td>
      <td></td>
      <td>3.21</td>
      <td>3.50</td>
    </tr>
    <tr>
      <td>Cre02.g139500.t1.1*</td>
      <td></td>
      <td></td>
      <td>3.04</td>
      <td>2.12</td>
    </tr>
    <tr>
      <td>Cre19.g756100.t1.1</td>
      <td></td>
      <td></td>
      <td>3.04</td>
      <td>6.53</td>
    </tr>
    <tr>
      <td>Cre01.g036000.t1.2</td>
      <td></td>
      <td></td>
      <td>3.02</td>
      <td>1.16</td>
    </tr>
    <tr>
      <td>Cre14.g618400.t1.1*</td>
      <td></td>
      <td></td>
      <td>2.97</td>
      <td>2.16</td>
    </tr>
    <tr>
      <td>Cre17.g741300.t1.2*</td>
      <td></td>
      <td></td>
      <td>2.88</td>
      <td>1.92</td>
    </tr>
    <tr>
      <td>Cre16.g648700.t1.2*</td>
      <td></td>
      <td></td>
      <td>2.79</td>
      <td>2.35</td>
    </tr>
    <tr>
      <td>Cre17.g729950.t1.1</td>
      <td></td>
      <td></td>
      <td>2.77</td>
      <td>2.61</td>
    </tr>
    <tr>
      <td>Cre17.g721000.t1.1</td>
      <td></td>
      <td></td>
      <td>2.70</td>
      <td>2.12</td>
    </tr>
    <tr>
      <td>Cre06.g263500.t1.1*</td>
      <td></td>
      <td></td>
      <td>2.67</td>
      <td>3.37</td>
    </tr>
    <tr>
      <td>Cre01.g016150.t1.1*</td>
      <td></td>
      <td></td>
      <td>2.65</td>
      <td>2.92</td>
    </tr>
    <tr>
      <td>Cre08.g380000.t1.1*</td>
      <td></td>
      <td></td>
      <td>2.59</td>
      <td>3.74</td>
    </tr>
    <tr>
      <td>Cre04.g224800.t1.1</td>
      <td>VAMP74</td>
      <td>R-SNARE protein, VAMP72-family</td>
      <td>2.58</td>
      <td>3.34</td>
    </tr>
    <tr>
      <td>Cre03.g210150.t1.1</td>
      <td></td>
      <td></td>
      <td>2.57</td>
      <td>3.44</td>
    </tr>
    <tr>
      <td>Cre14.g615600.t1.1*</td>
      <td></td>
      <td></td>
      <td>2.53</td>
      <td>2.40</td>
    </tr>
    <tr>
      <td>Cre06.g293100.t1.1</td>
      <td></td>
      <td>Qc-SNARE SYP6-like protein</td>
      <td>2.48</td>
      <td>4.90</td>
    </tr>
    <tr>
      <td>Cre08.g368950.t1.1</td>
      <td>DHQS</td>
      <td>3-dehydroquinate synthase</td>
      <td>2.39</td>
      <td>2.49</td>
    </tr>
    <tr>
      <td>Cre10.g424350.t1.2</td>
      <td></td>
      <td>metalloprotease</td>
      <td>2.37</td>
      <td>3.18</td>
    </tr>
    <tr>
      <td>Cre12.g537225.t1.1</td>
      <td></td>
      <td></td>
      <td>2.34</td>
      <td>3.39</td>
    </tr>
    <tr>
      <td>Cre07.g336900.t1.2</td>
      <td></td>
      <td></td>
      <td>2.32</td>
      <td>2.31</td>
    </tr>
    <tr>
      <td>Cre16.g664050.t1.1</td>
      <td></td>
      <td></td>
      <td>2.31</td>
      <td>1.88</td>
    </tr>
    <tr>
      <td>Cre16.g677750.t1.1</td>
      <td></td>
      <td></td>
      <td>2.04</td>
      <td>2.22</td>
    </tr>
    <tr>
      <td>Cre12.g537227.t1.1</td>
      <td></td>
      <td></td>
      <td>2.00</td>
      <td>3.46</td>
    </tr>
    <tr>
      <td>Cre17.g737050.t1.1</td>
      <td></td>
      <td>RabGAP/TBC protein</td>
      <td>1.99</td>
      <td>2.32</td>
    </tr>
    <tr>
      <td>Cre06.g297450.t1.1</td>
      <td></td>
      <td></td>
      <td>1.93</td>
      <td>1.46</td>
    </tr>
    <tr>
      <td>Cre06.g258600.t1.1*</td>
      <td></td>
      <td></td>
      <td>1.91</td>
      <td>3.63</td>
    </tr>
    <tr>
      <td>Cre16.g663950.t1.1</td>
      <td></td>
      <td>SC5D, C-5 sterol desaturase</td>
      <td>1.89</td>
      <td>2.03</td>
    </tr>
    <tr>
      <td>Cre13.g588150.t1.1</td>
      <td></td>
      <td></td>
      <td>1.86</td>
      <td>6.21</td>
    </tr>
    <tr>
      <td>Cre17.g722150.t1.1</td>
      <td>PKS3</td>
      <td>type III polyketide synthase</td>
      <td>1.85</td>
      <td>1.61</td>
    </tr>
    <tr>
      <td>Cre16.g688550.t1.1</td>
      <td>GSTS1</td>
      <td>glutathione-S-transferase</td>
      <td>1.84</td>
      <td>1.20</td>
    </tr>
    <tr>
      <td>Cre03.g207800.t1.1</td>
      <td></td>
      <td></td>
      <td>1.84</td>
      <td>7.09</td>
    </tr>
    <tr>
      <td>Cre10.g444550.t1.1*</td>
      <td>SPP1A</td>
      <td>signal peptide peptidase</td>
      <td>1.81</td>
      <td>5.33</td>
    </tr>
    <tr>
      <td>Cre13.g602500.t1.2</td>
      <td></td>
      <td></td>
      <td>1.76</td>
      <td>1.59</td>
    </tr>
    <tr>
      <td>Cre03.g163400.t1.2*</td>
      <td></td>
      <td></td>
      <td>1.76</td>
      <td>2.15</td>
    </tr>
    <tr>
      <td>Cre10.g450000.t1.1</td>
      <td></td>
      <td></td>
      <td>1.74</td>
      <td>2.18</td>
    </tr>
    <tr>
      <td>Cre01.g015500.t1.1</td>
      <td></td>
      <td></td>
      <td>1.72</td>
      <td>1.55</td>
    </tr>
    <tr>
      <td>Cre02.g105750.t1.2</td>
      <td></td>
      <td></td>
      <td>1.71</td>
      <td>3.23</td>
    </tr>
    <tr>
      <td>Cre01.g061750.t1.1</td>
      <td>SPT2</td>
      <td>serine palmitoyltransferase</td>
      <td>1.71</td>
      <td>2.29</td>
    </tr>
    <tr>
      <td>Cre83.g796250.t1.1</td>
      <td></td>
      <td></td>
      <td>1.68</td>
      <td>1.59</td>
    </tr>
    <tr>
      <td>Cre16.g656150.t1.1</td>
      <td></td>
      <td></td>
      <td>1.67</td>
      <td>3.55</td>
    </tr>
    <tr>
      <td>Cre01.g002050.t1.2</td>
      <td></td>
      <td></td>
      <td>1.66</td>
      <td>3.15</td>
    </tr>
    <tr>
      <td>Cre12.g556750.t1.2</td>
      <td>Tic32-like 1</td>
      <td>Short-chain dehydrogenase, classical family, similar to PsTic32</td>
      <td>1.66</td>
      <td>3.15</td>
    </tr>
    <tr>
      <td>Cre12.g559100.t1.1</td>
      <td></td>
      <td></td>
      <td>1.66</td>
      <td>3.11</td>
    </tr>
    <tr>
      <td>Cre09.g411750.t1.2</td>
      <td></td>
      <td></td>
      <td>1.61</td>
      <td>1.96</td>
    </tr>
    <tr>
      <td>Cre11.g482650.t1.2</td>
      <td></td>
      <td></td>
      <td>1.57</td>
      <td>3.40</td>
    </tr>
    <tr>
      <td>Cre06.g310500.t1.1*</td>
      <td></td>
      <td></td>
      <td>1.57</td>
      <td>6.23</td>
    </tr>
    <tr>
      <td>Cre09.g397900.t1.1</td>
      <td></td>
      <td>transmembrane protein</td>
      <td>1.56</td>
      <td>2.02</td>
    </tr>
    <tr>
      <td>Cre04.g215600.t1.1</td>
      <td></td>
      <td></td>
      <td>1.53</td>
      <td>2.64</td>
    </tr>
    <tr>
      <td>Cre02.g093800.t1.1</td>
      <td></td>
      <td></td>
      <td>1.51</td>
      <td>4.99</td>
    </tr>
    <tr>
      <td>Cre02.g093750.t1.1</td>
      <td>NRX2</td>
      <td>Nucleoredoxin 2</td>
      <td>1.50</td>
      <td>6.26</td>
    </tr>
    <tr>
      <td>Cre01.g004350.t1.1</td>
      <td></td>
      <td></td>
      <td>1.50</td>
      <td>2.29</td>
    </tr>
    <tr>
      <td>Cre01.g034600.t1.1</td>
      <td></td>
      <td></td>
      <td>1.50</td>
      <td>2.22</td>
    </tr>
    <tr>
      <td>Cre11.g472600.t1.2</td>
      <td></td>
      <td></td>
      <td>1.48</td>
      <td>2.00</td>
    </tr>
    <tr>
      <td>Cre12.g500500.t1.2</td>
      <td>SMT1</td>
      <td>sterol-C24-methyltransferase</td>
      <td>1.46</td>
      <td>3.05</td>
    </tr>
    <tr>
      <td>Cre13.g577950.t1.1</td>
      <td>VPS6</td>
      <td>subunit of the ESCRT-III complex</td>
      <td>1.45</td>
      <td>2.36</td>
    </tr>
    <tr>
      <td>Cre02.g118200.t1.1</td>
      <td></td>
      <td></td>
      <td>1.44</td>
      <td>2.79</td>
    </tr>
    <tr>
      <td>Cre01.g012500.t1.1</td>
      <td>PRA1</td>
      <td>prenylated rab acceptor family protein</td>
      <td>1.43</td>
      <td>2.46</td>
    </tr>
    <tr>
      <td>Cre12.g521600.t1.2</td>
      <td></td>
      <td></td>
      <td>1.42</td>
      <td>2.89</td>
    </tr>
    <tr>
      <td>Cre03.g179100.t1.1</td>
      <td></td>
      <td>ubiquitin fusion degradation protein</td>
      <td>1.41</td>
      <td>3.38</td>
    </tr>
    <tr>
      <td>Cre09.g413150.t1.2</td>
      <td></td>
      <td></td>
      <td>1.39</td>
      <td>4.31</td>
    </tr>
    <tr>
      <td>Cre13.g572200.t1.1</td>
      <td></td>
      <td>tyrosine/tryptophan transporter protein</td>
      <td>1.39</td>
      <td>2.57</td>
    </tr>
    <tr>
      <td>Cre03.g185850.t1.2</td>
      <td></td>
      <td>PfkB-type carbohydrate kinase</td>
      <td>1.37</td>
      <td>3.05</td>
    </tr>
    <tr>
      <td>Cre18.g743600.t1.1</td>
      <td></td>
      <td></td>
      <td>1.37</td>
      <td>1.65</td>
    </tr>
    <tr>
      <td>Cre02.g076800.t1.1</td>
      <td></td>
      <td>sterol reductase</td>
      <td>1.36</td>
      <td>2.41</td>
    </tr>
    <tr>
      <td>Cre06.g256750.t1.1</td>
      <td>FAT1</td>
      <td>acyl carrier protein thioesterase</td>
      <td>1.35</td>
      <td>1.67</td>
    </tr>
    <tr>
      <td>Cre17.g729450.t1.1</td>
      <td></td>
      <td></td>
      <td>1.34</td>
      <td>1.90</td>
    </tr>
    <tr>
      <td>Cre11.g471550.t1.1</td>
      <td></td>
      <td></td>
      <td>1.34</td>
      <td>3.29</td>
    </tr>
    <tr>
      <td>Cre09.g395750.t1.2</td>
      <td></td>
      <td></td>
      <td>1.33</td>
      <td>2.87</td>
    </tr>
    <tr>
      <td>Cre14.g617100.t1.1</td>
      <td></td>
      <td></td>
      <td>1.33</td>
      <td>3.33</td>
    </tr>
    <tr>
      <td>Cre16.g691500.t1.1</td>
      <td></td>
      <td>Sec14p-like lipid-binding protein</td>
      <td>1.33</td>
      <td>2.28</td>
    </tr>
    <tr>
      <td>Cre02.g079550.t1.1</td>
      <td>DRP2</td>
      <td>Dynamin-related GTPase</td>
      <td>1.32</td>
      <td>2.34</td>
    </tr>
    <tr>
      <td>Cre02.g079300.t1.1</td>
      <td>VPS4</td>
      <td>AAA-ATPase of VPS4/SKD1 family</td>
      <td>1.32</td>
      <td>1.96</td>
    </tr>
    <tr>
      <td>Cre05.g231700.t1.2</td>
      <td></td>
      <td></td>
      <td>1.31</td>
      <td>2.40</td>
    </tr>
    <tr>
      <td>Cre02.g132300.t1.2</td>
      <td>DNJ12</td>
      <td>DnaJ-like protein</td>
      <td>1.30</td>
      <td>2.24</td>
    </tr>
    <tr>
      <td>Cre69.g794101.t1.1</td>
      <td></td>
      <td></td>
      <td>1.30</td>
      <td>2.65</td>
    </tr>
    <tr>
      <td>Cre13.g565600.t1.2</td>
      <td></td>
      <td></td>
      <td>1.29</td>
      <td>3.42</td>
    </tr>
    <tr>
      <td>Cre13.g593700.t1.1</td>
      <td></td>
      <td>monooxygenase, DBH-like</td>
      <td>1.29</td>
      <td>1.81</td>
    </tr>
    <tr>
      <td>Cre12.g498000.t1.2</td>
      <td></td>
      <td></td>
      <td>1.28</td>
      <td>3.88</td>
    </tr>
    <tr>
      <td>Cre06.g292900.t1.2</td>
      <td></td>
      <td></td>
      <td>1.28</td>
      <td>2.16</td>
    </tr>
    <tr>
      <td>Cre08.g372100.t1.1</td>
      <td>HSP70A</td>
      <td>Heat shock protein 7A</td>
      <td>1.27</td>
      <td>2.28</td>
    </tr>
    <tr>
      <td>Cre01.g039350.t1.1</td>
      <td>NCR2</td>
      <td>NADPH-cytochrome P45 reductase</td>
      <td>1.26</td>
      <td>2.19</td>
    </tr>
    <tr>
      <td>Cre03.g211100.t1.1</td>
      <td></td>
      <td></td>
      <td>1.26</td>
      <td>2.11</td>
    </tr>
    <tr>
      <td>Cre17.g731800.t1.1</td>
      <td></td>
      <td></td>
      <td>1.25</td>
      <td>1.78</td>
    </tr>
    <tr>
      <td>Cre17.g730650.t1.1</td>
      <td></td>
      <td></td>
      <td>1.25</td>
      <td>2.28</td>
    </tr>
    <tr>
      <td>Cre02.g123000.t1.2</td>
      <td></td>
      <td></td>
      <td>1.24</td>
      <td>1.42</td>
    </tr>
    <tr>
      <td>Cre05.g247700.t1.2</td>
      <td></td>
      <td></td>
      <td>1.24</td>
      <td>2.71</td>
    </tr>
    <tr>
      <td>Cre08.g360800.t1.2</td>
      <td></td>
      <td>haloacid dehalogenase-like hydrolase</td>
      <td>1.23</td>
      <td>4.39</td>
    </tr>
    <tr>
      <td>Cre07.g350750.t1.1</td>
      <td>PTOX1</td>
      <td>alternative oxidase</td>
      <td>1.22</td>
      <td>3.32</td>
    </tr>
    <tr>
      <td>Cre17.g703750.t1.1</td>
      <td></td>
      <td></td>
      <td>1.20</td>
      <td>2.21</td>
    </tr>
    <tr>
      <td>Cre06.g306041.t1.1</td>
      <td></td>
      <td></td>
      <td>1.20</td>
      <td>2.90</td>
    </tr>
    <tr>
      <td>Cre02.g116650.t1.1</td>
      <td></td>
      <td></td>
      <td>1.20</td>
      <td>2.83</td>
    </tr>
    <tr>
      <td>Cre08.g379400.t1.2</td>
      <td></td>
      <td></td>
      <td>1.18</td>
      <td>3.04</td>
    </tr>
    <tr>
      <td>Cre16.g677000.t1.1</td>
      <td>HSP70E</td>
      <td>Heat shock protein 7E</td>
      <td>1.18</td>
      <td>2.50</td>
    </tr>
    <tr>
      <td>Cre06.g283900.t1.1</td>
      <td></td>
      <td></td>
      <td>1.18</td>
      <td>5.24</td>
    </tr>
    <tr>
      <td>Cre14.g626750.t1.1</td>
      <td></td>
      <td></td>
      <td>1.17</td>
      <td>4.12</td>
    </tr>
    <tr>
      <td>Cre01.g010700.t1.1</td>
      <td></td>
      <td></td>
      <td>1.16</td>
      <td>2.10</td>
    </tr>
    <tr>
      <td>Cre01.g002000.t1.2</td>
      <td></td>
      <td>predicted proteim</td>
      <td>1.15</td>
      <td>1.68</td>
    </tr>
    <tr>
      <td>Cre04.g213150.t1.1</td>
      <td></td>
      <td></td>
      <td>1.15</td>
      <td>2.78</td>
    </tr>
    <tr>
      <td>Cre16.g694250.t1.1</td>
      <td></td>
      <td></td>
      <td>1.15</td>
      <td>2.92</td>
    </tr>
    <tr>
      <td>Cre05.g246400.t1.1</td>
      <td></td>
      <td></td>
      <td>1.15</td>
      <td>2.74</td>
    </tr>
    <tr>
      <td>Cre02.g128450.t1.1</td>
      <td></td>
      <td></td>
      <td>1.13</td>
      <td>2.82</td>
    </tr>
    <tr>
      <td>Cre03.g180250.t1.1</td>
      <td></td>
      <td>Myo-inositol-1-phosphate synthase</td>
      <td>1.13</td>
      <td>2.05</td>
    </tr>
    <tr>
      <td>Cre03.g186150.t1.1</td>
      <td></td>
      <td></td>
      <td>1.13</td>
      <td>1.78</td>
    </tr>
    <tr>
      <td>Cre02.g137800.t1.1</td>
      <td></td>
      <td></td>
      <td>1.13</td>
      <td>2.00</td>
    </tr>
    <tr>
      <td>Cre11.g471500.t1.1</td>
      <td>MFT10</td>
      <td>predicted protein</td>
      <td>1.11</td>
      <td>1.40</td>
    </tr>
    <tr>
      <td>Cre10.g435200.t1.1</td>
      <td></td>
      <td></td>
      <td>1.10</td>
      <td>2.13</td>
    </tr>
    <tr>
      <td>Cre13.g593850.t1.2</td>
      <td></td>
      <td></td>
      <td>1.10</td>
      <td>3.91</td>
    </tr>
    <tr>
      <td>Cre19.g754000.t1.2</td>
      <td></td>
      <td></td>
      <td>1.10</td>
      <td>2.33</td>
    </tr>
    <tr>
      <td>Cre13.g593869.t1.1</td>
      <td></td>
      <td></td>
      <td>1.10</td>
      <td>3.90</td>
    </tr>
    <tr>
      <td>Cre08.g377300.t1.2</td>
      <td></td>
      <td></td>
      <td>1.09</td>
      <td>3.27</td>
    </tr>
    <tr>
      <td>Cre04.g225050.t1.2</td>
      <td></td>
      <td>predicted protein</td>
      <td>1.09</td>
      <td>3.55</td>
    </tr>
    <tr>
      <td>Cre07.g330300.t1.1</td>
      <td></td>
      <td></td>
      <td>1.08</td>
      <td>2.22</td>
    </tr>
    <tr>
      <td>Cre12.g500450.t1.2</td>
      <td></td>
      <td></td>
      <td>1.08</td>
      <td>3.00</td>
    </tr>
    <tr>
      <td>Cre06.g262000.t1.1</td>
      <td></td>
      <td></td>
      <td>1.08</td>
      <td>1.87</td>
    </tr>
    <tr>
      <td>Cre10.g441550.t1.2</td>
      <td>MAM3B</td>
      <td>predicted protein</td>
      <td>1.07</td>
      <td>1.54</td>
    </tr>
    <tr>
      <td>Cre06.g249800.t1.1</td>
      <td></td>
      <td>unknown conserved protein</td>
      <td>1.07</td>
      <td>2.08</td>
    </tr>
    <tr>
      <td>Cre01.g038250.t1.1</td>
      <td>SDC1</td>
      <td>serine decarboxylase</td>
      <td>1.06</td>
      <td>1.92</td>
    </tr>
    <tr>
      <td>Cre44.g788200.t1.1</td>
      <td></td>
      <td></td>
      <td>1.06</td>
      <td>2.13</td>
    </tr>
    <tr>
      <td>Cre08.g359200.t1.2</td>
      <td></td>
      <td></td>
      <td>1.03</td>
      <td>2.69</td>
    </tr>
    <tr>
      <td>Cre05.g245950.t1.1</td>
      <td>DRP1</td>
      <td>Dynamin-related GTPase</td>
      <td>1.03</td>
      <td>2.15</td>
    </tr>
    <tr>
      <td>Cre05.g234100.t1.1</td>
      <td>CYP745A1</td>
      <td>cytochrome P45</td>
      <td>1.01</td>
      <td>2.61</td>
    </tr>
    <tr>
      <td>Cre07.g328700.t1.2</td>
      <td></td>
      <td></td>
      <td>1.01</td>
      <td>1.56</td>
    </tr>
    <tr>
      <td>Cre10.g440250.t1.2</td>
      <td></td>
      <td></td>
      <td>1.01</td>
      <td>2.14</td>
    </tr>
    <tr>
      <td>Cre17.g725200.t1.1</td>
      <td></td>
      <td>MDR-like ABC transporter</td>
      <td>1.01</td>
      <td>3.30</td>
    </tr>
    <tr>
      <td>Cre82.g796100.t1.1</td>
      <td></td>
      <td></td>
      <td>1.01</td>
      <td>2.49</td>
    </tr>
  </tbody>
</table>

_*Genes defined as SAK1-dependent in Table 4._

### SAK1 is a key intermediate component in the retrograde signaling pathway for 1O2 acclimation

Cloning of the SAK1 gene revealed that it encodes a large previously uncharacterized phosphoprotein located primarily in the cytosol (Figure 6A,D), suggesting that it functions as an intermediate in the retrograde signaling pathway from the chloroplast to the nucleus that leads to 1O2 acclimation. Previous genetic screens in Arabidopsis have identified proteins in the chloroplast, such as EX1 and EX2 (Wagner et al., 2004; Lee et al., 2007), and in the nucleus, such as PLEIOTROPIC RESPONSE LOCUS 1 (Baruah et al., 2009b) and topoisomerase VI (Simková et al., 2012), that are involved in 1O2 signaling. By screening for mutants that are unable to induce a 1O2-responsive reporter gene (HPS70A) in Chlamydomonas, a small zinc finger protein (Cre09.g416500.t1.2) called MBS was recently identified as having a role in ROS signaling in both Chlamydomonas and Arabidopsis (Shao et al., 2013). Like SAK1, MBS in Chlamydomonas is located in the cytosol, raising a question about the relationship of these two proteins in 1O2 signaling. As expected, we found HSP70A among the genes induced by RB treatment of Chlamydomonas (Table 3) however in sak1 it was not significantly induced above the twofold threshold, suggesting that SAK1 might function in the same signaling pathway as MBS. The MBS gene itself is not induced by 1O2 (Shao et al., 2013), and we will investigate the genetic and biochemical relationship of SAK1 and MBS in future research.

SAK1 contains a novel domain of ∼150 amino acid residues that is found in several chlorophyte species (Table 8). The sequence of this domain is not highly conserved (Figure 5—figure supplement 1), and is even less conserved among land plant proteins, although it is detectable by PSI-BLAST, indicating that it has diverged in sequence in plants and algae. We identified 37 proteins that have the SAK1 domain, 13 of which also contained a bZIP transcription factor domain, consistent with a function in regulating gene expression. Under our standard laboratory growth conditions, SAK1 appears to have a relatively low level of phosphorylation, but it becomes hyperphosphorylated during 1O2 acclimation (Figure 6D). Phosphorylation prediction software NetPhos 2.0 (http://www.cbs.dtu.dk/services/NetPhos/) predicted 24 serine, 9 threonine, and one tyrosine residue as possible sites throughout the protein (Figure 5—figure supplement 3). One of these serine residues is within the conserved SAK1 domain and is relatively conserved for polar amino acids. At this position, 18 SAK1 family members had threonine, and three had serine residues including SAK1 (Figure 5—figure supplement 1). We speculate that phosphorylation of SAK1 in the cytosol is a necessary intermediate step in 1O2 acclimation. Through further analysis of the transcriptome data, isolation of proteins that physically interact with SAK1, and characterization of additional, non-allelic sak mutants, we hope to identify the kinase that is responsible for the direct modification of SAK1 as well as other upstream and downstream components of this retrograde signaling pathway in Chlamydomonas.

## Material and methods

### Chlamydomonas strains and culture conditions

The sak1 mutant was generated by insertional mutagenesis as described previously (Dent et al., 2005) from WT strain 4A+. Cells were grown at 22°C photoheterotrophically in Tris-acetate phosphate media (TAP) unless otherwise stated (Harris, 2009).

### RB sensitivity screen and acclimation assays

For systematic screening of large number of strains for increased or decreased resistance to RB, individual strains were inoculated into 180-200 μl TAP medium in 96-well plates, grown for a at least 3 days to saturation under light intensity of 60–80 μmol photons m−2 s−1, spotted onto TAP plates with 2.7, 3.0, or 3.3 μM RB, and scored for their growth compared to WT and sak1. For more quantitative evaluation of RB sensitivity, the cells were grown to saturation in 1 ml of TAP medium because we have observed rapidly growing cells to have more variable sensitivity to RB (data not shown). The cells were counted and adjusted to equal cell density then dispensed into aliquots in duplicate 96-well plates. One of the duplicates was pretreated in dark while the other was placed in light for 40 min with 1 μM RB. For challenge treatments, 4.5, 5.1, 5.7, 6.3, 6.9, and 7.5 μM RB was added to both plates, which were placed under light for 1 hr and then spotted onto TAP agar media with no RB. All treatments were applied under light intensity of 60–80 µmol photons m−2 s−1, which is the light intensity described as low light unless stated otherwise.

### Pretreatment and challenge with RB and Fv/Fm measurement

Cells were grown under 100 μmol photons m−2 s−1, adjusted to 2 × 106 cells ml−1, and treated with RB at a final concentration of 0.5 μM for 30 min (pretreatment) in light (+) or dark (−). After the pretreatment all the cultures were exposed to an additional 3.75 μM RB (challenge) in low light and collected for measurement of Fv/Fm at 30, 60, and 90 min. The cells were dark-acclimated for at least 30 min before applying a saturating light pulse of 2000 μmol photons m−2 s−1 and measuring the chlorophyll fluorescence yield using an FMS2 fluorometer (Hansatech Instruments, Norfolk, UK).

### Culture conditions for gene expression analyses by qRT-PCR and RNA-seq

Cultures were grown for at least two light–dark cycles (12 hr light-12 hr dark), and then cell density was adjusted to 2–2.5 × 106 cells ml−1 and split into two flasks (one control and the other for RB treatment) at least an hour prior to adding RB to a final concentration of 1 μM. An equal volume of H2O was added to the control. RB was added ∼6 hr after the start of the light cycle under light intensity of ∼100 µmol photons m−2 s−1 and the treatment lasted for an hour before harvest. The cells were cooled and harvested by centrifugation at 1200×g for 3 min at 4°C, frozen with liquid nitrogen and stored at −80°C until extraction of RNA. For low light to high light transfer experiment, cultures were grown in continuous light in minimal (HS) medium for 3 days to cell density of 3 × 106 cells ml−1 at 45 µmol photons m−2 s−1. The light intensity was increased to 500 µmol photons m−2 s−1 for 1 hr before harvest.

### Gene expression analysis by qRT-PCR

RNA was extracted with TRIzol (Life Technologies, Carlsbad, CA) following manufacturer's instructions and treated with DNaseI (Promega, Madison, WI), then cleaned up using Qiagen RNeasy columns (Qiagen, Germantown, MD). cDNA was synthesized using Omniscript (Qiagen, Germantown, MD) starting with 2–3 μg DNA-free RNA per 20 μl reaction. qPCR was performed using a 7300 FAST qPCR machine (Life Technologies, Carlsbad, CA). The primers were designed with a Tm of 60°C using Primer3 or PrimerExpress (Life Technologies, Carlsbad, CA) (Table 10). All primer pairs described in this study were confirmed as having 90–105% amplification efficiency and linear amplification within their dynamic range in experimental samples using serial dilutions of cDNA prior to the experiments. Relative transcript levels were calculated by ΔΔCt method (Livak and Schmittgen, 2001) using CβLP as internal reference.

**Table 10.**
 Primers used for qRT-PCR analyses


<table>
  <thead>
    <tr>
      <th>v4 ID</th>
      <th>v5 ID</th>
      <th>Gene name</th>
      <th>Forward</th>
      <th>Reverse</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cre01.g007300.t1.1</td>
      <td>Cre01.g007300.t1.2</td>
      <td></td>
      <td>AGCATGTGCGTGTGGAGTAG</td>
      <td>CCTTACCATAGGCCTGACCA</td>
    </tr>
    <tr>
      <td>au5.g10700_t1a</td>
      <td>Cre03.g177600.t1.3</td>
      <td></td>
      <td>CTGGACATGTCGGCTATGAA</td>
      <td>GCTCATGTCGTACTCCAGCA</td>
    </tr>
    <tr>
      <td>au5.g13389_t1*</td>
      <td>Cre06.g299700.t1</td>
      <td>SOUL1†</td>
      <td>TGCGTATGGGTGTCCACTAA</td>
      <td>TGGGGATCTTCTTCATGTCC</td>
    </tr>
    <tr>
      <td>Cre06.g263550.t1.1</td>
      <td>Cre06.g263550.t1.2</td>
      <td>LCI7</td>
      <td>TTTGGTTGCGTTGCATGTAT</td>
      <td>TCAACGCGGTGTCAAACTTA</td>
    </tr>
    <tr>
      <td>Cre06.g281250.t1.1</td>
      <td>Cre06.g281250.t1.2</td>
      <td>CFA1</td>
      <td>CCTACAACGACAACGACGTG</td>
      <td>GGAAGTTCCAGGATGACCAG</td>
    </tr>
    <tr>
      <td>Cre06.g298750.t1.1</td>
      <td>Cre06.g298750.t1.2</td>
      <td>AOT4</td>
      <td>CCGTGTGCACAGATTCAAAG</td>
      <td>CACACAGCGCCTCCTACATA</td>
    </tr>
    <tr>
      <td>Cre08.g358200.t1.2</td>
      <td>Cre08.g358200.t2.1</td>
      <td></td>
      <td>TGTGGCATCAAGGTGTGTTGT</td>
      <td>AACCCCACACCCCTCTCTTT</td>
    </tr>
    <tr>
      <td>Cre09.g398700.t1.1</td>
      <td>Cre09.g398700.t1.2</td>
      <td>CFA2</td>
      <td>CGACCTGCTGCTCTACTTCC</td>
      <td>GTGTAGGCGGTGGTCAAGAT</td>
    </tr>
    <tr>
      <td>Cre10.g458450.t1.2</td>
      <td>Cre10.g458450.t1.3</td>
      <td>GPX5</td>
      <td>AACCAATCGCCTAACACCTG</td>
      <td>CACTTGCTAGCCACGTTCAC</td>
    </tr>
    <tr>
      <td>Cre12.g503950.t1.1</td>
      <td>Cre12.g503950.t1.2</td>
      <td></td>
      <td>GGAGGGAGTACCACGAGACA</td>
      <td>GATTGCTGTAAGGCCGGATA</td>
    </tr>
    <tr>
      <td>Cre13.g564900.t1.1</td>
      <td>Cre13.g564900.t1.2</td>
      <td>MRP3</td>
      <td>TCATGACGTACATCTCGATTCTCA</td>
      <td>AGGGAATGTAGTAGCGCTGAATG</td>
    </tr>
    <tr>
      <td>au5.g4402_t1*</td>
      <td>Cre13.g566800.t1.2</td>
      <td></td>
      <td>TGCTTGGAAGACCCACTTTT</td>
      <td>GAGCTGGAGTTGCAGTTGTG</td>
    </tr>
    <tr>
      <td>Cre13.g566850.t1.1</td>
      <td>Cre13.g566850.t1.2</td>
      <td>SOUL2</td>
      <td>CCCTCCCCTCCTTCAGACTA</td>
      <td>CGTACCTGAGGCGCATATTT</td>
    </tr>
    <tr>
      <td>Cre14.g613950.t1.1</td>
      <td>Cre14.g613950.t2.1</td>
      <td></td>
      <td>CGCCCAACCCCATGATC</td>
      <td>CCGCAACGTACCGTGATG</td>
    </tr>
    <tr>
      <td>Cre16.g683400.t1.1</td>
      <td>Cre16.g683400.t1.2</td>
      <td></td>
      <td>CCTGAACAAACACACGATGG</td>
      <td>GAACGCCGTCAAATCATCTT</td>
    </tr>
    <tr>
      <td>Cre16.g688550.t1.1</td>
      <td>Cre16.g688550.t1.2</td>
      <td>GST1</td>
      <td>AGTGCGGAGGAAGTCGTAAA</td>
      <td>GTAAAAGACGTGCGTGCAAA</td>
    </tr>
    <tr>
      <td></td>
      <td>g6364.t1</td>
      <td>CβLP(RCK1)</td>
      <td>GAGTCCAACTACGGCTACGC</td>
      <td>GGTGTTCAGGTCCCACAGAC</td>
    </tr>
    <tr>
      <td>Cre14.g623650.t1.1</td>
      <td>Cre14.g623650.t1</td>
      <td></td>
      <td>GACAACGCGGCCTACAAGA</td>
      <td>CCGAGCTGGCGGTGTTAA</td>
    </tr>
    <tr>
      <td>au5.g2281_t1*</td>
      <td>g16723.t1</td>
      <td>MKS1</td>
      <td>GCTTGAGCGCGAGACGAA</td>
      <td>CGCTGAAAGCATTGCAGAAG</td>
    </tr>
    <tr>
      <td>Cre08.g380300.t1.2</td>
      <td>Cre08.g380300.t1.2</td>
      <td></td>
      <td>ACCACCAGCAGTACCTGTCC</td>
      <td>CGCTCCAATAAAGCCTTCAG</td>
    </tr>
    <tr>
      <td>au5.g7871_t1‡</td>
      <td>(Cre17.g741300.t1.2)‡</td>
      <td>SAK1(5'UTR)</td>
      <td>CAAGTGCTCATGAGAGGCCTTA</td>
      <td>TACGTCATCCAGTTCCACATCC</td>
    </tr>
    <tr>
      <td>au5.g7871_t1‡</td>
      <td>(Cre17.g741300.t1.2)‡</td>
      <td>SAK1(3'UTR)</td>
      <td>TCAAGCGTGTGGGTAAGAGCTA</td>
      <td>ACGCTATCTCCGTCCTAATCCA</td>
    </tr>
    <tr>
      <td>Cre08.g365900.t1.1</td>
      <td>Cre08.g365900.t1.2</td>
      <td>LHCSR1</td>
      <td>CACACAATTCTGCCAACAGC</td>
      <td>ATCTGCTTCACGGTTTGGTC</td>
    </tr>
    <tr>
      <td>Cre04.g220850.t1.1</td>
      <td>Cre04.g220850.t1.2</td>
      <td></td>
      <td>TAATGGTATGGATGCGGTCA</td>
      <td>ACTGCCAGTTATGGGTCCTG</td>
    </tr>
    <tr>
      <td>Cre09.g395750.t1.2</td>
      <td>Cre09.g395750.t1.3</td>
      <td></td>
      <td>ACCGTCCGTGAACCTTACTG</td>
      <td>CGCAAACACGTCTCAAAGAA</td>
    </tr>
  </tbody>
</table>

_*Was originally mapped and identified as augustus version 5 models within Chlamydomonas genome v4.†SOUL1 was given the name in v4 but not v5.‡Primers were designed against experimentally obtained cDNA (Genbank accession KF985242) and differs from v5. Closest gene model is au5.g7871_t1._

### RNA-seq library preparation and analysis

RNA was extracted (Schmollinger et al., 2014) and the quality was determined using a 2100 Bioanalyzer (Agilent Technologies, Santa Clara, CA). The triplicate RNA was pooled and 10 μg total RNA was used to prepare RNA-seq library according to the manufacturer's protocol (Illumina, San Diego, CA). The quality of the library was assessed using a 2100 Bioanalyzer before sequencing with Genome Analyzer (Illumina, San Diego, CA). Each sample was run in replicates on two lanes. RNA-Seq data was analyzed as before (Duanmu et al., 2013). On average, 75% of the sequences could be assigned unambiguously to Augustus v10.2 gene models to generate the matrix of counts per gene. This matrix was used for differential expression analysis using DESeq (Anders and Huber, 2010) using per-condition dispersion estimates and variance stabilization to compute moderate fold changes. Genes were classified as differentially expressed based on a (moderate) twofold regulation and a false discovery rate (FDR) <1%.

### Amplification of cDNA and genomic region of SAK1 and transformation of sak1

Near full-length cDNA was isolated by RT-PCR (described in above section; Gene expression analysis by qRT-PCR) and rapid amplification of cDNA ends (RACE) using GeneRACER (Life Technologies, Carlsbad, CA) as previously described (Molnar et al., 2009). Despite multiple attempts the 5′ end of the transcript could not be amplified by 5′-RACE. Because the experimentally obtained CDS differed from the most current v5, it has been deposited to genbank (accession KF985242). Though some differences exist at the nucleotide level, the protein sequence of the resulting CDS was identical to that of au5.g7871_t1. Genomic DNA containing SAK1 was amplified using primers 5′-CAGGACCGGGCACTGAGTGAAGGTTA-3′ (+) and 5′-ATGATGCACTGTGGGACACGCTGAGT-3′ (−) using PrimeStar HS with GC buffer (Takara/Clontech, Palo Alto, CA) and cloned into pGEM-Teasy after adding an adenine. The resulting plasmid was co-transformed with pBC1 and selected with 1 μM paromomycin. Transformation of sak1 was performed as described previously (Kindle et al., 1989).

### SAK1 antibody generation and protein detection by immunoblotting

To raise antibodies against SAK1, an epitope at the N-terminus of the translated coding sequence of SAK1 (DTLLTPLREDATAESGGDA) was designed, synthesized and injected into rabbits, and the resulting crude serum was affinity purified (Open Biosystems/Thermo Scientific, Waltham, MA). For immunoblot detection of SAK1, proteins were separated with NuPAGE 3–8% Tris Acetate gels (Life Technologies, Carlsbad, CA) and transferred to nitrocellulose membranes. All other blots were prepared from running the protein on 10–20% Tris-glycine gels and transferring to a PVDF membrane. The membranes were blocked for several hours in 5% milk in TBS-T, incubated with the primary antibody overnight, then with secondary antibody for several hours in 1% milk TBS-T before washing and developing with a chemiluminescence detection kit. Commercial antibodies were anti-histone H3 (ab1791; Abcam, Cambridge, UK) and anti-KDEL (ab12223; Abcam, Cambridge, UK). Other antibodies were generous gifts from Jean-David Rochaix (anti-PSAD), Olaf Kruse (anti-NAB1), and Patrice Hamel (anti-cytochrome c).

### Subcellular fractionation and protein quantification

Nuclear fractions were prepared from 450 ml of synchronized cultures with ∼2 × 106 cells ml−1 that had been incubated with or without 2 μM RB under light for 40 min. The cells were collected and treated with autolysin for 40 min and examined for the removal of cell walls by addition of 1 volume of 0.1% Triton-X. Nuclear extract was prepared as described previously (Winck et al., 2011) using CelLytic PN kit (Sigma-Aldrich, St. Louis, MO). Because there were bands detected in the nuclear extract close to the size of SAK1, nuclear extract was prepared from WT (4A+) and sak1 rather than a cell wall-deficient strain (cw15). Chloroplasts were isolated from cell wall-less strain cw15 as described previously (Klein et al., 1983). Mitochondria were isolated as described (Eriksson et al., 1995). After unbroken cells, chloroplasts, and mitochondria were collected, the ER fraction was collected by centrifugation at 100,000×g for 90 min at 4°C. The remaining supernatant was enriched for cytosol. Protein was extracted and prepared for SDS-PAGE as described (Calderon et al., 2013) with minor modifications. Protein was quantified by using BCA1 kit (Sigma-Aldrich, St. Louis, MO) after extraction with the methanol-chloroform method (Wessel and Flügge, 1984).

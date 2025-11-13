# Prediction and characterization of enzymatic activities guided by sequence similarity and genome neighborhood networks

## Authors

- Suwen Zhao<sup>1</sup>
- Ayano Sakai<sup>2</sup>
- Xinshuai Zhang<sup>2</sup>
- Matthew W Vetting<sup>3</sup>
- Ritesh Kumar<sup>2</sup>
- Brandan Hillerich<sup>3</sup>
- Brian San Francisco<sup>2</sup>
- Jose Solbiati<sup>2</sup>
- Adam Steves<sup>4</sup>
- Shoshana Brown<sup>4</sup>
- Eyal Akiva<sup>4</sup>
- Alan Barber<sup>4</sup>
- Ronald D Seidel<sup>3</sup>
- Patricia C Babbitt<sup>4</sup>
- Steven C Almo<sup>3</sup> †
- John A Gerlt<sup>2</sup> †
- Matthew P Jacobson<sup>1</sup> †

### Affiliations

1. Department of Pharmaceutical Chemistry University of California, San Francisco San Francisco United States
2. Institute for Genomic Biology University of Illinois at Urbana-Champaign Urbana United States
3. Department of Biochemistry Albert Einstein College of Medicine New York United States
4. Department of Bioengineering and Therapeutic Sciences University of California, San Francisco San Francisco United States
5. Department of Biochemistry University of Illinois at Urbana-Champaign Urbana United States
6. Department of Chemistry University of Illinois at Urbana-Champaign Urbana United States

† Corresponding author

## Abstract

Metabolic pathways in eubacteria and archaea often are encoded by operons and/or gene clusters (genome neighborhoods) that provide important clues for assignment of both enzyme functions and metabolic pathways. We describe a bioinformatic approach (genome neighborhood network; GNN) that enables large scale prediction of the in vitro enzymatic activities and in vivo physiological functions (metabolic pathways) of uncharacterized enzymes in protein families. We demonstrate the utility of the GNN approach by predicting in vitro activities and in vivo functions in the proline racemase superfamily (PRS; InterPro IPR008794). The predictions were verified by measuring in vitro activities for 51 proteins in 12 families in the PRS that represent ~85% of the sequences; in vitro activities of pathway enzymes, carbon/nitrogen source phenotypes, and/or transcriptomic studies confirmed the predicted pathways. The synergistic use of sequence similarity networks3 and GNNs will facilitate the discovery of the components of novel, uncharacterized metabolic pathways in sequenced genomes.

## Introduction

The explosion in the number of sequenced eubacterial and archaeal genomes provides a challenge for the biological community: >50% of the proteins/enzymes so identified have uncertain or unknown in vitro activities and in vivo physiological functions. Genome context can provide important clues for assignment of functions to individual enzymes and, also, guide the discovery of novel metabolic pathways: pathways often are encoded by operons and/or gene clusters. However, large-scale approaches are required to efficiently mine this information for entire protein/enzyme families (Dehal et al., 2010; Caspi et al., 2012; Markowitz et al., 2012; Franceschini et al., 2013; Overbeek et al., 2014).

In this manuscript, we describe the use of a new bioinformatic strategy, genome neighborhood networks (GNNs), to discover the enzymes, transport systems, and transcriptional regulators that constitute metabolic pathways, thereby facilitating prediction of their individual in vitro activities and combined in vivo metabolic functions. As the first demonstration of its use, we applied this approach to the functionally diverse proline racemase superfamily (PRS) and predicted functions for >85% of its members. The predictions were verified using high-throughput protein expression and purification, in vitro enzyme activity measurements, microbiology (phenotypes and transcriptomics), and X-ray crystallography.

Three enzymatic activities have been described for the PRS: proline racemase (ProR; eubacteria [Stadtman et al., 1957] and eukaryotes [Reina-San-Martín et al., 2000], 4R-hydroxyproline 2-epimerase (4HypE; eubacteria [Adams and Frank, 1980; Goytia et al., 2007; Gavina et al., 2010]), and trans 3-hydroxy-L-proline dehydratase (t3HypD; eukaryotes [Visser et al., 2012] and eubacteria [Watanabe et al., 2014]); these reactions and the pathways in which they participate are shown in Figure 1. The previously characterized ProRs and 4HypEs catalyze racemization/epimerization of the a-carbon in a 1,1-proton transfer mechanism that, in the structurally characterized enzymes, uses two general acidic/basic Cys residues located on opposite faces of the active site (Buschiazzo et al., 2006; Rubinstein and Major, 2009). The syn-dehydration reaction catalyzed by t3HypD requires a general basic catalyst to abstract the proton from the a-carbon; its conjugate acid likely functions as the general acidic catalyst to facilitate departure of the 3-hydroxyl group. Sequence alignment of the functionally characterized t3HypDs and ProRs suggests the presence of a single active site Cys residue in the active sites of the t3HypDs (the second Cys in ProR is replaced by a Thr residue).

![Figure 1.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig1-v2.jpg)

**Figure 1.:** cHyp oxidase, Pyr4H2C deaminase, a-KGSA dehydrogenase, and ?1-Pyr2C reductase belong to the D-amino acid oxidase (DAAO), dihydrodipicolinate synthase (DHDPS), aldehyde dehydrogenase, and ornithine cyclodeaminase (OCD) (or malate/L-lactate dehydrogenase 2 [MLD2]) superfamilies, respectively. Abbreviations: L-Pro: L-proline; D-Pro: D-proline; 5-AV: 5-aminovalerate; t4Hyp: trans-4-hydroxy-L-proline; c4Hyp: cis-4-hydroxy-D-proline; Pyr4H2C: ?1-pyrroline 4-hydroxy 2-carboxylate; a-KGSA: a-ketoglutarate semialdehyde; a-KG: a-ketoglutarate; t3Hyp: trans-3-hyroxy-L-proline; ?2-Pyr2C: ?2-pyrroline 2-carboxylate; ?1-Pyr2C: ?1-pyrroline 2-carboxylate.

## Results

### Sequence similarity network for the PRS

A sequence similarity network (SSN) (Atkinson et al., 2009) for 2333 unique sequences in the PRS (InterPro family IPR008794; release 43.0) was constructed and displayed at various e-value thresholds (Figure 2). When the network is displayed with an e-value threshold of 10-55 (> ~35% sequence identity is required to draw an edge [line] between nodes [proteins]), the majority of the members of the PRS are located in a single functionally heterogeneous cluster (Figure 2A). As the e-value threshold stringency is increased to 10-110 (sequence identity required to draw an edge is increased to > ~60%), the PRS separates into 28 clusters and 49 singletons (Figure 2B). For analyses of the genome neighborhoods (vide infra), each cluster in the 10-110 network was assigned a unique color and number as shown in Figure 2B (the node colors in Figure 2A depict their association with the clusters in Figure 2B).

![Figure 2.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig2-v2.jpg)

**Figure 2.:** (A) The SSN displayed with an e-value threshold of 10-55 (~35% sequence identity). (B) The SSN displayed with an e-value threshold of 10-110 (~60% sequence identity).

At the e-value threshold of 10-110 (Figure 2B) the nodes for the experimentally characterized functions—ProR (magenta; cluster 7), 4HypE (blue and red; clusters 1 and 2, respectively), and t3HypD (brown; cluster 8)—are located in separate clusters that account for ~30% of the sequences in the PRS. When the e-value threshold is relaxed to 10-55, most of the clusters merge, although the nodes associated with the two previously characterized 4HypE clusters in the 10-110 network remain separated. Sequence alignments predict that the active sites of both characterized 4HypE clusters contain two active site Cys residues. We conclude that these two families of 4HypEs evolved from divergent, but homologous, ancestors.

At the e-value threshold of 10-110 (Figure 2B), the separated clusters are expected to be isofunctional because, from sequence alignments, their active sites are formed from conserved amino acid residues (acid/base catalysts and specificity determining residues). Although many of the clusters are predicted to have the two active site Cys residues found in the structurally characterized ProR (PDB: 1W61) and 4HypE (PDB: 2AZP [Liu et al.]), others are missing one or both of the Cys residues. The previously uncharacterized enzymes with differing residues could either represent new functions or additional examples of evolution of the ProR, 4HypE, and t3HypD functions from divergent, but homologous, ancestors.

### GNN for the PRS

We predicted functions for ~80% of the remaining members of the PRS by analyzing the SSN for the proteins (including enzymes, transport systems, and transcriptional regulators) encoded by the genome neighborhoods for ‘all’ members of the PRS (specifically, ± 10 genes relative to the gene encoding each PRS member, the query). A protein in this genome neighborhood SSN, designated the ‘genome neighborhood network’ (GNN), is expected to be functionally related to a query in the PRS if they are located in an operon and/or gene cluster that encodes a metabolic pathway that includes the query. By analyzing many genome neighborhoods simultaneously, e.g., for all members of the PRS, the signals associated with functionally related proteins will be amplified; the signals associated with functionally unrelated genome proximal proteins that occur ‘randomly’ across many species will contribute to the background ‘noise’. We propose that this large-scale approach is more efficient in identifying ‘all’ of the enzymes/transport systems/transcriptional regulators in a conserved metabolic pathway than by a one-genome-at-a-time analysis.

Our approach for visualizing a GNN first assigns a unique query color and number to the members of each cluster in the input SSN that separates the members of the PRS into clusters that are likely to be isofunctional (e-110 in this work). After collecting the genome neighbors, we assign each of them the same color as the color of the query; with this strategy, proteins that are encoded by the same genome neighborhood as the query are easily identified in the GNN because they share the same color as the query. We then perform an all-by-all BLAST on the sequences of the genome neighbors and display the results as an SSN using an e-value threshold of 10-20; this SSN is the GNN. Using this e-value threshold, most of the clusters in the GNN contain the members of distinct protein families and superfamilies (e.g., Pfam families); however, in some cases, divergent families in functionally diverse superfamilies may be found in separate clusters. Genome neighborhood proteins that occur randomly across divergent species and are functionally unrelated to the queries are expected to be located in small clusters with multiple colors, so these can be quickly identified visually and discarded from further analysis. The PRS queries from the input SSN (‘zero sequences’ in collecting the ±10 neighbors) are not displayed in the GNN, except when multiple members of the PRS are proximal on the genome, that is, when one PRS member is in the genome neighborhood of another (vide infra).

The GNN for the PRS (Figure 3A) contains many clusters (protein families). In some clusters, all of the nodes have the same color, that is, they are identified by a single query cluster in the SSN (e.g., the clusters in Figure 3B,C). However, in most clusters the nodes have multiple colors, that is, they are identified by several query clusters in the SSN (e.g., the clusters in Figure 3D–H); this suggests that different query clusters in the SSN have the same in vitro activity and in vivo metabolic function. The clusters in the GNN (Figure 3A) are labeled with their Pfam annotations. The ligand/substrate specificities and/or reaction mechanisms that characterize these families are then used to predict the individual in vitro activities and the shared metabolic pathway identified by a query cluster.

![Figure 3.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig3-v2.jpg)

**Figure 3.:** (A) The GNN displayed with an e-value threshold of 10-20. The nodes are colored by the color of query nodes in the SSN (Figure 2A). The clusters are labeled with the UniProtKB/TrEMBL annotations. (B–I) Selected superfamily clusters from the GNN showing node colors. (B) D-proline reductase PrdA. (C) D-proline reductase, PrdB. (D) D-amino acid oxidase (DAAO). (E) Dihydrodipicolinate synthase (DHDPS). (F) Aldehyde dehydrogenase. (G) Ornithine cyclodeaminase (OCD). (H) Malate/L-lactate dehydrogenase 2 (MLD2). (I) Proline racemase.

### Retrospective tests of GNN: ProR and 4HypE functions

As a retrospective use of the GNN, the ProR function is encoded by anaerobic eubacteria that ferment L-proline and is represented by the magenta cluster (cluster 7) in the SSN (Figure 2B). The first step in the catabolism of L-proline is racemization to D-proline (by ProR) that is reduced to 2-keto-5-aminopentanoate by D-proline reductase (Kabisch et al., 1999) (by PrdAB; Figure 1). In the GNN, the clusters for the PrdA and PrdB polypeptides in D-proline reductase are uniformly magenta, as expected if the genes encoding ProR and PrdAB are colocalized with the gene encoding ProR (Figure 3B,C). The lack of other colors in the PrdAB clusters in the GNN implies that no other clusters in the SSN have the ProR function.

As a second retrospective example, the 4HypE function has been assigned to members of the blue (cluster 1) and red (cluster 2) clusters in the SSN (Figure 2B). In the GNN, clusters identified by the blue and red clusters include the D-amino acid oxidase (DAAO; Figure 3D) (Watanabe et al., 2012), dihydrodipicolinate synthase (DHDPS; Figure 3E) (Singh and Adams, 1965; Watanabe et al., 2012), and aldehyde dehydrogenase (Figure 3F) (Koo and Adams, 1974; Watanabe et al., 2007) superfamilies as well as components of several types of transport systems. As we and others recently established for organisms that use trans-4-hydroxy-L-proline betaine as sole carbon and nitrogen source (Zhao et al., 2013; Kumar et al., 2014), the catabolic pathway for trans-4-hydroxy-L-proline (t4Hyp) (Figure 1) can be initiated by the epimerization of t4Hyp to cis-4-hydroxy-D-proline (c4Hyp) by 4HypE, followed by reactions catalyzed by c4Hyp oxidase (a member of the DAAO superfamily), c4Hyp imino acid dehydratase/deaminase (a member of the DHDPS superfamily), and a-ketoglutarate semialdehyde dehydrogenase (a member of the aldehyde dehydrogenase superfamily). Thus, the occurrence of blue and red nodes in these three clusters in the GNN is expected.

### Discovery of new families of 4HypEs

The DAAO (Figure 3D), DHDPS (Figure 3E), and aldehyde dehydrogenase (Figure 3F) clusters also contain nodes with other colors from the SSN (Figure 2B), including orange (cluster 9), pale green (cluster 11), and teal (cluster 4). Proteins from the orange and pale green clusters were purified and assayed using a library of proline derivatives (Figure 4). As expected, members of the orange and pale green clusters catalyze the 4HypE reaction (Tables 1 and 2). We were unable to purify proteins from the teal cluster (insolubility), so we used the growth phenotypes of the encoding organisms and transcriptomics to identify their in vitro enzymatic activities and in vivo metabolic functions. As predicted from the GNN, Bacillus cereus ATCC14579 (cluster 4, teal) and Streptomyces lividans TK24 (cluster 11, pale green) both utilize t4Hyp as sole carbon source (Table 3); also, the genes encoding the predicted 4HypEs (Table 4) and the proximal genes encoding the predicted c4Hyp oxidases, c4Hyp imino acid dehydratase/deaminases, and a-ketoglutarate semialdehyde dehydrogenases (Table 5) are up-regulated when the encoding organism is grown on t4Hyp as carbon source (Table 4). The purified proteins from the orange groups are promiscuous for the 3HypE reaction (Tables 1 and 2), but their genome neighborhood context identifies their physiological functions as 4HypE.

![Figure 4.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig4-v2.jpg)

**Figure 4.:** These substrates were divided into four groups to avoid mass duplication.

**Table 1.**
 Mass spectroscopy screening results in D2O. Hits were observed by mass shift for racemization/epimerization (+1) and dehydration (-17) for reactions performed


<table>
  <thead>
    <tr>
      <th>Locus tag</th>
      <th>UniProt</th>
      <th>L-Pro</th>
      <th>D-Pro</th>
      <th>t4Hyp</th>
      <th>c4Hyp</th>
      <th>t3Hyp</th>
      <th>cis-3-OH-L-Pro</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cluster 1: blue</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Pden_4859</td>
      <td>A3QFI1</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Shew_2363</td>
      <td>A9AQW9</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Bmul_5265</td>
      <td>A6WXX7</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>Oant_1111</td>
      <td>D2QN44</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>Slin_1478</td>
      <td>B9JHU6</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>Arad_8151</td>
      <td>Q8FYS0</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>BR1792</td>
      <td>A1BBM5</td>
      <td>0</td>
      <td>0</td>
      <td>+ 1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>Cluster 2: red</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>A1S_1325</td>
      <td>A3M4A9</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>Bamb_3550</td>
      <td>Q0B9R9</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>BceJ2315_47180</td>
      <td>B4EHE6</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>BMULJ_04062</td>
      <td>B3D6W2</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>BTH_II2067</td>
      <td>Q2T3J4</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>-17</td>
      <td>0</td>
    </tr>
    <tr>
      <td>CV_2826</td>
      <td>Q7NU77</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>Csal_2705</td>
      <td>Q1QU06</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>PFL_1412</td>
      <td>A5VZY6</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>Pput_1285</td>
      <td>Q1QBF3</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>Pcryo_1219</td>
      <td>A3M4A9</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>XCC2415</td>
      <td>Q8P833</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>Bmul_4447</td>
      <td>A9AL52</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>ABAYE2385</td>
      <td>B0VB44</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>BURPS1106B_1521</td>
      <td>C5ZMD2</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>BURPS1710b_A1887</td>
      <td>Q3JHA9</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>PA1268</td>
      <td>Q9I476</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Cluster 3: ligthskyblue</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Pden_1184</td>
      <td>A1B195</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>-17</td>
      <td>0</td>
    </tr>
    <tr>
      <td>SIAM614_28502</td>
      <td>A0NXQ9</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>-17</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Atu4684</td>
      <td>A9CH01</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>-17</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Avi_7022</td>
      <td>B9K4G4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>-17</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Oant_0439</td>
      <td>A6WW16</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>SM_b20270</td>
      <td>Q92WR9</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>-17</td>
      <td>0</td>
    </tr>
    <tr>
      <td>BMEI1586</td>
      <td>Q8YFD6</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>BR0337</td>
      <td>Q8G2I3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>-17</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Cluster 5: navy</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>BC_0905</td>
      <td>Q81HB1</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>-17</td>
      <td>0</td>
    </tr>
    <tr>
      <td>BCE_0994</td>
      <td>Q73CS0</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>-17</td>
      <td>0</td>
    </tr>
    <tr>
      <td>BT9727_0799</td>
      <td>Q6HMS9</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>-17</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Cluster 9: orange</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Avi_0518</td>
      <td>B9JQV3</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>Atu0398</td>
      <td>A9CKB4</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>RHE_CH00452</td>
      <td>Q2KD13</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>Arad_0731</td>
      <td>B9J8G8</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>Cluster 11: palegreen</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sros_6004</td>
      <td>D2AV87</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Cluster 12: olive</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bamb_3769</td>
      <td>Q0B950</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>-17</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Bmul_4260</td>
      <td>A9AKG8</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>Cluster 16: salmon</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Csal_2339</td>
      <td>Q1QV19</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Maqu_2141</td>
      <td>A1U2K1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Cluster 17: lime</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Rsph17029_3164</td>
      <td>A3PPJ8</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>RSP_3519</td>
      <td>Q3IWG2</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Cluster 18: cyan</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>SIAM614_28492</td>
      <td>A0NXQ7</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>SADFL11_2813</td>
      <td>B9R4E3</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>SPOA0266</td>
      <td>Q5LKW3</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
    <tr>
      <td>Cluster 22: steelblue</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Spea_1705</td>
      <td>A8H392</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>-17</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Swoo_2821</td>
      <td>B1KJ76</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>-17</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Cluster 61:</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Plim_2713</td>
      <td>D5SQS4</td>
      <td>0</td>
      <td>0</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
      <td>+1</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Kinetic constants for 3/4HypE and t3HypD activities of the screened PRS targets


<table>
  <thead>
    <tr>
      <th>Cluster</th>
      <th>Locus tag</th>
      <th>UniProt</th>
      <th>Function</th>
      <th>kcat [s-1]</th>
      <th>Km [mM]</th>
      <th>kcat/KM[M-1s-1]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="6">1</td>
      <td>Pden_4859</td>
      <td>A1BBM5</td>
      <td>4HypE</td>
      <td>16 ± 2</td>
      <td>25 ± 5</td>
      <td>630</td>
    </tr>
    <tr>
      <td>Shew_2363</td>
      <td>A3QFI1</td>
      <td>4HypE</td>
      <td>50 ± 6</td>
      <td>12 ± 3</td>
      <td>4000</td>
    </tr>
    <tr>
      <td rowspan="2">Bmul_5265</td>
      <td rowspan="2">A9AQW9</td>
      <td>3HypE</td>
      <td>0.34 ± 0.03</td>
      <td>- a</td>
      <td>- a</td>
    </tr>
    <tr>
      <td>4HypE</td>
      <td>5.6 ± 0.5</td>
      <td>11 ± 2</td>
      <td>530</td>
    </tr>
    <tr>
      <td rowspan="2">Oant_1111</td>
      <td rowspan="2">A6WXX7</td>
      <td>3HypE</td>
      <td>2.4 ± 0.2</td>
      <td>31 ± 7</td>
      <td>77</td>
    </tr>
    <tr>
      <td>4HypE</td>
      <td>89 ± 2</td>
      <td>7.1 ± 0.6</td>
      <td>13000</td>
    </tr>
    <tr>
      <td rowspan="9">2</td>
      <td rowspan="2">BTH_II2067</td>
      <td rowspan="2">Q2T3J4</td>
      <td>t3HypD</td>
      <td>17 ± 3</td>
      <td>26 ± 9</td>
      <td>660</td>
    </tr>
    <tr>
      <td>4HypE</td>
      <td>40 ± 4</td>
      <td>1.4 ± 0.4</td>
      <td>28000</td>
    </tr>
    <tr>
      <td rowspan="2">CV_2826</td>
      <td rowspan="2">Q7NU77</td>
      <td>3HypE</td>
      <td>30 ± 0.6</td>
      <td>57 ± 4</td>
      <td>520</td>
    </tr>
    <tr>
      <td>4HypE</td>
      <td>70 ± 7</td>
      <td>6.8 ± 3</td>
      <td>10000</td>
    </tr>
    <tr>
      <td rowspan="3">Pput_1285</td>
      <td rowspan="3">A5VZY6</td>
      <td>3HypE</td>
      <td>4.8 ± 0.6</td>
      <td>19 ± 5</td>
      <td>250</td>
    </tr>
    <tr>
      <td>4HypE</td>
      <td>26 ± 0.7</td>
      <td>0.54 ± 0.08</td>
      <td>48000</td>
    </tr>
    <tr>
      <td>ProR</td>
      <td>2.8 ± 0.1</td>
      <td>200 ± 20</td>
      <td>14</td>
    </tr>
    <tr>
      <td rowspan="2">XCC2415</td>
      <td rowspan="2">Q8P833</td>
      <td>4HypE</td>
      <td>28 ± 0.4</td>
      <td>0.67 ± 0.05</td>
      <td>42000</td>
    </tr>
    <tr>
      <td>3HypE</td>
      <td>1.3 ± 0.07</td>
      <td>15 ± 3</td>
      <td>86</td>
    </tr>
    <tr>
      <td rowspan="11">3</td>
      <td>Pden_1184</td>
      <td>A1B195</td>
      <td>t3HypD</td>
      <td>nd b</td>
      <td>nd b</td>
      <td>nd b</td>
    </tr>
    <tr>
      <td>SIAM614_28502</td>
      <td>A0NXQ9</td>
      <td>t3HypD</td>
      <td>15 ± 0.9</td>
      <td>7.8 ± 1</td>
      <td>1900</td>
    </tr>
    <tr>
      <td rowspan="2">Atu4684</td>
      <td rowspan="2">A9CH01</td>
      <td>t3HypD</td>
      <td>27 ± 1</td>
      <td>4.2 ± 0.8</td>
      <td>6300</td>
    </tr>
    <tr>
      <td>4HypE</td>
      <td>0.40 ± 0.02</td>
      <td>2.0 ± 0.3</td>
      <td>200</td>
    </tr>
    <tr>
      <td>Avi_7022</td>
      <td>B9K4G4</td>
      <td>t3HypD</td>
      <td>4.3 ± 0.4</td>
      <td>15 ± 3</td>
      <td>280</td>
    </tr>
    <tr>
      <td>Oant_0439</td>
      <td>A6WW16</td>
      <td>4HypE</td>
      <td>0.064 ± 0.002</td>
      <td>1.3 ± 0.2</td>
      <td>49</td>
    </tr>
    <tr>
      <td rowspan="2">SM_b20270</td>
      <td rowspan="2">Q92WR9</td>
      <td>t3HypD</td>
      <td>7.9 ± 0.2</td>
      <td>3.8 ± 0.4</td>
      <td>2100</td>
    </tr>
    <tr>
      <td>4HypE</td>
      <td>0.089 ± 0.01</td>
      <td>6.3 ± 2</td>
      <td>14</td>
    </tr>
    <tr>
      <td rowspan="2">BMEI1586</td>
      <td rowspan="2">D0B556</td>
      <td>3HypE</td>
      <td>0.085 ± 0.003</td>
      <td>2.6 ± 0.4</td>
      <td>33</td>
    </tr>
    <tr>
      <td>4HypE</td>
      <td>0.082 ± 0.005</td>
      <td>4.5 ± 1</td>
      <td>18</td>
    </tr>
    <tr>
      <td>BR0337</td>
      <td>Q8G2I3</td>
      <td>t3HypD</td>
      <td>17 ± 2</td>
      <td>5.1 ± 2</td>
      <td>3300</td>
    </tr>
    <tr>
      <td rowspan="4">5</td>
      <td rowspan="2">BCE_0994</td>
      <td rowspan="2">Q73CS0</td>
      <td>t3HypD</td>
      <td>nd b</td>
      <td>nd b</td>
      <td>nd b</td>
    </tr>
    <tr>
      <td>4HypE</td>
      <td>1.2 ± 0.03</td>
      <td>3.2 ± 0.3</td>
      <td>370</td>
    </tr>
    <tr>
      <td rowspan="2">BT9727_0799</td>
      <td rowspan="2">Q6HMS9</td>
      <td>t3HypD</td>
      <td>23 ± 5</td>
      <td>7.5 ± 3</td>
      <td>3100</td>
    </tr>
    <tr>
      <td>4HypE</td>
      <td>0.16</td>
      <td>- a</td>
      <td>- a</td>
    </tr>
    <tr>
      <td rowspan="6">9</td>
      <td rowspan="2">Avi_0518</td>
      <td rowspan="2">B9JQV3</td>
      <td>3HypE</td>
      <td>0.75 ± 0.04</td>
      <td>4.8 ± 0.9</td>
      <td>160</td>
    </tr>
    <tr>
      <td>4HypE</td>
      <td>1.3 ± 0.07</td>
      <td>5.6 ± 0.5</td>
      <td>230</td>
    </tr>
    <tr>
      <td rowspan="2">Atu0398</td>
      <td rowspan="2">A9CKB4</td>
      <td>3HypE</td>
      <td>4.0 ± 0.6</td>
      <td>25 ± 7</td>
      <td>160</td>
    </tr>
    <tr>
      <td>4HypE</td>
      <td>0.86 ± 0.1</td>
      <td>4.6 ± 2</td>
      <td>190</td>
    </tr>
    <tr>
      <td>RHE_CH00452</td>
      <td>Q2KD13</td>
      <td>3HypE</td>
      <td>0.94 ± 0.06</td>
      <td>2.1 ± 0.7</td>
      <td>450</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4HypE</td>
      <td>1.9 ± 0.08</td>
      <td>2.1 ± 0.3</td>
      <td>880</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Sros_6004</td>
      <td>D2AV87</td>
      <td>4HypE</td>
      <td>14 ± 0.8</td>
      <td>7.8 ± 1</td>
      <td>1800</td>
    </tr>
    <tr>
      <td rowspan="3">12</td>
      <td>Bamb_3769</td>
      <td>Q0B950</td>
      <td>t3HypD</td>
      <td>43 ± 4</td>
      <td>13 ± 3</td>
      <td>3400</td>
    </tr>
    <tr>
      <td rowspan="2">Bmul_4260</td>
      <td rowspan="2">A9AKG8</td>
      <td>3HypE</td>
      <td>30 ± 1</td>
      <td>18 ± 2</td>
      <td>1700</td>
    </tr>
    <tr>
      <td>4HypE</td>
      <td>1.3 ± 0.04</td>
      <td>2.7 ± 0.3</td>
      <td>470</td>
    </tr>
    <tr>
      <td>16</td>
      <td>Csal_2339</td>
      <td>Q1QV19</td>
      <td>4HypE</td>
      <td>0.070 ± 0.005</td>
      <td>2.5 ± 0.7</td>
      <td>28</td>
    </tr>
    <tr>
      <td rowspan="2">17</td>
      <td>RSP_3519</td>
      <td>Q3IWG2</td>
      <td>4HypE</td>
      <td>nd b</td>
      <td>nd b</td>
      <td>nd b</td>
    </tr>
    <tr>
      <td>Rsph17029_3164</td>
      <td>A3PPJ8</td>
      <td>4HypE</td>
      <td>nd b</td>
      <td>nd b</td>
      <td>nd b</td>
    </tr>
    <tr>
      <td rowspan="2">18</td>
      <td>SIAM614_28492</td>
      <td>A0NXQ7</td>
      <td>4HypE</td>
      <td>55 ± 3</td>
      <td>3.2 ± 0.5</td>
      <td>17000</td>
    </tr>
    <tr>
      <td>SADFL11_2813</td>
      <td>B9R4E3</td>
      <td>4HypE</td>
      <td>67 ± 5</td>
      <td>4.1 ± 0.8</td>
      <td>16000</td>
    </tr>
    <tr>
      <td rowspan="2">22</td>
      <td>Spea_1705</td>
      <td>A8H392</td>
      <td>t3HypD</td>
      <td>0.15 ± 0.03</td>
      <td>- b</td>
      <td>- b</td>
    </tr>
    <tr>
      <td>Swoo_2821</td>
      <td>B1KJ76</td>
      <td>t3HypD</td>
      <td>4.1 ± 0.4</td>
      <td>6.7 ± 2</td>
      <td>600</td>
    </tr>
  </tbody>
</table>

_aThe reaction is to slow to measure Km.bThe reaction is slow to measure kinetic parameters._

**Table 3.**
 Growth phenotypes of bacterial strains when grown on the indicated carbon sources


<table>
  <thead>
    <tr>
      <th>Organism</th>
      <th>t4Hyp</th>
      <th>c4Hyp</th>
      <th>t3Hyp</th>
      <th>cis-3-OH-L-proline</th>
      <th>L-Pro</th>
      <th>D-glucose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Agrobacterium tumefaciens C58</td>
      <td>++</td>
      <td>++</td>
      <td>+</td>
      <td>-</td>
      <td>+++</td>
      <td>+++</td>
    </tr>
    <tr>
      <td>Sinorhizobium meliloti 1021</td>
      <td>++</td>
      <td>++</td>
      <td>+</td>
      <td>-</td>
      <td>+++</td>
      <td>+++</td>
    </tr>
    <tr>
      <td>Labrenzia aggregate IAM12614</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+++</td>
      <td>+++</td>
    </tr>
    <tr>
      <td>Pseudomonas aeruginosa PAO1</td>
      <td>++</td>
      <td>++</td>
      <td>+</td>
      <td>-</td>
      <td>+++</td>
      <td>+++</td>
    </tr>
    <tr>
      <td>Paracoccus denitrificans PD1222</td>
      <td>+++</td>
      <td>+++</td>
      <td>+</td>
      <td>+</td>
      <td>+++</td>
      <td>+++</td>
    </tr>
    <tr>
      <td>Rhodobacter sphaeroides 2.4.1</td>
      <td>+</td>
      <td>+</td>
      <td>-</td>
      <td>-</td>
      <td>+++</td>
      <td>+++</td>
    </tr>
    <tr>
      <td>Rhodobacter sphaeroides 2.4.1?RSP3519</td>
      <td>-</td>
      <td>+</td>
      <td>-</td>
      <td>-</td>
      <td>+++</td>
      <td>+++</td>
    </tr>
    <tr>
      <td>Bacillus cereus ATCC14579</td>
      <td>++</td>
      <td>++</td>
      <td>+</td>
      <td>+</td>
      <td>+++</td>
      <td>+++</td>
    </tr>
    <tr>
      <td>Roseovarius nubinhibens ISM</td>
      <td>++</td>
      <td>++</td>
      <td>+</td>
      <td>-</td>
      <td>+++</td>
      <td>+++</td>
    </tr>
    <tr>
      <td>Escherichia coli MG1655</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>+++</td>
      <td>+++</td>
    </tr>
    <tr>
      <td>Streptomyces lividans TK24</td>
      <td>+++</td>
      <td>++</td>
      <td>+</td>
      <td>ND</td>
      <td>+++</td>
      <td>+++</td>
    </tr>
  </tbody>
</table>

_‘+++’ represents robust growth (like growth on D-glucose); ++/+ represents slow growth phenotype; ‘--’ represents growth-deficient phenotype; ‘ND’, not determined_

**Table 4.**
 Transcriptional analysis of PRS members


<table>
  <thead>
    <tr>
      <th>Organism/Locus Tag</th>
      <th>t4Hyp</th>
      <th>t3Hyp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3">Agrobacterium tumefaciens C58</td>
    </tr>
    <tr>
      <td>A9CKB4</td>
      <td>12 ± 2</td>
      <td>11 ± 1.5</td>
    </tr>
    <tr>
      <td>A9CFV0</td>
      <td>3 ± 1</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>A9CH01</td>
      <td>64 ± 5</td>
      <td>32 ± 4</td>
    </tr>
    <tr>
      <td colspan="3">Sinorhizobium meliloti 1021</td>
    </tr>
    <tr>
      <td>Q92WS1</td>
      <td>5 ± 1</td>
      <td>3 ± 1</td>
    </tr>
    <tr>
      <td>Q92WR9</td>
      <td>5.5 ± 1.5</td>
      <td>3.5 ± 1</td>
    </tr>
    <tr>
      <td colspan="3">Labrenzia aggregate IAM12614</td>
    </tr>
    <tr>
      <td>A0NXQ7</td>
      <td>22 ± 2</td>
      <td>5 ± 1</td>
    </tr>
    <tr>
      <td>A0NXQ9</td>
      <td>12 ± 2</td>
      <td>6 ± 2</td>
    </tr>
    <tr>
      <td colspan="3">Pseudomonas aeruginosa PAO1</td>
    </tr>
    <tr>
      <td>Q9I489</td>
      <td>8 ± 2</td>
      <td>5 ± 1</td>
    </tr>
    <tr>
      <td>Q9I476</td>
      <td>35 ± 3</td>
      <td>7 ± 2</td>
    </tr>
    <tr>
      <td colspan="3">Paracoccus denitrificans PD1222</td>
    </tr>
    <tr>
      <td>A1B0W2</td>
      <td>2.0 ± 0.5</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>A1B195</td>
      <td>NC</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>A1B7P4</td>
      <td>NC</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>A1BBM5</td>
      <td>4.5 ± 0.5</td>
      <td>NC</td>
    </tr>
    <tr>
      <td colspan="3">Rhodobacter sphaeroides 2.4.1</td>
    </tr>
    <tr>
      <td>Q3IWG2</td>
      <td>10 ± 1</td>
      <td>NC</td>
    </tr>
    <tr>
      <td colspan="3">Bacillus cereus ATCC14579</td>
    </tr>
    <tr>
      <td>Q81HB1</td>
      <td>4 ± 1</td>
      <td>4.5 ± 1</td>
    </tr>
    <tr>
      <td>Q81CD7</td>
      <td>22 ± 2</td>
      <td>18 ± 3</td>
    </tr>
    <tr>
      <td colspan="3">Roseovarius nubinhibens ISM</td>
    </tr>
    <tr>
      <td>A3SLP2</td>
      <td>12 ± 2</td>
      <td>4+1.5</td>
    </tr>
  </tbody>
</table>

_Fold change in expression for each gene when grown on the indicated carbon source, relative to growth on D-glucose. The identities of the bacterial species and the protein encoded by each gene are indicated. Fold-changes are the averages of five biological replicates with standard deviation (p value < 0.005). NC, no change._

**Table 5.**
 Transcriptional analysis of genome neighborhoods


<table>
  <thead>
    <tr>
      <th>Organism/Locus tag</th>
      <th>UniProt</th>
      <th>Enzyme</th>
      <th>Cluster</th>
      <th>t4Hyp</th>
      <th>t3Hyp</th>
      <th>L-Pro</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2">Bacillus cereus ATCC 14579</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bc_0905</td>
      <td>Q81HB1</td>
      <td>ProR</td>
      <td>navy</td>
      <td>121 ± 11</td>
      <td>87 ± 10</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Bc_0906</td>
      <td>Q81HB0</td>
      <td>OCD</td>
      <td></td>
      <td>20 ± 3</td>
      <td>14 ± 2</td>
      <td>NC</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bc_2832</td>
      <td>Q81CE0</td>
      <td>ALDH</td>
      <td></td>
      <td>630 ± 39</td>
      <td>625 ± 57</td>
      <td>13 ± 2</td>
    </tr>
    <tr>
      <td>Bc_2833</td>
      <td>Q81CD9</td>
      <td>DHDPS</td>
      <td></td>
      <td>644 ± 61</td>
      <td>498 ± 37</td>
      <td>6 ± 0.7</td>
    </tr>
    <tr>
      <td>Bc_2834</td>
      <td>Q81CD8</td>
      <td>ProR</td>
      <td>hot pink</td>
      <td>594 ± 27</td>
      <td>485 ± 29</td>
      <td>8 ± 1</td>
    </tr>
    <tr>
      <td>Bc_2835</td>
      <td>Q81CD7</td>
      <td>ProR</td>
      <td>teal</td>
      <td>408 ± 15</td>
      <td>567 ± 33</td>
      <td>5 ± 0.5</td>
    </tr>
    <tr>
      <td>Bc_2836</td>
      <td>Q81CD6</td>
      <td>oxidase</td>
      <td></td>
      <td>623 ± 37</td>
      <td>633 ± 42</td>
      <td>10 ± 0.6</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Streptomyces lividans TK24</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>SSPG_01342</td>
      <td>D6EJL0</td>
      <td>DAAO</td>
      <td></td>
      <td>81 ± 5</td>
      <td>20 ± 5</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>SSPG_01341</td>
      <td>D6EJK9</td>
      <td>oxidase</td>
      <td></td>
      <td>65 ± 9</td>
      <td>6 ± 0.2</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>SSPG_01340</td>
      <td>D6EJK8</td>
      <td>oxidase</td>
      <td></td>
      <td>225 ± 22</td>
      <td>30 ± 3</td>
      <td>3 ± 0.4</td>
    </tr>
    <tr>
      <td>SSPG_01339</td>
      <td>D6EJK7</td>
      <td>DHDPS</td>
      <td></td>
      <td>136 ± 5</td>
      <td>16 ± 0.2</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>SSPG_01338</td>
      <td>D6EJK6</td>
      <td>ProR</td>
      <td>palegreen</td>
      <td>171 ± 8</td>
      <td>23 ± 1</td>
      <td>3 ± 0.2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Agrobacterium tumefaciens C58</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Atu_0398</td>
      <td>A9CKB4</td>
      <td>ProR</td>
      <td>orange</td>
      <td>14 ± 0.4</td>
      <td>16 ± 0.6</td>
      <td>NC</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Atu_3947</td>
      <td>Q7CTP1</td>
      <td>DAAO</td>
      <td></td>
      <td>NC</td>
      <td>4 ± 0.2</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_3948</td>
      <td>Q7CTP2</td>
      <td>AlaR</td>
      <td></td>
      <td>NC</td>
      <td>NC</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_3949</td>
      <td>Q7CTP3</td>
      <td>OCD</td>
      <td></td>
      <td>NC</td>
      <td>NC</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_3950</td>
      <td>Q7CTP4</td>
      <td>ALDH</td>
      <td></td>
      <td>NC</td>
      <td>NC</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_3951</td>
      <td>A9CFU8</td>
      <td>LysR</td>
      <td></td>
      <td>NC</td>
      <td>NC</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_3952</td>
      <td>A9CFU9</td>
      <td>DAAO</td>
      <td></td>
      <td>NC</td>
      <td>NC</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_3953</td>
      <td>Q7CFV0</td>
      <td>ProR</td>
      <td>blue</td>
      <td>NC</td>
      <td>NC</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_3958</td>
      <td>Q7CTQ2</td>
      <td>DAAO</td>
      <td></td>
      <td>NC</td>
      <td>NC</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_3959</td>
      <td>Q7CTQ3</td>
      <td>ALDH</td>
      <td></td>
      <td>NC</td>
      <td>NC</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_3960</td>
      <td>A9CFV4</td>
      <td>DHDPS</td>
      <td></td>
      <td>NC</td>
      <td>NC</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_3961</td>
      <td>Q7CTQ5</td>
      <td>GntR</td>
      <td></td>
      <td>NC</td>
      <td>NC</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_3985</td>
      <td>A9CFW8</td>
      <td>ProC</td>
      <td></td>
      <td>NC</td>
      <td>NC</td>
      <td>NC</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Atu_4675</td>
      <td>A9CGZ4</td>
      <td>DHDPS</td>
      <td></td>
      <td>148 ± 2</td>
      <td>87 ± 7</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_4676</td>
      <td>Q7CVK1</td>
      <td>MLD2</td>
      <td></td>
      <td>30 ± 5</td>
      <td>40 ± 7</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_4678</td>
      <td>A9CGZ5</td>
      <td>SBP</td>
      <td></td>
      <td>198 ± 18</td>
      <td>79 ± 8</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_4682</td>
      <td>A9CGZ9</td>
      <td>DAAO</td>
      <td></td>
      <td>294 ± 15</td>
      <td>14 ± 3</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_4684</td>
      <td>A9CH01</td>
      <td>ProR</td>
      <td>light sky blue</td>
      <td>116 ± 14</td>
      <td>8 ± 1</td>
      <td>NC</td>
    </tr>
    <tr>
      <td>Atu_4691</td>
      <td>A9CH04</td>
      <td>2-Hacid_dh</td>
      <td></td>
      <td>NC</td>
      <td>NC</td>
      <td>NC</td>
    </tr>
  </tbody>
</table>

_Fold changes in expression for the indicated gene when grown on the indicated carbon source, relative to growth on Dglucose. Fold changes are the averages of three biological replicates with standard deviation. NC, no change._

### X-ray structure of a novel 4HypE

The X-ray structure of one of the previously functionally assigned 4HypEs (Uniprot: Q4KGU2; locus tag: PFL_1412; red, cluster 2) was determined in the presence of the substrate, t4Hyp and, also, pyrrole-2-carboxylate (PYC), a stable analogue of the enolate anion intermediate (Figure 5A,B; Table 6). These are the first liganded structures of a 4HypE and the first structure of a PRS with an authentic substrate. These structures corroborate the positioning of the active site Cys/Cys pair (Cys 88, Cys 236) to facilitate substrate epimerization, highlight residues specific to the coordination of the 4-hydroxyl group, and validate the hypothesis that PYC and substrate bind in a similar fashion. In addition, the X-ray structure of one of the newly functionally assigned 4HypEs (Uniprot: B9K4G4; locus tag: Avi_7022; orange, cluster 8) was determined in the presence of its substrate, t4Hyp. The active site contains Ser 93 on one face and Cys 255 on the opposite face (Figure 5C). Thus, despite the conserved ability of this enzyme to catalyze the 4HypE reaction (a two-base 1,1-proton transfer reaction), the Cys–Cys general acid/base pair observed in the structure of Q4KGU2 from the red cluster is not conserved. This observation highlights the structural diversity associated with evolution of function in the PRS. Without the information provided by the GNNs, the 4HypE function would not have been expected.

![Figure 5.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig5-v2.jpg)

**Figure 5.:** (A) Structure of Q4KGU2 (locus tag: PFL_1412; cluster 2) with PYC illustrating the utilization of the carboxyl group to bridge the N-terminal amide backbone groups of two opposing a-helices. While In B9K4G4 (D) and B9JQV3 (C) the relative positions of residues that coordinate the prolyl nitrogen (Asp 232, His 90) are conserved His 90 is replaced by a Ser. (B) Structure of Q4KGU2 with t4Hyp illustrating the interactions Q4KGU2 with the 4-hydroxyl group and the relative positions of the two catalytic cysteine residues. (C) Structure of B9JQV3 (locus tag: Avi_0518, cluster 9) with t4Hyp illustrating the interactions of B9JQV3 with the 4-hydroxyl group of t4Hyp and the relative positions of the catalytic Ser (Ser 93, trans?cis) and Cys (Cys 236, cis?trans). (D) Structure of B9K4G4 (Avi_7022, cluster 3) with PYC illustrating the position of the catalytic Ser (Ser 90, dehydration), and the non-catalytic orientation of Thr 256 which replaces the Cys observed in Cys/Cys containing PRS members. In addition, the catalytic Ser (Ser 90) is positioned by hydrogen bonding interactions between the side chain of Asn 93 (shown) and the backbone nitrogen of Asn 93 (not shown). Based on this work, all ProR family members with a catalytic Ser at this position (including B9JQV3, determined here) are proposed to have this motif.

**Table 6.**
 Data Collection and Refinement Statisticsa


<table>
  <thead>
    <tr>
      <th>UNIPROT / CLUSTER / PROTEIN</th>
      <th>A5VZY6 / 2 / Pput_1285</th>
      <th>A5VZY6 / 2 / Pput_1285</th>
      <th>Q1QU06 / 2 / Csal_2705</th>
      <th>Q8P833 / 2 / XCC_2415</th>
      <th>B3D6W2 / 2 / BMULJ_04062</th>
      <th>Q4KGU2 / 2 / PFL_1412</th>
      <th>Q4KGU2 / 2 / PFL_1412</th>
      <th>A6WW16 / 3 / Oant_0439</th>
      <th>B9K4G4 / 3 / Avi_7022</th>
      <th>B9JQV3 / 9 / Avi_0518</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Organism</td>
      <td>Pseudomonas putida F1</td>
      <td>Pseudomonas putida F1</td>
      <td>Chromohalobacter salexigens DSM 3043</td>
      <td>Xanthomonas campestris</td>
      <td>Burkholderia multivorans</td>
      <td>Pseudomonas fluorescens Pf-5</td>
      <td>Pseudomonas fluorescens Pf-5</td>
      <td>Ochrobacterium anthropi</td>
      <td>Agrobacterium vitis S4</td>
      <td>Agrobacterium vitis S4</td>
    </tr>
    <tr>
      <td>PDBID</td>
      <td>4JBD</td>
      <td>4JD7</td>
      <td>4JCI</td>
      <td>4JUU</td>
      <td>4K7X</td>
      <td>4J9W</td>
      <td>4J9X</td>
      <td>4K8L</td>
      <td>4K7G</td>
      <td>4LB0</td>
    </tr>
    <tr>
      <td colspan="11">DIFFRACTION DATA STATISTICS</td>
    </tr>
    <tr>
      <td>Space Group</td>
      <td>I2</td>
      <td>P212121</td>
      <td>P212121</td>
      <td>P212121</td>
      <td>I4122</td>
      <td>P21</td>
      <td>P212121</td>
      <td>I222</td>
      <td>P43212</td>
      <td>P42212</td>
    </tr>
    <tr>
      <td>Unit Cell (Å , °)</td>
      <td>a=45.2 b=54.2 c=142.7</td>
      <td>a=64.8 b=96.8 c=109.2</td>
      <td>a=48.1 b=54.4 c=253.0</td>
      <td>a=54.9 b=108.8 c=116.2</td>
      <td>a=114.9 b=114.9 c=173.7</td>
      <td>a=56.2 b=74.6 c=87.1 β=105.5</td>
      <td>a=64.8 b=96.8 c=109.2</td>
      <td>a=77.3 b=78.3 c=114.4</td>
      <td>a=54.9 b=108.8 c=116.2</td>
      <td>a=178.0 b=178.0 c=49.7</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>1.3 (1.3-1.32)</td>
      <td>1.5 (1.5-1.58)</td>
      <td>1.7 (1.7-1.79)</td>
      <td>1.75 (1.75-1.84)</td>
      <td>1.75 (1.75-1.84)</td>
      <td>1.6 (.6-1.69)</td>
      <td>1.7 (1.7-1.79)</td>
      <td>1.9 (1.9-2.0)</td>
      <td>2.0 (2.0-2.1)</td>
      <td>1.7 (1.7-1.79)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>99.8 (99.6)</td>
      <td>99.5 (98.9)</td>
      <td>97.0 (94.0)</td>
      <td>99.7 (99.4)</td>
      <td>100.0 (100.0)</td>
      <td>99.3 (99.5)</td>
      <td>99.5 (99.0)</td>
      <td>99.8 (100.0)</td>
      <td>100 (100)</td>
      <td>99.9 (99.9)</td>
    </tr>
    <tr>
      <td>Redundancy</td>
      <td>3.6 (3.5)</td>
      <td>7.3 (7.1)</td>
      <td>9.3 (7.8)</td>
      <td>7.3 (7.1)</td>
      <td>14.3 (13.5)</td>
      <td>3.6 (3.5)</td>
      <td>6.7 (6.0)</td>
      <td>7.2 (7.3)</td>
      <td>14.1 (13.2)</td>
      <td>10.4 (7.9)</td>
    </tr>
    <tr>
      <td>Mean(I)/sd(I)</td>
      <td>7.9 (1.4)</td>
      <td>18.0 (1.1)</td>
      <td>17.5 (3.3)</td>
      <td>18.0 (1.1)</td>
      <td>14.1 (1.1)</td>
      <td>6.9 (1.7)</td>
      <td>11.6 (1.5)</td>
      <td>6.0 (1.3)</td>
      <td>11.6 (3.3)</td>
      <td>18.3 (2.7)</td>
    </tr>
    <tr>
      <td>Rsym</td>
      <td>0.062 (0.735)</td>
      <td>0.067 (0.707)</td>
      <td>0.073 (0.644)</td>
      <td>0.074 (0.725)</td>
      <td>0.130 (0.699)</td>
      <td>0.093 (0.434)</td>
      <td>0.088 (0.531)</td>
      <td>0.09 (0.594)</td>
      <td>0.17 (0.836)</td>
      <td>0.078 (0.745)</td>
    </tr>
    <tr>
      <td colspan="11">REFINEMENT STATISTICS</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>1.3 (1.3-1.31)</td>
      <td>1.5 (1.5-1.52)</td>
      <td>1.7 (1.7-1.72)</td>
      <td>1.75 (1.75-1.77)</td>
      <td>1.75 (1.75-1.78)</td>
      <td>1.6 (1.6-1.62)</td>
      <td>1.7 (1.7-1.72)</td>
      <td>1.9 (1.9-1.97)</td>
      <td>2.0 (2.0-2.02)</td>
      <td>1.7 (1.72-1.70)</td>
    </tr>
    <tr>
      <td>Unique reflections</td>
      <td>82749</td>
      <td>109888</td>
      <td>72128</td>
      <td>70700</td>
      <td>58574</td>
      <td>90740</td>
      <td>77405</td>
      <td>27674</td>
      <td>86628</td>
      <td>87548</td>
    </tr>
    <tr>
      <td>Rcryst (%)</td>
      <td>15.8 (30.4)</td>
      <td>15.9 (22.6)</td>
      <td>17.1 (23.7)</td>
      <td>15.2 (21.5)</td>
      <td>13.8 (19.7)</td>
      <td>19.7 (28.8)</td>
      <td>19.4 (23.5)</td>
      <td>16.8 (17.6)</td>
      <td>13.6 (19.5)</td>
      <td>15.8 (22.9)</td>
    </tr>
    <tr>
      <td>Rfree (%, 5% of data)</td>
      <td>18.4 (31.1)</td>
      <td>17.5 (25.4)</td>
      <td>20.5 (26.2)</td>
      <td>18.4 (26.4)</td>
      <td>15.6 (18.5)</td>
      <td>23.2 (33.8)</td>
      <td>22.5 (27.5)</td>
      <td>20.7 (21.7)</td>
      <td>16.6 (22.9)</td>
      <td>19.2 (27.3)</td>
    </tr>
    <tr>
      <td>Residues In Model [Expected]</td>
      <td>A1-A308 [1-308]</td>
      <td>A(-5)-A308, D(-3)-D308 [1-308]</td>
      <td>A(-3)-A169, A171-A309 [1-311]</td>
      <td>A(-2)-A312, B(-2)-B312 [1-312]</td>
      <td>A(-3)-A310 [1-311]</td>
      <td>A1-A310, B1-B310 [1-310]</td>
      <td>A1-310, B1-310 [1-310]</td>
      <td>A0-A157, A161-A184, A193-A245, A255-280, A289-A332 [1-343]</td>
      <td>B5-B342, D(-9)-D342 [1-342]</td>
      <td>A1-A323, A326-A344, B0-B346 [1-347]</td>
    </tr>
    <tr>
      <td>Residues / Waters / Atoms total</td>
      <td>308 / 453 / 3142</td>
      <td>626 / 752 / 6225</td>
      <td>620 / 494 / 5780</td>
      <td>626 / 596 / 5841</td>
      <td>314 / 463 / 3223</td>
      <td>620 / 537 / 5301</td>
      <td>620 / 630 / 5378</td>
      <td>305 / 191 / 2824</td>
      <td>690 / 780 / 6761</td>
      <td>689 / 701 / 6633</td>
    </tr>
    <tr>
      <td>Bfactor Protein/Waters/Ligand</td>
      <td>17.3 / 31.2 / 21.7</td>
      <td>19.3 / 30.5 / 27.9</td>
      <td>24.8 / 33.6 / -</td>
      <td>23.9 / 35.2 / 37.3</td>
      <td>15.6 / 34.0 / 30.6</td>
      <td>21.1 / 32.2 / 12.9</td>
      <td>22.9 / 34.0 / 16.3</td>
      <td>31.3 / 37.7 / -</td>
      <td>24.1 / 37.5 / 15.2</td>
      <td>25.1 / 36.2 / 17.9</td>
    </tr>
    <tr>
      <td>Ligand</td>
      <td>Citrate</td>
      <td>Sulfate</td>
      <td>-</td>
      <td>Phosphate / UNL</td>
      <td>Phosphate</td>
      <td>(PYC) Pyrrole 2-carboxylate</td>
      <td>(t4Hyp) Trans- 4OH-L-Proline</td>
      <td>-</td>
      <td>(PYC) Pyrrole 2-carboxylate</td>
      <td>(t4Hyp) Trans- 4OH-L-Proline / Acetate</td>
    </tr>
    <tr>
      <td>RMSD Bond Lengths (Å) / Angles (°)</td>
      <td>0.008 / 1.283</td>
      <td>0.009 / 1.325</td>
      <td>0.011 / 1.332</td>
      <td>0.010 / 1.26</td>
      <td>0.009 / 1.268</td>
      <td>0.006 / 1.079</td>
      <td>0.006 / 1.093</td>
      <td>0.011 / 1.349</td>
      <td>0.011 / 1.311</td>
      <td>0.010 / 1.320</td>
    </tr>
    <tr>
      <td>Ramachandran Favored / Outliers (%)</td>
      <td>98.7 / 0.0</td>
      <td>96.8 / 0.00</td>
      <td>98.2 / 0.00</td>
      <td>99.0 / 0.0</td>
      <td>97.7 / 0.0</td>
      <td>98.7 / 0.0</td>
      <td>98.5 / 0.0</td>
      <td>98.3 / 0.0</td>
      <td>98.0 / 0.3</td>
      <td>98.4 / 0.3</td>
    </tr>
    <tr>
      <td>Clashscore b</td>
      <td>2.32 (99th pctl)</td>
      <td>3.02 (98th pctl)</td>
      <td>3.74 (97th pctl)</td>
      <td>4.14 (97th pctl)</td>
      <td>3.12 (97th pctl)</td>
      <td>1.59 (99th pctl)</td>
      <td>1.82 (99th pctl)</td>
      <td>6.6 (93rd pctl)</td>
      <td>2.8 (99th pctl)</td>
      <td>2.2 (99th pctl)</td>
    </tr>
    <tr>
      <td>Overall scoreb</td>
      <td>1.01 (99th pctl)</td>
      <td>1.29 (95th pctl)</td>
      <td>1.16 (99th pctl)</td>
      <td>1.22 (99th pctl)</td>
      <td>1.16 (99th pctl)</td>
      <td>0.97 (100th pctl)</td>
      <td>0.94 (100th pctl)</td>
      <td>1.36 (98th pctl)</td>
      <td>1.08 (100th pctl)</td>
      <td>1.0 (100th pctl)</td>
    </tr>
  </tbody>
</table>

_aData in parenthesis is for the highest resolution binbScores are ranked according to structures of similar resolution as formulated in MOLPROBITY_

### Discovery of novel families of t3HypDs and ?1-Pyr2C reductases

The t3HypD function previously was assigned to eukaryotic members of the PRS (Visser et al., 2012), so their genome neighbors are not represented in the GNN. However, the members of the navy cluster (cluster 5; species of Bacilli) identify several clusters in the GNN, including families of the components of TRAP and ABC transport systems, families of peptidases, and a family in the ornithine cyclodeaminase superfamily (OCDS); several members of the olive cluster (cluster 12) also identify the same OCDS cluster (Figure 3G). Members of the OCDS catalyze NAD(P)+/NAD(P)H-dependent reactions that involve the ketimines obtained by oxidation of a-amino acids (Goodman et al., 2004; Schröder et al., 2004; Gatto et al., 2006); some have been reported to catalyze the reduction of the ketimine of proline (Hallen et al., 2011) (and oxidation of L-proline; Figure 6A). Using purified proteins, we determined that members of both the navy (cluster 5) and olive (cluster 12) clusters in the SSN catalyze the t3HypD reaction (Tables 1 and 2). We also determined that members of the OCDS cluster catalyze the NADPH-dependent reduction of the ketimine of proline to form L-proline (Figure 6A,B). The catabolic pathway for trans-3-hydroxy-L-proline is known to proceed by dehydration, nonenzymatic tautomerization of the dehydration product to the ketimine of proline and, finally, reduction of the ketimine to form L-proline (Figure 1). In the OCDS SSN (Figure 6A), the previously characterized proline ketimine reductases are located in clusters/families distinct from the members of the OCDS identified in our GNN. Thus, assignment of the t3HypD function to the members of navy and olive clusters in the SSN would not have been possible without the synergistic information contained in the GNN.

![Figure 6.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig6-v2.jpg)

**Figure 6.:** (A) The OCDS SSN displayed at the e-value cutoff 10-45 (~35% sequence identity). The Pyr2C reductase function is located in four clusters; these proteins are shown in large colored circles, labeled from 1 to 16, and color-coded by the colors of the PRS query sequences shown in Figure 2B. Proteins representing several previously characterized functions in the OCDS are shown by large diamonds, with borders in hotpink (L-alanine dehydrogenase [Schröder et al., 2004]), brown (ornithine cyclodeaminase [Goodman et al., 2004]), magenta (lysine cyclodeaminase [Gatto et al., 2006]), red (ketamine reductase [Hallen et al., 2011]), green (L-arginine dehydrogenase [Li and Lu, 2009]) and palegreen (tauropine dehydrogenase [Kan-No et al., 2005; Plese et al., 2008]), respectively. Their annotations are shown in italics. The diamonds with blue and olive borders are Pyr2C reductases recently characterized by Watanabe et al. (2014). (B) Kinetics data for the Pyr2C reductase activity for the 16 members of the OCDS shown in panel A using NADPH as the cosubstrate.

### Structure of a novel t3HypD

We determined the structure of a t3HypD (B9K4G4) from the light sky blue cluster (cluster 3) in the presence of PYC (Table 6). Instead of the typical PRS Cys/Cys pair, B9K4G4 contains Ser 90 in a similar conformation as was determined for B9JQV3 from the orange cluster (4HypE activity) and Thr 256 on the opposing face (Figure 5D). Thr 256 mimics the conformation of the typical PRS Cys residue but with the side-chain methylene positioned against the anomeric carbon. Again, the assignment of function enabled by the GNNs identifies convergent evolution of function within the PRS.

### Discovery of additional families of 4HypEs, t3HypDs, and ?1-Pyr2C reductases

Members of the light sky blue (cluster 3) cluster in the SSN identify the same (super)families identified by both the 4HypE and t3HypD clusters (transport systems, transcriptional regulators, DAAO [Figure 3D], DHDPS [Figure 3E], aldehyde dehydrogenase [Figure 3F], and OCD [Figure 3G]); however, several members of the light sky blue cluster identify a GNN cluster annotated as the malate/L-lactate dehydrogenase 2 superfamily (MLD2; NADH-dependent oxidoreductases) (Muramatsu et al., 2005) (Figure 3H). Using purified members of the PRS, we determined that the light sky blue cluster is functionally heterogeneous (and some members are promiscuous) for the 4HypE and t3HypD functions (Tables 1 and 2). We also determined that members of the MLD2 superfamily in the GNN catalyze the reduction of proline ketimine (Table 7). Thus, the GNN provided essential information for predicting/assigning functions to the members of the light sky blue cluster in the PRS SSN.

**Table 7.**
 Kinetic constants for the proline ketimine reductases (members of the malate/Llactate dehydrogenase 2 [MLD2] and ornithine cyclodeaminase [OCD] superfamilies) that are in the genome neighborhoods of members of the PRS


<table>
  <thead>
    <tr>
      <th>Cluster</th>
      <th>UniProt</th>
      <th>Locus tag</th>
      <th>Cofactor</th>
      <th>kcat [s-1]</th>
      <th>Km [mM]</th>
      <th>kcat/KM[M-1s-1]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">MLD2_PRS_light skyblue (3)</td>
      <td>Q7CVK1</td>
      <td>Atu4676</td>
      <td>NADPH</td>
      <td>32 ± 1</td>
      <td>0.33 ± 0.04</td>
      <td>99000</td>
    </tr>
    <tr>
      <td>Q9I492</td>
      <td>PA1252</td>
      <td>NADPH</td>
      <td>1.6 ± 0.05</td>
      <td>0.41 ± 0.06</td>
      <td>3900</td>
    </tr>
    <tr>
      <td rowspan="3">MLD2_PRS_Red (2)</td>
      <td>Q4KGT8</td>
      <td>PFL_1416</td>
      <td>NADPH</td>
      <td>20 ± 0.8</td>
      <td>1.1 ± 0.2</td>
      <td>18000</td>
    </tr>
    <tr>
      <td>Q0B9S2</td>
      <td>Bamb_3547</td>
      <td>NADPH</td>
      <td>54 ± 13</td>
      <td>9.4 ± 4</td>
      <td>5700</td>
    </tr>
    <tr>
      <td>A9ALD3</td>
      <td>Bmul_4451</td>
      <td>NADPH</td>
      <td>33 ± 2</td>
      <td>7.4 ± 1</td>
      <td>4400</td>
    </tr>
    <tr>
      <td>MLD2_PRS_indigo (13)</td>
      <td>Q4KAT3</td>
      <td>PFL_3547a</td>
      <td>NADPH</td>
      <td>-</td>
      <td>-</td>
      <td>2300b</td>
    </tr>
    <tr>
      <td rowspan="11">OCD_PRS_light skyblue (3)</td>
      <td rowspan="2">A1B196</td>
      <td rowspan="2">Pden_1185</td>
      <td>NADPH</td>
      <td>260 ± 20</td>
      <td>3.1 ± 0.7</td>
      <td>85000</td>
    </tr>
    <tr>
      <td>NADH</td>
      <td>81 ± 20</td>
      <td>16 ± 6</td>
      <td>5100</td>
    </tr>
    <tr>
      <td>A3S939</td>
      <td>EE36_06353a</td>
      <td>NADPH</td>
      <td>6.8 ± 0.7</td>
      <td>1.0 ± 0.3</td>
      <td>6700</td>
    </tr>
    <tr>
      <td rowspan="2">A3SU01</td>
      <td rowspan="2">NAS141_11281a</td>
      <td>NADPH</td>
      <td>39 ± 4</td>
      <td>1.2 ± 0.4</td>
      <td>32000</td>
    </tr>
    <tr>
      <td>NADH</td>
      <td>8.2 ± 4</td>
      <td>73 ± 50</td>
      <td>110</td>
    </tr>
    <tr>
      <td rowspan="2">Q16D96</td>
      <td rowspan="2">RD1_0323a</td>
      <td>NADPH</td>
      <td>15 ± 1</td>
      <td>0.27 ± 0.07</td>
      <td>56000</td>
    </tr>
    <tr>
      <td>NADH</td>
      <td>3.7 ± 0.4</td>
      <td>11 ± 3</td>
      <td>320</td>
    </tr>
    <tr>
      <td rowspan="2">Q5LLV0</td>
      <td rowspan="2">SPO3821a</td>
      <td>NADPH</td>
      <td>130 ± 20</td>
      <td>3.0 ± 0.9</td>
      <td>43000</td>
    </tr>
    <tr>
      <td>NADH</td>
      <td>-</td>
      <td>-</td>
      <td>840b</td>
    </tr>
    <tr>
      <td rowspan="2">Q3IZJ8</td>
      <td rowspan="2">RSP_0854a</td>
      <td>NADPH</td>
      <td>66 ± 4</td>
      <td>0.43 ± 0.09</td>
      <td>150000</td>
    </tr>
    <tr>
      <td>NADH</td>
      <td>12c</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td rowspan="8">OCD_PRS_navy (5)</td>
      <td rowspan="2">Q81HB0</td>
      <td rowspan="2">BC_0906</td>
      <td>NADPH</td>
      <td>15 ± 1</td>
      <td>0.47 ± 0.1</td>
      <td>31000</td>
    </tr>
    <tr>
      <td>NADH</td>
      <td>19 ± 1</td>
      <td>11 ± 2</td>
      <td>1800</td>
    </tr>
    <tr>
      <td rowspan="2">Q73CR9</td>
      <td rowspan="2">BCE_0995</td>
      <td>NADPH</td>
      <td>15 ± 1</td>
      <td>1.1 ± 0.3</td>
      <td>13000</td>
    </tr>
    <tr>
      <td>NADH</td>
      <td>2.1 ± 0.3</td>
      <td>7.6 ± 3</td>
      <td>270</td>
    </tr>
    <tr>
      <td rowspan="2">Q6HMS8</td>
      <td rowspan="2">BT9727_0800</td>
      <td>NADPH</td>
      <td>11 ± 1</td>
      <td>3.4 ± 0.9</td>
      <td>3100</td>
    </tr>
    <tr>
      <td>NADH</td>
      <td>2.1 ± 0.4</td>
      <td>18 ± 6</td>
      <td>120</td>
    </tr>
    <tr>
      <td rowspan="2">Q63FA5</td>
      <td rowspan="2">BCE33L0803</td>
      <td>NADPH</td>
      <td>5.8c</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>NADH</td>
      <td>0.87 ± 0.1</td>
      <td>4.9 ± 2</td>
      <td>180</td>
    </tr>
    <tr>
      <td rowspan="7">OCD_PRS_olive (12)</td>
      <td rowspan="2">Q0B953</td>
      <td rowspan="2">Bamb_3766</td>
      <td>NADPH</td>
      <td>106 ± 4</td>
      <td>1.6 ± 0.2</td>
      <td>64000</td>
    </tr>
    <tr>
      <td>NADH</td>
      <td>41 ± 6</td>
      <td>7.3 ± 3</td>
      <td>5700</td>
    </tr>
    <tr>
      <td rowspan="2">Q2T596</td>
      <td rowspan="2">BTH_II1457a</td>
      <td>NADPH</td>
      <td>73 ± 2</td>
      <td>0.39 ± 0.05</td>
      <td>190000</td>
    </tr>
    <tr>
      <td>NADH</td>
      <td>203 ± 23</td>
      <td>32 ± 7</td>
      <td>6400</td>
    </tr>
    <tr>
      <td rowspan="2">Q3JFG0</td>
      <td rowspan="2">BURPS1710b_A2543a</td>
      <td>NADPH</td>
      <td>7.8 ± 0.5</td>
      <td>0.64 ± 0.1</td>
      <td>12000</td>
    </tr>
    <tr>
      <td>NADH</td>
      <td>6.0 ± 1</td>
      <td>31 ± 13</td>
      <td>190</td>
    </tr>
    <tr>
      <td>A9AKH1</td>
      <td>Bmul_4263</td>
      <td>NADPH</td>
      <td>25 ± 6</td>
      <td>4 ± 2</td>
      <td>6400</td>
    </tr>
    <tr>
      <td rowspan="4">OCD_PRS_blue (1)</td>
      <td rowspan="2">Q485R8</td>
      <td rowspan="2">CPS_1455</td>
      <td>NADPH</td>
      <td>35 ± 0.8</td>
      <td>1.8 ± 0.2</td>
      <td>20000</td>
    </tr>
    <tr>
      <td>NADH</td>
      <td>-</td>
      <td>-</td>
      <td>170b</td>
    </tr>
    <tr>
      <td rowspan="2">A3QH73</td>
      <td rowspan="2">Shew_2955a</td>
      <td>NADPH</td>
      <td>6.7 ± 0.7</td>
      <td>1.6 ± 0.6</td>
      <td>4300</td>
    </tr>
    <tr>
      <td>NADH</td>
      <td>0.37 ± 0.1</td>
      <td>26 ± 10</td>
      <td>14</td>
    </tr>
  </tbody>
</table>

_aHighly homologous to MLD2 or OCD which are in the gene context of proline racemase.bThe enzyme didn’t saturate.cKM is too small (< 0.03mM)._

## Discussion

Although in most cases interpretations of the functional relationships of the clusters in the GNN with those in the query SSN are straightforward, complications can arise. For example, in several species, two members of the PRS are encoded by proximal genes, that is, a 4HypE and a t3HypD; these species can utilize both t4Hyp and trans-3-hydroxy-L-proline as carbon and nitrogen sources. Thus, the GNN contains a cluster for the PRS (right-hand cluster in the top row [when used as query, each PRS finds the adjacent PRS; Figure 3I]). For these species, clusters in the GNN are a composite of two genome contexts, that is, the proteins/enzymes that participate in both catabolic pathways. These situations can be deconvoluted by coloring the nodes identified by two queries with the colors for both query clusters in the GNN. With the genome contexts/metabolic pathways identified for ‘genome-isolated’ 4HypEs and t3HypDs, this complication is easy to identify and understand.

The GNN also is useful to assess the physiological importance of in vitro promiscuity. Several of the purified proteins catalyze both the 4HypE and t3HypD reactions (Tables 1 and 2). Some of these promiscuous proteins identify both the OCD or MLD2 superfamilies (predicting the t3HypD pathway) and the DAAO, DHDPS, and aldehyde dehydrogenase superfamilies (predicting the 4HypE pathway) in their genome neighborhoods (Figure 7). In these cases, we conclude that the in vitro promiscuity is not an ‘artifact’ but is physiologically significant.

![Figure 7.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig7-v2.jpg)

**Figure 7.:** (A) SSN for the PRS with cluster numbers. (B) D-amino acid oxidase (DAAO). (C) Dihydrodipicolinate synthase (DHDPS). (D) Aldehyde dehydrogenase. (E) Ornithine cyclodeaminase (OCD). (F) Malate/L-lactate dehydrogenase 2 (MLD2). (G) The color scheme for B–F.

As established in this study, the majority of the members of the PRS catalyze only the three previously characterized (known) reactions (Figure 1). As a result, we were able to use the GNN without any additional information to correctly predict functions for all of the highly populated clusters/families (>85% of the members; Figure 8). Because of this simplicity, the PRS provides a lucid illustration of the strategy by which a query SSN and its GNN can be used to predict and assign enzymatic functions.

![Figure 8.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig8-v2.jpg)

**Figure 8.:** Colors match the color scheme in Figure 2B.

However, large-scale prediction and assignment of function to members of many functionally diverse (super)families will be more complicated than that described for the PRS and require information from complementary experimental and computational approaches. The use of GNNs is restricted to those enzymes that are encoded by proximal operons and/or gene clusters in eubacteria and archaea. For Escherichia coli K-12, 60% of the genes are located in polycistronic transcriptional units that may provide linked functional information that can be used to identify pathways; 40% are located in monocistronic transcriptional units (http://regulondb.ccg.unam.mx/menu/tools/regulondb_overviews/chart_form.jsp). Thus, genome neighborhood context is not a general solution to infer functions for many proteins/enzymes of unknown function encoded eubacterial and archaeal genomes. Even for those proteins encoded by polycistronic transcriptional units, complete metabolic pathways may be encoded by multiple transcriptional units (mono- and/or polycistronic) that are not genome proximal; these pathways and their component enzymes and ligand binding proteins (solute binding proteins for transport systems and transcriptional regulators) may be recognized by regulon analyses that identify conserved binding sites for transcriptional regulators (Ravcheev et al., 2013; Rodionov et al., 2013).

To the extent that genome neighborhoods and/or regulons allow the identification of the components of unknown/novel metabolic pathways, the locations of these proteins/enzymes in the SSNs for their (super)families will provide restrictions on their ligand/substrate specificities and/or reaction mechanisms (Atkinson et al., 2009). Also, as we recently demonstrated (Zhao et al., 2013), in silico (virtual) docking of ligand libraries to multiple binding proteins and enzymes in an unknown metabolic pathway (pathway docking) is a powerful approach to enhance the reliability of docking to predict novel ligand/substrate specificities and identify novel metabolic pathways

Irrespective of the many complications associated with assignment of function to unknown proteins/enzymes, we conclude that GNNs provide a novel approach for large-scale analysis and visualization of genome neighborhood context in enzyme (super)families. We are continuing to improve the use of GNNs as well as regulon analyses and pathway docking to facilitate the discovery of novel enzymes and the metabolic pathways in which they function.

## Materials and methods

### Sequence similarity networks (SSN)

The SSNs for the PRS (Figure 2) and the OCDS (Figure 5A) were created using Pythoscape v1.0 (Barber and Babbit, 2012) that is available for download from http://www.rbvi.ucsf.edu/trac/Pythoscape The input sequences were downloaded from the InterPro webpages of PRS and OCDS: http://www.ebi.ac.uk/interpro/entry/IPR008794, http://www.ebi.ac.uk/interpro/entry/IPR003462, respectively. Cytoscape v2.8 (Smoot et al., 2011) is used for visualization and analysis of the SSN.

### Genome neighborhood network (GNN)

The GNN for the PRS (Figure 3) was also created using Pythoscape v1.0 (Barber and Babbit, 2012). At an e-value cutoff 10-110, each cluster in the SSN was assigned a unique cluster number and color, which are used for labeling and coloring genome context sequences. Genome context sequences were collected from the ±10 gene range of each PRS member and used as the input sequences for making the GNN using the procedure for generating a SSN.

### Protein production

Genes for members of the PRS that are encoded by the genomic DNAs in the Macromolecular Therapeutics Development Facility at the Albert Einstein College of Medicine were cloned into pNIC28-BSA4-based expression vectors as previously described (Sauder et al., 2008).

### Protein expression

The pNIC28-BSA4-based expression plasmids were transformed into Escherichia coli BL21(DE3) containing the pRIL plasmid (Stratagene, Agilent Technologies, Inc., Wilmington, DE) and used to inoculate 20 ml 2xYT cultures containing 50 µg/ml kanamycin and 34 µg/ml chloramphenicol. Cultures were allowed to grow overnight at 37°C in a shaking incubator; these were used to inoculate 2 L of PASM-5052 auto-induction medium (Studier). The cultures were placed in a LEX48 airlift fermenter and incubated at 37°C for 5 hr and then at 22°C overnight (16–20 hr). The cells were collected by centrifugation at 6000×g for 10 min and stored at -80°C.

### Purification of proteins

Cells were resuspended in Lysis Buffer (20 mM HEPES, pH 7.5, containing 20 mM imidazole, 500 mM NaCl, and 5% glycerol) and lysed by sonication. Lysates were clarified by centrifugation at 35,000×g for 45 min. The clarified lysates were loaded on a 1-ml His60 Ni-NTA column (Clontech) using an AKTAxpress FPLC (GE Healthcare). The columns were washed with 10 column volumes of Lysis Buffer and eluted with buffer containing 20 mM HEPES, pH 7.5, containing 500 mM NaCl, 500 mM imidazole, and 5% glycerol. The purified proteins were loaded onto a HiLoad S200 16/60 PR gel filtration column equilibrated with a buffer containing 20 mM HEPES, pH 7.5, 150 mM NaCl, 5% glycerol, and 5 mM DTT. The purities of the proteins were analyzed by SDS-PAGE. The proteins were snap frozen in liquid N2 and stored at -80°C.

### Crystallization

Proteins were screened for crystallization conditions using commercially available screens (MCSG 1, 2, and 4 [Microlytic, Woburn MA] and MIDAS [Molecular Dimensions, Altamonte Springs FL]) using sitting drop vapor diffusion 96-well INTELLIPLATES (Art Robbins Instruments, Sunnyvale CA), a PHOENIX crystallization robot (Art Robbins Instruments), and stored and monitored in a Rock Imager 1000 (Formulatrix, Waltham MA) plate hotel. Protein (1 µl) was combined with an equivalent volume of precipitant and equilibrated against a 70 µl reservoir of the same precipitant at room temperature (~292 K).

A5VZY6, (27.9 mg/mL, 15 mM HEPES, pH 7.5, containing 150 mM NaCl, and 5 mM DTT) was crystallized in 0.1 M sodium acetate, pH 4.6, containing 1.5 M LiSO4; the crystals grew as rectangular bricks over a 1-week period (SPG-P212121). For the cryoprotectant, the LiSO4 concentration was increased to 1.8M.

A5VZY6 was also crystallized (27.9 mg/ml, 15 mM HEPES, pH 7.5, containing 150 mM NaCl, and 5 mM DTT) in 0.2 M diammonium hydrogen citrate pH 5.0, containing 20% (wt/vol) PEG 3350; the crystals grew as wedges over a 1-week period. The cryoprotectant contained 20% glycerol.

Q1QU06 (21.1 mg/ml, 15 mM HEPES, pH 7.5, containing 150 mM NaCl, and 5 mM DTT) was crystallized in 0.2 M di-ammonium hydrogen citrate, pH 5.0, containing 20% (wt/vol) PEG 3350; the crystals grew as plates over 2–3 days. The cryoprotectant contained 20% glycerol.

XCC2415 (29.3 mg/ml, 15 mM HEPES, pH 7.5, containing 150 mM NaCl, and 5 mM DTT) was crystallized in 0.1 M HEPES, pH 7.5, containing 0.8 M sodium phosphate and 0.8 M potassium phosphate and grew as thin rods over 2–3 days. The cryoprotectant contained 20% glycerol.

B3D6W2 (21.8 mg/ml, 15 mM HEPES, pH 7.5, containing 150 mM NaCl, and 5 mM DTT) was crystallized in 0.1 M phosphate-citrate, pH 4.2, containing 1.6 M NaH2PO4, and 0.4 M K2HPO4 and grew as large rods over 2 weeks. The cryoprotectant contained 20% glycerol.

Q4KGU2 (25.7 mg/ml, 15 mM HEPES, pH 7.5, containing 150 mM NaCl, and 5 mM DTT) was crystallized in 0.2 M ammonium acetate, 0.1 M trisodium citrate, pH 5.6, containing 14% PEG4000, 5% glycerol, and either 20 mM PYC or 50 mM t4Hyp and grew as thick plates over 2–3 days. The cryoprotectant contained 20% glycerol.

For A6WW16, B9K4G4, and B9JQV3, TEV protease (Tropea et al., 2009) was added at a 1/80 ratio prior to crystallization setup. The samples were incubated on ice for 2 hr, and the buffer was exchanged with 15 mM HEPES, pH 7.5, containing 5 mM DTT by dilution and centrifugal filtration. The extent of TEV cleavage was not measured.

A6WW16 (17.3 mg/ml, 15 mM HEPES, pH 7.5, containing 5 mM DTT) was crystallized in 0.2 M sodium nitrate and 20% PEG3350 and grew as leaf petals over 2 to 3 weeks. The cryoprotectant contained 20% glycerol.

B9K4G4, (17.1 mg/ml, 15 mM HEPES, pH 7.5, containing 5 mM DTT) was crystallized in 0.1 M sodium acetate, pH 4.6, containing 1 M ammonium citrate and 25 mM pyrrole 2-carboxylate. Crystals grew from an initial precipitate as multifaceted crystals over a month. The cryoprotectant contained 20% glycerol.

B9JQV3 (30.0 mg/ml, 15 mM HEPES, pH 7.5, containing 5 mM DTT) was crystallized in 0.1 M sodium acetate, containing 25% Peg4000, 8% 2-propanol, and 200 mM t4Hyp and grew as tetragonal rods over 2–3 days. The cryoprotectant contained 20% 2-propanol.

### Structure determination

Diffraction data were collected on beamline 31-ID (LRL-CAT, Advanced Photon Source, Argonne National Laboratory, IL) from single crystals at 100 K and a wavelength of 0.9793 Å. Data were integrated using MOSFLM (Battye et al., 2011) and scaled in SCALA (Evans, 2006).

Suitable molecular replacement models existed for all of the protein targets of this study. These included, 2AZP, a putative 4HypE (from cluster 2) determined unliganded by the Midwest Center for Structural Genomics, and 1TM0 (Forouhar et al., 2007), a putative t3HypD (cluster 3, also similar to cluster 9) with an unliganded and disordered active site, determined by the Northeast Structural Genomics Consortium. Molecular replacement computations were performed in AMORE (Navaza, 1994) utilizing the structure that exhibited the greatest homology to the target. If this was unsuccessful, either due to the particular issues with the space group, asymmetric unit composition, or a different orientation of the two domains, molecular replacement was performed with each of the domains separately within PHENIX (Adams et al., 2004; Zwart et al., 2008).

Iterative cycles of manual rebuilding within COOT (Emsley and Cowtan, 2004) and refinement within PHENIX were performed until the entire sequence was modeled. Inclusion of ligands, TLS (translation/libration/screw) refinement (domains chosen automatically within PHENIX) (Winn et al., 2001; Painter and Merritt, 2006) and editing of the solvent structure were performed in the final refinement cycles.

With one exception, the entire sequences of all of the targets could be modeled, except for a small number of residues at the N- or C-termini. The one outlier was A6WW16 that had several disordered regions around the active site similar to the previously determined structure from this cluster (1TM0, cluster 3, light sky blue). Due to the relatively weak binding of the proline racemase family members for their substrates, inhibitors and substrates were included at high concentrations (25–200 mM). Even at these concentrations, several structures were determined from cluster 2 that bound anionic ligands (phosphate, citrate, etc) from the crystallization medium rather than the co-crystallized ligand, and the degree of domain closure about that ligand varied. For all of the structures liganded with either PYC or t4Hyp, the structures are determined in a closed state with Ca–Ca distances of 7–8 Å for the opposing active site catalytic Cys–Cys (cluster 2, red), Ser–Thr (cluster 3, light sky blue) or Ser–Cys dyad (cluster 9, orange). In the case of Q4KGU2, the ligand was t4Hyp state based on the electron density. In contrast, for B9JQV3, the density for the ligand had significant planer character, suggesting a mixture of t4Hyp and c4Hyp.

### ESI-MS screening of ProR, 4HypE, and t3HypD activities

Enzyme activity was screened by the mass change resulting from racemization /epimerization (+1 peak shift) and/or dehydration (-17 peak shift) for reactions in D2O. Each enzyme (1 µM) was incubated with substrate libraries (Table 1) containing proline and proline betaine derivatives (0.1 mM each) along with 20 mM ammonium bicarbonate in D2O at a final volume of 200 µl at 30°C for 16 hr. 50 µl of the reaction mixture was aliquoted and dried with an Eppendorf vacufuge concentrator. The residue was suspended in 10 µl of H2O, and 5 µl of the solution was mixed with the 5 µl of 50% methanol containing 0.4% (vol/vol) formic acid. A 10 µl sample was analyzed for ESI-MS.

### 1H NMR assay to confirm PRS reactions

If a change in mass was observed in the ESI-MS screening assays, a 1H NMR assay was performed to determine the product. Each reaction mixture contained 1 µM enzyme, 10 mM substrate, and 25 mM sodium phosphate buffer, pD 8, in a total volume of 800 µl D2O. The mixture was incubated at 30°C for 16 hr before acquisition of the 500 MHz (Hunter et al., 2012) H NMR spectrum (Figure 9).

![Figure 9.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig9-v2.jpg)

**Figure 9.:** (A) 1H NMR spectra of the 4Hyp substrate mixture in 25 mM Na+-phosphate buffer, pD 8, in D2O (top) and 4Hyp mixture with A3QFI1 (cluster 1, blue) showing 4Hyp epimerization (bottom). The red arrow indicates the proton at C2 for epimerization. The enzyme was stored in glycerol, so the spectra show resonances for glycerol between 3.4 and 3.7 ppm. (B) 1H NMR spectra of the t3Hyp substrate mixture in 25 mM Na+-phosphate buffer, pD 8, in D2O (top), t3Hyp mixture with D0B556 (cluster 3, light sky blue) showing 3Hyp epimerization (middle), and t3Hyp mixture with B9K4G4 (cluster 3, light sky blue) showing t3Hyp dehydration (bottom). The red arrow indicates the proton at C2 for epimerization; the green arrow indicates the proton at C3 for dehydration.

### Polarimetric assay to determine PRS kinetics

The enzyme activity was measured in a Jasco P-1010 polarimeter with a Hg 405-nm filter at 25°C by quantitating the change in optical rotation. The assay mixture contained 1 mM dithiothreitol (DTT) and 50 mM Na+-phosphate buffer, pH 8.0.

### UV spectrophotometric assay for ?1-Pyr2C reductase activity

?1-Pyr2C reductase assays were performed by measuring the decrease in the absorbance of NAD(P)H at 340 nm at 25°C with a Cary 300 Bio UV-Visible spectrophotometer (Varian). The reaction mixture (300 µl) contained variable concentrations of Pyr2C, 50 mM Tris–HCl buffer, pH 7.6, 0.16 mM NAD(P)H, and enzyme.

### 1H NMR assay for ?1-Pyr2C reductase activity

The reaction mixture contained 10 mM ?1-Pyr2C, 1 µM enzyme, 0.16 mM NADPH, 25 mM phosphate-Na buffer, pD 8.0, 1 U/ml alcohol dehydrogenase (NADP+-dependent from Thermoanaerobium brockii, Sigma) and 80 µl isopropanol in a total volume of 800 µl of D2O; the reaction was incubated at 30°C for 16 hr. The solvent was removed by lyophilization, 800 µl of D2O was added, and the 1H NMR spectrum was recorded. Representative spectra are shown in Figure 10.

![Figure 10.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig10-v2.jpg)

**Figure 10.:** (A) 1H NMR spectrum of ?1-Pyr2C substrate in sodium phosphate, pD 8.0, in D2O. (B) 1H NMR spectrum of Q7CVK1 (locus tag: Atu4676) incubated with ?1-Pyr2C, NADPH, and the cofactor regeneration system of alcohol dehydrogenase (NADP+-dependent) and isopropanol in sodium phosphate, pD 8.0 in D2O. (C) 1H NMR spectrum of L-proline in 25 mM sodium phosphate, pD 8.0, in D2O.

### Bacterial strains and growth conditions

Bacterial strains are listed in Table 8. All strains were grown at 30°C with shaking at 225 rpm and were routinely cultured in Tryptic Soy Broth (Difco), supplemented with 30 g L-1 sea salts (Sigma-Aldrich) for Labrenzia aggregata IAM12614 and Roseovarius nubinhibens ISM.

**Table 8.**
 Strains used in this study


<table>
  <thead>
    <tr>
      <th>Organism</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Agrobacterium tumefaciens C58</td>
    </tr>
    <tr>
      <td>Sinorhizobium meliloti 1021</td>
    </tr>
    <tr>
      <td>Labrenzia aggregata IAM12614</td>
    </tr>
    <tr>
      <td>Pseudomonas aeruginosa PAO1</td>
    </tr>
    <tr>
      <td>Paracoccus denitrificans PD1222</td>
    </tr>
    <tr>
      <td>Rhodobacter sphaeroides 2.4.1</td>
    </tr>
    <tr>
      <td>Rhodobacter sphaeroides 2.4.1?RSP3519</td>
    </tr>
    <tr>
      <td>Bacillus cereus ATCC14579</td>
    </tr>
    <tr>
      <td>Roseovarius nubinhibens ISM</td>
    </tr>
    <tr>
      <td>Escherichia coli MG1655</td>
    </tr>
    <tr>
      <td>Streptomyces lividans TK24</td>
    </tr>
  </tbody>
</table>

For gene expression analyses and carbon utilization studies, strains were cultured in the following defined media:

Agrobacterium tumefaciens C58 was cultured in M9 minimal medium (per liter: 12.8 g Na2HPO4.7H2O, 3.0 g KH2PO4, 0.5 g NaCl, 1.0 g NH4Cl); B. cereus ATCC 14579 was cultured in a modified Spizizen's minimal medium (Spizizen., 1958) (per liter: 2.0 g (NH4)2SO4, 11.0 g K2HPO4, 6.0 g KH2PO4, 1.0 g sodium citrate.2H2O).

Streptomyces lividans TK24 was cultured in a modified minimal medium of Hopwood (Hopwood., 1967) (per liter: 1.0 g (NH4)2SO4, 0.5 g K2HPO4, 0.005 g FeSO4.7H2O). M9 minimal medium, and Spizizen's minimal medium were supplemented with the following trace metals (per liter: 0.003 mg CuSO4.5H2O, 0.025 mg H3BO3, 0.007 mg CoCl2.6H2O, 0.016 mg MnCl2.4H2O, 0.003 mg ZnSO4.7H2O, 0.3 mg FeSO4.7H2O). The minimal medium of Hopwood was supplemented with the following trace metals (per liter: 0.08 mg ZnCl2, 0.4 mg FeCl3.6H2O, 0.02 mg CuCl2.2H2O, 0.02 mg MnCl2.4H2O, 0.02 mg Na2B4O7.10H2O, 0.02 mg (NH4)6Mo7O24.4H2O).

All other strains were grown in the following defined medium (per liter: 17.0 g K2HPO4, 2.5 g (NH4)2SO4, 2.0 g NaCl) supplemented with the following trace metals (0.3 mg FeSO4.7H2O, 0.003 mg ZnSO4.7H2O, 0.003 mg CuSO4.5H2O, 0.025 mg H3BO3), supplemented with 30 g L-1 sea salts (Sigma-Aldrich) for L. aggregata IAM12614 and R. nubinhibens ISM. All of the above defined media were additionally supplemented with 1 mM MgSO4, 100 µM CaCl2, and vitamins (33 µM thiamine, 41 µM biotin, 10 nM nicotinic acid). 20 mM of one of the following served as the sole source of carbon: D-glucose (Thermo Fisher), t3Hyp (BOC Sciences), c3Hyp (Chem Impex Int’l), t4Hyp (Bachem), c4Hyp (Sigma-Aldrich), or L-proline (CalBiochem).

### Plasmid construction for gene disruption

RSP3519 was amplified from Rhodobacter sphaeroides 2.4.1 genomic DNA using Pfu DNA polymerase (Thermo) with primers RSP3519F and RSP3519R (Table 9). The resulting PCR product was inserted into the pGEM T Easy vector (Promega) to generate plasmid pRK_RSP3519-1. pRK_RSP3519-1 was digested with SmaI and ligated to a 900 bp blunt-ended chloramphenicol resistance cassette to generate pRK_RSP3519-2. pRK_RSP3519-2 was then used as the template in a PCR with primers RSP3519F and RSP3519R. The resulting product was digested with EcoRI and ligated into pSUP202 to give the plasmid used for gene disruption: pRK_RSP3519-3. To disrupt RSP3519, pRK_RSP3519-3 was electroporated into R. sphaeroides 2.4.1, and double crossover chromosomal gene disruptions were selected by resistance to chloramphenicol and sensitivity to ampicillin (Matsson et al., 1998).

**Table 9.**
 Oligonucleotide primers used for construction of the RS3519 knock-out in Rhodobacter sphaeroides 2.4.1


<table>
  <thead>
    <tr>
      <th>Oligo</th>
      <th>Sequence (5'–3')</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RS3519F.KO</td>
      <td>CATATGATGCGCGTTCAGGACGTGTATAACG</td>
    </tr>
    <tr>
      <td>RS3519R.KO</td>
      <td>GCTGAGCTCAGAGGACGAGGAAGCCCGCGTCC</td>
    </tr>
  </tbody>
</table>

### Cell preparation for gene expression analysis

Starter cultures were initiated from a single colony and grown in the appropriate rich medium overnight. This culture was used to inoculate the appropriate minimal medium (1% inoculum) supplemented with 20 mM D-glucose; the cultures were grown until OD600 0.3–0.5. The cells were pelleted by centrifugation (4750×g for 5 min at 4°C), washed once, and resuspended in minimal medium with no carbon source. For gene expression analysis of individual PRS genes, cultures were divided into two equal volumes, 20 mM D-glucose was added to one volume and 20 mM trans-4-hydroxy-L-proline or trans-3-L-hydroxy proline was added to the other, and cultures were grown for three additional hr prior to cell harvest.

For evaluation of whole genome neighbourhoods of select PRS targets (orange, navy, hotpink, pale green, blue, and sky blue clusters) in A. tumefaciens C58, B. cereus ATCC 14579, and S. lividans TK24, cultures were divided into four equal volumes, supplemented with D-glucose, trans-4-hydroxy-L-proline, trans-3-hydroxy-L-proline, or L-proline to a final concentration of 20 mM, and grown until OD600 0.8–1.0. At the time of cell harvest, one volume of RNAprotect Bacteria Reagent (Qiagen) was added to two volumes of each culture. Samples were mixed by vortexing for 10 s and then incubated for 5 min at room temperature. Cells were pelleted by centrifugation (4750×g for 5 min at 4°C), the supernatant was decanted, and cell pellets were stored at -80°C until further use.

### RNA isolation

RNA isolation was performed in an RNAse-free environment at room temperature using the RNeasy Mini Kit (Qiagen) per the manufacturer's instructions. For B. cereus ATCC 14579 and S. lividans TK24, cells were initially disrupted using a modified bead-beating procedure: cells were resuspended in 400 µl Soil Pro Lysis Buffer (MP Bio), transferred to Lysis Matrix E tubes (MP Bio), and agitated horizontally on a Vortex Mixer (Fisher) with Vortex Adapter (Ambion) for 10 min at speed 10. Beads and cellular debris were pelleted by centrifugation at 16,000 × g for 5 min. 200 µl of the supernatant was used for subsequent RNA isolation. Cell pellets for all other organisms were disrupted according to the ‘Enzymatic Lysis Protocol’ in the RNAprotect Bacteria Reagent Handbook (Qiagen); lysozyme (Thermo-Pierce) was used at 15 mg ml-1. RNA concentrations were determined by absorption at 260 nm using the Nanodrop 2000 (Thermo) and absorption ratios A260/A280 and A260/A230 were used to assess sample integrity and purity. Isolated RNA was stored at -80°C until further use.

### Reverse transcription and quantitative real-time PCR

Reverse transcription (RT) PCRs for A. tumefaciens C58 and B. cereus ATCC 14579 were performed with 300 ng of total isolated RNA using the ProtoScript First Strand cDNA Synthesis Kit (NEB) as per the manufacturer's instructions. For S. lividans TK24 RT-PCRs were performed with 300 ng of total RNA using the Transcriptor First Strand cDNA Synthesis Kit (Roche), with 2.5% DMSO added to relieve secondary structures. All other RT-PCRs were performed with 1 µg of total RNA using the RevertAid H Minus First Strand cDNA Synthesis Kit (Fermentas).

Primers for quantitative real-time (qRT) PCR for A. tumefaciens C58 and B. cereus ATCC 14579 gene targets were designed using the Primer3 primer tool; amplicons were 150–200 bps in length; primers for all other qRT-PCRS were designed using the Universal ProbeLibrary System (Roche); amplicons were 66–110 bps in length Primer sequences are provided in Tables 10 and 11. Primers were 18–27 nucleotides in length and had a theoretical Tm of 55–60°C. Primer efficiency was determined to be at least 90% for each primer pair.

**Table 10.**
 qRT-PCR primers for transcriptional analysis of individual proline racemase superfamily members


<table>
  <thead>
    <tr>
      <th>Oligo</th>
      <th>Sequence (5'–3')</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Atu16s-F</td>
      <td>GACACGGCCCAAACTCCTAC</td>
    </tr>
    <tr>
      <td>Atu16s-R</td>
      <td>GGGCTTCTTCTCCGACTACC</td>
    </tr>
    <tr>
      <td>Atu0398-F</td>
      <td>TCACCATTGAGAAGGCCAAT</td>
    </tr>
    <tr>
      <td>Atu0398-R</td>
      <td>GGTTGACGAGGTCCTTCAGA</td>
    </tr>
    <tr>
      <td>Atu3953-F</td>
      <td>CAGCTTCAGTGGCATCAGG</td>
    </tr>
    <tr>
      <td>Atu3953-R</td>
      <td>GTGTTGTGCCCAATGATCC</td>
    </tr>
    <tr>
      <td>Atu4684-F</td>
      <td>GAAGAGGCGCATGAGATTG</td>
    </tr>
    <tr>
      <td>Atu4684-R</td>
      <td>CGAAACCCAAAGCCTTGTT</td>
    </tr>
    <tr>
      <td>Bc16s-F</td>
      <td>CTCGTGTCGTGAGATGTTGG</td>
    </tr>
    <tr>
      <td>Bc16s-R</td>
      <td>TGTGTAGCCCAGGTCATAAGG</td>
    </tr>
    <tr>
      <td>Bc0905-F</td>
      <td>CTTCGCTGACGGACAAGTAGA</td>
    </tr>
    <tr>
      <td>Bc0905-R</td>
      <td>TGTACCGCTGTTACGGACAA</td>
    </tr>
    <tr>
      <td>Bc2835-F</td>
      <td>AACAGACCCGTGTCATCCTG</td>
    </tr>
    <tr>
      <td>Bc2835-R</td>
      <td>ACTAAGCCAGCCGGTGTATCT</td>
    </tr>
    <tr>
      <td>La16s-F</td>
      <td>TGGTGGGGTAAAGGCCTAC</td>
    </tr>
    <tr>
      <td>La16s-R</td>
      <td>TGGCTGATCATCCTCTCAGAC</td>
    </tr>
    <tr>
      <td>La28492-F</td>
      <td>TGTTGAAGACGAGGCCAAG</td>
    </tr>
    <tr>
      <td>La28492-R</td>
      <td>AAAAGCCGAGCTGTTCGTT</td>
    </tr>
    <tr>
      <td>La28502-F</td>
      <td>CGCGTAATCGACAGCCATA</td>
    </tr>
    <tr>
      <td>La28502-R</td>
      <td>GGCACAGAAATCGAGATGCT</td>
    </tr>
    <tr>
      <td>Rs16s-F</td>
      <td>ACACTGGGACTGAGACACGG</td>
    </tr>
    <tr>
      <td>Rs16s-R</td>
      <td>TACACTCGGAATTCCACTCA</td>
    </tr>
    <tr>
      <td>Rs3519-F</td>
      <td>AGGACATCGCCTTCGAACT</td>
    </tr>
    <tr>
      <td>Rs3519-R</td>
      <td>CGATGATGCCGAAATAGTTG</td>
    </tr>
    <tr>
      <td>Pa16s-F</td>
      <td>TCACACTGGAACTGAGACACG</td>
    </tr>
    <tr>
      <td>Pa16s-R</td>
      <td>ATCAGGCTTTCGCCCATT</td>
    </tr>
    <tr>
      <td>Pa1255-F</td>
      <td>CCACCCTCTGGGAACAGTC</td>
    </tr>
    <tr>
      <td>Pa1255-R</td>
      <td>TCGTTGAGGACGAAGTTGC</td>
    </tr>
    <tr>
      <td>Pa1268-F</td>
      <td>AACAGTGGCTACCTCGGCA</td>
    </tr>
    <tr>
      <td>Pa1268-R</td>
      <td>TCGCCGACCGGTGTCTCGAT</td>
    </tr>
    <tr>
      <td>Rn16s-F</td>
      <td>ATCTGTGTGGGCGCGATT</td>
    </tr>
    <tr>
      <td>Rn16s-R</td>
      <td>GTGAGCGCATTGGTGGTCT</td>
    </tr>
    <tr>
      <td>Rn08250-F</td>
      <td>TATGGCGGCGACAGTTTC</td>
    </tr>
    <tr>
      <td>Rn08250-R</td>
      <td>GACGGCTCGAGCGTAAAC</td>
    </tr>
    <tr>
      <td>Pd16s-F</td>
      <td>GACTGAGACACGGCCCAGA</td>
    </tr>
    <tr>
      <td>Pd16s-R</td>
      <td>TCACCTCTACACTCGGAAT</td>
    </tr>
    <tr>
      <td>Pd1045-F</td>
      <td>TCGGACTACTATGTGCCGATG</td>
    </tr>
    <tr>
      <td>Pd1045-R</td>
      <td>CCTGATCGAGGCCAAAGAC</td>
    </tr>
    <tr>
      <td>Pd1184-F</td>
      <td>GCAATTTCGTGTTGAACGAG</td>
    </tr>
    <tr>
      <td>Pd1184-R</td>
      <td>CATGATGATCCAGCCCATCT</td>
    </tr>
    <tr>
      <td>Pd3467-F</td>
      <td>CTTCGCAGCCCTGTTCAT</td>
    </tr>
    <tr>
      <td>Pd3467-R</td>
      <td>GACCAGCCCTTCCTCGAT</td>
    </tr>
    <tr>
      <td>Pd4859-F</td>
      <td>GGCAAGGTGGACATCGAATA</td>
    </tr>
    <tr>
      <td>Pd4859-R</td>
      <td>CCTCGGGGTAAAGGAAGC</td>
    </tr>
    <tr>
      <td>Sm16s-F</td>
      <td>CGTGGGGAGCAAACAGGATT</td>
    </tr>
    <tr>
      <td>Sm16s-R</td>
      <td>CTAAGGGCGAGGGTTGCGCTC</td>
    </tr>
    <tr>
      <td>Sm20268-F</td>
      <td>CTGGCAAGGTGGACATCAC</td>
    </tr>
    <tr>
      <td>Sm20268-R</td>
      <td>GTAAGGCGCACTTCCTCAA</td>
    </tr>
    <tr>
      <td>Sm20270-F</td>
      <td>CGCCATGTCAATCTCCTGGT</td>
    </tr>
    <tr>
      <td>Sm20270-R</td>
      <td>GGCAGCATCCACGATCACGA</td>
    </tr>
  </tbody>
</table>

**Table 11.**
 qRT-PCR primers for transcriptional analysis of genome neighborhoods


<table>
  <thead>
    <tr>
      <th>Primer</th>
      <th>Sequence (5'–3')</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Sliv-Sco16srRNA-F</td>
      <td>CCGTACAATGAGCTGCGATA</td>
    </tr>
    <tr>
      <td>Sliv-Sco16srRNA-R</td>
      <td>GAACTGAGACCGGCTTTTTG</td>
    </tr>
    <tr>
      <td>Sliv-Sco6289-F</td>
      <td>GACCCTGAAGGTCGTCGTC</td>
    </tr>
    <tr>
      <td>Sliv-Sco6289-R</td>
      <td>GGTGACCGTGACGTCCAT</td>
    </tr>
    <tr>
      <td>Sliv-Sco6290-F</td>
      <td>GTCTTCTGCGGCATCGG</td>
    </tr>
    <tr>
      <td>Sliv-Sco6290-R</td>
      <td>AGTCATCGTCGTCCTCCA</td>
    </tr>
    <tr>
      <td>Sliv-Sco6291-F</td>
      <td>GCCGACCTCGACGAAGA</td>
    </tr>
    <tr>
      <td>Sliv-Sco6291-R</td>
      <td>TTGTCGGTTTCACTGCTGTC</td>
    </tr>
    <tr>
      <td>Sliv-Sco6292-F</td>
      <td>CATCGACACCAAGGTGGAC</td>
    </tr>
    <tr>
      <td>Sliv-Sco6292-R</td>
      <td>TGACCCCGACGATGTACC</td>
    </tr>
    <tr>
      <td>Sliv-Sco6293-F</td>
      <td>GACTACGGCGTGCTCTTCAT</td>
    </tr>
    <tr>
      <td>Sliv-Sco6293-R</td>
      <td>CTCGGTGACCTCGACCAT</td>
    </tr>
    <tr>
      <td>Bc0905-F</td>
      <td>CTTCGCTGACGGACAAGTAGA</td>
    </tr>
    <tr>
      <td>Bc0905-R</td>
      <td>TGTACCGCTGTTACGGACAA</td>
    </tr>
    <tr>
      <td>Bc0906-F</td>
      <td>ACTACGAACGCAACCACACC</td>
    </tr>
    <tr>
      <td>Bc0906-R</td>
      <td>CGGAACTTGAAGGTCTCCTGT</td>
    </tr>
    <tr>
      <td>Bc2832-F</td>
      <td>TACCAGGCTTTGGTCCTGAA</td>
    </tr>
    <tr>
      <td>Bc2832-R</td>
      <td>ATTTGCCGCCAAGCTCTAAC</td>
    </tr>
    <tr>
      <td>Bc2833-F</td>
      <td>GGATGGGTTTCAGTAGCAGGA</td>
    </tr>
    <tr>
      <td>Bc2833-R</td>
      <td>CCTAGTCTTGGATAGCGAGAAGG</td>
    </tr>
    <tr>
      <td>Bc2834-F</td>
      <td>AGGTGCGTATTCGCCAGAAA</td>
    </tr>
    <tr>
      <td>Bc2834-R</td>
      <td>CCTGGCGAACGTACGATAAA</td>
    </tr>
    <tr>
      <td>Bc2835-F</td>
      <td>AACAGACCCGTGTCATCCTG</td>
    </tr>
    <tr>
      <td>Bc2835-R</td>
      <td>ACTAAGCCAGCCGGTGTATCT</td>
    </tr>
    <tr>
      <td>Bc2836-F</td>
      <td>CCTTGCATTCTCGCTTCTGT</td>
    </tr>
    <tr>
      <td>Bc2836-R</td>
      <td>AATCTTAGGAGCCCACACACC</td>
    </tr>
    <tr>
      <td>Atu3947-F</td>
      <td>TCCGGCCAAGTATGTGAAAG</td>
    </tr>
    <tr>
      <td>Atu3947-R</td>
      <td>CTATAGCCGTTCGCAGCAAG</td>
    </tr>
    <tr>
      <td>Atu3948-F</td>
      <td>ATTTCGCCCGTGATCTGTC</td>
    </tr>
    <tr>
      <td>Atu3948-R</td>
      <td>CGGCATCCACAATAATCCAG</td>
    </tr>
    <tr>
      <td>Atu3949-F</td>
      <td>GCGAACAGGCTGAAGAGATG</td>
    </tr>
    <tr>
      <td>Atu3949-R</td>
      <td>CGGCGGTAATTCCTGTTTG</td>
    </tr>
    <tr>
      <td>Atu3950-F</td>
      <td>GCTGCCGAACATATCAAGGT</td>
    </tr>
    <tr>
      <td>Atu3950-R</td>
      <td>GACCTTCGCGGTTATCTGGT</td>
    </tr>
    <tr>
      <td>Atu3951-F</td>
      <td>TGACGGACTCCAGCCTTATC</td>
    </tr>
    <tr>
      <td>Atu3951-R</td>
      <td>ATGTAACATCGGCGTGGTCT</td>
    </tr>
    <tr>
      <td>Atu3952-F</td>
      <td>GATATCGTCAAGGGCGGTTT</td>
    </tr>
    <tr>
      <td>Atu3952-R</td>
      <td>ACGCAGAGCCTTCATGTGTT</td>
    </tr>
    <tr>
      <td>Atu3953-F</td>
      <td>CAACGTCGCCAGTTACCTTC</td>
    </tr>
    <tr>
      <td>Atu3953-R</td>
      <td>GGCTGAGATCAACGACATCC</td>
    </tr>
    <tr>
      <td>Atu3958-F</td>
      <td>GGCGGCTGATACACATCTTC</td>
    </tr>
    <tr>
      <td>Atu3958-R</td>
      <td>AAAGTTGGTGCTTCGTCAGG</td>
    </tr>
    <tr>
      <td>Atu3959-F</td>
      <td>CATTCCTGACACGATCCACA</td>
    </tr>
    <tr>
      <td>Atu3959-R</td>
      <td>CAGCATCAGCAAAGGGAAGT</td>
    </tr>
    <tr>
      <td>Atu3960-F</td>
      <td>GAATGTCGTCGCCATCAAG</td>
    </tr>
    <tr>
      <td>Atu3960-R</td>
      <td>TCGTAGAGTGCCACATGCTC</td>
    </tr>
    <tr>
      <td>Atu3961-F</td>
      <td>TTCGGCACTTCTTTCTGGTC</td>
    </tr>
    <tr>
      <td>Atu3961-R</td>
      <td>GCTCGCCTGCAGATAAACA</td>
    </tr>
    <tr>
      <td>Atu4675-F</td>
      <td>TTCCTGTTATCGTCGGCACT</td>
    </tr>
    <tr>
      <td>Atu4675-R</td>
      <td>GCCTTGAAGTGAGCCTTCTG</td>
    </tr>
    <tr>
      <td>Atu4676-F</td>
      <td>ACGGCTATCGTGAAGGTCAA</td>
    </tr>
    <tr>
      <td>Atu4676-R</td>
      <td>GAATAGCTCGGGCACATCAC</td>
    </tr>
    <tr>
      <td>Atu4682-F</td>
      <td>TCCTCAGAAAGACCGACACC</td>
    </tr>
    <tr>
      <td>Atu4682-R</td>
      <td>GTGAATGTGCCGCAGGTAA</td>
    </tr>
    <tr>
      <td>Atu4684-F</td>
      <td>CCTCGGCAAACTCAAGGTC</td>
    </tr>
    <tr>
      <td>Atu4684-R</td>
      <td>GCGAAGAGGCAGAAGGAAA</td>
    </tr>
    <tr>
      <td>Atu4691-F</td>
      <td>AAGGGCGATATGGGTCTTTC</td>
    </tr>
    <tr>
      <td>Atu4691-R</td>
      <td>GAGCTCTTCGATGCTGTCGT</td>
    </tr>
  </tbody>
</table>

qRT-PCRs were carried out in 96-well plates using the Roche LightCycler 480 II instrument with the LightCycler 480 SYBR Green I Master Mix (Roche) per the manufacturer's instructions. Each 10-µl reaction contained 1 µM of each primer, 5 µl of SYBR Green I Master Mix, and an appropriate dilution of cDNA. Reactions were run as follows: one cycle at 95°C for 5 min, 45 cycles at 95°C for 10 s, 50°C for 10 s, 72°C for 10 s, and a final dissociation program at 95°C for 15 s, 60°C for 1 min, and 95°C for 15 s. Minus-RT controls were performed to verify the absence of genomic DNA in each RNA sample for each gene target analyzed. Gene expression data were expressed as crossing threshold (CT) values. Data were analyzed by the 2-??CT (Livak) method (Livak and Schmittgen, 2001), using the 16S rRNA gene as a reference. Each qRT-PCR was performed in triplicate, and fold-changes are the averages of at least three biological replicates.

### Data deposition

The atomic coordinates and structure factors for ‘4R-hydroxyproline 2-epimerases’ (4HypE) from Pseudomonas putida F1 (citrate-liganded, PDBID:4JBD; sulfate-liganded, PDBID:4JD7), Chromohalobacter salexigens DSM 3043 (apo, PDBID:4JCI), Xanthomonas campestris (phosphate-liganded, PDBID:4JUU), Burkholderia multivorans (phosphate-liganded, PDBID:4K7X), Pseudomonas fluorescens Pf-5 (pyrrole 2-carboxylate-liganded, PDBID:4J9W; trans-4-hydroxy-L-proline-liganded, PDBID:4J9X), Ochrobacterrium anthropic (apo, PDBID:4K8L), and Agrobacterium vitis S4 (trans-4-hydroxy-L-proline-liganded, PDBID:4LB0) and ‘trans-3-hydroxy-L-proline dehydratase’ (t3HypD) from Agrobacterium vitis S4 (pyrrole 2-carboxylate-liganded, PDBID:4K7G) have been deposited in the Protein Data Bank, www.pdb.org.

### UniProt accession IDS

This manuscript describes functional characterization of proteins with the following UniProt accession IDs: A0NXQ7, A0NXQ9, A1B0W2, A1B195, A1B196, A1B7P4, A1BBM5, A1U2K1, A3M4A9, A3PPJ8, A3QFI1, A3QH73, A3S939, A3SU01, A5VZY6, A6WW16, A6WXX7, A8H392, A9AKG8, A9AKH1, A9AL52, A9ALD3, A9AQW9, A9CFU8, A9CFU9, A9CFV0, A9CFV4, A9CFW8, A9CGZ4, A9CGZ5, A9CGZ9, A9CH01, A9CH04, A9CKB4, B0VB44, B1KJ76, B3D6W2, B4EHE6, B9J8G8, B9JHU6, B9JQV3, B9K4G4, B9R4E3, C5ZMD2, D2AV87, D2QN44, D5SQS4, D6EJK6, D6EJK7, D6EJK8, D6EJK9, D6EJL0, Q0B950, Q0B953, Q0B9R9, Q0B9S2, Q16D96, Q1QBF3, Q1QU06, Q1QV19, Q2KD13, Q2T3J4, Q2T596, Q3IWG2, Q3IZJ8, Q3JFG0, Q3JHA9, Q485R8, Q4KAT3, Q4KGT8, Q4KGU2, Q5LKW3, Q5LLV0, Q63FA5, Q6HMS8, Q6HMS9, Q73CR9, Q73CS0, Q7CFV0, Q7CTP1, Q7CTP2, Q7CTP3, Q7CTP4, Q7CTQ2, Q7CTQ3, Q7CTQ5, Q7CVK1, Q7NU77, Q81CD6, Q81CD7, Q81CD8, Q81CD9, Q81CE0, Q81HB0, Q81HB1, Q8FYS0, Q8P833, Q8YFD6, Q92WR9, Q92WS1, Q9I476, Q9I489, and Q9I492.

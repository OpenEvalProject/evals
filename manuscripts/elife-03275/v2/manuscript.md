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

10.7554/eLife.03275.001 Metabolic pathways in eubacteria and archaea often are encoded by operons and/or gene clusters (genome neighborhoods) that provide important clues for assignment of both enzyme functions and metabolic pathways. We describe a bioinformatic approach (genome neighborhood network; GNN) that enables large scale prediction of the in vitro enzymatic activities and in vivo physiological functions (metabolic pathways) of uncharacterized enzymes in protein families. We demonstrate the utility of the GNN approach by predicting in vitro activities and in vivo functions in the proline racemase superfamily (PRS; InterPro IPR008794). The predictions were verified by measuring in vitro activities for 51 proteins in 12 families in the PRS that represent ~85% of the sequences; in vitro activities of pathway enzymes, carbon/nitrogen source phenotypes, and/or transcriptomic studies confirmed the predicted pathways. The synergistic use of sequence similarity networks 3 and GNNs will facilitate the discovery of the components of novel, uncharacterized metabolic pathways in sequenced genomes. DOI: http://dx.doi.org/10.7554/eLife.03275.001

## Introduction

The explosion in the number of sequenced eubacterial and archaeal genomes provides a challenge for the biological community: >50% of the proteins/enzymes so identified have uncertain or unknown in vitro activities and in vivo physiological functions. Genome context can provide important clues for assignment of functions to individual enzymes and, also, guide the discovery of novel metabolic pathways: pathways often are encoded by operons and/or gene clusters. However, large-scale approaches are required to efficiently mine this information for entire protein/enzyme families (Dehal et al., 2010; Caspi et al., 2012; Markowitz et al., 2012; Franceschini et al., 2013; Overbeek et al., 2014).

In this manuscript, we describe the use of a new bioinformatic strategy, genome neighborhood networks (GNNs), to discover the enzymes, transport systems, and transcriptional regulators that constitute metabolic pathways, thereby facilitating prediction of their individual in vitro activities and combined in vivo metabolic functions. As the first demonstration of its use, we applied this approach to the functionally diverse proline racemase superfamily (PRS) and predicted functions for >85% of its members. The predictions were verified using high-throughput protein expression and purification, in vitro enzyme activity measurements, microbiology (phenotypes and transcriptomics), and X-ray crystallography.

Three enzymatic activities have been described for the PRS: proline racemase (ProR; eubacteria [

![Figure 1.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig1-v2.jpg)

**Figure 1.:** trans-3-hydroxy-L-proline dehydratase (t3HypD) and the metabolic pathways in which they participate.cHyp oxidase, Pyr4H2C deaminase, a-KGSA dehydrogenase, and ?1-Pyr2C reductase belong to the D-amino acid oxidase (DAAO), dihydrodipicolinate synthase (DHDPS), aldehyde dehydrogenase, and ornithine cyclodeaminase (OCD) (or malate/L-lactate dehydrogenase 2 [MLD2]) superfamilies, respectively. Abbreviations: L-Pro: L-proline; D-Pro: D-proline; 5-AV: 5-aminovalerate; t4Hyp: trans-4-hydroxy-L-proline; c4Hyp: cis-4-hydroxy-D-proline; Pyr4H2C: ?1-pyrroline 4-hydroxy 2-carboxylate; a-KGSA: a-ketoglutarate semialdehyde; a-KG: a-ketoglutarate; t3Hyp: trans-3-hyroxy-L-proline; ?2-Pyr2C: ?2-pyrroline 2-carboxylate; ?1-Pyr2C: ?1-pyrroline 2-carboxylate.DOI: http://dx.doi.org/10.7554/eLife.03275.003

## Results

## Sequence similarity network for the PRS

A sequence similarity network (SSN) (

![Figure 2.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig2-v2.jpg)

**Figure 2.:** (A) The SSN displayed with an e-value threshold of 10-55 (~35% sequence identity). (B) The SSN displayed with an e-value threshold of 10-110 (~60% sequence identity).DOI: http://dx.doi.org/10.7554/eLife.03275.004

At the e-value threshold of 10-110 (Figure 2B) the nodes for the experimentally characterized functions—ProR (magenta; cluster 7), 4HypE (blue and red; clusters 1 and 2, respectively), and t3HypD (brown; cluster 8)—are located in separate clusters that account for ~30% of the sequences in the PRS. When the e-value threshold is relaxed to 10-55, most of the clusters merge, although the nodes associated with the two previously characterized 4HypE clusters in the 10-110 network remain separated. Sequence alignments predict that the active sites of both characterized 4HypE clusters contain two active site Cys residues. We conclude that these two families of 4HypEs evolved from divergent, but homologous, ancestors.

At the e-value threshold of 10-110 (Figure 2B), the separated clusters are expected to be isofunctional because, from sequence alignments, their active sites are formed from conserved amino acid residues (acid/base catalysts and specificity determining residues). Although many of the clusters are predicted to have the two active site Cys residues found in the structurally characterized ProR (PDB: 1W61) and 4HypE (PDB: 2AZP [Liu et al.]), others are missing one or both of the Cys residues. The previously uncharacterized enzymes with differing residues could either represent new functions or additional examples of evolution of the ProR, 4HypE, and t3HypD functions from divergent, but homologous, ancestors.

## GNN for the PRS

We predicted functions for ~80% of the remaining members of the PRS by analyzing the SSN for the proteins (including enzymes, transport systems, and transcriptional regulators) encoded by the genome neighborhoods for ‘all’ members of the PRS (specifically, ± 10 genes relative to the gene encoding each PRS member, the query). A protein in this genome neighborhood SSN, designated the ‘genome neighborhood network’ (GNN), is expected to be functionally related to a query in the PRS if they are located in an operon and/or gene cluster that encodes a metabolic pathway that includes the query. By analyzing many genome neighborhoods simultaneously, e.g., for all members of the PRS, the signals associated with functionally related proteins will be amplified; the signals associated with functionally unrelated genome proximal proteins that occur ‘randomly’ across many species will contribute to the background ‘noise’. We propose that this large-scale approach is more efficient in identifying ‘all’ of the enzymes/transport systems/transcriptional regulators in a conserved metabolic pathway than by a one-genome-at-a-time analysis.

Our approach for visualizing a GNN first assigns a unique query color and number to the members of each cluster in the input SSN that separates the members of the PRS into clusters that are likely to be isofunctional (e-110 in this work). After collecting the genome neighbors, we assign each of them the same color as the color of the query; with this strategy, proteins that are encoded by the same genome neighborhood as the query are easily identified in the GNN because they share the same color as the query. We then perform an all-by-all BLAST on the sequences of the genome neighbors and display the results as an SSN using an e-value threshold of 10-20; this SSN is the GNN. Using this e-value threshold, most of the clusters in the GNN contain the members of distinct protein families and superfamilies (e.g., Pfam families); however, in some cases, divergent families in functionally diverse superfamilies may be found in separate clusters. Genome neighborhood proteins that occur randomly across divergent species and are functionally unrelated to the queries are expected to be located in small clusters with multiple colors, so these can be quickly identified visually and discarded from further analysis. The PRS queries from the input SSN (‘zero sequences’ in collecting the ±10 neighbors) are not displayed in the GNN, except when multiple members of the PRS are proximal on the genome, that is, when one PRS member is in the genome neighborhood of another (vide infra).

The GNN for the PRS (

![Figure 3.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig3-v2.jpg)

**Figure 3.:** (A) The GNN displayed with an e-value threshold of 10-20. The nodes are colored by the color of query nodes in the SSN (Figure 2A). The clusters are labeled with the UniProtKB/TrEMBL annotations. (B–I) Selected superfamily clusters from the GNN showing node colors. (B) D-proline reductase PrdA. (C) D-proline reductase, PrdB. (D) D-amino acid oxidase (DAAO). (E) Dihydrodipicolinate synthase (DHDPS). (F) Aldehyde dehydrogenase. (G) Ornithine cyclodeaminase (OCD). (H) Malate/L-lactate dehydrogenase 2 (MLD2). (I) Proline racemase.DOI: http://dx.doi.org/10.7554/eLife.03275.005

## Retrospective tests of GNN: ProR and 4HypE functions

As a retrospective use of the GNN, the ProR function is encoded by anaerobic eubacteria that ferment L-proline and is represented by the magenta cluster (cluster 7) in the SSN (Figure 2B). The first step in the catabolism of L-proline is racemization to D-proline (by ProR) that is reduced to 2-keto-5-aminopentanoate by D-proline reductase (Kabisch et al., 1999) (by PrdAB; Figure 1). In the GNN, the clusters for the PrdA and PrdB polypeptides in D-proline reductase are uniformly magenta, as expected if the genes encoding ProR and PrdAB are colocalized with the gene encoding ProR (Figure 3B,C). The lack of other colors in the PrdAB clusters in the GNN implies that no other clusters in the SSN have the ProR function.

As a second retrospective example, the 4HypE function has been assigned to members of the blue (cluster 1) and red (cluster 2) clusters in the SSN (Figure 2B). In the GNN, clusters identified by the blue and red clusters include the D-amino acid oxidase (DAAO; Figure 3D) (Watanabe et al., 2012), dihydrodipicolinate synthase (DHDPS; Figure 3E) (Singh and Adams, 1965; Watanabe et al., 2012), and aldehyde dehydrogenase (Figure 3F) (Koo and Adams, 1974; Watanabe et al., 2007) superfamilies as well as components of several types of transport systems. As we and others recently established for organisms that use trans-4-hydroxy-L-proline betaine as sole carbon and nitrogen source (Zhao et al., 2013; Kumar et al., 2014), the catabolic pathway for trans-4-hydroxy-L-proline (t4Hyp) (Figure 1) can be initiated by the epimerization of t4Hyp to cis-4-hydroxy-D-proline (c4Hyp) by 4HypE, followed by reactions catalyzed by c4Hyp oxidase (a member of the DAAO superfamily), c4Hyp imino acid dehydratase/deaminase (a member of the DHDPS superfamily), and a-ketoglutarate semialdehyde dehydrogenase (a member of the aldehyde dehydrogenase superfamily). Thus, the occurrence of blue and red nodes in these three clusters in the GNN is expected.

## Discovery of new families of 4HypEs

The DAAO (

![Figure 4.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig4-v2.jpg)

**Figure 4.:** These substrates were divided into four groups to avoid mass duplication.DOI: http://dx.doi.org/10.7554/eLife.03275.006

## X-ray structure of a novel 4HypE

The X-ray structure of one of the previously functionally assigned 4HypEs (Uniprot: Q4KGU2; locus tag: PFL_1412; red, cluster 2) was determined in the presence of the substrate,

![Figure 5.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig5-v2.jpg)

**Figure 5.:** (A) Structure of Q4KGU2 (locus tag: PFL_1412; cluster 2) with PYC illustrating the utilization of the carboxyl group to bridge the N-terminal amide backbone groups of two opposing a-helices. While In B9K4G4 (D) and B9JQV3 (C) the relative positions of residues that coordinate the prolyl nitrogen (Asp 232, His 90) are conserved His 90 is replaced by a Ser. (B) Structure of Q4KGU2 with t4Hyp illustrating the interactions Q4KGU2 with the 4-hydroxyl group and the relative positions of the two catalytic cysteine residues. (C) Structure of B9JQV3 (locus tag: Avi_0518, cluster 9) with t4Hyp illustrating the interactions of B9JQV3 with the 4-hydroxyl group of t4Hyp and the relative positions of the catalytic Ser (Ser 93, trans?cis) and Cys (Cys 236, cis?trans). (D) Structure of B9K4G4 (Avi_7022, cluster 3) with PYC illustrating the position of the catalytic Ser (Ser 90, dehydration), and the non-catalytic orientation of Thr 256 which replaces the Cys observed in Cys/Cys containing PRS members. In addition, the catalytic Ser (Ser 90) is positioned by hydrogen bonding interactions between the side chain of Asn 93 (shown) and the backbone nitrogen of Asn 93 (not shown). Based on this work, all ProR family members with a catalytic Ser at this position (including B9JQV3, determined here) are proposed to have this motif.DOI: http://dx.doi.org/10.7554/eLife.03275.012

## Discovery of novel families of t3HypDs and ?1-Pyr2C reductases

The

![Figure 6.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig6-v2.jpg)

**Figure 6.:** (A) The OCDS SSN displayed at the e-value cutoff 10-45 (~35% sequence identity). The Pyr2C reductase function is located in four clusters; these proteins are shown in large colored circles, labeled from 1 to 16, and color-coded by the colors of the PRS query sequences shown in Figure 2B. Proteins representing several previously characterized functions in the OCDS are shown by large diamonds, with borders in hotpink (L-alanine dehydrogenase [Schröder et al., 2004]), brown (ornithine cyclodeaminase [Goodman et al., 2004]), magenta (lysine cyclodeaminase [Gatto et al., 2006]), red (ketamine reductase [Hallen et al., 2011]), green (L-arginine dehydrogenase [Li and Lu, 2009]) and palegreen (tauropine dehydrogenase [Kan-No et al., 2005; Plese et al., 2008]), respectively. Their annotations are shown in italics. The diamonds with blue and olive borders are Pyr2C reductases recently characterized by Watanabe et al. (2014). (B) Kinetics data for the Pyr2C reductase activity for the 16 members of the OCDS shown in panel A using NADPH as the cosubstrate.DOI: http://dx.doi.org/10.7554/eLife.03275.014

## Structure of a novel t3HypD

We determined the structure of a t3HypD (B9K4G4) from the light sky blue cluster (cluster 3) in the presence of PYC (Table 6). Instead of the typical PRS Cys/Cys pair, B9K4G4 contains Ser 90 in a similar conformation as was determined for B9JQV3 from the orange cluster (4HypE activity) and Thr 256 on the opposing face (Figure 5D). Thr 256 mimics the conformation of the typical PRS Cys residue but with the side-chain methylene positioned against the anomeric carbon. Again, the assignment of function enabled by the GNNs identifies convergent evolution of function within the PRS.

## Discovery of additional families of 4HypEs, t3HypDs, and ?1-Pyr2C reductases

Members of the light sky blue (cluster 3) cluster in the SSN identify the same (super)families identified by both the 4HypE and t3HypD clusters (transport systems, transcriptional regulators, DAAO [Figure 3D], DHDPS [Figure 3E], aldehyde dehydrogenase [Figure 3F], and OCD [Figure 3G]); however, several members of the light sky blue cluster identify a GNN cluster annotated as the malate/L-lactate dehydrogenase 2 superfamily (MLD2; NADH-dependent oxidoreductases) (Muramatsu et al., 2005) (Figure 3H). Using purified members of the PRS, we determined that the light sky blue cluster is functionally heterogeneous (and some members are promiscuous) for the 4HypE and t3HypD functions (Tables 1 and 2). We also determined that members of the MLD2 superfamily in the GNN catalyze the reduction of proline ketimine (Table 7). Thus, the GNN provided essential information for predicting/assigning functions to the members of the light sky blue cluster in the PRS SSN.10.7554/eLife.03275.015Table 7.Kinetic constants for the proline ketimine reductases (members of the malate/Llactate dehydrogenase 2 [MLD2] and ornithine cyclodeaminase [OCD] superfamilies) that are in the genome neighborhoods of members of the PRSDOI: http://dx.doi.org/10.7554/eLife.03275.015ClusterUniProtLocus tagCofactorkcat [s-1]Km [mM]kcat/KM[M-1s-1]MLD2_PRS_light skyblue (3)Q7CVK1Atu4676NADPH32 ± 10.33 ± 0.0499000Q9I492PA1252NADPH1.6 ± 0.050.41 ± 0.063900MLD2_PRS_Red (2)Q4KGT8PFL_1416NADPH20 ± 0.81.1 ± 0.218000Q0B9S2Bamb_3547NADPH54 ± 139.4 ± 45700A9ALD3Bmul_4451NADPH33 ± 27.4 ± 14400MLD2_PRS_indigo (13)Q4KAT3PFL_3547aNADPH--2300bOCD_PRS_light skyblue (3)A1B196Pden_1185NADPH260 ± 203.1 ± 0.785000NADH81 ± 2016 ± 65100A3S939EE36_06353aNADPH6.8 ± 0.71.0 ± 0.36700A3SU01NAS141_11281aNADPH39 ± 41.2 ± 0.432000NADH8.2 ± 473 ± 50110Q16D96RD1_0323aNADPH15 ± 10.27 ± 0.0756000NADH3.7 ± 0.411 ± 3320Q5LLV0SPO3821aNADPH130 ± 203.0 ± 0.943000NADH--840bQ3IZJ8RSP_0854aNADPH66 ± 40.43 ± 0.09150000NADH12c--OCD_PRS_navy (5)Q81HB0BC_0906NADPH15 ± 10.47 ± 0.131000NADH19 ± 111 ± 21800Q73CR9BCE_0995NADPH15 ± 11.1 ± 0.313000NADH2.1 ± 0.37.6 ± 3270Q6HMS8BT9727_0800NADPH11 ± 13.4 ± 0.93100NADH2.1 ± 0.418 ± 6120Q63FA5BCE33L0803NADPH5.8c--NADH0.87 ± 0.14.9 ± 2180OCD_PRS_olive (12)Q0B953Bamb_3766NADPH106 ± 41.6 ± 0.264000NADH41 ± 67.3 ± 35700Q2T596BTH_II1457aNADPH73 ± 20.39 ± 0.05190000NADH203 ± 2332 ± 76400Q3JFG0BURPS1710b_A2543aNADPH7.8 ± 0.50.64 ± 0.112000NADH6.0 ± 131 ± 13190A9AKH1Bmul_4263NADPH25 ± 64 ± 26400OCD_PRS_blue (1)Q485R8CPS_1455NADPH35 ± 0.81.8 ± 0.220000NADH--170bA3QH73Shew_2955aNADPH6.7 ± 0.71.6 ± 0.64300NADH0.37 ± 0.126 ± 1014aHighly homologous to MLD2 or OCD which are in the gene context of proline racemase.bThe enzyme didn’t saturate.cKM is too small (< 0.03mM).

## Discussion

Although in most cases interpretations of the functional relationships of the clusters in the GNN with those in the query SSN are straightforward, complications can arise. For example, in several species, two members of the PRS are encoded by proximal genes, that is, a 4HypE and a t3HypD; these species can utilize both t4Hyp and trans-3-hydroxy-L-proline as carbon and nitrogen sources. Thus, the GNN contains a cluster for the PRS (right-hand cluster in the top row [when used as query, each PRS finds the adjacent PRS; Figure 3I]). For these species, clusters in the GNN are a composite of two genome contexts, that is, the proteins/enzymes that participate in both catabolic pathways. These situations can be deconvoluted by coloring the nodes identified by two queries with the colors for both query clusters in the GNN. With the genome contexts/metabolic pathways identified for ‘genome-isolated’ 4HypEs and t3HypDs, this complication is easy to identify and understand.

The GNN also is useful to assess the physiological importance of in vitro promiscuity. Several of the purified proteins catalyze both the 4HypE and

![Figure 7.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig7-v2.jpg)

**Figure 7.:** (A) SSN for the PRS with cluster numbers. (B) D-amino acid oxidase (DAAO). (C) Dihydrodipicolinate synthase (DHDPS). (D) Aldehyde dehydrogenase. (E) Ornithine cyclodeaminase (OCD). (F) Malate/L-lactate dehydrogenase 2 (MLD2). (G) The color scheme for B–F.DOI: http://dx.doi.org/10.7554/eLife.03275.016

As established in this study, the majority of the members of the PRS catalyze only the three previously characterized (known) reactions (

![Figure 8.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig8-v2.jpg)

**Figure 8.:** Colors match the color scheme in Figure 2B.DOI: http://dx.doi.org/10.7554/eLife.03275.017

However, large-scale prediction and assignment of function to members of many functionally diverse (super)families will be more complicated than that described for the PRS and require information from complementary experimental and computational approaches. The use of GNNs is restricted to those enzymes that are encoded by proximal operons and/or gene clusters in eubacteria and archaea. For Escherichia coli K-12, 60% of the genes are located in polycistronic transcriptional units that may provide linked functional information that can be used to identify pathways; 40% are located in monocistronic transcriptional units (http://regulondb.ccg.unam.mx/menu/tools/regulondb_overviews/chart_form.jsp). Thus, genome neighborhood context is not a general solution to infer functions for many proteins/enzymes of unknown function encoded eubacterial and archaeal genomes. Even for those proteins encoded by polycistronic transcriptional units, complete metabolic pathways may be encoded by multiple transcriptional units (mono- and/or polycistronic) that are not genome proximal; these pathways and their component enzymes and ligand binding proteins (solute binding proteins for transport systems and transcriptional regulators) may be recognized by regulon analyses that identify conserved binding sites for transcriptional regulators (Ravcheev et al., 2013; Rodionov et al., 2013).

To the extent that genome neighborhoods and/or regulons allow the identification of the components of unknown/novel metabolic pathways, the locations of these proteins/enzymes in the SSNs for their (super)families will provide restrictions on their ligand/substrate specificities and/or reaction mechanisms (Atkinson et al., 2009). Also, as we recently demonstrated (Zhao et al., 2013), in silico (virtual) docking of ligand libraries to multiple binding proteins and enzymes in an unknown metabolic pathway (pathway docking) is a powerful approach to enhance the reliability of docking to predict novel ligand/substrate specificities and identify novel metabolic pathways

Irrespective of the many complications associated with assignment of function to unknown proteins/enzymes, we conclude that GNNs provide a novel approach for large-scale analysis and visualization of genome neighborhood context in enzyme (super)families. We are continuing to improve the use of GNNs as well as regulon analyses and pathway docking to facilitate the discovery of novel enzymes and the metabolic pathways in which they function.

## Materials and methods

## Sequence similarity networks (SSN)

The SSNs for the PRS (Figure 2) and the OCDS (Figure 5A) were created using Pythoscape v1.0 (Barber and Babbit, 2012) that is available for download from http://www.rbvi.ucsf.edu/trac/Pythoscape The input sequences were downloaded from the InterPro webpages of PRS and OCDS: http://www.ebi.ac.uk/interpro/entry/IPR008794, http://www.ebi.ac.uk/interpro/entry/IPR003462, respectively. Cytoscape v2.8 (Smoot et al., 2011) is used for visualization and analysis of the SSN.

## Genome neighborhood network (GNN)

The GNN for the PRS (Figure 3) was also created using Pythoscape v1.0 (Barber and Babbit, 2012). At an e-value cutoff 10-110, each cluster in the SSN was assigned a unique cluster number and color, which are used for labeling and coloring genome context sequences. Genome context sequences were collected from the ±10 gene range of each PRS member and used as the input sequences for making the GNN using the procedure for generating a SSN.

## Protein production

Genes for members of the PRS that are encoded by the genomic DNAs in the Macromolecular Therapeutics Development Facility at the Albert Einstein College of Medicine were cloned into pNIC28-BSA4-based expression vectors as previously described (Sauder et al., 2008).

## Protein expression

The pNIC28-BSA4-based expression plasmids were transformed into Escherichia coli BL21(DE3) containing the pRIL plasmid (Stratagene, Agilent Technologies, Inc., Wilmington, DE) and used to inoculate 20 ml 2xYT cultures containing 50 µg/ml kanamycin and 34 µg/ml chloramphenicol. Cultures were allowed to grow overnight at 37°C in a shaking incubator; these were used to inoculate 2 L of PASM-5052 auto-induction medium (Studier). The cultures were placed in a LEX48 airlift fermenter and incubated at 37°C for 5 hr and then at 22°C overnight (16–20 hr). The cells were collected by centrifugation at 6000×g for 10 min and stored at -80°C.

## Purification of proteins

Cells were resuspended in Lysis Buffer (20 mM HEPES, pH 7.5, containing 20 mM imidazole, 500 mM NaCl, and 5% glycerol) and lysed by sonication. Lysates were clarified by centrifugation at 35,000×g for 45 min. The clarified lysates were loaded on a 1-ml His60 Ni-NTA column (Clontech) using an AKTAxpress FPLC (GE Healthcare). The columns were washed with 10 column volumes of Lysis Buffer and eluted with buffer containing 20 mM HEPES, pH 7.5, containing 500 mM NaCl, 500 mM imidazole, and 5% glycerol. The purified proteins were loaded onto a HiLoad S200 16/60 PR gel filtration column equilibrated with a buffer containing 20 mM HEPES, pH 7.5, 150 mM NaCl, 5% glycerol, and 5 mM DTT. The purities of the proteins were analyzed by SDS-PAGE. The proteins were snap frozen in liquid N2 and stored at -80°C.

## Crystallization

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

## Structure determination

Diffraction data were collected on beamline 31-ID (LRL-CAT, Advanced Photon Source, Argonne National Laboratory, IL) from single crystals at 100 K and a wavelength of 0.9793 Å. Data were integrated using MOSFLM (Battye et al., 2011) and scaled in SCALA (Evans, 2006).

Suitable molecular replacement models existed for all of the protein targets of this study. These included, 2AZP, a putative 4HypE (from cluster 2) determined unliganded by the Midwest Center for Structural Genomics, and 1TM0 (Forouhar et al., 2007), a putative t3HypD (cluster 3, also similar to cluster 9) with an unliganded and disordered active site, determined by the Northeast Structural Genomics Consortium. Molecular replacement computations were performed in AMORE (Navaza, 1994) utilizing the structure that exhibited the greatest homology to the target. If this was unsuccessful, either due to the particular issues with the space group, asymmetric unit composition, or a different orientation of the two domains, molecular replacement was performed with each of the domains separately within PHENIX (Adams et al., 2004; Zwart et al., 2008).

Iterative cycles of manual rebuilding within COOT (Emsley and Cowtan, 2004) and refinement within PHENIX were performed until the entire sequence was modeled. Inclusion of ligands, TLS (translation/libration/screw) refinement (domains chosen automatically within PHENIX) (Winn et al., 2001; Painter and Merritt, 2006) and editing of the solvent structure were performed in the final refinement cycles.

With one exception, the entire sequences of all of the targets could be modeled, except for a small number of residues at the N- or C-termini. The one outlier was A6WW16 that had several disordered regions around the active site similar to the previously determined structure from this cluster (1TM0, cluster 3, light sky blue). Due to the relatively weak binding of the proline racemase family members for their substrates, inhibitors and substrates were included at high concentrations (25–200 mM). Even at these concentrations, several structures were determined from cluster 2 that bound anionic ligands (phosphate, citrate, etc) from the crystallization medium rather than the co-crystallized ligand, and the degree of domain closure about that ligand varied. For all of the structures liganded with either PYC or t4Hyp, the structures are determined in a closed state with Ca–Ca distances of 7–8 Å for the opposing active site catalytic Cys–Cys (cluster 2, red), Ser–Thr (cluster 3, light sky blue) or Ser–Cys dyad (cluster 9, orange). In the case of Q4KGU2, the ligand was t4Hyp state based on the electron density. In contrast, for B9JQV3, the density for the ligand had significant planer character, suggesting a mixture of t4Hyp and c4Hyp.

## ESI-MS screening of ProR, 4HypE, and t3HypD activities

Enzyme activity was screened by the mass change resulting from racemization /epimerization (+1 peak shift) and/or dehydration (-17 peak shift) for reactions in D2O. Each enzyme (1 µM) was incubated with substrate libraries (Table 1) containing proline and proline betaine derivatives (0.1 mM each) along with 20 mM ammonium bicarbonate in D2O at a final volume of 200 µl at 30°C for 16 hr. 50 µl of the reaction mixture was aliquoted and dried with an Eppendorf vacufuge concentrator. The residue was suspended in 10 µl of H2O, and 5 µl of the solution was mixed with the 5 µl of 50% methanol containing 0.4% (vol/vol) formic acid. A 10 µl sample was analyzed for ESI-MS.

## 1H NMR assay to confirm PRS reactions

If a change in mass was observed in the ESI-MS screening assays, a

![Figure 9.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig9-v2.jpg)

**Figure 9.:** t3HypD reactions by 1H NMR.(A) 1H NMR spectra of the 4Hyp substrate mixture in 25 mM Na+-phosphate buffer, pD 8, in D2O (top) and 4Hyp mixture with A3QFI1 (cluster 1, blue) showing 4Hyp epimerization (bottom). The red arrow indicates the proton at C2 for epimerization. The enzyme was stored in glycerol, so the spectra show resonances for glycerol between 3.4 and 3.7 ppm. (B) 1H NMR spectra of the t3Hyp substrate mixture in 25 mM Na+-phosphate buffer, pD 8, in D2O (top), t3Hyp mixture with D0B556 (cluster 3, light sky blue) showing 3Hyp epimerization (middle), and t3Hyp mixture with B9K4G4 (cluster 3, light sky blue) showing t3Hyp dehydration (bottom). The red arrow indicates the proton at C2 for epimerization; the green arrow indicates the proton at C3 for dehydration.DOI: http://dx.doi.org/10.7554/eLife.03275.018

## Polarimetric assay to determine PRS kinetics

The enzyme activity was measured in a Jasco P-1010 polarimeter with a Hg 405-nm filter at 25°C by quantitating the change in optical rotation. The assay mixture contained 1 mM dithiothreitol (DTT) and 50 mM Na+-phosphate buffer, pH 8.0.

## UV spectrophotometric assay for ?1-Pyr2C reductase activity

?1-Pyr2C reductase assays were performed by measuring the decrease in the absorbance of NAD(P)H at 340 nm at 25°C with a Cary 300 Bio UV-Visible spectrophotometer (Varian). The reaction mixture (300 µl) contained variable concentrations of Pyr2C, 50 mM Tris–HCl buffer, pH 7.6, 0.16 mM NAD(P)H, and enzyme.

## 1H NMR assay for ?1-Pyr2C reductase activity

The reaction mixture contained 10 mM ?

![Figure 10.](https://cdn.elifesciences.org/articles/03275/elife-03275-fig10-v2.jpg)

**Figure 10.:** 1H NMR spectra for ?1-pyrroline-2-carboxylate (?1-Pyr2C) reductase activity.(A) 1H NMR spectrum of ?1-Pyr2C substrate in sodium phosphate, pD 8.0, in D2O. (B) 1H NMR spectrum of Q7CVK1 (locus tag: Atu4676) incubated with ?1-Pyr2C, NADPH, and the cofactor regeneration system of alcohol dehydrogenase (NADP+-dependent) and isopropanol in sodium phosphate, pD 8.0 in D2O. (C) 1H NMR spectrum of L-proline in 25 mM sodium phosphate, pD 8.0, in D2O.DOI: http://dx.doi.org/10.7554/eLife.03275.019

## Bacterial strains and growth conditions

Bacterial strains are listed in Table 8. All strains were grown at 30°C with shaking at 225 rpm and were routinely cultured in Tryptic Soy Broth (Difco), supplemented with 30 g L-1 sea salts (Sigma-Aldrich) for Labrenzia aggregata IAM12614 and Roseovarius nubinhibens ISM.10.7554/eLife.03275.020Table 8.Strains used in this studyDOI: http://dx.doi.org/10.7554/eLife.03275.020OrganismAgrobacterium tumefaciens C58Sinorhizobium meliloti 1021Labrenzia aggregata IAM12614Pseudomonas aeruginosa PAO1Paracoccus denitrificans PD1222Rhodobacter sphaeroides 2.4.1Rhodobacter sphaeroides 2.4.1?RSP3519Bacillus cereus ATCC14579Roseovarius nubinhibens ISMEscherichia coli MG1655Streptomyces lividans TK24

For gene expression analyses and carbon utilization studies, strains were cultured in the following defined media:

Agrobacterium tumefaciens C58 was cultured in M9 minimal medium (per liter: 12.8 g Na2HPO4.7H2O, 3.0 g KH2PO4, 0.5 g NaCl, 1.0 g NH4Cl); B. cereus ATCC 14579 was cultured in a modified Spizizen's minimal medium (Spizizen., 1958) (per liter: 2.0 g (NH4)2SO4, 11.0 g K2HPO4, 6.0 g KH2PO4, 1.0 g sodium citrate.2H2O).

Streptomyces lividans TK24 was cultured in a modified minimal medium of Hopwood (Hopwood., 1967) (per liter: 1.0 g (NH4)2SO4, 0.5 g K2HPO4, 0.005 g FeSO4.7H2O). M9 minimal medium, and Spizizen's minimal medium were supplemented with the following trace metals (per liter: 0.003 mg CuSO4.5H2O, 0.025 mg H3BO3, 0.007 mg CoCl2.6H2O, 0.016 mg MnCl2.4H2O, 0.003 mg ZnSO4.7H2O, 0.3 mg FeSO4.7H2O). The minimal medium of Hopwood was supplemented with the following trace metals (per liter: 0.08 mg ZnCl2, 0.4 mg FeCl3.6H2O, 0.02 mg CuCl2.2H2O, 0.02 mg MnCl2.4H2O, 0.02 mg Na2B4O7.10H2O, 0.02 mg (NH4)6Mo7O24.4H2O).

All other strains were grown in the following defined medium (per liter: 17.0 g K2HPO4, 2.5 g (NH4)2SO4, 2.0 g NaCl) supplemented with the following trace metals (0.3 mg FeSO4.7H2O, 0.003 mg ZnSO4.7H2O, 0.003 mg CuSO4.5H2O, 0.025 mg H3BO3), supplemented with 30 g L-1 sea salts (Sigma-Aldrich) for L. aggregata IAM12614 and R. nubinhibens ISM. All of the above defined media were additionally supplemented with 1 mM MgSO4, 100 µM CaCl2, and vitamins (33 µM thiamine, 41 µM biotin, 10 nM nicotinic acid). 20 mM of one of the following served as the sole source of carbon: D-glucose (Thermo Fisher), t3Hyp (BOC Sciences), c3Hyp (Chem Impex Int’l), t4Hyp (Bachem), c4Hyp (Sigma-Aldrich), or L-proline (CalBiochem).

## Plasmid construction for gene disruption

RSP3519 was amplified from Rhodobacter sphaeroides 2.4.1 genomic DNA using Pfu DNA polymerase (Thermo) with primers RSP3519F and RSP3519R (Table 9). The resulting PCR product was inserted into the pGEM T Easy vector (Promega) to generate plasmid pRK_RSP3519-1. pRK_RSP3519-1 was digested with SmaI and ligated to a 900 bp blunt-ended chloramphenicol resistance cassette to generate pRK_RSP3519-2. pRK_RSP3519-2 was then used as the template in a PCR with primers RSP3519F and RSP3519R. The resulting product was digested with EcoRI and ligated into pSUP202 to give the plasmid used for gene disruption: pRK_RSP3519-3. To disrupt RSP3519, pRK_RSP3519-3 was electroporated into R. sphaeroides 2.4.1, and double crossover chromosomal gene disruptions were selected by resistance to chloramphenicol and sensitivity to ampicillin (Matsson et al., 1998).10.7554/eLife.03275.021Table 9.Oligonucleotide primers used for construction of the RS3519 knock-out in Rhodobacter sphaeroides 2.4.1DOI: http://dx.doi.org/10.7554/eLife.03275.021OligoSequence (5'–3')RS3519F.KOCATATGATGCGCGTTCAGGACGTGTATAACGRS3519R.KOGCTGAGCTCAGAGGACGAGGAAGCCCGCGTCC

## Cell preparation for gene expression analysis

Starter cultures were initiated from a single colony and grown in the appropriate rich medium overnight. This culture was used to inoculate the appropriate minimal medium (1% inoculum) supplemented with 20 mM D-glucose; the cultures were grown until OD600 0.3–0.5. The cells were pelleted by centrifugation (4750×g for 5 min at 4°C), washed once, and resuspended in minimal medium with no carbon source. For gene expression analysis of individual PRS genes, cultures were divided into two equal volumes, 20 mM D-glucose was added to one volume and 20 mM trans-4-hydroxy-L-proline or trans-3-L-hydroxy proline was added to the other, and cultures were grown for three additional hr prior to cell harvest.

For evaluation of whole genome neighbourhoods of select PRS targets (orange, navy, hotpink, pale green, blue, and sky blue clusters) in A. tumefaciens C58, B. cereus ATCC 14579, and S. lividans TK24, cultures were divided into four equal volumes, supplemented with D-glucose, trans-4-hydroxy-L-proline, trans-3-hydroxy-L-proline, or L-proline to a final concentration of 20 mM, and grown until OD600 0.8–1.0. At the time of cell harvest, one volume of RNAprotect Bacteria Reagent (Qiagen) was added to two volumes of each culture. Samples were mixed by vortexing for 10 s and then incubated for 5 min at room temperature. Cells were pelleted by centrifugation (4750×g for 5 min at 4°C), the supernatant was decanted, and cell pellets were stored at -80°C until further use.

## RNA isolation

RNA isolation was performed in an RNAse-free environment at room temperature using the RNeasy Mini Kit (Qiagen) per the manufacturer's instructions. For B. cereus ATCC 14579 and S. lividans TK24, cells were initially disrupted using a modified bead-beating procedure: cells were resuspended in 400 µl Soil Pro Lysis Buffer (MP Bio), transferred to Lysis Matrix E tubes (MP Bio), and agitated horizontally on a Vortex Mixer (Fisher) with Vortex Adapter (Ambion) for 10 min at speed 10. Beads and cellular debris were pelleted by centrifugation at 16,000 × g for 5 min. 200 µl of the supernatant was used for subsequent RNA isolation. Cell pellets for all other organisms were disrupted according to the ‘Enzymatic Lysis Protocol’ in the RNAprotect Bacteria Reagent Handbook (Qiagen); lysozyme (Thermo-Pierce) was used at 15 mg ml-1. RNA concentrations were determined by absorption at 260 nm using the Nanodrop 2000 (Thermo) and absorption ratios A260/A280 and A260/A230 were used to assess sample integrity and purity. Isolated RNA was stored at -80°C until further use.

## Reverse transcription and quantitative real-time PCR

Reverse transcription (RT) PCRs for A. tumefaciens C58 and B. cereus ATCC 14579 were performed with 300 ng of total isolated RNA using the ProtoScript First Strand cDNA Synthesis Kit (NEB) as per the manufacturer's instructions. For S. lividans TK24 RT-PCRs were performed with 300 ng of total RNA using the Transcriptor First Strand cDNA Synthesis Kit (Roche), with 2.5% DMSO added to relieve secondary structures. All other RT-PCRs were performed with 1 µg of total RNA using the RevertAid H Minus First Strand cDNA Synthesis Kit (Fermentas).

Primers for quantitative real-time (qRT) PCR for A. tumefaciens C58 and B. cereus ATCC 14579 gene targets were designed using the Primer3 primer tool; amplicons were 150–200 bps in length; primers for all other qRT-PCRS were designed using the Universal ProbeLibrary System (Roche); amplicons were 66–110 bps in length Primer sequences are provided in Tables 10 and 11. Primers were 18–27 nucleotides in length and had a theoretical Tm of 55–60°C. Primer efficiency was determined to be at least 90% for each primer pair.10.7554/eLife.03275.022Table 10.qRT-PCR primers for transcriptional analysis of individual proline racemase superfamily membersDOI: http://dx.doi.org/10.7554/eLife.03275.022OligoSequence (5'–3')Atu16s-FGACACGGCCCAAACTCCTACAtu16s-RGGGCTTCTTCTCCGACTACCAtu0398-FTCACCATTGAGAAGGCCAATAtu0398-RGGTTGACGAGGTCCTTCAGAAtu3953-FCAGCTTCAGTGGCATCAGGAtu3953-RGTGTTGTGCCCAATGATCCAtu4684-FGAAGAGGCGCATGAGATTGAtu4684-RCGAAACCCAAAGCCTTGTTBc16s-FCTCGTGTCGTGAGATGTTGGBc16s-RTGTGTAGCCCAGGTCATAAGGBc0905-FCTTCGCTGACGGACAAGTAGABc0905-RTGTACCGCTGTTACGGACAABc2835-FAACAGACCCGTGTCATCCTGBc2835-RACTAAGCCAGCCGGTGTATCTLa16s-FTGGTGGGGTAAAGGCCTACLa16s-RTGGCTGATCATCCTCTCAGACLa28492-FTGTTGAAGACGAGGCCAAGLa28492-RAAAAGCCGAGCTGTTCGTTLa28502-FCGCGTAATCGACAGCCATALa28502-RGGCACAGAAATCGAGATGCTRs16s-FACACTGGGACTGAGACACGGRs16s-RTACACTCGGAATTCCACTCARs3519-FAGGACATCGCCTTCGAACTRs3519-RCGATGATGCCGAAATAGTTGPa16s-FTCACACTGGAACTGAGACACGPa16s-RATCAGGCTTTCGCCCATTPa1255-FCCACCCTCTGGGAACAGTCPa1255-RTCGTTGAGGACGAAGTTGCPa1268-FAACAGTGGCTACCTCGGCAPa1268-RTCGCCGACCGGTGTCTCGATRn16s-FATCTGTGTGGGCGCGATTRn16s-RGTGAGCGCATTGGTGGTCTRn08250-FTATGGCGGCGACAGTTTCRn08250-RGACGGCTCGAGCGTAAACPd16s-FGACTGAGACACGGCCCAGAPd16s-RTCACCTCTACACTCGGAATPd1045-FTCGGACTACTATGTGCCGATGPd1045-RCCTGATCGAGGCCAAAGACPd1184-FGCAATTTCGTGTTGAACGAGPd1184-RCATGATGATCCAGCCCATCTPd3467-FCTTCGCAGCCCTGTTCATPd3467-RGACCAGCCCTTCCTCGATPd4859-FGGCAAGGTGGACATCGAATAPd4859-RCCTCGGGGTAAAGGAAGCSm16s-FCGTGGGGAGCAAACAGGATTSm16s-RCTAAGGGCGAGGGTTGCGCTCSm20268-FCTGGCAAGGTGGACATCACSm20268-RGTAAGGCGCACTTCCTCAASm20270-FCGCCATGTCAATCTCCTGGTSm20270-RGGCAGCATCCACGATCACGA10.7554/eLife.03275.023Table 11.qRT-PCR primers for transcriptional analysis of genome neighborhoodsDOI: http://dx.doi.org/10.7554/eLife.03275.023PrimerSequence (5'–3')Sliv-Sco16srRNA-FCCGTACAATGAGCTGCGATASliv-Sco16srRNA-RGAACTGAGACCGGCTTTTTGSliv-Sco6289-FGACCCTGAAGGTCGTCGTCSliv-Sco6289-RGGTGACCGTGACGTCCATSliv-Sco6290-FGTCTTCTGCGGCATCGGSliv-Sco6290-RAGTCATCGTCGTCCTCCASliv-Sco6291-FGCCGACCTCGACGAAGASliv-Sco6291-RTTGTCGGTTTCACTGCTGTCSliv-Sco6292-FCATCGACACCAAGGTGGACSliv-Sco6292-RTGACCCCGACGATGTACCSliv-Sco6293-FGACTACGGCGTGCTCTTCATSliv-Sco6293-RCTCGGTGACCTCGACCATBc0905-FCTTCGCTGACGGACAAGTAGABc0905-RTGTACCGCTGTTACGGACAABc0906-FACTACGAACGCAACCACACCBc0906-RCGGAACTTGAAGGTCTCCTGTBc2832-FTACCAGGCTTTGGTCCTGAABc2832-RATTTGCCGCCAAGCTCTAACBc2833-FGGATGGGTTTCAGTAGCAGGABc2833-RCCTAGTCTTGGATAGCGAGAAGGBc2834-FAGGTGCGTATTCGCCAGAAABc2834-RCCTGGCGAACGTACGATAAABc2835-FAACAGACCCGTGTCATCCTGBc2835-RACTAAGCCAGCCGGTGTATCTBc2836-FCCTTGCATTCTCGCTTCTGTBc2836-RAATCTTAGGAGCCCACACACCAtu3947-FTCCGGCCAAGTATGTGAAAGAtu3947-RCTATAGCCGTTCGCAGCAAGAtu3948-FATTTCGCCCGTGATCTGTCAtu3948-RCGGCATCCACAATAATCCAGAtu3949-FGCGAACAGGCTGAAGAGATGAtu3949-RCGGCGGTAATTCCTGTTTGAtu3950-FGCTGCCGAACATATCAAGGTAtu3950-RGACCTTCGCGGTTATCTGGTAtu3951-FTGACGGACTCCAGCCTTATCAtu3951-RATGTAACATCGGCGTGGTCTAtu3952-FGATATCGTCAAGGGCGGTTTAtu3952-RACGCAGAGCCTTCATGTGTTAtu3953-FCAACGTCGCCAGTTACCTTCAtu3953-RGGCTGAGATCAACGACATCCAtu3958-FGGCGGCTGATACACATCTTCAtu3958-RAAAGTTGGTGCTTCGTCAGGAtu3959-FCATTCCTGACACGATCCACAAtu3959-RCAGCATCAGCAAAGGGAAGTAtu3960-FGAATGTCGTCGCCATCAAGAtu3960-RTCGTAGAGTGCCACATGCTCAtu3961-FTTCGGCACTTCTTTCTGGTCAtu3961-RGCTCGCCTGCAGATAAACAAtu4675-FTTCCTGTTATCGTCGGCACTAtu4675-RGCCTTGAAGTGAGCCTTCTGAtu4676-FACGGCTATCGTGAAGGTCAAAtu4676-RGAATAGCTCGGGCACATCACAtu4682-FTCCTCAGAAAGACCGACACCAtu4682-RGTGAATGTGCCGCAGGTAAAtu4684-FCCTCGGCAAACTCAAGGTCAtu4684-RGCGAAGAGGCAGAAGGAAAAtu4691-FAAGGGCGATATGGGTCTTTCAtu4691-RGAGCTCTTCGATGCTGTCGT

qRT-PCRs were carried out in 96-well plates using the Roche LightCycler 480 II instrument with the LightCycler 480 SYBR Green I Master Mix (Roche) per the manufacturer's instructions. Each 10-µl reaction contained 1 µM of each primer, 5 µl of SYBR Green I Master Mix, and an appropriate dilution of cDNA. Reactions were run as follows: one cycle at 95°C for 5 min, 45 cycles at 95°C for 10 s, 50°C for 10 s, 72°C for 10 s, and a final dissociation program at 95°C for 15 s, 60°C for 1 min, and 95°C for 15 s. Minus-RT controls were performed to verify the absence of genomic DNA in each RNA sample for each gene target analyzed. Gene expression data were expressed as crossing threshold (CT) values. Data were analyzed by the 2-??CT (Livak) method (Livak and Schmittgen, 2001), using the 16S rRNA gene as a reference. Each qRT-PCR was performed in triplicate, and fold-changes are the averages of at least three biological replicates.

## Data deposition

The atomic coordinates and structure factors for ‘4R-hydroxyproline 2-epimerases’ (4HypE) from Pseudomonas putida F1 (citrate-liganded, PDBID:4JBD; sulfate-liganded, PDBID:4JD7), Chromohalobacter salexigens DSM 3043 (apo, PDBID:4JCI), Xanthomonas campestris (phosphate-liganded, PDBID:4JUU), Burkholderia multivorans (phosphate-liganded, PDBID:4K7X), Pseudomonas fluorescens Pf-5 (pyrrole 2-carboxylate-liganded, PDBID:4J9W; trans-4-hydroxy-L-proline-liganded, PDBID:4J9X), Ochrobacterrium anthropic (apo, PDBID:4K8L), and Agrobacterium vitis S4 (trans-4-hydroxy-L-proline-liganded, PDBID:4LB0) and ‘trans-3-hydroxy-L-proline dehydratase’ (t3HypD) from Agrobacterium vitis S4 (pyrrole 2-carboxylate-liganded, PDBID:4K7G) have been deposited in the Protein Data Bank, www.pdb.org.

## UniProt accession IDS

This manuscript describes functional characterization of proteins with the following UniProt accession IDs: A0NXQ7, A0NXQ9, A1B0W2, A1B195, A1B196, A1B7P4, A1BBM5, A1U2K1, A3M4A9, A3PPJ8, A3QFI1, A3QH73, A3S939, A3SU01, A5VZY6, A6WW16, A6WXX7, A8H392, A9AKG8, A9AKH1, A9AL52, A9ALD3, A9AQW9, A9CFU8, A9CFU9, A9CFV0, A9CFV4, A9CFW8, A9CGZ4, A9CGZ5, A9CGZ9, A9CH01, A9CH04, A9CKB4, B0VB44, B1KJ76, B3D6W2, B4EHE6, B9J8G8, B9JHU6, B9JQV3, B9K4G4, B9R4E3, C5ZMD2, D2AV87, D2QN44, D5SQS4, D6EJK6, D6EJK7, D6EJK8, D6EJK9, D6EJL0, Q0B950, Q0B953, Q0B9R9, Q0B9S2, Q16D96, Q1QBF3, Q1QU06, Q1QV19, Q2KD13, Q2T3J4, Q2T596, Q3IWG2, Q3IZJ8, Q3JFG0, Q3JHA9, Q485R8, Q4KAT3, Q4KGT8, Q4KGU2, Q5LKW3, Q5LLV0, Q63FA5, Q6HMS8, Q6HMS9, Q73CR9, Q73CS0, Q7CFV0, Q7CTP1, Q7CTP2, Q7CTP3, Q7CTP4, Q7CTQ2, Q7CTQ3, Q7CTQ5, Q7CVK1, Q7NU77, Q81CD6, Q81CD7, Q81CD8, Q81CD9, Q81CE0, Q81HB0, Q81HB1, Q8FYS0, Q8P833, Q8YFD6, Q92WR9, Q92WS1, Q9I476, Q9I489, and Q9I492.

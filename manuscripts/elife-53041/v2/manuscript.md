# Cre-assisted fine-mapping of neural circuits using orthogonal split inteins

## Authors

- Haojiang Luan<sup>1</sup>
- Alexander Kuzin<sup>2</sup>
- Ward F Odenwald<sup>2</sup>
- Benjamin H White<sup>1</sup> ([ORCID: 0000-0003-0612-8075](https://orcid.org/0000-0003-0612-8075)) †

### Affiliations

1. Laboratory of Molecular Biology, National Institute of Mental Health, NIH Bethesda United States
2. Neural Cell-Fate Determinants Section, National Institute of Neurological Disorders and Stroke, NIH Bethesda United States

† Corresponding author

## Abstract

Existing genetic methods of neuronal targeting do not routinely achieve the resolution required for mapping brain circuits. New approaches are thus necessary. Here, we introduce a method for refined neuronal targeting that can be applied iteratively. Restriction achieved at the first step can be further refined in a second step, if necessary. The method relies on first isolating neurons within a targeted group (i.e. Gal4 pattern) according to their developmental lineages, and then intersectionally limiting the number of lineages by selecting only those in which two distinct neuroblast enhancers are active. The neuroblast enhancers drive expression of split Cre recombinase fragments. These are fused to non-interacting pairs of split inteins, which ensure reconstitution of active Cre when all fragments are expressed in the same neuroblast. Active Cre renders all neuroblast-derived cells in a lineage permissive for Gal4 activity. We demonstrate how this system can facilitate neural circuit-mapping in Drosophila.

## Introduction

An essential step in mapping brain circuits is identifying the function of the individual neurons that comprise them. This is commonly achieved by manipulating neuronal function using effectors encoded by transgenes whose expression is targeted to small subsets of cells using the regulatory elements of neurally-expressed genes (Gohl et al., 2017; Luo et al., 2018). While it has proved relatively easy to target large groups of neurons for cellular manipulation by this means in genetic model organisms using binary expression systems, such as the Cre-lox system of mice or the Gal4-UAS system of fruit flies, highly-specific targeting of neurons requires combinatorial methods. Genetic combinatorial methods typically use either the regulatory elements of two neurally-expressed genes or exploit stochastic events to limit transgene targeting to a subpopulation of a larger group of neurons. In fruit flies, both types of method have been used to target single cells under optimal conditions (Aso et al., 2014; Gao et al., 2008; Gordon and Scott, 2009; Kohatsu et al., 2011; Lee and Luo, 1999; Luan et al., 2012; Pool et al., 2014; Sen et al., 2019; Shang et al., 2008; Yu et al., 2010), and combinatorial approaches using three regulatory elements have achieved some success (Dolan et al., 2017; Pankova and Borst, 2017; Shirangi et al., 2016; Sullivan et al., 2019). However, general limitations apply to all such approaches: stochastic methods are, by nature, poorly reproducible, while combinatorial methods are labor-intensive, often requiring the characterization of many neurally active enhancer elements (Dionne et al., 2018; Tirian et al., 2017). Simpler methods of targeting small populations of brain cells are therefore desirable in the effort to comprehensively map neural function.

An attractive approach to increase the specificity of neuronal targeting is to identify neurons based not only on the genes they express in the terminally differentiated state (i.e. terminal effector genes, TEG), but also on their developmental history (Awasaki et al., 2014; Dymecki et al., 2010; Huang, 2014). Most neuronal lineages produce diverse neuron types, and while some striking correspondences have been found (Lacin et al., 2019), lineage identity, in general, correlates poorly with neuronal identity as defined by gene expression (Hobert et al., 2016; Zeng and Sanes, 2017). Conversely, gene expression is often correlated across neurons that differ in identity as defined by their function, morphology, and neuroanatomical location (Hobert, 2016; Hobert and Kratsios, 2019). This is because neuronal identities are defined not by single genes, but by the expression of often overlapping batteries of TEGs. An intersection of lineage with the expression of a specific TEG may thus, in general, include fewer neurons than an intersection of the expression patterns of two TEGs. In addition, because neurons from a given lineage typically remain regionally localized, intersections made using lineage information will tend to restrict neuronal targeting anatomically.

Recombinase-based intersectional methods that combine information about lineage and cell type have been developed in both mice and fruit flies and have been shown to substantially restrict targeting to cell groups of interest (Brust et al., 2014; Ren et al., 2016). However, the use of such methods has remained largely limited to specific cases—in mice, sublineages of brainstem serotonergic neurons (Okaty et al., 2015), and in flies, subtypes of Type II transit-amplifying neural stem cells (i.e. neuroblasts, NBs) of the central brain (Ren et al., 2018; Ren et al., 2017). This is because of the paucity of lineage-restricted enhancers. Just as there are few TEG enhancers that are active in small numbers of mature neurons, there are also few identified enhancers that exhibit lineage-specific activity. In the fly, a systematic analysis of some 5000 neural enhancer domains identified 761 with activity in embryonic NBs, but 99 of these expressed in most or all lineages (Manning et al., 2012). A separate analysis indicates that the remainder are at best active in 5–20 lineages (Awasaki et al., 2014). The routine use of lineage-cell type intersections for neural circuit mapping will thus require more refined methods of isolating neuronal lineages or sub-lineages.

To achieve such lineage refinement, we introduce here a combinatorial method analogous to the Split Gal4 technique used to restrict neuronal targeting to the intersection of two TEG expression patterns (Luan et al., 2006). We restrict reconstitution of a Split Cre recombinase to the expression patterns of two independent NB-active enhancers (i.e. NBEs). Only NBs in which both enhancers are active thus make full-length Cre. Cre is then used to selectively promote activity of the Gal4 transcription factor—expressed under the control of a TEG enhancer—in the mature progeny of these NBs, thus implementing a second intersection. Our method (i.e. ‘Split Cre-assisted Restriction of Cell Class-Lineage Intersections,’ or SpaRCLIn) generalizes the capabilities of the CLIn technique introduced by Ren et al. (2016) by expanding the range of possible intersections to most Drosophila lineages while maintaining compatibility with all existing Drosophila Gal4 driver lines. To facilitate SpaRCLIn’s use, we have generated a variety of tools, including two libraries of transgenic fly lines, each of which expresses distinct Split Cre components under the control of 134 different NBEs. We characterize the efficacy of these SpaRCLIn reagents and provide examples of their use in restricted neuronal targeting and circuit-mapping.

## Results

### Development of bipartite and tripartite split cre recombinases

SpaRCLIn was developed to refine the expression pattern of a Gal4 driver using the basic strategy shown in Figure 1. In common with other existing methodologies, SpaRCLIn uses a recombinase (i.e. Cre) to excise an otherwise ubiquitously expressed construct encoding Gal80, a suppressor of the Gal4 transcription factor (Figure 1A–B). As in the CLIn technique, recombinase expression—and thus the excision of Gal80—occurs only in targeted NBs, rendering the progeny of these NBs permissive to Gal4 activity (Figure 1C). Those progeny that lie within the expression pattern of the Gal4 driver will be competent to drive UAS-reporters and effectors, such as UAS-GFP. In the SpaRCLIn technique, distinct NBEs are used to express components of a bipartite Split Cre molecule in restricted subsets of NBs. In lineages of these NBs that contain mature neurons within the Gal4 expression pattern, Gal4 will be active. This population of neurons can be additionally parsed using a tripartite Split Cre to further restrict the subset of NBs that make active Cre (Figure 1D).

![Figure 1.](https://cdn.elifesciences.org/articles/53041/elife-53041-fig1-v2.jpg)

**Figure 1.:** (A–D) Components and genetic logic of the SpaRCLIn system. (A) A Gal4 driver that drives expression of UAS-transgenes, such as UAS-GFP, in a specific pattern of cells within the CNS (green filled circle). (B) Conditional expression of Gal80, a repressor of Gal4 activity, in all cells using an Actin5C promoter, subject to excision by Cre (gray shading indicates repression of Gal4 by Gal80). (C) Selective activation of Cre in specific NBs (red dotted circle) to excise Gal80 and permit expression of the marker tdTomato (red stripes) and activity of Gal4 (solid green) in neurons derived from those NBs. (D) Use of split Cre components to target NBs at the intersection of two NB expression patterns (red and blued dotted circles) to permit Gal4 activity selectively within cells derived from these NBs (solid green). Note that Gal80 excision results in persistent expression of tdTomato in the affected neurons, but that expression of UAS-reporters and effectors is determined by the temporal properties of the Gal4 line used to drive it. (E) Primary sequence of the Cre protein using the single letter amino acid code. Residues that participate in DNA-binding (blue) or catalysis (yellow highlight) are indicated as are the break-points (green highlight) chosen to generate the split Cre fragments for fusion to split inteins: CreA, CreB, CreAB, and CreC as indicated (magenta boxes). (F–G) The bipartite SpaRCLIn system. (F) Schematics of the Cre fragments fused to NrdJ-1 split inteins, indicating their ability to reconstitute full-length Cre, (G) CreAB expression is directed to all NBs (white plus red shading) using the NB-specific DNE enhancer (see text), and CreC expression is directed to a subset of NBs (red) by the NBE enhancer, which will also express in other cell types (gray). Only the NBs targeted by NBE will express both CreAB and CreC and reconstitute full-length Cre. (H–I) The tripartite SpaRCLIn system. (H) Similar to (F) except that the CreAB fragment has been further divided into CreA and CreB components which have been fused to gp41-1 split inteins at breakpoints. All three fragments are now required to reconstitute full-length Cre. (I) Venn diagram similar to (G) indicating the intersection of the three enhancers used to drive CreA (DNE), CreB (NBE2), and CreC (NBE1). (J) Schematic of the floxed Gal80 construct used in the SpaRCLIn system, the expression of which is driven by the ubiquitously active Actin5C promoter. Cre-mediated excision of Gal80 via the flanking loxP sites causes a myristoylated tdTomato (tdTom) red fluorescent protein to be expressed instead of Gal80. (K–M) Restriction of NB expression by SpaRCLIn. (K, L) tdTom expression (red) driven by the bipartite SpaRCLIn system using two different NBEs (44F03 and 43H02) to drive CreC expression. (M) tdTom expression driven by the tripartite SpaRCLIn system at the intersection of the two NBE expression patterns, which overlap in several NB pairs of the ventral nerve cord (VNC) and brain (Br). Neuropil labeling by the nc82 antibody is shown in blue. Scale bar: 50 μM. Note that the genotypes of the flies for panels of this and all subsequent figures are provided in Supplementary file 2.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/53041/elife-53041-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A–I) Nine representative examples of CNS expression of the 134 neuroblast-active enhancers (NBEs) used in this study. Shown are volume-rendered confocal micrographs of larval CNS whole mounts taken from animals expressing tdTomato in NB lineages in which the indicated enhancers are active. The expression patterns were generated using the bipartite SpaRCLIn system described in Figure 1 to drive the tdTomato reporter in the labeled neuroblast lineages. Some of the NBEs show limited expression, as in (A), where only a single major neuroblast lineage with multiple, clustered progeny is labeled (arrow). Most, however, express in multiple NBs broadly distributed throughout the brain (Br) and ventral nerve cord (VNC), as in (E), where the arrows indicate some of the larger NB clones with many labeled progeny. The number of progeny in NB clones could be as small as one to two cells as in (B; arrows), indicating that NBEs could be active in some NBs only at later stages of neurogenesis where they would thus label sublineages. Scale bar: 50 μM.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/53041/elife-53041-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Sequence of the chimeric neuroblast enhancer used in this study, which is composed of an enhancer for the gene encoding the transcriptional repressor, deadpan (blue) fused via a 10 bp linker (red) to an enhancer for the gene encoding nerfin-1 (black). Upper case letters signify the highly conserved sequences used to identify the enhancers using the Evoprinter. Underlined are conserved sequence blocks shared by the two enhancers that represent putative transcription factor binding sites. Yellow highlight indicates two nucleotide substitutions that expand the range of the nerfin-1 enhancer expression in NBs. For further details see Materials and Methods. (B) Cis-regulatory activity of the DNE. The DNE was used to drive Gal4 expression, which was monitored during embryonic development by mRNA in situ hybridization. Shown are filleted wholemount embryos, stages 8–13 (anterior up). Most, if not all, CNS NBs are labeled during early to late stages of lineage development. By early embryonic stage 15, only a small subset of late neuroblasts have detectable signal and most, if not all, neurons and glia of the ventral cord and cephalic lobes have no detectable expression (data not shown). Scale bar: 50 μM. (C) DNE-mediated expression of CreAB and CreC fragments leads to reconstitution of Cre activity, excision of Gal80, and activation of tdTomato expression (magenta) in the embryonic CNS beginning at stage 8. Dorsal view, s8; lateral view, s9-13. (D) DNE-dependent Cre reconstitution and tdTomato expression in the NB 3–5 lineage of VNC hemisegments in a late-stage embryo. The previously described NB 3–5-specific Gal4 line, R59E09-Gal4 (Lacin and Truman, 2016), was used to drive expression of UAS-CreC in flies bearing the DNE-CreB, DNE-CreA and CreStop (i.e. actin^STOP^tdTomato) constructs. Excision of Gal80 specifically in NB 3–5 leads to tdTomato expression (red). Blue: 22C10 (anti- futsch) immunostaining. An enlarged image of the outlined region (left) is shown on the right. Scale bar: 50 μM.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/53041/elife-53041-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A–B) tdTomato expression patterns generated in 3rd instar larval CNS preparations by the R12E08 NBE driving: (A) CreB (insertion on chromosome II) or (B) CreC (insertion on Chromosome III). The expression patterns of five representative preparations are shown for each construct. In general, they appear similar for all preparations, which was the case for all but 24 of the 134 NBEs used to generate the NBE-CreB and NBE-CreC libraries. (Note that the DNE was used to drive CreA and CreC expression in (A) and CreAB expression in (B)). (C–D) tdTomato expression patterns generated as in (A–B) but using the R19C09 NBE to drive: (C) CreB (insertion on chromosome II) or (D) CreC (insertion on Chromosome III). R19C09 was one of the 24 NBEs that gave differing expression for the NBE-CreB and CreC constructs, with VNC lineages labeled when CreC, but not CreB, was used. Scale bars: 50 μM.

Although most recombinase-based expression systems in Drosophila, such as MARCM (Lee and Luo, 1999), Flp-out Gal80 (Gordon and Scott, 2009), and FINGR (Bohm et al., 2010) have preferentially used the Flp recombinase for Gal80 excision, we selected Cre for use in SpaRCLIn because of its demonstrated ability to retain high activity in a variety of bipartite forms (Hirrlinger et al., 2009; Jullien, 2003; Kawano et al., 2016; Kennedy et al., 2010; Rajaee and Ow, 2017). Although Cre activity has been reported to be toxic in Drosophila when chronically expressed at high levels (Heidmann and Lehner, 2001; Nern et al., 2011), it has previously been used in NBs without apparent adverse effects (Awasaki et al., 2014; Hampel et al., 2011; Ren et al., 2016). Because our system requires use of a tripartite Cre to achieve the most refined targeting it was also desirable to use a method of splitting Cre that would permit reconstitution of the intact molecule to obtain the highest activity levels. Split inteins, which are capable of autocatalytically joining two proteins to which they are fused, are well-suited to this purpose and distinct split inteins have been previously shown to support reconstitution of recombinase activity from complementary Cre fragments fused to them (Ge et al., 2016; Han et al., 2013; Hermann et al., 2014; Wang et al., 2012). Figure 1E shows the primary structure of Cre, indicating the location of the breakpoints (green highlight) at which we introduced split intein moieties into the molecule. These breakpoints separate the amino acid residues in the primary structure that form the DNA-binding sites (blue) and the active site (yellow highlight), thus insuring that none of the fragments retains catalytic activity. Two Split Cre fragments, CreAB and CreC, were generated by the breakpoint between amino acids P250 and S251 to implement the bipartite Split Cre system (Figure 1F,G), while dividing the CreAB fragment at the breakpoint between amino acids D109 and S110 was used to create two further fragments (i.e. CreA and CreB) which together with CreC form the basis of the tripartite Split Cre system (Figure 1H,I). The split intein pairs used to generate these fragments, gp41-1 and NrdJ-1, were chosen based on their trans-splicing efficiency and their lack of cross-reactivity (Carvajal-Vallejos et al., 2012). The latter criterion was critical for avoiding the generation of unproductive fusion products of the Cre fragments.

After confirming the ability of the bi- and tripartite constructs to reconstitute Cre activity when co-expressed in transfected S2 cells (data not shown), we used them to generate transgenic fly lines in which they were expressed in patterns dictated by individual enhancers that exhibited activity in neuroblasts. Most of the NBEs selected for this purpose were taken from the large collection of enhancer fragments with fully defined sequences created by the Rubin lab (Pfeiffer et al., 2008 #43). Most of the NBEs selected were from a previously characterized collection of embryonically active NB enhancers (Manning et al., 2012), with the remainder characterized as indicated in the Materials and Methods and Supplementary file 1. A total of 134 NBEs were used to make two libraries of transgenic fly lines, one expressing the CreB fragment under the control of each of the 134 NBEs and the other similarly expressing the CreC fragment. These lines thus collectively express CreB and CreC in a large number of distinct and often overlapping subsets of NBs (Figure 1—figure supplement 1). However, because the 134 enhancers are also typically active in mature neurons, the production of full-length Cre is not necessarily restricted to NBs (Jenett et al., 2012).

To ensure NB-specific reconstitution of Cre activity, we placed the CreA and CreAB fragments under the control of a compound enhancer formed by fusing individual enhancer elements of the NB-specific genes, deadpan (dpn) and nervous fingers-1 (nerfin-1; see Materials and methods). This synthetic dpn-nerfin-1 enhancer (i.e. DNE) combines the complementary temporal characteristics of both component enhancers, maintaining strong, broad, and specific activity throughout embryonic neurogenesis (Figure 1—figure supplement 2A,B). Use of the DNE thus ensured that full-length, active Cre would be generated only in NBs where expression of the Cre fragments overlapped, and not in fully-differentiated neurons (Figure 1G,I). This enhancer also expresses in most of the NBs that give rise to the Drosophila CNS with the exception of those found in the late-developing optic lobes, and thus guarantees substantial coverage of the mature neurons found within the expression patterns of Gal4 lines.

To detect activity of the Split Cre constructs in vivo, we created transgenic flies carrying a reporter construct in which the floxed Gal80 gene, the expression of which is driven by a ubiquitously active Actin 5C promoter, is followed by the gene encoding the red fluorescent protein, tdTomato (Figure 1J). Expression of tdTomato from this construct, which we call Cre80Tom, thus identifies neurons in which Gal80 has been excised. Gal80 excision, identified by the appearance of tdTomato expression, is identifiable as early as embryonic stage eight when the CreAB and CreC fragments are driven by the DNE and it is widespread in the developing CNS by stage 13 (Figure 1—figure supplement 2C). The onset of Cre activity is sufficiently early to label many of the progeny of a defined NB lineage targetable by the R59E09-Gal4 line, previously identified by Lacin and Truman (2016) (Figure 1—figure supplement 2D). These data suggest that Gal80 excision occurs relatively early.

The bipartite system, using the DNE-CreAB and CreC fragments expressed under the control of two different neuroblast enhancers (NBE43H02 and NBE44F03), also generated expression patterns in neuronal lineages of third instar larvae (Figure 1K and L). The expression patterns include not only the NBs in which Cre activity is reconstituted, but also the progeny of these NBs, since tdTomato expression is activated in all cells born within these lineages after Gal80 is excised. Although the expression patterns differ in the two cases, they share a small number of common NB lineages as is revealed by application of the tripartite Cre system using the NBE44F03 and NBE43H02 enhancers to drive CreB and CreC, respectively, together with DNE-CreA (Figure 1M). Expression in this case is limited to approximately three bilateral lineages in the ventral nerve cord (VNC) and two in the brain. These examples illustrate how the bi- and tripartite Split Cre constructs selectively reconstitute Cre activity in NBs targeted by individual NBEs, and demonstrate that the tripartite Split Cre system can be used to restrict Cre activity to only those NBs in which two distinct NBEs are active.

As this example illustrates, the tripartite system generates intersections of two NBE-CreC expression patterns by substituting one CreC fragment with a CreB fragment driven by the identical NBE. To facilitate such substitutions, all NBE-CreC insertions were made on Chromosome III and all NBE-CreB insertions were made on Chromosome II. To evaluate the reproducibility of expression driven by individual NBEs, we examined NBE-CreC∩DNE-CreAB >CreTom crosses for all 134 NBEs in multiple preparations (on average four per NBE) and compared these patterns with expression observed in all NBE-CreB∩DNE-CreA∩ DNE-CreC >CreTom crosses. The large size of the patterns and the inability to reliably identify identical neurons and lineages across preparations prevented a systematic analysis, but in general the patterns were similar across preparations for any given cross (Figure 1—figure supplement 3) In most cases, patterns obtained with a given NBE-CreB line also resembled the pattern obtained with the NBE-CreC line made with the same enhancer (compare panels A and B in Figure 1—figure supplement 3). However, for 24 NBEs overt differences were observed (Figure 1—figure supplement 3C vs 3D). Apart from these NBEs, which have been marked with an asterisk in Supplementary file 1 along with guidance as to their use, the tripartite system represents a reliable intersectional method for restricting Cre activity to subsets of NBs. The progeny of these NBs that are generated after Cre activation will not only express the reporter tdTomato, but will also fail to express the Gal80 transgene, thus permitting Gal4 to function.

### Using the bipartite and tripartite cre systems to restrict expression of TH-Gal4

The selective disinhibition of Gal4 activity in targeted lineages permits UAS-transgenes to be expressed in cells of those lineages whenever they lie within the expression pattern of a Gal4 driver. This allows targeted lineages to be parsed according to the properties of the mature neurons to which they give rise using cell-type specific Gal4 drivers. Such so-called ‘cell class-lineage intersections’ have been previously performed to identify subsets of neurons generated by Type II NBs of the Drosophila brain, which can be selectively targeted using a Type II-specific enhancer (Ren et al., 2016; Ren et al., 2018; Ren et al., 2017). Among the neurons generated by Type II NBs are several populations of dopaminergic neurons, identified by a Tyrosine Hydroxylase-specific Gal4 driver (TH-Gal4). Dopaminergic neurons are of considerable interest because of their roles in a variety of important neurobiological processes, including learning, sleep, and locomotion (for review see Kasture et al., 2018). The approximately 120–130 dopaminergic neurons in the Drosophila CNS are produced by diverse NBs and numerous reagents have been generated to selectively target them (Aso et al., 2014; Friggi-Grelin et al., 2003; Xie et al., 2018).

As a first test of the SpaRCLIn system, we therefore asked whether it could restrict expression of the TH-Gal4 driver (Figure 2A) to small numbers of distinct dopaminergic neurons based on their different lineages of origin. Using a small subset of the NBE-CreC lines in combination with DNE-CreAB, we examined the expression patterns produced by intersection with TH-Gal4. The expression patterns produced by these intersections were noticeably reduced compared with the full pattern of the TH-Gal4 driver, but they typically still contained 10’s of dopaminergic neurons distributed broadly across the neuraxis (Figure 2B–C). In cases where the expression patterns produced by the bipartite crosses shared a neuron (Figure 2B–C, arrows), combining the relevant NBEs using the tripartite system succeeded in isolating these neurons from most others in the two original crosses (Figure 2D). In general, restricting NB expression using the tripartite system—by pairing the NBE-CreC constructs with NBE-CreB constructs made with different enhancers—produced significantly reduced expression patterns, sometimes consisting of one to two cells or bilateral cell pairs (Figure 2D–H).

![Figure 2.](https://cdn.elifesciences.org/articles/53041/elife-53041-fig2-v2.jpg)

**Figure 2.:** (A) Expression pattern of the TH-Gal4 driver revealed by UAS-mCD8GFP (green). In all panels: Anti-nc82 labeled neuropil (magenta); ventral nerve cord; VNC; brain; Br. (B–D) Restriction of TH-Gal4 expression using SpaRCLIn. (B, C) mCD8GFP expression (green) in mature dopaminergic neurons isolated using the bipartite SpaRCLIn system and two different NBEs (R44F03 and R52B02) to drive CreC expression. A neuronal pair common to both patterns is indicated (yellow arrows). (D) mCD8GFP expression (green) driven by the tripartite SpaRCLIn system at the intersection of the two NBE expression patterns in B and C. (E–H) Examples of TH-Gal4 restriction to small numbers of neurons using the tripartite system and the indicated pairs of NBEs. Scale bar: 50 μM. (I) Size and stereotypy of the restricted expression patterns produced by the indicated Step two intersections. The average number of neurons per preparation (± standard deviation) observed for each intersection is shown together with the number of preparations examined. For each, intersection the neuron that was most frequently observed across preparations (i.e. the ‘principal common neuron’) was identified and the percentage of preparations containing this neuron is shown in the bar graph (black bars) together with the percentage of preparations showing expression only in other neurons (gray bars) or no expression (white bars). Examples of principal common neurons are indicated by yellow arrows in D-H.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/53041/elife-53041-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A–G) Seven distinct restrictions of the TH-Gal4 expression pattern produced by the same pair of NBEs: R44F09-CreB∩R52B02-CreC. For five of the CNS preparations (A–E), labeling of one or more neurons was observed only in the brain (Br), while in two preparations labeling was observed in cells of both the ventral nerve cord (VNC) and brain (F), or in the VNC alone (G). The identity of all neurons isolated in these preparations appeared to be unique. Anti-nc82 labeled neuropil (magenta); UAS-mCD8GFP (green). Scale bar: 50 μM.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/53041/elife-53041-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Yellow labels (a-c) identify the somata of neurons identified to be the same in different preparations, based on position and morphology. The neuron labeled ‘a’ represents the primary expression pattern in that it occurs with the greatest frequency (8/16 preparations). Neurons ‘b’ and ‘c’ recur in 5 and 6 of the 16 preparations, respectively. In some cases, both neurons of these bilateral pairs are labeled, while in others only a single neuron is labeled. In all panels: Anti-nc82 labeled neuropil (magenta); UAS-mCD8GFP (green). Scale bar: 50 μM.

The expression patterns from 14 NBE-CreC∩NBE-CreB intersections—produced by combining 15 distinct NBEs—were analyzed in detail to quantify both the average number of dopaminergic neurons and the stereotypy of expression for each intersection (Figure 2I). We found that the average number of labeled neurons per preparation did not exceed 8.5 (±3.8, n = 16) for any intersection and was less than 4.3 (±2.3, n = 17) for two-thirds of them. This sparseness of expression suggests that the NBEs tested do not overlap extensively in their NB expression patterns. Stereotypy of expression was also generally present despite considerable variability. Only in one extreme case, did there appear to be a complete absence of stereotypy, with all CNS preparations that had expression displaying a distinct pattern (Figure 2—figure supplement 1). For all other intersections, at least one principal neuron was found that was shared by multiple preparations, based on cell position and morphology (Figure 2I, black bars). For over half of the intersections, this principal common neuron was shared by 50% or more of preparations. In most cases, other neurons were also found, though preparations containing only such neurons typically occurred at lower frequency (Figure 2I, gray bars). Consistent with this variability of expression, neurons that recurred across preparations were not necessarily found in the same combinations (Figure 2—figure supplement 2).

The sparseness of labeling combined with the variability of expression likely accounts for why half of the intersections yielded at least one preparation without any expression. Interestingly, four of the seven intersections that yielded preparations devoid of expression shared an enhancer (R14E10), suggesting that particular enhancers may strongly influence the extent of labeling. Variability of labeling also appeared to be enhancer-dependent in that use of the same enhancer (i.e. R17A10) to drive both CreB and CreC components did not necessarily reduce stochasticity. Indeed, although all preparations that had expression shared a common identifiable neuron in this case (Figure 2I), their expression in other neurons varied considerably. A possible source of this variability of expression is weak NBE activity that results in lowered expression of Cre components and consequently more sporadic reconstitution of Cre activity. More work will be required to examine this hypothesis. Regardless, our results demonstrate SpaRCLIn’s ability to substantially restrict expression of a Gal4 driver with sufficient stereotypy in single neurons to be useful for the neuronal manipulations employed in neural circuit mapping.

### Functional circuit-mapping using SpaRCLIn

To examine SpaRCLIn’s efficacy for circuit mapping, we used it to identify neural substrates of proboscis extension (PE), a motor pattern normally elicited by gustatory stimuli, but also by the hormone Bursicon in newly eclosed flies (Peabody et al., 2009). Robust PE can be readily induced even in older flies using a driver (rkpan-Gal4) that selectively expresses in Bursicon-responsive neurons (Video 1, Figure 3A,B; Diao and White, 2012). Expressing the heat-sensitive ion channel UAS-dTrpA1 under the control of this driver, we performed an initial (‘Step 1’) screen of the CreC library using the bipartite SpaRCLIn system (Figure 3—figure supplement 1A). In this screen, crosses were conducted between each NBE-CreC line and a line that combined all other components, including Cre80Tom, DNE-CreAB, rkpan-Gal4, and UAS-dTrpA1. To facilitate visualization of neurons within the resulting expression pattern without requiring additional genomic insertions, we used a dual expression construct (Cre80Tom- GFP) that contained actin^Gal80^myr-tdTomato and a 10XUAS-mCD8GFP reporter (Figure 3—figure supplement 2). Progeny were videorecorded in small chambers on a temperature-controlled plate and assayed for heat-induced PE. Interestingly, several different PE phenotypes were apparent, but only those that involved full extension of the proboscis could be reliably scored under our assay conditions and we therefore focused on the latter. Applying this criterion, we identified 23 NBE-CreC∩DNE-CreAB intersections for which UAS-dTrpA1 activation reliably induced robust PE in greater than 50% of the progeny. The expression patterns resulting from these CreAB∩C∩rkpan-Gal4 (i.e. Step 1) intersections, examined using a UAS-GFP reporter, were clearly restricted relative to rkpan-Gal4 expression (Figure 3C–D), but they were insufficiently sparse to readily identify the neurons—or population of neurons—responsible for inducing the PE motor pattern.

![Figure 3.](https://cdn.elifesciences.org/articles/53041/elife-53041-fig3-v2.jpg)

**Figure 3.:** (A) Induced PE (arrowhead) in a fly expressing the heat-sensitive ion channel dTrpA1 under the control of the rkpan-Gal4 driver. Labels as described in the legend of Figure 2A. (B) Expression pattern of the rkpan-Gal4 driver revealed by UAS-mCD8GFP (green). In all panels: Anti-nc82 labeled neuropil (magenta); ventral nerve cord: VNC; brain: Br. (C–D) mCD8GFP expression (green) in mature subsets of RK-expressing neurons isolated using the bipartite SpaRCLIn system and NBEs R44F09 and R516H11 to drive CreC expression. (E) PE induced in a fly expressing dTrpA1 in the PErk neurons, isolated using the tripartite system with the R44F09 and R16H11 NBEs to parse the rkpan-Gal4 pattern. (F–H) Typical expression patterns in rkpan-Gal4R44F09 ∩ R16H11 flies, showing expression in both bilateral pairs of PErk neurons (F), one neuron of each of the two bilateral pairs of PErk neurons (G), or no neurons (H). All scale bars: 50 μM.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/53041/elife-53041-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Crossing scheme for implementing a Step one screen using the bipartite SpaRCLIn system. The example given illustrates the strategy to be used when the Gal4 driver is on chromosome III, but reagents for use when the driver is on chromosome II are also provided (see Key Resources Table). An initial set of crosses brings the Gal4 driver together with two essential components of SpaRCLIn: an X chromosome containing the combined Actin 5C-loxP-Gal80-loxP-tdTomato and UAS-mCD8GFP constructs (abbreviated here as Cre80Tom-GFP) and a 2nd chromosome containing the DNE-CreAB. If a functional screen is being performed, an effector—such as UAS-dTrpA1—can also be recombined with the DNE-CreAB or Gal4 driver on an autosome, as illustrated here. Alternatively, we have made variants of the Cre80Tom-GFP (on X) that contain UAS-dTrpA1 (Cre80-dTrpA1) or Kir2.1 (Cre80-Kir2.1) that can be used instead of Cre80Tom-GFP. Flies bearing the Gal4 driver and essential SpaRCLIn components, are then crossed in a final step to flies of the CreC library to generate the desired progeny for testing. The NBEs of those CreC library lines that test positive (e.g. NBEn-CreC and NBEm-CreC) can then be used for intersectional analysis in a Step two tripartite screen. This is done by combining one of the NBE-CreC components, say NBEn-CreC, with the NBEm-CreB component, which is readily accomplished by a series of genetic crosses (dotted arrow) because all NBE-CreC inserts are on chromosome III, and all NBE-CreB inserts are on II. (B) Crossing scheme for a tripartite SpaRCLIn screen. Initial crosses similar to those described for the bipartite screen are performed to combine essential SpaRCLIn components together with the Gal4 driver. Now, however, DNE-CreA is used instead of DNE-CreAB. Progeny with the final genotype for testing are generated using flies made as described in A that combine NBE-CreB and -CreC components.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/53041/elife-53041-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Schematic of the plasmid used to make flies with the Cre80Tom construct and either the UAS-mCD8GFP, UAS-dTrpA1, or UAS-Kir2.1 construct. The latter are inserted into the plasmid via a unique NdeI restriction site in the plasmid. (B) Annotated sequence of the Cre80Tom-GFP expression construct.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/53041/elife-53041-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** (A–C) Three representative examples of the labeling patterns obtained with the R16H11-CreB∩R25G06-CreC enhancer pair in the tripartite SpaRCLIn system. All animals whose expression was restricted in this way (n = 14) showed induced PE when expressing dTrpA1 and all had expression in the PErk neurons of the SEZ. In addition, however, each preparation also exhibited expression in a range of other neurons (arrows). Scale bar: 50 μM.

![Video 1.](https://cdn.elifesciences.org/articles/53041/elife-53041-video1.mp4.jpg)

**Video 1.:** rkpan-Gal4 was used to drive expression of the heat-activated ion channel, UAS-dTrpA1. At 18°C the channel is inactive and animals expressing it throughout the rkpan-Gal4 pattern do not extend their proboscis. In contrast, at 31°C when the channel is activated, animals display prolonged proboscis extension.

Taking advantage of SpaRCLIn’s ability to further restrict expression, we used the tripartite system to carry out a second (‘Step 2’) screen in which the 23 identified NBE-CreC components were combined pairwise with NBE-CreB components made using the same 23 enhancers (Figure 3—figure supplement 1B). The latter were selected from the NBE-CreB library and crosses were made that combined distinct NBE-CreB and NBE-CreC components with DNE-CreA, rkpan-Gal4, and Cre80Tom-GFP. These Step two crosses resulted in CreA∩B∩C ∩ rkpan-Gal4 intersections that were assayed for PE as before. Approximately 70 intersections were tested before screening was discontinued because 11 intersections had already yielded PE phenotypes in greater than 50% of flies. The phenotype observed was typically less sustained than that produced by activation of the full rkpan-Gal4 expression pattern in that activation typically caused rhythmic, rather than tonic, extension of the proboscis, which after prolonged heating often transitioned to lifting of the rostrum rather than full extension (Video 2; Figure 3E).

![Video 2.](https://cdn.elifesciences.org/articles/53041/elife-53041-video2.mp4.jpg)

**Video 2.:** The tripartite SpaRCLIn system isolates a subset of neurons within the rkpan-Gal4DNE-CreA∩R16H11-CreB∩R44F09-CreC intersection called the PErk neurons. When activated using dTrpA1 and a temperature of 31°C repeated, rhythmic proboscis extension is induced.

The rkpan-Gal4 expression patterns in flies exhibiting this phenotype were substantially reduced for many of the intersections tested and they consistently included particular neurons in the subesophageal zone (SEZ) that were characterized by somata near the saddle, broad arbors along the superior gnathal ganglion (GNG), and axons that extended medially before turning, with one branch coursing down each side of the midline and then turning laterally along the medial-inferior edges of the GNG (Video 3). Two closely apposed neurons of this type were observed, sometimes as bilateral pairs (Figure 3F), and sometimes on only one side (Figure 3G). These neurons, which we call the PErk neurons, were notably prominent in the 16H11-CreB∩44F09-CreC intersection, where they constituted the entire expression pattern of 16 animals (n = 78 total), all of which exhibited PE induction upon heating. Indeed, all 36 animals from this intersection that tested positive for the PE phenotype and were successfully dissected showed expression in the PErk neurons, while none of the animals (n = 38) that tested negative had such expression (Figure 3I). Most of the latter, in fact, had little to no expression. Similar results were obtained with a second intersection (44F09-CreB∩10G07-CreC). All 19 animals that exhibited induced PE in this intersection had expression in the PErk neurons, and in three animals these were the only neurons present. A third intersection that yielded the PE phenotype in all animals likewise showed consistent expression in the PErk neurons, but the correlation between the PE phenotype and expression in these neurons was somewhat less readily established because of expression in other neurons (5.6 ± 1.8; n = 14 preparations; Figure 3—figure supplement 3).

![Video 3.](https://cdn.elifesciences.org/articles/53041/elife-53041-video3.mp4.jpg)

**Video 3.:** GFP-labeled PErk neurons (green) were imaged by confocal microscopy to show the location of their somata and their arborization. Neuropil labeled by nc82 antibody is shown in blue to identify brain regions.

### FRTerminator: a self-excising DNE-CreAB to facilitate fine-mapping in Step one screens

The above examples demonstrate that SpaRCLIn can be used to rationally parse the expression patterns of Gal4 drivers using the workflow shown in Figure 3—figure supplement 1. One challenge to using this system, however, is the large number of transgenes required to implement it. This is especially true for Step two screening with the tripartite system. To mitigate this burden, we have created several reagents that will facilitate use of the system. In addition to the Cre80Tom-GFP construct described above, we have developed other dicistronic constructs to facilitate manipulating neuronal activity in SpaRCLIn screens (see Key Resources Table). These include constructs and fly lines for Cre80-Kir2.1 and Cre80-dTrpA1 (Figure 3—figure supplement 2). In addition, we have developed an alternate Step one strategy that may avert the need for Step two screening in favorable cases.

The alternate strategy uses a transiently expressed DNE-CreAB designed to be active only during early stages of neurogenesis. This construct, which we call ‘FRTerminator,’ is self-excising in that it is flanked by Flp Recombination Target (FRT) sites and encodes a Flp recombinase gene that is co-expressed with CreAB (Figure 4A). Upon expression under control of the DNE enhancer, this construct will remove the CreAB gene and thus limit its expression to early (embryonic) neuroblasts (Figure 4B). CreAB will thus be available to reconstitute Cre activity only with complimentary CreC fragments that are also expressed at this time. CreCs whose expression is driven by NBEs that become active only after the elimination of CreAB from neuroblasts, will not lead to the generation of Gal4-competent neurons. Expression patterns resulting from the combination of FRTerminator with NBE-CreCs will thus, in general, be reduced relative to those produced by DNE-CreAB (Figure 4C,D).

![Figure 4.](https://cdn.elifesciences.org/articles/53041/elife-53041-fig4-v2.jpg)

**Figure 4.:** (A) The FRTerminator construct: a DNE-CreAB that terminates its own expression. The FRTerminator expression cassette contains sequences for the Flp recombinase and CreAB-NrdJ-1N linked by a viral T2A sequence to ensure separate translation of the two gene products. The entire cassette is flanked by FRT sites. Upon expression of the cassette—which will occur in NBs at the onset of neurogenesis—Flp will excise the cassette, thus terminating any further expression of both Flp and CreAB-NrdJ-1N. (B) Schematic comparing the consequences of DNE-CreAB (left box) and FRTerminator (right box) action in two NB lineages (NB1 and NB2) in which an NBE (used to drive expression of CreC) is active. In NB1 the NBE is active early in neurogenesis and CreC will therefore be expressed in the young neuroblast. In contrast, the NBE becomes active only late in neurogenesis in NB2 and CreC is therefore only present in the older NB. Because DNE-CreAB is expressed throughout neurogenesis, it will be available to reconstitute full-length Cre whenever CreC is expressed. This means that Gal80 will be excised and tdTomato expression turned on (red) early in NB1—leading to the labeling of all progeny—and late in NB2—leading to labeling of only late-generated progeny. In contrast, FRTerminator is present only early in neurogenesis and Cre reconstitution (and tdTomato expression) will therefore occur only in NB1. No progeny of the NB2 clone will be labeled and the overall pattern of labeling will thus be diminished. (C–D) NB lineages targeted using NBER16H11-CreC and either the DNE-CreAB construct of the bipartite SpaRCLIn system (C), or FRTerminator (D). NB progeny are visualized with tdTomato (red) after excision of Gal80 by Cre. The breadth of tdTomato expression when using DNE-CreAB compared with FRTerminator reflects the loss of sublineages generated by NBs in which the R16H11 enhancer becomes active only later in neurogenesis, as illustrated in B. Anti-nc82 labeled neuropil (blue); ventral nerve cord; VNC; brain; Br. Scale bar: 50 μM. (E–F) Restriction of the rkpan-Gal4 expression pattern by SpaRCLIn using R14E10-CreC with DNE-CreAB (E) or FRTerminator (F). FRTerminator significantly reduces the expression pattern compared with the restriction obtained with DNE-CreAB, labeling principally the PErk neurons. Reporter: UAS-mCD8GFP (green); Anti-nc82 labeled neuropil (magenta); ventral nerve cord; VNC; brain; Br. Scale bar: 50 μM.

To determine whether the FRTerminator might therefore expedite parsing of Gal4 expression using the SpaRCLIn system, we repeated selected crosses from the rkpan-Gal4 Step one screen described above. We focused on the 23 NBE-CreC lines that yielded flies with PE phenotypes, combining each with the FRTerminator, rkpan-Gal4 and Cre80-GFP. Progeny were tested for PE upon dTrpA1 activation. We found that three NBE-CreC lines (44F09, 57B09, and 14E10) produced progeny with PE phenotypes at frequencies ranging from 9–17%. Although these frequencies were considerably lower than those obtained using DNE-CreAB, the resulting expression patterns were substantially sparser compared with those of progeny from DNE-CreAB crosses (Figure 4E,F). All animals examined that had PE phenotypes also included in their expression patterns the PErk neurons (n = 40). In contrast, only one of the animals examined that lacked the phenotype had these neurons (n = 39). A strong correlation between PE and the presence of the PErk neurons was thus observed, again permitting the conclusion that these neurons are substrates for the behavioral phenotype. We conclude that FRTerminator-based Step one screens may serve as a useful shortcut to serial Step one and Step two screens for restricting Gal4 expression and identifying functionally important neuronal subsets.

## Discussion

The SpaRCLIn system introduced here permits the refined targeting of neurons within a group of interest based on both their developmental origins and their patterns of gene expression in the terminally differentiated state. By permitting the combinatorial targeting of many, if not most, of the neuroblasts that generate the mature CNS, the SpaRCLIn system provides end-users with a comprehensive, ‘off-the-shelf’ set of reagents for systematically isolating and characterizing the anatomy and function of specific neurons. The reagents that we have created include extensive lineage-selective Split Cre lines for bipartite (Step 1) and tripartite (Step 2) neuronal screens, in addition to a range of tools that facilitate application of the system. Dual effector and reporter constructs reduce the number of transgenes required to implement the system, and a self-terminating Split Cre component (i.e. FRTerminator) can be used to expedite screening in favorable circumstances. The system is compatible with existing Gal4 driver lines and the examples provided here indicate that it is capable of routinely parsing Gal4 expression patterns into subsets of neurons numbering in the single digits.

### Utility of SpaRCLIn to circuit mapping

Our use of SpaRCLIn to identify the RK-expressing neurons that trigger robust proboscis extension demonstrates SpaRCLIn’s ability to systematically parse a neuronal group and identify the functionally relevant subset. Just over 200 crosses—134 crosses for the Step 1 screen of NBE-CreC lines and 70 NBE-CreB∩C Step two crosses—were required to identify two pairs of command-like neurons capable of inducing PE upon activation (i.e. the PErk neurons). Importantly, we discontinued the Step two screen after testing 70 of the 253 possible intersections because of evident redundancy of the command-like neurons. The latter were prominent in the expression patterns of numerous independent Step two intersections and were readily correlated with PE induction in three that produced particularly reduced expression patterns. In the intersection with the sparsest expression, the two pairs of PE-inducing neurons often comprised the entire observable pattern in flies that had the PE phenotype, illustrating the extreme reduction in expression achievable with SpaRCLIn. The demonstration that the PErk neurons can be isolated in single crosses using the FRTerminator indicates that this reduction in expression can be attained without the labor of Step two screening. However, the lower frequency of the PE phenotype in FRTerminator crosses in our example also suggests that FRTerminator-based screens may require testing more animals for each intersection than a standard Step one screen in order to reliably identify positives.

Activation of the PErk neurons elicits rhythmic proboscis extension, rather than the tonic PE elicited by activation of all rkpan-Gal4 neurons. This suggests that additional RK-expressing neurons—perhaps lacking command capability—modulate the effects of activating the PErk neurons. Based on their induction of rhythmic extension and their apparent lack of a projection to the proboscis muscles, we conjecture that the PErk neurons identified here are not motor neurons, the activation of which results in tonic and often partial PE (Gordon and Scott, 2009; Schwarz et al., 2017). Similarly, the anatomy of the PErk neurons differs from that of other identified neurons that can drive PE when activated, including second-order projection neurons (Kain and Dahanukar, 2015), modulatory neurons (Marella et al., 2012), and a local SEZ interneuron called the Fdg-neuron (Flood et al., 2013). Like the Fdg-neuron, however, the neurons identified here seem to function in a premotor capacity, perhaps as part of the central pattern generator for PE that regulates fly feeding (Itskov et al., 2014). Further work will be required to determine the precise role of the PErk neurons in the feeding circuitry and their relationship to other identified neurons involved in PE.

It also remains to be determined whether activation of both PErk neurons is required to induce the PE phenotype. Indeed, from the standpoint of the efficacy of the SpaRCLIn system it is important to ask why SpaRCLIn failed to separate these two pairs of neurons. The similarity of the two PErk neurons in both soma position and projection pattern is consistent with their being part of the same lineage. Such neurons will necessarily be more difficult to parse using SpaRCLIn, which can separate neurons within the same lineage only based on their birth order. What would be required to do so is having two NBEs that are active in the same lineage but at different times so that they separate earlier- from later-born neurons. Such NBEs, by generating Cre only in older neuroblasts, will generate sublineages of Gal4-competent neurons. Although many of the NBE’s used to make our CreB and CreC libraries clearly generate such sublineages—based on the patterns shown in Figure 1—figure supplement 1—it is doubtful that they cover more than a fraction of all temporal windows of neurogenesis in all neuronal lineages. A method for systematically isolating sublineages of later born neurons using SpaRCLIn may become possible if neuroblast-specific enhancers can be found that are selectively active at later stages of neurogenesis. These could then be used in lieu of the DNE used here. Candidates for such enhancers are those that determine expression of the so-called ‘temporal transcription factors’ that regulate the progressive divisions of many neuroblasts (Doe, 2017).

### Variability of SpaRCLIN expression

Although stochasticity is not an uncommon feature of many expression systems (Bohm et al., 2010; Tastekin and Louis, 2017), the variability of expression generated by SpaRCLIn was notable. Even for intersections that reliably produce very similar expression across animals, it is not common to get exactly the same pattern twice. The infidelity of expression may derive, at least in part, from intrinsic stochasticity of NBE activity. However, our results indicate that individual NBEs drive expression in broadly reproducible patterns. Other factors that may contribute to expression variability include the strength and/or temporal properties of NBE activity. If a Cre component is only weakly expressed, or expressed late during neurogenesis, a limited amount of active, full-length Cre may be produced and excision of Gal80 may be sporadic in the expressing neuroblasts. Also, the success of Cre reconstitution may vary, and may be particularly low when the religation of three fragments is required. Although the two split inteins used in the SpaRCLIn system were chosen based on their favorable reaction kinetics as determined in vitro, the speed, efficiency, and variability with which they react in different types of cells remain unknown. Finally, because the efficacy of Cre-mediated excision depends on the distance between the loxP sites flanking the excised fragment, it may prove possible to increase the efficacy of excision—and thus reduce variability of expression—using strategies that decrease the distance between the loxP sites flanking the fragment to be excised.

While further work will be required to identify the sources of variable expression within the system, the observed stochasticity is not necessarily a disadvantage for circuit-mapping applications, as illustrated by the examples presented here. By providing partially ‘randomized’ expression patterns, SpaRCLIn permits causative relationships to be inferred between groups of manipulated neurons and the effects produced by their manipulation (Jazayeri and Afraz, 2017). Such randomization has been commonly exploited in so-called ‘Flp-out’ methods that rely on stochastically induced recombinase activity to remove an FRT-flanked gene or transcription stop cassette (Flood et al., 2013; Gordon and Scott, 2009; Kain and Dahanukar, 2015). This logic is naturally implemented in SpaRCLIn, but because randomness of expression is considerably more constrained than that observed in systems that rely on strictly stochastic methods, and because the size of the expression patterns is typically small, correlations can be readily established.

One consequence of SpaRCLIn’s stochasticity that must be considered in circuit mapping applications, however, is the lowered frequency of bilateral labeling. Most neurons occur as members of bilateral pairs and we observed numerous instances in which SpaRCLIn-derived expression patterns contained only a single member of each pair in a given preparation—presumably due to the variable success of Gal80 excision in both NBs giving rise to the pair. The reduced bilateral representation of neurons may likewise reduce the frequency of phenotypes observed as a consequence of a particular manipulation if, for example, both neurons in a pair must be affected to produce a phenotype. This is often the case for suppression of function, where both neurons in the pair must be inhibited. It is therefore possible that SpaRCLIn will be most effective in applications that involve neuronal activation where unilateral manipulations are often sufficient to generate an effect as they are for proboscis extension.

### Other considerations in the use of SpaRCLIn

The ability of SpaRCLIn to isolate a given set of neurons of interest in a Gal4 pattern depends critically on the extent to which the various Split Cre components are expressed in the neuroblast lineages of the fly. This will be determined both by the breadth of NB expression of the DNE enhancer used here to delimit Cre activity and by the collective coverage of NB expression provided by the NBEs represented in the libraries of CreB and CreC lines. Our analysis of 3rd instar larval expression in DNE∩NBE intersections (Figure 1—figure supplement 1 and data not shown) indicates that many, if not most, NB lineages of the ventral nerve cord and central brain are likely represented within the libraries. Indeed, many lineages are clearly represented multiple times in that different intersections repeatedly isolated the same neurons (e.g. the PErk neurons) for both the rkpan-Gal4 and TH-Gal4 drivers. It is less clear, however, that all members of each lineage are represented as not all NBE’s are active during early NB divisions. This is evident from the restriction in NB expression observed when the FRTerminator construct is used, since this construct acts by eliminating lineages or sublineages in which Cre activity is initiated sometime after neurogenesis has begun. It is also clear that the DNE does not express efficiently in NB lineages in the optic lobe (data not shown). To extend the capability of the system to include these lineages will require either the development of a more general neuroblast-specific enhancer or augmenting the system to include an enhancer that specifically targets optic lobe NBs.

The effectiveness of SpaRCLIn also depends critically on the success of Cre reconstitution by the system, which is effected by two pairs of split inteins (Shah and Muir, 2011; Shah and Muir, 2014). These trans-splicing protein fragments function naturally in protein religation and are an emerging technology for use in transgenic animals (Hermann et al., 2014; Wang et al., 2018; Wang et al., 2012). Their advantages are that they lend themselves readily to intersectional methods, are genetically encoded, and in numerous cases display rapid reaction kinetics and low cross-reactivity. A disadvantage, on which some recent progress has been made (Stevens et al., 2017), is that most split inteins require specific flanking amino acid residues in the proteins to which they are fused, in particular a cysteine or serine residue immediately downstream of the N-intein. We were able to create self-ligating split Cre fragments capable of reconstituting full-length, active Cre enzyme in Drosophila NBs by choosing breakpoints in the Cre sequence preceded by a serine residue—the native condition of the NrdJ-1 and gp41-1 split inteins used here (Carvajal-Vallejos et al., 2012). Orthogonal (i.e. non-interacting) split inteins thus represent attractive tools for reconstituting the function of multiply split proteins, a methodology that should be applicable in other model organisms.

### Conclusions and future development

Although sophisticated methods for neuronal targeting have been a hallmark of neurobiological studies on the fly, and single cell manipulations are being leveraged in a growing number of cases to elucidate Drosophila brain circuits, targeting every cell in the fly CNS remains an aspirational goal. Recent progress towards this goal has been made using the Split Gal4 system (Dionne et al., 2018; Tirian et al., 2017), and innovative methods continue to be developed using emerging tools (Garcia-Marques et al., 2019). An advantage of SpaRCLIn is that it represents a relatively small set of stand-alone reagents for high-specificity neuronal targeting that can be used with the many existing components of the Gal4-UAS system. Importantly, SpaRCLIn also represents an open resource that can readily be augmented by end-users. As methods improve for rationally identifying NB lineages based on gene expression and enhancer activity, the existing SpaRCLIn libraries can be supplemented with lines that together permit the selective targeting of an increasing number of neuroblast lineages. The NB-specific enhancers recently identified by Lacin and Truman (2016) and used here to characterize our split Cre components (Figure 1—figure supplement 2D) provide good examples of reagents that can be used to improve the SpaRCLIn libraries. By combining these libraries with an optimized set of Gal4 drivers that express in distinct subsets of brain cells (distinguished, for example, by transcription factor expression), one can imagine having a set of 3 libraries that in combination can selectively target most neurons in CNS.

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
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w; Sco/Cyo; Rkpan-Gal4</td>
      <td>Diao and White, 2012</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w; UAS-TrpA1(attP16);+</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>RRID:BDSC_26263</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w; +; TH-Gal4</td>
      <td>J Hirsh and S Birman</td>
      <td>THGal4-1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>yw; mCD8-GFP/Cyo;+</td>
      <td>Gift of Liqun Luo</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w; DNE-CreAB (JK22C);+</td>
      <td>This paper</td>
      <td>HJ210</td>
      <td>Supplementary file 4</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w, DNE-CreB[su(Hw)attP8]; Pin/CyO; TM3,Sb1/TM6B,Hu1,Tb1</td>
      <td>This paper</td>
      <td>HJ201</td>
      <td>Supplementary file 4</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w; +; DNE-CreA (VK00027)</td>
      <td>This paper</td>
      <td>HJ200</td>
      <td>Supplementary file 4</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w; DNE-CreA (attP40); +</td>
      <td>This paper</td>
      <td>HJ200</td>
      <td>Supplementary file 4</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w, Cre80Tom[su(Hw)attP8]; Pin/CyO; TM3,Sb1/TM6B,Hu1,Tb1</td>
      <td>This paper</td>
      <td>HJ223</td>
      <td>Supplementary file 4</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w, Cre80Tom-GFP[su(Hw)attP8]; Pin/CyO; TM3,Sb1/TM6B,Hu1,Tb1</td>
      <td>This paper</td>
      <td>HJ224</td>
      <td>Supplementary file 4</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w; DNE-Frterminator (attP40);+</td>
      <td>This paper</td>
      <td>HJ473</td>
      <td>Supplementary file 4</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w; +; DNE-CreBC (attP2)</td>
      <td>This paper</td>
      <td>HJ209</td>
      <td>Supplementary file 4</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-CreC (attP40)</td>
      <td>This paper</td>
      <td>HJ226</td>
      <td>Supplementary file 4</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>CreStop (attP2)</td>
      <td>This paper</td>
      <td>HJ225</td>
      <td>Supplementary file 4</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w, Cre80-Kir2.1[su(Hw)attP8]; Pin/CyO; TM3,Sb1/TM6B,Hu1,Tb1</td>
      <td>This paper</td>
      <td>HJ472-actin5C-FloxSyn21Gal80-pMUH-Kir2.1</td>
      <td>Supplementary file 4</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w, Cre80-TrpA1[su(Hw)attP8]; Pin/CyO; TM3,Sb1/TM6B,Hu1,Tb1</td>
      <td>This paper</td>
      <td>HJ382-actin5C-FloxSyn21Gal80-10XUAS-dTrpA1</td>
      <td>Supplementary file 4</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>R59E09-Gal4(attP2)</td>
      <td>BloomingtonDrosophila Stock Center</td>
      <td>RRID:BDSC_39220</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat monoclonal anti-Mouse CD8a</td>
      <td>Invitrogen Life Technologies</td>
      <td>RRID:AB_10392843</td>
      <td>1:100 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal Alexa Fluor 488 anti-rat IgG (H+L)</td>
      <td>Invitrogen Life Technologies</td>
      <td>RRID:AB_2534074</td>
      <td>1:500 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal Anti-RFP Antibody</td>
      <td>Rockland, Imm.</td>
      <td>RRID:AB_2209751</td>
      <td>1:5000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal Anti-futsch Antibody</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>RRID:AB_528403</td>
      <td>1:50 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal Living Colors DsRed Polyclonal Antibody</td>
      <td>CLONTECH Laboratories</td>
      <td>RRID:AB_10013483</td>
      <td>1:500 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal Cy3 AffiniPure Goat Anti-Rabbit IgG (H+L)</td>
      <td>Jackson Immuno-Research</td>
      <td>RRID:AB_2338006</td>
      <td>1:500 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal nc82</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>RRID:AB_2314866</td>
      <td>1:50 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal Alexa Fluor 488 goat anti-mouse IgG (H+L)</td>
      <td>Invitrogen Life Technologies</td>
      <td>RRID:AB_2534069</td>
      <td>1:500 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal Alexa Fluor 647-AffiniPure Goat Anti-Mouse IgG (H+L)</td>
      <td>Jackson Immuno-Research</td>
      <td>RRID:AB_2338914</td>
      <td>1:500 dilution</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>CreA</td>
      <td>This paper</td>
      <td>HJP-176-IVS-Syn21-CreA-gp41-1N-WPREw</td>
      <td>For making CreA line from promoter</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>CreB</td>
      <td>This paper</td>
      <td>HJP-180-IVS-Syn21-gp41-1C-CreB-NrdJ-1N-WPREw</td>
      <td>For making CreB line from promoter</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>CreC</td>
      <td>This paper</td>
      <td>HJP-179-IVS-Syn21-NrdJ-1C-CreC-WPREw</td>
      <td>For making CreC line from promoter</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>CreAB</td>
      <td>This paper</td>
      <td>HJP-178-IVS-Syn21-CreAB-NrdJ-1N-WPREw</td>
      <td>For making CreAB line from promoter</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>CreBC</td>
      <td>This paper</td>
      <td>HJP-177-IVS-Syn21-gp41-1C-CreBC-WPREw</td>
      <td>For making CreBC line from promoter</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>CreAU</td>
      <td>This paper</td>
      <td>HJP-194-IVS-Syn21-CreA-gp41-1N-WPREUw</td>
      <td>For making CreA from enhancer</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>CreBU</td>
      <td>This paper</td>
      <td>HJP-195-IVS-Syn21-gp41-1C-CreB-NrdJ-1N-WPREUw</td>
      <td>For making CreB line from enhancer</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>CreCU</td>
      <td>This paper</td>
      <td>HJP-196-IVS-Syn21-NrdJ-1C-CreC-WPREUw</td>
      <td>For making CreC line from enhancer</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>CreABU</td>
      <td>This paper</td>
      <td>HJP-208-IVS-Syn21-CreAB-NrdJ-1N-WPREUw</td>
      <td>For making CreAB line from enhancer</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>CreBCU</td>
      <td>This paper</td>
      <td>HJP-207-IVS-Syn21-gp41-1C-CreBC-WPREUw</td>
      <td>For making CreBC line from enhancer</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>CreStop</td>
      <td>This paper</td>
      <td>HJP-225-actin5C-Flox-IVS-Syn21myr-tdTomato-p10w</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Cre80Tom</td>
      <td>This paper</td>
      <td>HJP-223-actin5C^Syn21Gal80^IVS-Syn21myr-tdTomato-p10w</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Cre80Tom-GFP</td>
      <td>This paper</td>
      <td>HJP-224-actin5C^Syn21Gal80^IVS-Syn21myr-tdTomato-10UAS-mCD8GFP-p10w</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>UAS-CreC</td>
      <td>This paper</td>
      <td>HJP-226-10XUAS-NrdJ-1C-CreC</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>DNE-FRterminator</td>
      <td>This paper</td>
      <td>HJP-473-DNE &gt; -T2A-CreAB-NrdJ-1N</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Cre80-Kir2.1</td>
      <td>This paper</td>
      <td>HJP-472-actin5C-FloxSyn21Gal80-10XUAS-EGFP-Kir2.1</td>
      <td>Genetic reagent (D. melanogaster)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Cre80-dTrpA1</td>
      <td>This paper</td>
      <td>HJP-382-actin5C-FloxSyn21Gal80-10XUAS-dTrpA1</td>
      <td>Genetic reagent (D. melanogaster)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Gateway LR Clonase II Enzyme mix</td>
      <td>Thermofisher Scientific</td>
      <td>11791100</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>In-Fusion HD Cloning Plus</td>
      <td>Takara Bio USA, Inc</td>
      <td>638911</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>pCR8/GW/TOPO TA Cloning Kit with One Shot TOP10 Chemically Competent E. coli</td>
      <td>Invitrogen Life Technologies</td>
      <td>K2500-20</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>pENTR/D-TOPO Cloning Kit, with One Shot TOP10 Chemically Competent E. coli</td>
      <td>Invitrogen Life Technologies</td>
      <td>K240020</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Q5 High-Fidelity 2X Master Mix</td>
      <td>New England Biolabs</td>
      <td>M0492S</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Quick Ligation Kit</td>
      <td>New England Biolabs</td>
      <td>M2200L</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Drosophila stocks

Vinegar flies of the species Drosophila melanogaster were used in this study. Unless otherwise noted, all flies were grown on BDSC Cornmeal Food and maintained at 25°C in a constant 12 hr light–dark cycle. Both male and female progeny of the genotypes indicated in Supplementary file 2 were used in this study. Previously described fly stocks and their sources are listed in the Key Resources Table. Fly lines generated for this study were made using the DNA constructs described below. Injection of these constructs to produce transgenic flies was carried out by Rainbow Transgenic Flies, Inc (Camarillo, CA). All transgene insertions except the insertion of the DNE-Gal4 were mediated by ΦC31 integrase and placed in the defined attP landing sites indicated in Key Resources Table. Flies made with the DNE-Gal4 were generated by p-element mediated transgenesis. Transgenic flies of the NBE-CreB library have transgene insertions on the 2nd chromosome at attP40, while all flies in the NBE-CreC library have insertions on the 3rd chromosome at either VK00033 or VK00027.

### Molecular biology

All oligonucleotide and gBlock synthesis was carried out by Integrated DNA Technologies, Inc (Coralville, Iowa), and all final constructs were verified by sequencing (Eurofins Scientific, Louisville, KY or Macrogen Corp, Rockville MD). For routine molecular biology, the following reagents were used according to the manufacturers’ supplied protocols: PCR amplification: Q5 High-Fidelity 2X Master Mix #M0492S (New England Biolabs, Ipswich, MA); DNA ligation: Quick Ligation Kit #M2200L (New England Biolabs, Ipswich, MA); Cloning: Gateway LR Clonase II Enzyme mix #11791100 (Thermofisher Scientific, Waltham, MA), and In-Fusion HD Cloning Plus #638911(Takara Bio USA, Inc, Mountain View, CA). gBlocks were used to generate most of the final and intermediate constructs described below, including the DNA fragments encoding the NrdJ-1 and gp41-1 split inteins and the Cre fragments described in the manuscript. DNA sequences of the split inteins were back-translated from the published protein sequences (Carvajal-Vallejos et al., 2012) and all sequences were codon biased for Drosophila. Sequences of all gBlock fragments and PCR primers are listed in Supplementary file 3. The following reagents, which were used to make several constructs as indicated below, are all described in Pfeiffer et al. (2010): pBPGal80Uw-5, pBPLexA::P65, 10XUAS-IVS-myr::tdTomato, 10XUAS-mCD8::GFP, and pBPGAL80Uw-6.

### Cre80Tom constructs

The indicated Cre80Tom constructs were made stepwise using the described procedures.

#### Cre80Tom

Step 1 - Made the intermediate construct ‘M1:’ an NgoMIV-gBlock013-AatII fragment, an AatII-Gal80-SV40-MfeI fragment (from pBPGal80Uw-5), and an MfeI-gBlock014-KpnI fragment were placed between the NgoMIV and KpnI restriction sites of pBPLexA::P65. Step 2: PCR amplified a KpnI-IVS-StuI-AgeI-myr-tdTomato fragment (Primer71 + Primer72, 10XUAS-IVS-myr::tdTomato as template) and a p10-XbaI fragment (Primer71a + Primer72a, using as template CCAP-IVS-Syn21-KZip+-p10; Dolan et al., 2017) and used these to replace the KpnI-XbaI fragment of M1 using In-Fusion HD cloning to make the intermediate construct ‘M2.’ Gateway cloning of M2 was then performed to add the Actin5C promoter (Harris et al., 2015) and get the final Cre80Tom construct.

#### Cre80Tom-GFP

Step 1: A 10XUAS-mCD8GFP PCR fragment (template 10XUAS-mCD8::GFP, Primer59+Primer58) was inserted into the unique NdeI site between the mini-white gene and the attB sequence of the M1 vector. Step 2: A KpnI-IVS-Syn21-myr-tdTomato-StuI PCR fragment (Primer75, Primer76, template:10XUAS-IVS-myr::tdTomato) and a StuI-p10-SpeI PCR fragment (primer HJ077, HJ078) were placed between the KpnI and SpeI restriction sites to replace the LexA::P65 fragment and to produce the intermediate construct ‘M3’ using the In-Fusion HD cloning kit. Step 3: Used Gateway Cloning to add the Actin 5C promoter to produce the Cre80Tom-GFP.

#### Cre80-dTrpA1 and Cre80-Kir2.1

The sequence between the KpnI and NsiI of M3 (including the IVS-Syn21-myr-tdTomato-p10- and a small part of the mini-white gene) were replaced with gBlock25 by HD-infusion cloning to make the intermediate construct ‘M4.’ This step removed the tdTomato gene. The BglII-mCD8GFP-XbaI fragment of M4 was replaced with BglII-dTrpA1-XbaI (template: UAS-dTrpA1, gift from Paul Garrity) and BglII-EFGP-Kir2.1-XbaI (template UAS-EGFP-Kir2.1, gift of Sean Sweeney) PCR fragments and then the actin5C promoter was inserted by Gateway cloning to get Cre80-dTrpA1 and Cre80-Kir2.1.

### Split Cre constructs

All split Cre constructs were made by Gateway cloning (LR reaction). Two sets of destination vectors with split Cre components were made: one for use with entry clones containing promoters, and another for entry clones containing enhancers. The 134 NBE entry clones were combined with the latter to make the expression clones used to generate the CreB and CreC libraries.

To make the CreA (HJP-176) destination vectors for use with promoter entry clones, a KpnI-IVS-NheI fragment made from annealed oligonucleotides, a NheI-gBlock012-AgeI gBlocks fragment and an AgeI-PmeI-WPRE-HindIII PCR fragment (amplified from pBPGAL80Uw-6 using PrimerS472 and PrimerS473) were placed between the NheI and HindIII restriction sites of the pBPGw vector (Addgene Plasmid #17574 Pfeiffer et al., 2008). Other split Cre destination vectors (i.e. HJP177 ~HJP180; see the Key Resources Table) were made by replacing the NheI-CreA-gp41-1N-AgeI fragment in CreA (HJP-176) with fragments consisting of: NheI-gBlock010-SphI + SphI-gBlock011-AgeI (HJP177), NheI-gBlock008-BsaI+BsaI-gBlock009-AgeI (HJP178), NheI-gBlock007-AgeI (HJP179), or NheI-gBlock010-SphI+SphI-gBlock015-AgeI (HJP180). To create a set of destination vectors for use with enhancer entry clones (‘the U-series’), an FseI-DSCP-KpnI synthetic core promoter (Pfeiffer et al., 2008) was made from annealed oligos and inserted between the FseI and KpnI restriction sites of each of the destination vectors made for use with promoter entry clones. This produced constructs HJP194 ~196, HJP-207 and HJP-208 (See Key Resources Table).

Prior to the production of transgenic fly lines, the functionality of all Cre constructs was validated in cultured S2 cells by placing the constructs under the control of the Actin5C promoter and testing in appropriate combinations for expression and activity using a floxed reporter construct.

### DNE and NBE entry clones

#### DNE

A 2 kb region upstream of the deadpan gene previously shown to harbor a NB enhancer by Emery and Bier (1995) was Evoprinted (Yavatkar et al., 2008) using the sequences of five Drosophila species (D. sechellia, D. simulans, D. erecta, D. yakuba, and D. ananasseae) in addition to D. melanogaster. A 607 bp region starting 899 nucleotides 5’ of the transcription start exhibited highly conserved sequence blocks containing transcription factor binding sites, including three CAGCTG E-boxes commonly found in other NB enhancers (Brody et al., 2012). A PCR fragment containing this 607 bp region was cloned into the Bullfinch Gal4 reporter vector (Brody et al., 2012), and the DNE enhancer was made by inserting next to it a previously described mutant nerfin-1 enhancer with two adjacent bp substitutions (G→C and T→C) that were shown to expand the pattern of NB expression (Kuzin et al., 2011). The mutant nerfin-1 enhancer was amplified by PCR from pCRII-TOPO (Thermofisher Scientific, Waltham, MA) and is separated from the dpn enhancer by 10 bp of DNA sequence from the pCRII-TOPO vector, including the EcoRI site that was used to insert this enhancer adjacent to the dpn enhancer. A DNE vector for use in Gateway cloning was made by transferring the DNE enhancer into the pENTR-D-TOPO entry clone as a PCR fragment (primers: DNE-Sense and DNE-Antisense) using the pENTR/D-TOPO Cloning Kit).

Most of the neuroblast-active enhancers used to make the NBE entry clones were from the JFRC Flylight Collection (Pfeiffer et al., 2008).Candidate Flylight enhancers were selected based either on their previous identification as embryonic neuroblast enhancers (active in subset of neuroblasts) (Manning et al., 2012) or on the presence of expression in NBs in the 3rd instar CNS as determined by visual inspection of the expression patterns at the Flylight website (https://www.janelia.org/project-team/flylight). To verify NB expression of the latter NBEs, we applied the same method used to examine Cre activity in the single ventral nerve cord lineage labeled by the R59E09-Gal4 line (Figure 1—figure supplement 2D). Flylight Gal4 lines made with the candidate enhancers were pre-screened by crossing them to flies containing the CreStop (HJP225) and UAS-CreC (HJP266) constructs described below with the following genotype: w, DNE-CreB(attP8); UAS-CreC(attP40); CreStop (i.e. actin^STOP^tomato(attP2)), DNE-CreA(VK00027). CNS preparations of the progeny (third instar larvae or adults) were examined for tdTomato expression in NB clones. Selected JFRC Neuroblast active enhancers (NBEs) with ‘sparse’ expression in neuroblasts were amplified by PCR or synthesized when PCR failed (Epoch Life Science, Inc, Missouri City, TX) and cloned into either the pCR8-GW-TOPO or pENTR-D-TOPO donor vectors. Primers listed at the Flylight website were used to amplify most JFRC NBEs using genomic DNA from either y; cn bw sp [gift from James A. Kennison] or Canton S wildtype flies as template.

The cas-8 and CG7229-5 enhancers (Brody et al., 2012; Kuzin et al., 2012) were synthesized as gBlock fragments and cloned by HD-Infusion cloning. The pdm-2-37a (Ross et al., 2015), cas-5 (Kuzin et al., 2012), danR-1, svp-29, and tll-15 enhancer sequences (gifts from Jermaine Ross) were amplified as PCR fragments from plasmids and placed between the NotI and AscI sites of pENTR/D-TOPO vector. The entry clones for the stg-14 (Wang et al., 2014) and otd (Asahina et al., 2014; Gao and Finkelstein, 1998) enhancers have been previously described.

### FRTerminator

This construct (HJP-473) was made as follows: an AvrII and PmeI flanked DNA fragment (including partial nerfin-1 enhancer, FRT and Syn21-flipase-T2A-CreA-gp41-1N-AgeI-FRT) were synthesized (Epoch Life Science, Inc, Missouri City, TX) and put between the AvrII and PmeI restriction sites of DNE-CreA-gp41-1N. The resulting construct can be used in place of DNE-CreA in Step 2 SpaRCLIn screens. It was tested, but its use is not described in this manuscript. This construct was used as an intermediary to make the final FRTerminator construct by inserting gBlock-043 (part of the CreAB sequence and Nrdj-1N) into its SbfI and AgeI restriction sites using the In-Fusion HD cloning technique.

### Other constructs

Two constructs were used to pre-screen candidate enhancers driving Gal4 expression. These included CreStop (HJP225) and UAS-CreC (HJP266). The CreStop construct was made using a NgoMIV-loxP-hsp70 terminator-MluI gBlock to replace the loxP-Gal80 in Cre80Tom (HJP223) by In-Fusion HD cloning. UAS-CreC was made by cloning a NotI-NrdJ-1C-CreC-XbaI PCR fragment (Primer116 and Primer117; CreC as template) between the NotI and XbaI sites of pJFRC1-10XUAS-mCD8::GFP using the In-Fusion HD cloning technique.

### Immunostaining and image acquisition

Embryos were prepared and immunostained as described by Lécuyer et al. (2008). Excised nervous system whole mounts were prepared from wandering third-instar larvae or adults after dissection into PBS and fixation in 4% paraformaldehyde in PBS for 20–30 min. Immunostaining was done with the antibodies listed in the Key Resources Table at the indicated dilutions. For confocal imaging, all tissues were attached to poly-L-lysine coated cover glass and mounted in Vectashield (Vector Laboratories, Burlingame, CA) prior to imaging with a Nikon C-2 confocal microscope. Z-series were acquired in 0.85 μm increments using a 20X objective using 488 nm, 543 nm or 633 nm laser emission lines for fluorophore excitation. The images shown are maximal projections of volume rendered z-stacks of confocal sections taken through the entire nervous system. NB expression of Gal4 driven by the DNE enhancer was examined in embryonic fillets by in situ hybridizations as previously described (Ross et al., 2015).

### Proboscis extension assay

Flies assayed for proboscis extension were raised at 25°C until the white prepupa stage and then transferred to 18°C until the time of testing. For neuronal activation using dTrpA1, the chambers were placed on the surface of the Echotherm Chilling/Heating Dry Bath IC25 (Torrey Pines Scientific, Inc, Carlsbad, CA) at 31°C. For the Step 1 SpaRCLIn screen, approximately a dozen adult flies (3–10 d old) of each genotype were placed in glass TriKinetics tubes (3 mm inner diameter; TriKinetics Inc, Waltham, MA) and videorecorded at 31°C for 3 min using a Sony NEX-VG10 videocamera. Proboscis extension behavior was analyzed from these recordings. If two or more flies exhibited robust, full-length extension, the cross was scored as positive. For the Step two tripartite SpaRCLIn screen, two flies at a time (one male and one female) were videorecorded together in glass minichambers (0.3 cm diameter X 0.7 cm length) for 3 min at 18°C followed by 3 min at 31°C. Flies were subjected to these temperature transitions twice and proboscis extension behavior was analyzed following the recording. The criteria for positive proboscis extension was three or more bouts of full proboscis extension in both tests. For the FRTerminator behavior experiments flies were subjected to only one test. Flies used to make the videos included in the manuscript were back-mounted on a 200 uL pipette tip with 5-Minute-Rapid-Curing, General Purpose Adhesive Epoxy (ITW polymers Adhesive, Danvers, MA) and placed just above the heating plate, which was adjusted to apply temperature changes.

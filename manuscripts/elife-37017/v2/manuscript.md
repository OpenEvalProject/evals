# Building a functional connectome of the Drosophila central complex

## Authors

- Romain Franconville<sup>1</sup> ([ORCID: 0000-0002-4440-7297](https://orcid.org/0000-0002-4440-7297)) †
- Celia Beron<sup>1</sup>
- Vivek Jayaraman<sup>1</sup> ([ORCID: 0000-0003-3680-7378](https://orcid.org/0000-0003-3680-7378)) †

### Affiliations

1. Janelia Research Campus Howard Hughes Medical Institute Ashburn United States

† Corresponding author

## Abstract

The central complex is a highly conserved insect brain region composed of morphologically stereotyped neurons that arborize in distinctively shaped substructures. The region is implicated in a wide range of behaviors and several modeling studies have explored its circuit computations. Most studies have relied on assumptions about connectivity between neurons based on their overlap in light microscopy images. Here, we present an extensive functional connectome of Drosophila melanogaster’s central complex at cell-type resolution. Using simultaneous optogenetic stimulation, calcium imaging and pharmacology, we tested the connectivity between 70 presynaptic-to-postsynaptic cell-type pairs. We identified numerous inputs to the central complex, but only a small number of output channels. Additionally, the connectivity of this highly recurrent circuit appears to be sparser than anticipated from light microscopy images. Finally, the connectivity matrix highlights the potentially critical role of a class of bottleneck interneurons. All data are provided for interactive exploration on a website.

## Introduction

Positioned in the middle of the insect brain, the central complex provides a unique opportunity to obtain mechanistic insights into the way brains build and use abstract representations (Turner-Evans and Jayaraman, 2016). Studies in a variety of insects, including locusts, dung beetles, bees and monarch butterflies, have used intracellular recordings to chart maps of polarized light E-vectors in substructures of the region (Heinze and Homberg, 2007; Heinze and Reppert, 2011a; el Jundi et al., 2015; Stone et al., 2017), and extracellular recordings from the cockroach have found sensory and motor correlates throughout the region (Bender et al., 2010; Guo and Ritzmann, 2013; Ritzmann, 2012). More recently, calcium imaging experiments in behaving Drosophila have shown that both visual and motor cues can update a fly’s internal representation of heading (Seelig and Jayaraman, 2015). Independently, neurogenetic studies have used disruptions of the normal physiology of the structure to highlight its involvement in a variety of functions, including motor coordination (Poeck et al., 2008), visual memory (Liu et al., 2006), sensory-motor adaptation (Triphan et al., 2010), and short- and long-term spatial memory (Neuser et al., 2008; Ofstad et al., 2011). It is likely that these tasks rely on the correct establishment and use of an internal representation of heading (Giraldo et al., 2018; Green et al., 2018).

The scale of the network—a few thousands of neurons in the fly central complex—and the ease of genetic access to individual cell types in Drosophila melanogaster, make this circuit tractable with existing theoretical and experimental methods. Detailed anatomy at the light microscopy level (Hanesch et al., 1989; Wolff et al., 2015; Lin et al., 2013) of a significant fraction of the cell types, along with the availability of tools to genetically target these neurons by type (Wolff et al., 2015), have fueled the first mechanistic investigations of how the circuit constructs a stable heading representation (Kim et al., 2017), and how this representation updates as the animal turns in darkness (Turner-Evans et al., 2017; Green et al., 2017). Such results and related findings from other insects have also inspired a number of modeling studies aimed at predicting or reproducing physiologically and behaviorally relevant response patterns (Kakaria and de Bivort, 2017; Givon et al., 2017; Chang et al., 2017; Cope et al., 2017; Su et al., 2017; Fiore et al., 2017; Kim et al., 2017; Stone et al., 2017; Turner-Evans et al., 2017). Many of these models make assumptions about connectivity within the central complex based on the degree of overlap at the light microscopy level between processes that look bouton-like and those that seem spiny, which are suggestive of pre-and post-synaptic specializations, respectively. To go beyond those anatomical approaches, we constructed a connectivity map based on functional data, which includes information about whether connections are effectively excitatory or inhibitory. This map will help dissect the function of the central complex by constraining large-scale models and aiding the formulation and testing of new hypotheses. Given the dozens of central complex cell types (known and yet to be discovered) omitted in our dataset, the diversity of neurotransmitters and receptors they express, the mixture of pre- and post-synaptic specializations in their arbors, and the dense recurrence of the network, we see this map not as a full connectome, but as an initial scaffold that will allow new information to be incorporated as and when it becomes available.

The quest to obtain circuit diagrams dates back to Cajal and Golgi (Azoulay, 1894; Pannese, 1999), who used sparse labeling techniques to reveal neuron morphology and circuit architectures. Anatomical methods based on marking a discrete subset of neurons and imaging them with light microscopy have recently been revived in the form of techniques relying on stochastic genetic labeling (Livet et al., 2007; Hampel et al., 2011; Nern et al., 2015; Lee and Luo, 2001; Chiang et al., 2011) and photoactivatable fluorophores (Patterson and Lippincott-Schwartz, 2002; Ruta et al., 2010). These methods allow the extraction of the detailed anatomy of individual neurons. But even when used in combination with synaptic markers (NicolaiNicolaï et al., 2010; DiAntonio et al., 1993; Zhang et al., 2002; Fouquet et al., 2009), such methods do not offer definitive evidence of synaptic connections, as they rely solely on the proximity of putative pre- and post-synaptic compartments. Recently, promising trans-synaptic genetic tagging systems (Talay et al., 2017; Huang et al., 2017) have been developed to address some of these issues. However, none of these approaches provide any insight into the functional properties of potential connections. Despite such shortcomings, light-level microscopy constitutes a good starting point by constraining the search for possible connections within large populations of neurons —at the simplest level, if putative pre- and post-synaptic compartments do not overlap in light microscopy images, they cannot be in synaptic contact.

Electron microscopy (EM) reconstruction is considered to be the gold standard for connectomics (White et al., 1986; Briggman and Bock, 2012; Zheng et al., 2017; Schneider-Mizell et al., 2016). Under ideal conditions, it permits the unambiguous identification of synapses between all neurons in a given volume. As powerful as this capability is, the technique also suffers from a few limitations. Acquiring, processing and analyzing the data is still time-consuming. As a result, connectomes from EM data are typically based on data from a single animal. In addition, EM does not permit the identification of neurotransmitter types at a given synapse, nor does it detect gap-junctions in invertebrate tissue, at least at present (Zheng et al., 2017). Finally, it can be challenging to assess the strengths of connections between neurons, because it is not yet clear whether the number of synapses predicts the functional strength of the connection.

Functional methods address some of these drawbacks. Simple measures of activity have been used to assess a form of functional connectivity: regions or neurons whose simultaneously recorded activity is correlated—either spontaneously or during a given task—are deemed connected. This has been used with EEG, fMRI and MEG recordings in humans to establish maps at the brain region level (Salvador et al., 2005; Stam, 2004) and with multi-electrode recordings in monkeys and rodents (for example, [Gerhard et al., 2011]). Functional connectivity has also been inferred from correlations or graded changes in the response properties of neurons recorded in different animals, usually in cases where the neurons have overlapping arbors when examined with light microscopy. This approach has been employed to suggest polarized light processing pathways in the central complex of the locust and monarch butterfly (Heinze et al., 2009; Heinze, 2014). However, such functional methods are correlative and do not provide a causal basis for the inferred connectivity.

To obtain a causal description of functional connectivity—sometimes termed effective connectivity—it is necessary to either stimulate one node of the network while recording from another one, or record both at sufficiently high resolution as to detect hallmarks of direct connectivity. The most reliable approach of this class is paired patch-clamp recording, which identifies connected pairs and their functional properties with a high level of detail (Huang et al., 2010; Yaksi and Wilson, 2010; Fişek and Wilson, 2014), but can only be performed at low throughput (Jiang et al., 2015). In recent years, the development of optogenetics has expanded the toolkit for simultaneous stimulation and recording experiments (Petreanu et al., 2007). In Drosophila, the ease of use of genetic reagents renders such approaches particularly attractive. Combinations of P2X2 (a mammalian purinergic receptor that can be ectopically expressed in Drosophila and activated by ATP application) and the genetically encoded calcium indicator GCaMP (Yao et al., 2012), P2X2 and patch-clamp recordings (Hu et al., 2010), Channelrhodopsin-2 and patch-clamp (Gruntman and Turner, 2013), CsChrimson (a red shifted Channelrhodopsin) and CaMPARI (a calcium activity integrator, see [Fosque et al., 2015]) and CsChrimson and GCaMP (Hampel et al., 2015; Zhou et al., 2015; Ohyama et al., 2015) have been used in individual studies to investigate a small number of connections. Methods that rely on the genetic expression of calcium indicators to detect potential post-synaptic responses operate at a lower resolution than paired-recordings since they usually establish connectivity between cell types, as defined by the genetic driver lines used, rather than between individual neurons. These methods cannot definitively distinguish connections that are direct from those that might involve several synapses (but see Results/Discussion) and are limited by the sensitivity of the calcium sensors used. Despite these shortcomings, such methods constitute a good compromise as they provide a causal measure of functional connectivity at a much higher throughput than double patch recordings. It is also worth noting that the advantages and limitations of these techniques complement those of serial EM reconstructions. We chose to apply this combination of optogenetics and calcium imaging on a large scale by systematically testing genetically defined pairs of central complex cell types in an ex vivo preparation, therefore building a large and extensible map of functional connections in the structure at cell-type resolution.

### Cell types and hypothetical information flow in the central complex

![Figure 1.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig1-v2.jpg)

**Figure 1.:** (A) Schematic representation of the central complex and associated structures used throughout the manuscript. (B) (i) Hypothesized global information flow in the central complex based on neuron morphologies and the overlap of putative pre- and post-synaptic processes between different neuron types, based on Wolff et al. (2015) and Hanesch et al. (1989). (ii) Connectivity map based on the results of this study. Faded arrows represent hypotheses that were not tested in the present study.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Same as figure Figure 1, but with neuron type names underlying the connections indicated. (i) Hypothesized connections based on the anatomy described in Wolff et al. (2015) and Hanesch et al. (1989). (ii) Connectivity map based on the results of this study. Faded arrows and names represent hypotheses that were not tested in the present study.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Neuron types included in the study, grouped by super-type. P-EN1 and P-EN2 (Green et al., 2017) are drawn identically as they are almost indistinguishable based solely on anatomy. Note that each diagram represents a single neuron of the class. The driver lines selected contained most neurons of a given class. For columnar neuron classes, this meant that all or most columns were innervated.

The central complex consists of four main neuropiles — the protocerebral bridge (PB), the ellipsoid body (EB, Central Body Lower in other insects), the fan-shaped body (FB, Central Body Upper in other insects) and the noduli (NO) — and at least three accessory neuropiles (also known as the lateral complex) — the gall (GA), the lateral accessory lobe (LAL) and the bulbs (BU) (Figure 1A and [Wolff et al., 2015; Lin et al., 2013; Hanesch et al., 1989]). Throughout this manuscript, we denote output (resp. input) neurons that link central complex neuropiles to neuropiles outside the central complex. Some of the most striking neural elements of the central complex are the columnar neurons, which innervate one of the 18 (in Drosophila) glomeruli of the PB, one vertical section of either the FB or EB, and one accessory neuropile — a column being constituted by the PB glomeruli and FB/EB section. A total of 12 different columnar cell types have been described, with stereotypical correspondences between the PB glomerulus and the EB/FB section. In addition to these ‘principal cells’, there are a number of neurons innervating multiple columns of one neuropile. These neurons often innervate subdivisions orthogonal to the columns. Moreover, they sometimes also project to neuropiles outside the central complex. This set of neurons includes the ring neurons, which innervate a ring within the EB and an accessory neuropile, and a collection of inputs and interneurons with processes in the FB and PB. From this light level anatomy and putative synaptic polarity, one can derive a hypothetical picture of information flow through the central complex (Figure 1Bi):

We show that this overall flow of information is generally supported functionally for the parts we have tested so far, but with a few potentially important differences (Figure 1Bii): the observed connectivity in the PB is sparse, rendering the function of PB interneurons possibly critical; accessory structures are usually input rather than output areas; and, consequently, output channels of the central complex are scarce.

## Results

### A functional connectivity screen

We picked driver lines for functional connectivity mapping by visually inspecting the Janelia Gal4-driver collection (Jenett et al., 2012) for strength of expression in the cell types of interest, and sparseness of the expression pattern in the central complex. The 37 driver lines (for 24 cell types) cover the main columnar neuron types (8 of the 11 types described in Wolff et al. (2015)) and PB interneurons (3 out of the five in Wolff et al. (2015)), a LAL-FB neuron, three types of ring neurons, a Gall-EB neuron columnar in the EB and neurons innervating accessory structures, namely four types of LAL interneuron and three types of neurons connecting the LAL to the noduli. Drivers are listed in Table 1 and Table 2. Neuron types are schematized in Figure 2A and Figure 1—figure supplement 1. The dataset includes inputs to the EB system, connections between EB columnar neurons, connections in the PB as well as potential inputs and outputs in the LAL, Gall and noduli. Among the types tested, 43 of the 59 anatomically possible connections could be tested with the reagents available. The connectivity of the multitude of cell types within the FB has not been explored: neither FB interneurons (also known as pontine cells), nor FB input neurons are part of this study.

**Table 1.**
 Drivers and neuron types used.When the ‘Driver’ name is followed by an insertion site, it is a LexA line (see Materials and methods). Names starting by SS are stable splits. All other driver names correspond to both Gal4 (in attP2) and LexA (in attP40) drivers. ‘New Type Name’ refers to the nomenclature for short names adopted in this paper (following [Kakaria and de Bivort, 2017; Turner-Evans et al., 2017; Green et al., 2017]). Type description is the long name, following the guidelines of Wolff et al. (2015). Pre and post regions are labeled based on anatomical characteristics. The finer subdivisions were used to establish if two neurons were anatomically overlapping. The corresponding name in other insect species were determined using the insect brain database (https://insectbraindb.org/) and related papers (Heinze and Homberg, 2008; Heinze and Reppert, 2011b; Stone et al., 2017)


<table>
  <thead>
    <tr>
      <th>Driver</th>
      <th>New type name</th>
      <th>Type description</th>
      <th>Super type</th>
      <th>Name in other insects</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>87G07</td>
      <td>P-F3N2d</td>
      <td>PBG2-9.s-FBl3.b-NO2D.b</td>
      <td>FB columnar</td>
      <td>CPU4 (b or c)</td>
    </tr>
    <tr>
      <td>85H06</td>
      <td>P-F1N3</td>
      <td>PBG2-9.s-FBl1.b-NO3PM.b</td>
      <td>FB columnar</td>
      <td>CPU5</td>
    </tr>
    <tr>
      <td>60D05</td>
      <td>E-PG</td>
      <td>PBG1-8.b-EBw.s-DV_GA.b</td>
      <td>EB columnar</td>
      <td>CL1a</td>
    </tr>
    <tr>
      <td>SS02191</td>
      <td>P-EG</td>
      <td>PBG1-8.s-EBt.b-DV_GA.b</td>
      <td>EB columnar</td>
      <td>CL1b</td>
    </tr>
    <tr>
      <td>67D09</td>
      <td>P-F3N2v</td>
      <td>PBG2-9.s-FBl3.b-NO2V.b</td>
      <td>FB columnar</td>
      <td>CPU4(a)</td>
    </tr>
    <tr>
      <td>67D09-attP5</td>
      <td>P-F3N2v</td>
      <td>PBG2-9.s-FBl3.b-NO2V.b</td>
      <td>FB columnar</td>
      <td>CPU4(a)</td>
    </tr>
    <tr>
      <td>67D09-VK22</td>
      <td>P-F3N2v</td>
      <td>PBG2-9.s-FBl3.b-NO2V.b</td>
      <td>FB columnar</td>
      <td>CPU4(a)</td>
    </tr>
    <tr>
      <td>37F06</td>
      <td>P-EN1</td>
      <td>PBG2-9.s-EBt.b-NO1.b.Type1</td>
      <td>EB columnar</td>
      <td>CL2</td>
    </tr>
    <tr>
      <td>37F06-VK22</td>
      <td>P-EN1</td>
      <td>PBG2-9.s-EBt.b-NO1.b.Type1</td>
      <td>EB columnar</td>
      <td>CL2</td>
    </tr>
    <tr>
      <td>VT008135</td>
      <td>P-EN1</td>
      <td>PBG2-9.s-EBt.b-NO1.b.Type1</td>
      <td>EB columnar</td>
      <td>CL2</td>
    </tr>
    <tr>
      <td>SS02232</td>
      <td>P-EN2</td>
      <td>PBG2-9.s-EBt.b-NO1.b.Type2</td>
      <td>EB columnar</td>
      <td>CL2</td>
    </tr>
    <tr>
      <td>84H05</td>
      <td>PF-LCre</td>
      <td>PBG1-7.s-FBl2.s-LAL.b-cre.b</td>
      <td>FB columnar</td>
      <td>CPU1a</td>
    </tr>
    <tr>
      <td>84H05-VK22</td>
      <td>PF-LCre</td>
      <td>PBG1-7.s-FBl2.s-LAL.b-cre.b</td>
      <td>FB columnar</td>
      <td>CPU1a</td>
    </tr>
    <tr>
      <td>84H05-attP5</td>
      <td>PF-LCre</td>
      <td>PBG1-7.s-FBl2.s-LAL.b-cre.b</td>
      <td>FB columnar</td>
      <td>CPU1a</td>
    </tr>
    <tr>
      <td>55G08</td>
      <td>Δ7</td>
      <td>PB18.s-GxΔ7Gy.b-PB18.s-9i1i8c.b</td>
      <td>PB interneuron</td>
      <td>TB1</td>
    </tr>
    <tr>
      <td>55G08-attP5</td>
      <td>Δ7</td>
      <td>PB18.s-GxΔ7Gy.b-PB18.s-9i1i8c.b</td>
      <td>PB interneuron</td>
      <td>TB1</td>
    </tr>
    <tr>
      <td>55G08-VK22</td>
      <td>Δ7</td>
      <td>PB18.s-GxΔ7Gy.b-PB18.s-9i1i8c.b</td>
      <td>PB interneuron</td>
      <td>TB1</td>
    </tr>
    <tr>
      <td>47G08</td>
      <td>IS-P</td>
      <td>PBG2-9.b-IB.s.SPS.s</td>
      <td>PB input</td>
      <td></td>
    </tr>
    <tr>
      <td>49H05</td>
      <td>IMPL-F</td>
      <td>LAL.s-IMP-FBl3.b</td>
      <td>FB input</td>
      <td></td>
    </tr>
    <tr>
      <td>75H04</td>
      <td>L-Ei</td>
      <td>EBIRP I-O-LAL.s</td>
      <td>Ring neuron</td>
      <td>TL4</td>
    </tr>
    <tr>
      <td>32A11</td>
      <td>L-Em</td>
      <td>EBMRP I-O-LAL.s</td>
      <td>Ring neuron</td>
      <td>TL4</td>
    </tr>
    <tr>
      <td>18A05</td>
      <td>GB-Eo</td>
      <td>EBORP O-I-GA-Bulb</td>
      <td>Ring neuron</td>
      <td></td>
    </tr>
    <tr>
      <td>18A05-VK22</td>
      <td>GB-Eo</td>
      <td>EBORP O-I-GA-Bulb</td>
      <td>Ring neuron</td>
      <td></td>
    </tr>
    <tr>
      <td>17H12</td>
      <td>AMPG-E</td>
      <td>EB.w-AMP.d-D_GAsurround</td>
      <td>EB input</td>
      <td></td>
    </tr>
    <tr>
      <td>12C11</td>
      <td>EFBG</td>
      <td>EBMRA-FB-LT-LT-GA-GA</td>
      <td>Other</td>
      <td></td>
    </tr>
    <tr>
      <td>72H06</td>
      <td>SMPL-L</td>
      <td>SMP.s-LAL.s-LAL.b.contra</td>
      <td>LAL-IN</td>
      <td></td>
    </tr>
    <tr>
      <td>72H06-attP5</td>
      <td>SMPL-L</td>
      <td>SMP.s-LAL.s-LAL.b.contra</td>
      <td>LAL-IN</td>
      <td></td>
    </tr>
    <tr>
      <td>72H06-VK22</td>
      <td>SMPL-L</td>
      <td>SMP.s-LAL.s-LAL.b.contra</td>
      <td>LAL-IN</td>
      <td></td>
    </tr>
    <tr>
      <td>SS02615</td>
      <td>SMPL-L2</td>
      <td>SMP.s-LAL.s-LAL.b.contra2</td>
      <td>LAL-IN</td>
      <td></td>
    </tr>
    <tr>
      <td>26B07</td>
      <td>WL-L</td>
      <td>Wedge-LAL.s-LAL.b.contra</td>
      <td>LAL-IN</td>
      <td></td>
    </tr>
    <tr>
      <td>31A11</td>
      <td>L-Cre</td>
      <td>LAL-Cre</td>
      <td>LAL-IN</td>
      <td></td>
    </tr>
    <tr>
      <td>SS00153</td>
      <td>S-P</td>
      <td>SPS.s-PB.b</td>
      <td>PB input</td>
      <td></td>
    </tr>
    <tr>
      <td>76E11</td>
      <td>GL-N1</td>
      <td>LAL.s-GAi.s-NO1i.b</td>
      <td>LAL-NO</td>
      <td></td>
    </tr>
    <tr>
      <td>76E11-VK22</td>
      <td>GL-N1</td>
      <td>LAL.s-GAi.s-NO1i.b</td>
      <td>LAL-NO</td>
      <td></td>
    </tr>
    <tr>
      <td>SS04448</td>
      <td>GL-N1</td>
      <td>LAL.s-GAi.s-NO1i.b</td>
      <td>LAL-NO</td>
      <td></td>
    </tr>
    <tr>
      <td>SS04420</td>
      <td>CreL-N2</td>
      <td>Cre.s-LAL.s-NO2.b</td>
      <td>LAL-NO</td>
      <td>TN1 ?</td>
    </tr>
    <tr>
      <td>12G04</td>
      <td>L-N3</td>
      <td>LAL.s-NO3Ai.b</td>
      <td>LAL-NO</td>
      <td>TN1 ?</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Number of cells per hemisphere and PB column (when relevant) in the drivers used in this study, as estimated by counting cell bodies in confocal stacks.When counting was difficult (e.g. because of densely packed somata) we indicated this by a $∼$ sign.


<table>
  <thead>
    <tr>
      <th>Driver</th>
      <th>New type name</th>
      <th>Cells per hemisphere</th>
      <th>Cells per column</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>87G07</td>
      <td>P-F3N2d</td>
      <td>16</td>
      <td>2</td>
    </tr>
    <tr>
      <td>85H06</td>
      <td>P-F1N3</td>
      <td>32</td>
      <td>4</td>
    </tr>
    <tr>
      <td>60D05</td>
      <td>E-PG</td>
      <td>24</td>
      <td>3</td>
    </tr>
    <tr>
      <td>SS02191</td>
      <td>P-EG</td>
      <td>16</td>
      <td>2</td>
    </tr>
    <tr>
      <td>67D09</td>
      <td>P-F3N2v</td>
      <td>24</td>
      <td>3</td>
    </tr>
    <tr>
      <td>37F06</td>
      <td>P-EN1</td>
      <td>24</td>
      <td>3</td>
    </tr>
    <tr>
      <td>VT008135</td>
      <td>P-EN1</td>
      <td>24</td>
      <td>3</td>
    </tr>
    <tr>
      <td>SS02232</td>
      <td>P-EN2</td>
      <td>16</td>
      <td>2</td>
    </tr>
    <tr>
      <td>84H05</td>
      <td>PF-LCre</td>
      <td>7</td>
      <td>1</td>
    </tr>
    <tr>
      <td>55G08</td>
      <td>Δ7</td>
      <td>16</td>
      <td></td>
    </tr>
    <tr>
      <td>47G08</td>
      <td>IS-P</td>
      <td>12</td>
      <td></td>
    </tr>
    <tr>
      <td>49H05</td>
      <td>IMPL-F</td>
      <td>4</td>
      <td></td>
    </tr>
    <tr>
      <td>75H04</td>
      <td>L-Ei</td>
      <td>∼30</td>
      <td></td>
    </tr>
    <tr>
      <td>32A11</td>
      <td>L-Em</td>
      <td>∼24</td>
      <td></td>
    </tr>
    <tr>
      <td>18A05</td>
      <td>GB-Eo</td>
      <td>2</td>
      <td></td>
    </tr>
    <tr>
      <td>17H12</td>
      <td>AMPG-E</td>
      <td>∼12</td>
      <td></td>
    </tr>
    <tr>
      <td>12C11</td>
      <td>EFBG</td>
      <td>9</td>
      <td></td>
    </tr>
    <tr>
      <td>72H06</td>
      <td>SMPL-L</td>
      <td>∼12</td>
      <td></td>
    </tr>
    <tr>
      <td>SS02615</td>
      <td>SMPL-L2</td>
      <td>∼12</td>
      <td></td>
    </tr>
    <tr>
      <td>26B07</td>
      <td>WL-L</td>
      <td>2</td>
      <td></td>
    </tr>
    <tr>
      <td>31A11</td>
      <td>L-Cre</td>
      <td>2</td>
      <td></td>
    </tr>
    <tr>
      <td>SS00153</td>
      <td>S-P</td>
      <td>2</td>
      <td></td>
    </tr>
    <tr>
      <td>76E11</td>
      <td>GL-N1</td>
      <td>2</td>
      <td></td>
    </tr>
    <tr>
      <td>SS04448</td>
      <td>GL-N1</td>
      <td>2</td>
      <td></td>
    </tr>
    <tr>
      <td>SS04420</td>
      <td>CreL-N2</td>
      <td>2</td>
      <td></td>
    </tr>
    <tr>
      <td>12G04</td>
      <td>L-N3</td>
      <td>2</td>
      <td></td>
    </tr>
  </tbody>
</table>

![Figure 2.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig2-v2.jpg)

**Figure 2.:** (A) Schematics of a subset of the neurons considered for the screen. The example neurons shown in B, C and D are indicated by blue and orange dotted-line boxes. (B) For each potential neuronal pair, driver lines with clean expression in the central complex were selected — the boxes delineate the approximate position of the neurons of interest in the brain. (C) To determine if a given pair is a promising candidate, we examined the degree of overlap between putative pre- and post-synaptic regions in the expression patterns in anatomy images registered to a common brain template. If the candidate pre- and post-synaptic regions overlapped (as indicated by the blue ellipse), we expressed CsChrimson in the presynaptic candidate and GCaMP6m in the postsynaptic candidate, and then imaged the ex-vivo brain in a two-photon laser scanning microscope while optogenetically stimulating the candidate presynaptic population (D). We selected the region imaged based on proximity to the overlapping processes, but ensured that it contained only GCaMP expressing arbors (yellow ellipse in C, and box in D).

Cell-type pairs to be tested were chosen based on overlaps between their expression patterns in light microscopy images. For each combination selected, we expressed CsChrimson and GCaMP6m in potential pre- and post-synaptic partners, respectively (Figure 2B,C), and probed their connection in an ex vivo preparation using a standardized protocol (see Figure 2D, and Materials and methods). Whenever large responses were observed, we used pharmacology to both check that observed transients were synaptically mediated, and to narrow down the neurotransmitters involved (Figure 4—figure supplement 2 and Figure 4—figure supplement 3).

Effects of stimulation ranged from very large and reliable transients (Figure 3Ai) to undetectable changes (Figure 3Aiii). In between those extremes, we observed transients of variable size and reliability (Figure 3B). To our surprise, we could also detect clear inhibitory responses (Figure 3Aii). This was possible because—at least in some cell types—fluctuations in baseline activity occasionally elevated GCaMP levels during the experiment (see Discussion and Figure 3—figure supplement 3). Therefore, even though hyperpolarization below resting potential is likely not detectable through calcium imaging, we could detect inhibition from an excited state as a dip in the fluorescence trace.

![Figure 3.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig3-v2.jpg)

**Figure 3.:** (A and B) Summary of different response types. Stimulation is indicated by the gray bar and consists of 20 light pulses (50 μW/mm2, each of 2 ms duration) delivered at 30 Hz. (A) Example neuron pairs, easily interpretable responses. (B) Example neuron pairs, responses that are more difficult to interpret. In A and B, all responses, expressed as $ΔF/F_{0}$, are baseline subtracted except for the inhibitory response in Aii. Scale bar 2 s. Grey dashed boxes show the region of overlap between the two patterns, and yellow boxes indicate the area that was generally imaged for the pairs shown. (C) Example of statistics computed on individual runs and cell pairs characterizing: (i) average response shape, (ii) reliability of the response, and (iii) response sensitivity. (D) Using the distribution of statistics from non-overlapping controls to assign classes to the responses: distributions of response amplitudes and reliability as measured by the scaled normalized integral (the median of the integral normalized to the baseline and scaled so that the dataset spans the [−1,1] range) and the between-flies correlation (see Materials and methods). Each point corresponds to a different cell pair (median statistics across flies). Control unconnected pairs are shown in blue, and self-activation (CsChrimson and GCaMP6m expressed in the same neuron type) in orange. Responses considered significantly different from the control sample (p<0.01, see Materials and methods) are circled.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Responses of non-overlapping pairs. Each line corresponds to a fly (six flies per pair), each panel to a cell pair tested. Note that when responses are present, they are either unreliable or small, and likely reflect effects of indirect connections.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Distributions of statistics computed for non-overlapping, overlapping and self-activation pairs. All statistics are the median per pair of per run statistics. Integral: the integral of the response (from the onset of stimulation to the time of the peak of the response), in $ΔF/F_{0}$s. Normalized integral: Integral divided by the baseline fluorescence. Scaled normalized integral: the normalized integral divided by the maximum (minimum for inhibitory responses) normalized integral measured. Peak fluorescence: the maximum (minimum for inhibitory responses) of the fluorescent transient $ΔF/F_{0}$. Normalized peak: the peak fluorescence divided by the baseline fluorescence. Decay half time: the time in seconds between the peak of the response to the moment where the fluorescence reaches half the level of the peak (relative to the baseline). Rise time: the time of the peak fluorescence (in seconds). Repeat to repeat correlations: the average correlation between several repeats of the same experiment (in the same fly). Correlations between experiments: the average correlation between experimental runs of the same pair but from different flies. Integral to baseline correlation: the correlation between the integral and the value of the baseline fluorescence.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Spread of fluorescence baseline, effect on the responses. (A) Distribution of baseline fluorescence for each cell pair tested. Pairs are colored according to the ‘anatomical’ class they belong to (overlapping, non-overlapping and self-activation). (B) Same as A, but pooled by class and rendered as a violin plot. (C) Correlations between the signed response distance and the baseline fluorescence intensity of significantly responding pairs. Inhibitory responses are (as expected) correlated, but excitatory pairs also show a mild correlation. (D) Example of distance to baseline relationship in four pairs. (i) PF-LCre to SMPL-L, corresponding to Figure 3Ai. (ii) GL-N1 to P-EN1, corresponding to Figure 3Aii. (iii) GL-N1 to L-Ei, corresponding to Figure 3Aiii. (iv) PF-LCre to PF-LCre.

Since no single characteristic of the responses could adequately capture their variety, variability and complexity, we chose to characterize the transients by using a battery of statistics reflecting response amplitude, shape, reliability and stimulus sensitivity (see Figure 3C, Figure 3—figure supplement 2, and Materials and methods). Responses of control pairs with non-overlapping processes were then used to form the null-hypothesis distributions of two metrics that capture response amplitude and reliability (see Figure 3D). For every data point, the Mahalanobis distance (a covariance corrected measure in a multidimensional space, see Materials and methods) to the null distribution was computed and used as a connection strength metric in summary diagrams like Figure 4 and Figure 5. Non-overlapping pairs usually showed no fluctuations upon stimulation, and when they did, they were small and unreliable (see Figure 3—figure supplement 1), likely reflecting effects of indirect connections. Not surprisingly, responses were always detected with same-cell-type-stimulation controls, where CsChrimson and GCaMP6m were expressed in the same neuron type (see Figure 3D).

![Figure 4.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig4-v2.jpg)

**Figure 4.:** Solid lines indicate anatomically overlapping cell pairs, whereas dotted lines correspond to the non-overlapping controls. The thickness of the lines maps to the functional connection strength. The reliability of the responses as measured by the between-flies correlations is mapped to the transparency of the connectors. Connection strengths are quantified in terms of the Mahalanobis distance to the null sample and the sign of the response integral, which is normalized to the maximum response. Three tested cell types (SMP-L2, L-Cre and EFBG) are not shown here for clarity, as tests with a few different partners did not produce significant results.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Matrix representation of the connectivity results. Dots denote anatomically overlapping pairs. The dashed diagonal correspond to self-activation (when the same cell expresses CsChrimson and GCaMP6m). Connection strengths are quantified in terms of the Mahalanobis distance to the null sample and the sign of the response integral, which is normalized to the maximum response.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** For each cell pair, plots in the right column correspond to average traces (+-s.e.m.) at three time points during drug application: before (in blue, 4 min preceding drug application), during (in purple 6 to 11 min after starting drug application) and after (in turquoise, last two runs of the experiment). Plots in the left column show the response integral as a function of time to/from drug application. Each line corresponds to a fly. Timespans corresponding to the plots on the right are shaded accordingly. The dashed vertical line corresponds to the time at which the drug perfusion was turned on. Cell pairs are grouped based on the presynaptic cell type tested (Columnar neurons,IS-P neuron and Others).

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Plots similar to Figure 4—figure supplement 2 for picrotoxin applications, except that experiments are now grouped based on the type of test that was run. ‘Inhibitory pairs’ show the straightforward assessment of inhibitory connections. Unmasking controls’ refers to attempts to uncover excitatory effects that might have been masked by global inhibition. Note that picrotoxin applications usually produce an increase in the baseline activity of the neuron, and hence an increase in the inhibitory driving force, which partially balances the transmission block.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** Dose responses. Thin lines correspond to median normalized scaled integrals of individual cell pairs. Cell pairs are grouped according to the class of their response (significantly excitatory/inhibitory or not significantly different from the controls). Note that both excitatory and inhibitory responses tend to saturate at 20 pulses.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig4-figsupp5-v2.jpg)

**Figure 4—figure supplement 5.:** Responses of pairs for which several genotypes were tested.

![Figure 5.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig5-v2.jpg)

**Figure 5.:** (A) Input channels. (i) Ring neurons provide inhibitory input to the E-PGs in the EB. (ii) GL-N1 inhibits P-EN neurons. (iii) Distributed excitatory input from IS-P neurons in the PB. (B) $Δ$7 is probably the bottleneck in PB motifs, as it is the only strong post-synaptic target of E-PG neurons and relays information to other columnar neurons. (C) The only output pair found so far connects the PF-LCre neuron to a LAL interneuron. (D) Recurrence in the central complex. (i) at the input stage, and (ii) within the EB columnar system.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/37017/elife-37017-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Various response types following $Δ$7 stimulation.A: $Δ$7 to P-F3N2v, inhibitory. B: $Δ$7 to P-EN1, excitatory. C: $Δ$7 to E-PG, mixed responses. (i) to (iv) correspond to 5, 10, 20 and 30 pulses stimulation protocol. Each line is the average response for one fly (four runs per fly).

All the individual responses and statistics, in the context of the overall connectivity diagram, are available at http://romainfr.github.io/CX-Functional-Website/romainfr.github.io/CX-Functional-Website/, a website that enables an interactive exploration of the results of this study. We plan to update this website as further experiments are performed. The website can also be expanded to accommodate other sources of data, which would make it an exhaustive source of information about the central complex. The connectivity matrix resulting from our experiments is shown in Figure 4 in two alternative visualizations, namely a network diagram (Figure 4) and a matrix of connection strengths.

### An emerging view of the central complex functional connectome

Figure 5 outlines some of the connectivity patterns we observed. We focus in particular on inputs and outputs to the ellipsoid body, protocerebral bridge and paired noduli, connectivity within the protocerebral bridge, and components of the ring attractor network within the central complex.

#### Inputs

We identified two classes of inhibitory, picrotoxin-sensitive (hence mediated either by GABA-A or Glutamate) inputs to the central complex. First, the two ring neuron types we tested (GB-Eo, L-Ei) target the wedge columnar neurons (E-PG, Figure 5Ai), as has been suggested previously (Martín-Peña et al., 2014; Kahsai et al., 2012; Hanesch et al., 1989). Note that the ring neurons presented here are non-canonical: they innervate the LAL or the Gall, but not the bulb. Second, a class of LAL-NO interneurons (the GL-N1 neuron) provides another source of inhibitory input into the EB columnar system by targeting the P-EN neurons (Figure 5Aii and Figure 3Aii). This connection is particularly interesting in the light of the finding that the P-EN neurons drive the rotation of the bump of activity in the heading representation system (Green et al., 2017; Turner-Evans et al., 2017). Since the left/right noduli segregation corresponds to individual cells coding turns in opposite direction (Turner-Evans et al., 2017), the GL-N1 neurons are likely involved in strengthening or refining those turn related signals. Moreover, it is likely that other types of LAL-NO interneurons innervating other noduli compartments target P-FN neurons, but these pairs have not been tested extensively yet.

We also identified two excitatory inputs to the central complex. First, a Gall to EB neuron, whose innervation pattern in the EB is reminiscent of the columnar neurons, excites the E-PG neurons (the same class that carries the heading representation and is inhibited by ring neurons). Second, several columnar neurons share excitatory inputs from the IS-P neuron in the PB (PB.b-IB.s-SPS.s, Figure 5Aiii). It is important to note that although we tested very few candidates in the FB, it is highly likely that this region receives many inputs from outside the central complex.

The neurons listed here do not necessarily provide feed-forward input from outside the central complex. For example, the gall ring neuron (GB-Eo), which is an inhibitory input to the E-PGs, likely participates in a feedback loop, as it receives excitatory input from P-EG neurons (Figure 5Di). It is possible that this kind of loop between the columnar system and input neurons from accessory structures is repeated at other places in the network. Another example would be the IMPL-F neuron, the FB-LAL neuron (top right corner of Figure 4) that receives input from the PF-LCre columnar neuron in the LAL. Its target in the central complex has not been identified so far, but since it is located in the FB, it likely involves the FB columnar system.

#### Outputs

In contrast with inputs, we found few potential channels leaving the central complex. The only output pathway identified in this dataset is presented in Figure 5C, and connects the PF-LCre columnar neuron to a LAL interneuron through a strong, mecamylamine-sensitive (hence cholinergic, see Materials and methods), excitatory connection (see Figure 3Ai and Figure 4—figure supplement 2 for the pharmacology). This information is likely further processed in the LAL, as we found indications of inhibition upon PF-LCre stimulation in another LAL interneuron (WL-L). Even if we could not trace the circuit responsible for this inhibition, it likely involves an intermediate interneuron in the LAL. Once again, as this dataset does not include every single cell type of the central complex, some outputs might easily have been missed. FB tangential neurons (Hanesch et al., 1989), for example, may also contribute output pathways.

#### Connectivity in the protocerebral bridge

A functional connectome is, by construction, sparser than can be predicted by light-level anatomy. Our study shows this most clearly in one neuropil, the PB (Figure 5B). E-PG neurons are the only columnar type that are presynaptic in the PB, but their activation did not trigger a significant response in any of the five other columnar neurons we tested. This came as a surprise because we assumed that the E-PG population would connect to the rest of the EB and FB columnar systems. To verify that this lack of observed connectivity was not due to the recruitment of global inhibitory circuits, we also ran these experiments in the presence of picrotoxin, and did not observe any difference in responses (see Figure 4—figure supplement 3). By contrast, the $Δ$7 interneurons are strongly activated by E-PG neurons, and their activation leads to significant responses in several columnar neuron types (E-PG, P-EN1, P-EN2, P-F1N3 and P-F3N2v). The $Δ$7 neurons, therefore, appear to constitute an important bottleneck in the system (Figure 5B), and may serve as the only strong link between columnar neurons in the PB. The response profiles following $Δ$7 activation are also unusually complex (see Figure 5—figure supplement 1): P-ENs display mild activation, E-PG and P-F3N2v inhibition, and P-F1N3 strong rebound excitation (see Figure 3Biii).

### Connectivity in the EB columnar system, the ring attractor network

Figure 5Dii shows the subpart of the network that has been proposed to sustain the ring attractor representation of heading (Green et al., 2017; Turner-Evans et al., 2017). One hypothesized feature of such a circuit is a large degree of recurrence between the different EB columnar types. In particular, P-EN to E-PG reciprocal connections are important for models of the rotation of the bump. While we found strong support for the P-EN1 to E-PG connection, the E-PG to P-EN1 connection that we reported functionally under a stronger stimulation protocol (Turner-Evans et al., 2017) may be mediated through the $Δ$7 interneurons. A few other connections were found in the EB (for example, P-EN1 to P-EN2), but it is important to stress that not all combinations could be tested due to limitations in the genetic reagents available. For example, the role of the P-EG neurons in this circuit, remains unclear. A key additional type that our results suggest may contribute in important ways to the persistence of activity in this circuit is the AMPG-E neuron, a columnar Gall-EB neuron not innervating the PB, which appears to provide localized excitatory feedback to the E-PG neurons.

## Discussion

The dataset presented in this study constitutes a resource for the growing community of researchers interested in the central complex. While similar coarse functional connectivity techniques have been used to map short pathways in previous studies, this is, to our knowledge, the first extensive dataset of its kind. We hope that it will become an evolving source of information, which we expect to be most useful when combined with other complementary data sources, such as EM-level anatomical connectivity and high-resolution gene expression profiles. Such combined data would constitute a solid base to build constrained network models of the central complex, and to generate detailed hypotheses of its function. As with any large dataset, we see this effort mainly as a starting point for more detailed research.

### Limitations of the method

The connectivity technique we applied has several limitations that are important to keep in mind. First, connections detected using CsChrimson and GCaMP cannot be guaranteed to be direct and monosynaptic. However, the large set of controls with cell-type pairs whose processes do not overlap provides a statistical framework to interpret the results — not surprisingly, uncertainty is highest for weak connections. We believe that the metric we used to assess connectivity – distance to a control set rather than just response strength – makes the resulting network more interpretable. Additionally, by releasing the entire dataset rather than just the derived network, we hope to provide interested central complex researchers the opportunity to explore the data and to potentially reinterpret it in the light of other findings.

A more fundamental issue concerns the sensitivity of our protocol, which is limited by the stimulation protocol and the sensitivity of GCaMP6m. Specifically, an absence of a post-synaptic response cannot be interpreted as an absence of a connection. The fact that some inhibitory responses are visible, and that strong responses saturate with the range of stimulations used (see Figure 4—figure supplement 4) is reassuring. However, it is likely that EM reconstructions of central complex circuits will reveal that some weak synaptic connections have been missed by our technique. Their functional importance will need to be investigated using more sensitive methods, for example, intracellular electrophysiology. For example, we may be underestimating the level of connectivity in the PB: our finding of sparseness in the structure should thus be interpreted as sparseness at the resolution of our technique, because this network may be dominated by weak connections below our detection threshold.

Further, we relied on full-field stimulation of populations of specific neuronal types, which comes with its own drawbacks: this approach provides no access to connectivity between neurons of the same class, and does not account for potential non-physiological network effects. One such effect would be the recruitment of global inhibitory networks that could mask an otherwise excitatory connection. However, whenever we suspected this could be a possibility, we controlled for it by blocking inhibition with picrotoxin, and never saw evidence of a significant effect (Figure 4—figure supplement 3). Even though picrotoxin was effective in blocking the inhibitory responses we observed when activating ring neurons or $Δ$7 neurons (Figure 4—figure supplement 3), we cannot exclude the possibility that picrotoxin-insensitive inhibition might be present in the network. Possible candidates mediating such effect would be GABA-B (Olsen and Wilson, 2008), metabotropic glutamatergic or peptidergic transmission (Kahsai and Winther, 2011). For example, the PB shows both GABA-B and metabotropic glutamatergic receptor immunoreactivity (Kahsai et al., 2012), which could make the observed connectivity seem sparser than it actually is. Interestingly, whereas in other insect species the PB displays peptidergic immunoreactivity (in particular Allatostatin-A, see[Vitzthum et al., 1996]), this seems not to be the case in Drosophila (with the exception of SIFamide, see [Kahsai et al., 2012]).

The fact that we stimulate entire presynaptic populations also means that the strength of connections we report is influenced both by neuron-to-neuron transmission strength and the degree of convergence in the network. Caution should therefore be exercised when comparing connections between columnar neuron population and other types (e.g. from PF-L and SMPL-L or P-EG to G-Eo), which are potentially highly convergent, to connections between columnar neuron types, or from accessory structure neuron types to columnar populations (like GL-N1 to P-EN1), which are both mediated by a single or small handful of presynaptic neurons for any given post-synaptic neuron. Furthermore, even though several of the neurons described have complex morphologies that are suggestive of local processing within specific neuropiles, we never found neuropile-specific responses: when a neuron responded, the response seemed to invade the entire neuron. This may be the result of our broad and artificial stimulation protocol.

Given that our protocol is limited to the activation of one cell type, we might also have missed connections gated by other inputs. For example, we failed to find any PB input for the PF-LCre neurons – the sole output neurons we identified in this study. It is possible that this neuron requires convergent inputs from the PB and FB to be activated, as was suggested in (Stone et al., 2017).

Finally, all our experiments were performed in ex vivo brain preparations. Given the variety of neuromodulators that operate in the central complex (Kahsai and Winther, 2011), it is likely that functional connectivity within this region is modulated by brain state (Homberg, 1994; Seelig and Jayaraman, 2013; Weir et al., 2014; Weir and Dickinson, 2015). Consistent with this possibility, we saw that the fluorescence baseline tended to fluctuate spontaneously during the course of our experiments in most types recorded (as shown in Figure 3—figure supplement 3A). Two neuron types had relatively small baseline fluctuations that could have make it difficult to detect inhibition when those were used as post-synaptic targets: P-EG and PF-LCre. Intriguingly, although increases in baseline activity allowed us to detect inhibitory responses, we noticed that excitatory responses also occasionally depended on this baseline fluctuation (Figure 3—figure supplement 3C). It is conceivable that such baseline fluctuations reflect a kind of artificial brain state upon which the response amplitudes depend.

### Potential neurotransmitters

From our pharmacology experiments, we propose that columnar neurons and IS-P neurons are likely cholinergic (see Figure 4—figure supplement 2), whereas the LAL and Gall ring neurons, as well as the $Δ$7 neurons are either glutamatergic or GABAergic (see Figure 4—figure supplement 3). A large fraction of ‘canonical’ BU-ring neurons have been shown previously to be GABAergic (Zhang et al., 2013), which makes this likely for the LAL and Gall-ring neurons described here. We argue below that the response profiles of $Δ$7 neurons suggests that they are glutamatergic, in accordance with (Daniels et al., 2008).

### Central complex motifs

The connectivity matrix we obtained is sparser than that predicted by light level anatomy. Our results suggest that the $Δ$7 interneurons are a bottleneck for information processing in the PB. This is all the more interesting given the range of responses evoked by $Δ$7 stimulation (Figure 5—figure supplement 1). Properties of the synapses that $Δ$7 neurons make with their post-synaptic partners may play a primary role in the way that a heading signal is generated and maintained in the EB columnar system, and also in how it may be transferred to the FB columnar system. This has also been suggested in other insect species (Stone et al., 2017) for the homologous TB1 neuron, which was a key component of the proposed compass circuit model in that study. Every $Δ$7 neuron innervates all columns of the PB, and has presynaptic-looking processes in two columns. The fact that a neuron with such extensive arbors participates in a circuit where representations are spatially restricted (heading-related activity is limited to a few neighboring columns at any given time) suggests that understanding local processing at the single neuron level might be critical to a complete understanding of how the circuit as a whole operates. This may also be the case for some of the ring neurons that provide input to the ellipsoid body.

The observation that $Δ$7 neuron stimulation can excite or inhibit its post-synaptic partners can have several explanations. Either the population of $Δ$7 is not homogeneous, and contain several functionally distinct types responsible for the different types, or the responses reflect a variety of receptors on the post-synaptic side. This latter hypothesis would be compatible with the previously discussed hypothesis that $Δ$7 are glutamatergic, as the diversity of ionotropic and metabotropic glutamate receptors would allow such response diversity.

The fact that several sources of input are inhibitory raises the question of how activity is maintained in the region. Candidate mechanisms are the uncovered excitatory inputs into the PB and EB, recurrent connections in the EB and intrinsic properties of neurons (Egorov et al., 2002; Yoshida and Hasselmo, 2009; Russell and Hartline, 1982) — some cell types, for example, showed robust post-stimulation rebounds (see Figure 3Bii). It is also possible that our selection of cell types and our methods missed some sources of excitation.

The range of inputs revealed here opens many avenues for investigation. Whereas some ring neuron subtypes have received considerable attention (Sun et al., 2017; Shiozaki and Kazama, 2017; Seelig and Jayaraman, 2013), most PB inputs and LAL-noduli interneurons have not yet been characterized. A recent study in the sweat bee (Stone et al., 2017), for example, reported that one of the LAL-noduli interneurons — a likely input to the FB system — carries forward and backward translational optic flow signals. This is all the more interesting given that we show that one of the LAL-NO interneuron types (GL-N1) provides input to the P-EN neurons, known to encode rotational signals (Turner-Evans et al., 2017; Green et al., 2017).

The specific functions subserved by the network motifs that we have uncovered may only become clear with functional studies in behaving animals. A key puzzle set up by our findings is the small number of output channels of the central complex. Our results are consistent with the LAL being the primary output structure for the central complex (Chiang et al., 2011; Hanesch et al., 1989), although the structure also acts as an input region (via ring neurons and potentially via IMPF-L neurons). While it is possible that our selection of Gal4 lines was unintentionally biased against output neurons, or that our technique otherwise missed a number of output pathways, the picture of the central complex that emerges is of a densely recurrent sensorimotor hub with relatively low dimensional output (much as proposed by some models for example [Stone et al., 2017; Fiore et al., 2015; Strauss and Berg, 2010]). The implications of this bottleneck for motor control remains a challenge for future studies to resolve.

## Materials and methods

### Fly stocks and crosses

Drivers were chosen based on relatively sparse expression within the central complex. For any given pair of neurons, the overlap between pre- and post-synaptic looking regions was assessed based on publicly available expression patterns ([Tirian and Dickson, 2017; Jenett et al., 2012], see Figure 1—figure supplement 1) digitally aligned on a common reference brain (as described in [Aso et al., 2014]). For every LexA driver used, we prepared two stocks containing GCaMP6m (Chen et al., 2013) and CsChrimson (Klapoetke et al., 2014) under LexAop (resp. UAS) or UAS (resp. LexAop) control: XXX-LexA;13XLexAop2-IVS-p10-GCaMP6m 50.629 in VK00005, 20xUAS-CsChrimson-mCherry-trafficked in us(How)attP1 and XXX-LexA;20xUAS-IVS-GCaMP6m 15.629 in attP2, 13XLexAop2-CsChrimson-tdTomato in VK00005. Those stocks were then crossed to a Gal4 driver or a split-Gal4 (Luan et al., 2006) driver for the experiment. For split-Gal4s, the two split halves were inserted in attP40 and attP2 respectively. To avoid transection between the split and the LexA driver (Mellert and Truman, 2012), we inserted the LexA drivers in alternative sites, either su(Hw)attP5 (Pfeiffer et al., 2010) or VK22 (Venken et al., 2006), and used the splits exclusively in combination with those lines after checking their expression patterns. The list of drivers used and the corresponding cell types are given in Table 1. Throughout this paper, we follow the naming convention set out in Wolff et al. (2015) for full names, and the scheme described in Kakaria and de Bivort (2017) and used in Green et al., (2017) and Turner-Evans et al., (2017) for abbreviations. For each cell type, we labeled every region innervated as presynaptic or postsynaptic (or both): this was done at the resolution of the glomerulus for the PB, the layer for the FB and the individual nodulus. We divided the LAL into three zones based on the overlap between the lines used. Existing subdivisions for the EB and Gall were preserved. This labeling was used to evaluate whether the arbors of a given cell-type-pair overlapped.

### Dissections

The brains of 5 to 9 days old female flies were extracted and laid on a poly-D-lysine coated coverslip (Corning, Corning, NY). In most experiments, both the brain and the ventral nerve chord (VNC) were dissected out, as we found that having the VNC attached to the brain increased the mechanical stability of the preparation. Dissection was performed using the minimum level of illumination possible to avoid spurious activation of CsChrimson. The preparation was bathed throughout in saline containing (in mM): 103 NaCl, 3 KCl, 5 TES, 8 trehalose dihydrate, 10 glucose, 26 NaHCO3, 1 NaH2PO4, 2 CaCl2, 4 MgCl2, bubbled with carbogen (95% O2, 5% CO2). Brains were positioned anterior-side-up, except when the connection tested was thought to be in the PB, in which case they were positioned posterior-side-up to maximize light access close to the assumed synaptic site. Trachea were removed. Only for experiments involving pharmacology, the glial sheath was gently torn with tweezers to enhance drug access to the neuropiles.

### Imaging conditions and trial structure

Imaging was performed on an Ultima II two-photon scanning microscope (Bruker, Billerica, MA) with a Vision II laser (Coherent, Santa Clara, CA). Brains were continuously perfused in the saline used for dissection at 60 mL/hr. Once the sample was placed and centered under the objective, we waited 5 min before starting the experiment to avoid any lingering network activation from the dissection or transmission lights. Two-photon excitation wavelength was 920 nm, and power at the sample varied between 3 and 10 mW. CsChrimson was excited with trains of 2 ms long 590 nm light pulses via an LED (M590L3-C1, Thorlabs, Newton, NJ) shone through the objective. The excitation light path contained a 605/55 nm bandpass filter and was delivered to the objective with a custom dichroic (zt488-568tpc, reflecting between 568 nm and 700 nm). A 575 nm dichroic beam splitter and bandpass filters (525/70 nm and 607/45 nm for the green and red respectively) were placed in the detection arm before photons reached the PMTs (Hamamatsu multi-alkali). Instantaneous power measured out of the objective was roughly 50 μW/mm2. Stimulus pulse trains were delivered at 30 Hz and the number of pulses varied between 1, 5, 10, 20 and 30 — corresponding to total stimulation durations ranging from 2 ms to 1 s. Imaging fields of view were chosen as to avoid scanning regions containing CsChrimson-expressing neuropil while being as close as possible to the putative connection site, as we observed occasional two-photon-evoked slow activation of CsChrimson-expressing cells (high-intensity two-photon stimulation of CsChrimson was used for spatially precise neuronal activation in [Kim et al., 2017]). When this was impossible — for example, in self-activation controls or for completely overlapping cell types — we chose a large ROI of which the CsChrimson/GCaMP6m-expressing neuropile represented a small fraction, so as to minimize duty cycle. ROIs were kept constant throughout the experiment. Each experimental run consisted of four repeats, each approximately 16s long. Runs were themselves repeated every 2 min. All experiments started with five runs corresponding to the five stimulation strengths, in a random order. This was sometimes followed by pharmacological testing. At the end of the experiment, a high intensity 3D stack was acquired to check that the expression patterns were as expected, and that the neutrophil imaged was the targeted one in cases where fluorescence levels during the experiments were very low. At least six flies were tested for every pair considered.

### Pharmacology

For blocking nicotinergic or inhibitory (GABAergic or glutamatergic) transmission, mecamylamine (50 μM) or picrotoxin (10 μM) (Sigma-Aldrich, St Louis, MO) were perfused by switching to a different line for 3 min, followed by a wash period during which the perfusion was drug-free again. Thirty pulses stimulation runs were repeated every 2 min, starting 4 min before the drug application and throughout the wash. Prior to use, solutions were kept frozen in 25 mM and 0.3 M aliquots, respectively.

### Analysis

All analyses were performed in http://julialang.org/Julia, using custom-written routines. All data and code are available as an OpenScienceFramework project at https://osf.io/vsa3z/ (Franconville, 2018a). Code is also centralized in a Github repository ([Franconville, 2018b], https://github.com/romainFr/CX-Functional-Analysis; copy archived at https://github.com/elifesciences-publications/CX-Functional-Analysis) and notebooks recapitulating the analysis can be run directly from the browser at https://mybinder.org/v2/gh/romainFr/CX-Functional-Analysis/master (using https://mybinder.org/Binder).

#### Data processing

For a given experiment, all movies were aligned to each other to compensate for slow drifts of the sample: for each run, the average image was calculated, and translation drifts between average images were calculated using correlation-based sub-pixel registration ([Guizar-Sicairos et al., 2008], and https://github.com/romainFr/SubpixelRegistration.jl for the Julia implementation used here; copy archived at https://github.com/elifesciences-publications/SubpixelRegistration.jl). A region of interest (ROI) was defined for the full experiment: the average image (of all the runs) between foreground and background was distinguished using k-means clustering. Note that the selection method relies only on average intensity and not activity —a method we chose so as to maintain the same detection method for responsive and non-responsive runs. This also relies on selecting fields of view as unambiguously containing the neuron of interest — and only the neuron of interest — during the experiment.

$ΔF/F_{0}$ =$\frac{(F−F_{0})}{(F_{0}−B)}$, where F is the raw fluorescence and B the background signal (calculated as the intensity of the dimmest 10% pixels of the average image) were then computed for each movie in the ROI. Given that baseline fluorescence could vary widely over the course of an experiment (see Discussion), we defined F0 as the median fluorescence in the ROI in the dimmest 3% of frames of the entire experiment.

#### Statistics

For every experimental repeat, we computed the following statistics:

Then, for every run, which consists of 4 repeats done on the same fly, we computed:

Subsequently, for every set of runs done on the same cell pair and the same stimulation protocol, we computed:

Moreover, we created $<I_{toPeak}>_{scaled}$, $<<I_{toPeak}>>_{scaled}$, $<I_{toPeak_norm}>_{scaled}$ and $<<I_{toPeak_norm}>>_{scaled}$, scaled versions of $<I_{toPeak}>$, $<<I_{toPeak}>>$, $<I_{toPeak_norm}>$ and $<<I_{toPeak_norm}>>$ so that the values cover the range [−1,1] by scaling positive (negative) values by the maximum (minimum) response in the dataset.

#### Distance from control and significance

Based on light level anatomy, we labeled each tested pair as overlapping or non-overlapping. We used the set of non-overlapping pairs as a control (the null sample). Considering only two parameters, the scaled normalized integral $<<I_{toPeak_norm}>>_{scaled}$ and the correlation across flies $R_{between−flies}$ (see Figure 3), we calculated the Mahalanobis distance between the null sample and each data point, using a robust estimate of the covariance matrix (following [Rousseeuw and Driessen, 1999]) of the null sample. For a point $x→=(<<I_{topeak_norm}>>_{scaled},R_{between−flies})^{T}$ this will be $\sqrt{(x→−\mu→)^{T}S^{−1}(x→−\mu→)}$ where $S$ is the covariance matrix and $\mu→$ is the vector the average parameters for the null sample. While single statistics never were sufficient to capture all relevant aspects of the response, we found that these two measurements recapitulated well distance measurements obtained by combining all the statistics. We then computed 99% confidence intervals on the distribution of distances by bootstrapping to determine significance.

### Preprint

An earlier version of this manuscript is available as a preprint at https://www.authorea.com/155729/_TsHpd9reMuWijjossgt6Q (DOI: 10.22541/au.151537454.41878908).

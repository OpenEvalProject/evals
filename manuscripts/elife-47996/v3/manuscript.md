# Self-organization of modular network architecture by activity-dependent neuronal migration and outgrowth

## Authors

- Samora Okujeni<sup>1</sup> ([ORCID: 0000-0001-7924-3651](https://orcid.org/0000-0001-7924-3651)) †
- Ulrich Egert<sup>1</sup> ([ORCID: 0000-0002-4583-0425](https://orcid.org/0000-0002-4583-0425))

### Affiliations

1. Laboratory for Biomicrotechnology, Department of Microsystems Engineering—IMTEK University of Freiburg Freiburg Germany
2. Bernstein Center Freiburg University of Freiburg Freiburg Germany

† Corresponding author

## Abstract

The spatial distribution of neurons and activity-dependent neurite outgrowth shape long-range interaction, recurrent local connectivity and the modularity in neuronal networks. We investigated how this mesoscale architecture develops by interaction of neurite outgrowth, cell migration and activity in cultured networks of rat cortical neurons and show that simple rules can explain variations of network modularity. In contrast to theoretical studies on activity-dependent outgrowth but consistent with predictions for modular networks, spontaneous activity and the rate of synchronized bursts increased with clustering, whereas peak firing rates in bursts increased in highly interconnected homogeneous networks. As Ca2+ influx increased exponentially with increasing network recruitment during bursts, its modulation was highly correlated to peak firing rates. During network maturation, long-term estimates of Ca2+ influx showed convergence, even for highly different mesoscale architectures, neurite extent, connectivity, modularity and average activity levels, indicating homeostatic regulation towards a common set-point of Ca2+ influx.

## Introduction

Modularity is a fundamental design principle of neuronal systems and exists at the scale of cellular compartments, local circuits or interconnected brain areas. From a structural perspective, modularity can arise from inhomogeneities in the physical substrate that facilitate connectivity within a group of functional entities versus connectivity between such groups.

At the mesoscale level of local circuits, the cerebral cortex is organized in local clusters of tightly interconnected neurons (Feldman and Peters, 1974; Skoglund et al., 2004) that share common inputs and targets (Bosking et al., 1997; Voges et al., 2010), have similar functional properties (Ringach et al., 2016) and are thought to constitute a basic computational module (Buxhoeveden and Casanova, 2002; Casanova and Casanova, 2019; Mountcastle, 1997).

Although cortical architecture is largely genetically predefined at this level, blocking electrical activity during development disturbed the characteristic clustering of connections, suggesting that activity-dependent self-organization influences network modularity (Durack and Katz, 1996; Ruthazer and Stryker, 1996; Thompson, 1997). Intriguingly, computational models predict that modular connectivity, in turn, promotes spontaneous activity (Kaiser and Hilgetag, 2010; Klinshov et al., 2014; Mazzucato et al., 2015). Modularization and spontaneous activity may thus co-evolve in a self-enhancing process.

In early postnatal development, neuronal migration and neurite outgrowth are regulated by activity-dependent changes of the intracellular Ca2+ concentration [Ca2+]i (Kater and Mills, 1991; Komuro and Kumada, 2005; Spitzer, 2006; Zheng and Poo, 2007), suggesting that morphodevelopmental processes contribute to cellular Ca2+ homeostasis (Zündorf and Reiser, 2011). Put simply, neurons would grow to increase neurite field overlap and the corresponding synaptic connectivity (Kossio et al., 2018; Shepherd et al., 2005; Stepanyants et al., 2002; Tetzlaff et al., 2010; van Ooyen et al., 1995) to establish the level of spike activity necessary to achieve some target value of [Ca2+]i. As inter-neuron distance strongly affects the overlap of neurite fields and thus connectivity (Barral and D Reyes, 2016; Schnepel et al., 2015; Seeman et al., 2018), spatial clustering of neurons may play an important role in shaping modularity (Hernández-Navarro et al., 2017).

In the current study, we focus on the developmental self-organization that leads to different network architectures. In a simple computational model, varying the ratio of activity-dependent homeostatic growth versus migration was sufficient to modify neuronal clustering, mesoscale network organization, and the degree of modularity. Since controlled manipulation of network architecture and simultaneous activity monitoring is impractical in vivo, we tested this developmental interaction by modifying growth and migration in networks of cortical neurons in cell culture. These networks recapitulate major developmental processes such as cell migration and neurite outgrowth (Guan et al., 2007; van Huizen et al., 1987; van Pelt et al., 2004), develop varying degrees of clustering (Kriegstein and Dichter, 1983; Okujeni et al., 2017; Soriano et al., 2008; Teller et al., 2014) and produce a rich repertoire of spontaneous bursting events (SBE) (Kamioka et al., 1996; Okujeni et al., 2017; Wagenaar et al., 2006), similar to the developing cortex (Golshani et al., 2009; Minlebaev et al., 2007).

On the biochemical level, neuronal morphology is regulated by an interplay between activity-dependent kinases and phosphatases controlling cytoskeletal turnover rates (Flynn, 2013; Quinlan and Halpain, 1996). A key player herein is PKC, a Ca2+-modulated enzyme regulating cell migration (Itoh et al., 1989; Larsson, 2006) and neurite outgrowth (Gundlfinger et al., 2003; Metzger, 2010).

Increasing PKC activity in cultured networks amplified cell body clustering and local neurite entanglement at the expense of long-range connections, promoting local burst initiation and average firing rate (AFR) but reducing network recruitment during SBEs (Okujeni et al., 2017; Okujeni and Egert, 2019). This supports the theoretical predictions for modular networks mentioned above and is consistent with results from clustered networks created by mechanical constraints or modified growth substrates (Bisio et al., 2014; Tibau Martorell et al., 2018; Yamamoto et al., 2018).

Irrespective of network architecture, activity stabilized after approximately 21 days in vitro (DIV), suggesting that the target of homeostatic network development had been achieved. Different AFRs at this stage, however, conflict with previous studies assuming that AFR development reflects the homeostatic regulation of [Ca2+]i (Abbott and Rohrkemper, 2007; Kossio et al., 2018; van Ooyen et al., 1995). Ca2+-influx, however, exponentially increases with membrane depolarization (Mazzanti et al., 1992) and thus depends on the temporal structure of spike activity. Our findings suggest that because of this non-linearity and specific differences in network-wide peak firing rates (PFR), long-term average Ca2+ influx converges despite different AFRs and connectivity. Migration and neurite growth thus interact in a homeostatic process that defines the mesoscale architecture of neuronal networks.

## Results

The connectivity between neurons depends on the overlap of their neurite fields and on their spatial distribution in the network. Like neurite growth, however, this distribution is dynamic because neurons migrate even in postnatal development. In a recurrent network, the input a neuron receives then depends on its embedding as well as the network’s overall connectivity and activity structure. Here, we investigated how activity-dependent neurite growth and migration interact to establish connectivity and activity in neuronal networks.

### Simulating activity-dependent neurite growth and migration

To gain insights into interdependencies between neurite growth and neuronal migration during the activity-dependent network self-organization, we extended a network growth model introduced by van Ooyen et al. (1995) that reproduces the outgrowth and subsequent pruning of neurites reported for developing neuronal networks (van Huizen et al., 1987; van Pelt et al., 2004). Following this, neurons were initially randomly seeded on a torus and their interconnectivity was modeled as degree of overlap between their circular neurite fields (no distinction was made between axons and dendrites). Input to neurons was calculated as the product of presynaptic firing rates and respective connectivity. A sigmoidal transfer function governed the relation between input-dependent membrane potential depolarization and firing rate (Figure 1A). A growth process superimposed onto this framework allowed neurons to adjust their input by growing or shrinking their neurite fields, and thus the overlap with other fields, to establish a defined target firing rate (Figure 1B,C). In addition to neurite growth, the final phase of neuronal migration observed in postnatal development is modulated by network activity and thus interacts with the formation of neurite fields and the regulation of connectivity. We therefore extended the original framework of the model by adding activity-dependent migration, where neuron somata migrated in the direction of the strongest input and gradually slowed down as their firing rates converged to the target level (Figure 1B,D). In contrast to the bidirectional modulation of neurite fields, neurons were not repelled, however, if the activity level was above target. Prior to the formation of first contacts, migration was determined by erratic movements only. Neurons could thus increase their input by extending neurites and by migration to increase the overlap of neurite fields. The relative contribution of migration in network formation herein depended on its rate in relation to the net rate of neurite extension or pruning.

![Figure 1.](https://cdn.elifesciences.org/articles/47996/elife-47996-fig1-v3.jpg)

**Figure 1.:** Neuronal wiring strategies may involve expansion of neurite fields and migration towards other neurons to increase connectivity modeled as neurite field overlap. (A) Transfer function of membrane depolarization between resting and maximal potential to firing rates. Dotted line: target firing rate. (B) Neurite growth (orange) and migration (green) were modulated as a function of [Ca2+]i that corresponded to average firing rates. Neurites grew while the firing rate (corresponding to long-term average Ca2+ influx) was below target and were pruned when above it. Migration rate decreased as neurons approached the target firing rate (dotted line). (C) The area of neurite field overlap, corresponding to connectivity in the model, can be increased by neurite outgrowth and neuronal migration towards neighboring neurons (D).

### Migration and neurite outgrowth shape network architecture

Initially, neurite outgrowth (Figure 2A) and migration (Figure 2B) did not depend on activity. Once neurite fields began to overlap, directed migration towards areas that provided more input amplified statistical variations in the local cell density and led to clustering, indicated by decreasing clustering index (CI, Figure 2C). CI was calculated as the ratio between the average nearest neighbor distance in a network and the expected average nearest neighbor distance for random networks. CI above one indicates grid-like cell body arrangements and CI below one indicates clustering. Increasing clustering promoted connectivity buildup (Figure 2D) and thus input to a neuron (Figure 2E), which advanced the onset of spontaneous network activity (Figure 2F). Migration and clustering of neurons ceased with the steep onset of network activity (Figure 2B,C,F). In homogeneous networks, neurite fields had to grow larger than in clustered networks to establish the same degree of overlap and thus connectivity (Figure 2A,D). As a result, the size of neurites in mature networks correlated negatively with the degree of neuronal clustering (Figure 2—figure supplement 1). Connectivity, input activity and firing rates eventually converged to the same levels for different migration conditions (Figure 2D–F).

![Figure 2.](https://cdn.elifesciences.org/articles/47996/elife-47996-fig2-v3.jpg)

**Figure 2.:** (A) Activity-dependent growth produced a characteristic overshoot and subsequent pruning of neurite fields. The overall size of developing neurites decreased with increasing migration rates and clustering. (B) Mean migration distance of neurons after seeding (smoothed by 1 hr sliding average). (C) Migration promoted clustering of neurons, which saturated with the onset of network activity and neurite pruning (curves smoothed by 1 hr sliding average). All networks were initialized with the same spatial cell body distribution with CI close to 1. Note that the fluctuations for zero migration results from the random jittering of neuron positions by half the cell body radius (6 µm). (D) Average connectivity increased more rapidly with stronger migration and clustering. (E) Input increased faster with increasing migration rate because clustering initially promoted connectivity. Input levels eventually converged. (F) Firing rates increased sharply once critical input levels were attained. Migration and clustering accelerated the onset of activity. With increasing migration, steps arise because of incremental integration and activation of clusters within the larger network. Note that clustering reduced the developmental overshoot of firing rates. (G) Moderate migration and clustering produced the highest variability of neurite field size across neurons in mature networks. (H) High migration rates increased modularity in mature networks. With increasing migration rate, the giant component more rapidly decreased in clustered networks when a certain fraction of neurons was randomly deleted, indicating that these networks break into disconnected subnets. Inset: the fraction of neurons in the giant cluster, that is the largest connected subnetwork, evolved similarly in different migration conditions. (I) Migration rates crucially determined the mesoscale architecture and modularity (increasing Q indicates stronger modularity) of developing networks. While average neurite fields were small in clustered networks, more isolated neurons generated larger fields (arrows) and formed bottlenecks for activity propagation by connecting otherwise unconnected or weakly connected subnetworks.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/47996/elife-47996-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** Increasing migration rates in the simulation promoted neuronal clustering leading to lower final CI and smaller neurite field sizes. At the onset of high network activity, neurite fields were pruned and CI did not change further.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/47996/elife-47996-fig2-figsupp2-v3.jpg)

**Figure 2—figure supplement 2.:** (A) Decreasing the slope of the sigmoidal transfer function mapping membrane potential to firing rate resulted in saturating growth (inset: blue: $a$ = 0.2) instead of an overshoot (inset: black, $a$ = 0.12, see Figure 2) in average neurite field size and connectivity. Note that the synaptic weight factor $s$ was reduced ($s$ = 0.05 instead of 0.1) to compensate for the increased baseline firing associated with higher $a$. Average neurite fields saturated at different levels depending on the rate of migration, average migration distance (B) and degree of clustering (C). (D) Connectivity increased faster with clustering as in the case of $a$ = 0.12. Network-activity, characterized by the average synaptic input (D) and the firing rate (F) increased earlier and more gradually with clustering. (G) Although there was no overshoot of connectivity on average (black line), neurons with faster increase of connectivity showed overshoot and pruning when the network firing rate rapidly increased. In the same network, neurons with slowly increasing connectivity displayed saturating growth. Color indicates the order in which 50 randomly chosen neurons attained 75% of their final connectivity. (H) With migration and clustering, connectivity increased more rapidly with the same dependency of the overshoot on early and late developing connectivity. (I) Saturating growth and migration produced mesoscale network architectures ranging from homogeneous to clustered networks similar to those in Figure 2I. Migration promoted clustering and modularization (increasing Q indicates stronger modularity).

Varying the rate of migration crucially impacted on the overall architecture of developing networks (Figure 2I, Figure 2—videos 1–4). Without migration, networks developed the most homogeneous neurite field diameters and neurite coverage (Figure 2G). Clustering led to more variable neurite field diameters as more isolated neurons required large fields to receive sufficient input, whereas within dense clusters, strongly overlapping neurite fields remained small.

The evolution of the largest connected subnetwork, that is the giant component, suggested that full network connectivity was established along the same developmental time line, irrespective of the degree of clustering (Figure 2H, inset). In clustered networks, however, individual neurons played an important role in bridging subnetworks (Figure 2I, arrows in the bottom panel). To quantify the tendency for modularity with different architectures, we calculated the giant component remaining after removing increasing subsets of randomly selected neurons in mature networks (Figure 2H). In clustered networks, the giant component shrunk faster with an increasing fraction of neurons removed, demonstrating that individual neurons became critical bottlenecks in connectivity. Increasing activity-dependent migration relative to neurite growth thus increased the modularity (Q, Figure 2I) of the network.

### Mesoscale network architecture in vitro

The growth model suggested that spatial clustering of neurons during development could play a crucial role in the formation of network connectivity by influencing the probability of neurites to overlap during outgrowth. We assessed this dependence experimentally by chronic activation or inhibition of PKC (PKC+ and PKC− respectively), a regulator of neuronal migration, in developing networks of cortical neurons in cell culture. As described previously (Okujeni et al., 2017), PKC manipulation significantly altered the mesoscale architecture of networks with 600–800 neurons/mm2 (Figure 3A), with striking similarity to mature networks generated with the growth model. Under control conditions (PKCN networks), networks appeared as inhomogeneous density landscapes with both, clustered and sparse regions (Figure 3A, center panel). In particular in clustered areas, neurites formed tangles, which would increase the probability of local connections. Axons spanning several millimeters indicated monosynaptic connections between distant network regions. In comparison, PKC− networks with diminished migration had a more homogeneous distribution of cell bodies and coverage with dendrites and axons (Figure 3A, left panel). Reduced fasciculation of neurites and a high density of long-range axons suggested a more isotropic embedding of neurons and more random-like connectivity. In turn, PKC+ networks with enhanced migration had well delineated clusters of about 30–60 neurons with dense tangles of neurites that rarely reached into neighboring clusters (Figure 3A, right panel), indicating high local connectivity and reduced inter-cluster connectivity.

![Figure 3.](https://cdn.elifesciences.org/articles/47996/elife-47996-fig3-v3.jpg)

**Figure 3.:** (A) Dense networks established characteristic mesoscale architectures for the different PKC conditions. PKC− networks had a more homogeneous distribution of axons (red), dendrites (green) and cell bodies (green) than PKCN networks. In PKC+ networks, neurons formed well-delineated clusters. Note that the following morphometric analyses are based on sparser cultures. (B) Decreasing CI during development reflects cell migration and ongoing clustering of neuronal cell bodies until ~15 DIV. PKC+ promoted and PKC− diminished clustering during development. (C) Dendrite size increased until 22 DIV, with boosted growth in PKC− and diminished growth in PKC+ networks. (D) In late development, dendrite size scaled inversely with the degree of clustering. For visualization the CI axis was inversed, so the degree of clustering increases from left to right. (E) The synapse density increased concurrently with dendrite growth. After 22 DIV synapse densities decreased in PKCN and PKC+ networks, indicating synaptic pruning. (F) Dendritic occupancy with synapses differed slightly between conditions and decreased after 22 DIV. (G) The number of synapse per neurons increased with the dendrite size. Gray lines connect networks of the same age. The blue line illustrates a proposed quadratic scaling rule between dendrite size and synapse densities. (H) Neuron density declined with DIV to about one third of the seeding density. (I) Estimated upper bounds for connectivity based on the synapse density and the total number of neurons (on 113 mm2 cover slips). PKC−at least doubled average connectivity. (J) In mature networks, maximum connectivity scaled inversely with clustering. All parameters are presented as mean ± SEM. Data from 4 to 24 images (Table 1, area 3.5 mm2) taken in each of 2 networks per condition and age. Asterisks indicate p-values ≤0.05 (*), ≤0.01 (**) and ≤0.001 (***) tested against PKCN.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/47996/elife-47996-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** Exemplary images with neuronal nuclei (NeuN, red) and dendrites (MAP2, green) stained at 8 and 22 DIV. PKC inhibition diminished and PKC stimulation promoted neuronal migration and clustering of neurons during development. Dendrite growth changed with the spatial arrangement of cell bodies. Homogeneous cell body arrangements correlated with larger dendrites, whereas clusters had local dendrite tangles and dendrite bundles reaching to other clusters.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/47996/elife-47996-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** Immunohistochemical staining of dendrites (MAP2, red), presynaptic compartments (synapsin, green) and cellular nuclei (DAPI, blue). Synapse densities on dendrites increased in all PKC conditions up to 22 DIV and slightly decreased afterwards. Overall synapse densities were highest in the PKC− and lowest in PKC+ networks.

### Cell migration promotes neuronal clustering

To quantify the structural development, we seeded networks at lower densities of about 300 neurons per mm2 that were more suitable for morphometric analyses (Figure 3—figure supplement 1). Within the first day of random seeding of neurons, rapid neurite outgrowth resulted in overlapping neurite fields between neighboring neurons. Simultaneously, neuronal cell bodies migrated across the substrate. Neuronal migration with concurrent outgrowth of neurites gradually increased neuron clustering within about three weeks in vitro (Figure 3B). Chronic manipulation of PKC activity differentially modulated neuronal clustering during development (Table 1). At 22 DIV, clustering was moderate in PKCN networks (CI = 0.75 ± 0.03) but significantly increased in the PKC+ networks (CI = 0.67 ± 0.02, p=3.3*10−2) and significantly reduced in the PKC− networks (CI = 0.88 ± 0.01, p=4.4*10−4). CI did not change significantly after 22 DIV, indicating cessation of neuronal migration.

**Table 1.**
 Morphometric analysis of network development under different PKC conditions.Results are presented as mean ± standard error of mean (SEM). Significance was determined against PKCN, or between specified developmental time windows, using independent Student’s t-test. N specifies the number of analyzed images taken from two networks per PKC condition and age.Table 1—source data 1.Source data and Matlab script.Table 1—source data 2.Source data and Matlab script.


<table>
  <thead>
    <tr>
      <th></th>
      <th>DIV</th>
      <th>PKC-</th>
      <th>PKCN</th>
      <th>PKC+</th>
      <th>unit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>clustering index</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>8</td>
      <td>0.92 ± 0.01 (1.8*10−10)</td>
      <td>0.84 ± 0.01</td>
      <td>0.82 ± 0.02 (6.1*10−1)</td>
      <td>CI</td>
    </tr>
    <tr>
      <td></td>
      <td>15</td>
      <td>0.9 ± 0.01 (1.5*10−6)</td>
      <td>0.73 ± 0.01</td>
      <td>0.69 ± 0.02 (1.1*10−1)</td>
      <td>CI</td>
    </tr>
    <tr>
      <td></td>
      <td>22</td>
      <td>0.88 ± 0.01 (4.4*10−4)</td>
      <td>0.75 ± 0.03</td>
      <td>0.67 ± 0.02 (3.3*10−2)</td>
      <td>CI</td>
    </tr>
    <tr>
      <td></td>
      <td>29</td>
      <td>0.89 ± 0.01 (8.0*10−9)</td>
      <td>0.79 ± 0.01</td>
      <td>0.67 ± 0.02 (2.1*10−5)</td>
      <td>CI</td>
    </tr>
    <tr>
      <td></td>
      <td>8 vs. 22</td>
      <td>−4.49 (3.5*10−4)</td>
      <td>−9.65 (3.1*10−2)</td>
      <td>−18.6 (1.2*10−5)</td>
      <td>% change</td>
    </tr>
    <tr>
      <td></td>
      <td>22 vs. 29</td>
      <td>1.04 (4.9*10−1)</td>
      <td>4.5 (2.7*10−1)</td>
      <td>0.01 (1.0)</td>
      <td>% change</td>
    </tr>
    <tr>
      <td>Dendrite size</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>8</td>
      <td>476 ± 9 (1.3*10−3)</td>
      <td>421 ± 12</td>
      <td>408 ± 8 (3.4*10−1)</td>
      <td>µm</td>
    </tr>
    <tr>
      <td></td>
      <td>15</td>
      <td>797 ± 22 (1.2*10−2)</td>
      <td>676 ± 37</td>
      <td>610 ± 30 (2.1*10−1)</td>
      <td>µm</td>
    </tr>
    <tr>
      <td></td>
      <td>22</td>
      <td>1413 ± 64 (7.9*10−5)</td>
      <td>1021 ± 41</td>
      <td>816 ± 24 (3.6*10−4)</td>
      <td>µm</td>
    </tr>
    <tr>
      <td></td>
      <td>29</td>
      <td>1380 ± 74 (1.9*10−4)</td>
      <td>962 ± 65</td>
      <td>760 ± 37 (1.3*10−2)</td>
      <td>µm</td>
    </tr>
    <tr>
      <td></td>
      <td>8 vs. 22</td>
      <td>196.59 (4.0*10−20)</td>
      <td>142.46 (9.1*10−12)</td>
      <td>100.08 (1.4*10−15)</td>
      <td>% change</td>
    </tr>
    <tr>
      <td></td>
      <td>22 vs. 29</td>
      <td>−2.38 (7.4*10−1)</td>
      <td>−5.81 (5.0*10−1)</td>
      <td>−6.86 (2.5*10−1)</td>
      <td>% change</td>
    </tr>
    <tr>
      <td>Synapse density</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>8</td>
      <td>281 ± 11 (2.2*10−1)</td>
      <td>255 ± 18</td>
      <td>254 ± 14 (9.4*10−1)</td>
      <td>#</td>
    </tr>
    <tr>
      <td></td>
      <td>15</td>
      <td>1142 ± 44 (2.3*10−4)</td>
      <td>754 ± 39</td>
      <td>510 ± 9 (2.4*10−5)</td>
      <td>#</td>
    </tr>
    <tr>
      <td></td>
      <td>22</td>
      <td>2188 ± 100 (2.1*10−5)</td>
      <td>1427 ± 99</td>
      <td>885 ± 27 (3.4*10−5)</td>
      <td>#</td>
    </tr>
    <tr>
      <td></td>
      <td>29</td>
      <td>2019 ± 110 (4.5*10−8)</td>
      <td>1114 ± 56</td>
      <td>669 ± 21 (5.7*10−8)</td>
      <td>#</td>
    </tr>
    <tr>
      <td></td>
      <td>8 vs. 22</td>
      <td>678.77 (4.7*10−24)</td>
      <td>458.69 (2.1*10−10)</td>
      <td>248.68 (1.2*10−17)</td>
      <td>% change</td>
    </tr>
    <tr>
      <td></td>
      <td>22 vs. 29</td>
      <td>−7.75 (2.7*10−1)</td>
      <td>−21.93 (6.7*10−3)</td>
      <td>−24.35 (1.2*10−6)</td>
      <td>% change</td>
    </tr>
    <tr>
      <td>Dendritic occupancy</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>8</td>
      <td>0.59 ± 0.02 (6.4*10−1)</td>
      <td>0.6 ± 0.04</td>
      <td>0.62 ± 0.03 (7.5*10−1)</td>
      <td>#/µm</td>
    </tr>
    <tr>
      <td></td>
      <td>15</td>
      <td>1.44 ± 0.05 (1.7*10−2)</td>
      <td>1.13 ± 0.11</td>
      <td>0.85 ± 0.04 (1.7*10−2)</td>
      <td>#/µm</td>
    </tr>
    <tr>
      <td></td>
      <td>22</td>
      <td>1.55 ± 0.03 (9.6*10−2)</td>
      <td>1.4 ± 0.09</td>
      <td>1.09 ± 0.04 (5.7*10−3)</td>
      <td>#/µm</td>
    </tr>
    <tr>
      <td></td>
      <td>29</td>
      <td>1.47 ± 0.04 (3.0*10−5)</td>
      <td>1.19 ± 0.04</td>
      <td>0.9 ± 0.04 (2.3*10−5)</td>
      <td>#/µm</td>
    </tr>
    <tr>
      <td></td>
      <td>8 vs. 22</td>
      <td>163.83 (7.2*10−28)</td>
      <td>132.26 (9.0*10−8)</td>
      <td>76.65 (3.7*10−10)</td>
      <td>% change</td>
    </tr>
    <tr>
      <td></td>
      <td>22 vs. 29</td>
      <td>−5.06 (1.5*10−1)</td>
      <td>−15.41 (2.3*10−2)</td>
      <td>−17.45 (3.8*10−3)</td>
      <td>% change</td>
    </tr>
    <tr>
      <td>Neuron density</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>8</td>
      <td>255 ± 6 (9.6*10−7)</td>
      <td>185 ± 11</td>
      <td>168 ± 7 (2.0*10−1)</td>
      <td>#/mm2</td>
    </tr>
    <tr>
      <td></td>
      <td>15</td>
      <td>214 ± 9 (5.9*10−4)</td>
      <td>131 ± 17</td>
      <td>158 ± 12 (2.0*10−1)</td>
      <td>#/mm2</td>
    </tr>
    <tr>
      <td></td>
      <td>22</td>
      <td>107 ± 8 (1.9*10−1)</td>
      <td>123 ± 6</td>
      <td>85 ± 6 (5.7*10−4)</td>
      <td>#/mm2</td>
    </tr>
    <tr>
      <td></td>
      <td>29</td>
      <td>87 ± 5 (3.0*10−1)</td>
      <td>96 ± 7</td>
      <td>77 ± 4 (2.6*10−2)</td>
      <td>#/mm2</td>
    </tr>
    <tr>
      <td></td>
      <td>8 vs. 22</td>
      <td>−58.03 (7.3*10−17)</td>
      <td>−33.66 (1.1*10−4)</td>
      <td>−49.42 (1.0*10−8)</td>
      <td>% change</td>
    </tr>
    <tr>
      <td></td>
      <td>22 vs. 29</td>
      <td>−18.93 (4.5*10−2)</td>
      <td>−21.71 (1.3*10−2)</td>
      <td>−9.79 (2.6*10−1)</td>
      <td>% change</td>
    </tr>
    <tr>
      <td>Maximum connectivity</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>8</td>
      <td>0.01 ± 0.001 (3.5*10−2)</td>
      <td>0.013 ± 0.001</td>
      <td>0.014 ± 0.001 (6.3*10−1)</td>
      <td>fraction</td>
    </tr>
    <tr>
      <td></td>
      <td>15</td>
      <td>0.048 ± 0.003 (4.6*10−1)</td>
      <td>0.053 ± 0.006</td>
      <td>0.029 ± 0.002 (9.2*10−4)</td>
      <td>fraction</td>
    </tr>
    <tr>
      <td></td>
      <td>22</td>
      <td>0.209 ± 0.031 (8.2*10−3)</td>
      <td>0.104 ± 0.007</td>
      <td>0.098 ± 0.009 (5.9*10−1)</td>
      <td>fraction</td>
    </tr>
    <tr>
      <td></td>
      <td>29</td>
      <td>0.229 ± 0.026 (9.2*10−4)</td>
      <td>0.116 ± 0.014</td>
      <td>0.081 ± 0.006 (3.8*10−2)</td>
      <td>fraction</td>
    </tr>
    <tr>
      <td></td>
      <td>8 vs. 22</td>
      <td>1987.43 (5.9*10−10)</td>
      <td>701.18 (2.6*10−11)</td>
      <td>604.32 (1.4*10−10)</td>
      <td>% change</td>
    </tr>
    <tr>
      <td></td>
      <td>22 vs. 29</td>
      <td>9.31 (6.3*10−1)</td>
      <td>11.48 (5.2*10−1)</td>
      <td>−17.23 (1.3*10−1)</td>
      <td>% change</td>
    </tr>
    <tr>
      <td>N</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>8</td>
      <td>24</td>
      <td>11</td>
      <td>15</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>15</td>
      <td>9</td>
      <td>4</td>
      <td>7</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>22</td>
      <td>15</td>
      <td>11</td>
      <td>11</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>29</td>
      <td>17</td>
      <td>16</td>
      <td>15</td>
      <td></td>
    </tr>
  </tbody>
</table>

Note that the spatial patterning of somata depended on neuron density. Clusters in dense networks (~700 neurons/mm2 at >22 DIV) typically contained 30–60 neurons (Okujeni et al., 2017), whereas in sparse networks (~100 neurons/mm2 at >22 DIV) clusters mostly consisted of fewer than 10 neurons (Figure 3—figure supplement 1).

### Clustering diminishes dendrite outgrowth

To address the interaction of neurite field extension, migration and clustering, we analyzed the average size of dendrites at several time points during development (Figure 3C). Dendrite size was quantified as the ratio between the total length of detected dendrite stretches and the number of neurons within regions of interest (Table 1). The measure estimates the average contribution of each neuron to the dendritic mesh. Chronic manipulation of PKC activity had little impact on dendrite size up to 8 DIV but significantly modulated dendrite outgrowth during subsequent development. At 22 DIV, dendrite size was significantly increased in the more homogeneous PKC− networks but significantly reduced in the more strongly clustered PKC+ networks (PKCN: 1021 ± 41 µm; PKC−: 1413 ± 64 µm, p=7.9*10−5; PKC+: 816 ± 24 µm, p=3.6*10−4). In all conditions, dendrite size did not change significantly between 22 and 29 DIV, indicating stabilization of the dendritic network after the third week in vitro. As in the model (Figure 2—figure supplement 1), dendrite size in mature networks was negatively correlated with the degree of cell body clustering and, thus, the distance between neurons (Figure 3D).

### Dendrite outgrowth promotes synaptic connectivity

Network connectivity requires neurite overlap but further depends on the probability by which synapses are realized at axo-dendritic intersections. To assess how synaptic connectivity evolved in the different PKC conditions, we stained and detected presynaptic boutons (Figure 3—figure supplement 2) and determined the synapse density as the average number of presynaptic boutons per neuron (Figure 3E, Table 1) and the dendritic occupancy as the number of synapses per unit dendrite length (Figure 3F, Table 1). Manipulating PKC activity had no significant influence on early synaptogenesis up to 8 DIV, consistent with the comparable dendrite density in different PKC conditions at this stage. Paralleling dendritic outgrowth, synapse density increased significantly with increasing dendritic occupancy between 8 and 22 DIV in all conditions. Synapse densities and dendritic occupancy subsequently decreased between 22 and 29 DIV. This reduction was not significant in PKC− networks, however. Developmental manipulation of PKC activity profoundly affected mature synapse densities (PKCN: 1114 ± 56; PKC−: 2019 ± 110, p=4.5*10−8; PKC+: 669 ± 21, p=5.7*10−8) and dendritic occupancy (PKCN: 1.19 ± 0.04 µm−1; PKC−: 1.47 ± 0.04, p=3.0*10−5 µm−1; PKC+: 0.9 ± 0.04 µm−1, p=2.3*10−5) at 29 DIV, both of which were significantly increased in the PKC− and reduced in the PKC+ condition. Similar to dendrite densities, synapse densities were thus negatively correlated with the degree of clustering. Across PKC conditions and developmental stages, synapse occupancy scaled approximately quadratic with the dendrite size (Figure 3G), which could result from similarly modulated axonal densities (Okujeni et al., 2017) and the corresponding multiplicative increase in intersection probability.

### Clustering reduces maximum global connectivity

Network connectivity is limited by the number of synapses per neuron and the overall number of neurons in a network since neurons obviously cannot have more partners than they have synapses. The ratio between the number of synapses per neuron and the total number of neurons in the network defines an upper bound of connectivity for a network (maximum connectivity). The degree of connectivity realized, however, could be lower because of multiple structural synapses between neuron pairs. Although the density of neurons decreased during early development (Figure 3H, Table 1), maximum connectivity increased significantly in all conditions between 8 and 22 DIV (Figure 3I) and saturated between 22–29 DIV. At the same time, maximum connectivity almost doubled in PKC− networks compared to PKCN networks but was significantly reduced in PKC+ networks (PKCN: 0.12 ± 0.01; PKC−: 0.23 ± 0.03, p=9.2*10−4; PKC+: 0.08 ± 0.01, p=3.8*10−2) and thus was negatively correlated with the degree of clustering (Figure 3J).

### Mesoscale architecture and the development of spontaneous activity

We recently showed that the specific spatiotemporal patterns of spontaneous bursting depended considerably on the mesoscale architecture of the network (Okujeni et al., 2017; Okujeni and Egert, 2019) (Figure 4—figure supplement 1). In all networks types, spikes were typically organized in bursts that were synchronized across micro-electrode arrays (MEA; Figure 4—figure supplement 1A,B) with low activity between SBEs. Mature PKC− networks typically generated strong SBEs at low rates with many spikes per recording site (Figure 4—figure supplement 1C). SBE rates were significantly increased in moderately clustered PKCN networks with fewer spikes per site (Figure 4—figure supplement 1D). Strongly clustered PKC+ networks generated weaker SBEs at even higher rates and fewer participating sites (Figure 4—figure supplement 1E).

During development, spontaneous activity started with sporadic, uncorrelated spiking in all networks. First SBEs typically appeared at very low rates at 3–5 DIV, indicating that neuronal migration and neurite outgrowth had connected neurons sufficiently to synchronize their activity. Subsequently, activity became increasingly dominated by SBEs attaining mature levels with around 70–90% of all spikes in SBEs at 10–14 DIV (PKCN: 82 ± 2%; PKC−: 87 ± 2%; PKC+: 71 ± 3%). SBE rates increased faster with enhanced migration and clustering (Figure 4A, Table 2). The positive correlation between the degree of clustering and SBE rates persisted beyond the end of the migratory phase (10–14 DIV) where SBE rates continued to increase in all PKC conditions until stabilizing after the fourth week. In late development (28–35 DIV), SBE rates were significantly increased in the clustered PKC+ networks and reduced in the more homogeneous PKC− networks (PKCN: 17.0 ± 1.1 min−1; PKC−: 5.0 ± 0.8 min−1, p=2.2*10−13; PKC+: 41.1 ± 5.1 min−1, p=7.9*10−9). Clustering thus promoted spontaneous activity generation, in line with predictions from simulations (Kaiser and Hilgetag, 2010) but inconsistent with homeostatic regulation of connectivity towards a target firing rate. Achieving defined AFR by homeostasis would require that increased SBE rates be counterbalanced by a proportional reduction in SBE strength, that is the average number of spikes per SBE. In early development, SBE strength rapidly increased and plateaued at levels that were indeed inversely correlated to SBE rates (Figure 4B, Table 2), which resulted in similar AFRs across PKC conditions at this age (Figure 4C, Table 2). Later in development, however, the decline in SBE strength was not proportional to the increase in SBE rates, in particular in PKC− networks. This resulted in significantly lower AFRs in PKC− networks (0.6 ± 0.1 Hz, p=2.9*10−3) and significantly increased AFRs in PKC+ networks (1.4 ± 0.2 Hz, p=6.9*10−3) compared to PKCN networks (1.0 ± 0.1 Hz) at 28–35 DIV.

![Figure 4.](https://cdn.elifesciences.org/articles/47996/elife-47996-fig4-v3.jpg)

**Figure 4.:** (A) SBE rates gradually increased during development until 28 DIV, which was accelerated in clustered PKC+ networks and decelerated in homogeneous PKC− networks. In result, SBE rates differed considerably in mature networks and increased with the degree of clustering. X-axis ticks indicate bin boundaries. (B) PKC− networks generated stronger SBEs with more APs per site than clustered networks, compensating lower SBE rates to some extent. Burst strength increased initially but declined later on, putatively because of the maturation of inhibition. (C) AFR increased comparably during early development in the different PKC conditions, indicating that stronger bursting compensated lower SBE rates. Later in development, AFRs were increased in PKC+ and reduced in PKC− networks. (D) Neurons in PKC− networks showed strong depolarization during SBEs that reached well above the spiking threshold around −40 mV causing depolarization block of spiking. In clustered networks, neurons displayed higher membrane potential fluctuations below threshold that occasionaly passed the threshold leading to spikes. (E) Membrane potential distribution. Thick lines indicate regions significantly different from PKCN (p≤0.05). The fraction of time in which neuronal membrane potentials were above the spiking threshold (dashed line) was significantly increased in PKC− networks compared to PKCN and PKC+ networks. Data in A-D and F show mean ± SEM derived from 1 hr recording sessions. Asterisks indicate p-values ≤0.05 (*), ≤0.01 (**) and ≤0.001 (***) tested against PKCN. The number of recordings per age and condition is provided in Table 2.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/47996/elife-47996-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** (A) SBE spike activity on a MEA electrode. Spike times (blue) were detected with a voltage threshold on high-pass filtered raw data. (B) Global spike histogram (10 ms bins) and spike activity of a PKCN network recorded with a 16 × 16 MEA (inset) at 11 DIV. Most spikes occurred in bursts (gray lines connect spikes assigned to a burst) that were typically organized in SBEs. Red lines indicate SBE onset and offset. Blue: electrode shown in A. (C–E) Global spike histogram (top row) and raster plot of typical activity in networks with different mesoscale architecture at 22–23 DIV (58–59 active sites; 6 × 10 MEAs). C SBEs (red ticks) in PKC− networks had high PFRs and typically occurred in regular intervals at low rates. (D) PKCN networks displayed a wide range of dynamics. The example shows SBEs occuring at intermediate rates and in irregular intervals. (E) Bursts of bursts, that is superbursts, occurred in PKCN and were very prominent in PKC+ (shown), but not in PKC− networks.

**Table 2.**
 Electrophysiological characterization of network activity during development.Data were pooled within defined developmental time windows. Significance was determined against PKCN using independent Student’s t-test. N specifies the number of recorded networks per PKC condition and age.


<table>
  <thead>
    <tr>
      <th></th>
      <th>DIV</th>
      <th>PKC−</th>
      <th>PKCN</th>
      <th>PKC+</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AFR</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>3–5</td>
      <td>0.03 ± 0.01 (1.0*10−1)</td>
      <td>0.05 ± 0.01</td>
      <td>0.09 (1.4*10−1)</td>
    </tr>
    <tr>
      <td></td>
      <td>6–9</td>
      <td>0.08 ± 0.01 (2.6*10−3)</td>
      <td>0.18 ± 0.03</td>
      <td>0.1 ± 0.02 (4.0*10−2)</td>
    </tr>
    <tr>
      <td></td>
      <td>10–14</td>
      <td>0.36 ± 0.04 (1.8*10−2)</td>
      <td>0.49 ± 0.03</td>
      <td>0.42 ± 0.04 (2.0*10−1)</td>
    </tr>
    <tr>
      <td></td>
      <td>15–20</td>
      <td>0.53 ± 0.06 (3.6*10−1)</td>
      <td>0.61 ± 0.06</td>
      <td>0.76 ± 0.19 (3.6*10−1)</td>
    </tr>
    <tr>
      <td></td>
      <td>21–27</td>
      <td>0.69 ± 0.08 (2.5*10-1)</td>
      <td>0.8 ± 0.06</td>
      <td>1.21 ± 0.12 (7.3*10−4)</td>
    </tr>
    <tr>
      <td></td>
      <td>28–35</td>
      <td>0.6 ± 0.07 (2.9*10−3)</td>
      <td>0.96 ± 0.09</td>
      <td>1.41 ± 0.15 (6.9*10−3)</td>
    </tr>
    <tr>
      <td></td>
      <td>36–44</td>
      <td>0.42 ± 0.08 (2.4*10−7)</td>
      <td>1.18 ± 0.1</td>
      <td>2.04 ± 0.83 (4.3*10−2)</td>
    </tr>
    <tr>
      <td></td>
      <td>45+</td>
      <td>0.24 ± 0.02 (9.9*10−8)</td>
      <td>1.06 ± 0.14</td>
      <td>1.2 ± 0.63 (8.3*10−1)</td>
    </tr>
    <tr>
      <td colspan="5">SBE rate (SBE/min)</td>
    </tr>
    <tr>
      <td></td>
      <td>3–5</td>
      <td>0.17 ± 0.04 (2.9*10−1)</td>
      <td>0.11 ± 0.03</td>
      <td>0.54 (1.5*10−2)</td>
    </tr>
    <tr>
      <td></td>
      <td>6–9</td>
      <td>0.18 ± 0.03 (5.4*10−6)</td>
      <td>1.02 ± 0.15</td>
      <td>1.46 ± 0.19 (7.4*10−2)</td>
    </tr>
    <tr>
      <td></td>
      <td>10–14</td>
      <td>1.21 ± 0.13 (2.0*10−8)</td>
      <td>4.26 ± 0.44</td>
      <td>11.69 ± 1.27 (3.4*10−10)</td>
    </tr>
    <tr>
      <td></td>
      <td>15–20</td>
      <td>2.83 ± 0.35 (1.4*10−8)</td>
      <td>6.36 ± 0.43</td>
      <td>14.31 ± 2.03 (4.7*10−7)</td>
    </tr>
    <tr>
      <td></td>
      <td>21–27</td>
      <td>4.58 ± 0.44 (2.4*10−10)</td>
      <td>10.3 ± 0.62</td>
      <td>26.82 ± 3 (5.5*10−12)</td>
    </tr>
    <tr>
      <td></td>
      <td>28–35</td>
      <td>4.98 ± 0.81 (2.2*10−13)</td>
      <td>16.97 ± 1.07</td>
      <td>41.1 ± 5.07 (7.9*10-9)</td>
    </tr>
    <tr>
      <td></td>
      <td>36–44</td>
      <td>4.08 ± 0.75 (9.0*10−12)</td>
      <td>17.25 ± 1.28</td>
      <td>26.21 ± 7.05 (8.7*10−2)</td>
    </tr>
    <tr>
      <td></td>
      <td>45+</td>
      <td>3.74 ± 0.56 (2.2*10−13)</td>
      <td>18.85 ± 1.62</td>
      <td>45.76 ± 23.86 (2.0*10−3)</td>
    </tr>
    <tr>
      <td colspan="5">SBE strength (APs per burst)</td>
    </tr>
    <tr>
      <td></td>
      <td>3–5</td>
      <td>6.2 ± 3 (1.0*100)</td>
      <td>6.2 ± 3.8</td>
      <td>3.5 (7.6*10−1)</td>
    </tr>
    <tr>
      <td></td>
      <td>6–9</td>
      <td>21.6 ± 2.1 (9.4*10−7)</td>
      <td>9.5 ± 1</td>
      <td>4.6 ± 0.6 (1.2*10−3)</td>
    </tr>
    <tr>
      <td></td>
      <td>10–14</td>
      <td>21.2 ± 2.1 (5.7*10−9)</td>
      <td>9 ± 0.8</td>
      <td>2.7 ± 0.5 (1.5*10−7)</td>
    </tr>
    <tr>
      <td></td>
      <td>15–20</td>
      <td>15.2 ± 1.9 (2.1*10−3)</td>
      <td>8 ± 1.3</td>
      <td>2.7 ± 0.3 (1.2*10−2)</td>
    </tr>
    <tr>
      <td></td>
      <td>21–27</td>
      <td>10.1 ± 1 (6.1*10−8)</td>
      <td>4.9 ± 0.4</td>
      <td>4.4 ± 0.9 (5.4*10−1)</td>
    </tr>
    <tr>
      <td></td>
      <td>28–35</td>
      <td>8.9 ± 0.9 (2.9*10−6)</td>
      <td>4 ± 0.5</td>
      <td>2.3 ± 0.3 (1.7*10−2)</td>
    </tr>
    <tr>
      <td></td>
      <td>36–44</td>
      <td>6.2 ± 0.6 (2.2*10−1)</td>
      <td>5.1 ± 0.6</td>
      <td>5.1 ± 1.6 (9.8*10−1)</td>
    </tr>
    <tr>
      <td></td>
      <td>45+</td>
      <td>5.6 ± 0.8 (4.2*10−2)</td>
      <td>3.8 ± 0.5</td>
      <td>1.1 ± 0.4 (2.2*10−1)</td>
    </tr>
    <tr>
      <td colspan="5">PFR (Hz)</td>
    </tr>
    <tr>
      <td></td>
      <td>3–5</td>
      <td>12.3 ± 3.8 (9.0*10−1)</td>
      <td>13.2 ± 7.3</td>
      <td>11.5 (9.2*10−1)</td>
    </tr>
    <tr>
      <td></td>
      <td>6–9</td>
      <td>50.8 ± 4.8 (6.4*10−5)</td>
      <td>28.3 ± 2.7</td>
      <td>17.4 ± 1.7 (4.9*10−3)</td>
    </tr>
    <tr>
      <td></td>
      <td>10–14</td>
      <td>76.6 ± 5.4 (6.7*10−14)</td>
      <td>32.1 ± 2.3</td>
      <td>10.3 ± 1.4 (2.1*10−9)</td>
    </tr>
    <tr>
      <td></td>
      <td>15–20</td>
      <td>59.1 ± 6.5 (5.3*10−5)</td>
      <td>29.8 ± 3.4</td>
      <td>10.9 ± 1.3 (6.4*10−4)</td>
    </tr>
    <tr>
      <td></td>
      <td>21–27</td>
      <td>43.3 ± 4.1 (7.4*10−10)</td>
      <td>18.9 ± 1.5</td>
      <td>13.7 ± 2 (4.4*10−2)</td>
    </tr>
    <tr>
      <td></td>
      <td>28–35</td>
      <td>42.3 ± 4.4 (2.4*10−8)</td>
      <td>15.5 ± 2</td>
      <td>8.1 ± 1.2 (1.8*10−2)</td>
    </tr>
    <tr>
      <td></td>
      <td>36–44</td>
      <td>30.5 ± 3.1 (2.7*10−2)</td>
      <td>21.4 ± 2.6</td>
      <td>6.1 ± 0.4 (1.3*10−1)</td>
    </tr>
    <tr>
      <td></td>
      <td>45+</td>
      <td>27.5 ± 3.8 (1.5*10−2)</td>
      <td>16.4 ± 2.3</td>
      <td>5.6 ± 1.7 (2.8*10−1)</td>
    </tr>
    <tr>
      <td colspan="5">Network synchrony</td>
    </tr>
    <tr>
      <td></td>
      <td>3–5</td>
      <td>0.1 ± 0.03 (2.6*10−1)</td>
      <td>0.04 ± 0.02</td>
      <td>0.08 (3.4*10−1)</td>
    </tr>
    <tr>
      <td></td>
      <td>6–9</td>
      <td>0.39 ± 0.02 (3.3*10−3)</td>
      <td>0.29 ± 0.02</td>
      <td>0.15 ± 0.02 (3.1*10−4)</td>
    </tr>
    <tr>
      <td></td>
      <td>10–14</td>
      <td>0.52 ± 0.03 (2.5*10−10)</td>
      <td>0.31 ± 0.02</td>
      <td>0.12 ± 0.02 (1.4*10−10)</td>
    </tr>
    <tr>
      <td></td>
      <td>15–20</td>
      <td>0.53 ± 0.04 (4.6*10−5)</td>
      <td>0.35 ± 0.02</td>
      <td>0.16 ± 0.03 (1.7*10−5)</td>
    </tr>
    <tr>
      <td></td>
      <td>21–27</td>
      <td>0.51 ± 0.03 (5.8*10−13)</td>
      <td>0.26 ± 0.02</td>
      <td>0.2 ± 0.02 (4.8*10−2)</td>
    </tr>
    <tr>
      <td></td>
      <td>28–35</td>
      <td>0.57 ± 0.04 (2.0*10−10)</td>
      <td>0.24 ± 0.03</td>
      <td>0.15 ± 0.03 (7.6*10−2)</td>
    </tr>
    <tr>
      <td></td>
      <td>36–44</td>
      <td>0.53 ± 0.04 (1.3*10−5)</td>
      <td>0.3 ± 0.03</td>
      <td>0.11 ± 0.03 (1.3*10−1)</td>
    </tr>
    <tr>
      <td></td>
      <td>45+</td>
      <td>0.45 ± 0.05 (2.5*10−3)</td>
      <td>0.26 ± 0.03</td>
      <td>0.14 ± 0.11 (3.8*10−1)</td>
    </tr>
    <tr>
      <td colspan="5">N</td>
    </tr>
    <tr>
      <td></td>
      <td>3–5</td>
      <td>7</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>6–9</td>
      <td>33</td>
      <td>40</td>
      <td>24</td>
    </tr>
    <tr>
      <td></td>
      <td>10–14</td>
      <td>70</td>
      <td>92</td>
      <td>47</td>
    </tr>
    <tr>
      <td></td>
      <td>15–20</td>
      <td>53</td>
      <td>65</td>
      <td>27</td>
    </tr>
    <tr>
      <td></td>
      <td>21–27</td>
      <td>77</td>
      <td>121</td>
      <td>56</td>
    </tr>
    <tr>
      <td></td>
      <td>28–35</td>
      <td>47</td>
      <td>62</td>
      <td>29</td>
    </tr>
    <tr>
      <td></td>
      <td>36–44</td>
      <td>38</td>
      <td>57</td>
      <td>4</td>
    </tr>
    <tr>
      <td></td>
      <td>45+</td>
      <td>38</td>
      <td>36</td>
      <td>2</td>
    </tr>
  </tbody>
</table>

### Clustering decreases PFR and depolarization during SBEs

The hypothetical set-point of the homeostatic process, however, is not the firing rate per se but the associated [Ca2+]i (Mattson and Kater, 1987), which is linked to molecular processes involved in growth and migration. Ca2+ influx increases supra-linearly with increasing membrane depolarization (Mazzanti et al., 1992). This suggests that the long-term Ca2+ gain is not a linear function of AFR but depends the depolarization of the membrane potential and thus on the temporal structure of activity. Depolarization depends on the number and synchronization of excitatory synaptic input, which becomes maximal during the peak phase of SBEs. Simultaneous intracellular and extracellular recording showed that higher SBE strength was indeed associated with stronger depolarization during SBEs (Okujeni et al., 2017). In PKC− networks, membrane depolarization high above spiking threshold frequently led to a depolarization block that outlasted the spike burst (Figure 4D top trace). The fraction of time spent above threshold (−40 mV, Figure 4E) was significantly larger in neurons of PKC− networks (5.2 ± 0.7%, p=1.7*10−4, N = 30 neurons; mean ± SEM, independent Student’s t-test) than in PKCN(1.7 ± 0.5%, N = 24) and PKC+(1.2 ± 0.7%, p=1.2*10−3, N = 24) networks (14–23 DIV). Depolarization was therefore not necessarily correlated with the individual firing rate of a neuron and the AFR in the network but rather reflected the network PFR during SBEs.

### Homeostatic regulation of growth by long-term Ca2+ influx

To assess how Ca2+ influx depends on PFR, we determined the amplitude of Ca2+ transients in excitatory neurons expressing GCaMP under the CAMKII promotor while simultaneously recording SBEs with MEAs (Figure 5A). Most neurons indeed showed an exponential relation between PFR and the amplitude of Ca2+ transients (Figure 5B). PKC− networks realized much higher PFRs and had somewhat smaller exponents than PKCN (PKCN0.12 ± 0.02, PKC−0.11 ± 0.01, p=3.2*10−18; Figure 5C,D,E).

![Figure 5.](https://cdn.elifesciences.org/articles/47996/elife-47996-fig5-v3.jpg)

**Figure 5.:** (A) Spiking raster and firing rate averaged across all electrodes within 40 ms bins (synchronized to the frame times of the Ca2+ measurement) and Ca2+ signal for one neuronal soma at 19 DIV in a PKCN network. Blue ticks: SBE onsets. (B) The amplitude of Ca2+ transients (shown for the PKCN neuron in A and a PKC− neuron at 20 DIV) scaled exponentially (solid line) with PFR. (C) Exponents had a narrow distribution and were slightly higher in PKCN (p=3.2*10−18) than in PKC− conditions (PKCN: 179 neurons, 5 networks at 19 DIV, 714 SBEs total, mean and standard deviation of exponent = 0.12 ± 0.02; PKC−: 622 neurons, 4 networks at 20 DIV, 248 SBEs total, exponent = 0.11 ± 0.01). Blue: average exponent (0.11 ± 0.01) for the entire data set. (D) Ca2+ amplitudes scaled exponentially with PFRs across many neurons in these PKCN and PKC− networks (E). The data represent median (data points) and standard deviation (error bars) of Ca2+ amplitudes, averaged across neurons for a given PFR range (bin size 0.1 Hz). (F) PFR assessed during SBEs were higher in homogeneous networks and lower in clustered networks. PFR decreased after week 3, putatively with the maturation of inhibition. (G) Prediction of the development of average Ca2+ influx per SBE estimated as $e^{0.11*PFR}-1$ (Figure 5D). (H) Average Ca2+ influx per minute, estimated from all SBEs in 1 hr recording sessions, suggests that long-term average Ca2+ influx in different PKC conditions converged at network maturation. Data in G and H are presented as mean ± SEM. Asterisks indicate p-values ≤0.05 (*), ≤0.01 (**) and ≤0.001 (***) tested against PKCN.

In all network types, PFR increased steeply in early development and later declined concurrently with SBE strength. Throughout development, however, PFRs were highest in homogeneous networks and lowest in clustered networks (Figure 5F, Table 2). Networks with low AFR thus had high PFR.

Knowing the relationship between PFR and Ca2+ influx allowed us to estimate Ca2+ levels during development based on MEA recordings. We approximated the development of the average Ca2+ influx per SBE (Figure 5G) from their respective PFRs and the exponential Ca2+ gain function with the average exponent of 0.11. Because higher PFRs, Ca2+ influx per SBE was highest in the more homogeneous PKC− networks and lowest in clustered PKC+ networks. Yet, in combination with the systematic increase of SBE rate with clustering, long-term Ca2+ influx converged during late development for different PKC conditions, network architectures and AFR (Figure 5H).

### Differences in PFR reflect variations of network recruitment during SBEs

The predominately short-range connectivity observed in clustered PKC+ networks could impair network-wide recruitment (Okujeni et al., 2017) and synchronization of activity. This would decorrelate inputs, explaining lower PFR and weaker membrane depolarization during SBEs. To test this, we determined network synchrony as the average spike correlations between all electrode pairs (Figure 6A). Consistent with the rapid buildup of connectivity, network synchrony increased steeply between 3–15 DIV and reached stable levels already between 15–21 DIV, even though activity levels, connectivity and inhibition continued to develop. In line with connectivity estimates, synchronization was highest in PKC− networks (0.53 ± 0.04, p=4.6*10−5 compared to PKCN), intermediate in PKCN networks (0.35 ± 0.02) and lowest in PKC+ networks (0.16 ± 0.03, p=1.7*10−5 compared to PKCN), that is network synchrony indeed decreased with the degree of clustering.

![Figure 6.](https://cdn.elifesciences.org/articles/47996/elife-47996-fig6-v3.jpg)

**Figure 6.:** (A) Network synchrony (average spike train correlation for all electrode pairs determined with 30 ms time bins, mean ± SEM) stabilized early in development in all PKC conditions but was significantly higher in homogeneous networks and significantly lower in clustered networks. Asterisks indicate p-values ≤0.05 (*), ≤0.01 (**) and ≤0.001 (***) tested against PKCN. (B) Inhibition was probed by acute blockade of GABA-A receptors with PTX. In early networks, PTX had highly variable impact on SBE strength (<14 DIV) but significantly increased it after 21 DIV in all network types. The maturation of inhibition was comparable across PKC conditions. (C) Illustration of the time course of key differentiation processes shown in detail in Figures 3 and 5 in relation to the development of long-term average Ca2+ influx. Morphological parameters that showed a similar time course across PKC conditions were normalized to final levels to visualize the relative change during development. The maturation of inhibition is shown as average relative change in SBE strength upon PTX appliction. Y-axis scaling is linear for all graphs. An offset was added for visualization.

### Maturation of inhibition is comparable across PKC conditions

Neural development involves a transition from excitatory to inhibitory GABAergic transmission by upregulation of the Cl--transporter KCC2. This maturation of inhibition considerably influences activity levels and dynamics, while being activity-dependent itself (Fiumelli and Woodin, 2007). Inhibition crucially affects network activity and thus interacts with Ca2+ influx and neuronal morphogenesis. Furthermore, since PKC promotes membrane incorporation of KCC2, reducing its activity could delay the maturation of inhibition and thus indirectly influence activity-dependent network development. To test if PKC manipulation altered the maturation of GABAergic inhibition on the network level, we blocked GABA-A receptor-dependent transmission at different developmental stages (10 µM PTX; Figure 6B) and recorded the resulting change of network activity with MEAs (number of recorded networks between 8–48 DIV; PKCN: N = 88; PKC−: N = 85; PKC+: N = 48). Acute application of PTX had variable impact on SBE strength up to 14 DIV (PKCN: +76 ± 31%, p=4.0*10−1, N = 33; PKC−: +62 ± 28%, p=3.6*10−3, N = 33; PKC+: +120 ± 45%, p=2.0*10−3, N = 24; mean ± SEM, paired Student’s t-test) but significantly amplified bursting after 21 DIV (PKCN: +785 ± 159%, p=1.4*10−5, N = 31; PKC−: +455 ± 103%, p=3.8*10−10, N = 29; PKC+: +524 ± 188%, p=3.7*10−2, N = 11). The developmental time course of the average PTX impact was comparable across PKC conditions, indicating a comparable maturation of GABAergic inhibition. We therefore concluded that the observed alterations in network dynamics were the result of differences in network architecture rather than the result of differences in inhibition levels.

## Discussion

Neuronal network architecture is not based on a genetic blueprint alone but is shaped by predefined rules of activity-dependent self-organization (Spitzer, 2006). Herein, neuronal migration (Komuro and Kumada, 2005; Zheng and Poo, 2007) and neurite outgrowth (Kater et al., 1988) are regulated by activity-related changes of [Ca2+]i. Indeed, cell motility and growth is optimal within a narrow [Ca2+] range and diminished otherwise, which led to the hypothesis that network connectivity and activity evolve under homeostatic control with the [Ca2+]i as set-point parameter (Kater and Mills, 1991). However, basal cytosolic [Ca2+] is very low due to efficient Ca2+-buffering and extrusion (Kater and Mills, 1991; Zündorf and Reiser, 2011) and remains relatively constant during development (Maravall et al., 2000). Free Ca2+ for the regulation of growth is thus essentially determined by transient [Ca2+]i elevations induced by synaptic input and spike activity. Accordingly, the developmentally attained spike rate was proposed to reflect the Ca2+ set-point of growth (van Ooyen et al., 1995).

The overall capacity for neurite growth ultimately relies on gene expression for cytoskeletal building blocks, which crucially depends on nuclear [Ca2+] (Berridge et al., 2000). Somatic membrane depolarization increases Ca2+ influx close to the nucleus (Greer and Greenberg, 2008). In this context, intracellular stores like the endoplasmic reticulum can accumulate Ca2+ over longer periods of time and then considerably amplify Ca2+ signals by additional Ca2+-triggered release (Berridge et al., 2000; Pivovarova et al., 2002). This effectively acts as a low-pass filter and amplifier for Ca2+-signaling to the nucleus – modulating the expression of cytoskeletal proteins. Supporting this link, neurite tree morphology and size in different neuron types appear to depend on the expression of specific Ca2+-binding proteins that determine nuclear Ca2+ buffering capacity (Mauceri et al., 2015). In contrast to nuclear Ca2+ levels, local Ca2+ transients in neurites direct migration and growth towards target neurons (Guan et al., 2007; Henley and Poo, 2004; Hutchins and Kalil, 2008), which promotes neurite overlap and synaptic connectivity (Shepherd et al., 2005; Stepanyants et al., 2002). Though local Ca2+ influx activating PKC modulates cytoskeletal turnover involved in guided outgrowth and migration (Fogh et al., 2014; Kabir et al., 2001; Larsson, 2006), PKC may not be essential for constitutive neurite outgrowth (Flynn, 2013; Letourneau et al., 1987). We therefore speculate that local Ca2+ transients and PKC activity regulate cytoskeletal motility to direct growth processes, whereas long-term accumulation of Ca2+ in intracellular stores modulates signaling to the nucleus, transcription levels and thus the overall availability of cytoskeletal building blocks. This predicts a cessation of growth at a target long-term average Ca2+ influx that is independent from PKC activity.

### Migration contributes to homeostatic network development

Extending on growth models for homeostatic network formation based on activity-dependent neurite outgrowth, neuronal migration could likewise contribute to the regulation of connectivity and activity in developing networks. Eglen et al. (2000) already added migration implemented as repulsion between neurons to the neurite growth model by van Ooyen et al. (1995) to generate regular neuronal arrangements as observed in dense retinal cell mosaics. We showed that activity-dependent attraction between migrating neurons leads to different degrees of modularity by the interaction of clustering with homeostatic regulation of neurite growth. While it is plausible to assume that neurons with small neurite fields and little connectivity may move, this seems less realistic once they are enmeshed in the network. In line with this, cell migration relies on localized Ca2+ transients in leading neurites and the resulting Ca2+ gradients across the cell (Guan et al., 2007) but ceases with increasing neuronal activity and frequency of Ca2+ transients (Bando et al., 2016). We approximated this in the model by allowing attraction while input was below the set-point but omitted repulsion with input above the set-point. In consequence, cell migration ended during the rapid increase of activity during development, similar to peaks in PFR and Ca2+ influx, and cessation of clustering around 10–15 DIV (Figure 3B, Figure 5F,H). Moreover, with rapid transitions to high network activity once neurite fields in the network overlapped sufficiently, the model showed a transient overshoot of connectivity. A more gradual build-up of activity diminished the average overshoot and pruning when the slope of the sigmoid mapping input to firing rate was reduced (Figure 2—figure supplement 2), in agreement with reports of varying degrees of growth overshoot or even saturating growth during development in vitro (Ito et al., 2013; Kondo et al., 2017; van Pelt et al., 2004). Neurons that connected to the network early in development, however, still showed an overshoot of connectivity, in agreement with Kossio et al. (2018).

### Average Ca2+ influx converges for different network architectures

Homeostatic regulation of growth processes by Ca2+ was proposed to guide network development towards target firing rates (van Ooyen et al., 1995), which implies a quasi-linear relationship between Ca2+ influx and AFR. In our model, connectivity, input activity and firing rates eventually converged to the same levels for different migration conditions and network architectures. In apparent conflict with the simulation, we found that different network architectures stabilized in vitro after about 3 weeks but with different AFR. Consistent with theoretical studies predicting that network modularity promotes spontaneous activity (Kaiser and Hilgetag, 2010; Klinshov et al., 2014; Mazzucato et al., 2015), SBE rates and AFRs increased with the level of clustering. Clustering, however, reduced network synchronization, lowered PFRs and weakened depolarization during SBEs. This strongly affected Ca2+-transients: Ca2+ peak amplitude increased exponentially with PFR during SBEs, in agreement with reports of Ca2+ currents through voltage-gated Ca2+ channels increasing exponentially with depolarization (Mayer et al., 1987; Mazzanti et al., 1992). Because of the opposite modulation of SBE rates and PFRs with clustering, however, the estimated long-term Ca2+-gain converged for different network architectures during development, despite different AFR. The low spike rates during inter-burst intervals had negligible influence on Ca2+ influx.

To account for the supra-linear increase of Ca2+ with PFR we would need to use spiking neurons in our model. In addition, Ca2+ influx would need to depend on the membrane potential, instead of on the average spike rate of a neuron as in extensions of the growth model with spiking dynamics (Abbott and Rohrkemper, 2007; Kossio et al., 2018). To accelerate the simulation of several weeks of network development, these studies initially increased the neurite growth rate and thus effectively decreased the temporal resolution until the networks approached the equilibrium state. The mesoscale structures forming in our networks, however, crucially depended on the continuous feedback between migration and neurite growth and activity. Low temporal resolution in the simulation would amount to a large decrease of the feedback speed, which leads to a random walk of neurons and more homogeneous network structures without clustering.

### Interaction between growth and migration shapes network modularity

Increasing the rate of activity-dependent migration in the model promoted clustering, decreased neurite fields and accelerated the development of spontaneous activity by more rapidly increasing neurite overlap and connectivity. This resulted in network architectures covering a continuous gradient from homogeneous via partially clustered with scattered neurons to fully clustered networks with corresponding degrees of modularity. This was remarkably similar to the development in vitro, where PKC activity promoted clustering and SBE rates, and decreased neurite density. The model suggests that different network architectures can arise spontaneously based on simple rules regulating connectivity to achieve a target level of [Ca2+]i.

Among the grand average developmental time courses of the most relevant aspects across all conditions, long-term Ca2+ influx was the first property to peak while the impact of inhibition on network activity only started to increase when Ca2+ influx stabilized (Figure 6C).

### Growth and migration shape the framework for synaptic connectivity

In our networks, synapse densities scaled approximately quadratically with the average dendrite size and thus negatively with the degree of clustering. This could be explained by the co-modulation of axonal and dendritic densities in the same direction (Okujeni et al., 2017), which multiplicatively increases the number of axo-dendritic contact sites, rather than their modulation in opposite directions as used in Tetzlaff et al. (2010). Such potential synapses realize into functional synapses with approximately constant probability in vivo (Stepanyants et al., 2002). The consistent relation of synapse density and dendrite size across developmental stages and PKC conditions (Figure 3G) suggests that PKC manipulation did not critically impair synaptogenesis. Our estimates of maximum connectivity suggest a saturation of connectivity towards 10% in clustered and 20% in homogeneous networks, in the range of values reported for cultured (Marom and Shahaf, 2002) and native cortical networks (Feldmeyer, 2012).

The mesoscale network architecture formed early thus appears to determine the probabilistic framework for connectivity. PKC activity additionally influences synaptic plasticity, yet without general directionality towards LTP or LTD (Chung et al., 2000; Ferreira et al., 2011; Lan et al., 2001; Boehm et al., 2006; ; Scott et al., 2007). Our model indirectly accommodates this influence. For example, synaptic depression, corresponding to reducing the synaptic weight factor $s$, would extend the outgrowth phase to increase connectivity and input necessary to reach the target level of [Ca2+]i. Conceptually, this would be the inverse of the homeostatic scaling of synaptic weights with the level of connectivity (Barral and D Reyes, 2016; Okujeni et al., 2017; Wilson et al., 2007). This contribution of synaptic plasticity to the activity-dependent fine-tuning of connectivity likely gains importance with increasing developmental age and structural complexity of a network.

### Conclusion

Based on our findings, we propose that interactions between neurite growth and neuronal migration affect the balance between local and global connectivity, thereby shaping network modularity. Cell migration defects were also proposed as a pathogenic mechanism involved in several neurological conditions associated with altered size and spacing of mini-columns in the cortex, aberrant neurite growth and hyper- or hypo-connectivity (Catts et al., 2013; Courchesne and Pierce, 2005; Di Rosa et al., 2009; Donovan and Basson, 2017; Fan et al., 2013; McKavanagh et al., 2015), suggesting that the mesoscale network organization could be a critical factor. The associated degree of modularity thus appears to have crucial impact on activity generation, propagation and perpetuation, neural synchronization as well as network function and dysfunction.

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
      <td>Strain, strain background (Rattus norvegicus domestica)</td>
      <td>wildtype wistar rat pups</td>
      <td>CEMT, University, Freiburg</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent</td>
      <td>AAV9.CAG.GCaMP6s.WPRE.SV40</td>
      <td>Penn Vector Core, University of Pennsylvania</td>
      <td>V3296TI-R</td>
      <td>titer 1e11</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-MAP2 (chicken polyclonal)</td>
      <td>Abcam, Cambridge, UK</td>
      <td>ab92434 RRID:AB_2138147</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-NeuN (rabbit polyclonal)</td>
      <td>Abcam, Cambridge, UK</td>
      <td>ab128886 RRID:AB_2744676</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Neurofilament (mouse monoclonal)</td>
      <td>Abcam, Cambridge, UK</td>
      <td>ab24571 RRID:AB_448148</td>
      <td>1:10</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Synapsin (mouse monoclonal)</td>
      <td>Synaptic Systems GmbH, Germany</td>
      <td>106001 RRID:AB_887805</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-chicken-Cy2 (goat polyclonal)</td>
      <td>Abcam, Cambridge, UK</td>
      <td>ab6960 RRID:AB_955003</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-rabbit-Cy3 (goat polyclonal)</td>
      <td>Abcam, Cambridge, UK</td>
      <td>ab6939 RRID:AB_955021</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-mouse-Cy5 (goat polyclonal)</td>
      <td>Abcam, Cambridge, UK</td>
      <td>ab6563 RRID:AB_955068</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>4,6-diamidino-2-phenyindole, diclactate (DAPI)</td>
      <td>Sigma-Aldrich, Germany</td>
      <td>D9562</td>
      <td>1:5000</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Gödecke6976</td>
      <td>Tocris Bioscience, Bristol, UK</td>
      <td>2253</td>
      <td>1 µM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Phorbol-12-Myristate-13-Acetate (PMA)</td>
      <td>Sigma-Aldrich, Munich, Germany</td>
      <td>P1585</td>
      <td>1 µM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Picrotoxin</td>
      <td>Tocris Bioscience, Bristol, UK</td>
      <td>1128</td>
      <td>10 µM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DMSO</td>
      <td>Sigma-Aldrich, Munich, Germany</td>
      <td>D8418</td>
      <td>0.1%</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DNase (type IV)</td>
      <td>Sigma-Aldrich, Munich, Germany</td>
      <td>D5025</td>
      <td>50 g/ml</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>minimal essential medium</td>
      <td>Invitrogen, Karlsruhe, Germany</td>
      <td>21090055</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>horse serum (heat-inactivated)</td>
      <td>Invitrogen, Karlsruhe, Germany</td>
      <td>26050088</td>
      <td>20%</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>phosphate buffered saline (PBS)</td>
      <td>Invitrogen, Karlsruhe, Germany</td>
      <td>21600010</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>glucose</td>
      <td>Sigma-Aldrich, Munich, Germany</td>
      <td>G7528</td>
      <td>20 mM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>L-glutamine</td>
      <td>Invitrogen, Karlsruhe, Germany</td>
      <td>25030024</td>
      <td>0.5 mM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>gentamycin</td>
      <td>Invitrogen, Karlsruhe, Germany</td>
      <td>15750060</td>
      <td>20 µg/ml</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>potassiumD-gluconate</td>
      <td>Sigma-Aldrich, Munich, Germany</td>
      <td>G4500</td>
      <td>125 mM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>EGTA</td>
      <td>Carl Roth, Karlsruhe, Germany</td>
      <td>3054</td>
      <td>5 mM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>KCl</td>
      <td>Sigma-Aldrich, Munich, Germany</td>
      <td>P4504</td>
      <td>20 mM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Na2-ATP</td>
      <td>Carl Roth, Karlsruhe, Germany</td>
      <td>K054</td>
      <td>2 mM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hepes</td>
      <td>Carl Roth, Karlsruhe, Germany</td>
      <td>9105</td>
      <td>10 mM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>CaCl2</td>
      <td>Sigma-Aldrich, Munich, Germany</td>
      <td>C3881</td>
      <td>0.5 mM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>KOH</td>
      <td>Sigma-Aldrich, Munich, Germany</td>
      <td>P4504</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>MgCl2</td>
      <td>Sigma-Aldrich, Munich, Germany</td>
      <td>MO250</td>
      <td>2 mM</td>
    </tr>
    <tr>
      <td>Software</td>
      <td>MC Rack software</td>
      <td>Multi Channel Systems, Germany</td>
      <td>versions 3.3–4.5 RRID:SCR_014955</td>
      <td></td>
    </tr>
    <tr>
      <td>Software</td>
      <td>Spike2 software</td>
      <td>Cambridge Electronics Design Ltd., Cambridge, UK.</td>
      <td>RRID:SCR_000903</td>
      <td></td>
    </tr>
    <tr>
      <td>Software</td>
      <td>Zen</td>
      <td>Carl Zeiss, Jena, Germany</td>
      <td>RRID:SCR_013672</td>
      <td></td>
    </tr>
    <tr>
      <td>Software</td>
      <td>MEA-Tools</td>
      <td>Egert et al., 2002 (PMID 12084562)</td>
      <td>version 2.8</td>
      <td></td>
    </tr>
    <tr>
      <td>Software</td>
      <td>FIND toolbox</td>
      <td>Meier et al., 2008 (PMID 18692360)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software</td>
      <td>ImageJ</td>
      <td>Schneider et al., 2012 (PMID 22930834)</td>
      <td>RRID:SCR_003070</td>
      <td></td>
    </tr>
    <tr>
      <td>Software</td>
      <td>Matlab</td>
      <td>Mathworks, Natick, MA, USA</td>
      <td>versions 2014a – 2017a</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Network growth model

We adopted and modified the model of activity-dependent network growth introduced by van Ooyen et al. (1995). All simulations were carried out with Matlab (version 2017a, Mathworks, Natick, MA, USA; code available at doi 10.5281/zenodo.3459678).

Networks were initialized by randomly seeding 500 neurons onto a torus surface of 1 mm2 to avoid boundary effects. Newly introduced neurons conflicting with the minimal neuron distance of 12 µm, approximately the size of cell bodies, were discarded and the procedure continued until the required neuron density was obtained.

Neurite fields were modeled as circular fields, centered at cell bodies and were initiated with a radius of 12 µm. Connectivity between neurons $W$ was nonsymmetrical and defined as the area $A$ of neurite field overlap normalized by the area of the presynaptic neuron, which reflected the probability that dendrites of neuron $i$ overlapped with the axons of presynaptic neuron $k$.

$$
W_{ki}=s\frac{A_{i}∩A_{k}}{A_{k}}
$$

The gain $s$ = 0.1 was chosen such that it produced networks with an intermediate degree of neurite field overlap (for $s$ = 1, neurons would only connect to one or a few other neurons). Instead of simulating network growth with dimensionless equations (van Ooyen et al., 1995), we adjusted the time steps such that we could compare the dynamics to realistic developmental timescales. We estimated the loop-time across which activity is integrated based on the time constants for the accumulation of Ca2+ in intracellular stores to be in the order of minutes (Pivovarova et al., 2002) and therefore set the temporal resolution of the simulation to 1 min.

Since inhibition is not explicitly relevant to the questions addressed here, we adapted the model for excitatory networks only. Long-term integration of activity in neurons was described by their state variable $x_{i}$ (ranging between 0 and 1), which increased with input from presynaptic neurons contributing with their firing rate $fx_{k}$ times the synaptic strength $W_{ki}$:

$$
\frac{dx_{i}}{dt}=-\frac{x_{i}}{\tau}+1-x_{i}\sumkNW_{ki}fx_{k}
$$

where $dt$= $\tau$= 1 min was the time resolution of the simulation, corresponding to the time constant of long-term integration of activity. A sigmoidal transfer function for the depolarization state $x_{i}$ determined the firing rate $fx$.

$$
fx_{i}=\frac{1}{1+e^{\theta-x_{i}/a}}
$$

where $\theta$ = 0.5 reflected the firing threshold and $a$ = 0.12 determined the steepness of the function that crucially impacted on the developmental overshoot of connectivity and subsequent pruning of neurites. We chose a slightly shallower function than the original model by Van Ooyen ($a$ = 0.1) to accommodate the degree of overshoot and pruning for cultured networks in recent reports (Ito et al., 2013; Kondo et al., 2017; van Pelt et al., 2004).

As in the original model by Van Ooyen, neurons were modeled to grow neurites and thereby increase input activity and firing rate to reach a target [Ca2+]i. If this Ca2+ level was surpassed, neurites were pruned, in turn. These bidirectional changes in the radius $R$ of circular neurite fields, were determined by a sigmoidal function of the firing rate of a neuron multiplied with a fixed growth rate $ρ_{growth}$.

$$
\frac{dR_{i}}{dt}=1-\frac{2}{1+e^{\frac{\epsilon-fx_{i}}{\beta}}}ρ_{growth}
$$

where $\epsilon$ = 0.6 defined the target level for activity or [Ca2+]i, $\beta$ = 0.1 determined the steepness of the sigmoidal function and $ρ_{growth}$ was the constant factor for the growth rate of neurite fields. We assumed that connectivity is mainly determined by the density of neurites rather than their maximal length. Given the homogeneous density of the neurite field used in the model, however, its radial expansion must be considerably slower than the average elongation rates of individual dendrites, which were reported to be 12 µm/day for isolated neurons in the first week in vitro (Mattson and Kater, 1988). We therefore set $ρ_{growth}$= 4 µm per day.

In our model, neurons additionally migrated in the direction of presynaptic inputs, thus mimicking the guidance of migration by leading processes (Flynn, 2013; Guan et al., 2007) and consistent with the positive correlation between the rate of soma translocation and the amplitude and frequency of Ca2+ transients (Komuro and Kumada, 2005; Zheng and Poo, 2007). We assumed synaptic activity in leading neurites as an important source of input, however, did not preclude contact-mediated Ca2+ signaling (Sheng et al., 2013), which may contribute in regulating migration early in development when activity levels are low. Changes in the spatial position of neuronal cell bodies S were caused by migration impulses that depended on [Ca2+]i and, thus, on the firing rate $f$ and a variable factor for the maximal migration rate $ρ_{migration}$.

$$
\frac{dS_{i}}{dt}=e^{µfx_{i}}ρ_{migration}
$$

where $ρ_{migration}$ ranged 0-300 µm/day and μ = -15 determined how strong migration impulses were diminished as neurons reached their target Ca2+ level. We chose μ to result in a negligible migration impulse at the target [Ca2+]i. This mimicked a realistic migration process in which neurons are guided by local Ca2+ transients in leading neurites and the resulting Ca2+ gradients across the cell (Guan et al., 2007), but at the same time cease migrating when spiking-based Ca2+ transients start to dominate (Bando et al., 2016). The migration speed of postnatal neurons in vitro indeed decays approximately exponentially during development from 0.7 µm/min (1008 µm/day) at 0 DIV to ~0.05 µm/min (72 µm/day) at 12 DIV on Matrigel-coated substrates and with slower initial migration speeds of 0.1 µm/min (144 µm/day) on PEI coated substrates (Sun et al., 2011), as used in this study. In the model we varied migration rates within this range.

The direction of movement was determined involving a directed movement component and a random movement component to match erratic movements observed in time lapse videos. Movement direction of the directed component was determined by the vector sum $v_{dir}$ of direction vectors $v_{ik}$ that pointed to presynaptic neurons and were weighted by their input.

$$
v_{dir}=-\sumkNW_{ki}fx_{k}v_{ik}
$$

To obtain the final direction vector $V$, directed and the random component (updated every 10 min) were weighted ($p$ = 0.9) and summed. The random directional component was necessary to mimic the erratic movement patterns observed in in vitro time lapse studies.

$$
V=\frac{v_{dir}}{v_{dir}}(1-p)+\frac{v_{rand}}{v_{rand}}p
$$

New neuronal cell body positions $P$ were determined by multiplying the normalized final direction vector with the migration impulse.

$$
P(x,y)_{new}=P(x,y)_{old}+\frac{v}{v}∙\frac{dS_{i}}{dt}
$$

In addition, neurons were set to jitter randomly around their current position by maximally their cell body radius to allow neurons to pass each other in the 2D simulation, which prevented unrealistic chains of neurons. This positional jitter decreased according to the exponential decay function modulating migration in dependence of [Ca2+]i such that neurons stopped moving when reaching the target value. It was reset after each time step. Movements violating the minimal possible inter-soma distance (12 µm) were discarded.

To assess the modularity of a network, we calculated the size of the largest subnetwork (the giant component) remaining after removing defined fractions of randomly selected neurons from the network as its fraction in the remaining total population. For each network, the results were averaged across 1000 repetitions of the procedure. We quantified the degree of modularity Q in the final networks based on the connectivity matrix using the Louvain method (Blondel et al., 2008) implemented for MATLAB by Mika Rubinov with gamma = 1 (Rubinov and Sporns, 2010). Q increases towards one with increasing modularity. Random networks yield Q = 0.

### Cell culture techniques

Primary cortical cell cultures were prepared on different MEAs (Multi Channel Systems, Reutlingen, Germany (MCS); electrode grid layout/pitch distance (µm): 8 × 8/200; 6 × 10/500; 16 × 16/200) and standard coverslips (12 mm diameter, Carl Roth, Karlsruhe, Germany). All substrates were coated with polyethylene-imine (150 µl 0.2% aqueous solution; Sigma-Aldrich, Munich, Germany) for cell adhesion. Cell cultures were prepared following (Shahaf and Marom, 2001). Cortical tissue was prepared from brains of neonatal Wistar rat pups of either sex, minced with a scalpel and transferred into phosphate buffered saline (Invitrogen, Karlsruhe, Germany). Tissue pieces were incubated with trypsin (isozyme mixture, 0.05%, 37°C, 15 min; Invitrogen). proteolysis was stopped with horse serum (20%; Invitrogen). DNase (type IV, 50 μg/ml; Sigma-Aldrich) was added to eliminate cell trapping in DNA strands if needed. Cells were dissociated by trituration with a serological pipette, centrifuged (5 min, 617 g) and resuspended in growth medium (Minimal Essential Medium supplemented with 5% heat-inactivated horse serum, 0.5–1 mM L-glutamine and 20 µg/ml gentamycin (all from Invitrogen), 20 mM glucose (Sigma); 1 ml/pup). Cells were counted with an automated cell counter (CASY, Schärfe Systems, Reutlingen, Germany) and seeded with ~300.000 cells per network (~1 cm2). Sparse cultures for morphological analysis were seeded with ~37.500 cells per network. Networks developed in 1 ml growth medium in a humidified incubator (5% CO2. 37°C). Animal handling and tissue preparation were done in accordance with the guidelines for animal research at the University of Freiburg and approved by the Regierungspräsidium Freiburg (permits X-12/08D, X-16/07A, X-15/01H, X-18/04K).

### PKC modulation and disinhibition

PKC inhibitor Gödecke6976 (Gö6976, 1 µM; Tocris Bioscience, Bristol, UK) and PKC agonist Phorbol-12-Myristate-13-Acetate (PMA, 1 µM; Sigma-Aldrich) were dissolved in dimethyl sulfoxide (DMSO, Sigma-Aldrich) and added to the culture medium directly after cell preparation. The maximal concentration of DMSO in the growth medium was 0.1%. GABAergic transmission was probed by acute application of the non-competitive GABA-A receptor antagonist Picrotoxin (PTX; 10 µM; Tocris Bioscience) during electrophysiological recordings. Recordings of spontaneous activity were started 10 min after application of PTX for 1 hr at different DIV. Changes of spike activity were calculated as mean burst strength across 1 hr with PTX vs. 1 hr baseline recording before application. Networks exposed to PTX were discarded.

### Morphological analyses

The development of neuronal clustering, dendrite outgrowth and synapse densities was analyzed in sparse networks of ~100 neurons/mm2 that were more accessible for quantitative morphological analysis. Clustering of neuronal cell bodies was analyzed based on immunocytochemical staining of neuronal nuclei (NeuN; Rabbit-anti-NeuN, 1:500; Abcam, Cambridge, UK, RRID:AB_2744676) and of all cellular nuclei (DAPI; Sigma-Aldrich). Neuronal nuclei were detected based on NeuN and DAPI colocalization and evaluated for their degree of clustering using a modified Clark-Evans clustering index (CI) that accounts for cell body diameter as minimal possible inter-neuron distance (Clark and Evans, 1954; Galli-Resta et al., 1999; Okujeni et al., 2017). CI was calculated as the ratio between the average nearest neighbor distance in a network and the expected average nearest neighbor distance for random networks. Note that the degree of clustering increases with decreasing CIs below 1. CIs above one indicate grid-like cell body arrangements. Dendrite morphology was examined by immunocytochemical staining of microtubule-associated protein 2 (MAP2, Chicken-anti-MAP2; 1:500; Abcam, RRID:AB_2138147). To quantify the total length of dendrites, MAP2 images taken at 20-fold magnification (0.323 µm/pixel) were processed by median filtering (3 × 3 kernel), background subtraction (lowest value in 7 × 7 pixel field), contrast adjustment (saturation at highest and lowest 10%), thresholding and skeletonization of the resulting binary image, similarly to Pani et al. (2014). Synapses were detected based on an immunohistological staining of the presynaptic protein synapsin (Mouse-anti-Synapsin; 1:200; Synaptic Systems GmbH, Göttingen, Germany, RRID:AB_887805). Synaptic punctae were then determined by local maximum detection in high-pass filtered and contrast-enhanced images. We analyzed two networks per condition and age taken from images covering approximately 3.5 mm2. In each image, we typically analyzed 10–20 regions of interest with varying size (could overlap) and including dense and sparse network regions. The following measures were determined as the slope of the linear regression through data pairs from all regions of interest: Dendrite size, total length of dendrite stretches relative to the number of neurons; Synapse density: average number of synapses relative to the number of neurons; Dendritic occupancy: average number of synapses relative to the total length of dendrite stretches; Neuron density, average number of neurons per area; Maximum connectivity, ratio between the number of synapses per neuron and the total number of neurons in the network (extrapolated for the entire network area of ~1.1 cm2 given the image neuron density). All morphometric analyses were done with Matlab (versions 2014a – 2017a). Results are presented as mean ± standard error of the mean (SEM) and significance was assessed with a two-tailed independent Student’s t-test. Network architectures of dense networks (600–800 neurons/mm2) were characterized qualitatively at 22 DIV with antibodies against MAP2 and phosphorylated neurofilament 200 kD (Rabbit-anti-neurofilament; 1:10; Abcam, RRID:AB_448148) to visualize dendritic and axonal compartments, respectively.

### Extracellular recording and analyses

MEA recordings (MEA1060-BC and USB-MEA256-Systems; MCS, 25 kHz sampling frequency, 12 bit AD-conversion; MCRack software versions 3.3–4.5, RRID:SCR_014955) of multi-unit spike activity from individual networks were performed under culture conditions (37°C, 5% CO2) and lasted at least 1 hr. Action potentials were detected with a threshold set to −5 standard deviations of the high-pass filtered baseline signal (Butterworth 2nd order high pass filter, 200 Hz cut-off; detection dead time 2 ms).

Raw data from MEA recordings was imported into Matlab using MEA-Tools (Egert et al., 2002) and the FIND toolbox (Meier et al., 2008). Spontaneous SBEs were detected as follows: Series of spikes with consecutive inter-spike intervals smaller than a threshold value (100 ms) were detected as bursts. SBEs were defined from periods in which a predefined fraction of electrodes showed simultaneous bursts (10% of all sites detecting spikes but minimally 3 and maximally 20 sites to keep criteria comparable between small and large MEAs). To account for buildup and fading phases of SBEs, spikes within a time windows of 25 ms prior to and following this SBE core were included into the SBE. Network activity was characterized by the following parameters: SBE rate in the recording period, SBE strength as the average number of APs per SBE divided by the number of electrodes with spikes at any time during the recording session (active sites); AFR as the grand average firing rate per active site during the recording session. PFR was calculated per SBE as the peak of the network-wide firing rate profile (box car filter applied to the global spike train; 0.2 s kernel width) divided by the number of active sites. Network synchrony was determined as average spike train correlation (30 ms bin width) between pairs of active sites.

For the developmental analysis of network activity, recordings from many networks were pooled within time windows of increasing width to account for the slowing development of activity dynamics as networks matured (Table 2). Numerical results are presented as mean ± SEM and significance was assessed with a two-tailed independent Student’s t-test.

For acute experiments with PTX, we defined as control period the last 1 hr section before application of PTX and excluded the first 10 min after application from the analysis to avoid transients due to handling. To determine the time course of the maturation of inhibition, changes in SBE strength following PTX application were quantified relative to the control period for different DIV. For visualization, trend lines were calculated with a sliding average (±7 DIV).

### Patch-clamp recording and analysis

Patch pipettes (6.3 ± 1.4 MΩ) were filled with a intracellular solution, containing potassium D-gluconate (125 mM; Sigma-Aldrich), KCl (20 mM; Sigma-Aldrich), EGTA (5 mM; Carl Roth), Na2-ATP (2 mM; Carl Roth), HEPES (10 mM; Carl Roth), MgCl2 (2 mM; Sigma-Aldrich) and CaCl2 (0.5 mM; Sigma-Aldrich), adjusted with KOH to pH 7.4, and with sucrose to 320 mOsm. Patch-clamp recordings in whole-cell configuration were conducted at 37°C (PH01 perfusion heating, MCS; TC02 temperature controller, MCS) and perfusion with carbogenated (95% O2 and 5% CO2; Air Liquide, Düsseldorf, Germany) culture medium without horse serum and without Gö6976 and PMA. Data were sampled at 25 kHz (Micro1401 amplifier and Spike2 software; Cambridge Electronics Design Ltd., Cambridge, UK (CED), RRID:SCR_000903). Up to four neurons were recorded sequentially per network for about 30 min each.

Data sets of at least 20 min were analyzed with Matlab. Membrane potential distributions for neurons with resting potentials between −64 ± 4 mV were determined for the entire recording period and averaged across neurons of the same PKC condition.

### Calcium measurements and analyses

To assess neuronal Ca2+ dynamics, cultures were transfected with AAV (=Adeno Associated Virus) vectors coding for GCaMP6s (AAV9.CAG.GCaMP6s.WPRE.SV40, titer:~1011; Penn Vector Core, School of Medicine Gene Therapy Program, University of Pennsylvania) under control of the CAG promotor after 10–14 days in vitro. Ca2+ dynamics were imaged at 20x magnification and 25 Hz frame rate (Examiner Z1 microscope, Zen software 2015, Carl Zeiss, Jena, Germany). Somatic regions were delineated by threshold detection in maximum projections of the Ca2+-movie with ImageJ (Schneider et al., 2012). The resulting regions of interest were corrected manually. Changes in the Ca2+ signal ΔF/F were calculated as relative change to baseline following (Jia et al., 2011). For each SBE, the peak of the Ca2+ signal (ΔF/F) within 200 ms after onset was related to the PFR determined from simultaneous MEA recordings. The exponential scaling between ΔF/F and PFR was assessed by fitting with the function $ΔF/F=e^{k*PFR}-1$ using the Matlab function fminsearch. Ca2+ data were derived from five PKCN and four PKC− networks at 19–20 DIV in recordings of ~30 min and analyzed with Matlab. Ca2+ influx during SBEs was estimated as $e^{0.11*PFR}-1$ to match the scaling found experimentally. Long-term Ca2+ influx was approximated as the Ca2+ influx integrated over all SBEs per hour. All results are presented as mean ± SEM. Significance was tested with a two-tailed independent Student’s t-test.

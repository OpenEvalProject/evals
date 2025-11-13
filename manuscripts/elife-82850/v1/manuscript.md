# Cytoarchitectonic, receptor distribution and functional connectivity analyses of the macaque frontal lobe

## Authors

- Lucija Rapan<sup>1</sup> ([ORCID: 0000-0002-6582-5826](https://orcid.org/0000-0002-6582-5826)) †
- Sean Froudist-Walsh<sup>2</sup>
- Meiqi Niu<sup>1</sup> ([ORCID: 0000-0001-7937-5814](https://orcid.org/0000-0001-7937-5814))
- Ting Xu<sup>4</sup>
- Ling Zhao<sup>1</sup>
- Thomas Funck<sup>1</sup>
- Xiao-Jing Wang<sup>2</sup> ([ORCID: 0000-0003-3124-8474](https://orcid.org/0000-0003-3124-8474))
- Katrin Amunts<sup>1</sup> ([ORCID: 0000-0001-5828-0867](https://orcid.org/0000-0001-5828-0867))
- Nicola Palomero-Gallagher<sup>1</sup> ([ORCID: 0000-0003-4463-8578](https://orcid.org/0000-0003-4463-8578))

### Affiliations

1. Institute of Neuroscience and Medicine INM-1, Research Centre Jülich Jülich Germany ([ROR:02nv7yv05](https://ror.org/02nv7yv05))
2. Center for Neural Science, New York University New York United States ([ROR:0190ak572](https://ror.org/0190ak572))
3. Bristol Computational Neuroscience Unit, Faculty of Engineering, University of Bristol Bristol United Kingdom ([ROR:0524sp257](https://ror.org/0524sp257))
4. Center for the Developing Brain, Child Mind Institute New York United States ([ROR:01bfgxw09](https://ror.org/01bfgxw09))
5. C. & O. Vogt Institute for Brain Research, Heinrich-Heine-University Düsseldorf Germany ([ROR:024z2rq82](https://ror.org/024z2rq82))

† Corresponding author

## Abstract

Based on quantitative cyto- and receptor architectonic analyses, we identified 35 prefrontal areas, including novel subdivisions of Walker’s areas 10, 9, 8B, and 46. Statistical analysis of receptor densities revealed regional differences in lateral and ventrolateral prefrontal cortex. Indeed, structural and functional organization of subdivisions encompassing areas 46 and 12 demonstrated significant differences in the interareal levels of α2 receptors. Furthermore, multivariate analysis included receptor fingerprints of previously identified 16 motor areas in the same macaque brains and revealed 5 clusters encompassing frontal lobe areas. We used the MRI datasets from the non-human primate data sharing consortium PRIME-DE to perform functional connectivity analyses using the resulting frontal maps as seed regions. In general, rostrally located frontal areas were characterized by bigger fingerprints, that is, higher receptor densities, and stronger regional interconnections. Whereas more caudal areas had smaller fingerprints, but showed a widespread connectivity pattern with distant cortical regions. Taken together, this study provides a comprehensive insight into the molecular structure underlying the functional organization of the cortex and, thus, reconcile the discrepancies between the structural and functional hierarchical organization of the primate frontal lobe. Finally, our data are publicly available via the EBRAINS and BALSA repositories for the entire scientific community.

## Introduction

The anterior portion of the primate frontal lobe, known as the prefrontal cortex (PFC), is a region notably involved in the higher cognitive functions (Fuster, 2008). It has been a focus region of numerous functional studies in human and monkey brains. Research involving non-human primates plays a vital role in the medical progress and scientific applications due to their close evolutionary relation to humans, but also due to ethical standards which do not allow all the vital material and data to be acquired directly from human brains (DeFelipe, 2015). In particular, macaque monkeys are the most widely used primate species in neurobiological research (Passingham, 2009). As a series of comparative analyses have shown, they share a similar basic architectonic plan to that of the human brain (Petrides et al., 2012; Petrides and Pandya, 1994; Petrides and Pandya, 1999; Petrides and Pandya, 2002; Petrides and Pandya, 2009).

Early cytoarchitectonic studies of the monkey cerebral cortex encountered the same issues and limitations as those of the human cortex with regard to both methodological and nomenclatural issues. Methodological limitations include small sample size, usually single of only a few cases, analysis of a single modality, and a subjective approach to the detection of cortical borders due to their identification by pure visual inspection. The nomenclature issue seems to be problematic as well since it not only affects comparability between different maps, but also translational analyses and identification of homolog areas in the human brain. The most influential cytoarchitectonic map of the monkey PFC was published by Walker, 1940, who used the numerical nomenclature introduced by Brodmann in his human brain map (Brodmann, 1909), although he did not compare the cytoarchitecture of the human and macaque monkey prefrontal regions in detail. Walker, 1940 labelled the frontopolar cortex of the monkey as area 10 and added areas 46 and 45 (Figure 1), which were not indicated in Brodmann’s map of the monkey frontal cortex (Brodmann, 1905). Thus, Walker’s (Walker, 1940) parcellation scheme became the basis for future microparcellation and anatomical–connectional studies with anterograde and retrograde tracers, as well as in physiological microstimulation studies (e.g. Barbas and Pandya, 1989; Carmichael and Price, 1996; Morecraft et al., 2012; Petrides and Pandya, 2006). This research led to a ‘golden era’ of experimental neuroanatomy with various research groups focused on the analysis of a specific region of interest (ROI) in the monkey brain, for example, the orbitofrontal (Barbas, 2007; Carmichael and Price, 1994), dorsolateral prefrontal (Petrides, 2005; Petrides and Pandya, 1999; Preuss and Goldman-Rakic, 1991), and ventrolateral PFC (Gerbella et al., 2007; Petrides and Pandya, 2002; Preuss and Goldman-Rakic, 1991).

![Figure 1.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig1-v1.jpg)

**Figure 1.:** Macroanatomical landmarks are marked with red dashed lines; cgs, cingulate sulcus; ias, inferior arcuate sulcus; ps, principal sulcus; ros, rostral orbital sulcus; sas, superior arcuate sulcus.

The development of a quantitative approach to the analysis of cytoarchitecture in the entire human brain sections enabled statistical validation of visually detectable cortical borders and thus an objective approach to brain mapping (Schleicher et al., 2009; Schleicher and Zilles, 1990). Furthermore, an implementation of the analyses, which include multiple architectonical modalities, also enabled a more comprehensive characterization of the cortical parcellation. Specifically, quantitative in vitro multireceptor autoradiography has been revealed as a powerful tool to describe the important aspects of the brain’s molecular and functional organization since neurotransmitters and their receptors are known to play an important role in a signalling process (Impieri et al., 2019; Palomero-Gallagher et al., 2009; Zilles et al., 2002). Concentrations of receptors for classical neurotransmitter systems vary between different cortical areas; hence, the area-specific balance of different receptor types (‘receptor fingerprint’) subserves its distinct functional properties. Quantification of heterogeneous receptors distribution throughout the cerebral cortex enables the identification and characterization of principal subdivisions such as primary sensory, primary motor, and hierarchically higher sensory or multimodal areas (Palomero-Gallagher and Zilles, 2019; Zilles and Palomero-Gallagher, 2017b). Multivariate analyses of the receptor fingerprints demonstrate not only structural but also functionally significant clustering of cortical areas (Zilles and Amunts, 2009). Therefore, this multimodal approach to cortical mapping provides detailed insights into the relationship between cytoarchitecture (which highlights the microstructural heterogeneity) and neurotransmitter receptor distributions (which emphasize the molecular aspects of signal processing) in the healthy non-human primate brain. It constitutes an objective and reliable tool which provides basic information of functional networks and precisely defined anatomical structures.

In vivo neuroimaging of the non-human primates has been advancing rapidly due to increased collaboration and data sharing (Milham et al., 2018; Milham et al., 2020). Primate imaging is a promising approach to link between precise electrophysiological and neuroanatomical studies of the cortex and distinct functional networks observed in humans. However, integration of neuroimaging data with high-quality postmortem anatomical data has been problematic since these results have not been conveyed in a common coordinate space. In recent years, several digital macaque atlases have been created (Bezgin et al., 2012; Frey et al., 2011; McLaren et al., 2009; Moirano et al., 2019; Reveley et al., 2017; Van Essen et al., 2012) based on the previous parcellations. Indeed, maps of Carmichael and Price, 1994; Petrides and Pandya, 2002; Petrides, 2005 and Preuss and Goldman-Rakic, 1991, used in atlas of Saleem and Logothetis, 2012, have been brought into stereotaxic space by Reveley et al., 2017. However, macaque maps, which are currently available to the in vivo neuroimaging researchers, do not contain information about receptor densities. Such information enables identification of the chemical underpinnings of functional activity and connectivity observed in vivo.

The primary aim of this study was to identify and characterize prefrontal areas based a quantitative cyto- and receptor architectonic approach, and to create a 3D statistically validated parcellation scheme in stereotaxic space. Since the functional connectivity analysis revealed a tight coupling between posterior prefrontal and premotor areas, and, also the fact that receptors play a key role in signal transduction, we hypothesized that this tight relationship would be associated with similarities in neurochemical composition. Thus, we decided to also include our previously published receptor fingerprints of (pre)motor areas (Rapan et al., 2021) in the multivariate analyses. Importantly, the densities of prefrontal and (pre)motor areas were all obtained from the same brains. All data are made available to the community in standard Yerkes19 surface via the EBRAINS repository of the Human Brain Project and the BALSA platform.

## Results

### Cytoarchitectonic analysis

The systematic identification of 35 prefrontal areas of every 20th coronal histological section of the brain DP1, as well as silver body-stained sections of brains 11530, 11539, 11543, resulted in a map containing the location and extent of all areas, and their relationships with macroanatomical landmarks is clearly depicted in Figure 2. Additionally, Table 1 was created to depict the relationship between areas defined by Rapan and colleagues (this study; Rapan et al., 2021) and referenced maps used here.

![Figure 2.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig2-v1.jpg)

**Figure 2.:** The files with the parcellation scheme are available via EBRAINS platform of the Human Brain Project (https://search.kg.ebrains.eu/instances/Project/e39a0407-a98a-480e-9c63-4a2225ddfbe4) and the BALSA neuroimaging site (https://balsa.wustl.edu/study/7xGrm). Macroanatomical landmarks are marked in red letters, while black dashed lines mark fundus of sulci. arcs, spur of the arcuate sulcus; cgs, cingulate sulcus; cs, central sulcus; ias, inferior arcuate sulcus; lf, lateral fissure; ps, principal sulcus; sas, superior arcuate sulcus.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Photographs of two of the postmortem brains used in this study. Brain ID DP1. (A) Macaca mulatta, and brain ID 11530 (B) Macaca fascicularis. Average surface representations of the Yerkes19. (C) Macaca mulatta template brains. arcs, spur of the arcuate sulcus; asd, anterior supracentral dimple; aspd, anterior superior principal dimple; cs, central sulcus; ias, inferior arcuate sulcus; ps, principal sulcus; pspd, posterior superior principal dimple; sas, superior arcuate sulcus; spcd, superior precentral dimple.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Areas are labelled on the left hemisphere, that is, prefrontal areas in black and previously mapped (pre)motor areas (Rapan et al., 2021) in grey. Due to limited space on the map, we used white arrows to mark anterior and posterior subdivisions of 46. Dashed yellow line on the hemispheres represents the midline, which separates medial and dorsolateral cortex. Black full lines mark the fundus of sulci. Macroanatomical landmarks are marked on the right hemisphere; arcs, spur of the arcuate sulcus; asd, anterior supracentral dimple; aspd, anterior superior principal dimple; cgs, cingulate sulcus; cs, central sulcus; ias, inferior arcuate sulcus; ipd, inferior principal dimple; lf, lateral fissure; lorb, lateraral orbital sulcus; morb, medial orbital sulcus; ps, principal sulcus; pspd, posterior superior principal dimple; sas, superior arcuate sulcus; spcd, superior precentral dimple.

**Table 1.**
 A list of cortical areas identified by the different authors (Walker, 1940; Petrides and Pandya, 1994; Petrides and Pandya, 2002; Preuss and Goldman-Rakic, 1991; Morecraft et al., 2012; Caminiti et al., 2017), whose maps were used as references for the present analysis, compared to areas identified by Rapan and colleagues.‘a46’, areas a46d, a46df, a46vf, a46v; ‘p46’, areas p46d, p46df, p46vf, p46v; ‘p46d’, areas p46d, p46df; ‘p46v’, areas p46v, p46vf.


<table>
  <thead>
    <tr>
      <th colspan="2">Walker vs.Rapan</th>
      <th colspan="2">Preuss &amp; Goldman-Rakic vs.Rapan</th>
      <th colspan="2">Carmichael &amp; Price vs.Rapan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">10</td>
      <td>10d</td>
      <td rowspan="4">10</td>
      <td>10d</td>
      <td rowspan="3">10m</td>
      <td>10d</td>
    </tr>
    <tr>
      <td>10md</td>
      <td>10md</td>
      <td>10md</td>
    </tr>
    <tr>
      <td>10mv</td>
      <td>10mv</td>
      <td>10mv</td>
    </tr>
    <tr>
      <td>10o</td>
      <td>10o</td>
      <td>10o</td>
      <td>10o</td>
    </tr>
    <tr>
      <td></td>
      <td>Rostral part of 'a46', 11m, 14r, 13b</td>
      <td></td>
      <td>Rostral part of a46d and a46v</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="3">9</td>
      <td>9d</td>
      <td rowspan="2">9d</td>
      <td>9d</td>
      <td rowspan="3">n.a.</td>
      <td rowspan="3"></td>
    </tr>
    <tr>
      <td>9l</td>
      <td>9l</td>
    </tr>
    <tr>
      <td>9m</td>
      <td>9m</td>
      <td>9m</td>
    </tr>
    <tr>
      <td>8B</td>
      <td>8Bd</td>
      <td rowspan="2">8Bd</td>
      <td>8Bd</td>
      <td rowspan="4">n.a.</td>
      <td rowspan="4"></td>
    </tr>
    <tr>
      <td></td>
      <td>8Bs</td>
      <td>8Bs</td>
    </tr>
    <tr>
      <td></td>
      <td>8Bm</td>
      <td>8Bm</td>
      <td>8Bm</td>
    </tr>
    <tr>
      <td></td>
      <td>Caudal part of 9d, 9l, and 9m</td>
      <td></td>
      <td>Caudal part of 9d, 9l, and 9m</td>
    </tr>
    <tr>
      <td>8A</td>
      <td>8Ad</td>
      <td>8Ar</td>
      <td>8Ad, 8Av, 45A, caudal part of 'p46'</td>
      <td rowspan="3">n.a.</td>
      <td rowspan="3"></td>
    </tr>
    <tr>
      <td></td>
      <td>8Av</td>
      <td>8Am</td>
      <td>8Ad</td>
    </tr>
    <tr>
      <td></td>
      <td>Caudal part of 'p46'</td>
      <td>8Ac</td>
      <td>8Av</td>
    </tr>
    <tr>
      <td rowspan="5">46</td>
      <td>a46'</td>
      <td>46r</td>
      <td>a46df, a46vf</td>
      <td rowspan="5">n.a.</td>
      <td rowspan="5"></td>
    </tr>
    <tr>
      <td>p46'</td>
      <td>46dr</td>
      <td>a46d, p46d, ventral part of 9l</td>
    </tr>
    <tr>
      <td>Dorsal part of 12r; ventral part of 9l</td>
      <td>46vr</td>
      <td>a46v, p46v, dorsal part of 12r</td>
    </tr>
    <tr>
      <td>Rostroventral part of 8Ad; rostrodorsal part of 45A</td>
      <td>46d</td>
      <td>a46df, p46df</td>
    </tr>
    <tr>
      <td></td>
      <td>46v</td>
      <td>a46vf, p46vf</td>
    </tr>
    <tr>
      <td rowspan="3">45</td>
      <td>45A</td>
      <td>45</td>
      <td>45B, 44</td>
      <td rowspan="3">n.a.</td>
      <td rowspan="3"></td>
    </tr>
    <tr>
      <td>45B</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Rostroventral part of 8Av</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>n.a.</td>
      <td></td>
      <td>n.a.</td>
      <td></td>
      <td>n.a.</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">12</td>
      <td>12r</td>
      <td rowspan="3">12vl</td>
      <td>12r</td>
      <td>12r</td>
      <td>12r</td>
    </tr>
    <tr>
      <td>12m</td>
      <td>12l</td>
      <td>12m</td>
      <td>12m, 12o</td>
    </tr>
    <tr>
      <td>12l</td>
      <td>Rostral part of 45A</td>
      <td>12l</td>
      <td>12l</td>
    </tr>
    <tr>
      <td>12o</td>
      <td></td>
      <td></td>
      <td>12o</td>
      <td>12o</td>
    </tr>
    <tr>
      <td></td>
      <td>Part of 45A; 13l</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">13</td>
      <td>13m</td>
      <td>13M</td>
      <td>13m</td>
      <td>13b</td>
      <td>13b</td>
    </tr>
    <tr>
      <td>13l</td>
      <td>13L</td>
      <td>13l</td>
      <td>13a</td>
      <td>13a</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>13m</td>
      <td>13m</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>13l</td>
      <td>13l</td>
    </tr>
    <tr>
      <td rowspan="2">11</td>
      <td>11m</td>
      <td rowspan="2">11</td>
      <td>11m</td>
      <td>11m</td>
      <td>11m</td>
    </tr>
    <tr>
      <td>11l</td>
      <td>11l</td>
      <td>11l</td>
      <td>11l</td>
    </tr>
    <tr>
      <td></td>
      <td>Part of12m, ventral part of 12l</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="2">14</td>
      <td>14r</td>
      <td>14A</td>
      <td>14r, 10o, 10mv, 11m, 13b</td>
      <td>14r</td>
      <td>14r</td>
    </tr>
    <tr>
      <td>14c</td>
      <td>14M</td>
      <td>14r, 14c</td>
      <td>14c</td>
      <td>14c</td>
    </tr>
    <tr>
      <td></td>
      <td>Part of 11m; 13b, 13a</td>
      <td>14L</td>
      <td>14r, 14c, 13b, 13a</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Petrides &amp; Pandya vs.Rapan</td>
      <td colspan="2">Morecraft vs.Rapan</td>
      <td colspan="2">Caminiti vs.Rapan</td>
    </tr>
    <tr>
      <td rowspan="4">10</td>
      <td>10d</td>
      <td rowspan="4">10</td>
      <td>10d</td>
      <td rowspan="4">10</td>
      <td>10d</td>
    </tr>
    <tr>
      <td>10md</td>
      <td>10md</td>
      <td>10md</td>
    </tr>
    <tr>
      <td>10mv</td>
      <td>10mv</td>
      <td>10mv</td>
    </tr>
    <tr>
      <td>10o</td>
      <td>10o</td>
      <td>10o</td>
    </tr>
    <tr>
      <td></td>
      <td>Rostral part of a46d and a46v; ventral part of 12r</td>
      <td></td>
      <td>Rostral part of a46d and a46v</td>
      <td></td>
      <td>Rostral part of a46d and a46v</td>
    </tr>
    <tr>
      <td rowspan="3">9</td>
      <td>9d</td>
      <td rowspan="2">9</td>
      <td>9d</td>
      <td rowspan="2">9l</td>
      <td>9d</td>
    </tr>
    <tr>
      <td>9l</td>
      <td>9l</td>
      <td>9l</td>
    </tr>
    <tr>
      <td>9m</td>
      <td>9m</td>
      <td>9m</td>
      <td>9m</td>
      <td>9m</td>
    </tr>
    <tr>
      <td rowspan="3">8B</td>
      <td>8Bd</td>
      <td rowspan="2">8Bd</td>
      <td>8Bd</td>
      <td rowspan="3">8B</td>
      <td>8Bd</td>
    </tr>
    <tr>
      <td>8Bs</td>
      <td>8Bs</td>
      <td>8Bs</td>
    </tr>
    <tr>
      <td>8Bm</td>
      <td>8Bm</td>
      <td>8Bm</td>
      <td>8Bm</td>
    </tr>
    <tr>
      <td></td>
      <td>Caudal part of 9d, 9l, and 9m</td>
      <td></td>
      <td>Caudal part of 9d, 9l, and 9m</td>
      <td></td>
      <td>Caudal part of 9d, 9l, and 9m</td>
    </tr>
    <tr>
      <td>8Ad</td>
      <td>8Ad</td>
      <td>8Ad</td>
      <td>8Ad</td>
      <td>8Ad</td>
      <td>8Ad</td>
    </tr>
    <tr>
      <td>8Av</td>
      <td>8Av</td>
      <td>8Av</td>
      <td>8Av</td>
      <td>8Av</td>
      <td>8Av</td>
    </tr>
    <tr>
      <td></td>
      <td>Caudal part of 'p46'</td>
      <td></td>
      <td>Caudal part of 'p46'</td>
      <td></td>
      <td>Caudal part of 'p46'</td>
    </tr>
    <tr>
      <td>46</td>
      <td>a46'</td>
      <td>46</td>
      <td>a46'</td>
      <td>46dr</td>
      <td>a46d, a46df</td>
    </tr>
    <tr>
      <td>9/46d</td>
      <td>p46d'</td>
      <td>9/46d</td>
      <td>p46d'</td>
      <td>46vr</td>
      <td>a46v, a46vf</td>
    </tr>
    <tr>
      <td>9/46v</td>
      <td>p46v'</td>
      <td>9/46v</td>
      <td>p46v'</td>
      <td>46dc</td>
      <td>Caudal part of a46d and a46df, 'p46d'</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>r46vc</td>
      <td>Caudal part of 'a46v', rostral part of 'p46v'</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>c46vc</td>
      <td>p46v, p46vf</td>
    </tr>
    <tr>
      <td>45A</td>
      <td>45A</td>
      <td>45</td>
      <td>45A</td>
      <td>45A</td>
      <td>45A</td>
    </tr>
    <tr>
      <td>45B</td>
      <td>45B</td>
      <td></td>
      <td></td>
      <td>45B</td>
      <td>45B</td>
    </tr>
    <tr>
      <td>44</td>
      <td>44</td>
      <td>44</td>
      <td>44, F5s</td>
      <td>n.a.</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">47/12</td>
      <td>12r</td>
      <td rowspan="2">47/12</td>
      <td>12r</td>
      <td>r12r</td>
      <td>12r</td>
    </tr>
    <tr>
      <td>12l</td>
      <td>12l</td>
      <td>i12r</td>
      <td>12r</td>
    </tr>
    <tr>
      <td>12m</td>
      <td></td>
      <td></td>
      <td>c12r</td>
      <td>12r, rostral part of 12l and 45A</td>
    </tr>
    <tr>
      <td>12o</td>
      <td></td>
      <td></td>
      <td>12l</td>
      <td>12l</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>12m</td>
      <td>12m, 12o</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>12o</td>
      <td>12o</td>
    </tr>
    <tr>
      <td>13</td>
      <td>13m</td>
      <td>n.a.</td>
      <td></td>
      <td>13a/13b</td>
      <td>13a, 13b</td>
    </tr>
    <tr>
      <td></td>
      <td>13l</td>
      <td></td>
      <td></td>
      <td>13m/13l</td>
      <td>13m, 13l</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11</td>
      <td>11l, part of 12r and 12m</td>
      <td>n.a.</td>
      <td></td>
      <td>11m</td>
      <td>11m</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>11l</td>
      <td>11l, 11m</td>
    </tr>
    <tr>
      <td rowspan="2">14</td>
      <td>14r</td>
      <td>14</td>
      <td>14r</td>
      <td rowspan="3">14</td>
      <td>14r</td>
    </tr>
    <tr>
      <td>14c</td>
      <td></td>
      <td>14c</td>
      <td>14c</td>
    </tr>
    <tr>
      <td></td>
      <td>Caudal part of 10mv; 13a, 13b</td>
      <td></td>
      <td>Caudal part of 10mv</td>
      <td>10mv</td>
    </tr>
  </tbody>
</table>

Additionally, Figure 2—figure supplements 1 and 2 show the characteristic macroanatomical features (i.e. dimples and sulci) of the macaque frontal lobe, used here to delineate our ROIs. The PFC is separated from the motor areas by the well-defined arcuate sulcus (arcs), which branches dorsally into the superior arcuate sulcus (sas) and ventrally into the inferior arcuate sulcus (ias), thus forming a letter Y on the lateral surface of the hemisphere. Ventrally, PFC is limited by the lateral fissure (lf), which represents the border with temporal areas, whereas on the medial surface, the cingulate sulcus (cgs) separates PFC from the limbic cortex. Another prominent feature on the lateral aspect of the PFC in the macaque monkey brain is the well-defined principal sulcus (ps), which starts rostrally within the frontopolar region and ends caudally within the arcuate convexity (Figure 2—figure supplement 2). These prominent macroanatomical features are recognizable in both macaque species (Macaca mulatta – brain ID DP1, and Macaca fascicularis – brain IDs rh11530, rh11539, and rh11543) studied here, as well as on the Yerkes19 surface used as a template for our 3D map (Figure 2—figure supplement 1).

In contrast, the orbitofrontal surface is characterized by a more variable sulcal pattern, comprised of lateral (lorb) and medial orbital sulcus (morb). In brain DP1 they are shown as two parallel, sagittally oriented sulci in the left hemisphere, while in the right hemisphere these sulci are partially connected forming a letter H (Figure 2—figure supplement 2). Though not as deep as sulci, there are several dimples within the PFC, for example, the anterior dimple (aspd) in its rostral part, and more caudally, the posterior dimple (pspd) in the dorsal PFC. Finally, ventral to the ps the inferior principal dimple (ipd) was recognizable only in the right hemisphere of DP1. The appearance of these dimples in three M. fascicularis brains is rather variable. Since the Yerkes19 atlas is based on structural MRI scans of 19 adult macaques, these dimples are missing from its surface (Figure 2—figure supplement 1).

As specified in the ‘Materials and methods’ section, previously published architectonic literature and nomenclature conventions were used as a starting point for the cytoarchitectonic analysis. All borders detected by visual inspection were then tested by image analysis and statistical validation, and the most distinguishing cytoarchitectonic features of the identified subdivisions belonging to the same area are summarized in Table 2.

**Table 2.**
 Prominent cytoarchitectonic features highlighted for all 35 identified prefrontal areas.


<table>
  <thead>
    <tr>
      <th>Area</th>
      <th>Layer IV</th>
      <th colspan="2">Cytoarchitecture</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>10d</td>
      <td rowspan="4">Granular</td>
      <td colspan="2">Small-size pyramids in III/V; dense granular layers II/IV</td>
    </tr>
    <tr>
      <td>10md</td>
      <td colspan="2">Wide, pale layer V</td>
    </tr>
    <tr>
      <td>10mv</td>
      <td colspan="2">Prominent middle-size pyramids in V</td>
    </tr>
    <tr>
      <td>10o</td>
      <td colspan="2">Prominent layer II</td>
    </tr>
    <tr>
      <td>14r</td>
      <td>Dysgranular</td>
      <td colspan="2">well-developed layer II; columnar pattern in IV-V</td>
    </tr>
    <tr>
      <td>14c</td>
      <td>Agranular</td>
      <td colspan="2">Pale layer III</td>
    </tr>
    <tr>
      <td>11m</td>
      <td rowspan="2">Granular</td>
      <td colspan="2">Sublamination of V (Va/Vb); cell clusters in Va</td>
    </tr>
    <tr>
      <td>11l</td>
      <td colspan="2">Sublamination of V (Va/Vb)</td>
    </tr>
    <tr>
      <td>13b</td>
      <td>Granular</td>
      <td colspan="2">Columnar pattern in IV-V</td>
    </tr>
    <tr>
      <td>13a</td>
      <td rowspan="3">Dysgranular</td>
      <td colspan="2">Sublamination of V (Va/Vb)</td>
    </tr>
    <tr>
      <td>13m</td>
      <td colspan="2">Sublamination of V (Va/Vb); layer Va wider than Vb</td>
    </tr>
    <tr>
      <td>13l</td>
      <td colspan="2">Sublamination of V (Va/Vb); both layers of comparable width</td>
    </tr>
    <tr>
      <td>12r</td>
      <td>Dysgranular</td>
      <td colspan="2">No sublamination of V</td>
    </tr>
    <tr>
      <td>12m</td>
      <td rowspan="2">Granular</td>
      <td colspan="2">Sublamination of V (Va/Vb)</td>
    </tr>
    <tr>
      <td>12l</td>
      <td colspan="2">Sublamination of V (Va/Vb)</td>
    </tr>
    <tr>
      <td>12o</td>
      <td>Dysgranula</td>
      <td colspan="2">No sublamination of V</td>
    </tr>
    <tr>
      <td>9m</td>
      <td rowspan="3">Granular</td>
      <td colspan="2">Sublamination of V (Va/Vb)</td>
    </tr>
    <tr>
      <td>9d</td>
      <td colspan="2">Gradient in cell-size within III; sublamination of V (Va/Vb);pale layer Vb is wider in 9d than 9l</td>
    </tr>
    <tr>
      <td>9l</td>
      <td colspan="2">Gradient in cell size within III; sublamination of V (Va/Vb)</td>
    </tr>
    <tr>
      <td>a46d</td>
      <td rowspan="4">Granular</td>
      <td rowspan="4">Scattered middle-sized pyramids in upper layer V</td>
      <td>Well-developed layer II</td>
    </tr>
    <tr>
      <td>a46df</td>
      <td>Scattered middle-sized pyramids in lower layer III</td>
    </tr>
    <tr>
      <td>a46vf</td>
      <td>Scattered middle-sized pyramids in layer III</td>
    </tr>
    <tr>
      <td>a46v</td>
      <td>Prominent layer II, but not as in a46d</td>
    </tr>
    <tr>
      <td>p46d</td>
      <td rowspan="4">Granular</td>
      <td rowspan="4">Cells more uniform in size throughout the cortex</td>
      <td>Well-developed layer II; densely packed cells in layer III</td>
    </tr>
    <tr>
      <td>p46df</td>
      <td>Densely packed cells in layer III; scattered middle-sized pyramids in lower layer III</td>
    </tr>
    <tr>
      <td>p46vf</td>
      <td>Scattered middle-sized pyramids in layer III</td>
    </tr>
    <tr>
      <td>p46v</td>
      <td>Prominent layer II, but not as in p46d</td>
    </tr>
    <tr>
      <td>8Bm</td>
      <td rowspan="3">Dysgranular</td>
      <td colspan="2">Layer VI pale compared to dorsal subdivisions</td>
    </tr>
    <tr>
      <td>8Bd</td>
      <td colspan="2">Dark, prominent layer II</td>
    </tr>
    <tr>
      <td>8Bs</td>
      <td colspan="2">Small size pyramids in III and V compared to 8Bd</td>
    </tr>
    <tr>
      <td>8Ad</td>
      <td rowspan="2">Granular</td>
      <td colspan="2">Upper layer III pale</td>
    </tr>
    <tr>
      <td>8Av</td>
      <td colspan="2">Lower layer III pale; highly granular cortex</td>
    </tr>
    <tr>
      <td>45A</td>
      <td rowspan="2">Granular</td>
      <td colspan="2">Middle-sized pyramids in layer III</td>
    </tr>
    <tr>
      <td>45B</td>
      <td colspan="2">Layer IV less developed</td>
    </tr>
    <tr>
      <td>44</td>
      <td>Dysgranular</td>
      <td colspan="2">Few larger pyramids scattered in layer V</td>
    </tr>
  </tbody>
</table>

### Frontopolar and orbital areas

The most rostral tip of the primate brain is occupied by the so-called frontal polar region (largely occupied by Walker’s area 10), where we identified four distinct areas (Figures 2 and 3A): that is, area 10d (dorsal) located on the dorsolateral surface of the frontal pole, areas 10mv (medioventral) and 10md (mediodorsal) on its medial surface, and 10o (orbital) on its most ventral aspect, occupying the rostral portion of the ventromedial gyrus. With a well-developed layer IV, this entire region represents a highly granular cortex, with slight differences in its appearance between the four defined areas, whereby medial areas 10md and 10mv show a slightly thinner layer IV compared to adjacent areas 10d and 10o, respectively (Figure 3B). Unlike the rest of area 10, area 10d has more densely packed layers II and V, with small-sized pyramids, whereas in the medial (10md/10mv) and orbital (10o) portions characteristic larger pyramids could be recognized in the upper part of layer V. 10mv can be distinguished from the neighbouring areas 10md and 10o by the much thinner appearance of its layer V. Additionally, the border between layers II and III is clearly visible in area 10o, but not in 10mv (Figure 3B). Figure 3C shows the result of the statistical validation of these newly defined subdivisions of area 10, as well as of the corresponding borders with adjacent areas.

![Figure 3.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig3-v1.jpg)

**Figure 3.:** (A) Position and extent of subdivisions of Walker’s area 10 within the hemisphere are displayed on orbital, lateral, and medial views of the Yerkes19. Macroanatomical landmarks are marked in red letters. (B) High-resolution photomicrographs show cytoarchitectonic features of areas 10d, 10md, 10mv, and 10o. Each subdivision is labelled by a coloured dot, matching the colour of the depicted area on the 3D model. (C) We confirmed cytoarchitectonic borders by a statistically testable method, where the Mahalanobis distance (MD) was used to quantify differences in the shape of profiles extracted from the region of interest. Profiles were extracted between outer and inner contour lines (yellow lines drawn between layers I/II and VI/white matter, respectively) defined on grey-level index (GLI) images of the histological sections (left column). Pink lines highlight the position of the border for which statistical significance was tested. The dot plots (right column) reveal that the location of the significant border remains constant over a large block size interval (highlighted by the red dots). (a) depicts analysis of the border between areas 10d and a46d (profile index 23); (b) depicts analysis of the border delineating dorsally located subdivisions, 10d and10md (profile index 48), as well as the medial border segregating dorsal and ventral subdivision, 10md and 10mv (profile index 127); and (c) depicts analysis of the borders between ventrally positioned subdivisions of the frontal polar region, 10mv and 10o (profile index 38) and 10o and 11m (profile index 81). Scale bar 1 mm. Roman numerals indicate cytoarchitectonic layers. arcs, spur of the arcuate sulcus; cgs, cingulate sulcus; cs, central sulcus; ias, inferior arcuate sulcus; ps, principal sulcus; sas, superior arcuate sulcus.

Twelve areas within the orbitofrontal and ventrolateral cortex (Figures 2 and 4A; Figure 4—figure supplements 1 and 2) were identified: two are located within Walker’s area 14 (14r and 14c), four are within Walker’s area 13 (13b, 13a, 13m, and 13l), two are in Walker’s area 11 (11m and 11l), and four are within Walker’s area 12 (12r, 12m, 12l, and 12o). Moving posteriorly along the ventromedial gyrus, granular cortex of area 10o transitions into dysgranular area 14r and further caudally into agranular area 14c. Similar to areas 14, subdivisions of area 13, which are found on the medial wall of the morb, show rostro-caudal differences in the appearance of their layer IV, that is, rostral area 13b is granular, whereas caudal area 13a is dysgranular (Figure 4B). However, unlike 14r and 14c, areas 13b and 13a have bilaminar layer V. Laterally, on the orbitofrontal gyrus, granular areas 11m and 11l occupy its rostral portion, while caudally dysgranular areas 13m and 13l are located, just rostral to the agranular insular region. The main difference among the subdivisions of area 11 is the pattern of cells in sublayer Vb, which is occasionally broken into aggregates of cells in area 11m, but continuous in area 11l. Similar, difference between 13m and 13l is related to the sublaminas V; that is, in 13m layer Va is wider that Vb, whereas in 13l both layers are of comparable width (Figure 4B). On the ventrolateral surface, the four subdivisions of Walker’s area 12 are distinguished by the degree of granularity of layer IV, and the size and distribution pattern of the pyramids in layers III and V (Figure 4B). The most rostral area on the medioventral surface of the prefrontal cortex, 12r, is a dysgranular cortex with characteristic columnar aspect in layers III and V. Area 12m, located on the lateral wall of the lorb, has a bipartite layer V and a well-developed layer IV which distinguishes it from surrounding areas 12r and 13l. Area 12o, located medial to 12l on the caudal medioventral convexity, has a thin and weakly stained layer IV, and no obvious sublamination in layer V. Area 12l is granular cortex with clear subdivisions in layer V (Figure 4B).

![Figure 4.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig4-v1.jpg)

**Figure 4.:** (A) Position and extent of the orbitofrontal areas within the hemisphere are displayed on orbital, lateral, and medial views of the Yerkes19. Macroanatomical landmarks are marked in red letters. (B) High-resolution photomicrographs show cytoarchitectonic features of orbitofrontal 14r, 14c, 11m, 11l, 12r, 12m, 12l, 12o, 13b, 13a, 13m, and 13l. Each subdivision is labelled by a coloured dot, matching the colour of the depict area on the 3D model. Scale bar 1 mm. Roman numerals (and letters) indicate cytoarchitectonic layers. arcs, spur of the arcuate sulcus; cgs, cingulate sulcus; cs, central sulcus; ias, inferior arcuate sulcus; ps, principal sulcus; sas, superior arcuate sulcus.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (a) Border between 14r and 10mv (profile index 55); (b) border between 14a and 13b (profile index 28); (c) border between 13b and 11m (profile index 38); (d) borders between 11m and 11l (profile index 110) and 11l and 12m (profile index 28); (e) border between 12m and 12r (profile index 43); and (f) border between 124 and a46v (profile index 31). For details see Figure 3.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (a) Border between 25 and 14c (profile index 26); (b) border between 14c and 13a (profile index 22); (c) border between 13a and 13m (profile index 40); (d) border between 13m and 13l (profile index 59); (e) border between 13l and 12o (profile index 56); and (f) border between 12o and 12l (profile index 76). For details see Figure 3.

### Medial and dorsolateral areas

The dorsal portion of the prefrontal cortex directly abutting area 10 of Walker is occupied by his area 9, within three distinct areas were identified (Figures 2 and 5A): area 9m, located on the medial surface between areas 10md rostrally and 8Bm caudally, is followed dorsally by area 9d, which in turn is delimited laterally by 9l (directly adjacent to area 46). Areas 9d and 9l are limited rostrally by area 10d and caudally by areas 8Bd and 8Bs, respectively. All subdivisions of area 9 are characterized by the low packing density and width of layer III, and the sublamination of layer V with a prominent Va containing relatively large pyramidal cells and a sparsely populated Vb, which distinguishes them from neighbouring areas (Figure 5B). This contrast between layers Va and Vb is particularly conspicuous in area 9l, thus clearly highlighting its border with area 9d (Figure 5C). Area 9d can be distinguished from 9l by its wider, pale layer V. The most recognizable feature of areas 9d and 9l, which is not visible in area 9m, is the gradual increase in the size of layer III pyramids, with largest cells found close to layer IV (Figure 5B).

![Figure 5.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig5-v1.jpg)

**Figure 5.:** (A) Position and extent of the rostral medial and dorsolateral prefrontal areas within the hemisphere are displayed on lateral and medial views of the Yerkes19. Macroanatomical landmarks are marked in red letters. (B) High-resolution photomicrographs show cytoarchitectonic features of areas 9m, 9d, and 9l. Each subdivision is labelled by a coloured dot, matching the colour of the depict area on the 3D model. (C) We confirmed cytoarchitectonic borders by statistically testable method (for details see Figure 3). (a) depicts analysis of the borders between area a46d and 9l (profile index 122), as well as 9l and 9d (profile index 44); (b) depicts analysis of the border between dorsal and medial subdivision, 9d and 9m (profile index 44); and (c) depicts analysis of the border distinguishing medial subdivision 9m from cingulate cortex, area 24 (profile index 35). Scale bar 1 mm. Roman numerals (and letters) indicate cytoarchitectonic layers. arcs, spur of the arcuate sulcus; cgs, cingulate sulcus; cs, central sulcus; ias, inferior arcuate sulcus; ps, principal sulcus; sas, superior arcuate sulcus.

As mentioned above, the dorsal portion of the most posterior part of the PFC is occupied by three subdivisions of Walker’s area 8B (Figures 2 and 6A): area 8Bm is located on the medial hemispheric surface, delimited caudally by the premotor cortex and rostrally by area 9m; area 8Bd is located on the dorsal surface along the midline; 8Bs is a newly identified area found on the cortical surface lateral to 8Bd and reaching the fundus of the sas. Walker’s area 8A occupies the cortex surrounding the most caudal portion of the ps, where it abuts areas p46. Here we identified area 8Ad dorsally, which extends into the ventral wall of the sas, reaching its fundus, and area 8Av ventrally, extending into the rostral wall of the ias, and also reaching its fundus (Figures 2 and 6A). Subdivisions of area 8B are dysgranular, whereas subdivisions of area 8A present a clearly developed layer IV (Figure 6B). Area 8Bm is more weakly laminated than 8Bd and 8Bs, but presents a columnar organization not visible in the lattermost areas. Area 8Bd is characterized by a more densely packed layer II and by lager pyramids in layers III and V than areas 8Bm or 8Bs. Both subdivisions of area 8A have a clear laminar structure, with a well-developed layer IV, which is especially wide and dense in 8Av (Figure 6B). All borders were statistically validated by the quantitative cytoarchitectonic analysis (Figure 6C; Figure 7—figure supplement 1 and Figure 8—figure supplement 2).

![Figure 6.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig6-v1.jpg)

**Figure 6.:** (A) Position and the extent of the caudal medial and dorsolateral prefrontal areas within the hemisphere are displayed on lateral and medial views of the Yerkes19. Macroanatomical landmarks are marked in red. (B) High-resolution photomicrographs show cytoarchitectonic features of areas 8B (8Bm, 8Bd, 8Bs) and 8A (8Ad, 8Av). Each subdivision is labelled by a coloured dot, matching the colour of the depict area on the 3D model. (C) We confirmed cytoarchitectonic borders of new 8B subdivisions by statistically testable method (for details see Figure 3). (a) depicts analysis of the border that separates new subdivisions 8Bs from neighbouring area 8Ad (profile index 25); (b) depicts analysis of the borders which delineate area 8Bd from surrounding areas 8Bs and 8Bm (profile index 69), as well as 8Bd and 8Bm (profile index 129); and (c) depicts analysis of the border distinguishing medial subdivision 8Bm from cingulate cortex, area 24 (profile index 37). Statistically testable borders for area 8Ad (adjacent to p46d) shown in Figure 7—figure supplement 2 and for area 8Av borders can be seen in the Figure 8—figure supplement 2. Scale bar 1 mm. Roman numerals (and letters) indicate cytoarchitectonic layers. arcs, spur of the arcuate sulcus; cgs, cingulate sulcus; cs, central sulcus; ias, inferior arcuate sulcus; ps, principal sulcus; sas, superior arcuate sulcus.

A mosaic of distinct areas was identified within Walker’s area 46 which encompasses our areas a46d, a46df, a46vf, a46v, p46d, p46df, p46vf, and p46v (Figures 2 and 7A; Figure 7—figure supplements 1 and 2). Such segregation results from a principal subdivision of area 46 into areas located within the anterior portion of the ps (the ‘a46-areas’) and those found in its posterior portion (the ‘p46-areas’), as well as differences between areas located on the dorsal (the ‘46d-areas’) and ventral (the ‘46v-areas’) shoulders of the sulcus, or around its fundus (the ‘46f-areas’), depicted on our schematic drawing of the ps (Figure 7A). Cytoarchitectonically, ‘a46’ and ‘p46’ areas can be distinguished by differences in the size of layer III and V pyramids, which are smaller in the posterior than in the anterior areas (Figure 7B). Dorsal subdivisions of area 46 have a wider and more densely packed layer II than the ventral areas, which, in turn, have more a more prominent layer IV, and larger cells in layers V and VI. Areas located around the fundus of the ps, that is, areas a46df/46vf and p46df/46vf, are additionally characterized by a clear border between layer VI and the white matter (Figure 7B).

![Figure 7.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig7-v1.jpg)

**Figure 7.:** (A) Position and the extent of areas located within and around the ps, are displayed on lateral view of the Yerkes19. Additionally, schematic drowning demonstrates how identified subdivisions are labelled with letters highlighted in red. Macroanatomical landmarks are marked in red letters. Black line indicates fundus, black dotted line marks border between shoulder and fundus region, and red dotted line separates anterior and posterior portion of sulcus. (B) High-resolution photomicrographs show cytoarchitectonic features of anterior areas of 46 (a46d, a46df, a46vf, a46v) and posterior ones (p46d, p46df, p46vf, p46v), separated by red dashed line. Each subdivision is labelled by a coloured dot, matching the colour of the depict area on the 3D model. Scale bar 1 mm. Roman numerals indicate cytoarchitectonic layers. arcs, spur of the arcuate sulcus; cs, central sulcus; ias, inferior arcuate sulcus; ps, principal sulcus; sas, superior arcuate sulcus.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** (a) Border between 9l and a46d (profile index 122); (b) borders between a46d and a46df (profile index 16) and a46df and a46vf (profile index 111); (c) border between ap46vf and a46v (profile index 38); and (d) border between a46v and 12l (profile index 35). For details see Figure 3.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig7-figsupp2-v1.jpg)

**Figure 7—figure supplement 2.:** (a) Border between 8Ad and p46d (profile index 42); (b) border between p46d and p46df (profile index 20); (c) borders between p46df and p46vf (profile index 39) and p46vf and p46v (profile index 124); and (d) border between p46v and 8Av (profile index 19). For details see Figure 3.

### Caudal ventral areas

Rostral to the ventral premotor cortex, we identified areas 44, 45A, and 45B (Figures 2 and 8A; Figure 8—figure supplements 1 and 2) belonging to the ventral granular PFC. Area 44 can be found along the deeper portion of the ventral wall of the ias, and encroaching onto its dorsal wall, where it abuts area 45B. The border between areas 45B and 45A was consistently found at the tip of the ias, whereby area 45A occupies the prearcuate convexity. Dysgranular areas 44 and granular area 45B can also be distinguished by differences in layer V which presents larger pyramids in the former than in the latter area (Figure 8B). Layer IV of 45A is wider than that of 45B. Additionally, layer III pyramids tend to build clusters in area 45B, but not in 45A (Figure 8B).

![Figure 8.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig8-v1.jpg)

**Figure 8.:** (A) Position and the extent of the posterior ventrolateral areas within the hemisphere are displayed on lateral view of the Yerkes19. Macroanatomical landmarks are marked in red letters. (B) High-resolution photomicrographs show cytoarchitectonic features of areas 44 and 45 (45A, 45B). Each subdivision is labelled by a coloured dot, matching the colour of the depict area on the 3D model. Scale bar 1 mm. Roman numerals indicate cytoarchitectonic layers. arcs, spur of the arcuate sulcus; cs, central sulcus; ias, inferior arcuate sulcus; ps, principal sulcus; sas, superior arcuate sulcus.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig8-figsupp1-v1.jpg)

**Figure 8—figure supplement 1.:** (a) Border between p46v and 45A (profile index 28); (b) border between 45A and 12l (profile index 44); and (c) border between 12l and 12o (profile index 26). For details see Figure 3.

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig8-figsupp2-v1.jpg)

**Figure 8—figure supplement 2.:** (a) Border between p46v and 8Av (profile index 19); (b) border between 8Av and 45B (profile index 30); (c) border between 45B and 44 (profile index 39); and (d) border between 44 and F5 (prolfile index 59). For details see Figure 3.

### Receptor architectonic analysis

The regional and laminar distribution patterns of 14 distinct receptor types were characterized throughout the macaque prefrontal cortex for each cytoarchitectonically defined area (with the exception for 13a and 14c due to technical limitations) by means of receptor profiles. Silver-stained sections from the corresponding receptor brain were aligned with the receptor autoradiographs at the same macroanatomic level in order to enable comparison of cytoarchitectonic border positions with receptor distribution patterns. Not all receptors show each areal border, and not all borders are equally clearly defined by all receptor types. Changes in receptor distribution patterns confirmed cytoarchitectonically identified borders, but did not reveal further subdivisions within the PFC.

In detail, neurotransmitter receptors display distinct laminar distribution patterns, which are preserved across all examined areas for most receptor types with the notable exception of the M2 receptors (Figure 9; Figure 9—figure supplements 1–3). In some areas M2 receptors present a single maximum in layer V (10mv, 10o, 14r, 13b, subdivisions of areas 11 and 46). Other areas present a bimodal pattern, with maxima in layers III and V. In some cases, both maxima are of comparable intensity (13m, 13l, subdivisions of area 12), and in other areas the maximum in layer III is clearly higher than that in layer V (10d, 10md, 44, and subdivisions of areas 9, 8B, 8A, and 45). Kainate receptors also constitute a notable exception because they are the only ones consistently presenting higher densities in the deeper than in the superficial cortical layers. The α1 and 5-HT1A receptors stand out due to their bimodal laminar distribution, with the highest of the two maxima located in the superficial layers. The remaining receptors present a rather unimodal laminar distribution pattern, whereby the width and position of the maximum varies depending on the receptor type. The D1 receptor reaches its maximum density in subcortical structures and a relatively homogeneous distribution throughout the neocortex.

![Figure 9.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig9-v1.jpg)

**Figure 9.:** The colour bar, positioned left to the autoradiographs, codes receptor densities in fmol/mg protein, and borders are indicated by black lines. The four schematic drawings at the top represent the distinct rostro-caudal levels and show the position of all prefrontal areas defined. C, caudal; D, dorsal; R, rostral; V, ventral.

![Figure 9—figure supplement 1.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig9-figsupp1-v1.jpg)

**Figure 9—figure supplement 1.:** The colour bar positioned left to the autoradiographs codes values of receptor densities in fmol/mg protein, and borders are indicated by the black lines.

![Figure 9—figure supplement 2.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig9-figsupp2-v1.jpg)

**Figure 9—figure supplement 2.:** The colour bar positioned left to the autoradiographs codes values of receptor densities in fmol/mg protein, and borders are indicated by the black lines.

![Figure 9—figure supplement 3.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig9-figsupp3-v1.jpg)

**Figure 9—figure supplement 3.:** The colour bar positioned left to the autoradiographs codes values of receptor densities in fmol/mg protein, and borders are indicated by the black lines.

Absolute receptor densities (averaged over all cortical layers) varied by several orders of magnitude depending on the receptor type (Table 3; Figure 10—figure supplement 1 and Figure 11—figure supplement 1). Highest absolute values were found for the GABAB receptor (2644 fmol/mg in 11l) and lowest densities for the D1 receptor (67 fmol/mg in 9l). Considerable differences in absolute densities were also found within a single neurotransmitter system. For example, highest muscarinic cholinergic densities were found for the M1 receptor (between 1152 fmol/mg in 12m and 708 fmol/mg in 8Av) and lowest for the M2 receptor (between 223 fmol/mg in 13l and 134 fmol/mg in 14r). In general, lowest receptor densities were measured in subdivisions of areas 8B and 8A, which consequently displayed the smallest fingerprints of all PFC areas. Conversely, highest receptor densities were mainly located in orbitofrontal and frontopolar areas (Figures 10 and 11; Figure 10—figure supplement 1 and Figure 11—figure supplement 1).

**Table 3.**
 Absolute receptor densities (mean ± SD) in fmol/mg protein.BZ, GABAA-associated benzodiazepine binding sites.


<table>
  <thead>
    <tr>
      <th>Area</th>
      <th>AMPA</th>
      <th>Kainate</th>
      <th>NMDA</th>
      <th>GABAA</th>
      <th>GABAB</th>
      <th>BZ</th>
      <th>M1</th>
      <th>M2</th>
      <th>M3</th>
      <th>α1</th>
      <th>α2</th>
      <th>5-HT1A</th>
      <th>5-HT2</th>
      <th>D1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>10dSD</td>
      <td>591161</td>
      <td>858116</td>
      <td>1430260</td>
      <td>1697162</td>
      <td>1970542</td>
      <td>2151829</td>
      <td>995230</td>
      <td>14135</td>
      <td>880117</td>
      <td>50775</td>
      <td>33768</td>
      <td>623169</td>
      <td>34075</td>
      <td>9320</td>
    </tr>
    <tr>
      <td>10mdSD</td>
      <td>586106</td>
      <td>89590</td>
      <td>1470177</td>
      <td>1651168</td>
      <td>2095495</td>
      <td>2307783</td>
      <td>1012274</td>
      <td>15445</td>
      <td>856112</td>
      <td>49448</td>
      <td>32748</td>
      <td>628151</td>
      <td>35760</td>
      <td>9020</td>
    </tr>
    <tr>
      <td>10mvSD</td>
      <td>628130</td>
      <td>90366</td>
      <td>1612151</td>
      <td>1680199</td>
      <td>2254606</td>
      <td>2451839</td>
      <td>1063332</td>
      <td>14535</td>
      <td>894124</td>
      <td>47194</td>
      <td>33456</td>
      <td>666214</td>
      <td>32067</td>
      <td>8618</td>
    </tr>
    <tr>
      <td>10oSD</td>
      <td>56976</td>
      <td>90950</td>
      <td>1523190</td>
      <td>1723160</td>
      <td>2336612</td>
      <td>2327774</td>
      <td>1068313</td>
      <td>15045</td>
      <td>923105</td>
      <td>47076</td>
      <td>34276</td>
      <td>682233</td>
      <td>35059</td>
      <td>8212</td>
    </tr>
    <tr>
      <td>14rSD</td>
      <td>47081</td>
      <td>818107</td>
      <td>1442255</td>
      <td>1427162</td>
      <td>2482424</td>
      <td>1715542</td>
      <td>921385</td>
      <td>13435</td>
      <td>833118</td>
      <td>497109</td>
      <td>29795</td>
      <td>583119</td>
      <td>32344</td>
      <td>8615</td>
    </tr>
    <tr>
      <td>11mSD</td>
      <td>604100</td>
      <td>77165</td>
      <td>1585139</td>
      <td>1762142</td>
      <td>2476466</td>
      <td>1975218</td>
      <td>1094200</td>
      <td>15964</td>
      <td>965132</td>
      <td>47350</td>
      <td>34240</td>
      <td>549167</td>
      <td>35760</td>
      <td>9227</td>
    </tr>
    <tr>
      <td>11lSD</td>
      <td>623111</td>
      <td>807123</td>
      <td>1562113</td>
      <td>1876235</td>
      <td>2644478</td>
      <td>2066247</td>
      <td>1050228</td>
      <td>15954</td>
      <td>944101</td>
      <td>46246</td>
      <td>35145</td>
      <td>529116</td>
      <td>35751</td>
      <td>9629</td>
    </tr>
    <tr>
      <td>13bSD</td>
      <td>48944</td>
      <td>820103</td>
      <td>1548223</td>
      <td>1615120</td>
      <td>2311452</td>
      <td>1901431</td>
      <td>1039263</td>
      <td>16657</td>
      <td>897104</td>
      <td>48073</td>
      <td>35075</td>
      <td>562206</td>
      <td>35557</td>
      <td>9322</td>
    </tr>
    <tr>
      <td>13mSD</td>
      <td>75367</td>
      <td>856111</td>
      <td>1499122</td>
      <td>1622126</td>
      <td>1908429</td>
      <td>1864269</td>
      <td>1059121</td>
      <td>20694</td>
      <td>918130</td>
      <td>48521</td>
      <td>41721</td>
      <td>527138</td>
      <td>35750</td>
      <td>7811</td>
    </tr>
    <tr>
      <td>13lSD</td>
      <td>71395</td>
      <td>75660</td>
      <td>1498187</td>
      <td>1683180</td>
      <td>2057240</td>
      <td>2052303</td>
      <td>1054148</td>
      <td>22378</td>
      <td>826108</td>
      <td>46115</td>
      <td>40426</td>
      <td>460107</td>
      <td>35143</td>
      <td>704</td>
    </tr>
    <tr>
      <td>12rSD</td>
      <td>659122</td>
      <td>854120</td>
      <td>1406121</td>
      <td>1843283</td>
      <td>2412312</td>
      <td>1991307</td>
      <td>1026301</td>
      <td>18072</td>
      <td>92296</td>
      <td>43938</td>
      <td>30652</td>
      <td>54088</td>
      <td>35051</td>
      <td>869</td>
    </tr>
    <tr>
      <td>12mSD</td>
      <td>598136</td>
      <td>79955</td>
      <td>1533175</td>
      <td>1792246</td>
      <td>2222353</td>
      <td>1873421</td>
      <td>1152262</td>
      <td>20274</td>
      <td>918108</td>
      <td>48148</td>
      <td>37971</td>
      <td>504103</td>
      <td>35445</td>
      <td>8622</td>
    </tr>
    <tr>
      <td>12lSD</td>
      <td>630112</td>
      <td>84073</td>
      <td>1400126</td>
      <td>1494221</td>
      <td>2010483</td>
      <td>1789417</td>
      <td>824347</td>
      <td>18275</td>
      <td>780132</td>
      <td>49182</td>
      <td>32043</td>
      <td>531163</td>
      <td>35148</td>
      <td>716</td>
    </tr>
    <tr>
      <td>12oSD</td>
      <td>670165</td>
      <td>81797</td>
      <td>1527158</td>
      <td>1579267</td>
      <td>2142414</td>
      <td>2102436</td>
      <td>888174</td>
      <td>20964</td>
      <td>832149</td>
      <td>48432</td>
      <td>40166</td>
      <td>54187</td>
      <td>38461</td>
      <td>8920</td>
    </tr>
    <tr>
      <td>9mSD</td>
      <td>607125</td>
      <td>81884</td>
      <td>1224252</td>
      <td>1460352</td>
      <td>2048235</td>
      <td>1864449</td>
      <td>868196</td>
      <td>16833</td>
      <td>76079</td>
      <td>50850</td>
      <td>30749</td>
      <td>629136</td>
      <td>35955</td>
      <td>8922</td>
    </tr>
    <tr>
      <td>9dSD</td>
      <td>584154</td>
      <td>76672</td>
      <td>1341206</td>
      <td>1633338</td>
      <td>2312235</td>
      <td>2081478</td>
      <td>1050177</td>
      <td>17634</td>
      <td>84180</td>
      <td>51540</td>
      <td>35559</td>
      <td>64281</td>
      <td>36261</td>
      <td>9224</td>
    </tr>
    <tr>
      <td>9lSD</td>
      <td>554151</td>
      <td>71156</td>
      <td>1311230</td>
      <td>1582324</td>
      <td>2173260</td>
      <td>1972464</td>
      <td>1029143</td>
      <td>16431</td>
      <td>82291</td>
      <td>49738</td>
      <td>36147</td>
      <td>59464</td>
      <td>36654</td>
      <td>6721</td>
    </tr>
    <tr>
      <td>a46dSD</td>
      <td>527138</td>
      <td>81081</td>
      <td>1247197</td>
      <td>1609253</td>
      <td>1993189</td>
      <td>1821349</td>
      <td>981234</td>
      <td>18740</td>
      <td>819114</td>
      <td>46268</td>
      <td>31865</td>
      <td>52186</td>
      <td>35466</td>
      <td>9026</td>
    </tr>
    <tr>
      <td>a46dfSD</td>
      <td>559126</td>
      <td>66744</td>
      <td>1348124</td>
      <td>1663219</td>
      <td>2071170</td>
      <td>1898444</td>
      <td>1083160</td>
      <td>17645</td>
      <td>86079</td>
      <td>47860</td>
      <td>38461</td>
      <td>46694</td>
      <td>35580</td>
      <td>9429</td>
    </tr>
    <tr>
      <td>a46vfSD</td>
      <td>619126</td>
      <td>67981</td>
      <td>1427102</td>
      <td>1752297</td>
      <td>2291280</td>
      <td>1873352</td>
      <td>1124161</td>
      <td>18047</td>
      <td>89494</td>
      <td>48447</td>
      <td>39539</td>
      <td>49788</td>
      <td>37676</td>
      <td>9330</td>
    </tr>
    <tr>
      <td>a46vSD</td>
      <td>50267</td>
      <td>80861</td>
      <td>1339167</td>
      <td>1614281</td>
      <td>2068200</td>
      <td>1908406</td>
      <td>1017235</td>
      <td>18752</td>
      <td>85685</td>
      <td>44052</td>
      <td>31935</td>
      <td>49679</td>
      <td>34958</td>
      <td>8717</td>
    </tr>
    <tr>
      <td>p46dSD</td>
      <td>563103</td>
      <td>78550</td>
      <td>1187318</td>
      <td>1449259</td>
      <td>1934231</td>
      <td>1786286</td>
      <td>889257</td>
      <td>18548</td>
      <td>77184</td>
      <td>43970</td>
      <td>30030</td>
      <td>48477</td>
      <td>36435</td>
      <td>8129</td>
    </tr>
    <tr>
      <td>p46dfSD</td>
      <td>592102</td>
      <td>69240</td>
      <td>1305254</td>
      <td>1649268</td>
      <td>2049177</td>
      <td>1978256</td>
      <td>1000241</td>
      <td>17643</td>
      <td>81284</td>
      <td>45378</td>
      <td>38847</td>
      <td>47886</td>
      <td>37342</td>
      <td>8522</td>
    </tr>
    <tr>
      <td>p46vfSD</td>
      <td>613115</td>
      <td>67171</td>
      <td>1369225</td>
      <td>1726315</td>
      <td>2295315</td>
      <td>2138383</td>
      <td>998230</td>
      <td>16341</td>
      <td>834115</td>
      <td>46774</td>
      <td>39567</td>
      <td>528107</td>
      <td>38148</td>
      <td>8824</td>
    </tr>
    <tr>
      <td>p46vSD</td>
      <td>51949</td>
      <td>75867</td>
      <td>1241207</td>
      <td>1444279</td>
      <td>1956213</td>
      <td>1814284</td>
      <td>810294</td>
      <td>17034</td>
      <td>78374</td>
      <td>41688</td>
      <td>32143</td>
      <td>46198</td>
      <td>36143</td>
      <td>8123</td>
    </tr>
    <tr>
      <td>8BmSD</td>
      <td>528136</td>
      <td>731128</td>
      <td>1018438</td>
      <td>1216217</td>
      <td>1888267</td>
      <td>1958236</td>
      <td>806173</td>
      <td>17831</td>
      <td>66787</td>
      <td>47270</td>
      <td>27349</td>
      <td>50880</td>
      <td>35132</td>
      <td>8327</td>
    </tr>
    <tr>
      <td>8BdSD</td>
      <td>48192</td>
      <td>641106</td>
      <td>973346</td>
      <td>1195151</td>
      <td>1896173</td>
      <td>2136385</td>
      <td>832131</td>
      <td>19541</td>
      <td>68092</td>
      <td>46673</td>
      <td>26370</td>
      <td>43789</td>
      <td>36247</td>
      <td>8928</td>
    </tr>
    <tr>
      <td>8BsSD</td>
      <td>49499</td>
      <td>57054</td>
      <td>1047348</td>
      <td>1232209</td>
      <td>1901389</td>
      <td>1931134</td>
      <td>831117</td>
      <td>16447</td>
      <td>682117</td>
      <td>43675</td>
      <td>30467</td>
      <td>484106</td>
      <td>35656</td>
      <td>8823</td>
    </tr>
    <tr>
      <td>8AdSD</td>
      <td>528115</td>
      <td>69465</td>
      <td>1108322</td>
      <td>1219200</td>
      <td>1972143</td>
      <td>1795301</td>
      <td>870227</td>
      <td>15837</td>
      <td>685139</td>
      <td>43867</td>
      <td>27236</td>
      <td>45082</td>
      <td>35943</td>
      <td>8229</td>
    </tr>
    <tr>
      <td>8AvSD</td>
      <td>44094</td>
      <td>591102</td>
      <td>1017264</td>
      <td>1205202</td>
      <td>1703264</td>
      <td>1807369</td>
      <td>708268</td>
      <td>16336</td>
      <td>603174</td>
      <td>347112</td>
      <td>25764</td>
      <td>262109</td>
      <td>32367</td>
      <td>7925</td>
    </tr>
    <tr>
      <td>45ASD</td>
      <td>55097</td>
      <td>73361</td>
      <td>1235165</td>
      <td>1461186</td>
      <td>1846280</td>
      <td>1810378</td>
      <td>880244</td>
      <td>16852</td>
      <td>73462</td>
      <td>422106</td>
      <td>32147</td>
      <td>394126</td>
      <td>35847</td>
      <td>7519</td>
    </tr>
    <tr>
      <td>45BSD</td>
      <td>601150</td>
      <td>58854</td>
      <td>1310271</td>
      <td>1472286</td>
      <td>1955301</td>
      <td>1911249</td>
      <td>972317</td>
      <td>14729</td>
      <td>705120</td>
      <td>44265</td>
      <td>37275</td>
      <td>499166</td>
      <td>37858</td>
      <td>8830</td>
    </tr>
    <tr>
      <td>44SD</td>
      <td>595162</td>
      <td>59286</td>
      <td>1310277</td>
      <td>1520220</td>
      <td>2065233</td>
      <td>1756294</td>
      <td>957339</td>
      <td>15422</td>
      <td>697164</td>
      <td>47579</td>
      <td>40270</td>
      <td>638253</td>
      <td>38557</td>
      <td>9327</td>
    </tr>
  </tbody>
</table>

![Figure 10.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig10-v1.jpg)

**Figure 10.:** Black dotted line on the plot represents the mean value over all areas for each receptor. Receptors displaying a negative z-score are indicative of absolute receptor densities which are lower than the average of that specific receptor over all examined areas. The opposite is true for positive z-scores. Labelling of different receptor types, as well as the axis scaling, is identical for each area plot, which is specified in the polar plot on the top of the figure.

![Figure 10—figure supplement 1.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig10-figsupp1-v1.jpg)

**Figure 10—figure supplement 1.:** Absolute receptor densities are given in fmol/mg protein. The positions of the different receptor types and the axis scaling are identical in all areas, and specified in the polar plot on the top of the figure.

![Figure 11.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig11-v1.jpg)

**Figure 11.:** Black dotted line on the plot represents the mean value over all areas for each receptor. Receptors displaying a negative z-score are indicative of absolute receptor densities which are lower than the average of that specific receptor over all examined areas. The opposite is true for positive z-scores. Labelling of different receptor types, as well as the axis scaling, is identical for each area plot, which is specified in the polar plot on the top of the figure. Due to the low receptor densities measured in area 8Av, scaling for its fingerprint is adjusted and shown directly on the corresponding polar plot.

![Figure 11—figure supplement 1.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig11-figsupp1-v1.jpg)

**Figure 11—figure supplement 1.:** Absolute receptor densities are given in fmol/mg protein. The positions of the different receptor types and the axis scaling are identical in all areas, and specified in the polar plot on the top of the figure.

Out of all prefrontal areas examined here, we found that the frontopolar region (i.e. areas 10) is characterized by the highest density of kainate and GABAA/BZ densities (Table 3). Changes in the laminar pattern of GABAA, M1, M2, α1, and 5HT1A receptors most clearly highlight the cytoarchitectonically defined borders within area 10 (Figure 9; Figure 9—figure supplements 1 and 2). Differences in the size of fingerprints particularly reflect the dorsoventral subdivision, with smaller sized fingerprints in areas 10d/10md compared to 10mv/10o (Figure 10; Figure 10—figure supplement 1). Both ventrally positioned subdivisions of area 10 (i.e. areas 10mv and 10o) differed significantly from caudally adjacent area 14r, though not always for the same receptor types (Table 4). Area 14r presented significantly lower AMPA and GABAA receptor densities than 10mv and 10o, respectively. Additionally, GABAA/BZ densities in 10mv and 10o were significantly higher than in 14r. Likewise, dorsal subdivisions of area 10 presented a differential pattern of significant receptor densities compared to neighbouring areas. Areas 10d and 10md contain significantly higher kainate and NMDA receptor densities, respectively, than caudally adjacent subdivisions of area 9.

**Table 4.**
 FDR-corrected p-values for the post hoc tests (i.e. third-level tests; p-values were corrected for 258 comparisons per receptor type).No p-values are provided for the M1, M2, 5-HT2, or D1 receptors because they did not reach the level of significance in the second-level test. Green background highlights significant pairs of adjacent prefrontal areas in the macaque brain. *p<0.05, **p<0.01, ***p<0.001.


<table>
  <thead>
    <tr>
      <th></th>
      <th>AMPA</th>
      <th>Kainate</th>
      <th>NMDA</th>
      <th>GABAᴀ</th>
      <th>GABAB</th>
      <th>BZ</th>
      <th>M3</th>
      <th>α1</th>
      <th>α2</th>
      <th>5-HT1A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>10d - 10md</td>
      <td>0.9393</td>
      <td>0.5591</td>
      <td>0.8028</td>
      <td>0.8776</td>
      <td>0.6976</td>
      <td>0.7871</td>
      <td>0.7553</td>
      <td>0.9104</td>
      <td>0.866</td>
      <td>0.9753</td>
    </tr>
    <tr>
      <td>10d - 9d</td>
      <td>0.9041</td>
      <td>0.1142</td>
      <td>0.5721</td>
      <td>0.8364</td>
      <td>0.1413</td>
      <td>0.8728</td>
      <td>0.6135</td>
      <td>0.9104</td>
      <td>0.5692</td>
      <td>0.9081</td>
    </tr>
    <tr>
      <td>10d - 9l</td>
      <td>0.618</td>
      <td>0.0091**</td>
      <td>0.4329</td>
      <td>0.5871</td>
      <td>0.4474</td>
      <td>0.7277</td>
      <td>0.4173</td>
      <td>0.9549</td>
      <td>0.4603</td>
      <td>0.746</td>
    </tr>
    <tr>
      <td>10d - a46d</td>
      <td>0.3472</td>
      <td>0.4435</td>
      <td>0.194</td>
      <td>0.7085</td>
      <td>0.9711</td>
      <td>0.3149</td>
      <td>0.3845</td>
      <td>0.5571</td>
      <td>0.6929</td>
      <td>0.1842</td>
    </tr>
    <tr>
      <td>10md - 10mv</td>
      <td>0.6304</td>
      <td>0.8867</td>
      <td>0.3033</td>
      <td>0.9407</td>
      <td>0.4908</td>
      <td>0.8415</td>
      <td>0.586</td>
      <td>0.7554</td>
      <td>0.8435</td>
      <td>0.7195</td>
    </tr>
    <tr>
      <td>10md - 9m</td>
      <td>0.8231</td>
      <td>0.1508</td>
      <td>0.0461*</td>
      <td>0.1826</td>
      <td>0.8701</td>
      <td>0.1242</td>
      <td>0.1456</td>
      <td>0.8313</td>
      <td>0.5417</td>
      <td>0.9816</td>
    </tr>
    <tr>
      <td>10mv - 10o</td>
      <td>0.4391</td>
      <td>0.9801</td>
      <td>0.5458</td>
      <td>0.8064</td>
      <td>0.7872</td>
      <td>0.8587</td>
      <td>0.7441</td>
      <td>0.9973</td>
      <td>0.8276</td>
      <td>0.9081</td>
    </tr>
    <tr>
      <td>10mv - 14r</td>
      <td>0.0386*</td>
      <td>0.149</td>
      <td>0.2167</td>
      <td>0.1305</td>
      <td>0.3529</td>
      <td>0.0291*</td>
      <td>0.3522</td>
      <td>0.7752</td>
      <td>0.2444</td>
      <td>0.3143</td>
    </tr>
    <tr>
      <td>10o - 11m</td>
      <td>0.7018</td>
      <td>0.0056**</td>
      <td>0.6676</td>
      <td>0.8425</td>
      <td>0.5291</td>
      <td>0.2996</td>
      <td>0.5396</td>
      <td>0.9549</td>
      <td>0.9936</td>
      <td>0.0666</td>
    </tr>
    <tr>
      <td>10o - 14r</td>
      <td>0.168</td>
      <td>0.1227</td>
      <td>0.5525</td>
      <td>0.0366*</td>
      <td>0.5751</td>
      <td>0.0291*</td>
      <td>0.1793</td>
      <td>0.7645</td>
      <td>0.1471</td>
      <td>0.2115</td>
    </tr>
    <tr>
      <td>11l - 11m</td>
      <td>0.8207</td>
      <td>0.5126</td>
      <td>0.8931</td>
      <td>0.4519</td>
      <td>0.4832</td>
      <td>0.8721</td>
      <td>0.7807</td>
      <td>0.9104</td>
      <td>0.7881</td>
      <td>0.8618</td>
    </tr>
    <tr>
      <td>11l - 12m</td>
      <td>0.8207</td>
      <td>0.9666</td>
      <td>0.9271</td>
      <td>0.7045</td>
      <td>0.058</td>
      <td>0.7409</td>
      <td>0.7964</td>
      <td>0.8085</td>
      <td>0.3854</td>
      <td>0.8686</td>
    </tr>
    <tr>
      <td>11l - 12r</td>
      <td>0.5848</td>
      <td>0.3727</td>
      <td>0.2291</td>
      <td>0.8932</td>
      <td>0.2739</td>
      <td>0.8721</td>
      <td>0.7446</td>
      <td>0.7645</td>
      <td>0.1325</td>
      <td>0.917</td>
    </tr>
    <tr>
      <td>11l - 13l</td>
      <td>0.2408</td>
      <td>0.6732</td>
      <td>0.9223</td>
      <td>0.4866</td>
      <td>0.0523</td>
      <td>0.9766</td>
      <td>0.2814</td>
      <td>0.9549</td>
      <td>0.1427</td>
      <td>0.7352</td>
    </tr>
    <tr>
      <td>11l - 13m</td>
      <td>0.1005</td>
      <td>0.4105</td>
      <td>0.9256</td>
      <td>0.3035</td>
      <td>0.0104*</td>
      <td>0.8678</td>
      <td>0.9487</td>
      <td>0.7645</td>
      <td>0.0781</td>
      <td>0.9081</td>
    </tr>
    <tr>
      <td>11m - 13b</td>
      <td>0.0988</td>
      <td>0.3998</td>
      <td>0.8028</td>
      <td>0.3063</td>
      <td>0.4593</td>
      <td>0.8728</td>
      <td>0.2991</td>
      <td>0.9549</td>
      <td>0.8403</td>
      <td>0.917</td>
    </tr>
    <tr>
      <td>11m - 13l</td>
      <td>0.1593</td>
      <td>0.9801</td>
      <td>0.8261</td>
      <td>0.8911</td>
      <td>0.208</td>
      <td>0.8652</td>
      <td>0.19</td>
      <td>0.9795</td>
      <td>0.0925</td>
      <td>0.6198</td>
    </tr>
    <tr>
      <td>11m - 13m</td>
      <td>0.06</td>
      <td>0.1684</td>
      <td>0.8261</td>
      <td>0.698</td>
      <td>0.0554</td>
      <td>0.9766</td>
      <td>0.7943</td>
      <td>0.8541</td>
      <td>0.0465*</td>
      <td>0.997</td>
    </tr>
    <tr>
      <td>11m - 14r</td>
      <td>0.0688</td>
      <td>0.4928</td>
      <td>0.2895</td>
      <td>0.0159*</td>
      <td>0.9809</td>
      <td>0.489</td>
      <td>0.0347*</td>
      <td>0.812</td>
      <td>0.149</td>
      <td>0.8153</td>
    </tr>
    <tr>
      <td>12l - 12o</td>
      <td>0.7396</td>
      <td>0.7221</td>
      <td>0.5477</td>
      <td>0.7785</td>
      <td>0.7117</td>
      <td>0.5449</td>
      <td>0.591</td>
      <td>0.9338</td>
      <td>0.0323*</td>
      <td>0.9837</td>
    </tr>
    <tr>
      <td>12l - 12r</td>
      <td>0.7423</td>
      <td>0.84</td>
      <td>0.9808</td>
      <td>0.0261*</td>
      <td>0.0824</td>
      <td>0.7523</td>
      <td>0.0613</td>
      <td>0.3864</td>
      <td>0.6495</td>
      <td>0.9869</td>
    </tr>
    <tr>
      <td>12l - 45A</td>
      <td>0.2779</td>
      <td>0.0773</td>
      <td>0.2152</td>
      <td>0.8729</td>
      <td>0.4924</td>
      <td>0.9984</td>
      <td>0.5606</td>
      <td>0.148</td>
      <td>0.9231</td>
      <td>0.0933</td>
    </tr>
    <tr>
      <td>12m - 12o</td>
      <td>0.4391</td>
      <td>0.8664</td>
      <td>0.9223</td>
      <td>0.1851</td>
      <td>0.7851</td>
      <td>0.7313</td>
      <td>0.2335</td>
      <td>0.9973</td>
      <td>0.6306</td>
      <td>0.7877</td>
    </tr>
    <tr>
      <td>12m - 12r</td>
      <td>0.4191</td>
      <td>0.3735</td>
      <td>0.3465</td>
      <td>0.8326</td>
      <td>0.4936</td>
      <td>0.8721</td>
      <td>0.9602</td>
      <td>0.5104</td>
      <td>0.0176*</td>
      <td>0.7772</td>
    </tr>
    <tr>
      <td>12m - 13l</td>
      <td>0.1742</td>
      <td>0.7207</td>
      <td>0.9867</td>
      <td>0.7785</td>
      <td>0.7649</td>
      <td>0.7496</td>
      <td>0.4295</td>
      <td>0.929</td>
      <td>0.5069</td>
      <td>0.8618</td>
    </tr>
    <tr>
      <td>12o - 12r</td>
      <td>0.9669</td>
      <td>0.5144</td>
      <td>0.4782</td>
      <td>0.0923</td>
      <td>0.2583</td>
      <td>0.8587</td>
      <td>0.2335</td>
      <td>0.5575</td>
      <td>0.004**</td>
      <td>0.9881</td>
    </tr>
    <tr>
      <td>12o - 13l</td>
      <td>0.5736</td>
      <td>0.6021</td>
      <td>0.9649</td>
      <td>0.5306</td>
      <td>0.9429</td>
      <td>0.9901</td>
      <td>0.9049</td>
      <td>0.929</td>
      <td>0.8128</td>
      <td>0.6789</td>
    </tr>
    <tr>
      <td>12r - a46v</td>
      <td>0.0151*</td>
      <td>0.3743</td>
      <td>0.6393</td>
      <td>0.0962</td>
      <td>0.0824</td>
      <td>0.8738</td>
      <td>0.3415</td>
      <td>0.9973</td>
      <td>0.7023</td>
      <td>0.6442</td>
    </tr>
    <tr>
      <td>12r - p46v</td>
      <td>0.0427*</td>
      <td>0.0659</td>
      <td>0.2246</td>
      <td>0.0032**</td>
      <td>0.019*</td>
      <td>0.7409</td>
      <td>0.0347*</td>
      <td>0.7253</td>
      <td>0.6634</td>
      <td>0.3438</td>
    </tr>
    <tr>
      <td>13b - 14r</td>
      <td>0.8536</td>
      <td>0.973</td>
      <td>0.4654</td>
      <td>0.2172</td>
      <td>0.4936</td>
      <td>0.7277</td>
      <td>0.339</td>
      <td>0.88</td>
      <td>0.1052</td>
      <td>0.9081</td>
    </tr>
    <tr>
      <td>13l - 13m</td>
      <td>0.7624</td>
      <td>0.2909</td>
      <td>0.9979</td>
      <td>0.8563</td>
      <td>0.7452</td>
      <td>0.8587</td>
      <td>0.4298</td>
      <td>0.8565</td>
      <td>0.8354</td>
      <td>0.6937</td>
    </tr>
    <tr>
      <td>44A - 45B</td>
      <td>0.9416</td>
      <td>0.9648</td>
      <td>0.9808</td>
      <td>0.8425</td>
      <td>0.677</td>
      <td>0.8415</td>
      <td>0.933</td>
      <td>0.6727</td>
      <td>0.4447</td>
      <td>0.089</td>
    </tr>
    <tr>
      <td>45A - 45B</td>
      <td>0.5714</td>
      <td>0.0122*</td>
      <td>0.6278</td>
      <td>0.97</td>
      <td>0.7593</td>
      <td>0.8721</td>
      <td>0.7363</td>
      <td>0.7902</td>
      <td>0.1275</td>
      <td>0.2574</td>
    </tr>
    <tr>
      <td>45A - 8Av</td>
      <td>0.0988</td>
      <td>0.0062**</td>
      <td>0.095</td>
      <td>0.1219</td>
      <td>0.5291</td>
      <td>0.9928</td>
      <td>0.0476*</td>
      <td>0.0857</td>
      <td>0.0401</td>
      <td>0.0853</td>
    </tr>
    <tr>
      <td>45A - p46v</td>
      <td>0.7274</td>
      <td>0.6956</td>
      <td>0.9363</td>
      <td>0.9604</td>
      <td>0.6792</td>
      <td>0.9901</td>
      <td>0.4861</td>
      <td>0.9549</td>
      <td>0.9686</td>
      <td>0.4794</td>
    </tr>
    <tr>
      <td>45B - 8Av</td>
      <td>0.0335*</td>
      <td>0.9801</td>
      <td>0.0327*</td>
      <td>0.0914</td>
      <td>0.3129</td>
      <td>0.8721</td>
      <td>0.1754</td>
      <td>0.0238*</td>
      <td>0.0004***</td>
      <td>0.0016**</td>
    </tr>
    <tr>
      <td>8Ad - 8Av</td>
      <td>0.2009</td>
      <td>0.0487*</td>
      <td>0.5458</td>
      <td>0.9852</td>
      <td>0.1933</td>
      <td>0.9897</td>
      <td>0.2412</td>
      <td>0.0155*</td>
      <td>0.6929</td>
      <td>0.0073**</td>
    </tr>
    <tr>
      <td>8Ad - 8Bs</td>
      <td>0.7142</td>
      <td>0.0183*</td>
      <td>0.7149</td>
      <td>0.9407</td>
      <td>0.8209</td>
      <td>0.7836</td>
      <td>0.9833</td>
      <td>0.9978</td>
      <td>0.2807</td>
      <td>0.7062</td>
    </tr>
    <tr>
      <td>8Ad - p46d</td>
      <td>0.6185</td>
      <td>0.0705</td>
      <td>0.5546</td>
      <td>0.123</td>
      <td>0.9152</td>
      <td>0.9984</td>
      <td>0.2024</td>
      <td>0.9795</td>
      <td>0.358</td>
      <td>0.7062</td>
    </tr>
    <tr>
      <td>8Av - p46v</td>
      <td>0.2667</td>
      <td>0.0009***</td>
      <td>0.0726</td>
      <td>0.1047</td>
      <td>0.2099</td>
      <td>0.9915</td>
      <td>0.0036**</td>
      <td>0.1038</td>
      <td>0.0344*</td>
      <td>0.0043**</td>
    </tr>
    <tr>
      <td>8Bd - 8Bm</td>
      <td>0.6165</td>
      <td>0.1226</td>
      <td>0.7936</td>
      <td>0.9194</td>
      <td>0.9698</td>
      <td>0.7409</td>
      <td>0.9038</td>
      <td>0.937</td>
      <td>0.8403</td>
      <td>0.4665</td>
    </tr>
    <tr>
      <td>8Bd - 8Bs</td>
      <td>0.8684</td>
      <td>0.2213</td>
      <td>0.6066</td>
      <td>0.8663</td>
      <td>0.968</td>
      <td>0.7386</td>
      <td>0.9602</td>
      <td>0.7048</td>
      <td>0.2297</td>
      <td>0.6243</td>
    </tr>
    <tr>
      <td>8Bd - 9d</td>
      <td>0.1213</td>
      <td>0.0168*</td>
      <td>0.0031**</td>
      <td>0.0011**</td>
      <td>0.0469*</td>
      <td>0.9557</td>
      <td>0.0155*</td>
      <td>0.3477</td>
      <td>0.0044**</td>
      <td>0.004**</td>
    </tr>
    <tr>
      <td>8Bm - 9m</td>
      <td>0.2744</td>
      <td>0.1202</td>
      <td>0.1303</td>
      <td>0.115</td>
      <td>0.5171</td>
      <td>0.9071</td>
      <td>0.1863</td>
      <td>0.5663</td>
      <td>0.2868</td>
      <td>0.1364</td>
    </tr>
    <tr>
      <td>8Bs - 9l</td>
      <td>0.385</td>
      <td>0.0058**</td>
      <td>0.0364*</td>
      <td>0.0083**</td>
      <td>0.2099</td>
      <td>0.9766</td>
      <td>0.0362*</td>
      <td>0.1957</td>
      <td>0.084</td>
      <td>0.1598</td>
    </tr>
    <tr>
      <td>9d - 9l</td>
      <td>0.6967</td>
      <td>0.3221</td>
      <td>0.8516</td>
      <td>0.7657</td>
      <td>0.5923</td>
      <td>0.8587</td>
      <td>0.7964</td>
      <td>0.8085</td>
      <td>0.8602</td>
      <td>0.6144</td>
    </tr>
    <tr>
      <td>9d - 9m</td>
      <td>0.7704</td>
      <td>0.3551</td>
      <td>0.3881</td>
      <td>0.2172</td>
      <td>0.2099</td>
      <td>0.6636</td>
      <td>0.2048</td>
      <td>0.9384</td>
      <td>0.1121</td>
      <td>0.9095</td>
    </tr>
    <tr>
      <td>9l - a46d</td>
      <td>0.7246</td>
      <td>0.054</td>
      <td>0.6553</td>
      <td>0.8908</td>
      <td>0.4226</td>
      <td>0.7544</td>
      <td>0.9602</td>
      <td>0.5726</td>
      <td>0.1595</td>
      <td>0.3769</td>
    </tr>
    <tr>
      <td>a46df - a46d</td>
      <td>0.6801</td>
      <td>0.004**</td>
      <td>0.4699</td>
      <td>0.7705</td>
      <td>0.7808</td>
      <td>0.8728</td>
      <td>0.5621</td>
      <td>0.833</td>
      <td>0.0257*</td>
      <td>0.5572</td>
    </tr>
    <tr>
      <td>a46df - a46vf</td>
      <td>0.3688</td>
      <td>0.8465</td>
      <td>0.5764</td>
      <td>0.5843</td>
      <td>0.3129</td>
      <td>0.9857</td>
      <td>0.6279</td>
      <td>0.9549</td>
      <td>0.747</td>
      <td>0.7573</td>
    </tr>
    <tr>
      <td>a46df-p46df</td>
      <td>0.6714</td>
      <td>0.6574</td>
      <td>0.7815</td>
      <td>0.9612</td>
      <td>0.9519</td>
      <td>0.8721</td>
      <td>0.528</td>
      <td>0.6964</td>
      <td>0.9208</td>
      <td>0.9138</td>
    </tr>
    <tr>
      <td>a46d-p46d</td>
      <td>0.6434</td>
      <td>0.6648</td>
      <td>0.6831</td>
      <td>0.3038</td>
      <td>0.8504</td>
      <td>0.9781</td>
      <td>0.5283</td>
      <td>0.7053</td>
      <td>0.5933</td>
      <td>0.7062</td>
    </tr>
    <tr>
      <td>a46vf - a46v</td>
      <td>0.0688</td>
      <td>0.0105*</td>
      <td>0.5349</td>
      <td>0.3464</td>
      <td>0.3066</td>
      <td>0.9766</td>
      <td>0.5895</td>
      <td>0.4481</td>
      <td>0.0101*</td>
      <td>0.9936</td>
    </tr>
    <tr>
      <td>a46vf - p46vf</td>
      <td>0.9393</td>
      <td>0.9003</td>
      <td>0.6864</td>
      <td>0.9146</td>
      <td>0.968</td>
      <td>0.489</td>
      <td>0.402</td>
      <td>0.7902</td>
      <td>0.9948</td>
      <td>0.7508</td>
    </tr>
    <tr>
      <td>a46v - p46v</td>
      <td>0.8536</td>
      <td>0.3958</td>
      <td>0.5219</td>
      <td>0.2731</td>
      <td>0.677</td>
      <td>0.8721</td>
      <td>0.287</td>
      <td>0.7048</td>
      <td>0.9504</td>
      <td>0.7352</td>
    </tr>
    <tr>
      <td>p46df - p46d</td>
      <td>0.7061</td>
      <td>0.0724</td>
      <td>0.3835</td>
      <td>0.1953</td>
      <td>0.638</td>
      <td>0.7277</td>
      <td>0.5781</td>
      <td>0.8386</td>
      <td>0.003**</td>
      <td>0.9546</td>
    </tr>
    <tr>
      <td>p46df - p46vf</td>
      <td>0.7953</td>
      <td>0.7199</td>
      <td>0.6601</td>
      <td>0.6934</td>
      <td>0.226</td>
      <td>0.7501</td>
      <td>0.7768</td>
      <td>0.8638</td>
      <td>0.8326</td>
      <td>0.6022</td>
    </tr>
    <tr>
      <td>p46vf - p46v</td>
      <td>0.1742</td>
      <td>0.0982</td>
      <td>0.3824</td>
      <td>0.0563</td>
      <td>0.0746</td>
      <td>0.3428</td>
      <td>0.4663</td>
      <td>0.3193</td>
      <td>0.0146*</td>
      <td>0.4608</td>
    </tr>
  </tbody>
</table>

Within the orbitofrontal cortex (OFC), laminar distribution patterns of kainate, GABAA, GABAB, M1, M2, and M3 receptors most clearly reflect the cytoarchitectonically identified areas 14r, 13b, 11m, and 11l, whereas caudal orbital areas 13m and 13l are highlighted by the laminar distribution of kainate, GABAA, α1, M2, M3, and 5HT1A receptors (Figure 9; Figure 9—figure supplements 1 and 2). Particularly areas 14r and 12l stand out due to the shape and size of their fingerprints (Figure 10; Figure 10—figure supplement 1). Area 14r is characterized by the lowest GABAA/BZ and M2 densities within PFC, but is among areas with the highest GABAB and α1 levels (Table 3). In addition to the above described differences with frontopolar areas, 14r contains significantly lower GABAA and M3 densities than area 11m (Table 4). Rostral orbital region occupied by the subdivisions 11m and 11l measured highest concentration levels for M3 among all prefrontal areas, and dysgranular areas 13m and 13l have the highest levels of AMPA, M2, and α2 in regard to all other orbital areas (Table 3). Significant differences between 11l and neighbouring areas were only found for the GABAB densities in area 13m, whereas 11m differed significantly from areas 14r and 10o in its GABAA and M3 and its kainate densities, respectively (Table 4).

Within Walker’s area 12, differences between rostral ventrolateral areas 12m and 12r are best delineated by changes in the laminar distribution patterns of AMPA, GABAA, 5HT1A, M1, and M3 receptors, whereas the border between caudal subareas 12o and 12l is most clearly revealed by the laminar distribution pattern of kainate, GABAA, α1, M2, M3, and 5HT1A receptors (Figure 9; Figure 9—figure supplements 1 and 2). In general terms, 12r has the highest and 12l the lowest densities measured within Walker’s area 12, and in the size of their fingerprints (Figure 10; Figure 10—figure supplement 1). Medially positioned areas (12m and 12o) have significantly higher α2 receptor densities than laterally positioned areas (12r and 12l). For the lateral areas we also found significant differences in the rostro-caudal direction, whereby 12r has significantly higher GABAA densities than 12l. Additionally, 12r contains significantly higher AMPA receptor densities than dorsally adjacent areas a46v and p46v. Area 12r also contains significantly higher GABAA, GABAB, and M3 receptor densities than does p46v (Table 4).

Differences in receptor architecture also revealed a novel cytoarchitectonic subdivisions of Walker’s areas 9 and 8B. In particular, the borders between areas 9m, 9d, and 9l are most clearly reflected in the laminar distribution patterns of kainate, NMDA, GABAA/BZ, M3, α2, 5HT1A, and 5HT2 receptors (Figure 9; Figure 9—figure supplements 1 and 3). Subdivision of area 8B into 8Bm, 8Bd, and 8Bs is clearly revealed by the differences in the laminar distribution patterns of AMPA, kainate, M1, M3, and 5-HT1A receptors (Figure 9; Figure 9—figure supplements 1 and 2). Newly defined area 8Bs contains the lowest kainate density out of all prefrontal areas, whereas area 8Bd presents the lowest NMDA and GABAA receptor densities within the PFC. In general, subdivisions of Walker’s area 9 contain higher receptor densities than those of his area 8B (Table 3), and this is reflected in their slightly larger fingerprints (Figure 11—figure supplement 1). There are also pronounced differences in the shape of the fingerprints, and this becomes particularly obvious when observing the normalized fingerprints (Figure 11). Areas 9d and 9l show significantly higher kainate, NMDA, GABAA, and M3 receptor densities than their caudal counterparts within area 8B (i.e. 8Bd and 8Bs, respectively). Additionally, α2 and 5-HT1A densities are significantly higher in 9d than in 8Bd (Table 4). Area 8Bs has significantly lower kainate receptor levels than laterally adjacent area 8Ad. The border between areas 8Bs and 8Ad is also revealed by differences in the laminar distribution pattern of kainate, M1, α1, 5-HT1A, and 5-HT2 receptors (Figure 9; Figure 9—figure supplements 1–3).

The border between the dorsal and ventral subdivisions of Walker’s area 8A (i.e. 8Ad and 8Av) is most clearly indicated by laminar differences in the distribution of kainate, GABAA, GABAB, M2, and α1 receptors. Area 8Av was characterized by the lowest density of AMPA, GABAB, M1, M3, α1, α2, and 5HT1A receptors out of all areas analysed here (Table 3), thus for this area the size of the fingerprint was the smallest in the PFC (Figure 11; Figure 11—figure supplement 1). Area 8Av has significantly lower kainate, α1, and 5HT1A receptor densities than 8Ad. It also has significantly lower densities of kainate, M3, and α2 than neighbouring area 45A, of AMPA, NMDA, α1, α2, and 5HT1A receptors than area 45B, as well as of kainate, M3, α2, and 5HT1A receptors than area p46v (Table 4).

Subdivisions of Walker’s area 46 within and around the ps identified by cytoarchitectonic analysis were revealed by the following differences in receptor architecture. Changes in the laminar distribution patterns of AMPA, kainate, GABAA, GABAB, GABAA/BZ, and M3 receptors most clearly reveal delineation of subdivisions within Walker’s area 46 for both anterior and posterior subareas (Figure 9; Figure 9—figure supplements 1 and 2). In general, higher densities were found in areas located around the fundus of ps than in those located on its dorsal and ventral shoulders, and higher muscarinic cholinergic densities were found in all anterior subdivisions of area 46 than in their caudal counterparts (Table 3). Furthermore, differences in the fingerprints of anteriorly located subdivisions of area 46 and their corresponding posterior counterparts were greater for areas located on the shoulder (e.g. when comparing a46d and p46d) than for areas located around the fundus (e.g. when comparing a46df and p46df; Figure 11; Figure 11—figure supplement 1). Along the entire length of the ps we found significantly higher α2 receptor densities in areas located around its fundus than the adjacent areas on the shoulder (Table 3). Interestingly, significant differences in kainate receptors were found only for anterior areas, whereby they were higher in a46d and a46v than in a46df and a46vf, respectively (Table 4).

Cytoarchitectonic borders between areas 45A, 45B, and 44 are clearly reflected by changes in the laminar distribution pattern of kainate, GABAB, GABAA/BZ, M1, M2, α1, and 5-HT1A receptors (Figure 9; Figure 9—figure supplements 1 and 2). The size of the normalized receptor fingerprints increases gradually when moving from area 45A through 45B to 44 (Figure 11). Area 45A contains significantly higher kainate levels compared to 45B (Table 4). Out of all prefrontal areas, area 44 had highest concentration levels recorded for 5HT2 receptors. Furthermore, whereas area 44 presents one of the highest 5-HT1A receptor densities within the PFC, area 45A contains the second lowest PFC density of this receptor type, and 45B only an intermediate to low value (Table 3), and these differences are reflected in the unique shaped normalized fingerprint of area 44 (Figure 11).

### Functional connectivity analysis

In addition to distinct cyto- and receptor architectonic features, areas have also been characterized by their unique functional connectivity pattern. To facilitate the description and interpretation of our results, we created summary figures emphasizing interareal connections (between subdivisions belonging to same area) as well as the most prominent connectivity correlation patterns of each area. Indeed, the results of the analysis of the functional correlation of each identified frontal area with a total of 138 areas of the prefrontal, cingulate, premotor, motor, somatosensory, parietal, and occipital cortex, previously identified by our group. Whereas a parcellation of the temporal cortex comes from Lyon atlas of Kennedy and colleagues (Markov et al., 2014). Connectivity patterns of prefrontal areas (including their intra-areal correlations) are depicted in Figures 12—15. In addition, same schematic summary of functional connectivity results for premotor and motor areas is shown in Figures 16—18.

![Figure 12.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig12-v1.jpg)

**Figure 12.:** Legend shows the strength of the functional connectivity coefficient (z) is coded by the appearance (wider-thinner-doted) of the connecting arrows. Areas related to different brain regions are marked on the scheme with distinct colours; prefrontal cortex (PFC) in light yellow, cingulate cortex (CC) in pink, premotor cortex (PMC) in light green, and temporal cortex (TC) in light blue.

![Figure 13.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig13-v1.jpg)

**Figure 13.:** Legend shows the strength of the functional connectivity coefficient (z) is coded by the appearance (wider-thinner-doted) of the connecting arrows. Areas related to different brain region are marked on the scheme with distinct colours; prefrontal cortex (PFC) in light yellow, cingulate cortex (CC) in pink, premotor cortex (PMC) in light green, motor cortex (MC) in dark green, somatosensory cortex (SSC) in orange, parietal cortex (PC) in red, occipital cortex (OCC) in purple, and temporal cortex (TC) in light blue.

![Figure 14.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig14-v1.jpg)

**Figure 14.:** Legend shows the strength of the functional connectivity coefficient (z) is coded by the appearance (wider-thinner-doted) of the connecting arrows. Areas related to different brain region are marked on the scheme with distinct colours; prefrontal cortex (PFC) in light yellow, cingulate cortex (CC) in pink, premotor cortex (PMC) in light green, motor cortex (MC) in dark green, somatosensory cortex (SSC) in orange, parietal cortex (PC) in red, occipital cortex (OCC) in purple, and temporal cortex (TC) in light blue.

![Figure 15.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig15-v1.jpg)

**Figure 15.:** Legend shows the strength of the functional connectivity coefficient (z) is coded by the appearance (wider-thinner-doted) of the connecting arrows. Areas related to different brain region are marked on the scheme with distinct colours; prefrontal cortex (PFC) in light yellow, cingulate cortex (CC) in pink, premotor cortex (PMC) in light green, motor cortex (MC) in dark green, somatosensory cortex (SSC) in orange, parietal cortex (PC) in red, occipital cortex (OCC) in purple, and temporal cortex (TC) in light blue.

![Figure 16.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig16-v1.jpg)

**Figure 16.:** Legend shows the strength of the functional connectivity coefficient (z) is coded by the appearance (wider-thinner-doted) of the connecting arrows. Areas related to different brain region are marked on the scheme with distinct colours; prefrontal cortex (PFC) in light yellow, cingulate cortex (CC) in pink, premotor cortex (PMC) in light green, motor cortex (MC) in dark green, somatosensory cortex (SSC) in orange, parietal cortex (PC) in red, occipital cortex (OCC) in purple, and temporal cortex (TC) in light blue.

#### Areas 10

Lateral frontopolar areas 10d and 10o present more restricted functional connectivity pattern than medial areas 10md and 10mv (Figure 12), apart from the weak correlation between 10d and areas a46d and a46v. Contrary, medial areas 10md and 10mv share strong connectivity with cingulate cortex, that is, dorsally located area 10md with p32, while ventral area 10mv was correlated with s32 and to a lesser extent with p32. Further differences are found since 10mv is strongly correlated to orbital area 14r, while this is not case with 10md. In contrast, 10md has connectivity with dorsal and lateral PFC. Within the frontal polar region, dorsal areas 10d and 10md are more strongly correlated to each other than to their ventral counterparts, which are also strongly connected to each other (Figure 12).

#### Areas 14

Rostral area 14r has more prominent functional correlation with medial PFC (area 10mv) and anterior cingulate cortex (ACC) than with caudally located area 14c, which is strongly correlated with caudal orbital (area 13a) and rostral cingulate area 25. Subdivisions of area 14 show weaker connectivity among each other than to their corresponding adjacent areas (Figure 12).

#### Areas 11

Subdivisions of area 11 displayed strong functional connectivity to each other and to their surrounding areas, that is, 11l and its laterally neighbouring areas 12r, 12m, and 12o, whereas area 11m was more strongly correlated with medially adjacent area 13b, and to a lesser extent with area 13l. Finally, both areas revealed connectivity with ventrolateral area 45A (Figure 12).

#### Areas 13

Among subdivisions of area 13, we found that areas 13a and 13m have most restricted connectivity pattern, whereby most rostral area 13b and laterally positioned area 13l show opposite trend. Interestingly, area 13a revealed weakest interconnectivity to 13l, but rather strong connections to adjoining areas 13b and 14c, whereby the strongest connectivity for area 13l is found to be with surrounding areas 13m and 12o. Additionally, area 13l revealed connectivity to posterior prefrontal region, in particular to areas 12l, 45A, p46d, and p46v (Figure 12).

#### Areas 12

Within the orbitofrontal region, subdivisions of area 12 presented a widespread functional connectivity pattern. This was particularly true for area 12r, which showed strong correlation to lateral areas 46, ventral areas 45A and 45B, as well as a correlation, although weaker, with premotor areas F5 and temporal polysensory areas STPi, PBc, and LB. Interareal connectivity pattern showed a weak correlation between area 12l and the rest of the area 12, which share strong functional connectivity among each other. In contrast, the strongest connections of 12l are found with areas 45A, 13l, and p46v (Figure 12).

#### Areas 9 and 8B

On the dorsolateral prefrontal cortex, rostro-caudal differences can be recognized between functional connectivity pattern of areas 9m, 9d, and 9l rostrally, and more caudally located areas 8Bm, 8Bd, and 8Bs, which displayed a more widespread connectivity pattern with various distinct areas in the prefrontal, pre(motor), parietal, medial occipital, and temporal cortex (Figure 13). While dorsal and lateral subdivisions of areas 9 and 8B are strongly intercorrelated, medial areas 9m and 8Bm showed a stronger connection to their medial neighbouring areas, that is, 9m to its adjacent cingulate area 24c, and 8Bm to surrounding areas a24’c and F6. Among all subdivisions of area 9, only medial area 9m shows functional connectivity with premotor cortex, in particular areas F6, F3, F2v, and F5s. Connectivity pattern of area 9d is restricted within prefrontal region; this is not true for 9m and 9l, which revealed connectivity with parietal area Opt and temporal areas STPr and STPi. Moreover, area 9m is rather correlated to anterior and mid-cingulate areas, whereas 9d has connection to posterior cingulate area d23a/b. All subdivisions of area 8B share strong functional connectivity with their surrounding prefrontal areas, parietal area Opt, and premotor areas F6 and F7. But opposite is found in regard to their connectivity with frontopolar and orbital areas. Additionally, only area 8Bd did not show connectivity with temporal areas. On the other hand, area 8Bs revealed functional connectivity with primary motor cortex, that is, areas 4a and 4m, as well as with transitional somatosensory area TSA and medial occipital region, that is, areas V6Adm and V6Avm (Figure 13).

#### Areas 46

Rostro-caudal differences in functional connectivity patterns were also found for the subdivisions of lateral prefrontal area 46, whereby posterior subdivisions showed a more widespread connectivity pattern across the brain. Within the ps, the anterior and posterior subdivisions of area 46 have a similar intraregional organization. Specifically, while dorsal subdivisions have strong connection to each other, as well as with areas ‘46vf,’ most ventrally located areas a46v and p46v revealed to have stronger connection to their counterparts ‘46vf’ than with corresponding dorsal subdivisions. Interestingly, connectivity between areas ‘46v’ and dorsal areas 46 is weaker in the rostral than in the caudal portion of the ps. Correlation with parietal areas Opt and LIP, and temporal STP areas is noticed throughout areas 46; however, these connections are particularly strong for ‘p46’ areas. Finally, areas ‘p46d’ show connectivity with primary motor cortex and somatosensory areas TSA and 3bm, which is not case with areas ‘p46v’ (Figure 14).

#### Areas 8A, 44, and 45

Within the most posterior portion of the lateral prefrontal cortex, areas 8Ad and 8Av revealed widespread connectivity pattern with region around ias, as well as with the cingulate, temporal, somatosensory, and parietal cortex (Figure 15). While both areas express similar connectivity pattern across cortex, we found that area 8Ad was more strongly connected with prefrontal area 8Bs and parietal area Opt. In contrast, area 8Av revealed stronger connection with prefrontal areas 45B and 44, as well as premotor area F4s and temporal TPt. Ventrolateral areas 45A and 45B have strong interconnection to each other, as well as to surrounding prefrontal and premotor areas (Figure 15). However, while 45B has widespread connectivity throughout the medial and inferior parietal cortex, this was not true for 45A. Instead, we found that area 45A has rather strong correlation with numerous orbital areas. Unlike areas 45, the more posteriorly located area 44 does not show strong correlation with auditory core region within the temporal cortex, but exhibits a wider connectivity pattern which also includes somatosensory cortex (i.e. areas 3al, 3bl, and 3bm) and primary motor area 4p (Figure 15).

#### Premotor areas

Medial premotor areas F6 and F3 have strongest connectivity with each other and their respective adjacent areas, that is, F6 with prefrontal area 8Bm and F3 with primary motor area 4m. In general, both areas revealed to have widespread functional connectivity across the brain. Concretely, with the posterior prefrontal, lateral premotor, cingulate, and parietal areas, but connections of posterior area F3 are more extensive across primary motor, somatosensory, and temporal region than F6 (Figure 16).

All subdivisions of area F7 revealed to have strong connection with surrounding premotor areas and posterior prefrontal areas 8B, 8A, and ‘p46.’ While strongest connection is shown between F7d and F7i, the weakest one is noticed between F7d and F7s. Interestingly, most dorsal area F7d showed most restricted connectivity pattern, while opposite was true for most lateral area F7s, located on the dorsal wall of the ias. This area displayed widespread connectivity across primary motor, somatosensory, parietal, and temporal cortex (Figure 16). Caudally neighbouring to areas F7, on the dorsal premotor cortex, subdivisions of area F2 have relatively strong connection to each other, but the strongest connection of F2v was rather displayed with adjacent areas, located within the spur of the arcuate sulcus, F7s and F4s. Also, connectivity pattern of F2v is more widespread across cingulate, parietal, and temporal regions than of F2d. Finally, only F2v revealed connection with somatosensory cortex, that is, areas TSA, 2 and 3bl (Figure 16).

Similar to connectivity trend shown in dorsal counterparts, subdivisions of areas F5 and F4, located within the arcuate sulcus (i.e. F5s and F4s respectively), displayed more extensive connectivity patterns compared to their respective subdivisions on the ventral premotor surface (Figure 17). While areas F5s and F4s have strong correlation to their respective dorsal subdivisions F5d and F4d, connectivity to the ventral subdivisions is weaker; this is particularly true for correlation between F4s and F4v. Interestingly, we found correlation between F5v and auditory core region within the temporal lobe. Also, we found strong correlation between primary area 4p and ventral premotor region, which was the strongest for areas F4d and F4v (Figure 17).

![Figure 17.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig17-v1.jpg)

**Figure 17.:** Legend shows the strength of the functional connectivity coefficient (z) is coded by the appearance (wider-thinner-doted) of the connecting arrows. Areas related to different brain region are marked on the scheme with distinct colours; prefrontal cortex (PFC) in light yellow, cingulate cortex (CC) in pink, premotor cortex (PMC) in light green, motor cortex (MC) in dark green, somatosensory cortex (SSC) in orange, parietal cortex (PC) in red, occipital cortex (OCC) in purple, and temporal cortex (TC) in light blue.

![Figure 18.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig18-v1.jpg)

**Figure 18.:** Legend shows the strength of the functional connectivity coefficient (z) is coded by the appearance (wider-thinner-doted) of the connecting arrows. Areas related to different brain region are marked on the scheme with distinct colours; prefrontal cortex (PFC) in light yellow, cingulate cortex (CC) in pink, premotor cortex (PMC) in light green, motor cortex (MC) in dark green, somatosensory cortex (SSC) in orange, parietal cortex (PC) in red, occipital cortex (OCC) in purple, and temporal cortex (TC) in light blue.

#### Primary motor areas

Subdivisions of area 4 have the strongest correlation with surrounding areas of premotor and somatosensory cortex. In particular, area 4m with medial premotor area F3 and somatosensory 3am and 3bm; area 4a with dorsal premotor areas F2d and F2v and most posterior area 4p with ventral premotor (F4d and F4v) and somatosensory areas 1, 3al, and 3bl. Additionally, 4p has strong correlation with rostral areas PF, PFG, and PFop of the inferior parietal lobule, as well as with intraparietal area AIP. In general, primary motor region revealed widespread connectivity with posterior prefrontal and cingulate areas, but also with parietal and temporal cortex (Figure 18).

### Hierarchical clustering and principal component analyses

The hierarchical cluster analysis (Figure 19) revealed differences in size of receptor fingerprints between areas occupying its most rostral portion (found in clusters 1 and 2) from the more caudally positioned prefrontal areas and (pre)motor areas (found in clusters 3–5). The five main clusters, which were identified by the k-means analysis, are mostly composed of neighbouring areas, but also group areas that do not share common borders and occupy different regions of the hemisphere.

![Figure 19.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig19-v1.jpg)

**Figure 19.:** The analyses include 33 of the 35 areas identified in this study (for areas 14c and 13a was not possible to extract receptor densities due to technical limitations), as well as 16 areas of the primary motor and premotor cortex identified in a previous study (Rapan et al., 2021) carried out on the same monkey brains. Above the hierarchical dendrogram, the extent and location of the five clusters are depicted on the medial, lateral, and orbital surface of the Yerkes19 atlas. Clusters are colour coded based on the corresponding colour on the dendrogram.

A principal component analysis was carried out to reduce the 14-dimensional space resulting from the analysis of 14 different receptors area to a 2-dimensional plot (Figure 20). Differences in the first principal component revealed a rostro-caudal trend driven by the gradual decrease in size of the receptor fingerprints. Consequently, subdivisions of area 4 (4m, 4a, and 4p) are segregated from the rest of the frontal areas since their fingerprints are the smallest among all analysed areas (present data, Rapan et al., 2021). In contrast, areas of clusters 1 and 2 present the highest receptor concentration levels. The second principal component further segregated primary motor areas (cluster 5) from the premotor ones (clusters 4 and 3), as well as rostral prefrontal areas (clusters 1 and 2) from the posterior ones (cluster 3) (Figure 20). The first and second principal components did not segregate areas located in clusters 1 and 2.

![Figure 20.](https://cdn.elifesciences.org/articles/82850/elife-82850-fig20-v1.jpg)

## Discussion

In this study, we provide a detailed parcellation of the macaque prefrontal cortex (apart from the cingulate cortex as a part of the limbic system), and which encompasses 35 cyto- and receptor architectonic areas. The new parcellation scheme integrates and refines former maps of the PFC, particularly concerning area 46 of Walker, and includes novel subdivisions of areas 10 (10mv, 10md, and 10d), 9 (9d and 9l) and 8B (8Bd and 8Bs). It is shown on a 2D flat map to facilitate comparison with previous maps (Barbas and Pandya, 1989; Caminiti et al., 2017; Carmichael and Price, 1994; Morecraft et al., 2012; Petrides and Pandya, 1994; Petrides and Pandya, 2002; Preuss and Goldman-Rakic, 1991; Walker, 1940), and, in addition, Table 1 was created as an overview of Rapan’s areas (this study; Rapan et al., 2021) in regard to the previous borders of referenced maps. Borders were also transferred to the Yerkes19 template (Donahue et al., 2016) to enable an architectonically informed analysis of functional connectivity in the macaque brain.

When analysing changes in receptor densities from area to area, the receptor fingerprints revealed differences across the frontal lobe when moving from rostral to caudal portions. Rostrally located areas contained higher receptor densities, thus bigger receptor fingerprints, than more caudally located areas. These differences in the size of receptor fingerprints seem to be the main force driving clustering of areas as revealed by the multivariate analyses. The heterogeneity within macaque frontal lobe is not only reflected by its architecture and molecular structure, but also by its functional diversity. The analysis of the functional connectivity revealed that posterior subdivisions of area 46 (‘p46’), 45, 44, and 8A displayed the most extensive connectivity patterns within the frontal region, as well as with distinct cortical regions across the brain. Although not widespread pattern as for areas mentioned above, within the OFC only area 12r displayed connectivity pattern which included also remote premotor and temporal areas. In contrast, areas 10, 14, 13, and 11 displayed functional connectivity limited within the prefrontal region, possibly suggesting that these areas are affected by a lower signal-to-noise ratio (Yeo et al., 2011). Thus, when available, we discuss the results of our functional connectivity analysis in the framework of tracer studies with injection sites within our region of interest (e.g. Markov et al., 2014; Gerbella et al., 2010; Carmichael and Price, 1996). Furthermore, areas located within and around spur of the arcuate sulcus, that is, F7s, F2v, F4s, and F5s, showed rather widespread connectivity pattern across the brain compared to their respective counterparts within the same premotor area. Primary motor areas 4m, 4a, and 4p revealed strongest connections with neighbouring premotor and somatosensory areas, as well as with the parietal cortex.

### Comparison with previous architectonic maps of macaque prefrontal region

#### Medial and orbital prefrontal regions (areas 10, 11, 14, 13, and 12)

Walker, 1940 identified five relatively large cytoarchitectonic areas on the medial and orbital prefrontal cortex, that is, area 10 located on the frontal pole and encroaching onto the orbital surface, area 11 on the rostral orbitolateral surface, caudal areas 13 and 12 on the medial and lateral orbital surface, and area 14 located on the ventromedial convexity. Preuss and Goldman-Rakic, 1991 identified subdivisions in areas 13 (labelled as 13L and 13M) and 14 (defined as 14A, 14L, and 14M), whereas Carmichael and Price, 1994 published a more detailed map, which also included cytoarchitectonic subdivisions of areas 10 and 11, and is in accordance with the connectional diversity of this region (Carmichael and Price, 1996). We were able to confirm all areas defined by Carmichael and Price, 1994, except for those located in the frontal pole region (area 10 of Walker). Their map of the rostral granular area 10 displays areas 10m, located on the medial and dorsal surface of the hemisphere, and 10o, occupying the orbital surface of the medioventral gyrus, and delimited caudally by area 14r (Carmichael and Price, 1994). Our cyto- and receptor analyses confirmed the location and extent of area 10o. But it revealed the existence of three subdivisions within 10m, that is, mediodorsal area 10md, medioventral 10mv, and area 10d on the dorsal surface of the frontal pole. Indeed, these novel areas differed not only in their cyto- and receptor architecture, but also in their functional connectivity. Medial areas 10md and 10mv contrasted from their lateral counterparts 10d and 10o by a strong connectivity with the cingulate cortex, that is, dorsally located area 10md with p32, and ventrally, 10mv with s32 and to a lesser extent with p32. Interestingly, macaque areas p32 and s32 have established homologies within the human brain, where they have been associated with the processing of emotion (Palomero-Gallagher et al., 2013; Palomero-Gallagher et al., 2019; Vogt et al., 2013). Comparison between the tracer study by Markov et al., 2014 and our functional connectivity analysis revealed certain similarities regarding connectivity of area 10. Careful inspection of their Figure 2 reveals that the injection sites are at a location comparable mainly to that of our area 10md and, to a lesser extent, of our area 10d. They describe connectivity with prefrontal areas 14, 9, 46d, 46v, and 9/46d as well as with cingulate areas 25, 32, and 24c (Markov et al., 2014), which is in accordance with our results for areas 10md, whereas our area 10d presents a more restricted functional connectivity than does 10md since it is not correlated with the cingulate cortex.

Within the OFC, the present analysis confirmed the position and extent of areas 11l, 11m, 13l, 13m, 13b, 13a, 14r, and 14c as identified by Carmichael and Price, 1994. We also identified four subdivisions of Walker’s area 12, but their spatial relationship differs from that described by Carmichael and Price, 1994. In both maps areas 12r and 12m occupy the rostral portion of the lateral orbital cortex, while areas 12l and 12o cover its caudal part. Areas 12r and 12l extend onto the ventrolateral convexity below the ps. However, unlike in the map of Carmichael and Price, 1994, where 12m abuts areas 12r, 12l, and 12o, in our parcellation area 12m does not have a common border with 12l since our area 12r extends further posteriorly than that of Carmichael and Price, 1994. The OFC plays an important role in a reward processing (e.g. association of stimulus), as well as in emotional and motivational aspects of behaviour (Mishkin and Manning, 1978; Rolls, 2000; Rolls et al., 1990; Rudebeck and Murray, 2011b), whereas the ventrolateral region is associated with working memory for non-spatial tasks, as well as object memory retrieval (Wilson et al., 1993). In particular, the ventrolateral prefrontal cortex contains visual neurons specialized for the identification of object features (Asaad et al., 1998; Wilson et al., 1993). This brain region also encompasses our areas 12r and 12l, which express significantly lower α2 receptor densities than their medial counterparts 12m and 12o, respectively. Furthermore, we found areas 12r, 12m, and 12o to be strongly connected, while area 12l, which contained the lowest α2 receptor density of all subdivisions of area 12, was more strongly associated with area 45A than with the other subdivisions of area 12. Thus, the structural and functional organization of this region seems to be closely related to differences in the interareal levels of α2 receptors. This is an interesting finding since catecholamine neurotransmitters have been associated with cognitive decline in aged non-human primates (Arnsten and Goldman-Rakic, 1985), and in particular α2 receptor agonists have been shown to improve the delayed response performance test results in macaques (Arnsten et al., 1988).

#### Dorsolateral prefrontal region (areas 9, 46, and 8B)

The analysis also resulted in a novel and more detailed subdivision within this region in regard to areas 9, 8B, and 46 than that described in previous maps (Petrides and Pandya, 1999; Preuss and Goldman-Rakic, 1991; Walker, 1940). Differences in the receptor architectonic organization of dorsolateral prefrontal areas are particularly obvious when looking at the normalized fingerprints, and significant differences were found between rostral and caudal mediodorsal prefrontal areas 9 and 8B, respectively.

Although some authors confirmed Walker’s area 9 (Walker, 1940; e.g. Barbas and Pandya, 1989; Carmichael and Price, 1994; Morecraft et al., 2012; Petrides and Pandya, 1994; Petrides and Pandya, 2002), others (e.g. Caminiti et al., 2017; Preuss and Goldman-Rakic, 1991) described a dorsal (9d) part, located on the convexity superior to the principal sulcus, and a medial (9m) subdivision on the medial surface of the hemisphere, dorsal to the cingulate sulcus. We confirmed the existence of 9m, but identified cyto- and receptor architectonic differences within their area 9d. Here only the most dorsal part was labelled as area 9d, whereas more laterally, we identified the distinct area 9l. Whereas area 9l presented a strong functional connectivity with laterally adjacent area a46d, this was not case for our areas 9d and 9m. These areas were more strongly associated with posterior area p46d. Moreover, dorsal areas 9d and 9l are strongly interconnected. Interestingly, medial area 9m, which has been included in the medial prefrontal network (Carmichael and Price, 1996), correlated with anterior cingulate area 24c more strongly than with the other subdivisions of area 9.

Further caudal on the mediodorsal prefrontal surface, a transitional region between granular prefrontal and agranular premotor areas was described, namely dysgranular area 8B of Walker, 1940 and Petrides and Pandya, 1994, which encompasses areas 8Bm and 8Bd of Preuss and Goldman-Rakic, 1991 and Morecraft et al., 2012. Similar to the situation described above for area 9, we were able to confirm the existence of area 8Bm, but we subdivided area 8Bd into a dorsal component located caudal to area 9d (our area 8Bd) and a ventral component 8Bs, which abuts area 9l. Previous maps (e.g. Morecraft et al., 2012; Petrides and Pandya, 1994; Petrides and Pandya, 2002; Preuss and Goldman-Rakic, 1991; Walker, 1940) depicted area 8B just rostral to the sas. However, the extent of our area 8B includes cortex above sas as well. Hence, area 8Bd was also identified on the most dorsal portion of the hemisphere rostral to and above the sas. Further lateral on the dorsal surface we identified area 8Bs, which extends onto the dorsal wall of the sas. Subdivisions of area 8B do not present a transitional region only by their structural features, but also based on their extensive functional connectivity since our analysis showed a widespread functional connectivity with prefrontal areas, as well as with the medial and dorsal premotor cortex. Dorsal prefrontal cortex, which is occupied by areas 9 and 8B, is involved in orientating processes and joint attention in primate brain (Petrides and Pandya, 1999), which is an important behavioural feature when animals need to integrate stimuli from different sensory modalities in order to select an adequate behavioural response. However, unlike area 9, more posteriorly adjacent mediodorsal area 8B is a prominent target region of the prestriate and the medial parietal cortex (Petrides and Pandya, 1999). In particular, neurons in area 8B fire during spontaneous ear and eye movement, as well as during the processing of auditory information (Bon and Lucchetti, 1994). Thus, it has been suggested that area 8B represents a macaque-specific region which is not present in humans, the so-called premotor ear-eye field (PEEF) (Lucchetti et al., 2008).

Walker, 1940 defined area 46 within and around ps, and occupying large portion of the lateral prefrontal surface caudal to area 10, while on the most posterior end of principal sulcus, area 46 was replaced by area 8A. This location of area 46 in the macaque monkey has been confirmed in various anatomical studies (Caminiti et al., 2017; Petrides and Pandya, 1994; Petrides and Pandya, 2002; Preuss and Goldman-Rakic, 1991); however, it was widely acknowledged that this large region is not homogeneous, and distinct subdivisions with many discrepancies among parcellation schemes were made by different authors. Preuss and Goldman-Rakic, 1991 identified four subareas along the principal sulcus. Two areas within the sulcus on the dorsal and ventral wall close to the fundus (inner subareas), areas 46d and 46v, respectively, and two areas on the dorsal and ventral shoulders of the sulcus and extending onto the free surface of the hemisphere (outer areas) areas 46dr and 46vr, respectively. Other authors identified rostro-caudal differences within Walker’s area 46, but only described a dorsoventral segregation in the caudal portion, thus resulting in a parcellation with a rostral area 46 and caudal areas 9/46d and 9/46v located on the dorsal and ventral banks of the principal sulcus, respectively, and extending onto the free surface of the hemisphere (Borra et al., 2019; Caminiti et al., 2017; Gerbella et al., 2013; Morecraft et al., 2012; Petrides and Pandya, 2006).

The existence of dorsoventral subdivisions along the entire length of the principal sulcus, proposed by Preuss and Goldman-Rakic, 1991, could be corroborated by the present quantitative cyto- and receptor architectonic analysis. This study also confirmed the existence of rostro-caudal differences within the region and resulted in a new parcellation scheme for Walker’s area 46 including a total of eight subdivisions – with areas ‘a46’ located within the anterior portion of ps and areas ‘p46’ occupying its most caudal. Receptor architectonic differences particularly highlighted borders between inner (subdivisions closer to the fundus, areas ‘46f’) and outer (subdivisions extending onto surface, areas ‘46d’ and ‘46v’) portions of the principal region. We measured significantly higher levels of α2 receptors in the inner areas compared to their respective outer areas along the rostro-caudal ps axis. Area 46 plays an important role in higher-level cognitive processes, such as working memory (Fuster, 2008; Goldman-Rakic, 1995; Petrides, 2000), which has been reported to decline with age (Arnsten and Goldman-Rakic, 1985). Similar to subdivisions of area 12, norepinephrine elicits different responses within area 46, depending on which type of receptor is stimulated. In particular, its binding to α1 and α2 receptors can have opposite effects on persistent activity during working memory. Stimulation of α1 receptors increases feedforward calcium-cAMP signalling, whereas stimulation of α2 receptors inhibits this process (Arnsten et al., 1988; Arnsten et al., 2021; Arnsten and Jentsch, 1997; Hara et al., 2012). Calcium-cAMP signalling must be kept within a tight range to support persistent activity, with excessive signalling leading to a shutdown of synaptic activity due to opening of potassium channels (Arnsten et al., 2021). The increase in α2 receptors in inner subdivisions of area 46 could help keep persistent activity in-check in these areas. In contrast, higher levels of kainate are measured in ‘shoulder’ areas of the ps than in the ‘fundus’ areas; however, only between anterior areas this difference has reached a significant level.

Our subdivision of Walker’s area 46 into anterior/posterior and fundal/shoulder regions is further supported by the differences in the functional connectivity patterns of the areas we identified since posterior subdivisions of area 46 displayed a more widespread connectivity pattern than the anterior areas, and also in regard to all other prefrontal areas. Specifically, anterior areas showed the most prominent correlations with areas of the rostral prefrontal region as well as with their caudal 46 counterparts, while posterior areas strongly correlate with surrounding premotor areas in the lateral and medial frontal region, as well as with the parietal, temporal, and mid to posterior cingulate cortex. Our results are in accordance with previous connectivity analyses of area 46 (Borra et al., 2019; Gerbella et al., 2013), and may be indicative of the role of areas ‘p46’ in the visuospatial and visuomotor control of arm/hand reaching and eye movement, whereas areas ‘a46’ are more strongly involved in higher cognitive processes (Borra et al., 2019; Gerbella et al., 2013). Furthermore, the anterior part of ps is a major target of projections from the auditory and limbic cortex, whereas the posterior portion receives topographic sensory inputs from auditory, somatosensory, visual, and polysensory cortex (Hackett et al., 1999). Taken together, these findings clearly suggest that the anterior and posterior portions of cortex within the ps are involved in different aspects of behaviour, whereby areas ‘p46’ constitute a multimodal integration centre within the lateral PFC. Additionally, significant differences of kanite and α2 receptors between ‘shoulder’ and ‘fundus’ areas suggest an intermediate role of these receptors on working memory, a higher cognitive function associated with this region.

#### Caudal region (areas 8Ad and 8Av)

Walker’s area 8A has been subject of numerous architectonic analyses, resulting in maps that differ in the number and extent of areas depicted. A region defined as the granular part of area 8 (Morecraft et al., 2012; Walker, 1940) is associated with the frontal eye field (FEF) (Bruce et al., 1985; Stanton et al., 1989) and eye movement. However, eye movements are invoked only within a fundus of the arcuate sulcus, whereby the prearcuate surface is rather involved in the visual attention (Germann and Petrides, 2020). The present quantitative analysis encompasses a cortex rostral to premotor representation of the forelimb and mouth by the arcuate sulcus, from the ventral wall of the sas, across the portion of the prearcuate convexity located around the posterior portion of ps (where it borders posterior parts of area 46) and extending ventrally to the most caudal part of the anterior wall within the ias (where it abuts areas 44 and 45B) (Morecraft et al., 2012; Walker, 1940). The results of the present quantitative multimodal analysis are in accordance with the map of Petrides and Pandya, 2006, which identifies dorsal and ventral subdivisions within 8A, and not the tripartite subdivision of area 8A proposed by Preuss and Goldman-Rakic, 1991, or the rostro-caudal segregation of Gerbella et al., 2007. Furthermore, contrary to the map of Preuss and Goldman-Rakic, 1991, where their area 8Ar extends ventrally along the cortical surface adjacent to the ias, where it was delimited rostrally by area 12vl, our results are in accordance with the relative dorsoventral extent of area 8A described by Petrides and Pandya, 2006 since area 8Av could be identified only on the cortical surface adjoining the most rostral portion of the ias and is replaced at this position by area 45A, so that it shares no common border with area 12. Moreover, the present receptor architectonic analysis also confirmed dorsoventral differences between subdivisions of area 8A since significantly higher kainate, α1, and 5-HT1A receptor densities were measured in 8Ad than in 8Av. Based on the qualitative cytoarchitectonic and receptor distribution pattern, we extended area 8Av onto the fundus of the arcuate sulcus, indicating that this area includes FEF. However, due to our material limitations in this study, this proposition was not tested by our quantitative approach. Both subdivisions displayed a widespread connectivity pattern, with strongest correlations in the lateral frontal, parietal, and mid to posterior cingulate cortex, similar to the situation found for areas ‘p46.’ Interestingly, both areas 8Av and 8Ad display a strong connectivity with areas p46d, p46df, p46vf, but not with area p46v, whose connectivity pattern also differs from that of remaining ‘p46’ areas by its stronger correlation with the ventrolateral frontal region, but its weaker correlation with the inferior parietal and posterior cingulate cortex. Finally, it is noteworthy that areas 8Av and 8Ad (considered to constitute a key region regulating visual attention; Germann and Petrides, 2020; Petrides, 2005) were negatively correlated with areas of the occipital lobe, whereas p46v presented a positive correlation with this brain region, indicating that subdivisions of area 8A operate at a higher visual processing level than area p46v.

#### Ventrolateral region (areas 45A, 45B, and 44)

Finally, the ventrolateral region also encompasses areas 44 and 45, which are thought to be the homologs of Broca’s region in humans (Petrides and Pandya, 2002). In contrast with the parcellations proposed by Walker, 1940 and Preuss and Goldman-Rakic, 1991, Petrides and Pandya, 2002 found area 45 to extend rostrally onto the adjacent lateral surface of the hemisphere for a considerable distance, reaching as far as the ipd. Previous maps depicted area 45 mainly within the ias, and only encroaching onto the free surface, where it was replaced dorsally by area 46 and ventrally by area 12 (in the map of Walker, 1940), or rostrally by area 8Ar (in the map of Preuss and Goldman-Rakic, 1991). Furthermore, Petrides and Pandya, 1999; Petrides and Pandya, 2002Petrides and Pandya, 1994 subdivided monkey area 45 into areas 45A and 45B. Area 45A occupies the ventral portion of the prearcuate convexity ventral to area 8Av, and extends rostrally into the ipd, where is substituted by 12r dorsally, and ventrally by 12l. Caudally 45A is delimited by 45B, which occupies the rostro-dorsal wall of the ias. The subdivision of area 45 was based primarily on differences in the appearance of layer IV (Petrides and Pandya, 1994; Petrides and Pandya, 1999; Petrides and Pandya, 2002). The results of the present quantitative multimodal approach not only support the presence of an area 45, and not of area 12, on the prearcuate convexity, but also confirm the existence of areas 45A and 45B, with higher kainate densities in the former than the latter area.

While the present functional connectivity analysis shows that both areas 45 area correlated with polysensory areas STP and auditory-related temporal cortex (contrary to the findings of Gerbella et al., 2010), a suggestion that area 45A is associated with vocalization and communication behaviour, whereas area 45B rather plays a role in oculomotor frontal system (Gerbella et al., 2010), is in accordance with our analysis. We found that 45B is correlated to parietal areas, such as oculomotor area LIPd, and has much more extensive connectivity across the premotor cortex compared to 45A. Indeed, area 45A revealed a strong correlation only with premotor areas F5, which are involved in hand and mouth movements (Fogassi et al., 2001; Maranesi et al., 2012), which may have a function in communication.

In the past the existence of area 44 has been the subject of controversy. Walker, 1940 and Preuss and Goldman-Rakic, 1991 did not identify an area 44 in their maps because they considered that area 45 not only occupied the rostral, but also the caudal wall of the ias. Similarly, Matelli et al., 1986 did not identify area 44 either since they thought that their area F5 continues rostrally into the ias, where it was followed by area 45. Petrides and Pandya (Petrides et al., 2012; Petrides and Pandya, 1994) identified a distinct dysgranular area between the caudally adjacent agranular premotor cortex and granular area 45, and this is supported by our structural (cyto- and receptor architecture) and functional connectivity analyses. Furthermore, tracer studies (Cavada and Goldman-Rakic, 1989; Matelli et al., 1986; Petrides and Pandya, 1984), which are in accordance with our functional connectivity results, showed that area 44 differs from the posteriorly adjacent ventral premotor cortex by its cortico-cortical projections to the parietal region. Whilst the ventral premotor region shares strong reciprocal connections with the most anterior areas of the inferior parietal lobule (IPL) (Cavada and Goldman-Rakic, 1989; Matelli et al., 1986; Petrides and Pandya, 1984), area 44 of the monkey brain is linked with the most posterior areas PFG and PG of the inferior parietal lobe (Petrides and Pandya, 2009). Thus, macaque area 44 may serve as an important region for the integration of different inputs in order to support the role of area 45B in oculomotor control (Gerbella et al., 2010) since the strongest correlations between frontal areas were found between area 44 and areas F5s and 45B, which also presented small Euclidean distances in the hierarchical clustering analysis. This finding further supports the hypothesis that similarities in the size and shape of fingerprints constitute the molecular underpinning for related brain functions (Zilles et al., 2015; Zilles and Palomero-Gallagher, 2017a).

### Receptor-driven clustering of macaque frontal areas is associated with distinct functional connectivity patterns

Although functional connectivity often indicates direct anatomical connections (Greicius et al., 2009; Thiebaut de Schotten et al., 2011), it also reflects indirect connections, as well as an input from a common source area (Smith et al., 2001). Moreover, such analysis may be affected by the differences in local recurrent activity across areas (Chaudhuri et al., 2015). It is important to understand that while structural and functional aspects of brain organization are genuinely interconnected, they are not equal (Rapan et al., 2021). Contrary to the tract-tracing approach, functional connectivity can be easily assessed for novel parcellations of cortex, as shown in a present study, since it enables differentiation among areas with similar receptor profiles (e.g. newly identified subdivisions of area 10). Concerning neurotransmitters and their receptors, which constitute the molecular underpinning of signal transduction, we here analysed receptors with different mechanisms of action (ionotropic/metabotropic) and outcomes (excitatory/inhibitory). Activation of metabotropic receptors results in slower, longer lasting, and more widespread changes in membrane potential than does activation of ionotropic receptors. Therefore, if two areas differ in the relative balance of ionotropic versus metabotropic receptors, this will indeed result in different constraints on computational properties and could influence the temporal signature of neural activity. Taken together, functional connectivity facilitates the use of gold-standard anatomical data (e.g. the cytoarchitectonic boundaries and receptor data described here) by specialist in neuroimaging and enables a more systematic understanding of the macaque frontal cortex.

#### Areas of cluster 1

Cluster 1 encompasses most of the rostrally positioned prefrontal areas, which share dense reciprocal connections with the limbic and auditory cortex (Hackett et al., 1999; Romanski, 2007), and also includes areas p46df and p46vf, which are located more posteriorly within the ps. The medial OFC is associated with value comparison since it shares reciprocal connections with brain regions involved in similar aspects of reward-guided behaviour (Price, 2007) and is a primary source of visceromotor inputs via reciprocal projections to the hypothalamus and brain stem (Carmichael and Price, 1994). Lesion studies of the medial OFC in the macaque brain, in particular to area 14, showed animals to be enticed into making incorrect choices, indicating that the decision-making process within the medial OFC is rather associated with motivation, than with action-like behaviour (Noonan et al., 2010; Rudebeck and Murray, 2011b). Since we found strong functional correlation between areas 10mv and 14r, it is interesting that most of the adjacent areas, such as 10o, 10mv, and 11m, showed significantly higher levels of inhibitory receptors (i.e. GABAA and GABAA/BZ), but only area 10mv contained significantly higher levels of AMPA in regard to 14r. Additionally, similar to the medial frontopolar cortex, we found area 14r to have a strong functional connectivity with the anterior cingulate cortex, in particular to area 25. In contrast, connections of the lateral OFC to high-order sensory areas, such as the anterior temporal and perirhinal cortex (Carmichael and Price, 1994; Price, 2007), indicate that this region plays an important role in the reward-associated behaviour by assigning a value to stimuli. Animals with lesions in the rostrolateral OFC were unable to learn when to ascribe a different value when a new object is introduced, thus highlighting the importance of this region in value learning (Noonan et al., 2010). Although the medial and lateral orbitofrontal regions display distinct connectional patterns with distant cortical and subcortical structures, they also share numerous reciprocal connections which are thought to support the exchange and integration of information (Carmichael and Price, 1994). Specifically, areas 14r, 14c, 13a, 11m, and 12o serve as ‘intermediary’ areas connecting the lateral and medial OFC networks (Carmichael and Price, 1994; Price, 2007).

Microstimulation recordings revealed the presence of the auditory-responsive neurons within the caudal ps (Hackett et al., 1999; Ito, 1982; Watanabe, 1992), although most input from the auditory cortex targets the rostral portion of ps (Barbas and Mesulam, 1985) and, in particular, the frontopolar region (Medalla and Barbas, 2014). In this study, we found only a weak connectivity of the frontal polar region and orbital areas outside of the prefrontal cortex. However, our multivariate analyses grouped together subdivisions of area 10, anterior parts of area 46, as well as caudal fundal portions of area 46, which are known to be targeted by the auditory cortex (Barbas and Mesulam, 1985; Hackett et al., 1999; Medalla and Barbas, 2014). Altogether, this suggests that the OFC provides an information on the object-value and motivation (Carmichael and Price, 1994; Noonan et al., 2010; Price, 2007; Romanski, 2007; Rudebeck and Murray, 2011a) which is then further processed by distinct regions in the medial and lateral PFC (Goulas et al., 2014). In addition, the dorsal prefrontal cortex, which is occupied by subdivisions of area 9 (also found in cluster 1), is involved in orientating processes and joint attention in the primate brain, which is an important feature when the animal processes and integrates stimuli from different sensory modalities in order to select the adequate behavioural response (Petrides and Pandya, 1999). Thus, PFC areas which we found to be grouped within cluster 1 based on similarities in their receptor fingerprints seem to be involved in distinct aspects of reward-guided behaviour.

#### Areas of cluster 2

Cluster 2 is composed of closely grouped areas located in the posterior orbital PFC, that is, areas 13m, 13l, 12o, and 12l. It also contains dorsolateral prefrontal area 9l and premotor area F5v, located on the ventral portion of the postarcuate convexity, with which orbital areas do not share common borders. This is interesting since it demonstrates that frontal areas are not grouped simply on the basis of neurochemical similarities among neighbouring areas, but across the frontal cortex. Area F5v is mostly associated with mouth movements (Maranesi et al., 2012) and shares strong cortico-cortical connections with ventrally adjacent area ProM, as well as with the gustatory, orbitofrontal, insular, and somatosensory cortex (Maranesi et al., 2012), indicating an important role of this area in a feeding-related behaviour (Cipolloni and Pandya, 1999). While areas of the posterior orbital PFC, and in particular subdivisions of area 13, represent a multimodal region, which is targeted by the gustatory visual, auditory, somatosensory, and olfactory cortex, as well as by the amygdala, which assigns an emotional value to the integrated stimuli (Barbas, 2007).

Our functional connectivity analysis showed that newly identified area 9l has a strong correlation with multimodal area 46 (in particular with area a46d, and to a lesser extent with area p46v), as well as with polysensory area STPi and posterior cingulate areas d23a/b. Thus, area 9l may be a part of the multimodal region in the lateral PFC and serve as bridge with polysensory areas in the posterior orbital cortex. Furthermore, electrophysiological recordings of a brain region which topologically corresponds to our areas 9l and 9d (which are strongly correlated to each other) revealed that it contains neurons which are activated solely during voluntary head rotation, and neurons which are also activated when the head rotation is observed in another individual (mirror-like neurons), indicating that area 9 mediates head movements associated with certain social settings (Lanzilotto et al., 2017).

#### Areas of cluster 3

Cluster 3 encompasses all subdivisions of area 8B, area 8Ad, ventrolateral areas 45A, 45B, and 44, areas occupying the posterior shoulder of ps (i.e. p46d, p46v), ventral premotor F5s and F5d, as well as medial and dorsal premotor areas F6, F3, F7d, and F2d. In accordance with our functional connectivity analysis, posterior prefrontal areas have strong correlation across the premotor cortex. With the exception of F7d and F5d, areas clustered here are also recognized by their widespread connectivity pattern with distant brain regions. Medial area F6 plays an important role in controlling when and how to execute complex motor plan (Matelli et al., 1991), but it lacks direct connections to the primary motor areas, as well as the spinal cord (Dum and Strick, 2002; Luppino et al., 1993), thus its contribution to movement is mediated via its dense connections with other premotor areas (e.g. F3, F2d). Thus, correlation found between area F6 and primary motor area 4m may reflect area’s indirect connections (Adachi et al., 2012) rather than direct ones. On the other hand, posterior medial area F3 contains a complete somatotopic map of the body motor representation (Woolsey et al., 1952), and its direct anatomical connections with a primary motor cortex has been described (Luppino et al., 1993).

Area 8B is a prominent target region of the prestriate and the medial parietal cortex (Petrides and Pandya, 1999) and constitutes the cytoarchitectonic correlate of the functionally identified PEEF (Lucchetti et al., 2008), which is involved in auditory stimuli recognition and orientation processes (Bon and Lucchetti, 1994; Lanzilotto et al., 2013). Since neurons in area 8B fire during spontaneous ear and eye movement, as well as during auditory information processing, indicating a role of this region in the integration of auditory inputs with ear and eye motor output, this area is thought to be monkey specific and have no homolog in the human brain (Bon and Lucchetti, 1994; Lanzilotto et al., 2013). In monkeys, ear movement improves localization of different sounds in the environment, whereas in humans this ability is rather shifted to eye-head coordination (Bon and Lucchetti, 1994).

Our novel architectonic subdivisions of area 8B presented different functional connectivity profiles. The functional connectivity profile of 8Bd is limited to adjacent areas on the dorsal portion of the PFC (e.g. areas 9d and F7d), whereas area 8Bs has a more widespread connectivity pattern which includes more ventrally located 8Ad and F7s. Furthermore, our cyto- and receptor architectonic results support the classification of area 8B as a transitional region between the prefrontal and the premotor cortex since the subdivisions of area 8B (which are dysgranular) showed a closer receptor architectonic relationship with premotor (agranular) than with the remaining prefrontal (granular) areas. This is particularly true for 8Bd and F7d, which are both (based on their position in our atlas) associated with the supplementary eye field (SEF) (Schlag and Schlag-Rey, 1987). Area 8Ad, which is partly associated to FEF, presents another region specialized for visual attention (Amiez and Petrides, 2009), but also, together with 8Bs, contributes to auditory responses (Bruce and Goldberg, 1985), as both areas have correlation with the auditory cortex, that is, parabelt areas PBr and PBc. The most prominent difference found between SEF and FEF is that saccades evoked from the latter region are of fixed vectors, whereas microstimulation recordings revealed evidence for the representation of eye position in SEF (Mitz and Godschalk, 1989; Schlag and Schlag-Rey, 1987). The present functional connectivity analysis revealed a strong correlation between areas 8Ad and p46d, which is in agreement with previous tracer studies (Barbas and Mesulam, 1981; Barbas and Mesulam, 1985; Barbas and Pandya, 1989). In general, input from the principalis region to the FEF may mediate regulatory control over gaze (Schall, 1997).

The posterior ventral cortex, which encompasses areas 45A (part of cluster 3) and 12l, shows evidence of overlapping auditory and visual responsive regions (Romanski and Goldman-Rakic, 2002; Wilson et al., 1993), indicating that convergent inputs allow response to both stimuli, especially when processing of information is related to face and vocalization communication, associated with the recognition of familiar and unfamiliar faces (Romanski, 2007). Finally, areas 45B and 44, located within the ias, are related with the oculomotor control (Gerbella et al., 2010). In addition, the present functional analysis showed that posterior area 44 has strong connection to neighbouring premotor area F5s, which, actually, presents the highest correlation found between two areas in our study. Therewith, ventral premotor areas F5s and F5d represent hand movements and are involved in object grasping (Fogassi et al., 2001). Specifically, area F5s (defined as area F5a by Belmalih et al., 2009) is associated with stereoscopic analysis of a 3D object (Fogassi et al., 2001). Thus, within cluster 3, we find caudal prefrontal areas associated with the attention and orientation based on the distinct visual and auditory inputs, whereas premotor areas grouped here are involved in arm reaching and orientation, with a main focus on a hand grasping (Gerbella et al., 2017).

#### Areas of cluster 4

Cluster 4 contains area 8Av and premotor areas F7i, F7s, F2v, F4s, F4d, and F4v. As mentioned above, area 8Av is part of FEF, which is largely associated with saccades (Bruce et al., 1985). Due to the unique receptor architectonic features of the ventral portion of area 8A, indicated by the smallest receptor fingerprint of all prefrontal areas, we found a clear differentiation between 8Av and almost all surrounding prefrontal areas, where all significant receptor types were lower in 8Av. Thus, area 8Av was found to be more comparable to posteriorly adjacent premotor areas located within and around arcs, which are also characterized by relatively small fingerprints.

Furthermore, the functional connectivity analysis revealed that areas 8Av, F7s, F2v, and F4s, which are located within the spur of the arcuate sulcus, have strong connectivity with parietal areas associated with visual responses and control of saccadic and oculomotor movements, for example, intraparietal area LIP, and rostral areas Opt and PG of the inferior parietal lobule (Niu et al., 2021; Andersen et al., 1990a). In addition, we also found correlation with polysensory temporal areas STP and TPt, as well as with area MST, which is part of the temporal motion complex region (Boussaoud et al., 1990; Kilintari et al., 2014). This is interesting since fMRI studies of macaque behaviour involving voluntary saccadic eye movement reported a bilateral activation of both the rostral and caudal banks of arcs, as well as of cortex within the spur of this sulcus (Baker et al., 2006; Koyama et al., 2004) That is, activations were found in a region which is thought to be part of an extended oculomotor region (Amiez and Petrides, 2009) associated with visual pursuit (Fukushima et al., 2002), and which is largely occupied by the areas composing our cluster 4. In particular, premotor areas of the extended oculomotor region are thought to play a role in blinking movement (Bruce et al., 1985) and in coordinating eye-arm movements within the peripersonal space (Fujii et al., 1998).

#### Areas of cluster 5

Finally, primary motor areas 4m, 4a, and 4p demonstrated greater dissimilarity of their receptor fingerprints in regard to rest of the frontal areas and formed segregated cluster. Indeed, these areas are characterized by the one of the smallest receptor fingerprints among all areas identified in this study. Present and previous analysis of subdivisions of area 4 of our own group (Rapan et al., 2021) revealed differences in cyto- and receptor architecture as well as functional connectivity between area 4p, located mainly on the anterior bank of the central sulcus, and two other motor subdivisions, occupying the precentral convexity and medial surface of the hemisphere. In particular, area 4p showed strong functional correlation to the rostral areas PF, PFop, and PFG of the inferior parietal lobule, associated with somatosensory and body-related responses (Andersen et al., 1990a), whereas areas 4m and 4a showed higher correlations with caudal areas Opt, PG, and PGm, which are involved in visuomotor coordination (Andersen et al., 1990a; Andersen et al., 1990b). Unlike medial and dorsolateral areas, cortex occupied by area 4p has a higher packing density of the cortico-motor neurons (Rathelot and Strick, 2009), associated with the fine movements, such as the independent finger movement (Porter and Lemon, 1995). These neurons also play a role in the mapping of a new motor outline, which would enable performance of an additional skill (Rathelot and Strick, 2009). Since prefrontal area 44 revealed to be strongly connected with areas in premotor cortex associated with a hand movement, it is interesting that it also has strong functional connectivity with motor area 4p.

## Materials and methods

### Tissue processing

Both hemispheres of an adult macaque monkey (M. mulatta; male; brain ID DP1; 8 y; obtained as a gift from Professor Deepak N. Pandya) were used for cytoarchitectonic analysis in histological sections of a paraffin-embedded brain. Sodium pentobarbital was applied to deeply anesthetize the monkey, followed by a transcardial perfusion with cold saline and then 10% buffered formalin. The brain was removed and stored in a buffered formalin solution until further processing.

The brains of three adult macaques (M fascicularis; males; brain IDs 11530, 11539, 11543; 6 ± 1 y of age; obtained from Covance Laboratories, Münster, Germany) were processed for both cyto- and receptor architectonic analysis. Monkeys were sacrificed by means of a lethal intravenous injection of sodium pentobarbital. However, since receptor proteins are delicate in nature, only unfixed, deep frozen tissue can be used for receptor autoradiography (Herkenham et al., 1990; Zilles et al., 2002). Thus, the brains were immediately removed from the skull together with meninges and blood vessels to avoid further damage of superficial layers. The cerebellum, together with the brainstem, was separated from the rest of the brain. Each hemisphere was further divided into an anterior and a posterior slab at the level of the most caudal portion of the central sulcus. In this study, we examined all left hemispheres, except for brain 11539, where both hemispheres were analysed. The slabs were carefully placed on an aluminium plate to avoid any further deformation and slowly introduced into N-methylbutane (isopentane) at –40°C, where they were left for 10–15 min. Frozen slabs were stored in air-tight plastic bags at –80°C until used for sectioning. Animal care was provided in accordance with the NIH Guide for Care and Use of Laboratory Animals, and the European local Committee, and complied with the European Communities Council Directive.

### Identification of cortical areas

Starting point for the present parcellation was visual and microscopic inspection of our sectioned brains and previously published cytoarchitectonic literature of the macaque prefrontal cortex. Specifically, analysis of the OFC and ventrolateral areas 10, 11, 12, 13, and 14 was based on the parcellation scheme and nomenclature proposed by Carmichael and Price, 1994. Nomenclature of prefrontal areas 9, 8B, 8A, 46, and 45 is based on Walker’s (Walker, 1940) original parcellation scheme, though integrating later modifications (Morecraft et al., 2012; Petrides, 2005; Preuss and Goldman-Rakic, 1991).

Since the identification of neighbouring areas, based on a pure visual inspection, has previously resulted in maps that differ in terms of number, localization, and shape of cortical areas, in this study we applied a quantitative and statistically testable approach to test the localization and existence of all visually identified cytoarchitectonic borders (Schleicher et al., 2000; Schleicher et al., 2009; Zilles et al., 2002). Furthermore, cytoarchitectonically identified areas were further confirmed by differences in the regional and laminar distribution patterns of multiple neurotransmitter receptors, that is, by differences in receptor architecture.

### Processing postmortem brain and analysis of cytoarchitecture

DP1 brain was dehydrated in ascending graded alcohols (70–100% propanol), completed by a step-in chloroform. The brain was then embedded in paraffin and serially cut in the coronal plane with a large-scale microtome, resulting in 3305 20-µm-thick whole-brain sections. Every fifth section was mounted on gelatin-coated slides. Paraffin was removed and sections were rehydrated by a two-step washing (each of 10 min) with Xem-200 (‘Xylol-Ersatz-Medium,’ Vogel, Diatec Labortechnik GmbH) followed by graded washes in alcohol (10 min each in 100, 96, and 70% propanol) and finally a rinse in a pure water.

Sections were stained with a modified silver method (Merker, 1983; Uylings et al., 1999), which provides a high contrast between cell bodies and neuropil. In short, sections were pretreated 4 hr in 4% formic acid, then overnight in a 10% formic acid/30% peroxide solution. Sections were thoroughly washed, immersed twice for 5 min in 1% acetic acid, placed in a physical developer under constant movement until they become greyish, and then further developed with constant monitoring under the microscope until cell bodies were dark grey/black. The developer was prepared immediately before use by adding 30 ml of stock solution B (2 g AgNO3, 2 g NH4NO3 and 10 g SiO2•12WO3•26H2O dissolved in 1 l distilled water; stored at room temperature) and then 70 ml of stock solution C (2 g AgNO3, 2 g NH4NO3, 10 g SiO2•12WO3•26H2O and 7.3 ml of a 37% formaldehyde solution dissolved in 1 l distilled water; stored at room temperature) to 100 ml of stock solution A (50 g Na2CO3 dissolved in 1 l distilled water; stored at 4°C) under vigorous stirring, and development was terminated by two 5 min washes in 1% acetic acid. Sections were then fixed 5 min in a T-Max fixative (Kodak, two parts of T-Max and seven parts of distilled water), dehydrated in ascending grades of alcohol (70%, 96%, 100%) for 5 min in each dilution followed by two 5 min immersions in xylene before coverslipping with DePex mounting medium.

Sections were scanned with a light microscope (Axioplan 2 imaging, Zeiss, Germany) equipped with a motor-operated stage controlled by the KS400 and Axiovision (Zeiss) image analysing systems applying a 6.3 ×1.25 objective (Planapo, Zeiss) and a CCD camera (Axiocam MRm, Zeiss). Digitalized images are produced by stitching individual frames of 524 × 524 µm in size, 512 × 512-pixel spatial resolution, and in-plane resolution of 1 µm per pixel and 8-bit grey resolution.

The quantitative approach to cytoarchitectonic analysis relies on the volume fraction of cell bodies as estimated by the grey level index (GLI) in square measuring field, which is of fixed size (Schleicher et al., 2009). For each identified area, GLI images were generated from three neighbouring sections in the rostro-caudal direction, and ROIs were defined around each portion of the cortical ribbon where border had been identified by visual inspection by manually drawing an outer (at the interface between layers I and II) and an inner (at the border between layer VI and the white matter) contour. These contour lines were used to define equidistant traverses running perpendicularly to the cortical surface, along which the changes in grey values quantify the laminar pattern characteristic of a cortical area (Schleicher et al., 2009) and are measured as GLI-profiles (for details see Palomero-Gallagher and Zilles, 2019; Zilles et al., 2002). The shape of the profile can be parametrized, that is, presented as a frequency distribution of 10 features, which quantitatively describe the laminar distribution of the volume fraction of the cell bodies, constitute a feature vector of each profile, and can be standardized using different scales to set equal weight to each of the values used for multivariate analyses (Schleicher et al., 2005; Zilles et al., 2002).

Assuming that each area has a distinctive laminar pattern, areal borders would be located at the transition of the laminar pattern of one area to that of the neighbouring area. Therefore, the Mahalanobis distance (MD; Mahalanobis et al., 1949) was applied to quantify differences in the shape of two profiles and enable detection of the position of borders (Schleicher et al., 2005; Zilles et al., 2002). Adjacent profiles were grouped into blocks to operate as a sliding widow shifting along the cortical ribbon by the distance of one profile, whereby the MD between immediately adjacent blocks was calculated and plotted as a distance function for all block positions. This process was repeated, but with systematically increasing block sizes from 10 to 24 profiles in order to control the stability of a distance function that changes with a number of profiles in a block. If two blocks belong to the same area, MD values are expected to be small since their laminar pattern coded by the profiles being compared is similar. To confirm and accept MD maxima as architectonically relevant borders, we applied Hotelling’s T2 test in combination with a Bonferroni adjustment of the p-values for multiple comparisons (Schleicher et al., 2005; Zilles et al., 2002). Finally, main maxima identified with numerous block sizes in one histological section were evaluated by comparison with corresponding maxima in three consecutive sections to exclude biologically meaningless maxima which may be caused by artefacts (e.g. ruptures, folds) or local discontinues in microstructure due to blood vessels or untypical cell clusters.

In order to visualize the relationship between identified areas and macroanatomic landmarks, we created a 2D flat map and a 3D model of the macaque prefrontal cortex. For the 2D flat map we generated a framework based on the sulcal anatomy of the DP1 brain, whereby every 40th section was represented as a line with indentations representing characteristic sulci and dimples and cytoarchitectonic borders were positioned relative to the corresponding macroscopic landmarks. Thus, the ensuing flat map enables visualization of borders even when they are located inside sulci (for more details see Rapan et al., 2021). To compute the 3D model, the positions of borders relative to macroanatomic landmarks (i.e. the fundus of sulci or dimples and the apex of gyri) were transferred by means of the connectome workbench software (https://www.humanconnectome.org/software/connectome-workbench) to the surface representation of the Yerkes19 template brain (Donahue et al., 2016), thus also bringing our parcellation scheme into stereotaxic space.

### Processing unfixed brains and analysis of receptor architecture

We used quantitative in vitro receptor autoradiography to visualize binding sites of native receptors expressed on the cell membrane of neurons and glia cells. The advantage of this method is that it can be carried out on a large number of sections encompassing an entire hemisphere, alongside the possibility of precise quantification and a high specificity (Palomero-Gallagher and Zilles, 2018; Zilles et al., 2002).

Unfixed frozen slabs were serially sectioned in the coronal plane using a cryostat at –20°C, into 20-µm-thick sections, which were thaw-mounted on gelatin-coated glass slides. Sections were left to air dry and stored overnight in air-tight plastic bags at –20°C. Serial sections were used for the visualization of 14 distinct receptors types, that is, for glutamate (AMPA, kainate, NMDA), gamma-aminobutyric acid (GABA) (GABAA, GABAB, GABAA-associated benzodiazepine binding sites [BZ]), acetylcholine (M1, M2, M3), noradrenalin (α1, α2), serotonin (5HT1A, 5HT2), and dopamine (D1), as well as for the visualization of cell bodies (see previous section) using previously published protocols (Palomero-Gallagher et al., 2009; Zilles et al., 2002; see Table 5), in three subsequent steps: a preincubation, a main incubation, and a rinsing step. The preincubation is carried out to rehydrate sections and to remove endogenous ligands that could block the binding sites. During the main incubation, two parallel experiments are conducted to test the specific binding ability of each ligand. In one, sections were incubated in a buffer solution with tritiated ligand to identify total binding of each ligand type. In the second, neighbouring sections were incubated in buffer solution containing the tritiated ligand and a receptor type-specific displacer in a 1000-fold higher concentration to visualize non-specific binding of the same ligand. Finally, the difference between total and non-specific binding demonstrates the specific binding ability for each ligand. In this study, specificity of ligands used resulted in a non-specific binding of less than 5% of the total binding. In the rinsing step, the binding process was stopped and free ligand and buffer salts removed. Air-dried, radioactive sections were then co-exposed with plastic tritium-standards (calibrated for protein density, and with known increasing concentrations of radioactivity) against β radiation-sensitive films (Hyperfilm, Amersham) for 4–18 wk depending on the analysed ligand. A densitometric analysis (Palomero-Gallagher and Zilles, 2018; Zilles et al., 2002) was carried to measure binding site concentrations in the ensuing receptor autoradiographs.

Autoradiographs were digitized with an image analysis system consisting of a source of homogeneous light and a CCD-camera (Axiocam MRm, Zeiss) with an S-Orthoplanar 60 mm macro lens (Zeiss) corrected for geometric distortions, connected to the image acquisition and processing system Axiovision (Zeiss). Spatial resolution of the resulting images was 3000 × 4000 pixels; 8-bit grey value resolution. The grey values of the digitized autoradiographs code for concentrations of radioactivity. To transform grey values into fmol binding sites/mg protein, a linearization of the digitized autoradiographs had to be performed in a two-steps process, carried out with in-house-developed MATLAB (The MathWorks, Inc, Natrick, MA) scripts. First, the grey value images of the plastic tritium standards were used to compute the calibration curve, which defines the nonlinear relationship between grey values and concentrations of radioactivity. Then radioactivity concentration R was then converted to binding site concentration Cb in fmol/mg protein using Equation 1:

$$
C_{b}=\frac{R}{E⋅B⋅W_{b}⋅S_{a}}⋅\frac{K_{D}+L}{L}
$$

where E is the efficiency of the scintillation counter used to determine the amount of radioactivity in the incubation buffer (depends on the actual counter), B is the number of decays per unit of time and radioactivity (Ci/min), Wb is the protein weight of a standard (mg), Sa is the specific activity of the ligand (Ci/mmol), KD is the dissociation constant of the ligand (nM), and L is the free concentration of the ligand during incubation (nM) (Palomero-Gallagher and Zilles, 2018; Zilles et al., 2002). For visualization purposes, a linear contrast enhancement and pseudo-colour coding of autoradiographs was applied using a spectre of 11 colours with equally spaced density ranges (red colour for highest and black for lowest receptor concentration levels).

Measurement of receptor binding sites (averaged over all cortical layers) was performed by computing the surface below receptor profiles, which were extracted from the linearized autoradiographs using in-house-developed scripts for MATLAB (The MathWorks, Inc) in a manner comparable to the procedure described above for GLI profiles. However, for receptor profiles the outer contour line was defined following the pial surface, and not the border between layers I and II. Thus, for each area (with the exception of areas 13m and 13l) and receptor type, we extracted profiles from three consecutive sections in each of the four hemispheres examined. Due to technical problems, we were only able to obtain this data for areas 13m and 13l from two hemispheres (11530 and 11539_R), and we could not measure receptor densities in areas 14c and 13a.

**Table 5.**
 Receptor labelling protocols.Square brackets indicate substances that are only included in the buffer solution for the main incubation.


<table>
  <thead>
    <tr>
      <th>Transmitter</th>
      <th>Receptor</th>
      <th>Mechanismoutcome</th>
      <th>Ligand(nM)</th>
      <th>Property</th>
      <th>Displacer(μM)</th>
      <th>Incubation buffer</th>
      <th>Pre- incubation</th>
      <th>Main incubation</th>
      <th>Final rinsing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Glutamate</td>
      <td>AMPA</td>
      <td>ExcitatoryIonotropic</td>
      <td>[3H]-AMPA(10)</td>
      <td>Agonist</td>
      <td>Quisqualate(10)</td>
      <td>50 mM Tris-acetate (pH 7.2) [+100 mM KSCN]</td>
      <td>3 × 10 min,4°C</td>
      <td>45 min, 4°C</td>
      <td>1. 4 × 4 s2. Acetone/glutaraldehyde (100 ml + 2,5 ml), 2 × 2 s, 4°C</td>
    </tr>
    <tr>
      <td>NMDA</td>
      <td>ExcitatoryIonotropic</td>
      <td>[3H]-MK-801(3.3)</td>
      <td>Antagonist</td>
      <td>(+)MK-801 (100)</td>
      <td>50 mM Tris-acetate (pH 7.2) + 50 μM glutamate [+30 μM glycine +50 μM spermidine]</td>
      <td>15 min, 4°C</td>
      <td>60 min, 22°C</td>
      <td>1. 2 × 5 min, 4°C2. Distilled water, 1 × 22°C</td>
    </tr>
    <tr>
      <td>Kainate</td>
      <td>ExcitatoryIonotropic</td>
      <td>[3H]-Kainate(9.4)</td>
      <td>Agonist</td>
      <td>SYM 2081(100)</td>
      <td>50 mM Tris-acetate (pH 7.1) [+10 mM Ca2+-acetate]</td>
      <td>3 × 10 min,4°C</td>
      <td>45 min, 4°C</td>
      <td>1. 3 × 4 s2. Acetone/glutaraldehyde (100 ml + 2.5 ml), 2 × 2 s, 22° C</td>
    </tr>
    <tr>
      <td rowspan="3">GABA</td>
      <td>GABAA</td>
      <td>InhibitoryIonotropic</td>
      <td>[3H]-Muscimol(7.7)</td>
      <td>Agonist</td>
      <td>GABA(10)</td>
      <td>50 mM Tris-citrate (pH 7.0)</td>
      <td>3 × 5 min,4°C</td>
      <td>40 min, 4°C</td>
      <td>1. 3 × 3 s, 4°C2. Distilled water, 1 × 22°C</td>
    </tr>
    <tr>
      <td>GABAB</td>
      <td>InhibitoryMetabotropic</td>
      <td>[3H]-CGP 54626(2)</td>
      <td>Antagonist</td>
      <td>CGP 55845(100)</td>
      <td>50 mM Tris-HCl (pH 7.2) + 2.5 mM CaCl2</td>
      <td>3 × 5 min,4°C</td>
      <td>60 min, 4°C</td>
      <td>1. 3 × 2 s, 4°C2. Distilled water, 1 × 22°C</td>
    </tr>
    <tr>
      <td>GABAA/Bz</td>
      <td>InhibitoryIonotropic</td>
      <td>[3H]-Flumazenil(1)</td>
      <td>Antagonist</td>
      <td>Clonazepam (2)</td>
      <td>170 mM Tris-HCl (pH 7.4)</td>
      <td>15 min, 4°C</td>
      <td>60 min, 4°C</td>
      <td>1. 2 × 1 min, 4°C2. Distilled water, 1 × 22°C</td>
    </tr>
    <tr>
      <td rowspan="3">Acetylcholine</td>
      <td>M1</td>
      <td>ExcitatoryMetabotropic</td>
      <td>[3H]-Pirenzepine(1)</td>
      <td>Antagonist</td>
      <td>Pirenzepine(2)</td>
      <td>Modified Krebs buffer(pH 7.4)</td>
      <td>15 min, 4°C</td>
      <td>60 min, 4°C</td>
      <td>1. 2 × 1 min, 4°C2. Distilled water, 1 × 22°C</td>
    </tr>
    <tr>
      <td>M2</td>
      <td>InhibitoryMetabotropic</td>
      <td>[3H]-Oxotremorine-M(1.7)</td>
      <td>Agonist</td>
      <td>Carbachol(10)</td>
      <td>20 mM HEPES-Tris (pH 7.5) + 10 mM MgCl2 + 300 nM pirenzepine</td>
      <td>20 min, 22°C</td>
      <td>60 min, 22°C</td>
      <td>1. 2 × 2 min, 4°C2. Distilled water, 1 × 22°C</td>
    </tr>
    <tr>
      <td>M3</td>
      <td>ExcitatoryMetabotropic</td>
      <td>[3H]–4-DAMP(1)</td>
      <td>Antagonist</td>
      <td>Atropine sulfate(10)</td>
      <td>50 mM Tris-HCl (pH 7.4) + 0.1 mM PSMF +1 mM EDTA</td>
      <td>15 min, 22°C</td>
      <td>45 min, 22°C</td>
      <td>1. 2 × 5 min, 4°C2. Distilled water, 1 × 22°C</td>
    </tr>
    <tr>
      <td rowspan="2">Noradrenaline</td>
      <td>α1</td>
      <td>ExcitatoryMetabotropic</td>
      <td>[3H]-Prazosin(0.2)</td>
      <td>Antagonist</td>
      <td>Phentolamine mesylate(10)</td>
      <td>50 mM Na/K-phosphate buffer (pH 7.4)</td>
      <td>15 min, 22°C</td>
      <td>60 min, 22°C</td>
      <td>1. 2 × 5 min, 4°C2. Distilled water, 1×22°C</td>
    </tr>
    <tr>
      <td>α2</td>
      <td>InhibitoryMetabotropic</td>
      <td>[3H]-UK 14,304(0.64)</td>
      <td>Agonist</td>
      <td>Phentolamine mesylate(10)</td>
      <td>50 mM Tris-HCl + 100 μM MnCl2 (pH 7.7)</td>
      <td>15 min, 22°C</td>
      <td>90 min, 22°C</td>
      <td>1. 5 min, 4°C2. Distilled water, 1×22°C</td>
    </tr>
    <tr>
      <td rowspan="2">Serotonin</td>
      <td>5-HT1A</td>
      <td>InhibitoryMetabotropic</td>
      <td>[3H]–8-OH-DPAT(1)</td>
      <td>Agonist</td>
      <td>5-Hydroxy- tryptamine, (1)</td>
      <td>170 mM Tris-HCl (pH 7.4) [+4 mM CaCl2+ 0.01% ascorbate]</td>
      <td>30 min, 22°C</td>
      <td>60 min, 22°C</td>
      <td>1. 5 min, 4°C2. Distilled water, 3×22°C</td>
    </tr>
    <tr>
      <td>5-HT2</td>
      <td>ExcitatoryMetabotropic</td>
      <td>[3H]-Ketanserin(1.14)</td>
      <td>Antagonist</td>
      <td>Mianserin(10)</td>
      <td>170 mM Tris-HCl (pH 7.7)</td>
      <td>30 min, 22°C</td>
      <td>120 min, 22°C</td>
      <td>1. 2 × 10 min, 4°C2. Distilled water, 3 × 22°C</td>
    </tr>
  </tbody>
</table>

Densities (i.e. averaged over all cortical layers) of each of the 14 different receptors in 33 of the 35 cytoarchitectonically defined areas were calculated. Due to technical limitations associated with the cutting angle of the coronal sections, it was not possible to measure densities in areas 13a and 14c. The precise sampling for the measurements of each cytoarchitectonically defined area was verified by aligning autoradiographs with defined cytoarchitectonic borders in neighbouring silver-staining sections in the corresponding brain processed for the receptor architectonic analysis. For each of the examined areas and their subdivisions, the mean densities of all receptors averaged over all four hemispheres in that area were then visualized simultaneously as ‘receptor fingerprints,’ that is, as polar coordinate plots which reveal the specific balance of different receptor types within a cytoarchitectonic entity (Zilles et al., 2002).

#### Statistical analysis of the receptor densities

To determine whether there were significant differences in receptor architecture between paired areas (in particular our analysis was focused on directly bordering areas within the prefrontal region), stepwise linear mixed-effect models were performed. A z-score normalization was performed for each receptor separately to ensure an equal weighting of all receptors in subsequent statistical analyses. All statistical analyses were conducted using the R programming language (version 3.6.3.; Team, 2013).

We conducted a statistical testing which included three levels. In the first level, an omnibus test was carried out to determine whether there were differences across all regions when all receptor types are considered simultaneously (Equation 2). The model consists of fixed effects for area and receptor type, and hemisphere was set as a random factor.

$$
D_{a,r,h}=\alpha_{o}+\alpha_{1}A_{a}+\alpha_{2}R_{r}+\alpha_{3}A_{a}R_{r}+\beta_{1}H_{h}
$$

where D represents the receptor density, A is the prefrontal area, R is the receptor type, and H is the hemisphere.

If the interaction effect between area and receptor type at first level of testing was found to be significant, a second level of simple effect tests was applied for each receptor separately to determine whether there were significant differences across all areas for each receptor type. The p-values were corrected for multiple comparison using the Benjamini–Hochberg correction for false discovery rate (Benjamini and Hochberg, 1995).

Finally, the third-level post hoc tests were used to identify the paired areas driving the statistical difference in the second-level tests. For each receptor type, 528 post hoc tests were performed. To correct for multiple comparisons in the third step tests, we performed the false discovery rate correction (Benjamini and Hochberg, 1995) separately for each receptor type (i.e. p-values were corrected for 528 comparisons per receptor type).

### Visualization and analysis of functional connectivity

All datasets used here for analysis are openly available sources from the recently established PRIME-DE (http://fcon_1000.projects.nitrc.org/indi/indiPRIME.html; Milham et al., 2018). Resting-state fMRI data from 19 macaque monkeys (all males, age = 4.01 ± 0.98 y) was collected with no contrast agent on a 3T scanner with a four-channel coil in Oxford (Noonan et al., 2014). For each animal, one resting-state scan (6.67 min, 250 volumes) was used. These data were downloaded from the PRIME-DE database (Milham et al., 2018) and preprocessed using a Human Connectome Project-like pipeline for Nonhuman Primate as described previously (Autio et al., 2020; Xu et al., 2015; Xu et al., 2018; Xu et al., 2019). For each macaque, the structural preprocessing includes denoising, skull-stripping, tissue segmentation, surface reconstruction, and surface registration to align to Yerkes19 macaque surface template (Donahue et al., 2016). The functional preprocessing includes temporal compressing, motion, correction, global mean scaling, nuisance regression (Friston’s 24 motion parameters, white matter, cerebrospinal fluid), band-pass filtering (0.01–0.1 Hz), and linear and quadratic detrending. The preprocessed data then were co-registered to the anatomy T1 and projected to the middle cortical surface. Finally, the data were smoothed (FWHM = 3 mm) on the high-resolution native surface, aligned, and downresampled to a 10k surface (10,242 vertices per hemisphere). The preprocessed BOLD activity time courses for each monkey brain were demeaned and then concatenated in time. This enabled us to estimate the group functional connectivity maps for each seed region in a single analysis.

The connectivity of each identified prefrontal areas was investigated in regard to 76 cortical areas, previously defined by Palomero-Gallagher group, that is, 16 areas of (pre)motor cortex, 15 areas of cingulate cortex, 6 areas of somatosensory cortex, 23 areas of parietal cortex, and 16 areas of occipital cortex (Impieri et al., 2019; Niu et al., 2021; Rapan et al., 2021; Rapan et al., 2022). A representative time course was calculated for each of the 35 prefrontal areas and the 76 (pre)motor, cingulate, somatosensory, parietal, and occipital areas, giving 111 areas in total. For each of the 111 areas, a principal components analysis was performed on activity across all vertices within the area, where the first principal component was taken as the representative activity time course for each area.

The representative time courses of each of the 35 prefrontal areas were used as seeds for functional connectivity analysis. Since they were correlated with the activity time courses for each vertex on the surface using a Pearson correlation. A Fisher’s r-to-z transformation was then applied to each of the correlation coefficients. This was visualized on the Yerkes19 cortical surface. Code used for the implementation and visualization of the functional connectivity analysis has been made publicly available (https://github.com/seanfw/macaque-pfc-func-conn, copy archived at Rapan, 2023).

### Multivariate analyses of receptor fingerprints

To reveal structure–function relationship between areas of the frontal lobe, we not only used receptor fingerprints of the here identified 33 prefrontal areas (except areas 13a and 14c, see above), but also included those of previously identified 16 motor and premotor areas (Rapan et al., 2021). Receptor densities were extracted from the same macaque brains. Hierarchical clustering and principal component analyses were carried out to enable grouping of areas based on receptor architectonic similarities (Palomero-Gallagher et al., 2009). We used a receptor fingerprint of each area as a feature vector characterizing the area of interest. The Euclidean distance, which takes into account difference in the size and shape of fingerprint, was applied as a measure of (dis)similarities between receptor fingerprints.

Before any statistical analysis was conducted, it was necessary to normalize all absolute receptor values due to large differences in absolute densities across receptor types. Receptors with high absolute density values (i.e. GABAergic receptors) would dominate the calculation of the Euclidean distance between areas, as well as of the principal component analysis, cancelling intended multimodal approach in the present analysis. Whereas normalized receptor values enable for each receptor type to contribute with equal significance to the statistical analyses. Here, z-scores calculation was applied since this approach maintains the relative differences in receptor densities among areas, that is, the mean density of a given receptor across all examined areas was subtracted from the mean density of the same receptor in a defined area and obtained value was divided by the standard deviation of that receptor over all areas. The Ward linkage algorithm was chosen as the linkage method in combination with the Euclidean distances. It yielded a higher cophenetic correlation coefficient than any other combination of alternative linkage methods and measurements of (dis)similarity. The cophenetic correlation coefficient quantifies how well the dendrogram represents the true, multidimensional distances within the input data. The k-means analysis was applied to identify the highest acceptable number of clusters and confirmed by the k-means permutation test.

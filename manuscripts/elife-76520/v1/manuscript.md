# Interplay of adherens junctions and matrix proteolysis determines the invasive pattern and growth of squamous cell carcinoma

## Authors

- Takuya Kato<sup>1</sup> ([ORCID: 0000-0002-4972-657X](https://orcid.org/0000-0002-4972-657X))
- Robert P Jenkins<sup>1</sup> ([ORCID: 0000-0002-6186-7746](https://orcid.org/0000-0002-6186-7746)) †
- Stefanie Derzsi<sup>1</sup>
- Melda Tozluoglu<sup>4</sup>
- Antonio Rullan<sup>1</sup>
- Steven Hooper<sup>1</sup>
- Raphaël AG Chaleil<sup>4</sup>
- Holly Joyce<sup>1</sup>
- Xiao Fu<sup>1</sup>
- Selvam Thavaraj<sup>6</sup> ([ORCID: 0000-0001-5720-7422](https://orcid.org/0000-0001-5720-7422))
- Paul A Bates<sup>4</sup> ([ORCID: 0000-0003-0621-0925](https://orcid.org/0000-0003-0621-0925))
- Erik Sahai<sup>1</sup> ([ORCID: 0000-0002-3932-5086](https://orcid.org/0000-0002-3932-5086)) †

### Affiliations

1. Tumour Cell Biology Laboratory, The Francis Crick Institute London United Kingdom ([ROR:04tnbqb63](https://ror.org/04tnbqb63))
2. Department of Pathology, Kitasato University Sagamihara Japan ([ROR:02b3e2815](https://ror.org/02b3e2815))
3. Hoffman La-Roche Basel Switzerland ([ROR:00by1q217](https://ror.org/00by1q217))
4. Biomolecular Modelling Laboratory, The Francis Crick Institute London United Kingdom ([ROR:04tnbqb63](https://ror.org/04tnbqb63))
5. Institute of Cancer Research London United Kingdom ([ROR:043jzw605](https://ror.org/043jzw605))
6. Centre for Oral, Clinical and Translational Sciences, King's College London London United Kingdom ([ROR:0220mzb33](https://ror.org/0220mzb33))

† Corresponding author

## Abstract

Cancers, such as squamous cell carcinoma, frequently invade as multicellular units. However, these invading units can be organised in a variety of ways, ranging from thin discontinuous strands to thick ‘pushing’ collectives. Here we employ an integrated experimental and computational approach to identify the factors that determine the mode of collective cancer cell invasion. We find that matrix proteolysis is linked to the formation of wide strands but has little effect on the maximum extent of invasion. Cell-cell junctions also favour wide strands, but our analysis also reveals a requirement for cell-cell junctions for efficient invasion in response to uniform directional cues. Unexpectedly, the ability to generate wide invasive strands is coupled to the ability to grow effectively when surrounded by extracellular matrix in three-dimensional assays. Combinatorial perturbation of both matrix proteolysis and cell-cell adhesion demonstrates that the most aggressive cancer behaviour, both in terms of invasion and growth, is achieved at high levels of cell-cell adhesion and high levels of proteolysis. Contrary to expectation, cells with canonical mesenchymal traits – no cell-cell junctions and high proteolysis – exhibit reduced growth and lymph node metastasis. Thus, we conclude that the ability of squamous cell carcinoma cells to invade effectively is also linked to their ability to generate space for proliferation in confined contexts. These data provide an explanation for the apparent advantage of retaining cell-cell junctions in squamous cell carcinomas.

## Introduction

Tumours exhibit a variety of histological patterns that inform pathological diagnosis and that are frequently linked to prognosis (Dive et al., 2014). This link with outcome suggests that the mechanisms specifying histological pattern are related to tumour malignancy. This may be due to some coupling between how cancer cells invade and their ability to proliferate. Epithelial cancer cells, including squamous cell carcinoma (SCC), frequently invade in collective units (Friedl and Gilmour, 2009; Khalil et al., 2017; Wang et al., 2016). The importance of collective invasion is underscored by several recent studies showing that collective seeding of metastases is more efficient than single cell seeding (Cheung et al., 2016; Fischer et al., 2015; Khalil et al., 2017; Padmanaban et al., 2019). Despite the prevalence and importance of collective patterns of cancer cell invasion, it remains less well understood than single cell forms of invasion. Collectively invading cancer strands can be organised in a variety of different ways, from single file strands that characterise invasive lobular breast cancer and diffuse gastric cancer to broad cohesive units found in basal cell carcinoma (Boelens et al., 2016; Carneiro et al., 2004; Friedl et al., 2012; Pandya et al., 2017). Histological analysis indicates that even within a single disease type there is considerable heterogeneity in the pattern of invasion; for example, both broad ‘pushing’ and strand-like infiltrative invasion can be observed in SCC (Dissanayaka et al., 2012). In this study, we set out to explore the key parameters that determine the pattern of collective invasion using a combination of computational and experimental approaches.

Several parameters might be expected to modulate tumour histology and, more specifically, collective cancer cell invasion. The ability of cancer cells to adhere to each other through cadherin-mediated junctions is linked to their organisation into tightly packed clusters. E-cadherin/CDH1 and, to a lesser extent, P-cadherin/CDH3 are the predominant cadherins in mucosal squamous cell carcinomas (SCC or muSCC specifically for mucosal SCC; Nieman et al., 1999) that typically do not undergo a clear epithelial to mesenchymal transition (EMT). These cadherins are coupled to the actin cytoskeleton via a complex containing α-catenin and β-catenin (Nelson et al., 2013). Cell adhesion to the extracellular matrix (ECM) is also critical for cell migration and invasion in many contexts (Cooper and Giancotti, 2019; Hamidi and Ivaska, 2018). This is primarily mediated by integrin receptors (Hamidi and Ivaska, 2018; Janes and Watt, 2006), with ITGB1 particularly highly expressed in SCC (Janes and Watt, 2006). The ECM presents a barrier to migration if the gaps between fibres are smaller than 3–5 μm (Wolf et al., 2013; Wolf et al., 2009). The dermal ECM underlying SCC lesions is predominantly composed of type I collagen (Watt and Fujiwara, 2011), and numerous studies have demonstrated that MMP14/MT-1MMP is the critical protease for degrading this type of matrix (Castro-Castro et al., 2016; Gifford and Itoh, 2019). The ECM can also be physically moved by forces generated by the contractile cytoskeleton (Mohammadi and Sahai, 2018; Wolf et al., 2013). In many cases, stromal cells are the major source of both matrix proteolytic and force-mediated matrix remodelling in tumours (Conklin and Keely, 2012; Kalluri and Zeisberg, 2006). Cancer-associated fibroblasts (CAFs, sometimes referred to as stromal fibroblasts) can promote the invasion of SCC by providing these functions and are frequently observed leading the migration of cancer cells that retain epithelial characteristics (Gaggioli et al., 2007).

Understanding the relative contributions of the multiple parameters outlined above to cell invasion is a complex multi-dimensional problem with non-linear relationships between parameters and migratory capability. This complexity means that developing a holistic and predictive framework for collective cancer cell invasion using empirical methods only is challenging. For this reason, several studies have sought to utilise computational models. Many different types of model have been used including those based on evolutionary game theory (Basanta et al., 2008; Swierniak and Krzeslak, 2013), Bayesian networks (Katz et al., 2011), differential equations (Gerisch and Chaplain, 2008; Peng et al., 2017; Weekes et al., 2014), agent-based models including cellular automata (Alarcón et al., 2003; Bull et al., 2020; Fiore et al., 2020; Gralka and Hallatschek, 2019; Karolak et al., 2019; Norton et al., 2017; Talkenberger et al., 2017) and hybrids of the above (Anderson, 2005; Anderson et al., 2006; Osborne et al., 2010). Cellular Potts modelling (Cickovski et al., 2007; Graner and Glazier, 1992; Hallou et al., 2017; Pramanik et al., 2021; Scianna et al., 2013; Shirinifard et al., 2009; Szabó and Merks, 2013; Turner and Sherratt, 2002) is a flexible approach that uses voxels to represent different parts of cells or their environment. Changes in the properties associated with each voxel are determined at each time step using principles of probabilistic energy minimisation. The behaviour of the model therefore emerges from iterative application of rules that describes the relative favourability of different events or changes. Here we combine a Potts modelling with extensive experimentation to unpick the determinants of the mode of collective cancer cell invasion and their linkage to cancer cell growth, both in vitro and in vivo.

## Results

### Diverse modes of collective invasion within individual SCC

We began by surveying the diversity of invasive pattern in muSCC. Figure 1a shows considerable diversity in the nature of collective invasion. Furthermore, it illustrates how initial invasion involves cells moving from the epithelial layer into the lamina propria (often termed epidermis and dermis, respectively, in cutaneous skin). Following the invasion into the dermis, cancer cells become surrounded on all sides by ECM. Interestingly, different patterns of invasion were observed in different regions of the same tumour (Figure 1a). These ranged from broad ‘pushing’ invasive masses of cells (box I), thinner strands of cells (box II), to single-cell width strands and apparently isolated single cells (box III - although this could not be definitively determined from single H&E (Hematoxylin and Eosin) sections). Quantitative analysis of the number of cell neighbours provided a more objective metric of invasion type, with high neighbour numbers (typically 4–7) indicating broad invasion patterns and low neighbour numbers (2 or 3) indicating thin strand-like invasion, respectively (Figure 1b). Similar patterns were observed in other muSCC biopsies with different strand thickness apparent (Figure 1—figure supplement 1a–f). Analysis of neighbour number suggested that strand thickness does not fall into distinct categories, with neighbour number varying continuously between 1 and 9.

![Figure 1.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig1-v1.jpg)

**Figure 1.:** (a) Images show a human invasive head and neck SCC stained with haematoxylin and eosin. Inset regions show different patterns of collective invasion: I – large rounded clusters, II – intermediate clusters, III – elongated strands only one or two cells wide. (b) Plot shows the mean number of cancer cell neighbours for each cell within invasive strands with the morphologies exemplified in panel (a) I, II, and III. One-way ANOVA with post-hoc multiple comparisons was performed. 95% confidence intervals are shown, one dot represents one cell analysed. (c) Images show phase contrast microscopy of a human oral SCC invading into a collagen/Matrigel mixture. Scale bar is 100 μm. Lower panels show manual tracking of individual cells within the clusters.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (a) Images show a human invasive head and neck squamous cell carcinoma stained with haematoxylin and eosin (left) and anti-α-Smooth Muscle Actin (SMA) (right). Inset regions show different patterns of collective invasion: I – large rounded clusters, II – intermediate clusters, III – elongated strands only one or two cells wide. (b–d) Images show three further human invasive head and neck squamous cell carcinoma: stained with haematoxylin and eosin and cytokeratin (bottom right). Inset regions show different patterns of collective invasion: I – large rounded clusters, II – intermediate clusters, III – elongated strands only one or two cells wide. (e) Plot shows the average number of cancer cell neighbours each cell within invasive strands with the morphologies exemplified in panels (a) and (b–d), respectively. ***p<0.0005, ****p<0.0001. One-way ANOVA with post-hoc multiple comparisons. Error bars indicate 95% confidence intervals, one dot represents one cell analysed.

To gain insight into the dynamics of SCC invasion, we performed time-lapse imaging of primary patient explants. Small pieces of tissue, roughly 1 mm3 in size, were embedded in a collagen-rich matrix and observed by time-lapse microscopy. Similar to the diversity observed in histological sections, this revealed a variety of behaviours, including single-cell ‘follow the leader’ migration through to large ‘dome-like’ multi-cellular invasion, even in samples from a single patient (Figure 1c). Cell tracking revealed that, in the larger invading structures, there was movement both in the direction of invasion and retrograde back to the main bulk of the explant. The diversity of collective invasion phenotype within a single tumour suggests that the type of collective invasion is not irreversibly determined by early events in the history of the tumour but can be influenced by variations in cell state that may occur later in tumorigenesis or local environmental differences.

### Generation of an agent-based model of collective cancer invasion

To explore the possible variables responsible for the different collective invasive behaviours observed, we set up both experimental and computational models. Two different experimental settings were implemented. First, an ‘organotypic’ invasion assay in which the SCC cells are cultured as a layer on top of a collagen-rich matrix and exposed to a gas-liquid interface. This recapitulates the early invasion of disease from the epidermis into the dermis (as in the top region of Figure 1a). Second, a ‘spheroid’ assay was used in which the SCC cells are encapsulated in a collagen-rich matrix, mimicking the more confined environment of disease that has already penetrated into the dermis (as in the bottom region of Figure 1a). Alongside these two experimental contexts, we developed a cellular Potts model that incorporated both SCC cells and stromal fibroblasts. The interaction of cancer cells with ECM and fibroblasts during invasion has been extensively modelled computationally in recent years (Arduino and Preziosi, 2015; Kim et al., 2015; Kumar et al., 2016; Norton et al., 2018; Pally et al., 2019; Sfakianakis et al., 2020). In our three-dimensional (3D) model, the voxel size was such that cells typically consisted of 400–800 (~83) voxels. Cell invasion could occur by a cell moving a voxel to a position that was previously occupied by matrix. To determine whether such a change might be favourable, the model included parameters that we anticipated would influence cancer cell invasion, including cancer cell–cancer cell adhesion, cancer cell–matrix adhesion, cancer cell–fibroblast adhesion, fibroblast–matrix adhesion, cell intrinsic motility, matrix displacement, and matrix proteolysis. The relative influence of these parameters on changes in the position of voxels that defined a cell between time-steps was determined along energy minimisation principles, with penalties of differing magnitudes for unfavourable changes in any single parameter (Figure 2a and Appendix 1 in Supplementary file 1).

![Figure 2.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig2-v1.jpg)

**Figure 2.:** (a) Images show the key steps and principles driving the agent-based model. At each time step, voxels are updated, and this can include growth – matrix replaced by cell, directional movement – cell voxel transposition, cell-cell adhesion – increase of voxels at the interface between cells, and extracellular matrix (ECM) remodelling or degradation – change in the ‘quantity’ of matrix in a voxel. Cancer cells are represented in green, fibroblasts in magenta, and matrix in greyscale. (b) Images show model outputs (panel columns 1, 2, 4, and 5) next to experimental data when fibroblasts are either absent or present in organotypic models (upper panels) or spheroids (lower panels). Cancer cells are green, fibroblasts are magenta. Scale bar = 100 μm. (c and d) Diverse patterns of collective invasion are shown in organotypic (c) and spheroid (d) models. Principal component analysis plot shows the metrics derived from over 2000 simulations in the presence of fibroblasts covering variation in cancer cell proteolysis, cancer cell–matrix adhesion, and cancer cell–cancer cell adhesion. The additional lines indicate how different metrics contribute to the first two components. The model runs corresponding to the exemplar images are indicated with roman numerals with three-dimensional images coloured according to mean number of squamous cell carcinoma (SCC) neighbours (blue low, red high). CAFs, cancer-associated fibroblasts.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (a) Images show model outputs next to experimental data for increasing numbers of fibroblasts. Cancer cells are green, fibroblasts are magenta. Scale bar = 100 μm. (b) Cartoon illustrates the different metrics of invasion. (c) Cartoons illustrate different types of invasive strand and the metrics that they would generate. (d) Images show model output in an organotypic assay in the absence of fibroblasts but with a single permissive track. (e) Images illustrate how the track invasion score is calculated from the simulations illustrated in panel (d). Briefly, the extent of matrix remodelling in each extracellular matrix voxel is weighted based on the vertical distance from the starting cell–matrix interface. (f) Principal component analysis plots showing the metrics derived from thousands of simulations in the absence of fibroblasts (grey-level plots) and both the presence and absence of fibroblasts (green-yellow plots) covering variation in cancer cell proteolysis, cancer cell–matrix adhesion, and cancer cell–cancer cell adhesion.

Experimental analysis using A431 SCC cells demonstrated that effective invasion required the addition of CAFs and, in both cases, the invasion was almost entirely collective (Figure 2b panels iii and vi). Careful parameterisation was performed, including analysis of the relative adhesive properties of the different cells to each other and the collagen-rich matrix used in our assays (Figure 2—figure supplement 1a and Table 1 and Appendix 2 – table 1 in Supplementary file 1). This enabled the in silico replication of the fibroblast-dependent invasion observed in both organotypic and spheroid assays (Figure 2b). In line with previous experimental reports (Gaggioli et al., 2007), the extent of increased invasion scaled with the number of fibroblasts (Figure 2—figure supplement 1a).

**Table 1.**
 Key CC3D parameter values.


<table>
  <thead>
    <tr>
      <th>CC3D parameter</th>
      <th>CC3D parameter value</th>
      <th>Real world value</th>
      <th>Comments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Monte Carlo timestep (MCS)</td>
      <td>1</td>
      <td>30 s</td>
      <td></td>
    </tr>
    <tr>
      <td>Voxel</td>
      <td>1</td>
      <td>2 microns</td>
      <td></td>
    </tr>
    <tr>
      <td>VCAF target volume</td>
      <td>800 voxels</td>
      <td>6400 microns3</td>
      <td>6500 microns3 experimental measure</td>
    </tr>
    <tr>
      <td>VCAF target surface</td>
      <td>700 voxels</td>
      <td>2800 microns2</td>
      <td>4900 microns2 experimental measure</td>
    </tr>
    <tr>
      <td>SCC initial target volume</td>
      <td>400 voxels</td>
      <td>3200 microns3</td>
      <td></td>
    </tr>
    <tr>
      <td>SCC dividing volume</td>
      <td>800 voxels</td>
      <td>6400 microns3</td>
      <td></td>
    </tr>
    <tr>
      <td>Median SCC volume in wild-type conditions</td>
      <td>550 voxels</td>
      <td>4400 microns3</td>
      <td>4500 microns3 experimental measure</td>
    </tr>
    <tr>
      <td>SCC surface area</td>
      <td>324 voxels (median)</td>
      <td>1296 microns2 (median)</td>
      <td>Sphere assumed for surface area1700 microns2 experimental measure</td>
    </tr>
    <tr>
      <td>Mean time to mitosis</td>
      <td>8640 MCS</td>
      <td>3 days</td>
      <td></td>
    </tr>
    <tr>
      <td>SCC-ECM adhesion</td>
      <td>10 (contact energy)</td>
      <td>45.53 (experimental measure)</td>
      <td>Adhesions are normalised to SCC-ECM adhesion. They are inverted and multiplied by 10 to give contact energies</td>
    </tr>
    <tr>
      <td>SCC-SCC adhesion</td>
      <td>21 (contact energy)</td>
      <td>21.8</td>
      <td></td>
    </tr>
    <tr>
      <td>SCC-CAF adhesion</td>
      <td>35</td>
      <td>25.2</td>
      <td>SCC-CAF adhesion was marginally reduced below experimental measure in model (contact energy would be 18 from experiment)</td>
    </tr>
    <tr>
      <td>CAF-CAF adhesion</td>
      <td>45</td>
      <td>9.3</td>
      <td></td>
    </tr>
    <tr>
      <td>CAF-ECM adhesion</td>
      <td>15</td>
      <td>29.6</td>
      <td></td>
    </tr>
    <tr>
      <td>SCC-ECM adhesion for zero-density ECM</td>
      <td>40</td>
      <td>11.4</td>
      <td></td>
    </tr>
    <tr>
      <td>CAF-CAF repulsion range</td>
      <td>20 voxels</td>
      <td>40 microns</td>
      <td>Approximately 1.5 CAF widths</td>
    </tr>
    <tr>
      <td>SCC taxis energy</td>
      <td>13</td>
      <td>median speed 0.2 microns/min</td>
      <td>0.2 microns/min experimental measure</td>
    </tr>
    <tr>
      <td>CAF taxis minimum energy</td>
      <td>3.5</td>
      <td>0.06 micron/min</td>
      <td></td>
    </tr>
    <tr>
      <td>CAF taxis maximum energy</td>
      <td>21</td>
      <td>0.29 microns/min</td>
      <td></td>
    </tr>
    <tr>
      <td>CAF median speed</td>
      <td>10</td>
      <td>0.1 microns/min</td>
      <td>0.1 microns/min experimental measure</td>
    </tr>
    <tr>
      <td>CAF taxis stimulation range</td>
      <td>30 voxels</td>
      <td></td>
      <td>Approximately 2.5 CAF widths</td>
    </tr>
    <tr>
      <td>CAF ECM pushing rate</td>
      <td>0.0140</td>
      <td>Corresponds to a reduced CAF speed of 0.07 microns/min through ECM</td>
      <td>Speed due to pushing is three times faster than speed due to degradation</td>
    </tr>
    <tr>
      <td>CAF ECM degradation rate</td>
      <td>0.0012</td>
      <td>Corresponds to a reduced CAF speed of 0.018 microns/min through ECM</td>
      <td>Degradation and pushing effects on speed are sub-linear. The effective median speed is between 0.07 and 0.088 microns/min</td>
    </tr>
    <tr>
      <td>SCC pushing rate</td>
      <td>0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>SCC degradation rate</td>
      <td>0.0001</td>
      <td>Corresponds to a reduced SCC speed of 0.009 microns/min through ECM</td>
      <td>Effect of degradation is half for SCCs compared to CAFs. Effects are normalised to kinesis levels</td>
    </tr>
  </tbody>
</table>

_CAF, cancer-associated fibroblast; ECM, extracellular matrix; SCC, squamous cell carcinoma; VCAF, vulval CAF._

### In silico generation of diverse collective invasion behaviours

Having established an in silico model, we then explored parameter space to investigate if different patterns of invasion could be generated by varying the combinations of input parameters. To quantitatively capture the range of invasive behaviours, a range of output metrics were collected, including total invasive extent, maximal invasion, number of cell neighbours, and cell proliferation (Figure 2—figure supplement 1b and c). The tapering metric recorded how the number of immediately neighbouring cells varied with the position of the cells in the invasive strand (cells were considered invasive if they had moved beyond the starting position of the interface between cancer cells and the matrix), whereas the strand width simply reflected the average width. A uniformly low neighbour number would indicate a long thin strand (Figure 2—figure supplement 1cI), a decreasing number of neighbours with increasing invasion would indicate a tapering strand (Figure 2—figure supplement 1cII), while a higher number of neighbours would suggest a bulkier form of collective invasion (Figure 2—figure supplement 1cIII). A critical function of fibroblasts is to generate permissive tracks for cancer cells to subsequently utilise. To mimic this without the variability generated by the somewhat stochastic behaviour of fibroblasts, we additionally ran simulations with a narrow track that could be permissive for invasion but no fibroblasts. This confirmed that cancer cells were able to exploit permissive tracks in the ECM (Figure 2—figure supplement 1d). Invasion in this context, termed track invasion score, was quantified based on the extent of matrix remodelling by invading cancer cells with weighting for the distance invaded (Figure 2—figure supplement 1e).

The outputs of the model in the presence of CAFs were analysed in two ways: using principal component analysis (PCA) and visual inspection (Figure 2c and d). PCA revealed a wide and continuous spread of invasion patterns, with the first two dimensions of the PCA accounting for 75% (organotypic) and 65% (spheroid) of the variation (Appendix 3 – table 1 in Supplementary file 1). Notably, there was no indication of discrete sub-classes of invasive pattern, suggesting a continuous spectrum of invasive behaviours. The continuous spectrum implied by PCA was in line with the range of invasive strand geometries observed in clinical muSCC samples (Figure 1). We additionally generated visual outputs of the model runs that lay at the edges of the PCA. This revealed diverse patterns of invasion, ranging from large rounded multicellular strands to single cells breaking off the main mass of tumour cells. The diversity in collective invasion observed in the presence of fibroblasts was in contrast to behaviours observed in the absence of CAFs. PCA analysis of the metrics generated from model runs without CAFs shows that the data reduces to a single dimension (Figure 2—figure supplement 1f and Appendix 3 – table 1 in Supplementary file 1), with remarkably similar behaviour in both organotypic and spheroid data. PCA combining runs with and without CAFs confirmed that fibroblasts boost invasion (Figure 2—figure supplement 1).

### Matrix proteolysis drives strand widening but not the extent of invasion

Having established that our model could generate diverse types of invasion, we undertook a more systematic analysis of parameter space to determine the contribution of specific parameters to both the extent and pattern of invasion. Figure 3a shows the PCA plots overlaid with shading for the input variable of cancer cell proteolysis, with high levels of proteolysis, trending along the vector for number of neighbours in both organotypics and spheroids. Somewhat contrary to expectation, we found that increasing cancer cell proteolysis led to only modestly elevated invasion scores in organotypic contexts. Moreover, the maximum invasive depth did not correlate with matrix proteolysis (Figure 3b). Instead the width of the strands (neighbour numbers) increased as a function of proteolysis, especially in organotypic assays. In simulations with low proteolysis, the model predicted thin strands (low neighbour and low tapering scores). To measure the effect of proteolysis on the shape of the invading front of cell clusters, we ran simulations initiated with a cluster of cells and a uniform directional cue, either without the complicating factor of pre-existing tracks or a simple single permissive track. Figure 3—figure supplement 1c shows that increasing proteolysis leads to reduced curvature and a ‘pushing’ front in the absence of a track. When a track was present, it was favoured for invasion and interfered with the generation of a pushing front most strikingly at intermediate levels of proteolysis. Inspired by previous studies (Ahmadzadeh et al., 2017; Park et al., 2020; Provenzano et al., 2006), we additionally considered the cases if the ECM had multiple tracks either oriented parallel to the direction of invasion – analogous to aligned matrix fibres – or had isotropic texture distributed as a chessboard – analogous to non-aligned matrix fibres. As might be expected, ECM fibres parallel to the direction of the invasive cue favoured invasion, but isotropic texture hindered invasion (Figure 3—figure supplement 1d).

![Figure 3.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig3-v1.jpg)

**Figure 3.:** (a) Principal component analysis plots show the metrics derived from over 2000 simulations in the presence of fibroblasts covering variation in cancer cell proteolysis with values indicated by the intensity of cyan, cancer cell–matrix adhesion (not colour coded), and cancer cell–cancer cell adhesion (not colour coded). (b) Heatmaps show how varying the cancer cell proteolysis value (x axis) impacts on different metrics when fibroblasts are included in all simulations. WT indicates the ‘wild-type’ value based on experimental parameterisation using A431 cancer cells. Yellow indicates a high value, dark blue a low value. (c) Images show the effect of modulating matrix proteolysis via either MMP14 Crispr KO or MMP14 over-expression in cancer cells (green) both organotypic and spheroid assays including fibroblasts (magenta). Scale bar = 100 μm. (d) Quantification of three biological replicates of the experiment shown in panel (c) with strand length, strand width, and tapering shown – 1 unit is equivalent to 0.52 μm. Error bars indicate 95% confidence intervals, one dot represents one strand. ECM, extracellular matrix.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (a) Heatmaps show how varying the cancer cell proteolysis value (x axis) impacts on different metrics in the absence of fibroblasts. WT indicates the ‘wild-type’ value based on experimental parameterisation using A431 cancer cells. (b) Heatmaps show the differential values resulting from the inclusion of fibroblasts (effectively a comparison of Figure 3b and Figure 3—figure supplement 1a). Red indicates an increase when fibroblasts are present, dark blue a reduction when in the presence of fibroblasts. (c) Images show simulation output initiated with a spheroid, no fibroblasts, a uniform chemotactic cue, and varying cancer cell proteolysis. Left panel – day 7output in the absence of permissive track, right panel – day 5 output in the presence of permissive track. (d) Heatmaps show how varying the distribution of extracellular matrix (ECM) density in organotypic simulations impacts on different metrics when fibroblasts are included in all simulations. Parametrisation and colourmap as in (a). ‘Aligned’ refers to alternating tracks of high and low ECM density parallel to direction of invasion. ‘Chessboard’ refers to three-dimensional (3D) chessboard distribution of high and low ECM density values. (e) Heatmaps show how varying the cancer cell proteolysis value (x axis) impacts on different metrics when cancer-cell proliferation rate is halved, and fibroblasts are included in all simulations. Parametrisation and colourmap as in (a). (f) Western blots of MMP14, alpha-catenin, vimentin, fibronectin, and β-actin in A431 cells engineered using Crispr/Cas9 to delete MMP14 or CTNNA1, or to over-express MMP14. (g) Images show F-actin (magenta) and degraded collagen I represented by fluorescence of DQ collagen I (green) in 3D culture of A431 cells genetically engineered as indicated. (h) Plot shows the quantification of strand width in spheroid invasion assay of A431 WT or MMP14 over-expressing cells, which are pre-treated with mitomycin C. Unpaired t-test was performed. Error bars indicate 95% confidence intervals, one dot represents one strand. For comparison, light blue lines show the same metrics in the absence of mitomycin C (data from Figure 3d).

Analysis of spheroid contexts yielded a different picture, with reduced maximum invasion depth with increasing proteolysis values. Notably, the very highest matrix degradation value yielded significantly lower maximum invasion depth than the intermediate and lowest level. There was less difference in the overall invasion score as increasing proteolysis was linked to slightly wider strands, which counter-balanced the reduction in maximum invasion depth (Figure 3a and b). Both organotypic assays and spheroids without CAFs exhibited low levels of invasion (Figure 3—figure supplement 1a and b). Comparative plots of the metrics in simulations with and without CAFs confirm this (note the red colour) and indicate that fibroblasts favour narrower strands (note the blue colour in the neighbour and tapering rows). Overall, cancer cell proteolysis is primarily predicted to regulate strand width in both organotypic and spheroid contexts. The relationship between matrix proteolysis and strand width was maintained even if cancer cell proliferation was reduced (Figure 3—figure supplement 1e), although the cell neighbour values were lower when proliferation was halved.

We tested the predictions that cancer cell matrix protease function was linked to width of invasion strands by generating A431 cancer cells that either over-expressed MMP14, the major collagen protease, or had it deleted via Crispr/Cas9 editing methods (Figure 3—figure supplement 1f). In line with expectation, MMP14 over-expression increased the proteolysis of collagen, while MMP14 deletion reduced proteolysis (as assessed by DQ collagen fluorescence) (Figure 3—figure supplement 1g). Figure 3c and d shows that experimentation confirmed the major predictions of our model. In particular, the maximum invasion depth in the organotypic context did not simply increase with MMP14 levels, with strand lengths similar between MMP14 KO and over-expressing cells. In contrast, the strand width was notably affected by MMP14 levels in both organotypic and spheroid assays (yellow lines in Figure 3c indicate strand width), with KO cells generating thin strands and over-expressing cells generating thick strands. The positive relationship between ECM proteolysis and strand width was particularly strong in organotypic contexts (Figure 3c and d). Of note, matrix proteolysis promoted wide strands even if cancer cell proliferation was prevented by pre-treatment with mitomycin C (Figure 3—figure supplement 1h). These results are highly concordant with the model predictions and confirm that MMP14 is a major determinant of the mode of collective cancer cell invasion but plays little role in determining the maximum distance invaded.

### Cancer cell-cell adhesion promotes wide invasive strands

We turned our attention to investigate how cancer cell adhesion to either other cancer cells or the matrix influenced the mode of collective invasion. Figure 4a shows PCA plots of invasion characteristics with the strength of cancer cell–matrix adhesion overlaid in green shading. There was no consistent association between cancer cell-matrix adhesion and invasive pattern in the organotypic context, with high adhesion values distributed across the PCA plot. The relationship between cell-matrix adhesion and invasion score was relatively flat, with only very high cell-matrix adhesion values boosting invasion. This prediction is supported by the lack of effect of ITGB1 deletion on cancer invasion in the experimental organotypic model (Figure 4c and d – Figure 4—figure supplement 1b and c confirm that ITGB1 KO cells are defective in collagen I and Matrigel adhesion). In the spheroid context, there was a somewhat stronger association between matrix adhesion and invasion. Minimal invasion was observed in the absence of fibroblasts (Figure 4—figure supplement 1a). Intriguingly, the strongest correlation was with the tapering metric that reflects whether strands have a uniform breadth or taper as they invade deeper (Figure 4b – row 4). Experiments using ITGB1 KO A431 cells provided support for this prediction. To rule out a compensatory role for ITGB3 in ITGB1 KO cells, we combined targeting of both ITGB1 and ITGB3. Figure 4—figure supplement 1d–f shows that these cells were still able to invade. Greater tapering observed in ITGB1 KO spheroids (Figure 4c and d). Interestingly, and in line with model predictions, this was not observed in organotypic assays (Figure 4b–d).

![Figure 4.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig4-v1.jpg)

**Figure 4.:** (a) Principal component analysis plots show the metrics derived from over 2000 simulations in the presence of fibroblasts covering variation in cancer cell–matrix adhesion with values indicated by the intensity of green, cancer cell proteolysis (not colour coded), and cancer cell–cancer cell adhesion (not colour coded). (b) Heatmaps show how varying the cancer cell–matrix adhesion value (x axis) impacts on different metrics when fibroblasts are included in all simulations. WT indicates the ‘wild-type’ value based on experimental parameterisation using A431 cancer cells. Yellow indicates a high value, dark blue a low value. (c) Images show the effect of modulating matrix adhesion via Crispr KO of ITGB1 in cancer cells (green) in both organotypic and spheroid assays including fibroblasts (magenta). Scale bar = 100 μm. (d) Quantification of three biological replicates of the experiment shown in panel (c) with strand length, strand width, and tapering metric shown – 1 unit is equivalent to 0.52 μm. Unpaired t-test was performed. 95% confidence intervals are shown, one dot represents one strand.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (a) Heatmaps show how varying the cancer cell–matrix adhesion value (x axis) impacts on different metrics in the absence of fibroblasts. WT indicates the ‘wild-type’ value based on experimental parameterisation using A431 cancer cells. (b) Western blots of integrin β1 and β-actin in A431 cells engineered using Crispr/Cas9 to delete integrin β1. (c) Images show adhesion of A431 WT cells or ITGB1 KO cells to extracellular matrices. The number of cells attached to matrices is quantified in the plot. Unpaired t-test was performed. Error bars indicate 95% confidence intervals, one dot represents one field of view with 3 fields quantified from 3 experiments. (d) Western blots of integrin β3, integrin β1, and β-actin in A431 cells engineered using Crispr/Cas9 to delete integrin β1 or to deplete integrin β3 by transfecting ITGB3 siRNA. (e) Images show DNA (cyan), integrin β3 (green), and F-actin (magenta) in A431 WT, ITGB1 KO, or ITGB1 KO/ ITGB1 KD cells. (f) Images show Invasion of A431 WT, ITGB1 KO, or ITGB1 KO/ ITGB3 KD cells in organotypic (left panel) or spheroid (right panel) invasion assay.

Next, we explored the relationship between cancer cell–cancer cell adhesion and invasion when fibroblasts were present (Figure 5a). These analyses yielded several predictions that caught our attention. First, reducing cancer cell–cancer cell adhesion reduced the total invasion score in organotypic assays across relatively large ranges of parameter space (Figure 5a and b – note the association of increasing magenta intensity and invasion score vectors in the PCA plot). This is counter to the widely held view that EMT and increased single cell characteristics promote invasion. Specifically, in organotypic contexts, lower cancer cell–cancer cell adhesion resulted in shorter invasive strands that thinned rapidly as they invaded (this is reflected in the Max. Invasion, Mean Neighbour, and Tapering rows in Figure 5b). Once again, little invasion was observed in the absence of fibroblasts (Figure 5—figure supplement 1a). Figure 5—figure supplement 1c explicitly plots the change in strand width as a function of depth for varying cancer cell–cancer cell adhesion. The simpler context of cell invasion into a thin permissive gap further supported the prediction that cancer cell–cancer cell adhesion is linked to wider invading strands (Figure 5—figure supplement 1d). The situation in spheroid assays was more subtle, with increases in invasion only predicted at very high values ≥2 WT (Figure 5b). Of note, the Neighbour and Tapering metrics did not vary much depending on cancer cell–cancer cell adhesion. To test these predictions, we generated A431 cells defective in cell–cell adhesion as a result of Crispr-mediated deletion of α-catenin/CTNNA1 (Figure 3—figure supplement 1f). Strikingly, and, in line with the model predictions, these cells lacking adherens junctions were significantly less invasive, both in terms of strand length and strand width, in organotypic assays (Figure 5d). In spheroid assays, loss of α-catenin did not affect strand length and had only a modest effect on strand width (~20% reduction compared to a 60% reduction in width in organotypic assays).

![Figure 5.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig5-v1.jpg)

**Figure 5.:** (a) Principal component analysis plots show the metrics derived from over 2000 simulations in the presence of fibroblasts covering variation in cancer cell–cancer cell adhesion with values indicated by the intensity of magenta, cancer cell proteolysis (not colour coded), and cancer cell–matrix adhesion (not colour coded). (b) Heatmaps show how varying the cancer cell–cancer cell adhesion value (x axis) impacts on different metrics when fibroblasts are included in all simulations. WT indicates the ‘wild-type’ value based on experimental parameterisation using A431 cancer cells. Yellow indicates a high value, dark blue a low value. (c) Images show the effect of modulating cancer cell-cell adhesion via Crispr KO of CTNNA1 in cancer cells (green) in both organotypic and spheroid assays including fibroblasts (magenta). Scale bar = 100 μm. (d) Quantification of three biological replicates of the experiment shown in panel (c) with strand length, strand width, and tapering shown – 1 unit is equivalent to 0.52 μm. Unpaired t-test was performed. Error bars indicate 95% confidence intervals, one dot represents one strand. (e) Plots show the track invasion score with varying cancer cell–cancer cell adhesion in simulations lacking fibroblasts but with a single permissive track favouring invasion. Cartoons indicate the initial set up of cell positions and the directional cue in the simulation.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (a) Heatmaps show how varying the cancer cell–cancer cell adhesion value (x axis) impacts on different metrics in the absence of fibroblasts. WT indicates the ‘wild-type’ value based on experimental parameterisation using A431 cancer cells. (b) Images show the β-catenin (magenta), fibronectin (FN; blue), and integrin β1 (green) staining in human squamous cell carcinoma tissue. ‘t’ indicates tumour clusters, scale bar is 50 microns. (c) Plots show how the mean number of neighbours of cancer cells varies as a function of invasion depth in simulations with varying cancer cell–cancer cell adhesion (c.f. Figure 2—figure supplement 1b). (d) Plots show how the strand width varies depending on cancer cell–cancer cell adhesion in permissive track simulations, one dot represents one simulation. (e) Heatmaps show how varying the proteolysis (left panel) or cancer cell–cancer cell adhesion (right panel) values (x axis) impacts on different metrics in organotypic simulations when fibroblasts are mixed in with the cancer cells rather than extracellular matrix. Parametrisation and colourmaps as in Figure 5 and part (a).

### The pro-invasive role of cell-cell junctions depends on a uniform directional cue and supra-cellular coordination of the actomyosin cytoskeleton

The data described above establish an intriguing context-dependent role for cell-cell junctions in collective invasion – with a positive relationship between cell-cell adhesion and invasion in organotypic contexts but not in spheroid contexts. To rule out that the location of CAFs drive invasive pattern, we mixed CAFs with SCCs in organotypic simulations (Figure 5—figure supplement 1e). The results were highly consistent with the results of CAFs mixed in with ECM, with only minor differences in the number of fractured objections and tapering. These analyses rule out CAF location as a dominant driver of invasive pattern. One key difference between these two contexts is that cancer cells in the organotypic context are subject to a uniform gradient of chemotactic cues, whereas in the spheroid context, the cancer cells are subject to a radial chemotactic cue. We used our model to test if switching to a uniform chemotactic gradient in the spheroid context would generate a positive relationship between cell-cell adhesion and invasion. Figure 5e quantifies track invasion score in simulations of spheroids with either uniform or radial chemotactic cues. These analyses indicate that cancer cell junctions are favourable for invasion when cells are subject to a uniform directional cue. The importance of junctions only when there is a uniform directional cue suggests that it may not be cell-cell adhesion per se that is important but some linkage between cell-cell adhesions and coordination of collective invasion. Consistent with this idea, cadherin-mediated coordination of actin and myosin dynamics is important for effective collective migration of neural crest cells during cranio-facial development and for border cell migration in the Drosophila egg chamber (Geisbrecht and Montell, 2002; Shellard et al., 2018). We hypothesised that a similar mechanism might also underlie the context-dependent importance of adherens junctions in cancer cell invasion.

Previous work revealed that collectively invading cancer cells have a supra-cellular actomyosin network that enables the coordinated migration of cell groups. Figure 6a confirms control A431 cells exhibit supra-cellular organisation of their actomyosin network (Hidalgo-Carcedo et al., 2011). Furthermore, knockout of CTNNA1 disrupts the formation of a supra-cellular actomyosin network (Figure 6a – quantification shown in Figure 6—figure supplement 1a). As expected, CTNNB1 failed to localise to cell-cell contacts in CTNNA1 KO A431 cells (Figure 6a). To experimentally disrupt the supra-cellular actomyosin network while retaining cell-cell junctions, we utilised two experimental tools, ROCK:ER (a fusion of the ROCK2 kinase domain to the regulatory domain of the oestrogen receptor) and ROCK kinase inhibition. In the presence of 4OHT, ROCK:ER boosts actomyosin contractility throughout the cytoplasm including at cell-cell interfaces (Croft et al., 2004), and the latter reduces the activity of the supra-cellular actomyosin belt. Figure 6b and c shows that these manipulations have the desired effect on active actomyosin, as determined by pS19-MLC staining (Figure 6—figure supplement 1b and c confirms these observations with staining for MYH9). We next tested the effect of these perturbations on A431 MMP14 over-expressing cells that generate wide invasive strands. Figure 6d and e shows that both manipulations reduce the width of invading strands, demonstrating that disrupting actomyosin coordination mechanisms phenocopy loss of adherens junctions with respect to the width of invading strands (note: for this experiment we used ECM pre-conditioned by fibroblasts in the absence of drug and then added cancer cells in the presence of the indicated perturbations). Furthermore, the data support a model in which adherens junctions influence invasive pattern by enabling supra-cellular coordination of actomyosin, and not simply determining whether cancer cells are able to maintain contact with one another. Consistent with this view, we observed supra-cellular organisation of actomyosin and the retention of adherens in all but the thinnest invading strands in human SCC.

![Figure 6.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig6-v1.jpg)

**Figure 6.:** (a) Images show the β-catenin (magenta), F-actin (orange), DNA (blue), and active myosin (pS19-MLC - green) networks in control A431 and CTNNA1 KO A431 cells.( b) Images β-catenin (magenta), F-actin (orange), DNA (blue), and active myosin (pS19-MLC - green) networks in control A431- and 10-μM Y27632-treated cells. Scale bar = 20 μm. (c) Images show β-catenin (magenta), F-actin (orange), DNA (blue), and active myosin (pS19-MLC - green) networks in control A431 ROCK:ER- and 4-OHT-treated cells. Scale bar = 20 μm. (d) Images show organotypic killing assays using control or MMP14 over-expressing A431 cells in the presence or absence of 10 μM Y27632. Scale bar = 100 μm. Plot shows the quantification of strand width from three biological replicates – 1 unit is equivalent to 0.52 μm. One-way ANOVA with post-hoc multiple comparisons was performed. Error bars indicate 95% confidence intervals, one dot represents one strand. (e) Images show organotypic invasion assays using MMP14 over-expressing A431 cells additionally engineered to contain ROCK:ER in the presence or absence of 4-OHT. Scale bar = 100 μm. Plot shows the quantification of strand width from three biological replicates. Unpaired t-test was performed. Error bars indicate 95% confidence intervals, one dot represents one strand.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (a) Plots show the quantifications of relative intensity of pMLC in A431 WT, CTNNA1 KO, A431 WT cells treated with Y27632 and ROCK:ER expressing A431 ± 4(O)HT at the edge or cell-cell junction of the cells. Mean, quartiles, and extremes are shown, data from 3 independent experiments. (b) Images show the F-actin (magenta) and myosin (MYH9/MHCIIa - green) networks in control A431- and 10-μM Y27632-treated cells. Scale bar = 20 μm. (c) Images show the F-actin (magenta) and myosin (MYH9/MHCIIa - green) networks in control A431 ROCK:ER with/without 4-OHT treatment. Scale bar = 20 μm. (d) Images show the F-actin (magenta), DNA (DAPI; blue), and MYH9/MHCIIA (green) staining in human squamous cell carcinoma tissue. ‘t’ indicates tumour clusters, arrows point to supra-cellular actomyosin network, scale bar is 50 microns.

### Protease-driven strand widening requires cell-cell junctions

The analyses above investigate the relationship between individual cancer cell parameters and invasion; we additionally explored how combinations of parameter variations influenced invasive pattern and extent. The data described above argue that, by virtue of their role in coordinating supra-cellular actomyosin, cell-cell junctions would be required for high levels of proteolysis to generate wide invasive tracks. We, therefore, explored the interplay between cancer cell–cancer cell adhesion and proteolysis in determining SCC invasion using both modelling and experimental strategies. Potts modelling predicted that the high neighbour number observed when matrix proteolysis is high would depend upon cell-cell junctions in organotypic assays (note the higher values in the top right regions on the plots in Figure 7ai). Interestingly, this cooperative interaction between proteolysis and cell-cell adhesion was not predicted to influence the extent of maximum invasion, which was dominated by cell-cell adhesion alone (Figure 7aii). These predictions were supported by experimentation: deletion of CTTNA1 prevented the formation of wide invasive strands by MMP14 over-expressing A431 cells in the organotypic invasion assays (Figure 7c), with more subtle effects observed in the spheroid assays (Figure 7a, d, and e). Figure 3—figure supplement 1a and b indicates that CAFs favour narrower invasive strands; therefore, to more fully explore how ECM proteolysis and cell-cell adhesion co-ordinately determine the geometry of collective invasion, we revisited simulations, without CAFs, designed to monitor the curvature of the invading cell cluster (Figure 3—figure supplement 1d). Figure 7—figure supplement 1a and b shows that if both ECM proteolysis and cell-cell adhesion are high then a broad, virtually flat, invasive front is generated. Reducing either proteolysis or cell-cell adhesion leads to increased curvature. Together, these analyses establish that a broad ‘pushing’ front of invasion requires both high proteolysis and high cancer cell–cancer cell adhesion.

![Figure 7.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig7-v1.jpg)

**Figure 7.:** (a) Heatmaps show how varying the matrix proteolysis (x-axis) and cancer cell–cancer cell adhesion value (y axis) impacts on different metrics when fibroblasts are included in all simulations. WT indicates the ‘wild-type’ value based on experimental parameterisation using A431 cancer cells. Yellow indicates a high value, dark blue a low value. (b) Images show the effect of combinatorial modulation of matrix proteolysis and cancer cell-cell adhesion via Crispr KO of CTNNA1 and/or MMP14 and/or MMP14 over-expression in cancer cells (green) in both organotypic assays including fibroblasts (magenta). Scale bar = 100 μm. (c) Quantification of three biological replicates of the experiment shown in panel (b) with strand length and strand width shown – 1 unit is equivalent to 0.52 μm. One-way ANOVA with post-hoc multiple comparisons was performed. Error bars indicate 95% confidence interval, one dot represents one strand. (d) Images show the effect of combinatorial modulation of matrix proteolysis and cancer cell-cell adhesion via Crispr KO of CTNNA1 and/or MMP14 and/or MMP14 over-expression in cancer cells (green) in both spheroid assays including fibroblasts (magenta). (e) Quantification of three biological replicates of the experiment shown in panel (d) with strand length and strand width shown. Scale bar = 100 μm. One-way ANOVA with post-hoc multiple comparisons was performed. Error bars indicate 95% confidence interval, one dot represents one strand.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** (a) Images show simulations initiated with a spheroid, no fibroblasts, and a uniform downward chemotactic cue. Matrix proteolysis and cancer cell–cancer cell adhesion are varied. (b) Heatmaps show how varying the cancer cell–cancer cell adhesion value (x axis) and matrix proteolysis (y-axis) impacts on the curvature of the front of the invading cluster.

### Strand widening is coupled to cancer cell growth

While the focus of our analysis has been the pattern of invasion, the widening of tracks might also represent a mechanism for generating additional space for cell growth in confined environments. As proliferation is a feature of our model, we additionally investigated whether cancer cell growth might be impacted as a result of change in cancer cell–cancer cell adhesion and proteolysis. Interestingly, the vectors reflecting cell growth and neighbour number in the PCA analysis were closely aligned (Figure 2c and d). EdU staining revealed that proliferating cells were observed throughout spheroids (Figure 8—figure supplement 1a and b). Moreover, there was a positive association between the proportion of EdU positive cells in invading strands and the strand width. The modelling indicated that the linkage between strand widening and growth was particularly pronounced in the spheroid simulations lacking fibroblasts (Figure 2—figure supplement 1f). Given that we have established matrix proteolysis and cancer cell–cancer cell adhesion as the major determinants of neighbour number and strand width, we therefore investigated the relationship between these parameters and cell growth. Neither was predicted to have a strong effect on cell growth in organotypic assays, either in the presence or absence of CAFs (Figure 8a). In contrast, a strong positive relationship between proteolysis and growth was predicted in the context of spheroids lacking CAFs (Figure 8a). Cancer cell–cancer cell adhesions were also predicted to make a positive contribution to growth, albeit smaller than the effect of proteolysis (Figure 8a). We proceeded to test these predictions experimentally. Manipulation of MMP14 and CTTNA1 had minimal effect on cell growth in unconfined two-dimensional (2D) culture conditions (Figure 8—figure supplement 1c). Figure 8b and c confirms that both proteolysis and cancer cell–cancer cell adhesion are required for effective cell growth in 3D collagen matrices. Moreover, the positive effect of boosting proteolysis required cell-cell adhesions (Figure 8b and c compares MMP14 OE with αCATKO MMP14 OE). Ectopic activation of ROCK2, which disrupts cytoskeletal cohesion in cell clusters, also reduced growth in 3D collagen (Figure 8—figure supplement 1d and e). Together, these data suggested that the supra-cellular actomyosin network, invasive strand width, and cancer cell growth might be linked.

![Figure 8.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig8-v1.jpg)

**Figure 8.:** (a) Heatmaps show how varying the matrix proteolysis (left) or cancer cell–cancer cell adhesion value (right) impacts on predicted cell growth in the presence or absence of fibroblasts. WT indicates the ‘wild-type’ value based on experimental parameterisation using A431 cancer cells. Yellow indicates a high value, dark blue a low value. (b) Phase contrast images show the growth of cancer cell colonies with the indicated manipulations of MMP14 and CTNNA1 after 8 days surrounded by matrix. Scale bar = 50 μm. (c) Plot shows quantification of the growth assay shown in (b). Two-way ANOVA with post-hoc multiple comparisons was performed. Error bars indicate 95% confidence intervals. Data from three biological replicates. (d) Fluorescent image shows reflectance of collagen fibre (cyan) and cell membrane of A431 WT cells in three-dimensional (3D) culture. (e) Fluorescent image shows reflectance of collagen fibres around A431 WT cells in 3D culture at two time points. t=0 min: magenta, t=100 min: green. (f) Fluorescent images show reflectance of collagen fibres (cyan) and cell membrane of A431 WT, CRNNA1 KO, or MMP14 over expressing cells (red) in 3D culture. White arrows highlight the formation and motion of collagen bundles adjacent to the cell clusters, yellow arrows highlight gaps.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig8-figsupp1-v1.jpg)

**Figure 8—figure supplement 1.:** (a) Images show EdU-labeled proliferating cells (green) and DNA (blue) in spheroid invasion assay with A431 WT, MMP14 KO, MMP14 OE, or CTNNA1 KO (magenta). (b) Plot shows the quantification of EdU-labeled cells shown in (a). One-way ANOVA with post-hoc multiple comparisons was performed. Error bars indicate 95% confidence intervals, n=3 biological replicates. (c) Plot shows quantification of growth of A431 cells with the indicated manipulations of MMP14 and CTNNA1 in two-dimensional cell culture. Two-way ANOVA with post-hoc multiple comparisons was performed. Error bars indicate 95% confidence intervals, n=3 biological replicates. (b) Phase contrast images show the growth of A431 ROCK:ER cancer cell colonies in the presence or absence of 4-OHT. Scale bar = 50 μm. (c) Plot shows quantification of the growth assay shown in (b). Data from three biological replicates. Two-way ANOVA with post-hoc multiple comparisons was performed. Error bars indicate 95% confidence intervals, n=3 biological replicates.

The linkage between strand widening and growth might be due to the ability of cells to generate space when surrounded by ECM. This could be the result of proteolysis, which would explain the effect of MMP14 manipulation, but it is less clear why this might require adherens junctions. We hypothesised that cell-cell junctions and the supra-cellular coordination of the actomyosin network might enable cancer cells to physically remodel the ECM (Figure 8d–f). Similar to previous work with single cells Wyckoff et al., 2006, we observed that clusters of control cancer cells displaced the ECM. This was observed directly in time-lapse movies and as the formation and compaction of ECM fibres at the cancer cell-ECM interface (note arrows in Figure 8e and f). These analyses also revealed highly dynamic membrane blebs and filopodia at the cancer cell-ECM interface. ECM compaction was absent when CTNNA1 KO cells were used. MMP over-expression reduced ECM compaction and led to the formation of gaps in the ECM adjacent to the cancer cells with reduced numbers of membrane blebs (Figure 8f). These analyses provide a direct demonstration of the ‘pushing’ term used in the computational modelling and are consistent with a role for the supra-cellular actomyosin cable in generating the pushing force.

### Protease-driven tumour growth and lymph node metastasis require cell-cell junctions

Finally, we sought to test whether key findings of our integrated in silico and in vitro analysis also applied in an in vivo context with a heterogeneous environment including a greater diversity of stromal cell types not included in our model. A431 cells engineered to have different levels of MMP14 and CTTNA levels were injected into the dermal space within the ears of mice. This anatomical location was chosen because the dermis represents the first tissue that SCC invades into, and cells can spread from the dermis to local lymph nodes, which reflects the clinical spread of the disease. This environment is spatially confined with some fibroblasts in addition to thin layers of fat, cartilage, and muscle. It was not possible to include all these additional factors with appropriately controlled parameterisation. Therefore, we concentrated on validating the relationship between matrix proteolysis, cancer cell-cell adhesion, and invasive spread in vivo. In addition, if stromal support, such as that provided by fibroblasts, is limited then the mechanisms that promote wide invasive strands also favour growth. To test these ideas, we injected A431 cells with combinations of MMP14 and α-catenin manipulations into the intradermal space of mouse ears. This environment is spatially restrictive with lymphatic drainage to local lymph nodes. Of note, MMP over-expressing cells generated tumours with particularly wide, bulging, margins (Figure 9a). Strikingly, there was a strong correlation between the levels of MMP14 and tumour growth (Figure 9b). Histological analysis revealed clusters of SCC cells in the ear distant from the main tumour. In MMP14 over-expressing tumours, these clusters were larger, rounder (as judged by aspect ratio), and further from the tumour (Figure 9—figure supplement 1a and b). Metastatic spread to lymph nodes also correlated with MMP14 levels, which are in line with previous reports (Bartolomé et al., 2009; Devy et al., 2009; Wang et al., 2021). Notably, and in contrast to the prevailing dogma, reducing cancer cell–cancer cell adhesion did not lead to a more aggressive tumour phenotype but reduced both tumour growth, and very few mice were observed to have lymph node metastases (Figure 9c). This could be partly compensated by over-expression of MMP14, suggesting that a defect in ‘space’ generation might underpin the defect in the CTNNA1 KO cells. However, the growth and lymph node metastasis of MMP14 o.e./CTNNA1 KO cells were reduced compared to the MMP14 o.e. cells (Figure 9c), indicating that the tumour promoting effect of elevated MMP14 levels depends on cell-cell adhesion. Together, these analyses demonstrate that MMP14-driven matrix proteolysis promotes invasion in wide collective units and tumour growth in spatially confined contexts. Furthermore, the widening of invasive units, tumour growth, and lymph node metastases depends upon adherens junction-mediated supra-cellular coordination of the actomyosin network.

![Figure 9.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig9-v1.jpg)

**Figure 9.:** (a) H&E images are shown on tumours growing in the ears of mice with the indicated manipulations of MMP14 and CTNNA1. Scale bar = 50 μm. (b) Plot shows quantification of A431 tumour growth with the indicated manipulations of MMP14 and CTNNA1. (c) Table shows quantification of mice with primary tumours and mice with lymph node metastases when injected with A431 cells with the indicated manipulations of MMP14 and CTNNA1. The total number of mice for each condition also applies to the data plotted in (b). Two-way ANOVA with post-hoc multiple comparisons was performed. Error bars indicate 95% confidence intervals.

![Figure 9—figure supplement 1.](https://cdn.elifesciences.org/articles/76520/elife-76520-fig9-figsupp1-v1.jpg)

**Figure 9—figure supplement 1.:** (a) Images show collective invasion from wild type and MMP14OE A431 tumours grown in the ear. Black arrows indicate invading cell clusters. (b) Left plot shows the ‘invasion score’ (product of the distance of the cluster and cluster area) vs the aspect ratio of the cluster, and right plot shows the invasion distance vs the aspect ratio. Each dot represents one invading cluster. (c) Table relating patterns of collective invasion to cancer cell properties and the presence or absence of fibroblasts.

## Discussion

The combined computational and experimental analysis of collective cancer cell invasion presented here raises several findings that warrant further consideration. Although, matrix proteolysis was broadly associated with higher levels of invasion (Castro-Castro et al., 2016; Egeblad and Werb, 2002), it was not a simple linear relationship (Figure 8—figure supplement 1d). Most notably, high proteolysis reduces the maximal extent of invasion but increases the strand width in both the model and experiments. The ability of cells with high levels of proteolysis to generate space means that there is less pressure to constrict cells into longer thinner strands. The importance of space limitation for effective invasion is underscored by the reduced invasion observed when spheroids have a ‘choice’ between invasion and spreading over an unimpeded matrix layer. High proteolysis essentially reduces the space limitation. This is also linked with high levels of proliferative capacity in 3D environments. Our analysis demonstrated that this growth effect was clearly observed in vivo. MMP14 over-expressing tumours grew and metastasised aggressively. This argues that SCC cells invading in thick strands are efficient at metastasis. Crucially, the aggressive behaviour of MMP14 over-expressing cells is reduced by depletion of α-catenin. This argues strongly against a single cell form of migration being optimal for lymph node metastasis of SCC cells. The importance of adherens junctions for efficient metastasis is increasingly appreciated, this work suggests that one advantage of both adherens junctions and matrix proteases in collective migration is that the cells remain in a state capable of generating the space required for growth.

In silico analysis revealed that reducing cancer cell-ECM adhesion had a minor effect on determining the mode of invasion. Experimentation using ITGB1 knock-out cells supported this analysis and notably confirmed the relationship between strand tapering and cancer cell-ECM adhesion. Moreover, unless cancer cell-ECM adhesion was very strong, the relationship between this variable and extent of invasion was rather weak in both organotypic and spheroid assays. Broadly, these data are consistent with the integrin independence of amoeboid forms of migration in 3D and hint at a role for either adhesion forces mediated by the glycocalyx or a role for outward forces that enable a ‘chimneying’ type of migration. In the future, it will be interesting to explore feedback loops between ECM properties, including density and stiffness, cell-matrix adhesion, cell behaviour, and low-affinity ECM adhesion mechanisms. A more sophisticated framework covering cell-ECM adhesion might also enable explanation of the experimental observation of thinner strands when ITGB1 is deleted (Figure 4). Cancer cell-cell adhesions exert a greater influence on collective cancer invasion than cell-ECM adhesions (Figure 8—figure supplement 1d). Intriguingly, the positive role of cancer cell-cell adhesions was most pronounced in simulations with a uniform chemotactic gradient. We propose that this reflects a crucial role of cell-cell adhesions in coordinating a supra-cellular actomyosin cytoskeleton in collectively invading clusters. This is likely to involve coordination of cell polarity complexes at sites of cell-cell contact. Interestingly, loss of cell-cell junctions was not sufficient to promote a clear switch to single cell invasion. This is likely due to the lack of available space in 3D contexts. This observation is consistent with CDH1-deficient tumours, such as invasive lobular carcinoma of the breast and some gastric cancers, typically showing thin strand-like patterns of invasion. Intriguingly, we observed transitions to single cell behaviour upon combined manipulation of CTNNA1 and MMP14 – either over-expression or knockout. The reasons for this are not immediately apparent, but the MMP14 knockout phenotype and the increase in single cell migration when ITGB1 and ITGB3 are depleted are consistent with protease- and adhesion-independent amoeboid cell migration (Friedl and Wolf, 2010; Lämmermann et al., 2008; Tozluoğlu et al., 2013; Wolf et al., 2003). Our modelling framework is not set up to consider amoeboid migration; hence, the transitions to single cell migration are not efficiently predicted. In future work, it will be interesting to integrate modelling frameworks for collective and amoeboid forms of migration.

To conclude, our integrated in silico and experimental approach reveals some of the key determinants of the mode of collective cancer invasion. Broad pushing fronts are associated with high matrix proteolysis and strong cancer cell-cell junctions and a lower dependence on CAFs. Reducing either proteolysis or cancer cell-cell adhesions leads to thinner invasive strands, with cell-matrix adhesions tuning strand tapering. We observe and experimentally demonstrate an unexpected linkage between the mechanisms that promote the widening of invasive strands and ability of cancer cells to grow when surrounded by ECM.

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
      <td>Antibody</td>
      <td>Anti-MMP14 (rabbit monoclonal)</td>
      <td>Abcam</td>
      <td>ab51074</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-alpha-catenin (rabbit monoclonal)</td>
      <td>Abcam</td>
      <td>ab51032</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-vimentin (mouse monoclonal)</td>
      <td>Sigma</td>
      <td>SAB4200761</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-fibronectin (rabbit polyclonal)</td>
      <td>Sigma</td>
      <td>F3648</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-integrin β1 (mouse monoclonal)</td>
      <td>Abcam</td>
      <td>ab24693</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-integrin β3 (rabbit monoclonal)</td>
      <td>Abcam</td>
      <td>ab179473</td>
      <td>WB (1:1000)IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-actin (mouse monoclonal)</td>
      <td>Sigma</td>
      <td>A4700</td>
      <td>WB (1:2000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-pS19-MLC (rabbit polyclonal)</td>
      <td>Cell Signaling</td>
      <td>3671</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-myosin MHC IIa (rabbit polyclonal)</td>
      <td>Covance</td>
      <td>PRB-440P</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-β-catenin (mouse monoclonal)</td>
      <td>Santa Cruz</td>
      <td>sc7963</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-integrin β1 (mouse monoclonal)</td>
      <td>Santa Cruz</td>
      <td>sc13590</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>A431</td>
      <td>Cell Service department of Francis Crick Institute</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>VCAF2B</td>
      <td>Previously established (Gaggioli et al., 2007)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (Homo-sapiens)</td>
      <td>px458CTNNA1 gRNA</td>
      <td>Santa Cruz</td>
      <td>sc-419475</td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (Homo-sapiens)</td>
      <td>px458MMP14 gRNA</td>
      <td>This paper</td>
      <td>gctgctttgggccgagccg</td>
      <td>Targeting gRNA sequence</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>siRNA: non-targeting</td>
      <td>Dharmacon</td>
      <td>siGENOME Non-Targeting Control siRNAD-001210-01-05</td>
      <td>Silencer SelectUsed at 20 nM</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>siRNA: targeting ITGB3</td>
      <td>Dharmacon</td>
      <td>siGENOME SMARTpool M-004124-02-0010</td>
      <td>Silencer SelectUsed at 20 nM</td>
    </tr>
    <tr>
      <td>Transfected construct (Homo-sapiens)</td>
      <td>pMMP14-mCherry</td>
      <td>Generous gift from Dr. Machesky at CRUK Beatson Institute</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (Homo-sapiens)</td>
      <td>pCSII-mCherry-CAAX</td>
      <td>Previously generated</td>
      <td></td>
      <td>Lentiviral construct to transfect and express membrane targeting mCherry</td>
    </tr>
    <tr>
      <td>Transfected construct (Homo-sapiens)</td>
      <td>pCSII-ECFP-CAAX</td>
      <td>Previously generated</td>
      <td></td>
      <td>Lentiviral construct to transfect and express membrane targeting ECFP</td>
    </tr>
    <tr>
      <td>Transfected construct (Homo-sapiens)</td>
      <td>pCSII-KEIMA-CAAX</td>
      <td>Previously generated</td>
      <td></td>
      <td>Lentiviral construct to transfect and express membrane targeting KEIMA</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Collagen I</td>
      <td>BD Biosciences</td>
      <td>354236</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Matrigel</td>
      <td>BD Biosciences</td>
      <td>354234</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DQ collagen, type I from bovine skin, fluorescein conjugate</td>
      <td>Thermo Fisher Scientific</td>
      <td>D12060</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Y27632</td>
      <td>Tocris Bioscience</td>
      <td>1254</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>4-Hydroxytamoxifen (4OHT)</td>
      <td>Sigma</td>
      <td>H7904</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Edu Cell Proliferation kit for imaging, Alexa Fluor 488 dye</td>
      <td>Fisher Scientific</td>
      <td>C10337</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Experimental

#### Cell culture

Human vulval CAFs are described in Gaggioli et al., 2007. CAFs were cultured in Dulbecco's Modified Eagle Medium (DMEM) supplemented with 10% Fetal Bovine Serum (FBS) and 1% insulin–transferrin–selenium (Invitrogen, no. 41400–045) and 100  U/ml penicillin, and 100  μg/ml streptomycin. Human vulval SCC cell line A431 cells were grown in DMEM supplemented with 10% FBS, 100  U/ml penicillin, and 100  μg/ml streptomycin. For ROCK inhibitor treatment cells were treated with 10 µM Y27632.

#### Stable cell lines

CTNNA1 or MMP14 KO A431 cells were generated by CRISPR-Cas9 as previously described (Labernadie et al., 2017). Briefly, pX458 vectors encoding gRNA sequences were transfected into A431 cells, and single GFP positive cells were sorted into 96-well plate 2 days after transfection. Cells were grown for 2 weeks, and KO was checked by western blot and sequencing of genome DNA. For MMP14 overexpressing cells, A431 cells were transfected with pMMP14-mCherry (generous gift from Dr. Machesky at CRUK Beatson Institute) and selected by G418 for 2 weeks. mCherry positive cells were sorted by flow cytometry. Stably labelled A431 cells and CAFs were obtained by infecting lentivirus containing fluorescent protein gene. 293 FT cells were transfected with pCSII-mCherry-CAAX, pCSII-ECFP-CAAX, or pCSII-KEIMA-CAAX construct and lentiviral RRE, REV, and VSVG encoding plasmids (5 µg each) by Xtremegene HP (Roche) according to the manufacturer’s recommendation. Resulting supernatant containing lentivirus was then infected to target cells.

#### Western blotting

Cells were lysed with Laemmli sample buffer containing 2.5% β-mercaptoethanol and heated at 95°C for 5  min. Samples were loaded to 4–15% polyacrylamide gels (Bio-Rad) for electrophoresis. Proteins were then transferred to a Poly Vinylidene DiFluoride (PVDF) membrane (Merck), which was blocked with 5% dry milk, Tris buffered saline, 0.2% Tween, and incubated with primary antibodies (overnight at 4°C) followed by secondary antibodies (1:10000) for 1  hr at room temperature. Proteins were detected by using Luminata Crescendo (Merck) and LAS600 (GE Healthcare). The following antibodies were used: anti-MMP14 rabbit monoclonal (1:1000, EP1264Y, Abcam), anti-alpha-catenin rabbit monoclonal (1:1000, EP1793Y, Abcam), anti-Vimentin mouse monoclonal (1:1000, 1A4, Sigma), anti-Fibronectin rabbit polyclonal (1:1000, Sigma), anti-integrin β1 mouse monoclonal (1:1000, P5D2, Abcam), anti-integrin β3 rabbit monoclonal (1:1000, ERP17507, Abcam), and anti-actin mouse monoclonal antibody (1:2000, AC-40, Sigma).

#### Explant invasion assay

Human head and neck squamous cell carcinoma were collected with informed consent from all subjects and following ethical approval from the Institute of Cancer Research/Royal Marsden Hospital – reference CCR 2924. Frozen sections were stained as described previously (Hidalgo-Carcedo et al., 2011 Calvo et al., 2013). Patient-derived SCC tissues were chopped into small pieces (roughly 1 mm3) and embedded in Collagen I/ Matrigel. Time-lapse images were taken by microscope every 10 min.

#### Spheroid invasion assay

A431 and CAF cells were detached from the cell culture dishes with trypsin and re-suspended in sterile 0.25% methylcellulose solution in DMEM. The cellulose solution contained a 1:1 ratio of A431 and CAF cells at a concentration of 1 × 105 cells/ml. Twenty microlitre droplets were plated onto the underside of a 10-cm culture dish and allowed to form spheroids in a 37°C incubator overnight (hanging drop method). The spheroids were then embedded in a collagen I/Matrigel gel mix at a concentration of approximately 4  mg/ml collagen I and 2  mg/ml Matrigel (BD Bioscience) in 24-well glass-bottomed cell culture plates (MatTek) on a 37°C hot block. The gel was incubated for at least 30  min at 37°C with 5% CO2. The gel was covered with DMEM media containing 10% FCS. Sixty hours later, the spheroids embedded in the gel were washed with PBS and then fixed for 30  min at room temperature with 4% paraformaldehyde. The spheroids were then imaged with an inverted Zeiss LSM780 at a magnification of ×10, ×20, and ×63. Z-stack images spanning 100–150  μm were collected, and image stacks were processed by ZEN software (Carl Zeiss) to yield maximum-intensity projections.

For quantification of the images, strand length and width were measured using Fiji software. Strand tapering was calculated by the following formula: strand width at 20% from the root/strand width at 80% from the root.

For EdU labelling experiment, spheroids were incubated with EdU containing medium for 1 hr prior to fix the samples.

For mitomycin C treatment experiment, cells were treated with 0.5 μg/ml mitomycin C for 24 hr prior to be subjected to hanging drop procedure.

#### Organotypic invasion assay

Organotypic invasion assays were performed as previously described (Gifford and Itoh, 2019). Briefly, collagen I (BD Biosciences cat. No. 354249) and Matrigel (BD Biosciences cat. No. 354234) were mixed to yield a final collagen concentration of 4 mg/ml and a final Matrigel concentration of 2 mg/ml. After the gel had been left to set at 37°C for 1 hr, mixture of 5 × 105 A431 cells and 5 × 105 vulval CAFs (VCAFs) were plated on the top in complete medium. Twenty-four hours later, the gel was then mounted on a metal bridge and fed from underneath with complete medium (changed daily). After 6 days, the cultures were fixed with 4% PFA plus 0.25% glutaraldehyde in PBS and imaged using Zeiss LSM780 at a magnification of ×10 and ×20. Z-stack images spanning 100–150  μm were collected, and image stacks were processed by ZEN software to yield maximum-intensity projections.

For organotypic killing assay, the gels containing 5 × 105 VCAFs were set without cancer cells and incubated for 5 days in complete media. Then the gels were incubated with the media with puromycin (5 µg ml–1) for 48 hr to kill the fibroblasts and then washed three times with complete media (30 min per wash). 5 × 105 cancer cells were then plated on top, and the assays proceeded as usual.

For quantification of the images, strand length and width were measured using Fiji software. Strand tapering was calculated by the following formula: strand width at 20% from the root/strand width at 80% from the root.

#### Wound healing assay

4 × 104 cells in 70 µL medium were seeded into each well of two-well culture insert (ibidi) and cultured overnight. After removing culture insert complete medium was added to the dish, and images were taken at 0, 9, and 24 hr. Empty area was measured using Fiji, and the results of 9 and 24 hr were normalised to that of 0 hr.

#### Proliferation assays

2D assay – 5 × 104 cells were seeded in 24-well plate, and the number of cells was counted everyday using Countess II automated cell counter (Thermo Fisher Scientific). Results were normalised to day 1. 3D ‘confined’ assay – SCC cells were mixed in collagen I/Matrigel at a concentration of 3 × 103 /ml, and 100 µL of the mixture was put in 96-well plate and incubated for an hour at 37°. After the incubation, 150 µL of complete medium was added to each well. Images of growing cells were taken at indicated time points with EVOS FL microscope system (Thermo Fisher Scientific).

#### ECM adhesion assay

Six-well plate was coated with collagen I (20 μg/ml) and Matrigel (20 μg/ml) for 2 hr. Cells were detached with Cell Dissociation Buffer enzyme-free (GIBCO), and 1 × 105 cells were seeded in each well. After 15 min of incubation, wells were washed twice with PBS, and cells were fixed with PFA. The number of cells in each field of view was counted to quantify the ECM adhesion ability of the cells.

#### Collagen and collagen proteolysis imaging

Cells were seeded in a collagen/Matrigel mix as described for the proliferation assays. Collagen fibres were imaged using reflectance imaging on a confocal microscope. For timelapse analysis, cell cultures were maintained at 37°C and 5% CO2. To visualise collagen proteolysis, the collagen/Matrigel mix was supplemented with 50 μg/ml DQ Collagen I. Collagen proteolysis was then imaged using a confocal with excitation at 488 nm and emission in the range 490–540 nm.

#### Immunostaining

Cells were fixed with 4% paraformaldehyde for 10  min and permeabilised in 0.1% Triton X-100 for 10  min. Cells were blocked in 1% BSA for 1  hr before incubation with primary antibodies – pS19-MLC (Cell Signaling #3671 L), myosin MHC IIa (Covance PRB-440P), fibronectin (Sigma F3648), β-catenin (Santa Cruz sc7963), integrin β1 (Santa Cruz sc13590), and integrin β3 (Abcam, ab179473) at 4°C overnight. After incubation, the appropriate fluorescence-conjugated secondary antibodies for 1 hr, cells were washed with PBS. Images were acquired with an inverted Zeiss LSM780 at a magnification of ×20 and ×63. For quantification of the pMLC staining, regions of interest were drawn around equal numbers of ‘free boundary zones’ of A431 cells in clusters and cell-cell contact zones, and the mean fluorescent intensity was measured. The values were then normalised to the mean of all the boundary and contact zones for WT A431 cells. Staining of frozen human tissue sections was performed in a similar manner, except that fixation and permeabilisation times were doubled, and 5% BSA was used as a block.

#### In vivo tumour growth

Cells were detached from culture flask and resuspended in 4 mg/ml Matrigel/PBS at a concentration of 2.5 × 107. Twenty microlitre of cell suspension was injected into ear intradermis of athymic nude mouse using 31 G needle (BD). The tumour size was measured every 3–4 days using caliper until it reached 0.6 mm in diameter. At the end point, mice were sacrificed, and the tumour samples were fixed with 4% PFA overnight and processed by standard methods for haematoxylin and eosin staining. Cervical lymph node was taken out and analysed for metastatic seeding.

### Computational

#### Cellular Potts model

Detailed information on mathematical background and C++ coding implementation for each cellular mechanism within the model can be found in Appendix 1 in Supplementary file 1 and at the GitHub repository https://github.com/RobertPJenkins/kato_jenkins_et_al_CC3D, (copy archived at swh:1:rev:b730d817f5c9cb11a4b3c5e02ccf03c829395fff; Jenkins, 2022).

#### Simulation quantification

MATLAB functions quantifying invasion metrics can be found at the GitHub repository listed above. For each simulation outcome of interest (e.g. each combination of parameter values), 10 CC3D simulations were run to generate invasion metrics. All invasion metrics were calculated in MATLAB (version 2019a). Unless stated, all invasion metrics were recorded at day 4. Invading cells are classed as all cells beyond the tumour interface at day 0. Maximum invasion is given by the maximum distance of any invasive SCC centroid to the initial tumour interface. Invasion score is equal to the total number of invasive SCCs multiplied by the mean distance of invasive centroids to the initial tumour interface. For mean number of SCC neighbours, tapering and number of fractured objects in the bulk tumour mass at day 4 are found. The mean number of SCC neighbours is calculated for all cells in the bulk tumour mass that is invading. For these cells, the gradient of line of best fit between the number of neighbours and distance from initial tumour interface is calculated to give the tapering metric. Fractured objects are defined as objects unconnected to the bulk tumour mass and containing at least one SCC. The number of these distinct objects is counted for the fractured object metric. For cell growth, the total number of SCCs versus time is recorded, and an exponential fitted to the resulting curve. For the combination of very large SCC-degradation (eight WT), SCC-SCC adhesion (two WT), and SCC-ECM adhesion (four WT) in the presence of CAFs, spheroids can become hollow and break apart. In such circumstances, there is no bulk tumour mass resulting in a mean number of neighbours of zero for the main tumour mass and a large number of fractured objects. There are four instances of this, and these data have been removed (leaving six simulations for this region of parameter space) prior to PCA analysis and heatmap generation. The track invasion score is taken at day 5. It is calculated by finding all points around a permissive track, beyond the initial tumour boundary where the ECM density is 0.75 or below (initial condition set to 1). These points are then weighted according to their distance from the boundary and then summed. For the spheroid permissive track simulations, both sides of the initial tumour mass are quantified. Track width is calculated as the maximum width of the invading strand. Strands that are either non-invasive or where the entire tumour mass has invaded uniformly do not record track width values. Curvature is quantified on day 7. The leading invasive edge is reduced to two one-dimensional signals in x-z and y-z for mid-points of y and x, respectively. Each one-dimensional signal is then smoothed with a smoothing window of 50 pixels. The LineCurvature2D function (Dirk-Jan Kroon (2021). 2D Line Curvature and Normals, MATLAB Central File Exchange. Retrieved 9 November 2021. https://www.mathworks.com/matlabcentral/fileexchange/32696-2d-line-curvature-and-normals) is used to calculate curvature for each signal and the average taken. For all heatmaps, for each box the x-axis represents the percentiles from 0.5 to 99.5 (left to right) of all 10 simulations for that outcome of interest.

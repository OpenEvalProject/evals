# Peer review - Round 1

Editors:
- Bernhard Schmid, University of Zurich Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62922.sa1](https://doi.org/10.7554/eLife.62922.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper presents a large data set of tree positions, heights and crown areas from 37 NEON sites across North America. Data obtained by remote sensing techniques about individual trees offer a large step forward from pixel-level data for ecologists interested in forest structure, size-density-diversity relationships and how these affect ecosystem functioning, arguably the most important topic in current forest research.

Decision letter after peer review:

Thank you for submitting your article "NEON Crowns: a remote sensing derived dataset of 100 million individual tree crowns" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Bernhard Schmid as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Meredith Schuman as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional work is required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This paper presents a large data set of tree positions, heights and crown areas from 37 NEON sites across North America. The authors used airborne RGB data and a previously published Python software tool to delineate crowns of individual canopy trees. They then compared a subset of these crowns with crowns identified by visual inspection of the airborne pictures and with field-measured stem positions and height and crown data. The accuracy of the automatic detection was about 70 %. Lidar measurements were used to exclude trees or objects less than 3 m tall and to estimate the height of the trees with an accuracy of roughly 2 m RMSE.

The authors discuss some possible uses of the individual-level tree data, but clearly these potential uses could be much extended if the data set could be updated and improved as further information becomes available, which the authors point out. It is difficult to judge to which extent this would be possible with the particular approach used in the paper. The authors would have to provide at least a summary of the algorithms implemented in their software tool (e.g. as supplement), because even the previously published paper in Methods in Ecology and Evolution does not provide this information, nor could I find it on the website of the tool.

Essential revisions:

The major issue that should be solved is that the LiDAR data should be included to improve the crown detection efficiency:

i) The reviewers are very surprised that you do not to use the LiDAR data in the segmentation of the single tree crowns. There exists a large body of different LiDAR-based individual tree crown (ITC) approaches, a number of benchmarking studies and open-source benchmarking datasets for comparing new methods with older ones.

ii) If you use LiDAR based ITC methods, you could remedy some of the error sources of your current approach, i.e. shaded crowns and sub-dominant trees. The references to such approaches are missing, even in contexts directly related to some of the potential applications of the dataset, i.e., the ITC-related papers of Duncanson et al., working on two of the NEON sites and, for the first time, showing the potential of LiDAR ITC-based allometries.

iii) Why not use height as a fourth dimension besides RGB? For example, two neighboring trees with similar optical properties could be separated by height. Also in general, does this approach allow to add more bands as from multi- or hyperspectral sensors?

iv) Besides the important measures of stem density and crown size distributions, the dataset could also be used as a starting point to refine other individual tree crown detection methods, for example using lidar point cloud segmentation in 3D space.

v) Finally, it's worth mentioning the various efforts for individual tree detection from airborne laser scanning data. It would be good to compare your results to point-cloud based segmentation, or also to test the use of this dataset for more extensive 3D segmentation algorithms, e.g. by using the tree locations as seed points for 3D segmentation of the point cloud.

Here is a list of references on ITC from LIDAR/RGB Imagery:

[1] Y. Wang, J. Hyyppa, X. Liang, H. Kaartinen, X. Yu, E. Lindberg, J. Holmgren, Y. Qin, C. Mallet, A. Ferraz, H. Torabzadeh, F. Morsdorf, L. Zhu, J. Liu, and P. Alho, "International benchmarking of the individual tree detection methods for modeling 3-d canopy structure for silviculture and forest ecology using airborne laser scanning," IEEE Transactions on Geoscience and Remote Sensing, vol. 54, no. 9, pp. 5011-5027, 2016.

[2] M. Parkan and D. Tuia, "Individual tree segmentation in deciduous forests using geodesic voting," in 2015 IEEE International Geoscience and Remote Sensing Symposium (IGARSS), pp. 637-640, July 2015.

[3] L. Duncanson, O. Rourke, and R. Dubayah, "Small sample sizes yield biased allometric equations in temperate forests," Scientific Reports, vol. 5, no. 1, p. 17153, 2015.

[4] L. Duncanson, R. Dubayah, B. Cook, J. Rosette, and G. Parker, "The importance of spatial detail: Assessing the utility of individual crown information and scaling approaches for lidar-based biomass density estimation," Remote Sensing of Environment, vol. 168, pp. 102 – 112, 2015.

[5] L. Eysn, M. Hollaus, E. Lindberg, F. Berger, J.-M. Monnet, M. Dalponte, M. Kobal, M. Pellegrini, E. Lingua, D. Mongus, and N. Pfeifer, "A benchmark of lidar-based single tree detection methods using heterogeneous forest data from the alpine space," Forests, vol. 6, no. 5, p. 1721, 2015.

[6] L. Duncanson, B. Cook, G. Hurtt, and R. Dubayah, "An efficient, multi-layered crown delineation algorithm for mapping individual tree structure across multiple ecosystems," Remote Sensing of Environment, vol. 154, pp. 378 – 386, 2014.

[7] A. Ferraz, F. Bretar, S. Jacquemoud, G. Gon?alves, L. Pereira, M. Tom?, and P. Soares, "3-d mapping of a multi-layered mediterranean forest using als data," Remote Sensing of Environment, vol. 121, pp. 210-223, June 2012.

[8] H. Kaartinen, J. Hyypp ̈a, X. Yu, M. Vastaranta, H. Hyypp ̈a, A. Kukko, M. Holopainen, C. Heipke, M. Hirschmugl, F. Morsdorf, E. Næsset, J. Pitk ̈anen, S. Popescu, S. Solberg, B. M. Wolf, and J.-C. Wu, "An international comparison of individual tree detection and extraction using airborne laser scanning," Remote Sensing, vol. 4, pp. 950-974, 2012.

[9] J. Vauhkonen, L. Ene, S. Gupta, J. Heinzel, J. Holmgren, J. Pitk ̈anen, S. Solberg, Y. Wang, H. Weinacker, K. M. Hauglin, V. Lien, P. Packal ́en, T. Gobakken, B. Koch, E. Næsset, T. Tokola, and M. Maltamo, "Comparative testing of single-tree detection algorithms under different types of forest," Forestry, vol. 85, no. 1, pp. 27-40, 2012.

[10] H. O. Orka, E. Næsset, and O. M. Bollandsas, "Classifying species of individual trees by intensity and structure features derived from airborne laser scanner data," Remote Sensing of Environment, vol. 113, no. 6, pp. 1163 – 1174, 2009.

[11] J. Reitberger, P. Krzystek, and U. Stilla, "Analysis of full waveform lidar data for the classification of deciduous and coniferous trees," International Journal of Remote Sensing, vol. 29, no. 5, pp. 1407-1431, 2008.[12] Y. Wang, H. Weinacker, and B. Koch, "A lidar point cloud based procedure for vertical canopy structure analysis and 3d single tree modelling in forest," Sensors, vol. 8, no. 6, pp. 3938-3951, 2008.

[13] S. Solberg, E. Naesset, and O. Bollandsas, "Single tree segmentation using airborne laser scanner data in a structurally heterogeneous spruce forest," Photogrammetric Engineering and Remote Sensing, vol. 72, no. 12, pp. 1369-1378, 2006.

[14] D. G. Leckie, F. A. Gougeon, S. Tinis, T. Nelson, C. N. Burnett, and D. Paradine, "Automated tree recognition in old growth conifer stands with high resolution digital imagery," Remote Sensing of Environment, vol. 94, no. 3, pp. 311-326, 2004.

[15] F. Morsdorf, E. Meier, B. K ̈otz, K. I. Itten, M. Dobbertin, and B. Allg ̈ower, "Lidar-based geometric reconstruction of boreal type forest stands at single tree level for forest and wildland fire management," Remote Sensing of Environment, vol. 92, no. 3, pp. 353 – 362, 2004. Forest Fire Prevention and Assessment.

[16] T. Brandtberg, T. A. Warner, R. E. Landenberger, and J. B. McGraw, "Detection and analysis of individual leaf-off tree crowns in small footprint, high sampling density lidar data from the eastern deciduous forest in north america," Remote Sens. Environ., vol. 85, no. 3, pp. 290-303, 2003.

[17] H.-E. Andersen, S. E. Reutebuch, and G. F. Schreuder, "Automated individual tree measurement through morphological analysis of a lidar-based canopy surface model," 2001.

[18] J. Hyypp ̈a, O. Kelle, M. Lehikoinen, and M. Inkinen, "A segmentation-based method to retrieve stem volume estimates from 3-d tree height models produced by laser scanners," IEEE Transactions on Geoscience and Remote Sensing, vol. 39, pp. 969-975, 2001.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A remote sensing derived dataset of 100 million individual tree crowns for the National Ecological Observatory Network" for further consideration by eLife. Your revised article has been evaluated by Meredith Schuman (Senior Editor) and Bernhard Schmid (Reviewing Editor).

Your revisions are convincing. However, we find:

1) you could still make it clearer why LiDAR currently could not further improve the detection of individual crowns (because of low resolution and inconsistencies across multiple sites in available LiDAR data) and what would be needed and hopefully will become available to include LiDAR more fully for future improvements of the data set (higher resolution data consistently available across all sites plus methods development).

2) Although this is essentially a data paper, it would be good if you could add more concrete suggestions what could be done with the data. You do mention the value of individual data as opposed to pixel data in very general terms. But for example, even though you show a figure with densities, in the corresponding paragraph it is not really discussed why density is so extremely important in forest ecology (see e.g. Barrufol et al. cited in the previous review for just one example). Individuals are also important for estimating biodiversity once you can assign traits or even species identities to them, and biodiversity is probably the most important variable you eventually would like to assess with such a data set (see e.g. J. Liang et al., 2016 and Huang et al., Science 362, 80-83 (2018), DOI: 10.1126/science.aat6405).

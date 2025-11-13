# anTraX, a software package for high-throughput video tracking of color-tagged insects

## Authors

- Asaf Gal<sup>1</sup> ([ORCID: 0000-0003-0834-2649](https://orcid.org/0000-0003-0834-2649)) †
- Jonathan Saragosti<sup>1</sup>
- Daniel JC Kronauer<sup>1</sup> ([ORCID: 0000-0002-4103-7729](https://orcid.org/0000-0002-4103-7729)) †

### Affiliations

1. Laboratory of Social Evolution and Behavior, The Rockefeller University New York United States

† Corresponding author

## Abstract

Recent years have seen a surge in methods to track and analyze animal behavior. Nevertheless, tracking individuals in closely interacting, group-living organisms remains a challenge. Here, we present anTraX, an algorithm and software package for high-throughput video tracking of color-tagged insects. anTraX combines neural network classification of animals with a novel approach for representing tracking data as a graph, enabling individual tracking even in cases where it is difficult to segment animals from one another, or where tags are obscured. The use of color tags, a well-established and robust method for marking individual insects in groups, relaxes requirements for image size and quality, and makes the software broadly applicable. anTraX is readily integrated into existing tools and methods for automated image analysis of behavior to further augment its output. anTraX can handle large-scale experiments with minimal human involvement, allowing researchers to simultaneously monitor many social groups over long time periods.

## Introduction

Our understanding of behavior, together with the biological, neural, and computational principles underlying it, has advanced dramatically over recent decades. Consequently, the behavioral and neural sciences have moved to study more complex forms of behavior at ever-increasing resolution. This has created a growing demand for methods to measure and quantify behavior, which has been met with a wide range of tools to measure, track, and analyze behavior across a variety of species, conditions, and spatiotemporal scales (Anderson and Perona, 2014; Berman, 2018; Brown and de Bivort, 2018; Krakauer et al., 2017; Dell et al., 2014; Robie et al., 2017a; Todd et al., 2017; Egnor and Branson, 2016). One of the exciting frontiers of the field is the study of collective behavior in group-living organisms and particularly the behavior of groups of insects. Insects provide an attractive and powerful model for collective and social behavior, as they exhibit a wide range in social complexity, from solitary to eusocial, while allowing for controlled, high-throughput experiments in laboratory settings (Feinerman and Korman, 2017; Lihoreau et al., 2012; Gordon, 2014; Schneider et al., 2012). However, although complex social behavior has been the focus of extensive research for over a century, technological advances are only beginning to enable systematic and simultaneous measurements of behavior in large groups of interacting individuals.

Solutions for automated video tracking of insects in social groups can be roughly divided into two categories (for reviews see Dell et al., 2014; Robie et al., 2017a): methods for tracking unmarked individuals (Branson et al., 2009; Pérez-Escudero et al., 2014; Romero-Ferrero et al., 2019; Sridhar et al., 2019; Feldman et al., 2012; Khan et al., 2005; Fasciano et al., 2014; Fasciano et al., 2013; Bozek et al., 2020), and methods for tracking marked individuals (Mersch et al., 2013; Robinson et al., 2012). The former category has the obvious advantages of reduced interference with natural behavior, unbounded number of tracked individuals, and not having the burden of tagging animals and maintaining these tags throughout the experiment. At the same time, these approaches, when applied to individual tracking, are limited by a more extensive computational burden, higher error rates, and stricter requirements for image quality. The most common approach for tracking unmarked individuals is to try and follow the trajectory of an individual for the duration of the video. The challenge in this approach is to resolve individuals from each other and link their locations in consecutive frames during close range interactions, when they are touching or occluding each other. Common solutions to this problem are to employ sophisticated segmentation methods (Branson et al., 2009; Pérez-Escudero et al., 2014; Sridhar et al., 2019), to use predictive modeling of the animals' motion (Branson et al., 2009; Fasciano et al., 2013), or to use image characteristics to match individuals before and after occlusions (Fasciano et al., 2014). The success of these solutions is case-specific and will usually be limited to relatively simple problems, where interactions are brief, occlusion is minimal, or image resolution is sufficient to resolve the individuals even during an interaction. One important limitation of this approach is that no matter how low the error rate is, it tends to increase rapidly with the duration of the experiment. The reason is that once identities are swapped, the error is unrecoverable, and will propagate from that moment on. A different algorithmic approach for tracking unmarked individuals is to use object recognition techniques to assign separate pieces of trajectories to the same individual (Pérez-Escudero et al., 2014; Romero-Ferrero et al., 2019). While this approach is promising and performs well on many tracking problems, it requires high image quality to identify unique features for each individual animal. It will also generally not perform well on animals with high postural variability and is hard to validate on large datasets.

On the other hand, tagging individuals with unique IDs has the advantage of having a stable reference, enabling error recovery. This approach also provides a simpler method for human validation or correction and enables following the behavior of individuals even if they leave the tracked region, or across experiments when the same animals are tested in different conditions. The use of general-purpose libraries such as AprilTags (Mersch et al., 2013; Olson, 2011; Heyman et al., 2017; Greenwald et al., 2018; Stroeymeyt et al., 2018) and ArUco (Garrido-Jurado et al., 2014), or application-specific patterned tags (Crall et al., 2015; Boenisch et al., 2018; Wario et al., 2015; Wild et al., 2018), has become the gold standard for this approach in recent years. However, these tags are applicable only to species with body sizes sufficiently large to attach them, have adverse effects on the animals’ behavior, and are often lost during experiments. They also require relatively high image resolution to correctly read the barcode pattern. Taken together, while currently available methods cover a wide range of experimental scenarios, the ability to accurately track the behavior of animals in groups remains one of the major hurdles in the field. As a result, much of the experimental work still relies on manual annotation, or on partially automated analysis pipelines that require considerable manual effort to correct computer-generated annotations (see Aguilar et al., 2018; Gelblum et al., 2015; Leitner and Dornhaus, 2019; Valentini et al., 2020 for recent examples). In principle, marked animals can also be tracked by general-purpose image-based trackers such as idTracker.ai, supplementing the pixel information of the animals’ appearances with artificial features. To the best of our knowledge, however, this approach has not been formally described, and it can be expected to perform less well than trackers specifically designed for a given marking technique.

Here, we present anTraX, a new software solution for tracking color-tagged insects and other small animals. Color tagging is one of the best-established and widely used methods to mark insects, both in the field and in the laboratory (Leitner and Dornhaus, 2019; Valentini et al., 2020; Walker and Wineriter, 1981; Gordon, 1989; Hagler and Jackson, 2001; Ulrich et al., 2018; Holbrook et al., 2011; Holbrook, 2009), with long-term durability and minimal effects on behavior. anTraX works by combining traditional segmentation-based object tracking with image-based classification using convolutional neural networks (CNNs). In addition, anTraX uses a graph object for representing tracking data (Nillius et al., 2006), enabling the inference of identity of unidentified objects by propagating temporal and spatial information, thereby optimizing the use of partial tag information. anTraX is uniquely suited for tracking small social insects that form dense aggregates, in which individuals are unidentifiable over large parts of the experiment even for the human observer. It will also be useful in tracking and analyzing behavior in heterogenic groups of ‘solitary’ insects, where keeping track of the individual identity for long experimental durations is important. Such experiments are of increasing interest, as the study of behavior in classical model systems like Drosophila fruit flies is shifting toward understanding more complex behavioral phenomena such as social interactions, individuality and inter-species interactions (Schneider et al., 2012; Seeholzer et al., 2018; Schneider and Levine, 2014; Honegger and de Bivort, 2018; Ayroles et al., 2015; Akhund-Zade et al., 2019).

While we tested anTraX and found it useful for behavioral analyses in a range of study systems, it was specifically developed for experiments with the clonal raider ant Ooceraea biroi. The clonal raider ant is an emerging social insect model system with a range of genomic and functional genetic resources (Ulrich et al., 2018; Oxley et al., 2014; Trible et al., 2017; McKenzie and Kronauer, 2018; Chandra et al., 2018; Teseo et al., 2014). The unique biological features of the species enable precise control over the size, demographics and genetic composition of the colony, parameters that are essential for systematic study of collective behavior in ants (Ulrich et al., 2018; Chandra et al., 2020). Moreover, the species is amenable to genetic manipulations (Trible et al., 2017), which opens new possibilities not only for understanding the genetic and neural bases of social and collective behaviors, but also for developing and validating theoretical models by manipulating behavioral rules at the level of the individual and studying the effects on group behavior. While these ants have great promise for the study of collective behavior, they are hard to track using available approaches, due to their small size and tendency to form dense aggregates. anTraX thus constitutes a crucial element in the clonal raider ant toolbox, enabling researchers to characterize behavior in unprecedented detail both at the individual and collective level.

anTraX was designed with large-scale behavioral experiments in mind, where hundreds of colonies are recorded in parallel for periods of weeks or months, making manual tracking or even error correction impractical. Its output data can be directly imported into software packages for higher level analysis of behavior (e.g. Kabra et al., 2013) or higher resolution postural analysis of individuals in the group (Pereira et al., 2019; Mathis et al., 2018; Berman et al., 2014; Graving et al., 2019). This enables the utilization of these powerful tools and methods for the study of social insects and collective behavior. anTraX is modular and flexible, and its many parameters can be set via a graphical interface. The software is open source, and its main algorithmic components can be easily modified. Here, we provide a brief description of the different steps and principles that constitute the anTraX algorithm, while a full description is given in the Appendix and the online documentation. We validate the performance of anTraX using a number of benchmark datasets that represent a variety of behavioral settings and experimental conditions.

## Materials and methods

The anTraX algorithm consists of three main steps. First, similar to other multi-object tracking algorithms (Pérez-Escudero et al., 2014; Romero-Ferrero et al., 2019), it segments the frames into background and ant-containing blobs and organizes the extracted blobs into trajectory fragments termed tracklets. The tracklets are linked together to form a directed tracklet graph (Nillius et al., 2006). The second step of the algorithm is tracklet classification, in which identifiable single-animal tracklets are labeled with a specific ID by a pre-trained CNN, while other tracklets are marked as either unidentified single-animal tracklets, or as multi-animal tracklets. Third, we infer the identity of unclassifiable tracklets in the tracklet graph by using temporal, spatial and topological propagation rules.

### Object tracking and construction of the tracklet graph

Each frame is subtracted from the background, and a fixed threshold is applied to segment the frame into background regions and animal-containing blobs to be tracked. When two or more animals are close together, they will often be merged into a single larger blob (Figure 1A–C). Unlike other tracking solutions, we do not attempt to separate these larger blobs into single animal blobs at this stage, because those attempts are based on heuristic decisions that do not generalize well across species and experimental conditions. Instead, we will infer the composition of these larger blobs from the tracklet graph in a later step. Each blob in the currently processed frame is then linked to blobs in the previous frame (Figure 1D–E). A link between a blob in frame t and a blob in frame t-1 implies that some or all of the animals that were part of the first blob, are present in the second one. A blob can be linked to one blob (the simplest case, where the two blobs have the same ant composition), to a few blobs (where animals leave or join the blob), or to none (suggesting the animals in the blob were not detected in the other frame). We use Optical Flow to decide which blobs should be linked across frames (Figure 1D). While Optical Flow is computationally expensive, we found it to be significantly more accurate than alternatives such as simple overlap or linear assignment (based either on simple spatial distance or on distance in some feature space). To reduce the computation cost, we run the optical flow in small regions of the image that contain more than one linking option (see Appendix section 1.4 for details).

![Figure 1.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig1-v1.jpg)

**Figure 1.:** (A) An example frame from an experiment with 16 ants marked with two color tags each. (B) The segmented frame after background subtraction. Each blob is marked with a unique color. Some blobs contain single ants, while others contain multiple ants. (C) A higher resolution segmentation example. While some ants are not distinguishable from their neighbors even for the human eye, others might be segmented by tuning the segmentation parameters, or by using other, more sophisticated segmentation algorithms. The anTraX algorithm takes a conservative approach and leaves those cases unsegmented to avoid segmentation errors. (D) Optical flow is used to estimate the ‘flow’ of pixels from one frame to the next, giving an approximation of the movements of the ants. The cyan silhouettes represent the location of an ant in the first frame, and the red silhouettes represent the location in the second frame. The results of the optical flow procedure are shown with blue arrows, depicting the displacement of pixels in the image. (E) An example of constructing and linking tracklets. Each layer represents a section of segmented frame. Two ants are approaching each other (tracklets marked τ1 and τ2), until they are segmented together. At that point, the two tracklets end, and a third multi-ant tracklet begins (τ3). Once the two ants are again segmented individually, the multi-ant tracklet ends, and two new single-ant tracklets begin (τ4 and τ5). (F) The graph representation of the tracklet example in E. (G) A tracklet graph from an experiment with 36 ants, representing 3 min of tracking data. The nodes are located according to the tracklet start time on the vertical axis, beginning at the bottom. The inset depicts a zoomed-in piece of the graph.

Blobs are organized into tracklets, defined as a list of linked blobs in consecutive frames that are composed of the same group of individuals (Figure 1E–F). Following linkage, tracklets are updated in the following way: (i) A blob in the current frame t that is not linked to any blob in the previous frame t-1, will 'open' a new tracklet. (ii) A blob in the previous frame that is not linked to any blob in the current frame, will 'close' its tracklet. (iii) If a pair of blobs in the previous and current frames are exclusively linked, the current blob will be added to the tracklet that contains the previous blob. (iv) Whenever a blob in the current or previous frames is connected to more than one blob, the tracklets of the linked blobs in the previous frames will 'close', and new tracklets will 'open' with the blobs in the current frame. In these latter cases, the linking between the blobs across different tracklets will be registered as an edge in the directed tracklet graph from the earlier tracklet to the latter. The tracklet graph is constructed by running an iterative loop over all the frames in the experiment. The result of this part of the algorithm, after processing all frames in the video, is a directed acyclic graph containing references to all tracklets and blobs in the dataset (Figure 1G).

### Tracklet classification

The next step is tracklet classification, in which we label tracklets containing single animals that can be reliably identified with a specific ID (Appendix section 2.3). The successful propagation of individual IDs on top of the tracklet graph requires at least one identification of each ID at this step. Propagation will improve with additional independent identifications of individuals throughout the video. Nevertheless, it is important to note that our approach does not rely on the identification of each and every tracklet, but rather on inferring the composition of tracklets based on propagation of IDs on top of the tracklet graph. Hence, we apply a conservative algorithm that classifies only reliable cases and leaves ambiguous ones as unidentified. Classification is done by training and applying a convolutional neural network (CNN) on each blob image in the tracklet. The most frequent ID is then applied to the entire tracklet (Figure 2A). In addition to the ID label, we also assign a classification confidence score to each classified tracklet, which takes into account the number of identified blobs in the tracklet, the confidence of each classification, and the prevalence of contradictory classifications across blobs in the tracklet (see Appendix section 2.4). anTraX comes with a graphical interface for training, validating, and running the CNN (see Supplementary Material and online documentation).

![Figure 2.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig2-v1.jpg)

**Figure 2.:** (A) Schematic of the tracklet classification procedure. All blobs belonging to the tracklet are classified by a pre-trained CNN classifier. The classifier assigns a label to each blob, which can be an individual ID (depicted as colored rectangles in the figure), or an ambiguous label (‘unknown’, depicted in gray). The tracklet is then classified as the most abundant ID in the label set, along with a confidence score that depends on the combination of blob classifications and their scores (see Supplementary Material for details). (B) A simple example of propagating IDs on top of the tracklet graph. The graph represents a tracking problem with three IDs (represented as red/blue/green) and eight tracklets, of which some are single-animal (depicted as circles) and some are multi-animal (depicted as squares). Three of the single-animal tracklets have classifications, and are depicted as color-filled circles. The graph shows how, within four propagation rounds, assigned IDs are propagated as far as possible, both negatively (round head arcs) and positively (arrow heads), until the animal composition of all nodes is fully resolved. See also Figure 2—video 1 for an expanded animated example. (C) An example of a solved tracklet graph from an experiment with 16 ants, representing 10 min of tracking. Single ant tracklets are depicted as circle nodes and multi ant tracklets are depicted as square nodes. Black circles represent single ant tracklets that were assigned an ID by the classifier. A subgraph that corresponds to a single focal ant ID (‘GO’: an ant marked with a green thorax tag and an orange abdomen tag) is highlighted in color. Green nodes represent single ant tracklets assigned by the classifier. Blue nodes represent tracklets assigned by the propagation algorithm. Red nodes are residual ambiguities. (D) Example snapshots of the focal ant GO at various points along its trajectory, where it is often unidentifiable. The second image from the bottom shows an image where the ant is identifiable. While the third image from the bottom shows an unidentifiable ant, it belongs to a tracklet which was assigned an ID by the classifier based on other frames in the tracklet. The first and last images show the focal ant inside aggregations, and were assigned by the propagation algorithm. The purple arrows connect each image to its corresponding node in C. (E) The 10-min long trajectories corresponding to the graph in C. The trajectory of the focal ant GO is plotted in orange, while the trajectories of all other ants are plotted in gray. Purple arrows again point from the images in D to their respective location in the trajectory plot. (F) Plot of the x and y coordinates of the focal ant during the 10 min represented in the graph in C. Gaps in the plot (marked with green asterisks) correspond to ambiguous segments, where the algorithm could not safely assign the ant to a tracklet. In most cases, these are short gaps when the ant does not move, and they can be safely interpolated to obtain a continuous trajectory.

### ID propagation

The last part of the algorithm is the propagation of ID assignments on the tracklet graph. While formal approaches for solving this problem using Bayesian inference have been proposed (Nillius et al., 2006), we chose to implement an ad-hoc greedy iterative process that we found to work best in our particular context. Each node in the graph (corresponding to a tracklet) is annotated with a dynamic list of assigned IDs (IDs that are assigned to the tracklet) and a list of possible IDs (IDs that might be assigned to the tracklet, i.e., that were not yet excluded). Initially, all nodes are marked as ‘possible’ for all IDs, and no IDs are assigned to any nodes. All the classified tracklets from the previous step are now ranked by their confidence score. Starting with the highest confidence tracklet, its ID is propagated on the graph as far as possible. Propagation is done vertically on the graph on top of edges, both positively (an ID that is assigned to a node must also be assigned to at least one of its successors and one of its predecessors) and negatively (an ID cannot be in the possible list of a node, if it is not in at least one successor and one predecessor node), horizontally (if an ID is assigned to a node, it cannot be assigned to any other time-overlapping node), and using topological constraints (Figure 2B, Figure 2—video 1). Only non-ambiguous propagation is performed, and propagation is halted whenever an ambiguity or contradiction arises. We iterate the propagation until no more assignments can be made. Some of the propagation rules are modified in cases of tracklets that start or end in regions where individuals can enter or leave the tracked area (see Appendix section 3). Figure 2C–F visualizes an example of tracking an ant throughout a 10 min segment from an actual experiment and depicts the path of the ant through the tracklet graph along with its spatial trajectory.

### Export positional and postural results for analysis

The tracking results are saved to disk and can be accessed using supplied MATLAB and Python interface functions. For each individual ID in the experiment, a table is returned, containing its assigned spatial coordinates in each frame of the experiment, and a flag indicating the type of the location estimation (e.g. direct single-animal classification, inferred single-animal, multi-animal tracklet). For frames where the location is derived from single animal tracklets (i.e. the animal was segmented individually), the animal orientation is also returned. Locations estimated from multi-animal tracklets are necessarily less accurate than locations from single-animal tracklets, and users should be aware of this when analyzing the data. For example, calculating velocities and orientations is only meaningful for single-animal tracklet data, while spatial fidelity can be estimated based also on approximate locations. A full description of how to import and process the tracking results is provided in Appendix section 3.6 and the online documentation.

### User interface and parameter tuning

anTraX has many parameters that control the image segmentation step, the classifier architecture and training procedure, and the propagation algorithm. The optimal value for each depends on the specific nature and settings of the processed experiment, from the resolution and quality of the camera, to the details of the organisms and number of tags. anTraX comes with a graphical user interface to tune and verify the value of these parameters. anTraX also contains a user interface for creating an image database and training the CNN for tracklet classification.

### Parallelization and usage on computer clusters

anTraX was specifically designed to process large-scale behavioral experiments, which can contain hundreds of video files and tens of terabytes of data. anTraX includes scripts to process such large datasets in batch mode where individual video files are tracked in parallel on multicore computers and high-performance computer clusters. Following per-video processing, anTraX will run a routine to ‘stitch’ the results of the individual files together (see online documentation).

### Availability and dependencies

The core tracking steps of anTraX are implemented using MATLAB version 2019a, while the classification parts are implemented using TensorFlow v1.15 in the Python 3.6 environment. Compiled binaries are available for use with the freely available MATLAB Runtime Library and can be run with a command line interface. anTraX can be run on Linux/OSX systems, and large datasets benefit considerably from parallelization on computer clusters. anTraX depends on the free FFmpeg library for handling video files. The result files are readable with any programming language, and we supply a Python module for easily interfacing with output data. anTraX is distributed under the GPLv3 license, and its source code and binaries are freely available (Gal et al., 2020a). anTraX is a work in progress and will be continuously extended with new features and capabilities. Online documentation for installing and using the software is available at http://antrax.readthedocs.io. Users are welcome to subscribe, report issues, and suggest improvements using the GitHub interface.

## Results

### anTraX tracks individual ants with near-human accuracy over a wide range of conditions

As any tracking algorithm, the performance of anTraX depends on many external factors, such as the image quality, the framerate, the quality of the color tags (size, color set, number of tags per individual), and the behavior of the organisms (e.g. their tendency to aggregate, their activity level, etc). anTraX was benchmarked using a number of datasets spanning a variety of experimental conditions (e.g. image quality and resolution, number of tracked individuals, number of tags and colors, size variability in the colony) and study organisms, including four different ant species, as well as the fruit fly Drosophila melanogaster (Table 1, Figure 3 and its supplements). All benchmark datasets, together with the raw videos, full description, configuration files, and trained classifiers are available for download (Gal et al., 2020b).

![Figure 3.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig3-v1.jpg)

**Figure 3.:** In this experiment, the ants are freely behaving in a closed arena that contains the nest (the densely populated area on the top left) and exploring ants. A short annotated clip from the tracked dataset is given as Figure 3—video 1. Tracking outputs and annotated videos of all datasets are also given in the supplementary figures and videos of this figure. (A) A labeled frame (background subtracted), showing the location of each ant in the colony, as well as a ‘tail’ of the last 10 s of trajectory. Ants that are individually segmented have precise locations. The ants clustered together have approximate locations. Labels indicate the color tag combination of the ant (e.g. ‘BG’ indicates a blue thorax tag and a green abdomen tag; colors are blue (B), green (G), orange (O), and pink (P)). (B) Individual trajectories for each ant in the colony, based on 1 hr of recording. (C) A cropped image of each ant from the video.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** The figure follows the same format as Figure 3.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** The figure follows the same format as Figure 3.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** The figure follows the same format as Figure 3.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig3-figsupp4-v1.jpg)

**Figure 3—figure supplement 4.:** The figure follows the same format as Figure 3.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig3-figsupp5-v1.jpg)

**Figure 3—figure supplement 5.:** The figure follows the same format as Figure 3.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig3-figsupp6-v1.jpg)

**Figure 3—figure supplement 6.:** The figure follows the same format as Figure 3.

![Figure 3—figure supplement 7.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig3-figsupp7-v1.jpg)

**Figure 3—figure supplement 7.:** The figure follows the same format as Figure 3.

![Figure 3—figure supplement 8.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig3-figsupp8-v1.jpg)

**Table 1.**
 Summary description of the benchmark datasets.All raw videos and parameters of the respective tracking session are available for download (Gal et al., 2020b).


<table>
  <thead>
    <tr>
      <th>Dataset</th>
      <th>Species</th>
      <th>#Animals</th>
      <th>#Colors</th>
      <th>#Tags</th>
      <th>Open* ROI</th>
      <th>Duration (hr)</th>
      <th>Camera</th>
      <th>FPS</th>
      <th>Image size (pixels)</th>
      <th>Resolution (pixels/mm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>J16</td>
      <td>Ooceraea biroi</td>
      <td>16</td>
      <td>4</td>
      <td>2</td>
      <td>No</td>
      <td>24</td>
      <td>Logitech C910</td>
      <td>10</td>
      <td>960 × 720</td>
      <td>10</td>
    </tr>
    <tr>
      <td>A36</td>
      <td>Ooceraea biroi</td>
      <td>36</td>
      <td>6</td>
      <td>2</td>
      <td>No</td>
      <td>24</td>
      <td>PointGrey Flea3 12MP</td>
      <td>10</td>
      <td>3000 × 3000</td>
      <td>25</td>
    </tr>
    <tr>
      <td>C12</td>
      <td>Camponotus fellah</td>
      <td>12</td>
      <td>7</td>
      <td>3</td>
      <td>No</td>
      <td>6</td>
      <td>Logitech C910</td>
      <td>10</td>
      <td>2592 × 1980</td>
      <td>17</td>
    </tr>
    <tr>
      <td>C32</td>
      <td>Camponotus sp.</td>
      <td>28</td>
      <td>6</td>
      <td>3</td>
      <td>No</td>
      <td>24</td>
      <td>PointGrey Flea3 12MP</td>
      <td>10</td>
      <td>2496 × 2500</td>
      <td>13</td>
    </tr>
    <tr>
      <td>G6 × 16</td>
      <td>Ooceraea biroi</td>
      <td>6 × 16†</td>
      <td>3</td>
      <td>2</td>
      <td>No</td>
      <td>1.33</td>
      <td>Logitech C910</td>
      <td>10</td>
      <td>2592 × 1980</td>
      <td>17</td>
    </tr>
    <tr>
      <td>V25</td>
      <td>Ooceraea biroi</td>
      <td>25</td>
      <td>5</td>
      <td>2</td>
      <td>Yes</td>
      <td>3</td>
      <td>Logitech C910</td>
      <td>10</td>
      <td>2592 × 1980</td>
      <td>17</td>
    </tr>
    <tr>
      <td>T10</td>
      <td>Temnothorax nylanderi</td>
      <td>10</td>
      <td>5</td>
      <td>4</td>
      <td>No</td>
      <td>6</td>
      <td>Logitech C910</td>
      <td>10</td>
      <td>2592 × 1980</td>
      <td>17</td>
    </tr>
    <tr>
      <td>D7</td>
      <td>Drosophila melanogaster</td>
      <td>7</td>
      <td>7</td>
      <td>1</td>
      <td>No</td>
      <td>3</td>
      <td>PointGrey Flea3 12MP</td>
      <td>18</td>
      <td>1056 × 1050</td>
      <td>26</td>
    </tr>
    <tr>
      <td>D16</td>
      <td>Drosophila melanogaster</td>
      <td>16</td>
      <td>4</td>
      <td>2</td>
      <td>No</td>
      <td>5</td>
      <td>PointGrey Flea3 12MP</td>
      <td>18</td>
      <td>1200 × 1200</td>
      <td>16</td>
    </tr>
  </tbody>
</table>

_ROI: region of interest; FPS: frames per second. *Whether or not the ants can leave the tracked region. †Dataset G6 × 8 is derived from six replicate colonies with eight ants each._

The performance of the tracking algorithm can be captured using two separate measures. The first is the rate of assignment, defined as the ratio of assigned locations in the experiments to the total possible assignments (i.e. the number of IDs times the number of frames). The second measure is the assignment error, defined as the ratio of wrong assignments to the total number of assignments made. While the assignment rate can be computed directly and precisely from the tracking results, the error rate in assigning IDs for a given data set needs to be tested against human annotation of the same dataset. Because the recording duration of these datasets is typically long (many hours), it is impractical to manually annotate them in full. Instead of using fewer or smaller datasets, which would have introduced a sampling bias, we employed a validation approach in which datasets were subsampled in a random and uniform way. In this procedure, a human observer was presented with a sequence of randomly selected test points, where each test point corresponded to a location assignment made by the software to a specific ID in a specific frame. The user was then asked to classify the assignment as either ‘correct’ or ‘incorrect’. If the user was unsure of the correctness of the assignment, they could skip to the next one. The process was repeated until the user had identified 500 points as either correct or incorrect. The accuracy of the tracking was measured as the ratio of correct test points to the sum of correct and incorrect test points, as determined by the human observer. This procedure samples the range of experimental conditions and behavioral states represented in each of the datasets in an unbiased manner, and provides a tracking performance estimate that can be applied and compared across experiments. Overall, anTraX performed at a level close to the human observer in all benchmark datasets (Table 2).

**Table 2.**
 Summary of tracking performance measures for the benchmark datasets using anTraX.Assignment rate is defined as the proportion of all data points (the number of individuals times the number of frames) in which a blob assignment was made. In cases of closed boundary regions of interest (ROIs; in which the tracked animals cannot leave the tracked region) this measure is in the range of 0–1. In cases of open boundary ROIs (marked with asterisks; e.g., dataset V25), the upper boundary is lower, reflecting the proportion of time the ants are present in the ROI. The assignment error is an estimation of the proportion of wrong assignments (i.e. an ant ID was assigned to a blob the respective ant is not present in). As explained in the text, the estimation is done by sequentially presenting the user with a sequence of randomly sampled assignments from the dataset and measuring the proportion of assignments deemed ‘incorrect’ by the observer, relative to the sum of all ‘correct’ and ‘incorrect’ assignments. To calculate the error rates reported in the table, the presentation sequence continued until exactly 500 assignments were marked as ‘correct’ or ‘incorrect’, ignoring cases with the third response ‘can’t say’. A 95% confidence interval of the error according to the Clopper-Pearson method for binomial proportions is also reported in the table. To quantify the contribution of using graph propagation in the tracking algorithm, the analysis was repeated ignoring assignments made during the graph propagation step, and the results are reported here for comparison. A graphical summary of the performance measures is shown in Figure 4A–B.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="3">Without graph propagation</th>
      <th colspan="3">With graph propagation</th>
    </tr>
    <tr>
      <th>Dataset</th>
      <th>Assignment rate</th>
      <th>Assignment error</th>
      <th>Assignment error 95% CI</th>
      <th>Assignment rate</th>
      <th>Assignment error</th>
      <th>Assignment error 95% CI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>J16</td>
      <td>0.28</td>
      <td>0.012</td>
      <td>0.0044–0.026</td>
      <td>0.93</td>
      <td>0</td>
      <td>0–0.0074</td>
    </tr>
    <tr>
      <td>A36</td>
      <td>0.24</td>
      <td>0.014</td>
      <td>0.0056–0.0286</td>
      <td>0.81</td>
      <td>0.006</td>
      <td>0.0012–0.0174</td>
    </tr>
    <tr>
      <td>C12</td>
      <td>0.82</td>
      <td>0</td>
      <td>0–0.0074</td>
      <td>0.99</td>
      <td>0</td>
      <td>0–0.0074</td>
    </tr>
    <tr>
      <td>C32</td>
      <td>0.26</td>
      <td>0.042</td>
      <td>0.0262–0.0635</td>
      <td>0.79</td>
      <td>0.022</td>
      <td>0.011–0.039</td>
    </tr>
    <tr>
      <td>G6 × 16</td>
      <td>0.57</td>
      <td>0.122</td>
      <td>0.0946–0.154</td>
      <td>0.89</td>
      <td>0.078</td>
      <td>0.056–0.105</td>
    </tr>
    <tr>
      <td>V25</td>
      <td>0.07*</td>
      <td>0.058</td>
      <td>0.0392–0.0822</td>
      <td>0.48*</td>
      <td>0.012</td>
      <td>0.0044–0.026</td>
    </tr>
    <tr>
      <td>T10</td>
      <td>0.56</td>
      <td>0.06</td>
      <td>0.041–0.0845</td>
      <td>0.96</td>
      <td>0.018</td>
      <td>0.0083–0.339</td>
    </tr>
    <tr>
      <td>D7</td>
      <td>0.88</td>
      <td>0</td>
      <td>0–0.0074</td>
      <td>0.98</td>
      <td>0</td>
      <td>0–0.0074</td>
    </tr>
    <tr>
      <td>D16</td>
      <td>0.89</td>
      <td>0.004</td>
      <td>0.0005–0.0144</td>
      <td>0.997</td>
      <td>0</td>
      <td>0–0.0074</td>
    </tr>
  </tbody>
</table>

### Graph inference dramatically improves tracking performance

The main novelty of anTraX compared to other tracking solutions is the use of a tracklet graph for ID inference. This method increases the tracking performance in several ways. First, it allows identification of tracklets that are unidentifiable by the classifier, using propagation of IDs from classified tracklets. Second, it corrects classification errors by overriding low-reliability assignments made by the classifier with IDs propagated from high-reliability tracklets. Third, it assigns IDs to multi-individual blobs and tracklets. This provides an approximate location for analysis, even when an animal cannot be individually segmented. Table 2 and Figure 4A–B show the increase in assignment coverage and decrease in assignment errors following graph propagation in all benchmark datasets.

![Figure 4.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig4-v1.jpg)

**Figure 4.:** (A) Contribution of graph inference to reduction of assignment error. The graph compares the assignment error in the benchmark datasets, defined as the rate of assigning wrong IDs to blobs across all IDs and frames in the experiment, and estimated as explained in the main text, before the graph propagation step of the algorithm (blue circles, ‘noprop’ category) and after the graph propagation step (orange circles, ‘final’ category). (B) Contribution of graph inference to increased assignment rate (the ratio of assignments made by anTraX to the total number of assignments possible in the experiment) in the benchmark datasets. The graph compares the assignment rate, as defined in the main text, before and after the graph propagation step (same depiction as in A). The performance measures for all benchmark datasets are reported in Table 2 and Figure 4—source data 1. (C–D) Same as in A and B, calculated for a large-scale dataset described in the text (10 colonies of 16 ants, recorded over 14 days). The performance measures for all replicas are reported in Figure 4—source data 2. (E) Generalizability of the blob classifier. Each point in categories 1–4 represents the generalization error of one classifier (trained with examples from number of replicas corresponding to its category) on data from one replica that was not used for its training. The replicas were recorded under similar conditions, but using different ants, different cameras, and different experimental setups. For classifiers trained on more than one replica, the combinations of replicas were randomly chosen, while maintaining the constraint that each replica is tested against the same number of classifiers in each condition. In the category ‘All’, the points depict the validation error of the full classifier, trained on data from the 10 replicas. All classifiers were trained with the same network architecture, started training from a scratch model, and were trained until saturation. The dashed line represents the mean validation error for the full classifier. The list of errors for all trained classifiers are given in Figure 4—source data 3.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) The relative fraction of assignment types for the benchmark datasets. Some datasets have only a small proportion of their assignments made by direct classification (e.g. dataset V25), while datasets with low interaction rates have most of their assignments made by direct classification (e.g. the Drosophila datasets D7 and D16). The two types of assignments add up to the total assignment rates as reported in Table 2. (B) The relative fraction of assignment types for the large-scale dataset described in the text (10 colonies of 16 ants each, recorded over 14 days). Here, the variability between the replicas is much reduced compared to the variability between the benchmark datasets in A. (C) The error in assignments via direct classification vs. propagation for the benchmark datasets. The errors were estimated by the same procedure used to estimate the total assignment error in Figure 4. The set of 500 random points was split according to the type of assignment, and the error was estimated by taking the relative number of incorrect assignments. No clear effect is observed between the groups (paired t-test, p=0.338). (D) The error in assignments via direct classification vs. propagation for the experiment in panel B, estimated as in C. No clear effect is observed between the groups (paired t-test, p=0.866). The low variability in the relative fraction of each assignment type between the replicas in this experiment also allows us to compare the total error, by pooling all 5000 validation points across all replicas. The total estimated error of assignments made by the classifier is 0.0039, with a 95% confidence interval of 0.0011–0.102, while the total estimated error of assignments made by the propagation algorithm is 0.0041, with a 95% confidence interval of 0.0025–0.0068. Overall, these results show that there is no systematic dependency of the assignment error on the step of the algorithm responsible for the assignment. Data for all plots in this figure are given in Figure 4—source data 1 and Figure 4—source data 2.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** In total, we detected 88 assignment errors in the validation procedure across all experiments. For each of these errors, we manually extracted the length of the erroneous segment, both in terms of number of tracklets (A) and time (B). Both histograms show that the algorithm is robust against error propagation, and successfully terminates the propagation after a small number of propagation steps. Checking the instances where the error was propagated for more than four steps showed that, in each case, the reason was that more than one incorrect classification existed in the erroneous segment. The raw data for the histograms are given in Figure 4—figure supplement 2—source data 1 and Figure 4—figure supplement 2—source data 2.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** (A) Cross-validation error of the blob classifier as a function of the number of examples per class in the training set. Each point represents an iteration of training/validation on a reduced labeled example set sampled randomly from the full example set of benchmark dataset A36 (36 O. biroi ants marked with two color dots each, see Table 1). For each value tested for the number of examples, 50 independent realizations of an example set of that size were sampled from the full example set. For each of these sampled example sets, a classifier was trained with 80% of the sampled examples, and its error was estimated on the remainder of the examples. (B) The procedure in A was repeated, but with the resolution of the example images reduced before training to 75%, 50% and 25% of the original size. Depicted are the mean and 95% confidence intervals of the cross-validation errors of the trained classifiers. (C) We used each classifier trained in B to classify the tracklets of 1 hr worth of tracking data from dataset A36, and then ran the propagation step of the algorithm. We estimated the resulting assignment error relative to a manually annotated set of validation points sampled randomly. We then plotted (mean and 95% confidence interval bands) the assignment error as a function of the classifier’s cross validation error. The graph shows that below a certain classification accuracy (around 90% in this case), the tracking error climbs rapidly. Moreover, the data of the classifiers from all image resolutions collapse onto a single curve, suggesting that the error of the classifier is the sole predictor of the final assignment error, irrespective of whether it is due to an insufficiently large training set or poor image quality.

To further demonstrate the utility of graph propagation, we used data from a full, large-scale experiment. We tracked the behavior of 10 clonal raider ant colonies, each consisting of 16 ants, for 14 days. The colonies were filmed at relatively low resolution using simple webcams (Logitech C910, 960 × 720 pixels image size, 10 frames per second), similar to that of benchmark dataset J16. This dataset represents a relatively challenging classification scenario, because the tags are small, and the colors are dull. Figure 4C–D show a comparison of assignment rate and accuracy across the 10 replicates before and after graph propagation, with both measures improving greatly. Moreover, the assignments made by the propagation algorithm are as reliable as the assignments made directly by the classifier (Figure 4—figure supplement 1). The propagation algorithm is also robust to classification errors, and successfully blocks their propagation on the tracklet graph (Figure 4—figure supplement 2).

### The blob classifier generalizes well across experimental replicates

Collecting examples and training the blob classifier is the most time-consuming step in the tracking pipeline, and a good classification is essential for high-quality tracking (Figure 4—figure supplement 3). Ideally, a universal blob classifier would be trained to identify the same tag combination across experiments, without the need to retrain a classifier for each experiment. In reality, however, this is impractical. CNN classifiers do not generalize well outside the image distribution they were trained on, so even apparently small changes in experimental conditions (e.g. the type or level of lighting used, or the color tuning of the camera) can markedly decrease classification performance. Nevertheless, when experiments are conducted using similar conditions (e.g. study organism, marking technique, experimental setup, etc), it is possible to construct a classifier that will generalize across these experiments with minimal or no retraining. This enables construction of efficient tracking pipelines for high-throughput and replicate experiments, without the need for additional manual annotations.

We assessed the generalizability of blob classifiers with the 10 replicates of the experiment described in the previous section. We trained a classifier on examples from one replicate, and then used it to classify blobs sampled from the other replicates. We similarly evaluated the performance of classifiers trained with examples from two, three, and four replicates, and compared the results to the performance of a classifier trained on examples from all replicates. The comparison shows that, despite variability in animal shape and behavior, tagging process, cameras, and experimental setups across replicates, the classifier performs remarkably well (Figure 4E). Moreover, when a classifier is trained with an example set obtained from as few as two replicates, it performs similarly well as a classifier trained with examples from all replicates. Obviously, the generalizability of this result will depend on how well conditions are standardized between replicates or experiments. Nevertheless, it demonstrates that robust behavioral tracking pipelines can be constructed with minimal retraining.

### anTraX can be combined with JAABA for efficient behavioral annotation of large datasets

While direct analysis of the tracking output is a possibility, phenotyping high-throughput experiments and extracting useful information from large-scale trajectory data beyond very simple measures are challenging and impractical. In recent years, the field of computational ethology has shifted to the use of machine learning, both supervised and unsupervised, for analyzing behavioral data (Todd et al., 2017; Egnor and Branson, 2016; Datta et al., 2019). One of the most useful and mature tools is JAABA, a package for behavioral annotation of large datasets using supervised learning (Kabra et al., 2013; Robie et al., 2017b). In short, JAABA projects trajectory data onto a high dimensional space of per-frame features. The user then provides the software with a set of examples for a certain behavior, and the software trains a classifier to find all occurrences of that behavior in a new dataset. anTraX includes functions to generate the per-frame data in a JAABA-compatible way. In addition to the original list of JAABA features, a set of anTraX-specific features is also generated (see online documentation for details). Beyond useful information about the appearance and kinematics of the tracked animals, these extra features provide information about whether an animal was segmented individually or was part of a multi-animal blob. This enables JAABA to learn behaviors that can only be assigned to individually segmented animals, such as those that depend on the velocity of the animal. The user can then label examples and train a classifier in the JAABA interface. This classifier can then be used to analyze entire experiments using the anTraX interface.

To demonstrate the power of this approach, we present two examples of using JAABA together with anTraX. In the first example, we train a classifier to detect O. biroi ants carrying a larva while walking. O. biroi ants carry their larva under their body, in a way not always obvious even to a human observer (Figure 5A, Figure 5—video 1). By using subtle changes in the ants’ appearance and kinematics, JAABA is able to classify this behavior with >93% accuracy (tested on a set of annotated examples not used for training). An example of trajectories from a 30 min period annotated with JAABA is shown in Figure 5B.

![Figure 5.](https://cdn.elifesciences.org/articles/58145/elife-58145-fig5-v1.jpg)

**Figure 5.:** (A) Ants carrying a larva while they move (green/green and yellow/blue) can be difficult to distinguish from ants not carrying larvae (blue/green and yellow/purple), even for a human observer. Figure 5—video 1 shows examples for ants walking with and without a larva. (B) However, using labeled examples to train a classifier, JAABA can reliably distinguish ants walking while carrying a larva from ants walking without one from anTraX tracking output. Shown here is a 30 min segment from the A36 dataset, where trajectories classified by JAABA as ants carrying a larva are plotted in red on the background of all other tracks (in gray). (C) Classifying stops using JAABA. The plot shows a 60 min segment from the A36 experiment, where all stops longer than 2 s are marked with a colored dot. The stops are classified into four categories: rest (red), local search (green), self-grooming (blue), and object-interaction (e.g. with a food item; pink). Figure 5—video 2 shows examples of stops from all types. (D) Applying a simple DeepLabCut model to track the ants’ antennae and main body axes, shown on segmented ant images from dataset A36. Figure 5—video 3 shows an animated tracking of all ants in the colony. (E–F) Using the results from DeepLabCut to track the behavior of an ant along its trajectory. A one-hour trajectory of one ant from dataset A36 is shown on the background of the tracks of all other ants in the colony in that period (in gray). In E, the focal trajectory is colored according to the total rate of antennal movement (measured in angular velocity units rad/s). In F, the focal trajectory is colored according to how much the antennae move in-phase or anti-phase (measured in angular velocity units rad/s). Together, these panels show the behavioral variability in antennal movement patterns.

In the second example, we used JAABA to classify the behavior of ants during periods when they are not moving. We trained a classifier to detect four distinct behaviors (Figure 5—video 2): rest, in which the ant is completely immobile; local search, in which the ant does not move but uses its antennae to explore the immediate environment; self-grooming, in which the ant stops to groom itself; and object-interaction, in which the ant interacts with a non-ant object such as a piece of food, a larva or a trash item. JAABA was able to identify these behaviors with >92% accuracy. Figure 5C shows the spatial distribution of the classified behaviors during all periods where an ant stops walking for more than 2 s in a 60-min experiment, across all ants in the colony.

### anTraX can be combined with DeepLabCut to augment positional data with pose tracking

Much attention has recently been given to tracking the relative position of animal body parts, taking advantage of the fast progress in machine learning and computer vision (Pereira et al., 2019; Mathis et al., 2018; Graving et al., 2019). This allows for the measurement and analysis of aspects of an animal’s behavior beyond what is extractable from its trajectory. Although these tools can in principle be directly applied to videos with multiple individuals (Iqbal et al., 2017; Insafutdinov et al., 2016), they are still not mature enough for large-scale use. A more reasonable approach it to combine individual animal pose tracking with a track-and-crop step (see discussion within Graving et al., 2019). To track body parts of individual animals within a group or a colony, we took advantage of the fact that anTraX segments and crops the images of individual animals as part of its workflow, and included an option to run pre-trained DeepLabCut models (Mathis et al., 2018) on these images, without the need to export the data in a DeepLabCut-readable format (which would have resulted in a heavy computational overhead). This way, the position of the tracked body parts relative to the animal’s centroid are returned together with the spatial location of the centroid. For training such a model, anTraX enables exporting cropped single animal videos that are loadable into the DeepLabCut user interface. Currently, this is only supported for single-animal tracklets, where animals are segmented individually.

Of course, the ability to perform accurate and useful pose estimation depends on the resolution at which animals appear in the video. To demonstrate the potential of this approach, we trained a simple DeepLabCut model to track the main body axis and antennae positions of ants from benchmark dataset A36. Figure 5D and Figure 5—video 3 show examples from the segmented and cropped images of the individual ants in the videos.

Ants use different antennation patterns to explore their environment (Draft et al., 2018), and the ability to track these patterns in parallel to their movement in space can contribute to our understanding of their sensory processing during free behavior. We used the pose tracking results to visualize the different modes of antennae movement used by the ants to explore their environment. Figure panels Figure 5E and F show the total movement rate and the relative phase of the two antennae along the trajectory of one ant in a 1-hr segment of the experiment, respectively, demonstrating the variability and richness inherent to these patterns.

## Discussion

anTraX is a new algorithm and software package that provides a solution for a range of behavioral tracking problems not well addressed by available methods. First, by using a deep neural network for image classification, it enables the tracking of insects that are individually marked with color tags. While color tags have been used successfully for behavioral analysis for decades in a wide range of social insects, and in many species they are the only practical type of marker, their use has been severely limited by the lack of automation. Second, unlike other existing approaches, it handles cases where insects tightly aggregate and are not segmentable, as well as cases where the tags are obscured. This is achieved by representing the tracking data as a directed graph, and using graph walks and logical operations to propagate information from identified to unidentified nodes. Third, anTraX handles very long experiments with many replicate colonies and minimal human oversight, and natively supports parallelization on computational clusters for particularly large datasets. Finally, anTraX can easily be integrated into the expanding ecosystem of open-source software packages for behavioral analysis, making a broad range of cutting-edge ethological tools available to the social insect community. anTraX is an open-source software and conveniently modular, with each step of the algorithm (segmentation, linking, classification, and propagation) implemented as a separate module that can be easily augmented or replaced to fit experimental designs that are not well handled by the current version of the algorithm. For example, the traditional background subtracted segmentation can be replaced with a deep learning-based semantic segmentation, that is training and using a classifier to distinguish pixels of the image as belonging to either background or foreground (Rajchl et al., 2017; Moen et al., 2019; Badrinarayanan et al., 2017). This can potentially allow analysis of field experiments with natural backgrounds, or experiments with non-static backgrounds, such as videos taken with a moving camera. Another possible extension is an informed ‘second pass segmentation’ step, where multi-animal blobs are further segmented into single-animal blobs, taking into account the composition of the blob (number and IDs of animals). Knowing the composition of the blob provides a method to algorithmically validate the segmentation, allowing a ‘riskier’ segmentation approach. Another approach to locate animals in aggregations more precisely is to use neural network-based detection of the tags themselves. This method has successfully been used for bees tagged with fiducial markers inside a hive (Wild et al., 2018). Having a record of the composition of tracklets and blobs also paves the way for performing image-based behavioral analysis of interactions (Dankert et al., 2009; Klibaite et al., 2017; Klibaite and Shaevitz, 2019), or constructing specialized image classifiers for interaction types (e.g. allogrooming, trophallaxis, aggression, etc). Lastly, a newer generation of pose-estimation tools, including SLEAP (Pereira et al., 2020) and the recent release of DeepLabCut with multi-animal support, enable the tracking of body parts for multiple interacting animals in an image. These tools can be combined with anTraX in the future to extend pose tracking to multi-animal tracklets, and to augment positional information for individual animals within aggregations.

In summary, anTraX fills an important gap in the range of available tools for tracking social insects, and considerably expands the range of trackable species and experimental conditions. It also interfaces with established ethological analysis software, thereby making these tools broadly accessible for the study of social insects. anTraX therefore has the potential to greatly accelerate our understanding of the mechanisms and principles underlying complex social and collective behavior.

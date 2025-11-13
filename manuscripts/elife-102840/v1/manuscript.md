# Automatic and accurate reconstruction of long-range axonal projections of single-neuron in mouse brain

## Authors

- Lin Cai<sup>1</sup> ([ORCID: 0000-0002-4413-3599](https://orcid.org/0000-0002-4413-3599))
- Taiyu Fan<sup>1</sup>
- Xuzhong Qu<sup>1</sup>
- Ying Zhang<sup>1</sup>
- Xianyu Gou<sup>1</sup>
- Quanwei Ding<sup>1</sup>
- Weihua Feng<sup>1</sup>
- Tingting Cao<sup>1</sup>
- Xiaohua Lv<sup>1</sup>
- Xiuli Liu<sup>1</sup>
- Qing Huang<sup>1</sup>
- Tingwei Quan<sup>1</sup> ([ORCID: 0000-0002-8393-4292](https://orcid.org/0000-0002-8393-4292)) †
- Shaoqun Zeng<sup>1</sup>

### Affiliations

1. Britton Chance Center for Biomedical Photonics, Wuhan National Laboratory for Optoelectronics, Huazhong University of Science and Technology Wuhan China ([ROR:00p991c53](https://ror.org/00p991c53))
2. MOE Key Laboratory for Biomedical Photonics, Wuhan National Laboratory for Optoelectronics, Huazhong University of Science and Technology Wuhan China ([ROR:00p991c53](https://ror.org/00p991c53))
3. School of Computer Science and Engineering, Hubei Key Laboratory of Intelligent Robot, Wuhan Institute of Technology Wuhan China ([ROR:04jcykh16](https://ror.org/04jcykh16))

† Corresponding author

## Abstract

Single-neuron axonal projections reveal the route map of neuron output and provide a key cue for understanding how information flows across the brain. Reconstruction of single-neuron axonal projections requires intensive manual operations in tens of terabytes of brain imaging data and is highly time-consuming and labor-intensive. The main issue lies in the need for precise reconstruction algorithms to avoid reconstruction errors, yet current methods struggle with densely distributed axons, focusing mainly on skeleton extraction. To overcome this, we introduce a point assignment-based method that uses cylindrical point sets to accurately represent axons and a minimal information flow tree model to suppress the snowball effect of reconstruction errors. Our method successfully reconstructs single-neuron axonal projections across hundreds of GBs (Gigabytes) images within a mouse brain with an average of 80% f1-score, while current methods only provide less than 40% f1-score reconstructions from a few hundred MBs (Megabytes) images. This huge improvement is helpful for high-throughput mapping of neuron projections.

## Introduction

Neuronal axons in general project to different brain regions, and their projection distribution is an essential cue for neuron type identification, neuronal circuit construction, and deeper insight into how information flows in the brain (Huang and Luo, 2015; Meijering, 2010; Parekh and Ascoli, 2013; Zingg et al., 2014). Advances in optical imaging and molecular labeling techniques (Cai et al., 2019; Chung and Deisseroth, 2013; Çiçek et al., 2016; Kim and Schnitzer, 2022; Li et al., 2010; Osten and Margrie, 2013) have allowed us to observe the entire mouse brain at single-axon resolution and provided the database for the study of neuronal projection patterns (Foster et al., 2021; Gao et al., 2022; Muñoz-Castañeda et al., 2021; Peng et al., 2021; Qiu et al., 2024; Sun et al., 2019; Xu et al., 2021; Zeng, 2022). However, the reconstruction of these long-range projected axons still requires extensive manual annotation in tens of TBs volumetric images (Çiçek et al., 2016; Friedmann et al., 2020; Wang et al., 2019; Winnubst et al., 2019; Zhou et al., 2021), this labor-intensive process creates a major bottleneck for high-throughput mapping of neuronal projections (Zeng and Sanes, 2017).

The difficulties in reconstructing the long-range projections of neurons are as follows. On the one hand, while molecular labeling techniques can shed light on a very small fraction of neurons, a significant fraction of neuronal axons is still densely distributed due to the morphological complexity of neurons. The identification of densely distributed axons is considered an open problem in the field (Li et al., 2019; Lichtman and Denk, 2011; Zeng and Sanes, 2017), which still has no good solution. On the other hand, during neuron reconstruction, reconstruction errors accumulate, and a single reconstruction error can result in an entire branch being connected erroneously to other neurons or missing (Helmstaedter, 2013). Therefore, effective large-scale reconstruction of neurons requires extremely high identification accuracy of dense axons. The contradictions between these two aspects seem hard to reconcile.

The current neuron reconstruction frameworks focus on how to accurately extract skeletons of neurites and establish the connections between skeletons (Meijering, 2010; Peng et al., 2015). The BigNeuron project (Manubens-Gil et al., 2023) conducts a systematic evaluation of 35 automatic neuron reconstruction algorithms, all of which are based on tracing neurite skeletons and can be divided into two categories: local and global approaches. In the local approach (Choromanska et al., 2012; Li et al., 2020; Peng et al., 2011; Yang et al., 2013), the localization of the next skeleton point requires computation of the signal anisotropy of the image region near the current skeleton point. Localization errors typically occur when this image region contains other neurite signals. The global approach (Li et al., 2019; Türetken et al., 2011; Xiao and Peng, 2013) first generates multiple seed points that are commonly located at the neurite centerline and then establishes connections between these seed points for generating the neurite skeleton. This connection relies mainly on spatial location information, resulting in densely distributed neurites being connected to each other erroneously. While deep learning is widely used in neuron reconstruction (Huang et al., 2020; Li and Shen, 2020; Liu et al., 2022; Zhou et al., 2018), - mainly for neuronal image segmentation and signal intensity enhancement to reduce reconstruction errors - even ideal segmentation with all neurite centers identified and their signal enhanced still exhibits significant reconstruction errors with skeleton-based methods (Figure 1—figure supplement 1).

To address the problem of error accumulation during neuron reconstruction, it is common practice to utilize statistical information of neuron morphology, such as the angle between two neurites, to identify and remove spurious connections between the reconstructed neurites. This strategy (Li et al., 2019; Quan et al., 2016) achieves 80% reconstruction accuracy from GB-scale images under two critical constraints: (1) precise identification of neurite terminals and branch points is required for accurate angle computation and morphological analysis, and (2) somatic locations are required as critical information to remove some links between the reconstructed neurites to ensure that each cell body can be mapped to the root node of a single tree structure. However, for long-range axonal reconstruction across hundreds of GB-scale images, the strategy is not effective to eliminate the accumulation of errors due to factors such as the position of the axon at a distance from the soma and slight morphological differences between axon junction and termination. Consequently, current long-range projection reconstruction methods are semi-automatic and require substantial human intervention (Gao et al., 2023; Wang et al., 2019; Winnubst et al., 2019; Zhou et al., 2021).

Here, we propose a new neuron reconstruction method called PointTree, which aims at how to assign foreground points in neuronal images to their own neurons. In the workflow, we design a constrained Gaussian clustering method to partition the foreground region of a neuronal image into a series of columnar regions whose centerline belongs to only a single neurite. This operation essentially eliminates the interference of different neurites in the dense reconstruction. In addition, each columnar region is characterized by a minimal envelope ellipsoid for constructing connections between columnar regions, which forms the neurite shapes. Based on the reconstructed shapes, we design a minimal information flow tree model to suppress the cumulative reconstruction error. Using the proposed method, we successfully achieve accurate reconstruction of long-range projections of neurons across hundreds of gigabytes of volumetric image.

## Results

### The architecture and principles of PointTree

In the design of PointTree, we have developed a series of optimization problems to assign foreground points in data blocks to their respective neurites. Firstly, the segment network is utilized for each data block to obtain foreground points. Subsequently, we apply a constrained Gaussian clustering method (Reynolds, 2009) to partition the foreground points into columnar regions and determine their geometrical parameters by solving the minimum-volume covering ellipsoids problem (Sun and Freund, 2004). Using these geometrical parameters, we construct a 0–1 assignment problem (Volgenant, 1996) to establish links between these columnar regions. Finally, skeletons are extracted from these linked columnar regions to reduce data redundancy by using region growing (Harris, 2011). The key procedures for neuron reconstruction are presented in Figure 1A.

![Figure 1.](https://cdn.elifesciences.org/articles/102840/elife-102840-fig1-v1.jpg)

**Figure 1.:** (A) The reconstruction procedure of PointTree involves the generation, clustering, and connection of foreground points (the first row). Within this procedure, three optimization problems are designed to allocate the foreground points into their respective neurites (the second row). (B) Schematic diagram of information flow score calculation. In a neurite branch with a fixed root node (green circle), the information flow score is calculated based on the assumption that a neurite has few directional changes. The assumption determines the neurite directly connecting to the root node (red), resulting in two branch angles used to calculate the information flow score. (C) Statistical analysis of the consistency between the minimum information flow and the real situation. For 208 neurite branches, the information flow scores are calculated as ground truth according to their manually determined skeletons and root nodes. These scores are then displayed in ascending order. The root nodes of neurite branches are changed to generate both maximum and minimum information flow scores. (D) One neurite branch is decomposed into two by minimizing the total information flow scores. (E) Performance of different methods on separating closely paralleled neurites. In PointTree, a single neurite is represented by a series of ellipsoids whose centerlines are not simultaneously located within different neurites. They are connected using an ellipsoid shape, which results in perfect reconstruction (Left). However, skeleton-based methods fail to separate two closely paralleled neurites due to interference from other signals (Red circle in middle) or connections being interfered with by another neighboring skeleton point (Red circle in right).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/102840/elife-102840-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** The ground-truth skeletons are generated using GTree (a semi-automatic software) with manual modification. A series of Gaussian kernels with mean values equal to the coordinates of skeleton points are summed to obtain the corresponding probability image block. The segmented image block is finally generated using a threshold method.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/102840/elife-102840-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** In (A), the calculation of the information flow score for a branch of neurites with root node 1 is illustrated. The reconstructed skeletons are transformed into a binary structure based on the root node, and the angles with respect to branching nodes labeled with brown circles determine the information flow. These angles will change when the root node changes. The angle of a branching node is formed by its father and child nodes, as exemplified by the N2 node. In (B), the optimization of tree structure to minimize the total information flow score is demonstrated. It shows that decreasing the information flow leads to a more proper tree structure. The second row of (B) provides an example of decomposing tree structure into two individual parts.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/102840/elife-102840-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (A) MIFT criterion will incorrectly split neurites with sharp directional changes into two branches, but the splitting location is explicitly recorded during this process. (B) Our algorithm searches for connectable neurites around the head nodes identified by MIFT. If no connectable neurites are found for both head nodes, the algorithm will reconnect them based on the recorded splitting points to prevent isolated neurite fragments. (C) presents two real examples violating the MIFT criterion. Through post-processing, PointTree successfully reconnects the split branches back to the correct neurites.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/102840/elife-102840-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** (A) shows an input swc file and its corresponding skeleton structure. (B) shows how the reconstructed skeletons are converted to a binary tree structure.

In addition, PointTree employed the statistical prior information to reduce the reconstruction errors. At the branching point (node) of the neurites, it can be divided into three segments of neurite skeletons. The segment entering the node forms two angles with the other two segments exiting the node respectively. The node angle is defined as the smaller angle between the entering segment and each exiting segment (Figure 1B). With node angle, we can identify the single complete neurite and its corresponding node angles. The skeleton of the neurite is generally smooth, with very few sudden directional changes and even fewer at the nodes. So, the node angles should be as small as possible. For neuronal branches, the node angles are uniquely determined when the root node is given, and the sum of the negative cosine of these node angles expressed by information flow value is small when the root node is correctly identified. This rule is defined as a minimal information flow tree (MIFT).

In image blocks of densely distributed neurites, we used semi-automatic software (Zhou et al., 2021) extracting 208 neuronal branches and identifying their root nodes. For each branch, we calculated their information flow values as the ground-truth information flow values (Figure 1C). To validate MIFT, we looped through all possible structures of these branches by changing the root node in order to compute the maximum and minimum information flow values (Figure 1C). It is evident that, for most neuronal branches (195/208), the ground-truth values of the information flow achieve the minimum value, suggesting that MIFT rule is reasonable. We utilized MIFT to modify skeleton structure and remove spurious connections between reconstructed neurites (Figure 1D and Figure 1—figure supplement 2), both for reconstructions within individual blocks and for the fused reconstruction in adjacent blocks.

PointTree has the capability to separate densely distributed neurites. When dealing with two parallel neurites in close proximity to each other, their shapes can be represented by a series of columnar regions (the left panels of Figure 1E). We have modified the Gaussian clustering algorithm by constraining the estimated mean and covariance parameters so that the cluster shape approaches a columnar shape. Additionally, foreground points within the same cluster are connected to each other. These two features ensure that the central line in the columnar region belongs to only a single neurite, which is crucial for separating densely packed neurites. Furthermore, we utilize the minimum volume covering ellipsoid to extract shape information of the columnar regions for constructing their connections. These designs enable PointTree to successfully reconstruct packed neurites. In contrast, skeleton-based local methods rely on determining the position of the next skeleton point based on the shape anisotropy of the region. This often leads to localization errors when there are two neurite image signals within a region (the middle panels of Figure 1E). When it comes to skeleton-based global methods, although seed points can be located at individual neurite centers, accurately constructing connections between these seed points proves challenging due to the reliance on distance between points and susceptibility to interference from densely distributed neurites (the right panels of Figure 1E).

### The merits of PointTree in dense reconstruction

In dense reconstruction, one of the main concerns is how well to separate densely distributed neurites that behave as crossover and closely paralleled neurites. These neurites can be manually identified by visualization with different view angles (Figure 2—figure supplement 1). We compared PointTree with several skeleton-based methods such as neuTube (Feng et al., 2015), PHDF (Radojevic and Meijering, 2017), NGPST (Quan et al., 2016), and MOST (Wu et al., 2014) in performing this task. We manually labeled the locations where neurites are crossover or closely parallel from five 256×256 × 256 image blocks. For a fair comparison, all methods are performed on segmented images derived from the segmentation network. Figure 2A illustrates the process of PointTree’s separation of crossover and closely paralleled neurites. PointTree can successfully separate the densely distributed neurites in a range of 71.4% and 91.7%, while these skeleton-based methods only separate 25.0% densely distributed neurites (Figure 2B) at most. We also present the comparison of PointTree and other methods on some reconstruction examples in which multi-crossover neurites (Figure 2C) and closely paralleled neurites are involved. PointTree provides the perfect reconstruction while other methods fail to reconstruct these neurites.

![Figure 2.](https://cdn.elifesciences.org/articles/102840/elife-102840-fig2-v1.jpg)

**Figure 2.:** (A) The reconstruction process of crossover and closely paralleled neurites. (B) Quantitative evaluation of PointTree and several skeleton-based methods on identifying closely distributed neurites. The box plots present the statistical information (n=5) in which the horizontal line in the box, the lower and upper borders of the box represent the median value, the first quartile (Q1), and the third quartile (Q3), respectively. The vertical black lines indicate 1.5 × IQR. (C) Three reconstruction examples derived from PointTree and several skeleton-based methods.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/102840/elife-102840-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** When the two parallel neurites are in close proximity, they can be distinguished by visualizing them from different angles.

Furthermore, we present the quantitative results derived from PointTree and five widely used skeleton-based reconstruction methods, including APP2, neuTube, NGPST, PHDF, and MOST. Eight 256×256 × 256 image blocks that include many densely distributed neurites are of the testing dataset. All reconstruction algorithms are performed on the segmentation images of these testing datasets. We give the intuitive reconstruction comparisons (Figure 3A). PointTree provides the reconstruction close to the ground truth. The skeleton-based methods generate lots of reconstruction errors and incorrectly combine multi-neurites into a single branch. The quantitative reconstructions suggest that PointTree is far superior to skeleton-based methods (Figure 3B). For PointTree, the average precision is above 90%, both recall and f1-score are above 85%. The skeleton-based methods cannot provide a good solution to separate the densely packed neurites. The f1-score of these reconstructions ranges from 30% to 40%, which indicates the ineffective reconstructions.

![Figure 3.](https://cdn.elifesciences.org/articles/102840/elife-102840-fig3-v1.jpg)

**Figure 3.:** (A) Comparison of reconstruction performance among six methods, including PointTree, NGPST, neuTube, APP2, PHDF, and MOST. Individual neurite branches are delineated in different colors. (B) Quantitative evaluation of reconstruction performance using precision, recall, and f1-score. The box plots display these three evaluation indexes (n=8). In the box, the horizontal line represents the median value. The box shows the interquartile range (IQR) from the first quartile (Q1) to the third quartile (Q3). The vertical lines indicate 1.5×IQR.

### Reconstruction of data with different signal-to-noise ratios

In the field of neuronal reconstruction, data acquired by different imaging systems often exhibit varying signal-to-noise ratio (SNR) characteristics. For some low-SNR datasets, severe noise interference makes it difficult even for human observers to accurately identify neurite structures. To systematically evaluate PointTree’s reconstruction performance across datasets with different SNRs, we selected and analyzed data from three imaging systems: light sheet microscopy (Stelzer et al., 2021) (LSM), fluorescent micro-optical sectioning tomography (Wang et al., 2021) (fMOST), and high-definition fluorescent micro-optical sectioning tomography (Zhong et al., 2021) (HD-fMOST), with SNR ranges of 2–7, 6–12, and 9–14, respectively (Figure 4A).

![Figure 4.](https://cdn.elifesciences.org/articles/102840/elife-102840-fig4-v1.jpg)

**Figure 4.:** (A) Data blocks from light sheet microscopy (LSM), fluorescent micro-optical sectioning tomography (fMOST), and high-definition fluorescent micro-optical sectioning tomography (HD-fMOST) are selected. SNR and corresponding reconstruction scores with PointTree are drawn with line charts. Each dataset is of sample size n=25 and each data block size of 128×128 × 128. (B) shows reconstruction performance of PointTree on different datasets. (C) The zoomed-in view displays the region marked by white box in the first column of (B), with 25 foreground points and 25 background points sampled respectively. The signal intensities of both the foreground points and background points are plotted in the adjacent line charts.

Experimental results demonstrate that, thanks to the powerful feature extraction capability of the deep learning network, the trained neural network achieves satisfactory segmentation performance (third row in Figure 4B) even on low-SNR data (first two columns in Figure 4B, top row), laying a solid foundation for subsequent accurate reconstruction (bottom row in Figure 4B). Quantitative analysis reveals that PointTree delivers stable reconstruction performance across all SNR levels. Specifically: for LSM data (sample size n=25, mean SNR = 5.01), average precision = 96.0%, recall = 88.7%, and f1-score=91.0%; for fMOST data (sample size n=25, mean SNR = 8.68), average precision = 95.8%, recall = 87.3%, and f1-score=90.0%; for HD-fMOST data (sample size n=25, mean SNR = 11.4), average precision = 98.1%, recall = 91.0%, and f1-score=93.3% (Figure 4A).

Notably, in low-SNR LSM data, background regions contain more artifactual signals (first panel in Figure 4C) due to similar intensity distributions between background and foreground points. In contrast, high-SNR datasets (fMOST and HD-fMOST) exhibit cleaner background features with distinct intensity separation between background noise and neurite signals (second and third panel in Figure 4C). This observation highlights the critical impact of SNR on reconstruction quality while simultaneously validating the robustness of PointTree, which is aided by the segmentation network, across diverse SNR conditions.

### Restrain error accumulation in the reconstruction

In order to achieve accurate axon reconstruction, it is essential to effectively suppress the snowballing accumulation of reconstruction errors. The performance of the minimal information flow tree (MIFT) in retraining the reconstruction errors is evaluated in this study. Figure 5A presents six 512×512 × 512 image blocks and their reconstructions using PointTree in the first column. The reconstruction fusing procedure is then performed on these axonal reconstructions (Figure 5A). By employing MIFT to revise the reconstructions and remove false connections between axons, reasonable reconstructions are achieved. In contrast, when the same fusion procedure is conducted without MIFT to revise the reconstruction, almost all axons are incorrectly connected together (bottom-right panel in Figure 5A).

![Figure 5.](https://cdn.elifesciences.org/articles/102840/elife-102840-fig5-v1.jpg)

**Figure 5.:** (A) Reconstruction comparisons in the fusion process with MIFT and without MIFT are shown. Both image blocks and neurite reconstructions are displayed using maximum projection along the z-direction. Two fusion procedures are performed, and the final fusion reconstructions are presented in the third column. (B) The variation in reconstruction accuracy during the fusion process with MIFT and without MIFT is illustrated. Blue points represent the initial reconstruction accuracy from six image blocks, while green points and red points denote the merged reconstruction accuracy with MIFT and without MIFT, respectively. The squares represent the mean values of the evaluation indexes. (C) The skeletons of three neurite branches from the final merged reconstructions with MIFT are shown. Additionally, corresponding ground-truth reconstructions and reconstruction evaluations are also presented.

We furthermore measure the enhancement in the reconstruction accuracy achieved by MIFT (Figure 5B). For the initial reconstructions from six image blocks, the average of f1-score is about 0.86. By using MIFT, the average of f1-score is above 0.8 for the reconstructions from two image blocks which are generated with the first fusion. In the second fusion (top-right panel in Figure 5A), the f1-score still keeps 0.79. In contrast, without MIFT, the first fusion leads to a drop of about f1-score of 0.3. After the second fusion, the f1-score is less than 0.2. We also present some reconstruction examples after two fusions in Figure 5C, which are close to the ground truth. These results suggest that the MIFT model takes consideration of the proper structure of axons and thus can restrain the error communications in the reconstruction fusion process.

### Long-range axonal projections reconstruction

We applied PointTree for long-range axon reconstruction. The testing image block has the size of 11226×8791 × 1486 voxels and includes axons from eight neurons (Figure 6A). We also used GTree to manually reconstruct these neurons as the ground-truth reconstruction (Figure 6B). Except for the labeling of training data for segmentation network and of the axon starting points of a single neuron, the whole reconstruction process is totally automatic. The results show PointTree successfully recovered the axonal morphology of these eight neurons without manual interference (Figure 6C and Videos 1 and 2), and we compared these reconstructions with ground truth (Figure 6—figure supplement 1). The average precision is above 85% and the average recall and f1-score are above 80% (Figure 6E). In addition, we presented the axon reconstructions from two image blocks (Figure 6C1 and C2) which include a large number of densely distributed axons. This reconstruction performance suggests that the point assignment and the minimal information flow tree mode, as the two key strategies in PointTree, perform well in long-range axonal reconstruction.

![Figure 6.](https://cdn.elifesciences.org/articles/102840/elife-102840-fig6-v1.jpg)

**Figure 6.:** (A) The image block contains eight neurons in the ventral posteromedial thalamic region. The projection of these neurons includes a large number of densely distributed axons, which are enlarged in A1 and A2. (B) The reconstruction of the eight neurons is achieved by annotators with semi-automatic software GTree, serving as ground-truth reconstruction to evaluate automatic algorithms. The reconstructions B1 and B2 correspond to the image blocks A1 and A2. (C) Automatic reconstruction with PointTree results in reconstructions of the densely distributed axons, which are enlarged in C1 and C2. (D) A comparison between automatic reconstruction and ground-truth reconstruction of axonal projection for one neuron is shown. Green indicates consistent reconstruction, blue indicates missed branches, and red denotes branches from other neurons. (E) Quantitative analysis of long-range projections for these neurons is presented. Statistical information is displayed in boxes (n=8), the horizontal line in the box, the lower and upper borders of the box represent the median value, the first quartile (Q1) and the third quartile (Q3) respectively, the vertical black lines indicate 1.5 × IQR, while black points represent the accuracy of the reconstructions for these neurons.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/102840/elife-102840-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** The reconstructions were performed using semi-automatic methods with manual modification (GTree, left column) and automatic methods (PointTree, right column). The semi-automatic reconstruction is considered the ground-truth reconstruction for quantifying the accuracy of the automatic reconstruction. In the right column, each panel includes a set of quantitative evaluation indexes in the bottom-right corner, which consist of precision, recall, and f1-score.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/102840/elife-102840-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** Axonal reconstructions were generated from the image blocks (10739×11226 × 3921) collected using the Limo system. The upper portion represents the ground-truth reconstruction, which includes data from 13 neurons. The automatic reconstruction (shown at the bottom) closely matches the ground-truth reconstruction. A quantitative evaluation of the automatic reconstruction is presented in Table 1.

![Video 1.](https://cdn.elifesciences.org/articles/102840/elife-102840-video1.mp4.jpg)

![Video 2.](https://cdn.elifesciences.org/articles/102840/elife-102840-video2.mp4.jpg)

We also applied PointTree to process another 10739×11226 × 3921 image blocks collected with HD-fMOST system (Zhong et al., 2021). The high signal-to-noise ratio in this optical system results in a significantly extended dynamic range of the signal. PointTree can effectively deal with this case, and all 14 long-range projections are successfully reconstructed (Figure 6—figure supplement 2). The quantitative results suggest that the average f1-score is above 90% (Table 1).

**Table 1.**
 Quantitative metrics comparing ground truth and reconstructed neurons are presented in Figure 6—figure supplement 2.


<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>F1-Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1.00</td>
      <td>0.92</td>
      <td>0.95</td>
    </tr>
    <tr>
      <td>2</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <td>3</td>
      <td>0.98</td>
      <td>0.76</td>
      <td>0.86</td>
    </tr>
    <tr>
      <td>4</td>
      <td>1.00</td>
      <td>0.82</td>
      <td>0.90</td>
    </tr>
    <tr>
      <td>5</td>
      <td>1.00</td>
      <td>0.77</td>
      <td>0.87</td>
    </tr>
    <tr>
      <td>6</td>
      <td>1.00</td>
      <td>0.92</td>
      <td>0.96</td>
    </tr>
    <tr>
      <td>7</td>
      <td>0.96</td>
      <td>0.75</td>
      <td>0.84</td>
    </tr>
    <tr>
      <td>8</td>
      <td>1.00</td>
      <td>0.87</td>
      <td>0.93</td>
    </tr>
    <tr>
      <td>9</td>
      <td>1.00</td>
      <td>0.82</td>
      <td>0.90</td>
    </tr>
    <tr>
      <td>10</td>
      <td>1.00</td>
      <td>0.96</td>
      <td>0.98</td>
    </tr>
    <tr>
      <td>11</td>
      <td>1.00</td>
      <td>0.99</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td>12</td>
      <td>1.00</td>
      <td>0.77</td>
      <td>0.87</td>
    </tr>
    <tr>
      <td>13</td>
      <td>1.00</td>
      <td>0.90</td>
      <td>0.95</td>
    </tr>
    <tr>
      <td>14</td>
      <td>0.99</td>
      <td>0.87</td>
      <td>0.93</td>
    </tr>
  </tbody>
</table>

Despite the need to solve multiple large-scale optimization problems, the reconstruction speed using PointTree is generally faster than the imaging speed. For instance, in a typical scenario involving 254 image blocks with 512×512 × 512 voxels, the total time required for reconstruction is approximately 44 min. Even for a larger dataset comprising 821 image blocks with 512×512 × 512 voxels and including a significant number of sparsely distributed neurites, the total time cost amounts to about 60 min (Table 2). It should be noted that the time cost does not increase linearly as data volume increases due to the influence of neurite density on overall reconstruction time. In summary, PointTree demonstrates remarkable speed in reconstructing long-range axons (Video 3).

**Table 2.**
 Time cost of three modules in the entire reconstruction for two testing datasets shown in Figure 6, Figure 6—figure supplement 2.


<table>
  <thead>
    <tr>
      <th>block number(size: 512×512 × 512)</th>
      <th>Points clustering(mins)</th>
      <th>Clusters connection(mins)</th>
      <th>Reconstruction merging (mins)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>254</td>
      <td>23</td>
      <td>18</td>
      <td>3</td>
    </tr>
    <tr>
      <td>821</td>
      <td>22</td>
      <td>35</td>
      <td>3</td>
    </tr>
  </tbody>
</table>

![Video 3.](https://cdn.elifesciences.org/articles/102840/elife-102840-video3.mp4.jpg)

## Discussion

We have presented an automated method for reconstructing the long-range projections of neurons. In this study, we address the problem of mutual interference among densely distributed neurites and the cumulative error during reconstruction by designing a reconstruction method based on point set assignment and the minimal information flow tree, respectively. As a result, our approach enables accurate reconstruction of long-range neuron projections from hundreds of gigabytes of data. This advance significantly enhances the efficiency of whole-brain-scale neuron reconstruction, bridging the substantial gap between factory-level generation of whole-brain-scale neuronal imaging data and tens of hours required to reconstruct one neuron.

Our approach is performed on image foregrounds where the segmented neurites have a fixed radius approximately equal to the total size of the three voxels. In this case, we can estimate the total number of foreground points (voxels) and set a suitable number of columnar regions for ensuring the anisotropy of each columnar region, which is based on the fact that the union of columnar regions equals the foreground region. The anisotropy of the columnar regions will reduce the difficulty in establishing their connection. The requirement that all segmented neurites have a relatively fixed radius can be fulfilled. For all neurites, the value of their voxels decreases as these voxels deviate from the nearest centerline. The deep learning network is able to grasp this feature and segment only the neurite centerline and its neighborhood. Typically, in reconstructions of neurons whose projections are distributed over hundreds to thousands of GBs of data, less than GB-sized images with labels are needed as training data. The labeling process takes a few hours, which is negligible for semi-automatic reconstruction of all neurons in the whole volume images.

We propose a new reconstruction mode centered on point set assignment instead of the current reconstruction mode focused on skeleton extraction. In the current reconstruction paradigm, most deep networks are used to enhance the signal-to-noise ratio of neuronal images and do not address the issue of signal interference during skeleton extraction. In contrast, our reconstruction approach is based on directly processing the foreground points generated by the deep learning network. With continued advances in deep learning techniques, the generality and accuracy of image segmentation will be continuously enhanced, thereby significantly boosting the application scope of our method in various scenarios. Essentially, our method can be applied to any skeleton tracking-based application scenario and effectively eliminate dense signal interference.

Our method still generates a few reconstruction errors. This is due to the following three aspects. First, our method directly handles image foregrounds, which leads to reconstruction errors when some neurites with weak image intensities are not identified. Second, relying solely on foreground point information and rule-based judgment methods may generate some connection errors when establishing connections between neurites. Finally, the minimal information flow tree’s fundamental assumption, that axons should be as smooth as possible, does not always hold true. In fact, real axons can take quite sharp turns (Figure 1—figure supplement 3) leading the algorithm to erroneously separate a single continuous axon into disjoint fibers (Figure 1—figure supplement 3). Therefore, for the automatic reconstruction of neurons on a brain-wide scale, further work is needed to enhance the imaging intensity and incorporate soma shapes and raw image signals for neurites connection recognition.

## Materials and methods

### Data collections

All animal experiments followed procedures approved by the Institutional Animal Ethics Committee of the Huazhong University of Science and Technology. The test datasets are collected through the preparation of two kinds of samples. For one C57BL/6 male mouse, 100 nl AAV-Cre virus and 100 nl of AAV-EF1α-DIO-EYFP virus were injected into the VPM nucleus at the same time. 21 days later, the chemical sectioning fluorescence tomography (CSFT) system (Wang et al., 2021) was used to acquire imaging data (Figures 1—6), more details can be seen in the reference (Zhang et al., 2021). For one C57BL/6 J male mouse, 100 nl of AAV-YFP was injected into the motor area. 21 days later, high-definition fluorescent micro-optical sectioning tomography (HD-fMOST) was used to acquire imaging data (Zhong et al., 2021; Figure 6—figure supplement 2).

### Generation of foreground points

Our reconstruction method performs on the image foregrounds. Here, we used UNet3D (Çiçek et al., 2016) for image stacks segmentation without network structure modification. The detailed information about UNet3D can be found in the reference (Çiçek et al., 2016). Considering the requirement that the network output, the segmented neurites, have the relatively fixed radius, we calculate the distance field of the neurite’s skeleton as the ground truth for supervising the network. Initially, the semi-automatic software GTree was utilized to extract the neurite skeleton and subsequently interpolate the skeleton points. The interpolation operation ensured that the distance between any skeleton point and its nearest point was less than 1 μm. Subsequently, the interpolated skeleton points were used as centers to mark spherical regions with a radius of 5 voxels. These spherical regions served as candidate areas for foreground. Within these candidate areas, the distance from each point to its nearest interpolated skeleton point was calculated. Finally, the distances are mapped into Gaussian kernel distances, which form the Gaussian density map. This map normalized by maximum value leads to the distance field map to supervise UNet3D output.

In the training stage, Adam optimizer is used with an initial learning rate at 3e-4. The input image size is 128×128 × 128. Batch size is set to 1, the L1-norm is used as loss function to train the network. We presented the reconstructions from two kinds of fMOST datasets. One is from the reference (Zhang et al., 2021) and the other is from the reference (Zhong et al., 2021). Therefore, we created two sets of training data, each consisting of 20 512×512 × 512 image blocks (each divided into 64 image blocks of size 128×128 × 128). In each set, 10 image blocks contain densely distributed neurites, while the other 10 blocks contain sparsely distributed neurites. In the predicting stage, we applied the threshold operation to the distance field image. The voxels whose values are more than 0.5 are regarded as the foreground points.

### Neuron Reconstruction based on Points assignment

For the image stack, we allocated the foreground points to their respective neurites and established connections between neurites by constructing three optimization models: (1) the constrained Gaussian mixture model divides the foreground points into a set of points, each of which has a column shape; (2) the minimum-volume covering ellipsoids model extracts the features of the column-shaped point set; (3) the 0–1 assignment optimization model establishes connections between the column-shaped point sets, resulting in the shapes of individual neurites, and then builds connections between the reconstructed neurites.

### Constrained Gaussian mixture model

The three-dimensional Gaussian function exhibits an ellipsoidal shape in space, which we have utilized to approximate the columnar shape of local neurites. In this study, Gaussian distribution mixture functions with $K$ components are employed to approximate the shape of all neurites in an image block. The component number $K$ is obtained by point density and will be discussed later. Given the foreground points $x_{1},x_{2},⋯,x_{n}$, for each foreground points $x_{i}$, the probability density function $P(x_{i})$ is calculated as follows:

$$
P(x_{i})=\sumj=1K\pi_{j}N(x_{i}|\mu_{j},Σ_{j})
$$

Here, $N(x_{i}|\mu_{j},Σ_{j})$ is the Gaussian density function with mean value $\mu_{j}$ and covariance matrix $Σ_{j}$. Weight $\pi_{j}$ is the regularization parameter. $N(x_{i}|\mu_{j},Σ_{j})$ is given by the formula:

$$
N(x_{i}|\mu_{j},Σ_{j})=\frac{1}{2\pi^{3/2}|Σ_{j}|^{1/2}}e^{−\frac{1}{2}(x_{i}−\mu_{j})^{T}Σ_{j}^{−1}(x_{i}−\mu_{j})}
$$

Based on probability density function, the conditional probability can be computed as:

$$
p_{i,j}=P(x_{i}|cluster_{j})=\frac{\pi_{j}N(x_{i}|\mu_{j},Σ_{j})}{\sumj=1K\pi_{j}N(x_{i}|\mu_{j},Σ_{j})}j=(1,2,...,K)
$$

Here, $p_{i,j}$ is the conditional probability for $x_{i}$ to assign to the j-th cluster. If $p_{i,k}$ is the maximum value among ${p_{i,1},...p_{i,K}}$, the foreground point $x_{i}$ will be assigned to the k-th cluster. All the points assigned to the k-th cluster form a columnar region. Considering that both the number of foreground points and component number are large, we have added some constrained conditions for Gaussian mixture model as follows:

$$
\sumj=1K\pi_{j}=1
$$



$$
I(\mu_{j})\geq\epsilon_{0},|Σ_{j}|\leq\epsilon_{1}
$$

$\sumj=1K\pi_{j}=1$ refers to the fact that the total probability distribution normalizes to 1. $I(⋅)$ represents the signal intensity from segment image, $\epsilon_{0}$ is the minimum signal intensity of foreground points and is set to 128 in the algorithm. $I(\mu_{i})\geq\epsilon_{0}$ restrain the center of the Gaussian distribution to be a foreground point. $|Σ_{j}|\leq\epsilon_{1}$ restrain the determinant of the covariance matrix which controls the suitable number of foreground points for each columnar region. $\epsilon_{1}$ is set to the cube of three times the average diameter of neurite.

Maximum likelihood is employed to estimate the parameters of Gaussian mixture model and the final optimization problem is formed as follows:

$$
(\pi_{j}^{∗},\mu_{j}^{∗},Σ_{j}^{∗})_{j=1,2,⋯,K}=arg⁡max\prodi=1nP(x_{i})=arg⁡max\prodi=1n(\sumj=1K\pi_{j}N(x_{i}|\mu_{j},Σ_{j}))
$$



$$
s.t.\sumj=1K\pi_{j}=1,I(\mu_{j})\geq\epsilon_{0},|Σ_{j}|\leq\epsilon_{1}
$$

In solving this optimization problem, we employ peak density algorithm (Wei et al., 2023) to compute density for each foreground points and sort them in descending order. We first select a point as a seed point, and the foreground points within a radius of 5 centered on it will be excluded. Then we continue selecting seed points until all foreground points are either selected or excluded. The selected $K$ seed points represent the initial $K$ components. We select signal points from the median (based on density) to both sides as seed points, which can decrease the situations that seed points lie in the center of a crossover or the edge of neurites. This strategy can make the generated columnar regions be more reasonable. The positions of the $K$ seed points are set to the initial $(\mu_{1},\mu_{2},⋯,\mu_{K})$. The initial setting of the covariance matrix is the identity matrix. The constrained Gaussian mixture model was solved by the EM algorithm (McLachlan and Krishnan, 2007), the EM algorithm is divided into two steps:

E-step: For each point $x_{i}$, compute its probability within each Gaussian distribution using the probability density function:

$$
p_{i,j}=\frac{\pi_{j}N(x_{i}|\mu_{j},Σ_{j})}{\sum_{j=1}^{K}\pi_{j}N(x_{i}|\mu_{j},Σ_{j})}
$$

M-step: Update the mean value, covariance matrices, and weight vectors.

$$
\pi_{j}=\frac{\sum_{i=1}^{n}p_{i,j}}{n}
$$



$$
\mu_{j}=\frac{\sum_{i=1}^{n}p_{i,j}x_{i}}{\sum_{i=1}^{n}p_{i,j}}
$$



$$
Σ_{j}=\frac{\sum_{i=1}^{n}p_{i,j}(x_{i}−\mu_{j})(x_{i}−\mu_{j})^{T}}{\sum_{i=1}^{n}p_{i,j}}
$$

Besides, the constrained Gaussian mixture model possesses additional constraints: $I(\mu_{j})\geq\epsilon_{0}$ and $|Σ_{j}|\leq\epsilon_{1}$. After finishing the M-step, $\mu_{j}$ with $I(\mu_{j})<\epsilon_{0}$ are selected. Eigenvalue decomposition is applied on $Σ_{j}$ and obtains eigenvalues $(\gamma_{1},\gamma_{2},\gamma_{3})$ in descending order and eigenvectors $(v_{1},v_{2},v_{3})$. $\mu_{j}$ is updated along $v_{1}$ and $−v_{1}$ to generate two new clusters with mean value and covariance matrices $(u_{j,1},Σ_{j,1})$ and $(u_{j,2},Σ_{j,2})$ as follows:

$$
u_{j,1}=u_{j}+v_{1}⋅\frac{\gamma}{2}
$$



$$
u_{j,2}=u_{j}−v_{1}⋅\frac{\gamma}{2}
$$



$$
Σ_{j,1}=\frac{\sumi=1np_{i,j}(x_{i}−\mu_{j,1})(x_{i}−\mu_{j,1})^{T}}{\sumi=1np_{i,j}}
$$



$$
Σ_{j,2}=\frac{\sumi=1np_{i,j}(x_{i}−\mu_{j,2})(x_{i}−\mu_{j,2})^{T}}{\sumi=1np_{i,j}}
$$

For $Σ_{j}>\epsilon_{1}$, it will be updated as follows:

$$
Σ_{j}^{′}=\frac{\epsilon_{1}}{Σ_{j}}Σ_{j}
$$

Iteration of E-step and M-step will continue until the k-th result ${\mu^{k},Σ^{k}}$ and (k-1)-th result satisfy the stopping criteria:

$$
‖\frac{u^{k}−u^{k−1}}{u^{k−1}}‖<\epsilonand‖\frac{Σ^{k}−Σ^{k−1}}{Σ^{k−1}}‖<\epsilon
$$

Here the division represents element-wise division and $‖·‖$ denotes $L_{2}$-norm and $\epsilon$ is set to 0.01.

### Shape characterization of columnar regions

After deriving the columnar regions through solving the constrained Gaussian mixture model, it is imperative to characterize their geometric shape (terminals and centerlines). For this purpose, we calculate the minimum-volume ellipsoids that can fully encompass each individual columnar region. For $c\inR^{3}$, $Q\inS_{++}^{3}$, a three-dimensional ellipsoid can be defined as follows Sun and Freund, 2004:

$$
E_{c,Q}:={x\inR^{3}|(x−c)^{T}Q(x−c)\leq1}
$$

Here, $c$ is the center of ellipsoid, $Q$ represents the geometric shape, $S_{++}^{3}$ denotes the convex cone of 3×3 symmetric positive definite matrices. The volume of $E_{c,Q}$ is given by the formula:

$$
Volume(E_{c,Q})=\frac{\pi^{3/2}}{Γ(3/2+1)}\frac{1}{\sqrt{det(Q)}}
$$

Here, $Γ(⋅)$ is the standard gamma function of calculus, $det(Q)$ means the determinant of matrix Q. Minimizing the volume of $E_{c,Q}$ is equivalent to minimizing $det(Q^{−1/2})$. Therefore, for a columnar region with foreground points $P{x_{1},x_{2},…x_{m}}$, we define the target function as follows:

$$
P1:(c^{∗},Q^{∗})=arg⁡min_{c,Q}det(Q^{−1/2})
$$



$$
s.t.(x_{i}−c)^{T}Q(x_{i}−c)\leq1,i=1,2...m
$$



$$
c\inCHull(P),Q\inS_{++}^{3}
$$

Here $c\inCHull(P_{i})$ restrain the solved center of ellipsoid to locate within the smallest convex hull formed by the clustering points. To solve this problem, a variable substitution $A=Q^{1/2}$ and $y=Q^{1/2}c$ were applied to Equation 20 and Equation 21, the original problem P1 can be transformed into a convex optimization problem as follows:

$$
P2:(A^{∗},y^{∗})=arg⁡minA,y-lndet(A)
$$



$$
s.t.(Ax_{i}−y)^{T}(Ax_{i}−y)\leq1,i=1,2,...,m
$$



$$
A\inS_{++}^{3}
$$

Through adding the logarithmic barrier function, we can obtain the following formula:

$$
P3:(A^{∗},y^{∗},\theta^{∗})=arg⁡minA,y,\theta-lndet(A)−\theta\sumi=1mln⁡(z_{i})
$$



$$
s.t.(Ax_{i}−y)^{T}(Ax_{i}−y)+z_{i}=1,i=1,2,...,m
$$



$$
A\inS_{++}^{3},z_{i}>0
$$

As $\theta$ varies in the interval $(0,∞)$, the solution of $P3$ changes. When $\theta$ approaches 0, the optimal solution of $P3$ tends to the optimal solution of $P2$. By adding the dual multipliers $d_{i}$ which satisfies $d_{i}⋅z_{i}=\theta$, the optimality conditions can be written as:

$$
\sumi=1md_{i}[(Ax_{i}−y)x_{i}^{T}+x_{i}(Ax_{i}−y)^{T}]−A^{−1}=0
$$



$$
\sumi=1md_{i}(y−Ax_{i})=0
$$



$$
(Ax_{i}−y)^{T}(Ax_{i}−y)+z_{i}=1i=1,2,...,m
$$



$$
\sumi=1md_{i}⋅z_{i}=\theta,i=1,2,...,m
$$



$$
d_{i},z_{i}\geq0
$$

At this point, the error between the solution of the system of equations and the optimal solution of $P3$ is less than $d^{T}z$. Through Equation 30, the explicit expression for solving $y$ can be obtained as follows:

$$
y=\frac{AXd}{e^{T}d}
$$

Here, $X$ stands for a $3\timesm$ matrix $[x_{1}|x_{2}|...|x_{m}]$, $e$ stands for vector of ones $(1,1,...,1)_{1\timesm}^{T}$ and $d$ stands for $(d_{1},d_{2},...,d_{m})_{1\timesm}^{T}$. Substitute Equation 34 into Equation 29, the equation for matrix $A$ can be obtained by:

$$
(XDX^{T}−\frac{Xdd^{T}X^{T}}{e^{T}d})A+A(XDX^{T}−\frac{Xdd^{T}X^{T}}{e^{T}d})=A^{−1}
$$

Here, $D$ stands for a $m\timesm$ diagonal matrix $Diag(d_{1},d_{2},...,d_{m})$. And the explicit expression for $A$ is formed as

$$
A=A(d)=[2(XDX^{T}−\frac{Xdd^{T}X^{T}}{e^{T}d})]^{−1/2}
$$

And explicit expression for $y$:

$$
y=\frac{[2(XDX^{T}−\frac{Xdd^{T}X^{T}}{e^{T}d})]^{−1/2}Xd}{e^{T}d}
$$

Through substituting the above two equations to the system of Equations 29-33, variables A and y are eliminated. The following system of equations with only variables d and z can be obtained:

$$
f(d)+z−e=0
$$



$$
Dz−\thetae=0
$$



$$
d_{i},z_{i}\geq0
$$

Here, $f(d)$ is nonlinear function of variable $d$:

$$
f_{i}(d)=(x_{i}−\frac{Xd}{e^{T}d})[2(XDX^{T}−\frac{Xdd^{T}X^{T}}{e^{T}d})]^{−1}⋅(x_{i}−\frac{Xd}{e^{T}d})i=1,2,...,m
$$

For a fixed barrier parameter $\theta$, we employ Newton’s method to solve the system of equations. We use $\nabla_{d}f(d)$ to represent the Jacobian matrix of $f(d)$. Thus, the Jacobian matrix of the system of equations can be computed as follows:

$$
[∇_{d}f(d)IZD]
$$

And the Newton’s direction is written as:

$$
Δ(d)=(\nabla_{d}f(d)−D^{−1}Z)^{−1}(h_{1}−D^{−1}h_{2})
$$



$$
Δ(z)=D^{−1}h_{2}−D^{−1}Z(\nabla_{d}f(d)−D^{−1}Z)^{−1}(h_{1}−D^{−1}h_{2})
$$



$$
h_{1}=e−z−f(d),h_{2}=\thetae−Dz
$$

With initial $(d_{0},z_{0})$, iterate with $(d_{n},z_{n})=(d_{n−1},z_{n−1})+\beta~(Δ(d_{n−1}),Δ(z_{n−1}))$ to obtain the final optimal solution, $\beta~$ represents the Newton’s step. Detailed process can see the pseudo code as follows:

<table>
  <thead>
    <tr>
      <th>Algorithm 1. Compute Newton’s direction.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Input: (d,z,θ)\begin{document}$\left (d,z,\theta \right)$\end{document} satisfying d,z&gt;0\begin{document}$d,z \gt 0$\end{document}, θ≥0\begin{document}$\theta\geq 0$\end{document}1. A−2(d)=[2(XDXT−XddTXTeTd)]\begin{document}$A^{- 2}\left (d\right)=\left [2\left (XDX^{T}- \frac{Xdd^{T}X^{T}}{e^{T}d}\right)\right ]$\end{document}2. Σ(d)=(X−XdeTeTd)A2(d)(X−XdeTeTd)\begin{document}$\Sigma \left (d\right)=\left (X- \frac{Xde^{T}}{e^{T}d}\right)A^{2}\left (d\right)\left (X- \frac{Xde^{T}}{e^{T}d}\right)$\end{document}3 ∇df(d)=−2(Σ(d)eTd+Σ(d)∘Σ(d))\begin{document}$\nabla _{d}f\left (d\right)=- 2\left (\frac{\Sigma \left (d\right)}{e^{T}d}+\Sigma \left (d\right)\circ \Sigma \left (d\right)\right)$\end{document}4. (Δ(d),Δ(z))=((∇df(d)−D−1Z)−1(h1−D−1h2),D−1h2−D−1ZΔ(d))\begin{document}$\left (\Delta \left (d\right),\Delta \left (z\right)\right)=\left (\left (\nabla _{d}f\left (d\right)- D^{- 1}Z\right)^{- 1}\left (h_{1}- D^{- 1}h_{2}\right), D^{- 1}h_{2}- D^{- 1}Z\Delta \left (d\right)\right)$\end{document}Output: (Δ(d),Δ(z))\begin{document}$(\Delta (d),\Delta (z))$\end{document}</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Algorithm 2. Process of solving P2.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Input: {x1,x2,...,xm}\begin{document}$\left \{x_{1}, x_{2},...,x_{m}\right \}$\end{document}1. r=0.99\begin{document}$r=0.99$\end{document}, (d0,z0)=(32me,e−f(d0))\begin{document}$\left (d_{0},z_{0}\right)=\left (\frac{3}{2m}e,e- f\left (d_{0}\right)\right)$\end{document}2.E=−det(A(d))\begin{document}$E=- \det \left (A\left (d\right)\right)$\end{document}3. while (|e−f(d)−z|&gt;ε1\begin{document}$\left|e- f\left (d\right)- z \right| \gt \varepsilon _{1}$\end{document} or dTzE&gt;ε2\begin{document}$\frac{d^{T}z}{E} \gt \varepsilon _{2}$\end{document})4.   θ=dTz10m\begin{document}$\theta =\frac{d^{T}z}{10m}$\end{document}5.  (Δ(d),Δ(z))\begin{document}$\left (\Delta \left (d\right),\Delta \left (z\right)\right)$\end{document} = Compute_Newton_direction (d,z)\begin{document}$\left (d,z\right)$\end{document}6.  β¯=max{β|(d,z)+β(Δ(d),Δ(z)≥0)}\begin{document}$\bar{\beta }=\max \left \{\beta \left|\left (d,z\right)+\beta \left (\Delta \left (d\right),\Delta \left (z\right)\geq 0\right)\right\}\right.$\end{document}7.  β~=min(rβ¯,1)\begin{document}$\tilde{\beta }=\min \left (\bar{r\beta },1\right)$\end{document}8.  (d,z)=(d,z)+β~(Δ(d),Δ(z))\begin{document}$\left (d,z\right)=\left (d,z\right)+\tilde{\beta }\left (\Delta \left (d\right),\Delta \left (z\right)\right)$\end{document}9.  E=−det(A(d))\begin{document}$E=- \det \left (A\left (d\right)\right)$\end{document}Output: Q=A(d)2,c=A(d)−1y(d)\begin{document}$Q=A\left (d\right)^{2},{c=A}\left (d\right)^{- 1}y\left (d\right)$\end{document}</td>
    </tr>
  </tbody>
</table>

With the solved optimal solution of $(Q,c)$, we then check whether $c$ is located within the convex hull of the input point set ${x_{1},x_{2},...,x_{m}}$. If it is not, a constrained Gaussian mixture model will be applied to partition it into two subsets and solve the minimum-volume covering ellipsoids problem again in the two subsets. Through solving the above minimum-volume covering ellipsoids problem, we can characterize the columnar regions more accurately.

Note that from constrained GMM, each cluster has the corresponding mean and covariance matrix of points in the cluster. These two values essentially describe the shape of the cluster. However, if these two values directly replace $c^{*}$ and $Q^{*}$, the exported ellipsoid may only encompass a part of points in the cluster. For covering all points in the cluster, all elements in the covariance matrix are needed to be proportionally enlarged, but the volume of the corresponding ellipsoid is not minimum. These two cases will reduce the accuracy of the connections between clusters, that is columnar regions. So, we introduce the minimum-volume covering ellipsoid model to extract the shape of columnar region.

### Skeleton generation using 0-1 assignment model

The 0–1 assignment model (Volgenant, 1996) can robustly and accurately establish connections between particles in live-cell imaging (Jaqaman et al., 2008). It is particularly effective in handling cases where particles are densely distributed, merged, or split. We analogize column regions to particles and apply the 0–1 assignment model to build the connections between column regions. For the i-th columnar region, the center and the two endpoints of the longest axis of its minimum-volume covering ellipsoid are denoted by $c_{i},t_{i,0},t_{i,1}$. The direction refers to the pointing of the center point towards $t_{i,k}$, k equal to 0 or 1. According to the direction and the endpoints, we design the cost matrix for building the 0–1 assignment model.

$$
C=[c(t_{1,0},t_{1,0})c(t_{1,0},t_{1,1})⋯c(t_{1,0},t_{n,1})c(t_{1,1},t_{1,0})c(t_{1,1},t_{1,1})⋯c(t_{1,1},t_{n,1})D⋮⋮⋮⋮c(t_{n,1},t_{1,0})c(t_{n,1},t_{1,1})⋯c(t_{n,1},t_{n,1})DD]_{4n\times4n}
$$



$$
c(t_{i,i0},t_{j,j0})={100if(i=j)\frac{norm(t_{i,i0},t_{j,j0})}{(0.5\times(\frac{\theta(t_{i,i0},t_{j,j0})}{3}+1.001))^{4}}if(i\neqj)
$$



$$
\theta(t_{i,i0},t_{j,j0})=⟨dir(c_{i},t_{i,i0}),dir(c_{i},t_{j,j0})⟩+⟨dir(c_{j},t_{j,j0}),dir(c_{j},t_{i,i0})⟩−⟨dir(c_{i},t_{i,i0}),dir(c_{j},t_{j,j0})⟩
$$

Here, D is 2n×2n auxiliary matrix all elements of which are all set 100. Both $i0$ and $j0$ in Equation 47 are equal to 0 or 1, labeling the two endpoints of the longest axis of the ellipsoid. $norm(t_{i,i0},t_{j,j0})$ represents the Euclidean distance between $t_{i,i0}$ and $t_{j,j0}$. $\theta(t_{i,i0},t_{j,j0})$ describes the angle between two ellipsoids, that is two columnar regions. $dir(c_{i},t_{i,i0})$ represents the line from point $c_{i}$ to $t_{i,i0}$. $〈dir(c_{i},t_{i,i0}),dir(c_{i},t_{j,j0})〉$ represents cosine angle between the two lines. The threshold of 100 in D in Equation 46 and Equation 47 is an experimental value designed to ensure that the terminal points of neurites do not connect to more than one other terminal point.

After setting the cost matrix, the 0–1 assignment problem is defined as follows:

$$
A=argmin_{A}\sumi=14n\sumj=14nA_{ij}C_{ij}
$$



$$
s.t.\sumi=14nA_{i,j}=1(j=1,2,⋯,4n)
$$



$$
\sumj=14nA_{i,j}=1(i=1,2,⋯,4n)
$$

Here, $A$ represents the connectivity matrix between different terminals of columnar regions: if $A_{i,j}=1$, then establish connection between terminal $i$ and terminal $j$, if $A_{i,j}=0$, then establish no connection between terminal $i$ and terminal $j$.$\sumi=14nA_{i,j}=1(j=1,2,⋯,4n)$ and $\sumj=14nA_{i,j}=1(i=1,2,⋯,4n)$ restrain each terminal from establishing connection with at most one other terminal. The Lapjv algorithm (Volgenant, 1996) is utilized to solve this optimization problem and the shapes of individual neurites in block images are formed. Furthermore, we employ the region growing method to generate skeletons from the reconstructed shape, achieving the neurites reconstruction from individual image blocks.

### Minimal information flow tree for revising the reconstruction

The minimal information flow tree model is designed to modify the topology of skeletons, eliminate incorrect connections, and decompose them into multiple branches. When given an input skeleton file such as the swc file (Cannon et al., 1998), we convert it into a binary tree structure with the following steps.

#### Step 1

select the neurite skeleton $S_{1}$. $S_{1}$ has the largest length in the neurite skeletons that connect with each other. One of its terminal nodes is recorded as the head node $n_{1}$.

#### Step 2

generate the initial tree structure. Starting at head node $n_{1}$, search the linking nodes along the skeleton $S_{1}$, denoted by $n_{1}^{s_{1}},n_{2}^{s_{1}},⋯,n_{k_{1}}^{s_{1}}$. The topology structure is $n_{i}→leftnode=n_{i+1}^{s_{1}}$.

#### Step 3

generate new structure induced by the linking node $n_{1}^{s_{1}}$. $n_{1}^{s_{1}}$ is regarded as the head node and its corresponding neurite skeleton is denoted by $S_{2}$. Let $n_{1}^{s_{2}},n_{2}^{s_{2}},⋯,n_{k_{2}}^{s_{2}}$ represent the linking nodes in skeleton $S_{2}$. The corresponding topology structure is $n_{1}^{s_{1}}→rightnode=n_{1}^{s_{2}}$, $n_{i}^{s_{2}}→leftnode=n_{i+1}^{s_{2}}$.

#### Step 4

repeat the operation in Step 3 for dealing with the linking nodes $n_{2}^{s_{1}},⋯,n_{k_{1}}^{s_{1}}$. The corresponding topology structures are added into the total tree structure. After obtaining the tree structures induced by linking nodes in $S_{1}$, use the operation in Step 3 to generate the tree structures induced by linking nodes in $S_{2}$. Continue in this manner until all linking nodes have been processed.

To gain a better understanding of the above process, we have provided a demonstration of how to generate the corresponding binary tree from the skeletons of neurites (Figure 1—figure supplement 4).

For the skeletons of neurites in an image block, the corresponding number of binary tree structures will be generated. We use the MIFT model to merge or split these binary structures. Suppose that an image stack contains $m$ skeletons all of which have K nodes, denoted by $n_{1},⋯,n_{K−1},n_{K}$. The connections among these nodes are stored in a matrix $W$ with $K\timesK$ elements. $W_{i,j}=0$ indicates that there is no connection between node $i$ and node $j$. $W_{i,j}=−1$ indicates that $j→headnode=i$, $W_{i,j}=−2$ indicates that $j→leftnode=i$, $W_{i,j}=−3$ indicates that $j→rightnode=i$.

The information flow can be computed as follows:

$$
W^{∗}=argmin_{W}\sumi=1Kf(W,n_{i})
$$



$$
f(W,n_{i})=cos(\theta(n_{i}→headnode,n_{i},n_{i}→leftnode))
$$

Here, the optimization objective function in Equation 53 is called information flow. $\theta(⋅)$ is the angle between flow from $n_{i}→headnode$ to $n_{i}$ and flow from $n_{i}$ to $n_{i}→leftnode$. To minimize the optimization problem while ensuring that the topology matrix $W$ does not exhibit abnormal values, we adopt the strategy of dynamic programming to update the topology matrix $W$. Briefly, we calculate the other two possible angles $\theta(n_{i}→headnode,n_{i},n_{i}→rightnode)$ and $\theta(n_{i}→leftnode,n_{i},n_{i}→rightnode)$ at the first linking node $n_{i}$. The minimum information flow is selected, and $W$ is updated. Following the updated $W$, the next branching node is found and information flow and $W$ is updated. The updating process iterates until all nodes are updated. The final root nodes ${r_{1},r_{2},...,r_{m}}$ are obtained (node satisfies $W(r_{t},i)=0or−1(i=1,...n)$ is set root node). The pseudo-code for solving the optimization problem is provided below:

<table>
  <thead>
    <tr>
      <th>Algorithm 3. Generation of Minimal Information Flow Tree.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td># Graph defines tree topology of the nodes, t_node-&gt;left represents the left child node of t_node, t_node-&gt;right represents the right child node of t_node, t_node-&gt;head represents the head node of t_node.Input: N: {N0,N1,...,Nk}\begin{document}$\left \{N_{0},N_{1},...,N_{k}\right \}$\end{document}, Graph head: {N0}\begin{document}$\left \{N_{0}\right \}$\end{document}    Set={N0}\begin{document}$Set=\left \{N_{0}\right \}$\end{document}    While |Set|&gt;0\begin{document}$|Set| \gt 0$\end{document}:      t_node=Set[0]\begin{document}$t\_ node=Set\left [0\right ]$\end{document}      # calculate three possible information flow      res=calc_three_directions(t_node)\begin{document}$res=calc\_ three\_ directions\left (t\_ node\right)$\end{document}      if (res==0)\begin{document}$\left (res==0\right)$\end{document}:      # maintain original structure.        Set[0]=t_node−&gt;left\begin{document}$Set\left [0\right ]=t\_ node- \gt left$\end{document}       Set.push_back(t_node−&gt;right)\begin{document}$Set.push\_ back\left (t\_ node- \gt right\right)$\end{document}      if (res==1)\begin{document}$\left (res==1\right)$\end{document}:      # change the position of t_node’s two child nodes.       Exchange_child(t_node)\begin{document}$Exchange\_ child\left (t\_ node\right)$\end{document}       Set[0]=t_node−&gt;left\begin{document}$Set\left [0\right ]=t\_ node- \gt left$\end{document}       Set.push_back(t_node−&gt;right)\begin{document}$Set.push\_ back\left (t\_ node- \gt right\right)$\end{document}      if (res==2)\begin{document}$\left (res==2\right)$\end{document}:      # Information flows from t_node-&gt;left to t_node-&gt;right, update the structure along t_node-&gt;left and t_node-&gt;head, generate new head if possible.        New_node=Reverse_head(t_node)\begin{document}$New\_ node=Reverse\_ head\left (t\_ node\right)$\end{document}        Set[0]=New_node\begin{document}$Set\left [0\right ]=New\_ node$\end{document}Output: N: {N0,N1,...,Nk}\begin{document}$\left \{N_{0},N_{1},...,N_{k}\right \}$\end{document}, Graph head: {N0′,N1′,...,Nm′}\begin{document}$\left \{N_{0}^{'},N_{1}^{'},...,N_{m}^{'}\right \}$\end{document}.</td>
    </tr>
  </tbody>
</table>

Please note that the model has the capability to merge binary trees. When two branches of neurites have identifiable root nodes, and one root node is in close proximity to the skeleton points on the other branch of neurites, the root node does not contribute to the calculation of information flow without fusion. However, after fusion, the root node becomes a linking node in the other branch of neurites, resulting in an additional negative information flow value. In this merging process, a threshold is required to be set. When the minimum distance between the root node of a branch of neurites and the skeleton point of the other branch of neurites is less than 8 for individual image blocks or less than 8,12,16 for fused image blocks respectively, these two branches are merged. When splitting a branch of neurites, the minimal information flow tree model is also applied to both individual and fused image blocks.

### The fusion of neurites reconstruction

By using the MIFT model to revise the neurites reconstruction in individual image blocks, the root nodes and leaf nodes of a branch of neurites can be extracted directly. Here, we use a 0–1 assignment model to merge the reconstructions between two adjacent image blocks. For two adjacent image blocks $P$ and $Q$, the neurite skeleton nodes which locate near the common boundary are extracted as ${p_{1},p_{2},...p_{m}}$, ${q_{1},q_{2},...q_{n}}$ and the cost matrix is constructed as follows:

$$
C=[c(p_{1},q_{1})⋯c(p_{1},q_{n})⋮⋱⋮c(p_{m},q_{1})⋯c(p_{m},q_{n})D_{m\timesm}D_{n\timesn}D_{n\timesm}]_{(m+n)\times(m+n)}
$$



$$
c(p_{i},q_{j})=d(p_{i},q_{j})\times(2−\theta(L(p_{i}),L(q_{j})))
$$

Here, $D_{m\timesm}$, $D_{n\timesn}$, $D_{n\timesm}$ are auxiliary matrix which the values are all set 20. $d(p_{i},q_{j})$ represents the Euclidean distance between terminal $p_{i}$ and $q_{j}$. $L(p_{i})$ and $L(q_{j})$ are fitted lines from the skeleton points near $p_{i}$ and $q_{j}$. $\theta(L(p_{i}),L(q_{j}))$ represents the cosine value of their angle. Thus, the 0–1 assignment problem is formed as follows:

$$
A=argmin_{A}\sumi=1m+n\sumj=1m+nA_{i,j}⋅C_{i,j}
$$



$$
s.t.\sumi=1m+nA_{i,j}=1(j=1,2,…m+n)
$$



$$
\sumj=1m+nA_{i,j}=1(i=1,2,…m+n)
$$

Here, $A$ represents the connectivity relationship between nodes, if $A_{i,j}=1$, there is connection between block $P$’s node $i$ and block $Q$’s node $j$, if $A_{i,j}=0$, there is no connection between block $P$’s node $i$ and block $Q$’s node $j$. $\sumi=1m+nA_{i,j}=1(j=1,2,…m+n)$ and $\sumj=1m+nA_{i,j}=1(i=1,2,…m+n)$ restrict each node to connect to one other node at most. With the solved matrix $A$, the neurite skeletons of adjacent blocks can be merged and fused skeleton structures can be obtained.

### Statistical analysis

In this study, three commonly used metrics defined in Quan et al., 2016 were used, including precision, recall, and f1-score, which are computed to measure the fidelity between the reconstruction results and the ground truth. They are defined as follows:

$$
precision(R,G)=\frac{|R∩G|}{|R|}=\frac{|TP|}{|R|}
$$



$$
recall(R,G)=\frac{|R∩G|}{|G|}=\frac{|TP|}{|G|}
$$



$$
f1−score(R,G)=2⋅\frac{precision\timesrecall}{precision+recall}
$$

$R$ represents the point set of reconstructed neurons, $G$ represents the point set of the ground truth, $|⋅|$ represents the number of points of a set. The three metrics are first computed on each individual neuron and then averaged by weighting each neuron with its point number of its ground truth neuritis.

We also calculated the signal-to-ratio (SNR) of the data using the following method: For a given data block $B$ and its corresponding ground-truth skeleton $S$, we first densify the skeleton $S$ by using linear interpolation to ensure that the Euclidean distance between adjacent skeleton points is less than 1 voxel. Next, we expand each skeleton point in the densified skeleton $S^{`}$ into a spherical mask with a radius of 3 voxels. The resulting region serves as the foreground $mask$. Finally, SNR is computed with mean intensity of foreground points and standard deviation of background points as follows:

$$
Mean_{foreground}=\sumx\inBI(x)\times\sigma_{1}(x)/\sumx\inB\sigma_{1}(x)
$$



$$
Mean_{background}=\sumx\inBI(x)\times\sigma_{2}(x)/\sumx\inB\sigma_{2}(x)
$$



$$
Std_{background}=\sqrt{\sumx\inB(I(x)−Mean_{background})^{2}\times\sigma_{2}(x)/\sumx\inB\sigma_{2}(x)}
$$



$$
\sigma_{1}(x)={1if(x\inS^{′})0if(x∉S^{′})
$$



$$
\sigma_{2}(x)={1if(x∉mask)0if(x\inmask)
$$

Here, $I(x)$ represents the signal intensity of the voxel at position $x$, the SNR is calculated by $Mean_{foreground}$ and $Std_{background}$ by the following formula:

$$
SNR=10log_{10}(Mean_{foreground}/Std_{background})
$$

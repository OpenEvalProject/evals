# Olfactory responses of Drosophila are encoded in the organization of projection neurons

## Authors

- Kiri Choi<sup>1</sup> ([ORCID: 0000-0002-0156-8410](https://orcid.org/0000-0002-0156-8410)) †
- Won Kyu Kim<sup>1</sup> ([ORCID: 0000-0002-6286-0925](https://orcid.org/0000-0002-6286-0925)) †
- Changbong Hyeon<sup>1</sup> ([ORCID: 0000-0002-4844-7237](https://orcid.org/0000-0002-4844-7237)) †

### Affiliations

1. School of Computational Sciences, Korea Institute for Advanced Study Seoul Republic of Korea ([ROR:041hz9568](https://ror.org/041hz9568))

† Corresponding author

## Abstract

The projection neurons (PNs), reconstructed from electron microscope (EM) images of the Drosophila olfactory system, offer a detailed view of neuronal anatomy, providing glimpses into information flow in the brain. About 150 uPNs constituting 58 glomeruli in the antennal lobe (AL) are bundled together in the axonal extension, routing the olfactory signal received at AL to mushroom body (MB) calyx and lateral horn (LH). Here we quantify the neuronal organization in terms of the inter-PN distances and examine its relationship with the odor types sensed by Drosophila. The homotypic uPNs that constitute glomeruli are tightly bundled and stereotyped in position throughout the neuropils, even though the glomerular PN organization in AL is no longer sustained in the higher brain center. Instead, odor-type dependent clusters consisting of multiple homotypes innervate the MB calyx and LH. Pheromone-encoding and hygro/thermo-sensing homotypes are spatially segregated in MB calyx, whereas two distinct clusters of food-related homotypes are found in LH in addition to the segregation of pheromone-encoding and hygro/thermo-sensing homotypes. We find that there are statistically significant associations between the spatial organization among a group of homotypic uPNs and certain stereotyped olfactory responses. Additionally, the signals from some of the tightly bundled homotypes converge to a specific group of lateral horn neurons (LHNs), which indicates that homotype (or odor type) specific integration of signals occurs at the synaptic interface between PNs and LHNs. Our findings suggest that before neural computation in the inner brain, some of the olfactory information are already encoded in the spatial organization of uPNs, illuminating that a certain degree of labeled-line strategy is at work in the Drosophila olfactory system.

## Introduction

Anatomical details of neurons obtained based on a full connectome of the Drosophila hemisphere reconstructed from electron microscope (EM) image datasets (Bates et al., 2020; Scheffer et al., 2020) offer the wiring diagram of the brain, shedding light on the origin of brain function. Out of the immense amount of data, we study the second-order neurons, known as the projection neurons (PNs) of the olfactory system. It is the PNs that bridge the olfactory receptor neurons (ORNs) in the antenna and maxillary palp to higher olfactory centers where neural computation occurs for Drosophila to sense and perceive the environment (Hallem and Carlson, 2004a). The three neuropils, namely the antennal lobe (AL), mushroom body (MB) calyx, and lateral horn (LH), are the regions that abound with an ensemble of axonal branches of PNs and synapses (Figure 1). PNs can be classified as uniglomerular and multiglomerular PNs based on their structure and connectivity to other PNs. The uniglomerular PNs (uPNs) in AL constitute glomeruli that collect olfactory signals from ORNs of the same receptor type (Gao et al., 2000; Couto et al., 2005). uPNs innervating MB calyx and LH relay the signals further inside the brain through synaptic junctions with the Kenyon cells (KCs) and lateral horn neurons (LHNs), respectively. Multiglomerular PNs (mPNs), on the other hand, innervate multiple glomeruli, often contributing to the inhibitory regulation of signals relayed from ORNs to third-order olfactory neurons (Berck et al., 2016). PNs can functionally be categorized into either excitatory (cholinergic) or inhibitory (GABAergic), where a many GABAergic PNs tend to bypass MB calyx while innervating multiple glomeruli in AL (and hence are mPNs) (Schultzhaus et al., 2017; Shimizu and Stopfer, 2017).

![Figure 1.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig1-v2.jpg)

**Figure 1.:** uPNs comprising each glomerulus in AL collect input signals from ORNs of the same receptor type and relay the signals to MB calyx and LH. uPNs in MB calyx synapse onto KCs; and uPNs in LH synapse onto LHNs.

Since the seminal work by Cajal, 1911, who recognized neurons as the basic functional units of the nervous system, there have been a series of attempts at classifying neurons using different representations of neuronal morphologies and at associating the classified anatomies with their electrophysiological responses and functions (Uylings and van Pelt, 2002; Scorcioni et al., 2008; Jefferis et al., 2007; Seki et al., 2010; Gillette and Ascoli, 2015; Lu et al., 2015; Li et al., 2017; Kanari et al., 2018; Mihaljević et al., 2018; Gouwens et al., 2019; Laturnus et al., 2020). Systematic and principled analyses of neuronal anatomy would be a prerequisite for unveiling a notable link between the PN organization and olfactory representations. Several different metrics involving spatial projection patterns (Jefferis et al., 2007), electrophysiological properties (Seki et al., 2010; Gouwens et al., 2019), topological characteristics (e.g. morphometrics) (Uylings and van Pelt, 2002; Scorcioni et al., 2008; Lu et al., 2015; Mihaljević et al., 2018; Gouwens et al., 2019), intersection profiles (Gouwens et al., 2019), and NBLAST scores (Jeanne et al., 2018; Zheng et al., 2018; Bates et al., 2020; Scheffer et al., 2020) have been utilized in the past. More recently, machine learning approaches have been popularized as a tool for classification tasks (Vasques et al., 2016; Buccino et al., 2018; Mihaljević et al., 2018; Zhang et al., 2021).

Among a multitude of information that can be extracted from the neural anatomy associated with uPNs, the inter-PN organization draws our attention. To compare spatial characteristics of uPNs across each neuropil and classify them based on the odor coding information, we confine ourselves to uPNs innervating all three neuropils, most of which are cholinergic and follow the medial antennal lobe tract (mALT). Within this scope, we first calculate inter-PN distance matrices in each neuropil and study them in reference to the glomerular types (homotypes) to discuss how the inter-PN organization changes as the PNs extend from AL to MB calyx and from AL to LH.

In this study, we utilize two representative EM-based reconstruction datasets for the analysis (the latest FAFB Bates et al., 2020 and the hemibrain datasets Scheffer et al., 2020). The FAFB dataset specifically encompasses the Drosophila olfactory system, while the hemibrain dataset aims for a reconstruction of the entire right hemisphere of the Drosophila brain. The results based on the two datasets are largely consistent and interchangeable, which generalizes our findings.

We have conducted statistical analyses to unravel potential associations between the uPN organization and the behavioral responses of Drosophila to external stimuli encoded by glomerular homotypes, finding that certain odor types and behavioral responses are linked to a characteristic inter-neuronal organization. The map of synaptic connectivity between uPNs and the third-order neurons (KCs and LHNs in MB calyx and LH, respectively) complements the functional implication of the association between the inter-PN organization and olfactory processing. A ‘labeled-line design’ in olfaction is generally considered to exhibit a chain of neurons dedicated to encoding a single olfactory feature with no direct integration with other features as the signal is passed onto higher-order neurons. While we do not demonstrate the full architecture of labeled-line design in the Drosophila olfactory system as the signals from odor-sensing by ORNs are passed down to the inner brain for perception, our analysis shows that homotypic uPNs encoding particular odor types not only maintain their spatially localized and bundled structure throughout all three neuropils but also display synaptic connections that converge to a narrow subset of third-order neurons. The Drosophila olfactory system leverages the efficiency of the labeled-line design in sensory information processing (Min et al., 2013; Howard and Gottfried, 2014; Andersson et al., 2015; Galizia, 2014).

## Results

### Spatial organization of neurons inside neuropils

#### The inter-PN distance dα⁢β

First, we define a metric with which to quantify the spatial proximity between neurons. Specifically, the inter-PN distance $d_{\alpha⁢\beta}$ represents the average taken over the minimum Euclidean distances between two uPNs $\alpha$ and $\beta$, such that $d_{\alpha⁢\beta}$ is small when two uPNs are tightly bundled together (see Equation 1 and Figure 2—figure supplement 1A). Although metrics such as the NBLAST score (Costa et al., 2016) and others (Kohl et al., 2013) can be used to study the PN organization, these metrics take both the morphological similarity and the spatial proximity into account. The distance $d_{\alpha⁢\beta}$ only measures the pairwise distance but not the dot product term (which measures the similarity of two neuronal morphologies), whereas the NBLAST score considers both. Therefore, while the distance $d_{\alpha⁢\beta}$ is computationally comparable to the NBLAST score, it only measures the spatial proximity between two neurons. We notice that the features of the uPN organization captured by the NBLAST distance are not necessarily aligned with $d_{\alpha⁢\beta}$ (see Figure 2—figure supplement 1B). The two distances are correlated but with significant dispersion, indicating that these two metrics are not the same. Since we are solely interested in the spatial proximity (or co-location) between two uPN innervations but not the morphological similarity between them (which the NBLAST score accounts for, a point also noted by Zheng et al., 2018), we deliberately chose the metric $d_{\alpha⁢\beta}$ instead of the NBLAST score for our analyses.

The distances $d_{\alpha⁢\beta}$ (Equation 1) between all the possible pairs ($\alpha$ and $\beta$) of 135 uPNs from the FAFB dataset are visualized in the form of a matrix (Figure 2). We perform hierarchical clustering on the distance matrix for uPNs in each neuropil (see the outcomes of $d_{\alpha⁢\beta}$-based clustering analysis in Figure 2—figure supplement 2 and Materials and methods for the details). Individual clusters from the hierarchical clustering of uPNs in MB calyx and LH from the FAFB dataset are visualized in Figure 3 and Figure 4 with the colors denoting the odor types encoded by the individual uPNs, which will be discussed in detail later.

![Figure 2.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig2-v2.jpg)

**Figure 2.:** The three matrices representing the pairwise distances $d_{\alpha⁢\beta}$ in units of $\mu⁢m$ between individual uPN in AL, MB calyx, and LH.The matrices are calculated based on uPNs available in the FAFB dataset. The diagonal blocks reflect the homotypic uPNs comprising the 57 glomerular homotypes defined in the FAFB dataset (Bates et al., 2020), labeled at the edges.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) A schematic showing how the ‘distance’ between two neurons $\alpha$ and $\beta$ ($d_{\alpha⁢\beta}$) is calculated. (B) The comparisons between $d_{\alpha⁢\beta}$ and the normalized NBLAST distance (which is equal to $1-NBLAST score$) for uPN innervation to AL, MB calyx, and LH. While the two distances are correlated, significant dispersion is also present. Unlike NBLAST score, $d_{\alpha⁢\beta}$ measures the spatial proximity between two neurons $\alpha$ and $\beta$ only, but not their morphological similarity.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** The analysis was done on the uPNs in the FAFB dataset. The diagonal block represents each cluster (see Figure 3, Figure 4, and Figure 2—figure supplement 3 for detailed information on the clustering labels). The indices of uPNs are reorganized based on the results from the clustering analysis.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** The analysis was done on the uPNs in the FAFB dataset. In (B) and (C), the different colored leaves correspond to a cluster generated from the tree-cutting method. A leaf represents an individual uPN and the label depicts the corresponding homotype for each uPN.

![Figure 3.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig3-v2.jpg)

**Figure 3.:** The $d_{\alpha⁢\beta}$-based clustering on uPNs based on the FAFB dataset in MB calyx resulting in 10 clusters.The individual uPNs are color-coded based on the encoded odor types (Dark green: decaying fruit, lime: yeasty, green: fruity, gray: unknown/mixed, cyan: alcoholic fermentation, red: general bad/unclassified aversive, beige: plant matter, brown: animal matter, purple: pheromones, pink: hygro/thermo) (Mansourian and Stensmyr, 2015; Bates et al., 2020). The first and second columns illustrate the dorsal and the anterior view, respectively (D: dorsal, M: medial, P: posterior). The black line denotes the approximate boundary of MB calyx.

![Figure 4.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig4-v2.jpg)

**Figure 4.:** The $d_{\alpha⁢\beta}$-based clustering on uPNs based on the FAFB dataset in LH resulting in 11 clusters.(inset) A cartoon illustrating the relative position between clusters $C_{I}^{LH}=C_{3}^{LH}$ and $C_{O}^{LH}=C_{4,5,6,9}^{LH}$. The individual uPNs are color-coded based on the encoded odor types (Dark green: decaying fruit, lime: yeasty, green: fruity, gray: unknown/mixed, cyan: alcoholic fermentation, red: general bad/unclassified aversive, beige: plant matter, brown: animal matter, purple: pheromones, pink: hygro/thermo). The first and second columns illustrate the dorsal and the anterior view, respectively (D: dorsal, M: medial, P: posterior). The black line denotes the approximate boundary of LH.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** 15 clusters from the $d_{\alpha⁢\beta}$-based clustering on the entire PN innervation in LH including those that do not innervate all three neuropils such as GABAergic mPNs.The 15 clusters from the $d_{\alpha⁢\beta}$-based clustering on the entire uPN innervation in LH using the FAFB dataset. The individual uPNs are color-coded based on the encoded odor types (Dark green: decaying fruit, lime: yeasty, green: fruity, gray: unknown/mixed, cyan: alcoholic fermentation, red: general bad/unclassified aversive, beige: plant matter, brown: animal matter, purple: pheromones, pink: hygro/thermo). The first and second columns illustrate the dorsal and the anterior view, respectively (D: dorsal, M: medial, P: posterior). The black line denotes the approximate boundary of LH.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Shown are 14 homotypes consisting of uPNs whose innervation is localized to LH.

#### Spatial proximity-based clustering results

In MB calyx, the hierarchical clustering divides the uPNs from the FAFB dataset into 10 clusters (Figure 3). Clusters $C_{2}^{MB}$ and $C_{10}^{MB}$ largely encompass the dorsal region and clusters $C_{6}^{MB}$ and $C_{7}^{MB}$ encompass the ventral region of the neuropil. The cluster $C_{7}^{MB}$ shows a characteristic biforked pattern projecting to the lateral and medial regions. The cluster $C_{3}^{MB}$ also exhibits the same structural pattern but is composed of a tight bundle of uPNs that are part of DL2d and DL2v (both of which encodes food-related odors). The cluster $C_{8}^{MB}$ is located between the biforked innervation pattern of clusters $C_{6}^{MB}$ and $C_{7}^{MB}$, and predominantly innervates the posterior region. Lastly, clusters $C_{1}^{MB}$, $C_{4}^{MB}$, and $C_{5}^{MB}$, innervate the anterior region of MB calyx, spatially separated from other uPNs.

In LH, 11 clusters are identified in the FAFB dataset (Figure 4). The cluster $C_{3}^{LH}$ is the largest, which mainly innervates the dorsal posterior region of LH. Clusters $C_{4}^{LH}$, $C_{5}^{LH}$, $C_{6}^{LH}$, and $C_{9}^{LH}$ display variable biforked projection patterns along the coronal plane, enveloping the boundary of the cluster $C_{3}^{LH}$. This creates a spatial pattern where a large blob of uPNs ($C_{I}^{LH}$) are surrounded by a claw-like structure ($C_{O}^{LH}$) (Figure 4, inset). Clusters $C_{1}^{LH}$, $C_{2}^{LH}$, and $C_{7}^{LH}$ innervate the anterior-ventral region and display clear segregation from the other uPNs. Another group composed of clusters $C_{10}^{LH}$ and $C_{11}^{LH}$ innervates the posterior-ventral-medial region.

We use Pearson’s $χ^{2}$-test (see Materials and methods for the details) to assess the likelihood of dependence between the $d_{\alpha⁢\beta}$-based clustering outputs for MB calyx, LH, and the glomerular labels (homotypes) statistically significant correlations are found in terms of both the p-value and the Cramér’s $V$ (see Appendix 1—table 1 and Methods for a detailed explanation of the meaning behind the p-value and the Cramér’s $V$), the latter of which is analogous to the correlation coefficient for the $χ^{2}$-test. The mutual information between the same set of nominal variables, which is calculated to verify our $χ^{2}$-tests (see Materials and methods), offers a similar conclusion (see Appendix 1 and Appendix 1—table 3).

We also categorize the spatial organization of uPNs in reference to the glomerular labels. The homotypic uPNs constituting a tightly bundled glomerulus in AL manifest themselves as the block diagonal squares in the $d_{\alpha⁢\beta}$-matrix (Figure 2). This is apparent in the dendrogram constructed from the distance matrix for the uPNs at AL (Figure 2—figure supplement 3), where uPNs sharing the same glomerular label are grouped under a common branch, thereby demonstrating the spatial proximity between uPNs forming the same glomerulus. The $d_{\alpha⁢\beta}$-matrix indicates that such organizations are also preserved in MB calyx and LH. However, clear differences are found in the off-diagonal part of $d_{\alpha⁢\beta}$ matrices (Figure 2).

The same hierarchical clustering analysis performed on the hemibrain dataset results in 14 clusters for uPN innervation in MB calyx and 13 clusters in LH. Despite the differences in the number of clusters, we find that spatial and structural characteristics of individual clusters observed from the FAFB dataset are well translated and comparable to those from the hemibrain dataset (see the clustering result in Figure 8—figure supplement 1). Furthermore, various statistical tests used in this study (e.g. Pearson’s $χ^{2}$-test) on the hemibrain dataset lead to the same conclusion (see Appendix 1, Appendix 1—table 2, and Appendix 1—table 4).

#### The degrees of bundling, packing, and overlapping

To conduct a quantitative and concise analysis of $d_{\alpha⁢\beta}$ matrices, we define the mean intra- and inter-homotypic uPN distances, $d¯_{intra,X}$ and $d¯_{inter,X}$ (see Methods for detailed formulation). The $d¯_{intra,X}$ is the average distance between uPNs in the same homotype and measures the degree of uPNs in the homotype $X$ being bundled. Therefore, a smaller $d¯_{intra,X}$ signifies a tightly bundled structure of $X$-th homotypic uPNs (see Figure 5—figure supplement 1 for raw $d¯_{intra,X}$ values). Similarly, $d¯_{inter,X}$, which measures the degree of packing (or segregation), is defined as the average distance between the neurons comprising the $X$-th homotype and neurons comprising other homotypes. Thus, a small value of $d¯_{inter,X}$ signifies tight packing of heterotypic uPNs around $X$-th homotype, while a large value indicates that the homotypic uPNs comprising the homotype $X$ are well segregated from other homotypes (see Figure 5—figure supplement 1 for raw $d¯_{inter,X}$ values).

The degrees of bundling averaged over all homotypes ($d¯_{intra}=N_{X}^{−1}\sumXN_{X}d¯_{intra,X}≈4 \mum$) are comparable over all three neuropils (blue dots in Figure 5A and B). On the other hand, from $d¯_{inter}$, which is defined as the mean inter-homotype distance averaged over all $X$ s, we find that homotypic uPNs are well segregated from others in AL as expected, whereas spatial segregation among homotypes is only weakly present in MB calyx (orange dots in Figure 5A and B and the cartoon of Figure 5C). We also observe that the $d¯_{intra}$ and  $d¯_{inter}$ are comparable for the two different datasets. A minor difference is observed in $d¯_{intra}$, indicating a slightly tighter bundling structure for the hemibrain dataset.

![Figure 5.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig5-v2.jpg)

**Figure 5.:** Plots of $d¯_{intra}$ (blue, degree of bundling), $d¯_{inter}$ (orange, degree of packing), and the ratio between the two distances $\lambda$ (red, degree of overlapping) calculated based on (A) the FAFB dataset and (B) the hemibrain dataset. Error bars depict the standard deviation. (C) Diagram illustrating the overall organization of uPNs at each neuropil. Homotypic uPNs are tightly bundled and segregated in AL. Several groups of homotypic uPNs form distinct heterotypic spatial clusters at higher olfactory centers, extensively overlapping in MB calyx (see Figure 3).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Comparison of the intra- ($d¯_{intra,X}$) and inter-PN ($d¯_{inter,X}$) distances of $X$-th homotype.Comparison of the intra- ($d¯_{intra,X}$, degree of bundling) and inter-PN ($d¯_{inter,X}$, degree of packing) distances of $X$-th homotype in AL, MB calyx, and LH (from lighter to darker colors) from (A) the FAFB dataset and (B) the hemibrain dataset. The homotype label is color-coded based on the odor types obtained from the literature (Dark green: decaying fruit, lime: yeasty, green: fruity, gray: unknown, cyan: alcoholic fermentation, red: general bad/unclassified aversive, beige: plant matter, brown: animal matter, purple: pheromones, pink: hygro/thermo). Homotypes are ordered based on both the odor type and the values of $\lambda_{X}$ in LH. Asterisks (*) mark homotypes composed of a single uPN while plus (+) mark homotypes composed of a single uPN under our selection criterion but are actually a multi-uPN homotype, whose intra-homotype uPN distance is not available. O and X denote attractive and aversive odors, respectively.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** A plot depicting $d¯_{intra}$ (blue, degree of bundling), $d¯_{inter}$ (orange, degree of packing), and the ratio between the two distances λ (red, degree of overlapping) of 15 homotypes without (left) and with (right) 27 additional uPNs added to the FAFB dataset, which are mostly GABAergic and follow mlALT.

Next, we take the ratio of mean intra- to inter-PN distances of $X$-th homotype as $\lambda_{X}$ to quantify the degree of overlapping around $X$-th homotype (see Materials and methods). The term ‘overlapping’ is specifically chosen to describe the situation where different homotypes are occupying the same space. A large value of $\lambda_{X}$ (particularly $\lambda_{X}>0.4$) suggests that the space occupied by the uPNs of the $X$-th homotype is shared with the uPNs belonging to other homotypes. The value $\lambda(=N_{X}^{-1}⁢\sum_{X}^{N_{X}}\lambda_{X})$ averaged over all the homotypes (red in Figure 5A and B) suggests that the extent of overlapping between uPNs is maximal in MB calyx and minimal in AL (Figure 5C).

Figure 6A and B, Figure 7, and Figure 7—figure supplement 1 show individual values of $\lambda_{X}$ for all homotypes in the three neuropils. We identify the following features: (i) In AL, $\lambda_{X}\leq0.4$ for all homotypes except DL5 (a homotype encoding aversive odors), indicating that homotypic uPNs are tightly bundled and segregated from uPNs in other glomeruli. The same trend is observable in the hemibrain dataset (Figure 6B), but with $\lambda_{DL5}\leq0.4$.; (ii) In MB calyx, a large portion ($≈65%$) of $\lambda_{X}$’s exceed 0.4 and even the cases with $\lambda_{X}>1$ are found (VC5, DL5), implying that there is a substantial amount of overlap between different homotypes. In the hemibrain dataset, $≈76%$ of $\lambda_{X}$’s exceed 0.4.; (iii) Although not as significant as those in AL, many of uPNs projecting to LH are again bundled and segregated in comparison to those in MB calyx (see Figure 7B). (iv) The scatter plot of $\lambda_{X}$ between MB calyx and LH (Figure 7C) indicates that there exists a moderate positive correlation ($r=0.642,p<0.0001$) between $\lambda_{X}$ at MB calyx and LH. This implies that a higher degree of overlapping in MB calyx carries over to the uPN organization in LH. The result from the hemibrain dataset is similar ($r=0.677$, $p<0.0001$, see Figure 7—figure supplement 1).

![Figure 6.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig6-v2.jpg)

**Figure 6.:** Degree of overlapping between inter-homotypic uPNs, $\lambda_{X}$ ($X=VM4,VC5,…,VP5$).The degree of overlapping ($\lambda_{X}$) for $X$-th homotype in AL, MB calyx, and LH (from lighter to darker colors) calculated from the uPNs based on (A) the FAFB dataset and (B) the hemibrain dataset. The homotype label is color-coded based on the odor types associated with the glomerulus obtained from the literature and is sorted based on the value of $\lambda_{X}$ for each odor type at LH. Asterisks (*) mark homotypes composed of a single uPN while plus (+) mark homotypes composed of a single uPN under our selection criterion but are actually a multi-uPN homotype, whose intra-homotype uPN distance is not available. O (attractive) and X (aversive) indicate the putative valence information collected from the literature. The blue horizontal line denotes $\lambda_{X}=0.4$. (C) Two homotypes taken from the FAFB dataset, DL3 (purple) and DL5 (red), which are indicated by yellow triangles in (A), are highlighted along with other uPNs (gray).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig6-figsupp1-v2.jpg)

![Figure 7.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig7-v2.jpg)

**Figure 7.:** Scatter plots depicting the relationships between $\lambda_{X}$ s at two different neuropils calculated from the uPNs based on the FAFB dataset; (A) AL versus MB calyx, (B) AL versus LH, and (C) LH versus MB calyx.The color code is the same as in Figure 6. The blue lines in (A) and (B) denote $\lambda_{X}=0.4$.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Scatter plots depicting the relationships between $\lambda_{X}$ s at two different neuropils calculated from the uPNs based on the hemibrain dataset; (A) AL versus MB calyx, (B) AL versus LH, and (C) LH versus MB calyx. The color code is the same as in Figure 6. The blue lines in (A) and (B) denote $\lambda_{X}=0.4$.

The entire neuron morphologies of uPNs from two homotypes with a small ($X=$ DL3, which largely responds to pheromones) and a large ($X=$ DL5) $\lambda_{X}$ s in LH are visualized along with the other uPNs (gray) (Figure 6C). The homotype DL3, which seldom overlaps with others in AL ($\lambda_{DL3}≈0.07$) and LH ($\lambda_{DL3}≈0.17$), displays an increased overlapping in MB calyx ($\lambda_{DL3}≈0.31$). Therefore, DL3 is tightly packed in AL and LH, whereas it is relatively dispersed in MB calyx. Meanwhile, the homotype DL5 displays a significant dispersion in all three neuropils, although the dispersion is the smallest in AL ($\lambda_{DL5}≈0.74$) compared to that in MB calyx ($\lambda_{DL5}≈1.1$) and LH ($\lambda_{DL5}≈1.5$).

There are minor variations between the FAFB and the hemibrain datasets in terms of $d¯_{intra,X}$, $d¯_{inter,X}$, and $\lambda_{X}$, and they likely arise from the factors such as a minor mismatch in the glomerulus label annotations that sometimes affects the number of uPNs constituting a given homotype, and the difference in the number of uPNs between two datasets as a result of our selection criterion. Regardless, still present in both datasets are the spatial and organizational trends described above. Taken together, the organization of olfactory uPNs varies greatly in the three neuropils. The clear homotype-to-homotype segregation in AL no longer holds in MB calyx. Instead, the $d_{\alpha⁢\beta}$ -based clustering suggests the presence of clusters made of multiple different homotypic uPNs (Figure 5C). For some homotypes, the well-segregated organizations in AL are recovered when they reach LH (compare Figure 7A and Figure 7B).

### Relationship between neuronal organization and olfactory features

Now we explore how the structural features identified from our clustering outputs are associated with odor types and valences (behavioral responses). As briefly mentioned earlier, the color codes in Figure 3, Figure 4, Figure 6, and Figure 7 depict odor types encoded by corresponding homotypic uPNs, which follow the same categorical convention used by Mansourian and Stensmyr, 2015 and Bates et al., 2020. The O and X represent the putative valence, which indicates whether Drosophila is attracted to or repelled from the activation of specific homotypic uPNs. For example, DA2 responds to geosmin, a chemical generated from harmful bacteria and mold, which evokes a strong repulsion in Drosophila (Stensmyr et al., 2012). Similarly, VM3 is suggested to encode repulsive odors, while VM2 and VM7d encode attractive odors (Mansourian and Stensmyr, 2015; Bates et al., 2020). Overall, the following information is acquired from the literature (Hallem et al., 2004b; Galizia and Sachse, 2010; Mansourian and Stensmyr, 2015; Badel et al., 2016; Bates et al., 2020) and labeled accordingly:

Collecting the glomerular types of tightly bundled homotypic uPNs with $\lambda_{X}<0.4$ in LH (Figure 6, Figure 7, and Figure 7—figure supplement 1), we explore the presence of any organizational trend.

Figure 8 recapitulates the cluster information from $d_{\alpha⁢\beta}$ -based analysis along with homotypes, odor types (color-codes), and putative valence (attractive (O) and aversive (X) odors). Some points are worth making:

![Figure 8.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig8-v2.jpg)

**Figure 8.:** Asterisks (*) mark homotypes composed of a single uPN while plus (+) mark homotypes composed of a single uPN under our selection criterion but are actually a multi-uPN homotype, whose intra-homotype uPN distance is not available. O and X represent the putative valence information collected from the literature (O: attractive, X: aversive).

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** A diagram summarizing how the clusters of uPNs in MB calyx (14 clusters) and LH (13 clusters) from the hemibrain dataset are associated with the odor types (Dark green: decaying fruit, olive: yeasty, green: fruity, cyan: alcoholic fermentation, red: general bad/unclassified aversive, beige: plant matter, brown: animal matter, purple: pheromones, gray: unknown, pink: hygro/thermo). Asterisks (*) mark homotypes composed of a single uPN while plus (+) mark homotypes composed of a single uPN under our selection criterion but are actually a multi-uPN homotype, whose intra-homotype uPN distance is not available. O and X represent the putative valence information collected from the literature (O: attractive, X: aversive).

Given that the synaptic communications with KCs and LHNs are critical for neural computation in the inner brain, the specific type of uPN organization in each neuropil should be of great relevance. Indeed, it has been suggested that the spatial convergence, segregation, and overlapping of different homotypic uPNs within neuropil influence the information processing in higher olfactory centers (Grosjean et al., 2011).

According to previous studies (Jefferis et al., 2007; Liang et al., 2013; Kohl et al., 2013; Fişek and Wilson, 2014), uPN innervation in LH and LHNs are highly stereotyped in terms of connectivity and response. Homotypic uPNs are spatially organized in AL, and to a certain degree, in LH, based on the odor type and valence information (Min et al., 2013; Huoviala et al., 2020). The presence of tightly bundled anatomy of homotypic uPNs ($\lambda_{X}<0.4$) in both AL and LH (Figure 7B and Figure 7—figure supplement 1B) may imply that the Drosophila olfactory system dedicates a part of the second-order neural circuit on behalf of the ‘labeled-line’ design, which enables the organism to sense urgent chemical stimuli at the early stage of information processing without going through more sophisticated neural computation in the inner brain (Howard and Gottfried, 2014; Andersson et al., 2015; Min et al., 2013).

### Labeled-line design of the higher order olfactory neurons

The concept of labeled-line design is widely considered at work at the ORN-PN interface (AL) as the signal generated from specific olfactory receptors converges to a single glomerulus (Vosshall et al., 2000; Couto et al., 2005; Fishilevich and Vosshall, 2005). A potential labeled-line strategy or separated olfactory processing of aversive odors encoded by DA2 has been extensively discussed (Stensmyr et al., 2012; Seki et al., 2017; Huoviala et al., 2020). It has been shown that pheromone-encoding homotypes in LH (Jefferis et al., 2007; Ruta et al., 2010; Kohl et al., 2013; Frechter et al., 2019; Bates et al., 2020; Das Chakraborty and Sachse, 2021) are at work in specific third-order olfactory neurons. So far, we have shown that the labeled-line design is present in the architecture of higher olfactory centers of second-order neurons, that is, MB calyx and LH, where homotypic uPNs are tightly bundled together despite the lack of glomerular structure. In this section, we will conduct a comprehensive analysis of the synaptic connectivity between PNs and third-order olfactory neurons (KCs and LHNs) using three demonstrations. We ask (i) whether the labeled-line strategy implied in the uPN organization is translated over to the third-order olfactory neurons, (ii) to what extent the signals encoded by different homotypic uPNs are integrated at synaptic interfaces with the third-order neurons, and (iii) whether the spatial properties of pre-synaptic neurons (PNs) play any role in signal integration by the third-order neurons.

#### Homotype-specific connections

For the analysis of the interface between homotypic uPNs and third-order neurons, we study the connectivity matrices $C^{PN−KC}$ and $C^{PN−LHN}$ (see Figure 9, Figure 9—figure supplement 1), which are extracted from the hemibrain dataset (Scheffer et al., 2020). The $C^{ξ}$ ($ξ=$ PN-KC or PN-LHN) is a binary matrix ($C_{X,i}^{ξ}=0$ or 1 dictating the connectivity) of synaptic connectivity between $X$-th homotypic uPNs and $i$-th third-order neuron (KC or LHN). It is observed that most of the KCs and LHNs integrate information from multiple homotypes, but that there are also a small number of KCs and LHNs that synapse only with a single homotype (Figure 10).

![Figure 9.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig9-v2.jpg)

**Figure 9.:** A schematic illustrating the connectivity between homotypes ($X=A,B,…,E$) and third-order neurons ($i=1,2,…,7$).(A) The connectivity matrix $C$ , where $C_{X,i}=1$ when any uPNs in the $X$-th homotype and $i$-th third-order neuron synapses and $C_{X,i}=0$ otherwise. (B) The number of $X$-th homotype-specific connections ($N_{X,sp}$) and the total number of third-order neurons synapsed to any uPNs in the $X$-th homotype. (C) The common synapse matrix ($S$) whose element specifies the number of third-order neurons commonly connected between two homotypes. The homotype A is connected to three third-order neurons 1, 2, and 3 ($N_{A,tot}=3$). Neuron 1 is not synapsing with any other homotype but A, and hence $N_{A,sp}=1$; similarly, $N_{D,sp}=2$ (the blue lines depict specific connections). The signals from the two homotypes B and C are shared by the third-order neurons 2, 3, and 5; therefore, $S_{BC}=3$ in the common synapse matrix $S$.

![Figure 9—figure supplement 1.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig9-figsupp1-v2.jpg)

**Figure 9—figure supplement 1.:** The $58\times1754$ and $58\times1285$ synaptic connectivity matrices for the synaptic interface between PNs and KCs ($C^{PN−KC}$) (left) and between PNs and LHNs ($C^{PN−LHN}$) (right). Homotypic uPNs are merged together.

![Figure 10.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig10-v2.jpg)

**Figure 10.:** Bar graphs depicting the number of KCs/LHNs that synapse with a specific homotype $X$ ($N_{X,sp}$, blue) and the percentage of KCs/LHNs that synapse with a specific homotype $X$ ($f_{X}=N_{X,sp}/N_{X,tot}$, red) at (A) PN-KC and (B) PN-LHN interfaces, with the synaptic weight of $N=3$ used as the threshold.

![Figure 10—figure supplement 1.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig10-figsupp1-v2.jpg)

**Figure 10—figure supplement 1.:** Homotype specific connections with the synaptic connectivity threshold of $N=8$.Bar graphs depicting the number of KCs/LHNs that synapse with a specific homotype $X$ ($N_{X,sp}$, blue) and the percentage of KCs/LHNs that synapse with a specific homotype $X$ ($f_{X}=N_{X,sp}/N_{X,tot}$, red) at (A) PN-KC and (B) PN-LHN interfaces with the synaptic connectivity threshold of $N=8$.

The ‘homotype-specific’ connections, defined as the number of third-order neurons that only synapses with a specific homotype but not with the others (see Figure 10 and Methods for more information) can be quantified in terms of the total number of third-order neurons in contact with $X$-th homotypic uPNs, and it can be obtained by counting the non-zero elements of the matrix $C$ with fixed $X$. For the case of the PN-KC interface, this number can be obtained from $N_{X,tot}^{PN−KC}=\sumi=11754C_{X,i}^{PN−KC}$. Specifically, Figure 10A shows $N_{X,sp}^{PN-KC}$ and those normalized by $N_{X,tot}^{PN−KC}$ ($f_{X}=N_{X,sp}^{PN−KC}/N_{X,tot}^{PN−KC}$, see Materials and methods for the detailed algorithms behind the calculation), for all homotypes ($X=VM4,VC5,…,VP4$). Compared to those in KCs, the ‘homotype-specific’ connections are much more prevalent in LHNs (Figure 10). Certain homotypic uPNs, in particular, the hygro/thermo-sensing homotypes are connected to the LHNs which are dedicated to process the signals from hygro/thermo-sensing homotypes ($\geq10%$ of PN-LHN connections made by homotypes).

To address the concern with potential false positives in the detected synapses, we reexamine our results based on the synaptic connectivity with a higher threshold ($N=8$). Figure 10—figure supplement 1 demonstrates that the homotype-specific connections tend to increase under a more stringent synapse selection criterion, especially in LH. This is most notable in homotypes DM1, DM4, DP1l, and VM6. The existence of these ‘homotype-specific’ third-order neurons suggests that a subset of olfactory processing may rely on the labeled-line strategy that extends beyond the layer of second-order neurons to the higher brain center.

#### Third-order neurons mediate signal integration

Figure 11A, B show the ‘common synapse matrices’ representing the number of commonly connected third-order neurons between two homotypes $X$ and $Y$ ($S_{XY}^{η}$ with $η=$ KC or LHN), which provide glimpses into the extent of signal integration mediated by KCs and LHNs (see Figure 9C and the caption for how these matrices are constructed from the connectivity matrix).

![Figure 11.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig11-v2.jpg)

**Figure 11.:** Common synapse matrices (A) $S^{KC}$ and (B) $S^{LHN}$, each of which represents the extent of signal integration from homotypic uPNs to KCs and LHNs.The color code represents $S_{XY}$, which is the number of the third-order neurons (KCs or LHNs) synapsing with both homotypes $X$ and $Y$. The black color is used when there is no third-order neuron-mediated signal integration ($S_{XY}=0$) happening between two homotypes $X$ and $Y$. See Figure 9C and its caption for how the common synapse matrices are calculated from the connectivity matrices provided in Figure 9—figure supplement 1.

![Figure 11—figure supplement 1.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig11-figsupp1-v2.jpg)

**Figure 11—figure supplement 1.:** The total number of third-order neurons connected to each homotype, which corresponds to the diagonal element of common synapse matrix ($S^{η}$) in MB calyx (top) and LH (bottom). Figure 11—figure supplement 2. [The same as Figure 11 but with a higher threshold ($N=8$) used to identify synaptic connectivity]. Common synapse matrices (A) $S^{KC}$ and (B) $S^{LHN}$ calculated with the synaptic connectivity threshold of $N=8$, each of which represents the extent of signal integration from homotypic uPNs to KCs and LHNs. The black color is used when there is no third-order neuron-mediated signal integration ($S_{XY}=0$) between two homotypes $X$ and $Y$.

![Figure 11—figure supplement 2.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig11-figsupp2-v2.jpg)

**Figure 11—figure supplement 2.:** Common Synapse matrices (A) $S^{KC}$ and (B) $S^{LHN}$ calculated with the synaptic connectivity threshold of $N=8$, each of which represents the extent of signal integration from homotypic uPNs to KCs and LHNs.The black colour is when there is no third-order neuron-mediated signal integration ($S_{XY}=0$) between two homotypes X and Y.

A more stringent selection criterion for synaptic connectivity does not affect our conclusion on the signal integration by the third-order olfactory neurons (Figure 11—figure supplement 2). The only notable change is the general increase in the cases with no integration ($S_{XY}=0$) in $S^{LHN}$, especially for hygro/thermo-sensing homotypes. Thus, the extent of signal integration from homotypic uPNs to KCs and LHNs summarized in $S^{KC}$ and $S^{LHN}$ is robust.

#### Spatial proximity-based versus connectivity-based clustering

Next, we study the relationship between spatial proximity-based clustering and connectivity-based clustering results. Upon visual inspection, the connectivity-based clustering at MB calyx (Figure 12A on the right) appears less structured than the spatial proximity-based clustering (Figure 12A on the left). Specifically, many homotypic uPNs are grouped under a common branch in the tree structure obtained from the spatial proximity-based clustering, whereas such a feature is largely absent in the output of the connectivity-based clustering. Therefore, the spatially well-clustered uPNs at MB calyx (or stereotyped structure) do not necessarily translate into structured connectivity patterns (or stereotyped connectivity), which is consistent with the notion of randomized PN-KC connections (Caron et al., 2013; Stevens, 2015; Eichler et al., 2017; Zheng et al., 2020). In stark contrast to the outcomes for MB calyx, most homotypic uPNs are grouped in the connectivity-based clustering for LH (Figure 12B). This suggests that the spatially proximal uPNs synapse with a similar group of LHNs. The stereotyped organization and stereotyped connectivity of uPNs in LH have been suggested before (Jefferis et al., 2007; Liang et al., 2013; Kohl et al., 2013; Fişek and Wilson, 2014), and we demonstrate such stereotypies are, in reality, expressed throughout LH over all uPNs. In LH, spatial and organizational characteristics of uPNs are well translated to connectivity to LHNs.

![Figure 12.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig12-v2.jpg)

**Figure 12.:** The same uPNs in the two tree structures are connected with lines, which visualize where the uPNs clustered by one method end up in the clustering results of another. The labels for uPNs are representative of the homotype and are color-coded based on the encoded odor types (Dark green: decaying fruit, lime: yeasty, green: fruity, gray: unknown/mixed, cyan: alcoholic fermentation, red: general bad/unclassified aversive, beige: plant matter, brown: animal matter, purple: pheromones, pink: hygro/thermo).

A quantitative comparison of two trees based on statistical tests lends support to the notion that the spatial organization of uPNs can be indicative of connective properties, most evident in LH (see Appendix 2 for Baker’s Gamma index, entanglement, and cophenetic distance correlation).

## Discussion

The inter-PN organization revealed in this study and its association with odor type/valence are reminiscent of the generally accepted notion that the form determines the function in biology. Previously observed stereotypes of neurons in the Drosophila olfactory system were largely based on the differentiation between pheromones and non-pheromones (Ruta et al., 2010; Kohl et al., 2013; Frechter et al., 2019; Das Chakraborty and Sachse, 2021), the whole-cell patch-clamp recording (Seki et al., 2017), and imaging studies suggestive of stimulus-dependent arrangement of neurons in LH (Marin et al., 2002; Wong et al., 2002; Jefferis et al., 2007). Our results are generally consistent with the previous studies, which suggest that a level of stereotypy in uPN organization in MB calyx and LH is universal throughout Drosophila, which can be captured through different metrics and methodologies. In line with Lin et al., 2007, our study finds that homotypes DL2v and DL2d constitute a bilateral cluster in MB calyx ($C_{3}^{MB}$), and that the dual organization of uPNs is present in MB calyx and LH, such that homotypes DC2, DL1, and VA5 are sorted into the same cluster in LH while sharing similar innervation pattern in MB calyx. Our clustering results in LH share similarities with the NBLAST score-based LH clusters (Bates et al., 2020). The uPNs that ended up in the same cluster or nearby clusters, such as homotypes DM1, DM3, DM4, VA4, and VM3 in the cluster $C_{3}^{LH}$, are also grouped in the NBLAST score-based clustering analysis (Bates et al., 2020). We find a significant correlation of $d_{\alpha⁢\beta}$ with NBLAST score (see Figure 2—figure supplement 1) despite the fact that two metrics prioritize different aspects of neuronal anatomy.

Our inter-PN distances and clustering results suggest the spatial organization of uPNs differs greatly in each neuropil (Figure 5). Some of the tightly bundled organization of uPN homotypes are well preserved throughout the neuropils despite the lack of glomerulus in MB calyx and LH. The spatial segregation between different homotypes is, however, practically not present in MB calyx, leading to a high degree of overlapping. Therefore, the heterogeneity of homotypes at the PN-KC synaptic interface may physically assist the randomized sampling known to exist between uPNs and KCs (Caron et al., 2013; Stevens, 2015; Eichler et al., 2017; Zheng et al., 2020).

Our analysis suggests that LH is compartmentalized into four regions: (1) Posterior-dorsal region primarily occupied by food-related uPNs; (2) Anterior-ventral region occupied by pheromone-encoding uPNs; (3) Biforked bundle surrounding posterior-dorsal region largely occupied by food-related uPNs with an aversive response; (4) Posterior-ventral-medial region occupied by hygro/thermo-sensing uPNs. Previous attempts at identifying regions of odorant space in LH revealed compatible results. The three domains (LH-PM, LH-AM, and LH-AL) suggested by Strutz et al., 2014 seem to be a different combination of our clustering result (LH-PM and LH-AM correspond to the posterior-dorsal region and LH-AL corresponds to a combination of anterior-ventral region and the biforked bundle). Although not perfect, the study of the axo-axonic communities in LH yields results with comparable characteristics (Bates et al., 2020), understandably due to the necessity of inter-neuronal proximity to form synapses. For example, the community 12 by Bates et al., 2020 is predominantly composed of homotypes VP1l and DL5, which resembles our cluster $C_{10}^{LH}$. The community 6 contains a mixture of homotypes VA5, VC1, D, DA4l, DC2, DA3, and VA7m, which is reminiscent of our cluster $C_{6}^{LH}$.

Many homotypic uPNs that are spatially localized in LH can be associated with key survival features and a strong innate response (Seki et al., 2017). In this sense, the stereotyped localization of pheromone-encoding uPNs in $C_{8}^{MB}$, $C_{1}^{LH}$, and $C_{2}^{LH}$ is of great interest. Our study not only lends support to the existing studies pointing to the labeled-line strategy in the Drosophila olfactory system but also suggests that there may exist an even more sophisticated level of spatial organization, which supersedes the pheromone versus non-pheromone segregation. Interestingly, while the spatial organization of uPNs in LH has a basis on the functionality of the odor type encoded, it does not seem to be directly translated to segregated chemical features seen in LHNs (Frechter et al., 2019). The apparent divergence observed at the PN-LHN interface, coupled with strongly stereotyped connectivity may contribute to a higher resolution of odor categorization.

### The uPN organizations from FAFB and hemibrain datasets are consistent

Our analyses of both the FAFB and the hemibrain dataset (Scheffer et al., 2020) find that the results from both datasets are generally consistent. For example, $d¯_{intra}$, $d¯_{inter}$, and $\lambda$ analyzed based on two different datasets are almost identical (see Figure 5A and B). $d¯_{intra,X}$, $d¯_{inter,X}$, and $\lambda_{X}$ show slight differences due to a mismatch between the FAFB and the hemibrain dataset (on glomerulus labels and the number of uPNs based on our selection criterion) leading to a different number of uPNs per homotype (Figure 6A and B and Figure 5—figure supplement 1), but the correlation between $\lambda_{X}$ s at MB calyx and LH are still observed (Figure 7C and Figure 7—figure supplement 1C). Most importantly, the clustering results are similar, where many spatial clusters in both datasets share the same set of homotypes. Additionally, odor type-dependent spatial properties are retained (Figure 8 and Figure 8—figure supplement 1), with all statistical tests supporting our hypothesis. In conclusion, the outcomes from our analyses of the two EM datasets lend support to the previous claims of stereotypy in the Drosophila brain and neuronal structures (Jenett et al., 2012; Jeanne et al., 2018; Schlegel et al., 2021).

### Odor signal processing and labeled-lines

Our study suggests that while the primary connectivity motif of third-order olfactory neurons indeed integrates signals, there still exist several labeled lines. The synaptic connections at the PN-KC interface in MB calyx are largely integrative and randomized - with an exception of hygro/thermo-sensing homotypes that display stereotypy even in terms of the connectivity to the KCs. A similar observation has been made by Li et al., 2020, who employed NBLAST score to identify a structural segregation between odor-encoding and hygro/thermo-sensing homotypes. They found that specific KC types are preferentially targeted by hygro/thermo-sensing homotypes. Marin et al., 2020, who carried out connectome analysis specific to hygro/thermo-sensing homotypes, also identified that lateral accessory calyx (lACA), the anterior-dorsal part of the calyx, are primarily targeted by hygro/thermo-sensing homotypes (analogous to our clusters $C_{1}^{MB}$ and $C_{4}^{MB}$ in Figure 3), and found that a number of KCs are dedicated to encoding signals from these homotypes. The uPNs in LH are spatially segregated, which translates to connectivity in three different levels. First, certain LHNs are dedicated to encoding signals from a specific homotype. The number of these ‘homotype-specific’ LHNs varies across the homotype and can make up a significant portion of PN-LHN connections depending on the homotype (Figure 10). Second, synaptic connectivity maps between uPNs and LHNs indicate odor type-dependent integration occurs at LH (Figure 11B). Channels of LHNs predominantly encoding specific odor types are observed; one primarily integrates responses from certain food-related homotypes, one integrates pheromone-encoding homotypes, and another integrates hygro/thermo-sensing homotypes. Third, homotypic uPNs share similar connectivity to LHNs, unlike those in MB calyx. The signals relayed from the spatially well-organized (or tightly bundled) homotypes are localized into a specific group of LHNs, thereby forming a ‘homotype-specific’ connectivity motif (Figure 10, Figure 11, and Figure 12).

In our study of the labeled-line strategy, we made several interesting observations, which are worth comparing with the concept of ‘fovea’ introduced by Zheng et al., 2020. A ‘fovea’ delineates deviations between experimentally observed connectivity matrices and connectivity under the assumption of random synapses in MB calyx, specifically for certain food-related uPNs (Zheng et al., 2020). A group of common KCs predominantly sampling ’food-related’ uPNs manifest themselves in the common synapse matrix $S^{KC}$ (see the group of homotypes comprising the clusters, highlighted by the blue arrows in Figure 11A). A subset of homotypic uPNs under the food-related ‘fovea’ reported by Zheng et al., 2020 are also spatially clustered (e.g. DM1, DM4, DP1m, DP1l, VA2, and VA4). While most of these homotypes are spatially proximal (the vast majority of the uPNs are located in clusters $C_{6}^{MB}$ and $C_{7}^{MB}$), some homotypes under the food-related ‘fovea’ such as VA2 are sampled from spatially disparate clusters. Thus, it is likely that factors other than the spatial organization of uPNs in neuropils contribute to creating the ‘fovea’. Interestingly, the spatial proximity of pheromone-encoding homotypes in MB calyx may suggest the existence of pheromone-encoding ‘fovea,’ but most uPNs in these homotypes do not converge in connectivity-based clustering with an exception of VA1d. In fact, we suspect the spatial organization of pheromone-encoding homotypes in MB calyx, which is placed at the center of the neuropil, to facilitate the observed randomization of connections by increasing the accessibility of KCs to these homotypes. There is, however, a potential hygro/thermo ‘fovea,’ where homotypes such as VP1d and VP2 are spatially clustered together and the signals from these homotypes are relayed by the same set of KCs. Curiously, VL1 is part of this hygro/thermo ‘fovea’ (Figure 12A).

### Multiglomerular PNs are spatially distinctive

Apart from uPNs primarily explored in this study, a host of local neurons (LNs) and multiglomerular PNs (mPNs) also constitute sophisticated neural circuits to regulate the signals received from ORNs (Sudhakaran et al., 2012; Bates et al., 2020), playing a significant role in the olfactory signal processing (Olsen et al., 2010; Jeanne and Wilson, 2015; Seki et al., 2017). A large portion of these mPNs is GABAergic and inhibitory (Berck et al., 2016; Tobin et al., 2017), whereas the role of interneurons can be both inhibitory and excitatory (Wilson et al., 2004; Turner et al., 2008). Electrophysiological measurements indicate that mPNs are narrowly tuned to a specific set of odor stimuli (Berck et al., 2016), which is significant given that PNs are generally thought to be more broadly tuned than presynaptic ORNs (Wilson et al., 2004). Several PNs do not follow the typical mALT, but mediolateral antennal lobe (mlALT) or lateral antennal lobe tracts (lALT) instead, thereby bypassing innervation through one of the higher olfactory centers (Schultzhaus et al., 2017; Zheng et al., 2018; Bates et al., 2020). As stated previously, we confined ourselves to uPNs innervating all three neuropils to compare the spatial organization across neuropils for each uPN. As a result, 28 uPNs present in the FAFB dataset are not explored in our study. In MB calyx, only two uPNs constituting VP3 were dropped as a result of our selection criterion, which ended up in an almost identical clustering output once hierarchical clustering was performed on the entire 137 uPNs that innervate MB calyx. Two missing uPNs were grouped into clusters $C_{4}^{MB}$ and $C_{6}^{MB}$, along with other hygro/thermo-sensing homotypes. On the other hand, the addition of 27 uPNs constituting 15 homotypes innervating LH but not MB calyx created four new clusters when hierarchical clustering was performed (Figure 4—figure supplement 1). The additional uPNs changed the content of the individual clusters; that is, the tree-cutting algorithm broke down a few clusters that became larger due to the additional uPNs. Furthermore, when we calculate the $d¯_{intra}$, $d¯_{inter}$, and $\lambda$ in LH for the 15 homotypes that included the 27 uPNs, we find that the $d¯_{intra}$ values increased when the 27 uPNs were included (see Figure 5—figure supplement 2). This suggests that the previously removed uPNs, most of which follow mlALT, are significantly different in terms of spatial and organizational characteristics and thus should be analyzed separately. Out of 27 additional uPNs in LH, 21 were in mlALT, 5 were in trans-lALT, and 1 was in mALT. Figure 4—figure supplement 2 illustrates how these 27 uPNs innervate LH which demonstrates the reason behind increased $d¯_{intra}$ values. These 27 uPNs are mostly GABAergic (21 are labeled as GABAergic, 1 as cholinergic, and 4 as unknown neurotransmitter type), covering 84% of all GABAergic uPNs available in the FAFB dataset. These uPNs innervate LH differently from other uPNs in the same homotype that follow mALT (see homotypes such as DA1, DC4, DL2d, DL2v, DP1l, VA1d, VA1v, VL2a, VL2p, and VP5 in Figure 4—figure supplement 2). Morphologically, inhibitory GABAergic neurons are often considered ‘smooth’ and aspiny (Douglas et al., 1989; Bopp et al., 2014; Gouwens et al., 2019), which are discernible from Figure 4—figure supplement 2.

### The single-uPN homotypes may have different morphological properties

It is of great interest that many of the single-uPN homotypes, characterized by densely branched morphology, encode signals with aversive responses. Direct transmission of the associated signals across the three neuropils via a single PN might simplify the overall processing of the olfactory signals as well as reduce the energetic cost. Similarly, the morphological characteristics of uPN innervation at each neuropil are intriguing. Even though a structural difference exists between the single-uPN and multi-uPN homotypes, all uPN innervations within neuropil share a similar morphology regardless of the homotype (see Figure 6—figure supplement 1; Choi et al., 2022). A localized morphological diversity within a neuron may be a characteristic aspect of pseudo-unipolar neurons like uPN and suggests a fundamentally multi-scale characteristic of neuron morphology.

The Drosophila brain EM reconstruction project has evolved to its near completion since the EM image dataset was first released (Dorkenwald et al., 2022). The reconstruction of the majority of the Drosophila central brain as well as the corresponding connectome with detailed information of the individual synapses has become publicly available (Scheffer et al., 2020). Our analysis of the second-order neurons inside the Drosophila olfactory system may be translated to other parts of the nervous system in Drosophila as well as different organisms including the central nervous system (CNS) of humans. For the mammalian olfactory system, the details of analyses must be adapted, however, since the wiring scheme is much more complex than that of an insect (Maresh et al., 2008). For example, multiple glomeruli encoding the same olfactory signal exist in humans (Mombaerts et al., 1996). When analyzing the spatial properties, this can be accounted for by prioritizing the individual glomerulus over the homotypes. Then, homotypic PNs forming different glomeruli may be compared or averaged if one were to consider the homotype-dependent characteristics. According to the neurotransmitter map from a recent study (Dolan et al., 2019), sophisticated processes beyond neuronal anatomy are apparently at work in the olfactory signal processing. Thus, functional studies incorporating odor response profiles in PNs (Badel et al., 2016) and ORNs (Münch and Galizia, 2016; Bak et al., 2018) would supplement our findings. The extension of our study to the other regulatory interneurons and mPNs, morphological studies of second-order neurons, and spatial analysis of third-order neurons will be of great interest for a better understanding of the olfactory signal processing beyond the implication of the neural anatomy and connectivity studied here.

## Materials and methods

### Data preparation

We used the neuron morphology reconstruction of 346 Drosophila olfactory neurons from the FAFB dataset (Bates et al., 2020) traced from EM images. The neurons were extracted from the right hemisphere of the female Drosophila. Out of 346 neurons in the FAFB dataset, 164 neurons were uPNs. One uPN in the dataset (neuron ID = 1356477 forming VP3) did not have an associated reconstruction (.swc file) available and was therefore ignored. For this study, uPNs that innervate all three neuropils were chosen because our aim is (1) to compare spatial characteristics of the uPN innervation across each neuropil and (2) to classify each uPN based on the odor encoding information. Thus, out of 164 uPNs, a total of 135 uPNs constituting 57 homotypes were collected under this criteria, resulting in mostly cholinergic uPNs that follow mALT. Rest of the uPNs that did not innervate all three neuropils are collected for the supplementary analysis. In MB calyx, a total of 137 PNs are identified with two PNs constituting VP3 that do not innervate all three neuropils. On the other hand, in LH, a total of 162 PNs are identified, indicating that 27 PNs constituting 15 homotypes do not innervate all three neuropils. The morphological information of each neuron is stored as a set of 3D coordinates with the connectivity specified with the parent nodes. Complete reconstruction of neuron morphology was made by connecting data points based on their parent-child relationship.

The hemibrain dataset (Scheffer et al., 2020) was taken from the neuPrint database (Clements et al., 2020), where we collected from the right hemisphere of the female Drosophila a total of 120 uPNs forming 58 glomeruli based on the same criterion we used for the FAFB dataset (uPNs that innervate all three neuropils). Unlike the FAFB dataset, the neurons in the hemibrain dataset are labeled with regions of interest (ROI), which are used to query uPNs conforming to our selection criterion. The discrepancy in the number of uPNs between the two datasets most likely resulted from the difference between the neuropil boundary we used and the region defined by the hemibrain dataset. In fact, we find that the total number of uPNs in both datasets is comparable, with 164 uPNs in the FAFB dataset and 162 uPNs in the hemibrain dataset. The two datasets also had a minor mismatch in the glomerulus label annotations, sometimes affecting the number of uPNs constituting a given homotype. Among the 120 uPNs from the hemibrain dataset, five uPNs had ambiguity in terms of their glomerulus labels, which is presumably due to poorly formed glomerular structures. For these uPNs, we adopted the glomerulus labels of the FAFB dataset with the matching hemibrain neuron IDs.

Additionally, a recent community-led effort identified three glomeruli in both databases with conflicting glomerulus labels, which have been a source of confusion (Schlegel et al., 2021). After an extensive study, the community agreed to rename the glomeruli in both datasets labeled as VC3l, VC3m, and VC5 as VC3, VC5, and VM6, respectively (Schlegel et al., 2021). Thus, we have manually incorporated these labels into our analyses for both the FAFB and the hemibrain dataset.

Next, we systematically demarcated the regions of AL, LH, and MB calyx. The density of data points projected to each axis was used for the identification since the neuropils are featured with a much higher density of data points than the rigid backbone connecting them. The boundaries defining each neuropil were systematically chosen from local minima that separate neuropils from rigid backbones. Due to the unique structure of uPNs, sometimes the projection along a given axis cannot fully differentiate two neuropils. To resolve this issue, projections along each axis were sampled while rotating the data points along the reference axes at $5^{∘}$ increments to obtain multiple snapshots. The densities were analyzed to choose the optimal degrees of rotation along the reference axes that could best segment the neuropils. We used the smallest average and deviation value of density at the local minima as the criteria to choose the optimal rotation. The process has been repeated for each neuropil to identify a set of boundaries along multiple transformed axes with various degrees of rotations that optimally confine each neuropil. This information has been combined to create a set of conditions per neuropil for segmentation. The resulting neuropils were confirmed through visual inspection. We compared our neuropil segmentation boundaries with neuropil volume surface coordinates provided by Ito et al., 2014 via CATMAID (Saalfeld et al., 2009) and found the boundaries are comparable (data not shown). An overview of the segmentation process is available in Figure 13.

![Figure 13.](https://cdn.elifesciences.org/articles/77748/elife-77748-fig13-v2.jpg)

**Figure 13.:** The data points from skeletal reconstruction are projected to each axis to generate distributions from which local minima are obtained. The process is repeated while rotating the uPNs along each axis. A collection of histograms and corresponding local minima are surveyed to generate a set of optimal rotations and boundaries for individual neuropil. The resulting parameters are combined to form a collection of conditions to segment each neuropil.

The odor type and odor valence information were extracted from various literature (Hallem et al., 2004b; Galizia and Sachse, 2010; Stensmyr et al., 2012; Mansourian and Stensmyr, 2015; Badel et al., 2016; Bates et al., 2020) and we closely followed the categorical convention established by Mansourian and Stensmyr, 2015 and Bates et al., 2020. However, we note that the categorization of a uPN under a specific odor category may overshadow the complete spectrum of odorants a uPN might encode, especially if the uPN encodes ORs that are broadly tuned. Therefore, we focused on the well-separated pheromone/non-pheromone encoding types and valence information.

To test our labeled-line hypothesis, the connectivity information between uPNs and higher olfactory neurons such as KCs and LHNs was necessary. Since only the hemibrain dataset contains detailed connectivity information, all of our connectivity studies are done using uPNs, KCs, and LHNs queried from the hemibrain dataset. We chose KCs and LHNs that made at least three synaptic connections with any of the 120 uPNs from the hemibrain dataset. This resulted in 1754 KCs and 1295 LHNs, creating bipartite connectivity matrices at each neuropil.

### Inter-PN distance

The ‘distance’ $d_{\alpha⁢\beta}$ between two neurons, $\alpha$ and $\beta$, with different lengths ($N_{\alpha}\leqN_{\beta}$) is quantified by calculating.

$$
d_{\alpha\beta}^{2}=\frac{1}{N_{\alpha}}\sumi=1N_{\alpha}min[(r_{i}^{\alpha}−r_{j}^{\beta})^{2}],
$$

where $r_{i}^{\alpha}$ is an i-th coordinate forming the neuron $\alpha$. Equation 1 is evaluated over all pairs of $r_{i}^{\alpha}$ and $r_{j}^{\beta}$ with $j=1,…,N_{\beta}$ that gives rise to the minimum value. This means that when $N_{\alpha}\leqN_{\beta}$, for every i-th coordinate in the neuron $\alpha$ ($r_{i}^{\alpha}$), we find j-th coordinate in the neuron $\beta$ ($r_{j}^{\beta}$) that is the closest to $r_{i}^{\alpha}$. Then, the spatial proximity of a given pair of neurons is assessed by the $d_{\alpha⁢\beta}$ that denotes the average of all the minimum Euclidean distances between the pair of coordinates.

### The degree of bundling, packing, and overlapping

We define the mean intra- and inter-homotype distances as.

$$
d¯_{intra,X}≡\frac{1}{N}\sum\alpha,\beta\inXNd_{\alpha\beta}
$$

and

$$
d¯_{inter,X}≡\frac{1}{N}\sum\alpha\inX,\beta∉XNd_{\alpha\beta},
$$

where $X$ denotes a homotype and $N$ is the total number of uPN pairs to be averaged. The $d¯_{intra,X}$ is calculated over all the pairs of uPNs in the $X$-th homotype, quantifying the tightness of bundling of uPNs constituting the $X$-th homotype. On the other hand, $d¯_{inter,X}$ is calculated over the pairs of uPNs between $\alpha$-th uPN belonging to the $X$-th homotype and $\beta$-th uPN in the $Y$-th homotype ($Y\neqX$), such that it measures the extent of packing of uPNs around the $X$-th homotype. The degree of overlapping for the $X$-th homotype, $\lambda_{X}$, is defined as the ratio of average intra- and inter-homotype distances,

$$
\lambda_{X}=\frac{d¯_{intra,X}}{d¯_{inter,X}},
$$

which represents how clearly the $X$-th homotype is segregated from other homotypes in a given space. A large value of $\lambda_{X}$ ($\lambda_{X}≫1$) implies that the space spanned by the $X$-th homotype is not clearly discerned from other homotypes.

### Spatial clustering of projection neurons

Hierarchical/agglomerative clustering was used to cluster the uPN innervation at each neuropil using the pairwise $d_{\alpha⁢\beta}$ matrices. First, the linkage was decided based on the pairwise distance matrix built with the Farthest Point Algorithm (or ‘complete’ method), where uses the maximum distance between neurons to define the distance between two clusters. This criterion is used to build hierarchical relations (or nested clusters) in a bottom-up approach where each neuron is treated as a cluster at the beginning. The result is a fixed tree structure of individual neurons from which the finalized clusters are formed using an optimal tree-cutting algorithm. In the dendrogram from AL (Figure 2—figure supplement 3), homotypic uPNs are grouped together with high accuracy, suggesting our distance metric $d_{\alpha⁢\beta}$ is adequate. We tested various tree-cutting criteria such as elbow method, gap statistics, maximum average silhouette coefficient, and dynamic hybrid cut tree method (Langfelder et al., 2008) to determine the optimal number of clusters. Among them, we selected the dynamic hybrid cut tree method, since it performed the best in giving the cluster number closest to the number of different odor types (which is 10) (Table 1). We deployed the dynamic hybrid cut tree method with the minimum cluster size of 4 neurons for the tree-cutting, following the neuron clustering procedure used by Gouwens et al., 2019.

**Table 1.**
 The optimal number of clusters of uPNs in the FAFB dataset determined by employing the dynamic hybrid cut tree method, elbow method, gap statistics, and maximum average silhouette coefficient.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Dynamic hybrid</th>
      <th>Elbow</th>
      <th>Gap</th>
      <th>Silhouette</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AL</td>
      <td>19</td>
      <td>14</td>
      <td>8</td>
      <td>54</td>
    </tr>
    <tr>
      <td>MB calyx</td>
      <td>10</td>
      <td>11</td>
      <td>7</td>
      <td>2</td>
    </tr>
    <tr>
      <td>LH</td>
      <td>11</td>
      <td>9</td>
      <td>7</td>
      <td>2</td>
    </tr>
  </tbody>
</table>

### Pearson’s x2-test of independence

The association between two categorical variables is assessed using Pearson’s $χ^{2}$-test. For the test, a contingency table, which lists the categorical frequency of two variables, is created. For example, $O_{i⁢j}$ of the $i$- and $j$-th element of the contingency table shown below is the frequency counting the putative valence $i=1$ (attractive), 2 (aversive), 3 (unknown), and the number of uPNs in one of the 10 clusters in MB calyx with $j=1$ ($C_{1}^{MB}$), 2 ($C_{2}^{MB}$), ... , 10 ($C_{10}^{MB}$).

<table>
  <thead>
    <tr>
      <th></th>
      <th>C1MB</th>
      <th>C2MB</th>
      <th>C3MB</th>
      <th>C4MB</th>
      <th>C5MB</th>
      <th>C6MB</th>
      <th>C7MB</th>
      <th>C8MB</th>
      <th>C9MB</th>
      <th>C10MB</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Attractive</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>4</td>
      <td>11</td>
      <td>11</td>
      <td>8</td>
      <td>44</td>
    </tr>
    <tr>
      <td>Aversive</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>12</td>
      <td>9</td>
      <td>8</td>
      <td>8</td>
      <td>3</td>
      <td>47</td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>4</td>
      <td>7</td>
      <td>8</td>
      <td>5</td>
      <td>6</td>
      <td>5</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>44</td>
    </tr>
    <tr>
      <td>Total</td>
      <td>5</td>
      <td>13</td>
      <td>8</td>
      <td>6</td>
      <td>10</td>
      <td>22</td>
      <td>14</td>
      <td>21</td>
      <td>22</td>
      <td>14</td>
      <td>135</td>
    </tr>
  </tbody>
</table>

Then the $χ^{2}$ value is evaluated based on the table using.

$$
χ^{2}=\sumi=1R\sumj=1C\frac{(O_{ij}−E_{ij})^{2}}{E_{ij}},
$$

where $R$ and $C$ are the numbers of rows and columns, and $O_{i⁢j}$ and $E_{i⁢j}$ are the observed and expected frequencies of the event in the $i$-th row and $j$-th column, respectively. $E_{i⁢j}$ is calculated from $O_{i⁢j}$ as.

$$
E_{ij}=Np_{i⋅}p_{⋅j},
$$

where $p_{i⁣⋅}=\sum_{j}^{C}O_{i⁢j}/N$ and $p_{⋅j}=\sum_{i}^{R}O_{i⁢j}/N$ with $N$ being the total count. Thus, $E_{i⁢j}$ is the frequency expected by assuming that the two categorical data are statistically independent. Pearson’s $χ^{2}$ test aims to check whether there is a significant difference between $O_{i⁢j}$ and $E_{i⁢j}$.

In the $χ^{2}$-test, the p-values are estimated using $f_{k}⁢(x)$, the $χ^{2}$-distribution with the degree of freedom $k=(R-1)⁢(C-1)$. If the test returns a $χ^{2}$ value that gives rise to a p-value smaller than the defined significance level ($\alpha=0.01$), the null hypothesis of independence between the two data sets should be rejected. As a result, the distribution of the categorical data is deemed significantly different from a randomly generated distribution, which concludes that the association between two sets of data is statistically significant.

For the above contingency table with $k=18$, which leads to $χ^{2}≈66.1$ (Equation 5), we get a p-value much smaller than the significance level ($\alpha=0.01$), $p=1−\int_{0}^{χ^{2}}f_{k=18}(x)dx≈2.016\times10^{−7}≪\alpha=0.01$.

When Pearson’s $χ^{2}$ statistics are available, one can calculate Cramér’s $V$ with bias correction, a measure of association between two categorical variables, as follows.

$$
V=\sqrt{\frac{ϕ^{′2}/N}{min(R^{′}−1,C^{′}−1)}},
$$

where $ϕ^{′⁣2}=max⁡(0,χ^{2}/N-(R-1)⁢(C-1)/(N-1))$, $R^{′}=R-(R-1)^{2}/(N-1)$, and $C^{′}=C-(C-1)^{2}/(N-1)$. Similar to the Pearson correlation coefficient, the value $V$ ranges between 0 and 1 where 0 indicates no correlation and 1 indicates a complete correlation between two categorical variables.

### Mutual information

Mutual information ($I$) is used to verify the significance of association between nominal variables observed in Pearson’s $χ^{2}$-test for independence. The $I$ measures the information transfer or the similarity between two data. The concept can be extended to clustering outputs to check how two different clustering labels from the same data are similar to each other. Traditionally, the $I$ between two jointly discrete variables $A$ and $B$ is given by.

$$
I(A;B)=\sumi=1n_{A}\sumj=1n_{B}P(A_{i},B_{j})log⁡[\frac{P(A_{i},B_{j})}{P(A_{i})P(B_{j})}],
$$

where $n_{A}$ (or $n_{B}$) is the number of clusters in $A$ (or $B$). Numerically, the $I$ between two clustering outputs $A$ and $B$ is calculated by evaluating $P⁢(A_{i})=N_{A_{i}}/N$, $P⁢(B_{i})=N_{B_{i}}/N$, and $P⁢(A_{i},B_{j})=N_{A_{i}∩B_{j}}/N$ where $N$ is the total count and $N_{A_{i}∩B_{j}}$ is the number of elements common in both clusters $A_{i}$ and $B_{j}$.

The significance was assessed by comparing the observed $I$ with the distribution of $I$ s from randomly sampled variables. Specifically, the cluster label was randomly sampled 1000 times to generate a distribution of $I$ under the assumption of independence. The value of observed $I$ is considered significant if the approximated p-value is below 0.01 (p< 0.01).

### Analysis of synaptic interfaces

We conducted three different analyses on the synaptic interfaces of uPNs with the third-order neurons (KCs or LHNs) from the hemibrain dataset.

(i) The ‘homotype-specific’ connections ($N_{X,sp}^{ξ}$ with $ξ=$ PN-KC or PN-LHN) are obtained by counting the number of third-order neurons that synapse with a homotype $X$ but do not synapse with any other homotypes, the information of which is provided by the binarized connectivity matrix $C$. The total number of synaptic connections for a homotype $X$ is simply the sum of the row of the connectivity matrix $C$ ($N_{X,tot}^{ξ}=Σ_{i=1}^{N_{ξ}}C_{Xi}$).

(ii) To generate the $S$ matrices, we counted the number of third-order neurons synapsing with a given homotype $X$ that also synapses with other homotypes.

(iii) The tanglegram study required a hierarchical clustering of uPNs based on their connectivity to third-order neurons. The distances between uPNs in the connectivity matrix $C$ represent the similarity of the connectivity patterns to third-order neurons between two uPNs. We utilized the metric of cosine distance, which is widely used for analyzing the connectivity matrix (Bates et al., 2019; Bates et al., 2020; Li et al., 2020; Eschbach et al., 2020; Schlegel et al., 2021). The cosine distance is defined as.

$$
d_{cos}=1−\frac{u⋅v}{|u||v|},
$$

where $u$ and $v$ are two vectors to be compared. After calculating the distances, we performed hierarchical clustering by Ward’s criterion, which minimizes the variance of merged clusters, to generate the tree structure. The results of hierarchical clustering using the spatial proximity ($d_{\alpha⁢\beta}$) and connectivity ($d_{cos}$) are compared using a tanglegram (Figure 12) after untangling two trees using the ’step1side’ method (Galili, 2015).

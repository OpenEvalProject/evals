# Multi-contrast anatomical subcortical structures parcellation

## Authors

- Pierre-Louis Bazin<sup>1</sup> ([ORCID: 0000-0002-0141-5510](https://orcid.org/0000-0002-0141-5510)) †
- Anneke Alkemade<sup>1</sup> ([ORCID: 0000-0002-3234-353X](https://orcid.org/0000-0002-3234-353X))
- Martijn J Mulder<sup>1</sup>
- Amanda G Henry<sup>4</sup> ([ORCID: 0000-0002-2923-4199](https://orcid.org/0000-0002-2923-4199))
- Birte U Forstmann<sup>1</sup> ([ORCID: 0000-0002-1005-1675](https://orcid.org/0000-0002-1005-1675))

### Affiliations

1. Integrative Model-based Cognitive Neuroscience research unit, University of Amsterdam Amsterdam Netherlands
2. Max-Planck Institute for Human Cognitive and Brain Sciences Leipzig Germany
3. Psychology Department, Utrecht University Utrecht Netherlands
4. Faculty of Archaeology, Leiden University Leiden Netherlands

† Corresponding author

## Abstract

The human subcortex is comprised of more than 450 individual nuclei which lie deep in the brain. Due to their small size and close proximity, up until now only 7% have been depicted in standard MRI atlases. Thus, the human subcortex can largely be considered as terra incognita. Here, we present a new open-source parcellation algorithm to automatically map the subcortex. The new algorithm has been tested on 17 prominent subcortical structures based on a large quantitative MRI dataset at 7 Tesla. It has been carefully validated against expert human raters and previous methods, and can easily be extended to other subcortical structures and applied to any quantitative MRI dataset. In sum, we hope this novel parcellation algorithm will facilitate functional and structural neuroimaging research into small subcortical nuclei and help to chart terra incognita.

## Introduction

Subcortical brain structures are often neglected in neuroimaging studies due to their small size, limited inter-regional contrast, and weak signal-to-noise ratio in functional imaging (Forstmann et al., 2016; Johansen-Berg, 2013). Yet, these small and diverse structures are prominent nodes in functional networks (Marquand et al., 2017; Ji et al., 2019), and they undergo pathological alterations already at early stages of neurodegenerative diseases (Andersen et al., 2014; Koshiyama et al., 2018). Deep brain stimulation surgery, originally performed to reduce motor symptoms in essential tremors, is now a promising therapeutic option in later stages of Parkinson’s disease and movement disorders, as well as refractory psychiatric illnesses in obsessive-compulsive disorder, anorexia, or depression (Forstmann et al., 2017; Mosley et al., 2018). Evolutionary genetics even uncovered that in modern humans, Neanderthal-inherited alleles were preferentially down-regulated in subcortical and cerebellar regions compared to other brain regions (McCoy et al., 2017), suggesting these structures to be essential in making us specifically human.

Despite their importance, these areas are particularly difficult to image. Furthermore, the size, shape, and location of these brain regions changes with development and aging (Fjell et al., 2013; Keuken et al., 2013; Yeatman et al., 2014; Herting et al., 2018). Experience-based plasticity continuously remodels myelin (Tardif et al., 2016; Hill et al., 2018; Turner, 2019), iron and other magnetic substances accumulate with age or pathology (Andersen et al., 2014; Zhang et al., 2018), both bringing changes in the MRI appearance of subcortical regions with diverse tissue characteristics (Draganski et al., 2011; Keuken et al., 2017).

Thus, mapping the structure and function of the subcortex is a major endeavor as well as a major challenge for human neuroscience. Extensive work available from animal brain models unfortunately does not translate in a straightforward way to human subcortical anatomy nor does it shed much light on its involvement in human cognition (Steiner and Tseng, 2017). Besides serious difficulties in obtaining adequate measures of subcortical neural activity in functional MRI (de Hollander et al., 2017; Miletić et al., 2020), atlases and techniques for labeling accurately and reliably individual subcortical structures have also been scarce (Frazier et al., 2005; Chakravarty et al., 2006; Ahsan et al., 2007; Yelnik et al., 2007; Qiu et al., 2010; Patenaude et al., 2011), typically labeling the thalamus, striatum (or its subdivision into caudate and putamen), and globus pallidus (internal and external segments combined), sometimes the amygdala. However, recent advances in anatomical MRI, combining multiple contrasts and/or quantitative MRI mapping and utilizing the higher resolution achievable with 7 Tesla (7T) and above have started to reduce the gap, each mapping a few additional structures or sub-structures, primarily the iron-rich substantia nigra, red nucleus and sub-thalamic nucleus (Keuken et al., 2013; Xiao et al., 2015; Visser et al., 2016a; Visser et al., 2016b; Wang et al., 2016; Makowski et al., 2018; Ewert et al., 2018; Iglesias et al., 2018; Pauli et al., 2018; Sitek et al., 2019). While these efforts generated valuable atlases, they do not yet enable to identify many subcortical structures in individual subjects. Manual delineation, on the other hand, requires extensive manual labor from highly trained experts which cannot be easily applied to large cohorts or clinical settings.

Here, we propose a new automated parcellation technique to identify and label 17 individual subcortical structures of varying size and composition in individual subjects, based on a large quantitative 7T MRI database (Alkemade et al., 2020), using quantitative maps of relaxation rates R1 and R2* (1/T1 and 1/T2*, respectively) and quantitative susceptibility maps (QSM) as anatomical contrasts. The algorithm, named Multi-contrast Anatomical Subcortical Structure Parcellation (MASSP), follows a Bayesian multi-object approach similar in essence to previous efforts (Fischl et al., 2002; Eugenio Iglesias et al., 2013; Visser et al., 2016a; Garzón et al., 2018), combining shape priors, intensity distribution models, spatial relationships, and global constraints. The main innovation of our approach is to explicitly estimate interfaces between subcortical structures based on a joint model derived from signed distance functions. Modeling interfaces in addition to the structure itself provides a rich basis to encode relationships and anatomical knowledge in shape and intensity priors. A voxel-wise Markovian diffusion regularizes the combined priors for each defined interface, lowering the imaging noise. Finally, the voxel-wise posteriors for the different structures and interfaces are further combined into global anatomical parcels by topology correction and region growing taking into account volumetric priors, which regularizes parcellation results further in smaller nuclei with low or heterogeneous contrast. To validate the results from this new method, in a thorough comparison with expert manual labeling, we show that the proposed method provides results very close from manual raters in many structures and exhibit reasonable bias across the adult lifespan. The method can easily be extended to new structures, can be applied to any quantitative MRI dataset and is available in Open Source as part of Nighres (Huntenburg et al., 2018), a neuroimage analysis package aimed at high-resolution neuroimaging.

## Results

The MASSP parcellation method presented here has been trained to parcellate the following 17 structures: striatum (Str), thalamus (Tha), lateral, 3rd and 4th ventricles (LV, 3V, 4V), amygdala (Amg), globus pallidus internal segment (GPi) and external segment (GPe), SN, STN, red nucleus (RN), ventral tegmental area (VTA), fornix (fx), internal capsule (ic), periaqueductal gray (PAG), pedunculopontine nucleus (PPN), and claustrum (Cl), see Figure 1. These structures include the most commonly defined subcortical regions (Str, Tha, Amg, LV), the main iron-rich nuclei (GPi, GPe, RN, SN, STN), as well as smaller, less studied areas (VTA, PAG, PPN, Cl), white matter structures (ic, fx), and the central ventricles (3V, 4V).

![Figure 1.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig1-v2.jpg)

**Figure 1.:** A), sagittal (B), and coronal (C) views.

MASSP uses a data set of ten expert delineations as a basis for its modeling. From the delineations, an atlas of interfaces between structures, shape skeletons, and interface intensity histograms are generated, and used as prior in a multiple-step non-iterative Bayesian algorithm, see Figure 2 and Materials and methods.

![Figure 2.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig2-v2.jpg)

**Figure 2.:** Atlas priors for interfaces between structures are combined to the MRI data, regularized via probability diffusion and topology correction, and the final structure posteriors are jointly estimated by region growing.

## Validation against manual delineations

In a leave-one-out validation study comparing performance with the manual delineations, MASSP performed above 95% of the level of quality of the raters for Str, Tha, 4V, GPe, SN, RN, VTA, ic in terms of Dice overlap, the most stringent of the quality measures (see Figures 3 and 4 and Table 1). Several of the smaller structures have lower overlap ratios likely due to their smaller size (GPi, STN, PAG, PPN). Structures with an elongated shape (fx, Cl) remain challenging, due to the fact that small differences in location can substantially reduce overlap (Bazin et al., 2016). Despite these challenges, when comparing the dilated Dice scores, all structures were above 75% of overlap, with most reaching over 90% of the manual raters ability. Note that the Dice coefficient is very sensitive to size, as smaller structures will have lower overlap ratios for the same number of misclassified voxels. The dilated Dice coefficient is more representative of the variability regardless of size, as the smaller structures can reach high levels of overlap, both in manual and automated parcellations (see Table 1). The average surface distance confirms these results, showing values generally between one and two voxels of distance at a resolution of 0.7 mm, except in the cases of Amg, LV, fx, PPN, and Cl. These structures are generally more variable (LV), elongated (fx, Cl), or have a particularly low contrast with neighboring regions (Amg, PPN).

![Figure 3.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig3-v2.jpg)

**Figure 3.:** Scores for the left and right side are computed separately and then combined into box-and-whisker plots.

![Figure 4.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig4-v2.jpg)

**Figure 4.:** Scores for the left and right side are computed separately and then combined into box-and-whisker plots.

## Comparison to other automated methods

To provide a basis for comparison, we applied other freely available methods for subcortical structure parcellation to the same 10 subjects. MASSP performs similarly to or better than Freesurfer, FSL FIRST and a multi-atlas registration using ANTs (see Table 2). Multi-atlas registration provides high accuracy in most structures as well, but is biased toward under-estimating the size of smaller and elongated structures where overlap is systematically reduced across the individual atlas subjects. Multi-atlas registration is also quite computationally intensive when using multiple contrasts at high resolution. Finally, MASSP provides many more structures than Freesurfer and FSL FIRST, and can be easily applied to new structures based on additional manual delineations.

## Application to new MRI contrasts

Quantitative MRI has only become recently applicable in larger studies, thanks in part to the development of integrated multi-parameter sequences (Weiskopf et al., 2013; Caan et al., 2019). Many data sets, including large-scale open databases, use more common T1- and T2-weighted MRI. In order to test the applicability of MASSP to such contrasts, we obtained the test-retest subset of the Human Connectome Project (HCP, Van Essen et al., 2013) and applied MASSP to the 45 pre-processed and skull-stripped T1- and T2-weighted images from each of the two test and retest sessions. While performing manual delineations on the new contrasts would be preferable, the model is already rich enough to provide stable parcellations. Test-retest reproducibility is similarly high for MASSP and Freesurfer, and are generally in agreement, see Figure 5 and Table 3.

![Figure 5.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig5-v2.jpg)

**Figure 5.:** MASSP priors were not derived from the contrasts, but transferred via a spatial mapping of the quantitative MRI intensities from AHEAD subjects.

## Biases due to atlas size

A common concern of brain parcellation methods is the risk of biases, as they are typically built from a small number of manual delineations. Our data set is part of a large scale study of the subcortex, for which we obtained manual delineations of the STN, SN, RN, GPe, and GPi on 105 subjects over the adult lifespan (18–80 year old, see Alkemade et al., 2020 for details). First, we investigated the impact of atlas size. We randomly assigned half of the subjects from each decade to two groups, and built atlas priors from subsets of 3, 5, 8, 10, 12, 15, and 18 subjects from the first group. The subjects used in the atlas were taken randomly from each decade (18-30, 31-40, 41-50,51-60, 61-70, 71-80), so as to maximize the age range represented in each atlas. Atlases of increasing size were constructed by adding subjects to previous atlases, so that atlases of increasing complexity include all subjects from simpler atlases. Results applying these atlases to parcellate the second group are given in Figure 6. As in previous studies (Eugenio Iglesias et al., 2013; Bazin and Pham, 2008), performance quickly stabilized with atlases of more than five subjects (no significant difference in Welch’s t-tests between using 18 subjects or any subset of 8 or more for all structures and measures).

![Figure 6.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig6-v2.jpg)

**Figure 6.:** Scores for the left and right side are computed separately and then combined into box-and-whisker plots.

## Biases due to age differences

To more specifically test the influence of age on parcellation accuracy, we defined again six age groups by decade and randomly selected 10 subjects from each group. Each set of subjects was used as priors for the five structures above, and applied to the other age groups. Results are summarized in Figure 7. Examining this age bias, we can see a decrease in performance when parcellating subjects in the range of 60 to 80 years of age. The choice of priors seem to have a limited impact, which varies across structures. In particular, using priors from a similar age group is not always beneficial.

![Figure 7.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig7-v2.jpg)

**Figure 7.:** Each matrix show the average Dice overlap (top), dilated Dice overlap (middle), and average surface distance (bottom) for using one age group as prior (’train’) to parcellate another age group (’test’).

## Bias on individual measures

Finally, we investigated the impact of this decrease in performance in the estimation of anatomical quantities, see Figure 8. The bias did affect the morphometric measures of structure volume and thickness, but the effects on the local measure of thickness was reduced compared to the global measure of volume. Quantitative MRI averages were very stable even when age biases are present in the parcellations.

![Figure 8.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig8-v2.jpg)

**Figure 8.:** Circles show individual data points, linear regression is indicated by a straight line, and 95% confidence interval is given as the shaded area. Pearson correlation coefficients are indicated when significant (p-value<0.01).

For reference, we report structure volumes, thickness, R1, R2* and QSM values estimated from the entire AHEAD cohort for different age groups, extending our previous work based on manual delineations on a different data set (Keuken et al., 2017; Forstmann et al., 2014). Results are given in Table 4, describing average volumes, thickness, and quantitative MRI parameters for young, middle-aged, and older subjects for the 17 subcortical structures.

## Discussion

Our goal with the MASSP algorithm was to provide a fully automated method to delineate as many subcortical structures as possible on high-resolution structural MRI now available on 7T scanners. We modeled 17 distinct structures, taking into account location, shape, volume, and quantitative MRI contrasts to provide individual subject parcellations. Based on our results, we can be confident that the automated parcellation technique performs comparably to human experts, providing delineations within one or two voxels of the structure boundaries (dilated Dice overlap over 75% for all structures, including in aging groups). Results were nearly indistinguishable from expert delineations for eight major structures (Str, Tha, 4V, GPe, SN, RN, VTA, ic), and smaller structures retain high levels of overlap, comparable to trained human raters. This parcellation includes the most commonly defined structures (Str, Tha, SN, RN, STN) with overlap scores comparable to those previously reported (Garzón et al., 2018; Visser et al., 2016a; Eugenio Iglesias et al., 2013; Chakravarty et al., 2013; Patenaude et al., 2011). More importantly, it also includes structures seldom or never before considered in MRI atlases and parcellation methods, such as GPe, GPi, VTA, 3V, 4V, ic, fx, PAG, PPN, Cl. The technique handles structures of varying sizes well, as indicated by dilated overlap and boundary distance. Additional structures can be added, if they can be reliably delineated by expert raters on single-subject MRI at achievable resolutions. Some enhancement techniques such as building a multi-subject template (Pauli et al., 2018) or adding a denoising step (Bazin et al., 2019) may be beneficial. Co-registration to a high-precision atlas as in Ewert et al., 2018 may also improve the initial alignment over the MASSP group average template.

Age biases are present both in expert manual delineations and automated parcellation techniques. Age trajectories in volume and quantitative MR parameters indicate systematic shifts in contrast intensities and an increasing variability with age, associated with changing myelination, iron deposition, and brain atrophy (Draganski et al., 2011; Daugherty and Raz, 2013; Fjell et al., 2013; Keuken et al., 2017). These changes seem only to impact the parcellation accuracy for age groups beyond 60 years and age-matched priors did not provide specific improvements, thus indicating that an explicit modeling of age effects may be required to further improve parcellation quality in elderly populations. These results also point to exercising caution when applying automated parcellation methods to study morphometry in elderly or diseased populations, where measured differences may include biases. They also point out that while global volume and local thickness are indeed affected by such biases, quantitative MRI measures are much more robust. Note that this bias is likely present is many automated methods, although they have not been systematically investigated due to the extensive manual labor required. Interestingly, biases also exist in expert delineations: when the size or shape of a structure is refined in neuroanatomical studies, experts may become more or less conservative in their delineations. Automated methods provide a more objective measure in such case, as the source of their bias is explicitly encoded in the atlas prior delineations and computational model. Important applications of subcortical parcellation also include deep-brain stimulation surgery (Ewert et al., 2018), where the number of structures parcellated by MASSP can help neurosurgeons orient themselves more easily, although precise targeting will still require manual refinements, especially in neurodegenerative diseases.

We observed that dilated overlap, that is, the overlap of structures up to one voxel, provided a measure of accuracy largely independent of size, for automated or manual delineations. Imprecision in the range of one voxel in the boundary is to be expected due to partial voluming which impacts Dice overlap. The dilated overlap measure is a better representative of performance and indicates that conservative or inclusive versions of the subcortical regions can be obtained by eroding or dilating the estimated boundary by a single voxel. Such masks may be useful when separating functional MRI signals between neighboring nuclei or when locating smaller features inside a structure. Additionally, the Bayesian estimation framework provides voxel-wise probability values, which can also be used to further weight the contribution of each voxel within a region in subsequent analyses.

In summary, our method provides fast and accurate parcellation for subcortical structures of varying size, taking advantage of the high resolution offered by 7T and the specificity of quantitative MRI. The algorithm is based on an explicit model of structures given in a Bayesian framework and is free of tuning parameters. Given a different set of regions of interest or different populations, new priors can be automatically generated and used as the basis for the algorithm. If more MRI contrasts are available, the method can also be augmented to take them into account. The main requirement for the technique is a set of manual delineations of all the structures of interest in a small group of representative subjects. Performance may further improve with the number of included structures, as the number of distinct interfaces increases, refining in particular the intensity priors. In future works, we plan to include more structures or sub-structures and model the effects of age on the priors. We hope that the method, available in open source, will help neuroscience researchers to include more subcortical regions in their structural and functional imaging studies.

## Materials and methods

## Data acquisition

Our parcellation method has been developed for the MP2RAGEME sequence (Caan et al., 2019). Briefly, the MP2RAGEME consists of two interleaved MPRAGEs with different inversions and four echoes in the second inversion. Based on these images, one can estimate quantitative MR parameters of R1, R2* and QSM. In this work, we used the following sequence parameters: inversion times TI1,2 = 670 ms, 3675.4 ms; echo times TE1 = 3 ms, TE2,1–4 = 3, 11.5, 19, 28.5 ms; flip angles FA1,2 = 4°, 4°; TRGRE1,2 = 6.2 ms, 31 ms; bandwidth = 404.9 MHz; TRMP2RAGE = 6778 ms; SENSE acceleration factor = 2; FOV = 205×205 x 164 mm; acquired voxel size = 0.70×0.7 x 0.7 mm; acquisition matrix was 292 × 290; reconstructed voxel size = 0.64×0.64 x 0.7 mm; turbo factor (TFE) = 150 resulting in 176 shots; total acquisition time = 19.53 min.

T1-maps were computed using a look-up table (Marques et al., 2010). T2*-maps were computed by least-squares fitting of the exponential signal decay over the multi-echo images of the second inversion. R1 and R2* maps were obtained as the inverse of T1 and T2*. For QSM, phase maps were pre-processed using iHARPERELLA (integrated phase unwrapping and background phase removal using the Laplacian) of which the QSM images were computed using LSQR (Li et al., 2014). Skull information was removed through creation of a binary mask using FSL’s brain extraction tool on the reconstructed uniform T1-weighted image and then applied to the quantitative contrasts (Smith, 2002). As all images were acquired as part of a single sequence, no co-registration of the quantitative maps was required (see Figure 9).

![Figure 9.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig9-v2.jpg)

**Figure 9.:** Manual delineations for the 17 structures of interest are overlaid on all images.

## Anatomical structure delineations

Manual delineations of subcortical structures were performed by two raters trained by an expert anatomist, according to protocols optimized to use the better contrast or combination of contrasts for each structure and to ensure a consistent approach across raters. The following 17 structures were defined on a group of 10 subjects (average age 24.4, eight female): striatum (Str), thalamus (Tha), lateral, 3rd and 4th ventricles (LV, 3V, 4V), amygdala (Amg), globus pallidus internal segment (GPi) and external segment (GPe), SN, STN, red nucleus (RN), ventral tegmental area (VTA), fornix (fx), internal capsule (ic), periaqueductal gray (PAG), pedunculopontine nucleus (PPN), and claustrum (Cl). Separate masks for left and right hemisphere were delineated except for 3V, 4V, and fx. In the following the algorithm treats each side separately, resulting in a total of 31 distinct structures (see Figure 1).

## Anatomical interface priors

In order to inform the algorithm, we built a series of priors derived from the manual delineations. Each subject was first co-registered to a MP2RAGEME anatomical template built from 105 subjects co-aligned with the MNI2009b atlas (Fonov et al., 2011) with the SyN algorithm of ANTs (Avants et al., 2008) using successively rigid, affine, and non-linear transformations, high levels of regularization as recommended for the subcortex (Ewert et al., 2019) and mutual information as cost function.

The first computed prior is a prior of anatomical interfaces, recording the most likely location of boundaries between the different structures, defined as follows. Given two delineated structures i,j, let φi,φj be the signed distance functions to their respective boundary, that is, φi⁢(x) is the Euclidean distance of any given voxel to the boundary of i, with a negative sign inside the structure. Then we define the interface Bi|j with the distance function di|j:(1)di|j⁢(x)=min⁡(φi⁢(x),φj⁢(x)-δ,0)where δ is a scale parameter for the thickness of the interface. These interfaces functions are not symmetrical, as the intensity inside i next to j is generally different from the intensity inside j next to i. Based on this definition, the prior for a given interface based on N manual delineations is given by:(2)P(x∈Bi|j)∼12⁢π⁢σi|j2⁢(x)exp-12μi|j2⁢(x)σi|j2⁢(x)μi|j⁢(x)=1N⁢∑n∈Ndi|j,n⁢(x),σi|j⁢(x)=1N⁢∑n∈N(di|j,n⁢(x)-μi|j⁢(x))2+δ

These probability functions are calculated for all possible configurations including i|i, which represent the inside of each structure. We thus have a total of N2 functions, but only a few are non-zero at a given voxel x, and we may keep only the 16 largest values to account for any number of interfaces in 3D (Bazin et al., 2007). Finally, we need to scale the prior to be globally consistent with the priors below by assuming that the 95th percentile of the highest kept P(x∈Bi|j) values have a probability of 0.95. The scale parameter δ is set to one voxel, representing the expected amount of partial voluming. The resulting interface prior is shown in Figure 10A.

![Figure 10.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig10-v2.jpg)

**Figure 10.:** A) and skeleton (B) priors derived from the 10 manually delineated subjects.

## Anatomical skeleton priors

Next, we defined priors for the skeleton of each structure, representing their essential shape regardless of exact boundaries (Blum, 1973). As we are mostly interested in the most likely components of the skeleton or medial axis Si, we follow a simple method to estimate its location:(3)Si={x,|∇φi(x)|<12}

We define as si⁢(x) the signed distance function of this discrete skeleton, and define prior probabilities as above:(4)P(x∈Si)∼12⁢π⁢σi2⁢(x)exp-12μi2⁢(x)σi2⁢(x)μi⁢(x)=1N⁢∑n∈Nsi,n⁢(x)⁢σi⁢(x)=1N⁢∑n∈N(si,n⁢(x)-μi⁢(x))2+δ

The skeletons are defined inside each structure, which implies P(x∈Si)≤P(x∈Bi|i). To respect this relationship, we scale P(x∈Si) with the same factor as P(x∈Bi|i) but use P(x∈Si) when combining probabilities during the estimation stage. The obtained anatomical skeleton priors are given on Figure 10B.

## Interface intensity priors

While anatomical priors already provide rich information, they are largely independent of the underlying MRI. From the co-aligned quantitative MRI maps and manual delineations, we defined intensity priors for every interface i|j, in the form of intensity histograms to ensure a flexible representation of intensity distributions. Given a quantitative contrast Rn⁢(x), we built a histogram Hi|j,n for each subject n and interface i|j. Histograms have 200 bins covering the entire intensity range within a radius of 10 mm from any of the delineated structures. To obtain an average histogram, we combine each histogram with a weighting function wn⁢(x) giving the likelihood of the subject’s intensity measurement compared to the group:(5)wi|j,n(x)=P(x∈Bi|j)12⁢π⁢σR2exp-12(Rn⁢(x)-μR⁢(x))2σR⁢(x)2where μR⁢(x) is the median of the Rn⁢(x) values at x, and σR⁢(x) is 1.349 times the inter-quartile range of Rn⁢(x). These are robust estimators of the mean and standard deviation, used here to avoid biases by intensity outliers. To further combine the R1, R2*, and QSM contrasts we take the geometric mean of the histogram probabilities: Hi|j⁢(x)=∏RHi|j⁢(R⁢(x))1/3.

## Global volume priors

The last type of priors extracted from manual delineations are volume priors for each of the structure. Here, we assume a log-normal distribution for the volumes Vi and simply estimate the mean μV,i and standard deviation σV,i of log⁡Vi,n over the subjects.

## Voxel-wise posterior probabilities

When parcellating a new subject, we first co-register its R1, R2*, and QSM maps jointly to the template and use the inverse transformation to deform the anatomical priors into subject space. Then we derive voxel-wise posteriors as follows:(6)P(x∈Bi|j|R(x))∼P(x∈Bi|j)Hi|j(x) if i≠jandP(x∈Bi|i|Si(x),R(x))∼max(P(x∈Bi|i),P(x∈Si)1/2)Hi|i(x)

Once again we should compute all possible combinations, but due to the multiplication of the priors we can restrict ourselves to the 16 highest probabilities previously estimated. To balance the contribution of the anatomical priors and the intensity histograms, we also need to normalize the intensity priors sampled on the subject’s intensities. We use the same approach, namely assuming that the 95th percentile of the highest kept Hi|j⁢(x) values have a probability of 0.95, separately for each contrast. The voxel-wise parcellation and posteriors obtained are shown in Figure 11A.

![Figure 11.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig11-v2.jpg)

**Figure 11.:** A) voxel-wise posteriors and parcellation, (B) diffused posteriors and parcellation, (C) topology-corrected posteriors and final region-growing parcellation.

## Markovian diffusion

The voxel-wise posteriors are independent from each other and do not reflect the continuous nature of the structures. The next step is to combine information from neighboring voxels. We define a sparse Markov Random Field model for the posteriors:(7)P(x∈Bi|j|R,S,C)=∑y∈C⁢(x)P(y∼x|R)P(y∈Bi|j|R,S,C)with P(y∼x|R)=∏Rexp-(R(y)-R(x))2/2σR2, where σR is the median of the standard deviations σi|j,R of the contrast histograms Hi|j⁢(R⁢(x)). The neighborhood C⁢(x) is defined as x itself and the four 26-connected neighboring voxels with highest probability P(y∼x|R), thus representing the neighbors most likely to be connected to x. The model is similar to a diffusion process and can be estimated with an iterated conditional modes (ICM) approach, updating sequentially the probabilities (Bazin and Pham, 2007):(8)P(x∈Bi|j|R,S,C)←∑y∈C⁢(x)P(y∼x|R)P(y∈Bi|j|R,S,C)from the initial voxel-wise posteriors until the ratio of changed parcellation labels decreases below 0.1, typically within 50–80 iterations. The diffused probabilities and parcellation are shown in Figure 11B.

## Topology correction

The final step of the parcellation algorithm takes a global view of the individual structures, growing from the highest posterior values inside toward the boundaries. This region growing approach makes the implicit assumption that posterior maps should be monotonically decreasing from inside to outside, which is not necessarily the case. Therefore, we perform first a topology correction step on the individual structure posteriors P(x∈i|R,B,S,C)=maxi|jP(x∈Bi|j|R,S,C) with a fast marching algorithm (Bazin and Pham, 2007). While the corrected posterior is very similar to the original one (see Figure 11C), it ensures that all regions obtained by growing to a threshold have spherical object topology.

## Anatomical region growing

Last, we turn the posteriors into optimized parcellations, by growing them concurrently (to avoid overlaps) until the target volume for each structure is reached. Given the volume Vi⁢(R,B,S,C) of the parcellation of the diffused and topology-corrected posteriors, we define the following target volume:(9)V^i=P⁢(Vi|μV,i,σV,i)⁢Vi+(1-P⁢(Vi|μV,i,σV,i))⁢exp⁡μV,itaking a weighted average of the volume estimated from the data and the prior volume. This approach ensures that even in extreme cases where some structures have low posteriors, they are still able to grow to a plausible size. The region growing algorithm is driven from the most likely voxels, defined as P(x∈i|R,B,S,C)-maxj≠iP(x∈j|R,B,S,C), and further modulated to follow isocontours of the skeleton prior:(10)P(x←y)∼P(y∈i|R,B,S,C)-maxj≠iP(y∈j|R,B,S,C)-|P(y∈Si)-P(x∈Si)|

Directionality of internal structures is a useful tool for understanding mechanical function in bones (Maquer et al., 2015). Here, we adapt this concept by using the skeleton isocontours as a representation of internal directionality, maintaining the intrinsic shape of structures. Thus, voxels with highest probability compared to the other structures and with similar distance to the internal skeleton are preferentially selected. The final parcellation is given in Figure 11C.

## Validation metrics

To validate the method against manual expert delineations, we compared the MASSP results and the expert delineations with the following three measures:

We computed all three measures for the manual delineations from the two independent raters, as well as the ratio of overlaps (automated over manual) and distances (manual over automated) to compare both performances, as detailed in the Results section.

## Comparisons with other automated methods

To assess the performance of MASSP compared to existing parcellation tools, we ran Freesurfer (Fischl et al., 2002), FSL FIRST (Patenaude et al., 2011) and a multi-atlas registration approach (co-registering 9 of the 10 manually delineated subjects on the remaining one with ANTs [Avants et al., 2008] and labeling each structure by majority voting, similarly to the MAGeT Brain approach of Chakravarty et al., 2013). Freesurfer and FIRST were run on the skull-stripped R1 map, while the multi-atlas approach used all three R1, R2*, and QSM contrasts. All methods were compared in terms of Dice overlap, dilated overlap and average surface distance. We also assessed the presence of a systematic volume bias, defined as the average of the signed difference of the estimated structure volume to the manually delineated volume, normalized by the manually delineated volume.

## Application to new MRI contrasts

Before applying MASSP to unseen contrasts, we need to convert its intensity prior histograms Hi|j,R to the new intensities. In order to perform this mapping, we first created a groupwise median of the HCP subjects, by co-registering every subject to the MASSP template using ANTs with non-linear registration and both T1w, T2w contrasts matched to the template’s R1 and R2* maps. The histogram bins are then updated as follows:(11)Hbin,i|j,R≡∑x|R⁢(x)∈binP(x∈Bi|j)Hi|j,R⁢1Hi|j,R⁢2⁣*Hi|j,Q⁢S⁢Madding the joint probability of the quantitative contrasts weighted by their importance for each interface to define the new intensity histograms. This model is essentially projecting the joint likelihood of the MASSP contrasts onto the new contrasts, assuming that the co-registration between the two is accurate enough. With these new histograms, we compared the test-retest reliability and overall agreement of MASSP with Freesurfer parcellations included in the HCP pre-processed data set.

## Measurement of structure thickness

Finally, when comparing derived measures obtained over the lifespan with MASSP compared to manual delineations, we explored the utility of a shape thickness metric, based on the medial representation. Given the signed distance function φi of the structure boundary and si of the structure skeleton, the thickness is given by:(12)t⁢hi⁢(x)=2⁢(si⁢(x)-φi⁢(x))

Like in cortical morphometry, thickness is a local measure, defined everywhere inside the structure, and expected to provide additional information about anatomical variations. Indeed, a similar measure of shape thickness has recently been able to highlight subtle anatomical changes in depression (Ho et al., 2020).

## Software implementation

The proposed method, Multi-contrast Anatomical Subcortical Structure Parcellation (MASSP), has been implemented as part of the Nighres toolbox (Huntenburg et al., 2018), using Python and Java for optimized processing. The software is available in open source from (release-1.3.0) and . A complete parcellation pipeline is included with the Nighres examples. Computations take under 30 min per subject on a modern workstation.

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

MASSP uses a data set of ten expert delineations as a basis for its modeling. From the delineations, an atlas of interfaces between structures, shape skeletons, and interface intensity histograms are generated, and used as prior in a multiple-step non-iterative Bayesian algorithm, see Figure 2 and Materials and methods.

![Figure 2.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig2-v2.jpg)

**Figure 2.:** Atlas priors for interfaces between structures are combined to the MRI data, regularized via probability diffusion and topology correction, and the final structure posteriors are jointly estimated by region growing.

### Validation against manual delineations

In a leave-one-out validation study comparing performance with the manual delineations, MASSP performed above 95% of the level of quality of the raters for Str, Tha, 4V, GPe, SN, RN, VTA, ic in terms of Dice overlap, the most stringent of the quality measures (see Figures 3 and 4 and Table 1). Several of the smaller structures have lower overlap ratios likely due to their smaller size (GPi, STN, PAG, PPN). Structures with an elongated shape (fx, Cl) remain challenging, due to the fact that small differences in location can substantially reduce overlap (Bazin et al., 2016). Despite these challenges, when comparing the dilated Dice scores, all structures were above 75% of overlap, with most reaching over 90% of the manual raters ability. Note that the Dice coefficient is very sensitive to size, as smaller structures will have lower overlap ratios for the same number of misclassified voxels. The dilated Dice coefficient is more representative of the variability regardless of size, as the smaller structures can reach high levels of overlap, both in manual and automated parcellations (see Table 1). The average surface distance confirms these results, showing values generally between one and two voxels of distance at a resolution of 0.7 mm, except in the cases of Amg, LV, fx, PPN, and Cl. These structures are generally more variable (LV), elongated (fx, Cl), or have a particularly low contrast with neighboring regions (Amg, PPN).

**Table 1.**
 Mean overlap and distance measures for the leave-one-out validation.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Str</th>
      <th>STN</th>
      <th>SN</th>
      <th>RN</th>
      <th>GPi</th>
      <th>GPe</th>
      <th>Tha</th>
      <th>LV</th>
      <th>3V</th>
      <th>4V</th>
      <th>Amg</th>
      <th>ic</th>
      <th>VTA</th>
      <th>fx</th>
      <th>PAG</th>
      <th>PPN</th>
      <th>Cl</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="18">Dice overlap</td>
    </tr>
    <tr>
      <td>MASSP</td>
      <td>0.893</td>
      <td>0.648</td>
      <td>0.805</td>
      <td>0.870</td>
      <td>0.702</td>
      <td>0.800</td>
      <td>0.867</td>
      <td>0.849</td>
      <td>0.741</td>
      <td>0.869</td>
      <td>0.723</td>
      <td>0.745</td>
      <td>0.570</td>
      <td>0.527</td>
      <td>0.641</td>
      <td>0.496</td>
      <td>0.485</td>
    </tr>
    <tr>
      <td>Manual</td>
      <td>0.897</td>
      <td>0.800</td>
      <td>0.841</td>
      <td>0.875</td>
      <td>0.762</td>
      <td>0.813</td>
      <td>0.877</td>
      <td>0.907</td>
      <td>0.797</td>
      <td>0.882</td>
      <td>0.866</td>
      <td>0.732</td>
      <td>0.574</td>
      <td>0.823</td>
      <td>0.791</td>
      <td>0.665</td>
      <td>0.727</td>
    </tr>
    <tr>
      <td>Ratio</td>
      <td>0.995</td>
      <td>0.811</td>
      <td>0.957</td>
      <td>0.996</td>
      <td>0.925</td>
      <td>0.987</td>
      <td>0.989</td>
      <td>0.936</td>
      <td>0.936</td>
      <td>0.988</td>
      <td>0.836</td>
      <td>1.020</td>
      <td>0.994</td>
      <td>0.641</td>
      <td>0.814</td>
      <td>0.754</td>
      <td>0.664</td>
    </tr>
    <tr>
      <td colspan="18">Dilated overlap</td>
    </tr>
    <tr>
      <td>MASSP</td>
      <td>0.982</td>
      <td>0.919</td>
      <td>0.977</td>
      <td>0.991</td>
      <td>0.909</td>
      <td>0.956</td>
      <td>0.970</td>
      <td>0.929</td>
      <td>0.890</td>
      <td>0.951</td>
      <td>0.891</td>
      <td>0.915</td>
      <td>0.863</td>
      <td>0.756</td>
      <td>0.897</td>
      <td>0.795</td>
      <td>0.789</td>
    </tr>
    <tr>
      <td>Manual</td>
      <td>0.987</td>
      <td>0.988</td>
      <td>0.985</td>
      <td>0.995</td>
      <td>0.953</td>
      <td>0.972</td>
      <td>0.970</td>
      <td>0.967</td>
      <td>0.944</td>
      <td>0.961</td>
      <td>0.978</td>
      <td>0.924</td>
      <td>0.818</td>
      <td>0.957</td>
      <td>0.960</td>
      <td>0.910</td>
      <td>0.914</td>
    </tr>
    <tr>
      <td>Ratio</td>
      <td>0.995</td>
      <td>0.930</td>
      <td>0.992</td>
      <td>0.995</td>
      <td>0.955</td>
      <td>0.984</td>
      <td>1.000</td>
      <td>0.961</td>
      <td>0.946</td>
      <td>0.991</td>
      <td>0.911</td>
      <td>0.992</td>
      <td>1.059</td>
      <td>0.790</td>
      <td>0.935</td>
      <td>0.879</td>
      <td>0.863</td>
    </tr>
    <tr>
      <td colspan="18">Average surface distance</td>
    </tr>
    <tr>
      <td>MASSP</td>
      <td>0.750</td>
      <td>0.911</td>
      <td>0.676</td>
      <td>0.491</td>
      <td>1.140</td>
      <td>0.863</td>
      <td>1.058</td>
      <td>2.690</td>
      <td>0.994</td>
      <td>0.817</td>
      <td>1.476</td>
      <td>1.275</td>
      <td>1.074</td>
      <td>2.950</td>
      <td>0.955</td>
      <td>1.484</td>
      <td>1.685</td>
    </tr>
    <tr>
      <td>Manual</td>
      <td>0.723</td>
      <td>0.508</td>
      <td>0.571</td>
      <td>0.482</td>
      <td>0.902</td>
      <td>0.804</td>
      <td>0.971</td>
      <td>0.615</td>
      <td>0.637</td>
      <td>0.671</td>
      <td>0.779</td>
      <td>1.045</td>
      <td>1.204</td>
      <td>0.703</td>
      <td>0.555</td>
      <td>0.801</td>
      <td>0.670</td>
    </tr>
    <tr>
      <td>Ratio</td>
      <td>0.971</td>
      <td>0.590</td>
      <td>0.852</td>
      <td>0.996</td>
      <td>0.861</td>
      <td>0.943</td>
      <td>0.916</td>
      <td>0.277</td>
      <td>0.662</td>
      <td>1.020</td>
      <td>0.553</td>
      <td>0.834</td>
      <td>1.161</td>
      <td>0.287</td>
      <td>0.610</td>
      <td>0.619</td>
      <td>0.465</td>
    </tr>
  </tbody>
</table>

![Figure 3.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig3-v2.jpg)

**Figure 3.:** Scores for the left and right side are computed separately and then combined into box-and-whisker plots.

![Figure 4.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig4-v2.jpg)

**Figure 4.:** Scores for the left and right side are computed separately and then combined into box-and-whisker plots.

### Comparison to other automated methods

To provide a basis for comparison, we applied other freely available methods for subcortical structure parcellation to the same 10 subjects. MASSP performs similarly to or better than Freesurfer, FSL FIRST and a multi-atlas registration using ANTs (see Table 2). Multi-atlas registration provides high accuracy in most structures as well, but is biased toward under-estimating the size of smaller and elongated structures where overlap is systematically reduced across the individual atlas subjects. Multi-atlas registration is also quite computationally intensive when using multiple contrasts at high resolution. Finally, MASSP provides many more structures than Freesurfer and FSL FIRST, and can be easily applied to new structures based on additional manual delineations.

**Table 2.**
 Comparison with multi-atlas registration, Freesurfer, and FSL FIRST.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Str</th>
      <th>STN</th>
      <th>SN</th>
      <th>RN</th>
      <th>GPi</th>
      <th>GPe</th>
      <th>Tha</th>
      <th>LV</th>
      <th>3V</th>
      <th>4V</th>
      <th>Amg</th>
      <th>Ic</th>
      <th>VTA</th>
      <th>Fx</th>
      <th>PAG</th>
      <th>PPN</th>
      <th>Cl</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="18">Dice overlap</td>
    </tr>
    <tr>
      <td>MASSP</td>
      <td>0.893</td>
      <td>0.648</td>
      <td>0.805</td>
      <td>0.870</td>
      <td>0.702</td>
      <td>0.800</td>
      <td>0.867</td>
      <td>0.849</td>
      <td>0.741</td>
      <td>0.869</td>
      <td>0.723</td>
      <td>0.745</td>
      <td>0.570</td>
      <td>0.527</td>
      <td>0.641</td>
      <td>0.496</td>
      <td>0.485</td>
    </tr>
    <tr>
      <td>Multi-atlas</td>
      <td>0.855</td>
      <td>0.662</td>
      <td>0.760</td>
      <td>0.820</td>
      <td>0.742</td>
      <td>0.796</td>
      <td>0.859</td>
      <td>0.734</td>
      <td>0.660</td>
      <td>0.691</td>
      <td>0.761</td>
      <td>0.718</td>
      <td>0.626</td>
      <td>0.478</td>
      <td>0.674</td>
      <td>0.539</td>
      <td>0.398</td>
    </tr>
    <tr>
      <td>Freesurfer</td>
      <td>0.876</td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">0.778</td>
      <td>0.838</td>
      <td>0.858</td>
      <td>0.430</td>
      <td>0.769</td>
      <td>0.692</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>FSL FIRST</td>
      <td>0.875</td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">0.813</td>
      <td>0.839</td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.653</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="18">Dilated overlap</td>
    </tr>
    <tr>
      <td>MASSP</td>
      <td>0.982</td>
      <td>0.919</td>
      <td>0.977</td>
      <td>0.991</td>
      <td>0.909</td>
      <td>0.956</td>
      <td>0.970</td>
      <td>0.929</td>
      <td>0.890</td>
      <td>0.951</td>
      <td>0.891</td>
      <td>0.915</td>
      <td>0.863</td>
      <td>0.756</td>
      <td>0.897</td>
      <td>0.795</td>
      <td>0.789</td>
    </tr>
    <tr>
      <td>Multi-atlas</td>
      <td>0.976</td>
      <td>0.938</td>
      <td>0.968</td>
      <td>0.989</td>
      <td>0.947</td>
      <td>0.968</td>
      <td>0.970</td>
      <td>0.920</td>
      <td>0.920</td>
      <td>0.908</td>
      <td>0.921</td>
      <td>0.939</td>
      <td>0.924</td>
      <td>0.798</td>
      <td>0.943</td>
      <td>0.871</td>
      <td>0.811</td>
    </tr>
    <tr>
      <td>Freesurfer</td>
      <td>0.975</td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">0.922</td>
      <td>0.946</td>
      <td>0.974</td>
      <td>0.562</td>
      <td>0.911</td>
      <td>0.857</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>FSL FIRST</td>
      <td>0.976</td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">0.946</td>
      <td>0.950</td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.843</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="18">Average surface distance</td>
    </tr>
    <tr>
      <td>MASSP</td>
      <td>0.750</td>
      <td>0.911</td>
      <td>0.676</td>
      <td>0.491</td>
      <td>1.140</td>
      <td>0.863</td>
      <td>1.058</td>
      <td>2.690</td>
      <td>0.994</td>
      <td>0.817</td>
      <td>1.476</td>
      <td>1.275</td>
      <td>1.074</td>
      <td>2.950</td>
      <td>0.955</td>
      <td>1.484</td>
      <td>1.685</td>
    </tr>
    <tr>
      <td>Multi-atlas</td>
      <td>0.961</td>
      <td>0.891</td>
      <td>0.858</td>
      <td>0.675</td>
      <td>0.992</td>
      <td>0.882</td>
      <td>1.083</td>
      <td>1.417</td>
      <td>0.932</td>
      <td>1.249</td>
      <td>1.359</td>
      <td>1.129</td>
      <td>0.813</td>
      <td>1.362</td>
      <td>0.794</td>
      <td>1.055</td>
      <td>1.273</td>
    </tr>
    <tr>
      <td>Freesurfer</td>
      <td>0.770</td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">1.211</td>
      <td>1.405</td>
      <td>0.685</td>
      <td>4.071</td>
      <td>1.361</td>
      <td>1.749</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>FSL FIRST</td>
      <td>0.867</td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">1.143</td>
      <td>1.675</td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.746</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="18">Volume bias</td>
    </tr>
    <tr>
      <td>MASSP</td>
      <td>0.041</td>
      <td>0.017</td>
      <td>-0.038</td>
      <td>0.007</td>
      <td>0.066</td>
      <td>0.089</td>
      <td>0.040</td>
      <td>0.0470</td>
      <td>0.121</td>
      <td>0.047</td>
      <td>0.078</td>
      <td>0.183</td>
      <td>0.032</td>
      <td>-0.016</td>
      <td>0.026</td>
      <td>0.009</td>
      <td>0.023</td>
    </tr>
    <tr>
      <td>Multi-atlas</td>
      <td>0.020</td>
      <td>-0.087</td>
      <td>-0.009</td>
      <td>0.031</td>
      <td>0.009</td>
      <td>0.014</td>
      <td>0.020</td>
      <td>-0.003</td>
      <td>-0.007</td>
      <td>-0.092</td>
      <td>-0.038</td>
      <td>0.055</td>
      <td>-0.067</td>
      <td>-0.264</td>
      <td>-0.090</td>
      <td>-0.269</td>
      <td>-0.376</td>
    </tr>
    <tr>
      <td>Freesurfer</td>
      <td>0.017</td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">0.087</td>
      <td>0.163</td>
      <td>0.122</td>
      <td>-0.551</td>
      <td>0.351</td>
      <td>0.468</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>FSL FIRST</td>
      <td>-0.100</td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">-0.021</td>
      <td>0.165</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.249</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Application to new MRI contrasts

Quantitative MRI has only become recently applicable in larger studies, thanks in part to the development of integrated multi-parameter sequences (Weiskopf et al., 2013; Caan et al., 2019). Many data sets, including large-scale open databases, use more common T1- and T2-weighted MRI. In order to test the applicability of MASSP to such contrasts, we obtained the test-retest subset of the Human Connectome Project (HCP, Van Essen et al., 2013) and applied MASSP to the 45 pre-processed and skull-stripped T1- and T2-weighted images from each of the two test and retest sessions. While performing manual delineations on the new contrasts would be preferable, the model is already rich enough to provide stable parcellations. Test-retest reproducibility is similarly high for MASSP and Freesurfer, and are generally in agreement, see Figure 5 and Table 3.

**Table 3.**
 Test-retest comparison with Freesurfer on Human Connectome Project data.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Str</th>
      <th>STN</th>
      <th>SN</th>
      <th>RN</th>
      <th>GPi</th>
      <th>GPe</th>
      <th>Tha</th>
      <th>LV</th>
      <th>3V</th>
      <th>4V</th>
      <th>Amg</th>
      <th>ic</th>
      <th>VTA</th>
      <th>fx</th>
      <th>PAG</th>
      <th>PPN</th>
      <th>Cl</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="18">Dice overlap</td>
    </tr>
    <tr>
      <td>MASSP test-retest</td>
      <td>0.914</td>
      <td>0.701</td>
      <td>0.818</td>
      <td>0.829</td>
      <td>0.791</td>
      <td>0.859</td>
      <td>0.928</td>
      <td>0.881</td>
      <td>0.837</td>
      <td>0.870</td>
      <td>0.866</td>
      <td>0.860</td>
      <td>0.738</td>
      <td>0.774</td>
      <td>0.714</td>
      <td>0.713</td>
      <td>0.785</td>
    </tr>
    <tr>
      <td>Freesurfer test-retest</td>
      <td>0.898</td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">0.770</td>
      <td>0.919</td>
      <td>0.894</td>
      <td>0.842</td>
      <td>0.849</td>
      <td>0.852</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>MASSP – Freesurfer</td>
      <td>0.876</td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">0.778</td>
      <td>0.838</td>
      <td>0.858</td>
      <td>0.430</td>
      <td>0.769</td>
      <td>0.692</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="18">Dilated overlap</td>
    </tr>
    <tr>
      <td>MASSP test-retest</td>
      <td>0.987</td>
      <td>0.939</td>
      <td>0.977</td>
      <td>0.978</td>
      <td>0.963</td>
      <td>0.977</td>
      <td>0.990</td>
      <td>0.980</td>
      <td>0.979</td>
      <td>0.986</td>
      <td>0.981</td>
      <td>0.973</td>
      <td>0.969</td>
      <td>0.961</td>
      <td>0.965</td>
      <td>0.972</td>
      <td>0.966</td>
    </tr>
    <tr>
      <td>Freesurfer test-retest</td>
      <td>0.986</td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">0.926</td>
      <td>0.986</td>
      <td>0.989</td>
      <td>0.972</td>
      <td>0.975</td>
      <td>0.978</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>MASSP – Freesurfer</td>
      <td>0.954</td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">0.788</td>
      <td>0.919</td>
      <td>0.934</td>
      <td>0.435</td>
      <td>0.901</td>
      <td>0.866</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="18">Average surface distance</td>
    </tr>
    <tr>
      <td>MASSP test-retest</td>
      <td>0.513</td>
      <td>0.528</td>
      <td>0.467</td>
      <td>0.461</td>
      <td>0.532</td>
      <td>0.508</td>
      <td>0.488</td>
      <td>0.509</td>
      <td>0.391</td>
      <td>0.419</td>
      <td>0.533</td>
      <td>0.536</td>
      <td>0.431</td>
      <td>0.464</td>
      <td>0.428</td>
      <td>0.402</td>
      <td>0.433</td>
    </tr>
    <tr>
      <td>Freesurfer test-retest</td>
      <td>0.876</td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">0.778</td>
      <td>0.838</td>
      <td>0.858</td>
      <td>0.430</td>
      <td>0.769</td>
      <td>0.692</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>MASSP – Freesurfer</td>
      <td>0.976</td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">1.673</td>
      <td>1.605</td>
      <td>1.946</td>
      <td>5.699</td>
      <td>1.428</td>
      <td>1.478</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

![Figure 5.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig5-v2.jpg)

**Figure 5.:** MASSP priors were not derived from the contrasts, but transferred via a spatial mapping of the quantitative MRI intensities from AHEAD subjects.

### Biases due to atlas size

A common concern of brain parcellation methods is the risk of biases, as they are typically built from a small number of manual delineations. Our data set is part of a large scale study of the subcortex, for which we obtained manual delineations of the STN, SN, RN, GPe, and GPi on 105 subjects over the adult lifespan (18–80 year old, see Alkemade et al., 2020 for details). First, we investigated the impact of atlas size. We randomly assigned half of the subjects from each decade to two groups, and built atlas priors from subsets of 3, 5, 8, 10, 12, 15, and 18 subjects from the first group. The subjects used in the atlas were taken randomly from each decade (18-30, 31-40, 41-50,51-60, 61-70, 71-80), so as to maximize the age range represented in each atlas. Atlases of increasing size were constructed by adding subjects to previous atlases, so that atlases of increasing complexity include all subjects from simpler atlases. Results applying these atlases to parcellate the second group are given in Figure 6. As in previous studies (Eugenio Iglesias et al., 2013; Bazin and Pham, 2008), performance quickly stabilized with atlases of more than five subjects (no significant difference in Welch’s t-tests between using 18 subjects or any subset of 8 or more for all structures and measures).

![Figure 6.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig6-v2.jpg)

**Figure 6.:** Scores for the left and right side are computed separately and then combined into box-and-whisker plots.

### Biases due to age differences

To more specifically test the influence of age on parcellation accuracy, we defined again six age groups by decade and randomly selected 10 subjects from each group. Each set of subjects was used as priors for the five structures above, and applied to the other age groups. Results are summarized in Figure 7. Examining this age bias, we can see a decrease in performance when parcellating subjects in the range of 60 to 80 years of age. The choice of priors seem to have a limited impact, which varies across structures. In particular, using priors from a similar age group is not always beneficial.

![Figure 7.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig7-v2.jpg)

**Figure 7.:** Each matrix show the average Dice overlap (top), dilated Dice overlap (middle), and average surface distance (bottom) for using one age group as prior (’train’) to parcellate another age group (’test’).

### Bias on individual measures

Finally, we investigated the impact of this decrease in performance in the estimation of anatomical quantities, see Figure 8. The bias did affect the morphometric measures of structure volume and thickness, but the effects on the local measure of thickness was reduced compared to the global measure of volume. Quantitative MRI averages were very stable even when age biases are present in the parcellations.

![Figure 8.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig8-v2.jpg)

**Figure 8.:** Circles show individual data points, linear regression is indicated by a straight line, and 95% confidence interval is given as the shaded area. Pearson correlation coefficients are indicated when significant (p-value<0.01).

For reference, we report structure volumes, thickness, R1, R2* and QSM values estimated from the entire AHEAD cohort for different age groups, extending our previous work based on manual delineations on a different data set (Keuken et al., 2017; Forstmann et al., 2014). Results are given in Table 4, describing average volumes, thickness, and quantitative MRI parameters for young, middle-aged, and older subjects for the 17 subcortical structures.

**Table 4.**
 Mean volume and quantitative MRI values for each age group.


<table>
  <thead>
    <tr>
      <th>Age</th>
      <th>Str</th>
      <th>STN</th>
      <th>SN</th>
      <th>RN</th>
      <th>GPi</th>
      <th>GPe</th>
      <th>Tha</th>
      <th>LV</th>
      <th>3V</th>
      <th>4V</th>
      <th>Amg</th>
      <th>ic</th>
      <th>VTA</th>
      <th>fx</th>
      <th>PAG</th>
      <th>PPN</th>
      <th>Cl</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="18">Volume (m⁢m3)</td>
    </tr>
    <tr>
      <td>18-40</td>
      <td>10656</td>
      <td>118</td>
      <td>566</td>
      <td>253</td>
      <td>567</td>
      <td>1366</td>
      <td>7112</td>
      <td>7524</td>
      <td>1895</td>
      <td>1391</td>
      <td>1315</td>
      <td>4335</td>
      <td>254</td>
      <td>1632</td>
      <td>250</td>
      <td>193</td>
      <td>843</td>
    </tr>
    <tr>
      <td>41-60</td>
      <td>10572</td>
      <td>124</td>
      <td>583</td>
      <td>256</td>
      <td>586</td>
      <td>1403</td>
      <td>7492</td>
      <td>8850</td>
      <td>2024</td>
      <td>1408</td>
      <td>1363</td>
      <td>4495</td>
      <td>264</td>
      <td>1808</td>
      <td>255</td>
      <td>195</td>
      <td>830</td>
    </tr>
    <tr>
      <td>61-80</td>
      <td>10734</td>
      <td>130</td>
      <td>584</td>
      <td>260</td>
      <td>586</td>
      <td>1397</td>
      <td>7463</td>
      <td>9142</td>
      <td>2023</td>
      <td>1407</td>
      <td>1321</td>
      <td>4407</td>
      <td>272</td>
      <td>1910</td>
      <td>259</td>
      <td>192</td>
      <td>829</td>
    </tr>
    <tr>
      <td colspan="18">Thickness (m⁢m)</td>
    </tr>
    <tr>
      <td>18-40</td>
      <td>5.94</td>
      <td>1.89</td>
      <td>2.55</td>
      <td>4.64</td>
      <td>3.09</td>
      <td>3.56</td>
      <td>8.31</td>
      <td>4.27</td>
      <td>2.77</td>
      <td>4.03</td>
      <td>4.81</td>
      <td>4.06</td>
      <td>1.69</td>
      <td>2.06</td>
      <td>1.78</td>
      <td>1.92</td>
      <td>1.79</td>
    </tr>
    <tr>
      <td>41-60</td>
      <td>5.47</td>
      <td>1.86</td>
      <td>2.66</td>
      <td>4.58</td>
      <td>2.96</td>
      <td>3.41</td>
      <td>8.28</td>
      <td>5.08</td>
      <td>2.95</td>
      <td>3.89</td>
      <td>4.85</td>
      <td>4.19</td>
      <td>1.76</td>
      <td>1.96</td>
      <td>1.84</td>
      <td>1.86</td>
      <td>1.80</td>
    </tr>
    <tr>
      <td>61-80</td>
      <td>5.22</td>
      <td>1.83</td>
      <td>2.60</td>
      <td>4.11</td>
      <td>2.92</td>
      <td>3.22</td>
      <td>8.28</td>
      <td>4.90</td>
      <td>3.18</td>
      <td>4.06</td>
      <td>4.73</td>
      <td>4.19</td>
      <td>1.80</td>
      <td>1.97</td>
      <td>1.90</td>
      <td>1.95</td>
      <td>1.82</td>
    </tr>
    <tr>
      <td colspan="18">qR1 (H⁢z)</td>
    </tr>
    <tr>
      <td>18-40</td>
      <td>0.647</td>
      <td>0.949</td>
      <td>0.857</td>
      <td>0.928</td>
      <td>0.868</td>
      <td>0.850</td>
      <td>0.761</td>
      <td>0.332</td>
      <td>0.346</td>
      <td>0.274</td>
      <td>0.546</td>
      <td>0.906</td>
      <td>0.819</td>
      <td>0.714</td>
      <td>0.654</td>
      <td>0.779</td>
      <td>0.650</td>
    </tr>
    <tr>
      <td>41-60</td>
      <td>0.662</td>
      <td>0.968</td>
      <td>0.893</td>
      <td>0.939</td>
      <td>0.879</td>
      <td>0.856</td>
      <td>0.758</td>
      <td>0.278</td>
      <td>0.315</td>
      <td>0.269</td>
      <td>0.559</td>
      <td>0.904</td>
      <td>0.833</td>
      <td>0.671</td>
      <td>0.653</td>
      <td>0.771</td>
      <td>0.664</td>
    </tr>
    <tr>
      <td>61-80</td>
      <td>0.648</td>
      <td>0.952</td>
      <td>0.882</td>
      <td>0.903</td>
      <td>0.860</td>
      <td>0.830</td>
      <td>0.743</td>
      <td>0.273</td>
      <td>0.300</td>
      <td>0.270</td>
      <td>0.552</td>
      <td>0.884</td>
      <td>0.814</td>
      <td>0.638</td>
      <td>0.647</td>
      <td>0.764</td>
      <td>0.669</td>
    </tr>
    <tr>
      <td colspan="18">qR2* (H⁢z)</td>
    </tr>
    <tr>
      <td>18-40</td>
      <td>43.8</td>
      <td>67.1</td>
      <td>67.8</td>
      <td>63.2</td>
      <td>75.2</td>
      <td>79.6</td>
      <td>38.1</td>
      <td>14.7</td>
      <td>18.9</td>
      <td>9.0</td>
      <td>25.5</td>
      <td>36.8</td>
      <td>39.2</td>
      <td>37.4</td>
      <td>25.9</td>
      <td>32.7</td>
      <td>32.6</td>
    </tr>
    <tr>
      <td>41-60</td>
      <td>50.4</td>
      <td>74.1</td>
      <td>74.1</td>
      <td>77.1</td>
      <td>80.2</td>
      <td>87.9</td>
      <td>40.3</td>
      <td>8.4</td>
      <td>12.4</td>
      <td>11.7</td>
      <td>28.1</td>
      <td>38.7</td>
      <td>42.8</td>
      <td>37.4</td>
      <td>28.0</td>
      <td>33.4</td>
      <td>36.9</td>
    </tr>
    <tr>
      <td>61-80</td>
      <td>51.8</td>
      <td>77.0</td>
      <td>72.5</td>
      <td>73.8</td>
      <td>77.8</td>
      <td>87.0</td>
      <td>40.1</td>
      <td>8.5</td>
      <td>10.2</td>
      <td>12.0</td>
      <td>30.1</td>
      <td>39.6</td>
      <td>52.6</td>
      <td>35.7</td>
      <td>28.4</td>
      <td>34.2</td>
      <td>35.4</td>
    </tr>
    <tr>
      <td colspan="18">QSM (p⁢p⁢m)</td>
    </tr>
    <tr>
      <td>18-40</td>
      <td>0.0329</td>
      <td>0.0609</td>
      <td>0.0738</td>
      <td>0.0717</td>
      <td>0.1015</td>
      <td>0.1150</td>
      <td>0.0138</td>
      <td>0.0130</td>
      <td>0.0100</td>
      <td>0.0279</td>
      <td>0.0036</td>
      <td>−0.0234</td>
      <td>0.0241</td>
      <td>0.0079</td>
      <td>0.0119</td>
      <td>0.0135</td>
      <td>−0.0122</td>
    </tr>
    <tr>
      <td>41-60</td>
      <td>0.0400</td>
      <td>0.0647</td>
      <td>0.0713</td>
      <td>0.0829</td>
      <td>0.0984</td>
      <td>0.1241</td>
      <td>0.0134</td>
      <td>0.0115</td>
      <td>0.0025</td>
      <td>0.0234</td>
      <td>0.0085</td>
      <td>−0.0226</td>
      <td>0.0201</td>
      <td>0.0079</td>
      <td>0.0089</td>
      <td>0.0099</td>
      <td>−0.0110</td>
    </tr>
    <tr>
      <td>61-80</td>
      <td>0.0411</td>
      <td>0.0705</td>
      <td>0.0610</td>
      <td>0.0738</td>
      <td>0.0925</td>
      <td>0.1249</td>
      <td>0.0064</td>
      <td>0.0089</td>
      <td>−0.0034</td>
      <td>0.0236</td>
      <td>0.0061</td>
      <td>−0.0243</td>
      <td>0.0177</td>
      <td>0.0100</td>
      <td>0.0039</td>
      <td>0.0096</td>
      <td>−0.0091</td>
    </tr>
  </tbody>
</table>

## Discussion

Our goal with the MASSP algorithm was to provide a fully automated method to delineate as many subcortical structures as possible on high-resolution structural MRI now available on 7T scanners. We modeled 17 distinct structures, taking into account location, shape, volume, and quantitative MRI contrasts to provide individual subject parcellations. Based on our results, we can be confident that the automated parcellation technique performs comparably to human experts, providing delineations within one or two voxels of the structure boundaries (dilated Dice overlap over 75% for all structures, including in aging groups). Results were nearly indistinguishable from expert delineations for eight major structures (Str, Tha, 4V, GPe, SN, RN, VTA, ic), and smaller structures retain high levels of overlap, comparable to trained human raters. This parcellation includes the most commonly defined structures (Str, Tha, SN, RN, STN) with overlap scores comparable to those previously reported (Garzón et al., 2018; Visser et al., 2016a; Eugenio Iglesias et al., 2013; Chakravarty et al., 2013; Patenaude et al., 2011). More importantly, it also includes structures seldom or never before considered in MRI atlases and parcellation methods, such as GPe, GPi, VTA, 3V, 4V, ic, fx, PAG, PPN, Cl. The technique handles structures of varying sizes well, as indicated by dilated overlap and boundary distance. Additional structures can be added, if they can be reliably delineated by expert raters on single-subject MRI at achievable resolutions. Some enhancement techniques such as building a multi-subject template (Pauli et al., 2018) or adding a denoising step (Bazin et al., 2019) may be beneficial. Co-registration to a high-precision atlas as in Ewert et al., 2018 may also improve the initial alignment over the MASSP group average template.

Age biases are present both in expert manual delineations and automated parcellation techniques. Age trajectories in volume and quantitative MR parameters indicate systematic shifts in contrast intensities and an increasing variability with age, associated with changing myelination, iron deposition, and brain atrophy (Draganski et al., 2011; Daugherty and Raz, 2013; Fjell et al., 2013; Keuken et al., 2017). These changes seem only to impact the parcellation accuracy for age groups beyond 60 years and age-matched priors did not provide specific improvements, thus indicating that an explicit modeling of age effects may be required to further improve parcellation quality in elderly populations. These results also point to exercising caution when applying automated parcellation methods to study morphometry in elderly or diseased populations, where measured differences may include biases. They also point out that while global volume and local thickness are indeed affected by such biases, quantitative MRI measures are much more robust. Note that this bias is likely present is many automated methods, although they have not been systematically investigated due to the extensive manual labor required. Interestingly, biases also exist in expert delineations: when the size or shape of a structure is refined in neuroanatomical studies, experts may become more or less conservative in their delineations. Automated methods provide a more objective measure in such case, as the source of their bias is explicitly encoded in the atlas prior delineations and computational model. Important applications of subcortical parcellation also include deep-brain stimulation surgery (Ewert et al., 2018), where the number of structures parcellated by MASSP can help neurosurgeons orient themselves more easily, although precise targeting will still require manual refinements, especially in neurodegenerative diseases.

We observed that dilated overlap, that is, the overlap of structures up to one voxel, provided a measure of accuracy largely independent of size, for automated or manual delineations. Imprecision in the range of one voxel in the boundary is to be expected due to partial voluming which impacts Dice overlap. The dilated overlap measure is a better representative of performance and indicates that conservative or inclusive versions of the subcortical regions can be obtained by eroding or dilating the estimated boundary by a single voxel. Such masks may be useful when separating functional MRI signals between neighboring nuclei or when locating smaller features inside a structure. Additionally, the Bayesian estimation framework provides voxel-wise probability values, which can also be used to further weight the contribution of each voxel within a region in subsequent analyses.

In summary, our method provides fast and accurate parcellation for subcortical structures of varying size, taking advantage of the high resolution offered by 7T and the specificity of quantitative MRI. The algorithm is based on an explicit model of structures given in a Bayesian framework and is free of tuning parameters. Given a different set of regions of interest or different populations, new priors can be automatically generated and used as the basis for the algorithm. If more MRI contrasts are available, the method can also be augmented to take them into account. The main requirement for the technique is a set of manual delineations of all the structures of interest in a small group of representative subjects. Performance may further improve with the number of included structures, as the number of distinct interfaces increases, refining in particular the intensity priors. In future works, we plan to include more structures or sub-structures and model the effects of age on the priors. We hope that the method, available in open source, will help neuroscience researchers to include more subcortical regions in their structural and functional imaging studies.

## Materials and methods

### Data acquisition

Our parcellation method has been developed for the MP2RAGEME sequence (Caan et al., 2019). Briefly, the MP2RAGEME consists of two interleaved MPRAGEs with different inversions and four echoes in the second inversion. Based on these images, one can estimate quantitative MR parameters of R1, R2* and QSM. In this work, we used the following sequence parameters: inversion times TI1,2 = 670 ms, 3675.4 ms; echo times TE1 = 3 ms, TE2,1–4 = 3, 11.5, 19, 28.5 ms; flip angles FA1,2 = 4°, 4°; TRGRE1,2 = 6.2 ms, 31 ms; bandwidth = 404.9 MHz; TRMP2RAGE = 6778 ms; SENSE acceleration factor = 2; FOV = 205×205 x 164 mm; acquired voxel size = 0.70×0.7 x 0.7 mm; acquisition matrix was 292 × 290; reconstructed voxel size = 0.64×0.64 x 0.7 mm; turbo factor (TFE) = 150 resulting in 176 shots; total acquisition time = 19.53 min.

T1-maps were computed using a look-up table (Marques et al., 2010). T2*-maps were computed by least-squares fitting of the exponential signal decay over the multi-echo images of the second inversion. R1 and R2* maps were obtained as the inverse of T1 and T2*. For QSM, phase maps were pre-processed using iHARPERELLA (integrated phase unwrapping and background phase removal using the Laplacian) of which the QSM images were computed using LSQR (Li et al., 2014). Skull information was removed through creation of a binary mask using FSL’s brain extraction tool on the reconstructed uniform T1-weighted image and then applied to the quantitative contrasts (Smith, 2002). As all images were acquired as part of a single sequence, no co-registration of the quantitative maps was required (see Figure 9).

![Figure 9.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig9-v2.jpg)

**Figure 9.:** Manual delineations for the 17 structures of interest are overlaid on all images.

### Anatomical structure delineations

Manual delineations of subcortical structures were performed by two raters trained by an expert anatomist, according to protocols optimized to use the better contrast or combination of contrasts for each structure and to ensure a consistent approach across raters. The following 17 structures were defined on a group of 10 subjects (average age 24.4, eight female): striatum (Str), thalamus (Tha), lateral, 3rd and 4th ventricles (LV, 3V, 4V), amygdala (Amg), globus pallidus internal segment (GPi) and external segment (GPe), SN, STN, red nucleus (RN), ventral tegmental area (VTA), fornix (fx), internal capsule (ic), periaqueductal gray (PAG), pedunculopontine nucleus (PPN), and claustrum (Cl). Separate masks for left and right hemisphere were delineated except for 3V, 4V, and fx. In the following the algorithm treats each side separately, resulting in a total of 31 distinct structures (see Figure 1).

### Anatomical interface priors

In order to inform the algorithm, we built a series of priors derived from the manual delineations. Each subject was first co-registered to a MP2RAGEME anatomical template built from 105 subjects co-aligned with the MNI2009b atlas (Fonov et al., 2011) with the SyN algorithm of ANTs (Avants et al., 2008) using successively rigid, affine, and non-linear transformations, high levels of regularization as recommended for the subcortex (Ewert et al., 2019) and mutual information as cost function.

The first computed prior is a prior of anatomical interfaces, recording the most likely location of boundaries between the different structures, defined as follows. Given two delineated structures $i,j$, let $\phi_{i},\phi_{j}$ be the signed distance functions to their respective boundary, that is, $\phi_{i}⁢(x)$ is the Euclidean distance of any given voxel to the boundary of i, with a negative sign inside the structure. Then we define the interface $B_{i|j}$ with the distance function $d_{i|j}$:

$$
d_{i|j}⁢(x)=min⁡(\phi_{i}⁢(x),\phi_{j}⁢(x)-\delta,0)
$$

where $\delta$ is a scale parameter for the thickness of the interface. These interfaces functions are not symmetrical, as the intensity inside i next to j is generally different from the intensity inside j next to i. Based on this definition, the prior for a given interface based on N manual delineations is given by:

$$
P(x\inB_{i|j})∼\frac{1}{\sqrt{2⁢\pi⁢\sigma_{i|j}^{2}⁢(x)}}exp-\frac{1}{2}\frac{\mu_{i|j}^{2}⁢(x)}{\sigma_{i|j}^{2}⁢(x)}\mu_{i|j}⁢(x)=\frac{1}{N}⁢\sumn\inNd_{i|j,n}⁢(x),\sigma_{i|j}⁢(x)=\sqrt{\frac{1}{N}⁢\sumn\inN(d_{i|j,n}⁢(x)-\mu_{i|j}⁢(x))^{2}}+\delta
$$

These probability functions are calculated for all possible configurations including $i|i$, which represent the inside of each structure. We thus have a total of $N^{2}$ functions, but only a few are non-zero at a given voxel x, and we may keep only the 16 largest values to account for any number of interfaces in 3D (Bazin et al., 2007). Finally, we need to scale the prior to be globally consistent with the priors below by assuming that the 95th percentile of the highest kept $P(x\inB_{i|j})$ values have a probability of 0.95. The scale parameter $\delta$ is set to one voxel, representing the expected amount of partial voluming. The resulting interface prior is shown in Figure 10A.

![Figure 10.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig10-v2.jpg)

### Anatomical skeleton priors

Next, we defined priors for the skeleton of each structure, representing their essential shape regardless of exact boundaries (Blum, 1973). As we are mostly interested in the most likely components of the skeleton or medial axis $S_{i}$, we follow a simple method to estimate its location:

$$
S_{i}={x,|\nabla\phi_{i}(x)|<\frac{1}{2}}
$$

We define as $s_{i}⁢(x)$ the signed distance function of this discrete skeleton, and define prior probabilities as above:

$$
P(x\inS_{i})∼\frac{1}{\sqrt{2⁢\pi⁢\sigma_{i}^{2}⁢(x)}}exp-\frac{1}{2}\frac{\mu_{i}^{2}⁢(x)}{\sigma_{i}^{2}⁢(x)}\mu_{i}⁢(x)=\frac{1}{N}⁢\sumn\inNs_{i,n}⁢(x)⁢\sigma_{i}⁢(x)=\sqrt{\frac{1}{N}⁢\sumn\inN(s_{i,n}⁢(x)-\mu_{i}⁢(x))^{2}}+\delta
$$

The skeletons are defined inside each structure, which implies $P(x\inS_{i})\leqP(x\inB_{i|i})$. To respect this relationship, we scale $P(x\inS_{i})$ with the same factor as $P(x\inB_{i|i})$ but use $\sqrt{P(x\inS_{i})}$ when combining probabilities during the estimation stage. The obtained anatomical skeleton priors are given on Figure 10B.

### Interface intensity priors

While anatomical priors already provide rich information, they are largely independent of the underlying MRI. From the co-aligned quantitative MRI maps and manual delineations, we defined intensity priors for every interface $i|j$, in the form of intensity histograms to ensure a flexible representation of intensity distributions. Given a quantitative contrast $R_{n}⁢(x)$, we built a histogram $H_{i|j,n}$ for each subject n and interface $i|j$. Histograms have 200 bins covering the entire intensity range within a radius of 10 mm from any of the delineated structures. To obtain an average histogram, we combine each histogram with a weighting function $w_{n}⁢(x)$ giving the likelihood of the subject’s intensity measurement compared to the group:

$$
w_{i|j,n}(x)=P(x\inB_{i|j})\frac{1}{\sqrt{2⁢\pi⁢\sigma_{R}^{2}}}exp-\frac{1}{2}\frac{(R_{n}⁢(x)-\mu_{R}⁢(x))^{2}}{\sigma_{R}⁢(x)^{2}}
$$

where $\mu_{R}⁢(x)$ is the median of the $R_{n}⁢(x)$ values at x, and $\sigma_{R}⁢(x)$ is 1.349 times the inter-quartile range of $R_{n}⁢(x)$. These are robust estimators of the mean and standard deviation, used here to avoid biases by intensity outliers. To further combine the R1, R2*, and QSM contrasts we take the geometric mean of the histogram probabilities: $H_{i|j}⁢(x)=\prod_{R}H_{i|j}⁢(R⁢(x))^{1/3}$.

### Global volume priors

The last type of priors extracted from manual delineations are volume priors for each of the structure. Here, we assume a log-normal distribution for the volumes $V_{i}$ and simply estimate the mean $\mu_{V,i}$ and standard deviation $\sigma_{V,i}$ of $log⁡V_{i,n}$ over the subjects.

### Voxel-wise posterior probabilities

When parcellating a new subject, we first co-register its R1, R2*, and QSM maps jointly to the template and use the inverse transformation to deform the anatomical priors into subject space. Then we derive voxel-wise posteriors as follows:

$$
P(x\inB_{i|j}|R(x))∼P(x\inB_{i|j})H_{i|j}(x)if i\neqjandP(x\inB_{i|i}|S_{i}(x),R(x))∼max(P(x\inB_{i|i}),P(x\inS_{i})^{1/2})H_{i|i}(x)
$$

Once again we should compute all possible combinations, but due to the multiplication of the priors we can restrict ourselves to the 16 highest probabilities previously estimated. To balance the contribution of the anatomical priors and the intensity histograms, we also need to normalize the intensity priors sampled on the subject’s intensities. We use the same approach, namely assuming that the 95th percentile of the highest kept $H_{i|j}⁢(x)$ values have a probability of 0.95, separately for each contrast. The voxel-wise parcellation and posteriors obtained are shown in Figure 11A.

![Figure 11.](https://cdn.elifesciences.org/articles/59430/elife-59430-fig11-v2.jpg)

### Markovian diffusion

The voxel-wise posteriors are independent from each other and do not reflect the continuous nature of the structures. The next step is to combine information from neighboring voxels. We define a sparse Markov Random Field model for the posteriors:

$$
P(x\inB_{i|j}|R,S,C)=\sumy\inC⁢(x)P(y∼x|R)P(y\inB_{i|j}|R,S,C)
$$

with $P(y∼x|R)=\prod_{R}exp-(R(y)-R(x))^{2}/2\sigma_{R}^{2}$, where $\sigma_{R}$ is the median of the standard deviations $\sigma_{i|j,R}$ of the contrast histograms $H_{i|j}⁢(R⁢(x))$. The neighborhood $C⁢(x)$ is defined as x itself and the four 26-connected neighboring voxels with highest probability $P(y∼x|R)$, thus representing the neighbors most likely to be connected to x. The model is similar to a diffusion process and can be estimated with an iterated conditional modes (ICM) approach, updating sequentially the probabilities (Bazin and Pham, 2007):

$$
P(x\inB_{i|j}|R,S,C)←\sumy\inC⁢(x)P(y∼x|R)P(y\inB_{i|j}|R,S,C)
$$

from the initial voxel-wise posteriors until the ratio of changed parcellation labels decreases below 0.1, typically within 50–80 iterations. The diffused probabilities and parcellation are shown in Figure 11B.

### Topology correction

The final step of the parcellation algorithm takes a global view of the individual structures, growing from the highest posterior values inside toward the boundaries. This region growing approach makes the implicit assumption that posterior maps should be monotonically decreasing from inside to outside, which is not necessarily the case. Therefore, we perform first a topology correction step on the individual structure posteriors $P(x\ini|R,B,S,C)=max_{i|j}P(x\inB_{i|j}|R,S,C)$ with a fast marching algorithm (Bazin and Pham, 2007). While the corrected posterior is very similar to the original one (see Figure 11C), it ensures that all regions obtained by growing to a threshold have spherical object topology.

### Anatomical region growing

Last, we turn the posteriors into optimized parcellations, by growing them concurrently (to avoid overlaps) until the target volume for each structure is reached. Given the volume $V_{i}⁢(R,B,S,C)$ of the parcellation of the diffused and topology-corrected posteriors, we define the following target volume:

$$
V^_{i}=P⁢(V_{i}|\mu_{V,i},\sigma_{V,i})⁢V_{i}+(1-P⁢(V_{i}|\mu_{V,i},\sigma_{V,i}))⁢exp⁡\mu_{V,i}
$$

taking a weighted average of the volume estimated from the data and the prior volume. This approach ensures that even in extreme cases where some structures have low posteriors, they are still able to grow to a plausible size. The region growing algorithm is driven from the most likely voxels, defined as $P(x\ini|R,B,S,C)-max_{j\neqi}P(x\inj|R,B,S,C)$, and further modulated to follow isocontours of the skeleton prior:

$$
P(x←y)∼P(y\ini|R,B,S,C)-max_{j\neqi}P(y\inj|R,B,S,C)-|P(y\inS_{i})-P(x\inS_{i})|
$$

Directionality of internal structures is a useful tool for understanding mechanical function in bones (Maquer et al., 2015). Here, we adapt this concept by using the skeleton isocontours as a representation of internal directionality, maintaining the intrinsic shape of structures. Thus, voxels with highest probability compared to the other structures and with similar distance to the internal skeleton are preferentially selected. The final parcellation is given in Figure 11C.

### Validation metrics

To validate the method against manual expert delineations, we compared the MASSP results and the expert delineations with the following three measures:

We computed all three measures for the manual delineations from the two independent raters, as well as the ratio of overlaps (automated over manual) and distances (manual over automated) to compare both performances, as detailed in the Results section.

### Comparisons with other automated methods

To assess the performance of MASSP compared to existing parcellation tools, we ran Freesurfer (Fischl et al., 2002), FSL FIRST (Patenaude et al., 2011) and a multi-atlas registration approach (co-registering 9 of the 10 manually delineated subjects on the remaining one with ANTs [Avants et al., 2008] and labeling each structure by majority voting, similarly to the MAGeT Brain approach of Chakravarty et al., 2013). Freesurfer and FIRST were run on the skull-stripped R1 map, while the multi-atlas approach used all three R1, R2*, and QSM contrasts. All methods were compared in terms of Dice overlap, dilated overlap and average surface distance. We also assessed the presence of a systematic volume bias, defined as the average of the signed difference of the estimated structure volume to the manually delineated volume, normalized by the manually delineated volume.

### Application to new MRI contrasts

Before applying MASSP to unseen contrasts, we need to convert its intensity prior histograms $H_{i|j,R}$ to the new intensities. In order to perform this mapping, we first created a groupwise median of the HCP subjects, by co-registering every subject to the MASSP template using ANTs with non-linear registration and both T1w, T2w contrasts matched to the template’s R1 and R2* maps. The histogram bins are then updated as follows:

$$
H_{bin,i|j,R}≡\sumx|R⁢(x)\inbinP(x\inB_{i|j})H_{i|j,R⁢1}H_{i|j,R⁢2⁣*}H_{i|j,Q⁢S⁢M}
$$

adding the joint probability of the quantitative contrasts weighted by their importance for each interface to define the new intensity histograms. This model is essentially projecting the joint likelihood of the MASSP contrasts onto the new contrasts, assuming that the co-registration between the two is accurate enough. With these new histograms, we compared the test-retest reliability and overall agreement of MASSP with Freesurfer parcellations included in the HCP pre-processed data set.

### Measurement of structure thickness

Finally, when comparing derived measures obtained over the lifespan with MASSP compared to manual delineations, we explored the utility of a shape thickness metric, based on the medial representation. Given the signed distance function $\phi_{i}$ of the structure boundary and si of the structure skeleton, the thickness is given by:

$$
t⁢h_{i}⁢(x)=2⁢(s_{i}⁢(x)-\phi_{i}⁢(x))
$$

Like in cortical morphometry, thickness is a local measure, defined everywhere inside the structure, and expected to provide additional information about anatomical variations. Indeed, a similar measure of shape thickness has recently been able to highlight subtle anatomical changes in depression (Ho et al., 2020).

### Software implementation

The proposed method, Multi-contrast Anatomical Subcortical Structure Parcellation (MASSP), has been implemented as part of the Nighres toolbox (Huntenburg et al., 2018), using Python and Java for optimized processing. The software is available in open source from (release-1.3.0) and . A complete parcellation pipeline is included with the Nighres examples. Computations take under 30 min per subject on a modern workstation.

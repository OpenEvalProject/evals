# Author response - Round 1

Authors:
- Chananchida Sang-aram ([ORCID: 0000-0002-0922-0822](https://orcid.org/0000-0002-0922-0822))
- Robin Browaeys ([ORCID: 0000-0003-2934-5195](https://orcid.org/0000-0003-2934-5195))
- Ruth Seurinck
- Yvan Saeys ([ORCID: 0000-0002-0415-1506](https://orcid.org/0000-0002-0415-1506))

## Response text

DOI: [10.7554/eLife.88431.3.sa3](https://doi.org/10.7554/eLife.88431.3.sa3)

The following is the authors’ response to the original reviews.

Reviewer #1 (Recommendation for the authors)

I only have one comment for improvement of this study and it has to do with the comparison of simulators that they conducted. There are many other simulators around now, including scDesign3, spaSim, SPIDER, SRTSIM, etc. Are any of those methods worth including in the comparison?

Indeed, many of the mentioned simulators did not exist when we initially developed synthspot, and upon closer examination, they are not directly comparable to our tool.

• scDesign3: The runtime of scDesign3 is quite long as a result of its generative model. The example provided in its tutorial only simulates 183 genes and takes over seven minutes when using four cores on a system with Intel Xeon E5-2640 CPUs running at 2.5GHz. In a small downsampling analysis, we simulated 10, 50, 100, and 150 genes with scDesign3 and observed runtimes of 30, 130, 245, and 360 seconds, respectively. This seems to indicate a linear relationship between the number of genes and the runtime, therefore rendering it unsuitable for simulating whole-transcriptome datasets for deconvolution.

• spaSim: spaSim focuses on modelling cell locations in different tissue structures but does not provide gene expression data. It is designed for testing cell colocalization capabilities rather than simulating gene expression.

• SPIDER: Although SPIDER appears to have some overlap with our work, it seems to be in the early stages of development. The GitHub repository contains only two scripts without any documentation, and the preprint does not provide instructions on how to use the tool.

• SRTSim: SRTSim explicitly states in its publication that it is not suitable for evaluating cell type deconvolution, as its focus is on simulating gene expression data without modelling cell type composition.

• scMultiSim: scMultiSim, like scDesign3, is limited in its capability to model the entire transcriptome.

Nonetheless, the inherent modularity of our Nextflow framework makes it possible for users to simply run the deconvolution methods on data that has been simulated by other simulators if need be.

Additionally, we have added the following rationale for why we developed synthspot in “Synthspot allows simulation of artificial tissue patterns”:

“On the other hand, general-purpose simulators are typically more focused on other inference tasks, such as spatial clustering and cell-cell communication, and are unsuitable for deconvolution. For instance, generative models and kinetic models like those of scDesign3 and scMultiSim are computationally intensive and unable to model entire transcriptomes. SRTSim focuses on modeling gene expression trends and does not explicitly model tissue composition, while spaSim only models tissue composition without gene expression.”

The other aspect of the simulation comparison that I'm missing is some kind of spatial metric. There are metrics about feature correlation, sample-sample correlation, library size, etc. But, what about spatial correlation (e.g., Moran's I or similar). Perhaps comparing the distribution of Moran's I across genes in a simulated and real dataset would be a good first start.

We would like to clarify that synthspot does not actually simulate the spatial location of spots, but synthetic regions where spots from the same region share similar compositions. Hence, incorporating a spatial metric in the comparison is not feasible. However, as RCTD is the only method that explicitly uses spot locations in its model (Supplementary Table 2, "Location information"), we believe that generating synthetic datasets with actual coordinates would not significantly impact the conclusions of the study.

Reviewer #2 (Public Review)

On the other hand, the authors state that in silver standard datasets one half of the scRNA-seq data was used for simulation and the other half was used as a reference for the algorithms, but the method of splitting the data, i.e., at random or proportionally by cell type, was not specified.

The data was split proportionally by cell type. To clarify this, we have included an additional sentence in the main text under the first paragraph of “Cell2location and RCTD perform well in synthetic data”, as well as in Figure S2.

Reviewer #2 (Recommendation for the authors)

Figure legends in Figures 3, 4 and across most Supplementary material are almost illegible. Please consider increasing font size for better readability.

Thank you for bringing this to our attention. The font size has been increased for all main and supplementary figures. Additionally, the supplementary figures have also been exported in higher resolution.

Supplementary Notes Figure 2c reads "... total count per sampled multiplied by..."

This has been adapted, as well as the captions of Supplementary Notes Figure 3c and 4c which had the same typo.

Review #3 (Public review)

The simulation setup has a significant weakness in the selection of reference single-cell RNAseq datasets used for generating synthetic spots. It is unclear why a mix of mouse and human scRNA-seq datasets were chosen, as this does not reflect a realistic biological scenario. This could call into question the findings of the "detecting rare cell types remains challenging even for top-performing methods" section of the paper, as the true "rare cell types" would not be as distinct as human skin cells in a mouse brain setting as simulated here.

We appreciate the reviewer’s concern and would like to clarify that within one simulated dataset, we never mix mouse and human scRNA-seq data together. The synthetic spots generated for the silver standards are always sampled from a single scRNA-seq or snRNA-seq dataset. Specifically, for each of the seven public scRNA-seq datasets, we generate synthetic datasets with one of nine abundance patterns, resulting in a total of 63 synthetic datasets. These abundance patterns only affect the sampling priors that are used—the spots are still created with combinations of cells sampled from the same dataset.

Furthermore, it is unclear why the authors developed Synthspot when other similar frameworks, such as SRTsim, exist. Have the authors explored other simulation frameworks?

While there are other simulation frameworks available now, synthspot was designed to specifically address the requirements of our study, offering unique capabilities that make it suitable for deconvolution evaluation. Moreover, many of the simulators did not exist when we initially developed our tool. We have added the following rationale for why we developed synthspot in “Synthspot allows simulation of artificial tissue patterns”:

“On the other hand, general-purpose simulators are typically more focused on other inference tasks, such as spatial clustering and cell-cell communication, and are unsuitable for deconvolution. For instance, generative models and kinetic models like those of scDesign3 and scMultiSim are computationally intensive and unable to model entire transcriptomes. SRTSim focuses on modeling gene expression trends and does not explicitly model tissue composition, while spaSim only models tissue composition without gene expression.”

In our response to Reviewer 1 copied below, we also outline specific reasons why other simulators were not suitable for our benchmark:

• scDesign3: The runtime of scDesign3 is quite long as a result of its generative model. The example provided in its tutorial only simulates 183 genes and takes over seven minutes when using four cores on a system with Intel Xeon E5-2640 CPUs running at 2.5GHz. In a small downsampling analysis, we simulated 10, 50, 100, and 150 genes with scDesign3 and observed runtimes of 30, 130, 245, and 360 seconds, respectively. This seems to indicate a linear relationship between the number of genes and the runtime, therefore rendering it unsuitable for simulating whole-transcriptome datasets for deconvolution.

• spaSim: spaSim focuses on modelling cell locations in different tissue structures but does not provide gene expression data. It is designed for testing cell colocalization capabilities rather than simulating gene expression.

• SPIDER: Although SPIDER appears to have some overlap with our work, it seems to be in the early stages of development. The GitHub repository contains only two scripts without any documentation, and the preprint does not provide instructions on how to use the tool.

• SRTSim: SRTSim explicitly states in its publication that it is not suitable for evaluating cell type deconvolution, as its focus is on simulating gene expression data without modelling cell type composition.

• scMultiSim: scMultiSim, like scDesign3, is limited in its capability to model the entire transcriptome.

Finally, we would have appreciated the inclusion of tissue samples with more complex structures, such as those from tumors, where there may be more intricate mixing between cell types and spot types.

We acknowledge the reviewer's suggestion and have incorporated a melanoma dataset from Karras et al. (2022) in response to this suggestion. This study profiled melanoma tumors by using both scRNA-seq and spatial technologies. The scRNA-seq consists of eight immune cell types and seven melanoma cell states. We have included this study as an additional silver standard and case study, the latter of which is presented in a separate section following the liver analysis (and a corresponding section in Methods).

We found that method performances on synthetic datasets generated from this melanoma dataset follow previous trends (Figure S3-S5). However, the inclusion of the case study led to the following changes in the overall rankings: cell2location and RCTD are now tied for first place (previously RCTD ranked first), and Seurat and SPOTlight have swapped places. Despite these changes, the core messages and conclusions of our paper remain unchanged. All relevant figures (Figures 1a, 2, 3a, 4a, 6b, 7a, S3-S6, S9) have been updated to incorporate these new analyses and results.

Review #3 (Recommendation for the authors)

To maintain consistency in the results, it is recommended to exclude the human scRNAseq set when generating synthetic spots. Furthermore, addressing the other significant weaknesses mentioned earlier would be beneficial.

Please refer to our response to the public review where we address the same remark.

It is essential to differentiate this work from previous benchmarking and simulation frameworks.

In addition to the rationale on why we developed our own framework (see response to the public review), we have included the following text in the discussion that highlights our versatile approach when using a real spatial dataset for evaluation:

“In the case studies, we demonstrated two approaches for evaluating deconvolution methods in datasets without an absolute ground truth. These approaches include using proportions derived from another sequencing or spatial technology as a proxy, and leveraging spot annotations, e.g., zonation or blood vessel annotations, that typically have already been generated for a separate analysis.”

Furthermore, we conducted an extra analysis in the liver case study, generating synthetic datasets with one experimental protocol and using the remaining two as separate references (Figure S13). This further illustrates the usefulness of our simulation framework, which we mentioned by appending this sentence in the discussion:

“As in our silver standards, users can select the abundance pattern most resembling the real tissue to generate the synthetic spatial dataset, as we have also demonstrated in the liver case study.”

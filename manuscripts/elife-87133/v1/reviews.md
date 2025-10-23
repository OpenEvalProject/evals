# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87133.3.sa0](https://doi.org/10.7554/eLife.87133.3.sa0)

This valuable manuscript presents a new approach to transform multi-omics datasets into images and to exploit Deep Learning methods for image analysis of the transformed datasets. As an example, the method is applied to multi-omics datasets on different cancers. While the evidence in this specific case is solid, whether the method is working as advertised in other settings is not yet known.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87133.3.sa1](https://doi.org/10.7554/eLife.87133.3.sa1)

This study by Sokač et al. entitled "GENIUS: GEnome traNsformatIon and spatial representation of mUltiomicS data" presents an integrative multi-omics approach which maps several genomic data sources onto an image structure on which established deep-learning methods are trained with the purpose of classifying samples by their metastatic disease progression signatures. Using published samples from the Cancer Genome Atlas the authors characterize the classification performance of their method which only seems to yield results when mapped onto one out of four tested image-layouts.

A few remaining issues are unclear to me:

1. While the authors have now extended the documentation of the analysis script they refer to as GENIUS, I assume that the following files are not part of the script anymore, since they still contain hard-coded file paths or hard-coded gene counts:

https://github.com/mxs3203/GENIUS/blob/master/GenomeImage/make_images_by_chr.py

https://github.com/mxs3203/GENIUS/blob/master/GenomeImage/randomize_normal_imgs.py

https://github.com/mxs3203/GENIUS/blob/master/GenomeImage/utils.py

If these files are indeed not part of the script anymore, then I would recommend removing them from the GitHub repo to avoid confusion. If, however, they are still part of the script, the authors failed to remove all hard-coded file paths and the software will fail when users attempt to use their own datasets.

2. The authors leave most of the data formatting to the user when attempting to use datasets other than their own presented for this study:

--clinical_data: Path to CSV file that must contain ID and label column we will use for prediction

--ascat_data: Path to output matrix of ASCAT tool. Check the example input for required columns

--all_genes_included: Path to the CSV file that contains the order of the genes which will be used to create Genome Image

--mutation_data: Path CSV file representing mutation data. This file should contain Polyphen2 score and HugoSymbol

--gene_exp_data: Path to the csv file representing gene expression data where columns=sample_ids and there should be a column named "gene" representing the HugoSymbol of the gene

--gene_methyl_data: Path to the csv file representing gene methylation data wherecolumns=sample_ids and there should be a column named "gene1" representing the HugoSymbol of the gene

While this suggests that users will have a difficult time adjusting this analysis script to their own data, this issue is exacerbated by the fact that their analysis script has almost no internal checks whether data format standards were met. Thus, the user will be left with cryptic error messages and will likely give up soon after. I therefore strongly recommend adding internal data format checks and helpful error or warning messages to their script to guide users in the input data adoption process.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87133.3.sa2](https://doi.org/10.7554/eLife.87133.3.sa2)

In this manuscript, Birkbak and colleagues use a novel approach to transform multi-omics datasets in images and apply Deep Learning methods for image analysis. Interestingly they find that the spatial representation of genes on chromosomes and the order of chromosomes based on 3D contacts leads to best performance. This supports that both 1D proximity and 3D proximity could be important for predicting different phenotypes. I appreciate that the code is made available as a github repository. The authors use their method to investigate different cancers and identify novel genes potentially involved in these cancers. Overall, I found this study important for the field.

In the original submission there were several major points with this manuscript could be grouped in three parts:

1. While the authors have provided validation for their model, it is not always clear that best approaches have been used. This has now been addressed in the revised version of the manuscript.

2. Potential improvement to the method

It is very encouraging the use of HiC data, but the authors used a very coarse approach to integrate it (by computing the chromosome order based on interaction score). We know that genes that are located far away on the same chromosome can interact more in 3D space than genes that are relatively close in 1D space. Did the authors consider this aspect? Why not group genes based on them being located in the same TAD? In the revised version of the manuscript, the authors discussed this possibility but did not do any new additional analysis.

Authors claim that "given that methylation negatively correlates with gene expression, these were considered together". This is clearly not always the case. See for example https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02728-5. In the revised version of the manuscript, the authors addressed fully this comment.

3. Interesting results that were not explained.

In Figure 3A methylation seems to be most important omics data, but in 3B, mutations and expression are dominating. The authors need to explain why this is the case. In the revised version of the manuscript, the authors have clarified this.

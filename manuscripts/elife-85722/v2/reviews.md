# Peer review - Round 1

Editors:
- Marisa Nicolás, https://ror.org/0498ekt05 Laboratório Nacional de Computação Científica Brazil

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85722.sa0](https://doi.org/10.7554/eLife.85722.sa0)

This study introduces Phantasus, a useful tool accessible through both web and local applications, designed to analyze transcriptome data derived from microarray or RNA-seq technologies. The compelling tool facilitates normalization, data visualization, and differential expression analysis. Phantasus represents a valuable contribution to the biomedical community, enabling individuals without extensive bioinformatics expertise to analyze new transcriptomic data or reproduce studies effectively.


---

# Peer review - Round 1

Editors:
- Marisa Nicolás, https://ror.org/0498ekt05 Laboratório Nacional de Computação Científica Brazil

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85722.sa1](https://doi.org/10.7554/eLife.85722.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Phantasus: web-application for visual and interactive gene expression analysis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Marisa Nicolás as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Ivan Rodrigo Wolf (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions (for the authors):

1) Improve English by checking and correcting misspelled words, such as typo errors, a few wrong or missing prepositions, punctuation, and the correct verb forms in some sentences.

2) Authors need to improve the details of local installation and tutorials for the end user.

3) Local functionality of the Phantasus through its Bioconductor package requires significant improvements to reach best practices in analyzing bulk RNA-seq data.

Reviewer #1 (Recommendations for the authors):

Phantasus is a good initiative as a tool that will be helpful for both experienced users in bioinformatics analysis and beginners. The manuscript describes all aspects of the tool needed to perform the tests with microarray samples and RNA-seq data.

For the case studies described in the manuscript, it would be a good idea for the authors to describe the RNA-seq tutorial in more detail.

The online version is user-friendly and aims to perform analyses using the tools from differential expression (by limma or DEGseq2), clustering (K-means, NN, or HC), Plots (Chart, PCA, GSEA, Volcano), and Pathway analysis (via Enrich or FGSEA).

The homepage contains a dataset selected by authors (GSE53986) and a list of diseases from TCGA (Acute Myeloid Leukemia to Uveal Melanoma). However, the information about the dataset for diseases of TCGA data needs to be included for the users.

Regarding the English written in the MS, using a spell checker, I found almost 60 misspelled words, such as typo errors. Also, the authors need to check a few wrong or missing prepositions, punctuation, and the right choice of verb forms in some sentences.

Reviewer #2 (Recommendations for the authors):

I would like to congratulate the authors for the development of Phantasus. The tool requires a small learning curve and can help researchers with less experience in bioinformatics. However, I have some general suggestions regarding the manuscript.

I notice some typos throughout the text, for your information:

PDF – page 8 line 181 – "procduces" – do you mean "produces"?

PDF – page 9 line 187 – "apthways" – do you mean "pathways"?

PDF – page 9 line 193 – there is no need to repeat the word "array" after "Arrays"

PDF – page 28 line 397 – do you mean "Submit" instead of "OK" ?

Also, the ARCHS4 is now plublished https://www.nature.com/articles/s41467-018-03751-6. I recommend changing the preprint citation to the final publication.

At the end of the manuscript, two appendices have tutorials on how to use the tool. However, the tutorial becomes superficial when using the RNA-Seq data in Appendix 3. I will cite some examples:

– It is not clear which column is used to sort the result table.

– There is no mention of the need to select the lines before opening the volcano graph to show the gene symbols on the graph.

– The padj and stat filter is mentioned only after the results are displayed.

– Contrast settings (such as what was selected in Class A and Class B in the Tool/Differential Expression/DESeq2 experimental menu entry) were not shown.

As such, I would like to see the same level of detail that is presented in the tutorial in Appendix 2, as RNA-Seq data is of great interest to researchers today.

Additionally, I believe that the authors need to improve the details of local installation and tutorials for the end user, below I will mention the main difficulties of the process.

When you open the Phantasus github page there are no instructions on how you can install Phantasus using the repository itself, only links to other sites and a redundant link to github repo itself. This can be improved with the installation information that is on Docker hub.

When visiting the image link on Docker Hub ther is no instructions on how to run or configure the container, but the instructions on how to install Phantasus R package through github. This can be improved with the information already present in the Phantasus documentation.

Now, regarding the R package installation instructions. I installed the listed dependencies and created an anaconda environment with a clean install of R. The Bioconductor package installation method does not work. Even the package available through the conda package installer did not work (but I believe this is the responsibility of the Bioconda maintainers and not the authors). The github install method (from the dockerhub page) didn't work either. Aware that installation errors can come from my computer's configuration, I chose to install using Docker.

The instructions on how to run the docker container in the documentation link on the github page let you download the container. However, the service only started correctly following the docker-compose instructions, probably due to some error in the docker run command from the documentation.

Finally, after these improvements in the installation documentation, the installation process can become less confusing, and the end user can benefit from Phantasus more easily.

# Phantasus, a web application for visual and interactive gene expression analysis

## Authors

- Maksim Kleverov<sup>1</sup> ([ORCID: 0009-0008-0353-8945](https://orcid.org/0009-0008-0353-8945))
- Daria Zenkova<sup>1</sup>
- Vladislav Kamenev<sup>1</sup>
- Margarita Sablina<sup>1</sup>
- Maxim N Artyomov<sup>2</sup>
- Alexey A Sergushichev<sup>1</sup> ([ORCID: 0000-0003-1159-7220](https://orcid.org/0000-0003-1159-7220)) †

### Affiliations

1. https://ror.org/04txgxn49 ITMO University, Computer Technologies Laboratory Saint Petersburg Russian Federation
2. https://ror.org/01yc7t268 Washington University in St. Louis School of Medicine, Department of Pathology and Immunology St Louis United States

† Corresponding author

## Abstract

Transcriptomic profiling became a standard approach to quantify a cell state, which led to the accumulation of huge amount of public gene expression datasets. However, both reuse of these datasets or analysis of newly generated ones requires significant technical expertise. Here, we present Phantasus: a user-friendly web application for interactive gene expression analysis which provides a streamlined access to more than 96,000 public gene expression datasets, as well as allows analysis of user-uploaded datasets. Phantasus integrates an intuitive and highly interactive JavaScript-based heatmap interface with an ability to run sophisticated R-based analysis methods. Overall Phantasus allows users to go all the way from loading, normalizing, and filtering data to doing differential gene expression and downstream analysis. Phantasus can be accessed online at https://alserglab.wustl.edu/phantasus or can be installed locally from Bioconductor ( https://bioconductor.org/packages/phantasus ). Phantasus source code is available at https://github.com/ctlab/phantasus under an MIT license.

## Introduction

Transcriptomic profiling is a ubiquitous method for whole-genome-level profiling of biological samples (Stark et al., 2019). Moreover, the deposition of these data into one of the public repositories has become a standard in the field, leading to the accumulation of a huge amount of publicly available data. The most significant example is the NCBI Gene Expression Omnibus (GEO) project (Barrett et al., 2013), which stores information from more than 225,000 studies.

Sharing of transcriptomic data opens up possibilities for reusing them: instead of carrying out a costly experiment, a publicly available dataset can be used, thus decreasing the cost and accelerating the research (Byrd et al., 2020). However, the standard approach for gene expression analysis requires significant technical expertise. In particular, many analysis methods are implemented in R as a part of Bioconductor project ecosystem (Gentleman et al., 2004), and thus one has to have programming skills in R to use them. On the other hand, domain knowledge is beneficial to improve quality control of the data, which is especially important when working with the publicly available data, as well as generation of biological hypotheses (Wang et al., 2016).

A number of applications have been developed with the aim to simplify analysis of transcriptomic datasets (see Appendix 1 for details). In particular, web-based applications remove the burden of setup and configuration from the end users, thus lowering the entry threshold. Shiny framework (Chang, 2022) revolutionized the field as it became easy to create a web interface for R-based pipelines, which led to a significant growth of web applications for gene expression analysis (Ge et al., 2018; Hunt et al., 2022; Mahi et al., 2019; Nelson et al., 2017). However, such applications generally have limited interactivity due to mainly server-side computations. Shiny-independent applications can be more interactive, but they suffer from lack of native R support and require reimplementation of existing methods from scratch (Gould, 2016; Alonso et al., 2015).

Here, we present Phantasus: a web application for gene expression analysis that integrates highly interactive client-side JavaScript heatmap interface with an R-based back-end. Phantasus allows us to carry out all major steps of gene expression analysis pipeline: data loading, annotation, normalization, clustering, differential gene expression, and pathway analysis. Notably, Phantasus provides streamlined access to more than 96,000 microarray and RNA-seq datasets from the GEO database, simplifying their reanalysis. Phantasus can be accessed online at https://alserglab.wustl.edu/phantasus or can be installed locally from Bioconductor. Phantasus is open source, and its code is available at https://github.com/ctlab/phantasus under MIT license (Sergushichev and Kamenev, 2024).

## Results

## Phantasus web application

We developed a web application called Phantasus for interactive gene expression analysis. Phantasus integrates a JavaScript-rich heatmap-based user interface originated from Morpheus (Gould, 2016) with an R back-end via the OpenCPU framework (Ooms, 2014). The heatmap graphical interface provides an intuitive way to manipulate the data and metadata: directly in a web browser the user can create or modify annotations, edit color schemes, filter rows and columns, and so on. On the other hand, the R back-end provides a way to easily run a multitude of computational analysis methods available as R packages. Altogether, this architecture (Figure 1) ensures a smooth experience for performing all common analysis steps: loading datasets, normalization, exploration, visualization, differential expression and gene set enrichment analyses.

![Figure 1.](https://cdn.elifesciences.org/articles/85722/elife-85722-fig1-v2.jpg)

**Figure 1.:** The front-end interface is a JavaScript application that requests the web server to load the data and perform resource-consuming tasks. The core element of the back-end is the OpenCPU-based server, which triggers the execution of R-based analysis methods. Protocol Buffers are used for efficient client-server dataset synchronization.

Several options for loading the gene expression data into Phantasus are available. First, datasets from GEO (Barrett et al., 2013) can be loaded by their identifier. Phantasus supports microarray datasets, which are loaded directly from GEO, as well as RNA-sequencing datasets, for which counts data from third-party databases are used (see section ‘Available datasets’ for details). Second, datasets can be loaded from a gene expression table file in GCT, TSV, CSV, and XLSX formats (with a support for gzip-archived files). Finally, a set of curated datasets is available directly from the home page.

A number of methods can be used to prepare, normalize, and explore the gene expression table. In particular, it is possible to aggregate microarray probe-level data to gene levels, transform and filter the data, conduct a principal component analysis (PCA), perform k-means or hierarchical clustering, etc. These tools allow you to perform a thorough quality control of the dataset and remove outliers if present.

When the dataset is properly filtered and normalized, differential expression analysis using limma (Ritchie et al., 2015) or DESeq2 pipelines (Love et al., 2014) can be carried out. These results can then be used with other web services for downstream analysis, with shortcuts for pathway analysis with Enrichr (Kuleshov et al., 2016) and metabolic network analysis with Shiny GAM (Sergushichev et al., 2016). Additionally, gene set enrichment analysis (GSEA) can be done directly in Phantasus as implemented in the fgsea package (Korotkevich et al., 2021).

All the plots produced by Phantasus during the data exploration and analysis can be exported as vector images in SVG format. This includes heatmaps, PCA plots, gene profiles, enrichment plots, etc. The obtained images can be used for publications as is or adjusted in a vector graphics editor.

Another option for presenting final or intermediate results is session link sharing. When a link is generated, a snapshot with the current dataset and its representation – annotations, color scheme, sample dendrograms, etc. – are saved on the server. The link can be shared with other users, and, when opened, restores the session.

## Stand-alone Phantasus distribution

Aside from using the official mirror (https://alserglab.wustl.edu/phantasus), there is a possibility to set up Phantasus locally. Phantasus can be installed as an R package from Bioconductor (https://bioconductor.org/packages/phantasus) or loaded as a Docker image (https://hub.docker.com/r/alserglab/phantasus). In both cases, almost all of the Phantasus functions will be available from the start.

Some of the Phantasus features require additional server-side setup. Extended support of GEO datasets requires preprocessed expression matrices and platform annotations. Identifier mapping requires organism annotation databases. Pathways enrichment requires pathway databases. The R package and Docker image versions of Phantasus can automatically handle this setup by downloading the required files from https://alserglab.wustl.edu/files/phantasus/minimal-cache. The detailed instructions for installing Phantasus locally are available at https://ctlab.github.io/phantasus-doc/installation.

Importantly, we have introduced a highly scalable data service (HSDS) server (https://alserglab.wustl.edu/hsds/?domain=/counts,), facilitating access to HDF5 files containing precomputed gene count matrices from the official Phantasus mirror. Through this service and a helper R package phantasusLite (https://bioconductor.org/packages/phantasusLite), a stand-alone Phantasus instance selectively loads the count matrix exclusive to the specified dataset, avoiding the need to burden local installations with unnecessarily large files. However, for users prioritizing increased reactivity, the option remains to load these files from the aforementioned cache mirror.

An important feature of the stand-alone version of Phantasus is the ability to share manually curated datasets. Similar to Phantasus session link sharing, one can generate a named session consisting of a dataset and its visual representation. Link to this named session (e.g. https://alserglab.wustl.edu/phantasus/?preloaded=GSE53986.Ctrl_vs_LPS) can then be shared for the other users to view. Such a predictable display of the data can be particularly useful in a publication context.

## Available datasets

Phantasus provides streamlined access to more than 96,649 GEO datasets. For these datasets, the expression values and gene identifiers (Entrez, ENSEMBL, or Gene Symbol) are readily available (Figure 2). Moreover, these datasets are used to populate the initial Phantasus cache, and thus they have low loading times.

![Figure 2.](https://cdn.elifesciences.org/articles/85722/elife-85722-fig2-v2.jpg)

**Figure 2.:** For fully supported datasets, gene expression data is accompanied by gene annotations in a standardized format. Partial support datasets have either incomplete gene expression matrix or gene annotations.Figure 2—source data 1.Figure 2.

Of these 96,649 datasets, 49,846 are microarrays based on 2767 platforms. For 1347 platforms, GEO databases have machine-readable annotations in the annot.gz format with Entrez gene and Gene symbol columns, corresponding to 39,621 datasets. The remaining 10,225 datasets are obtained from platforms that do not have a GEO-provided annotation. For these 1420 platforms, we have automatically marked up user-provided annotations in SOFT format to extract gene identifiers and convert the annotations into annot.gz format.

The RNA-seq subset of the datasets with streamlined access consists of 46,803 datasets. As GEO does not store expression values for RNA-seq datasets, we rely on other databases for the expression data. The first-priority database for RNA-seq gene counts is ARCHS4 (Human, Mouse, and Zoo versions), which covers 35,088 datasets. The other source is the DEE2 database (human, mouse, and other available organisms), which covers an additional 11,715 datasets. The DEE2 database contains run-level quantification, so it has been preprocessed to sum read counts into sample-level tables.

## Case study 1: Basic usage

To illustrate the basic usage of Phantasus, we will consider the dataset GSE53986 (Noubade et al., 2014) from the GEO database (Figure 3). This dataset consists of 16 samples of bone marrow-derived macrophages, untreated and treated with three stimuli: LPS, IFNg, and combined LPS + IFNg. The gene expression was measured with Affymetrix Mouse Genome 430 2.0 Array. Here, we give an overview of the steps; the full walk-through for the analysis is available in Appendix 2.

![Figure 3.](https://cdn.elifesciences.org/articles/85722/elife-85722-fig3-v2.jpg)

As the first step of the analysis, the dataset can be loaded and normalized. The dataset is loaded straightforwardly by the GSE53986 identifier. Because this is a microarray dataset, internally the gene expression values are obtained from GEO. In this particular case, the expression values have not been normalized, but it can be done in Phantasus. From the available normalization options, we select log2 scaling and quantile normalization. Furthermore, we can aggregate microarray probe-level expression values into gene-level expression. We chose the Maximum Median Probe method, which retains only a single probe per gene, the one that has the highest median expression value. Finally, we can filter out lowly expressed genes, for example, by keeping only the top 12000 expressed genes.

After the normalization step, we can apply a number of exploratory techniques. In particular, we can do a PCA, k-means gene clustering, and hierarchical clustering of the samples. From these analyses, we can discover that there is an overall good concordance between the replicates of the same treatment, with an exception of the first replicate in each group. We can conclude that these samples are outliers and remove them before the downstream analysis.

Finally, we can do a comparison between the sample groups, for example, by comparing untreated and LPS-treated samples. As the data has been normalized, we can apply limma for differential gene expression analysis. The result appears as additional gene annotation columns: p-values, log-fold-changes, and other statistics. Next, we can use differential expression results for a pathway enrichment analysis: for example, we can use R-based GSEA via the fgsea package or we can use external tools, such as Enrichr.

## Case study 2: Data reanalysis

To highlight Phantasus’s ability to reanalyze publicly available data in a context of a biological study, let us consider a study by Mowel et al., 2017. The study considers a genomic locus Rroid linked by the authors to homeostasis and function of group 1 innate lymphoid cells (ILC1). The authors hypothesized that Rroid locus controls ILC1s by promoting the expression of Id2 gene, a known regulator of ILCs. To confirm this hypothesis, the authors generated an Id2-dependent gene signature based on an existing transcriptomic data (Shih et al., 2016) and showed its deregulation in Rroid-deficient cells.

The computational analysis described above linking Rroid and Id2 can be replicated in Phantasus in a straightforward way (see Appendix 3 for the detailed walk-through).

First, we can open GEO dataset GSE76466 (Shih et al., 2016), containing gene expression data for Id2-deficient NK cells. Notably, GSE76466 is an RNA-sequencing dataset, without gene expression values stored directly in the GEO database; however, Phantasus loads the dataset leveraging precomputed expression values from the ARCHS4 project (Lachmann et al., 2018). Then we can perform differential gene expression analysis with the limma tool, comparing Id2-deficient and wild-type (WT) natural killer (NK) cells. Id2-dependent gene signature can be obtained by sorting the genes by t column.

Second, RNA-sequencing dataset GSE101458 (Mowel et al., 2017), generated by Mowel and colleagues for Rroid-deficient NK cells, can also be opened in Phantasus. There we can do differential gene expression analysis with DESeq2 and remove lowly expressed genes. Finally, we can input the generated Id2-dependent gene signature into Phantasus gene search field and use GSEA plot tool to obtain an enrichment plot, similar to the one presented by Mowel and colleagues, confirming a potential regulation via Id2.

## Discussion

Here, we present Phantasus: a web tool designed to simplify the analysis of gene expression data and provide streamlined access to tens of thousands of publicly available datasets. This is an important area of development, as evidenced by the numerous tools addressing this and similar objectives. In Appendix 1, we compare some of these tools, and we anticipate the development of more of them in the future. However, this diversity is highly beneficial to the broad research community as it enhances the overall accessibility of gene expression analysis by allowing researchers to find the most suitable tool for their needs.

Phantasus’s uniqueness lies in its highly interactive heatmap-based user interface, integrated with an R and Bioconductor-based back-end. In our experience, this combination effectively supports users from both computational and biological backgrounds. It also provides avenues for extending support to analysis methods available within the R and Bioconductor ecosystem.

A major focus of Phantasus’s development was to provide easy access to publicly available datasets from the GEO database. To our knowledge, Phantasus is the only web application for gene expression analysis that offers streamlined access to both microarray and RNA-seq datasets. Currently, it combines approximately 96,000 datasets, with additional datasets available following some manipulations by the user. About half of these datasets are RNA-sequencing datasets, where quantified gene expression values are not stored in GEO. For this purpose, we integrated the ARCHS4 and DEE2 databases and also made them available remotely from the R environment via the phantasusLite package in a GEOquery-compatible manner.

Phantasus is readily available online at https://alserglab.wustl.edu/phantasus, but it can also be installed as a Bioconductor R package at https://bioconductor.org/packages/phantasus. For further convenience, we provide a Docker image at https://hub.docker.com/r/alserglab/phantasus. Phantasus documentation, including comprehensive installation instructions, is available at https://ctlab.github.io/phantasus-doc/. The Phantasus source code is available at https://github.com/ctlab/phantasus under an MIT license (Sergushichev and Kamenev, 2024).

## Materials and methods

## Web application architecture

Phantasus is a web application that combines an interactive graphical user interface with access to a variety of R-based analysis methods (Figure 1). The front-end, which is JavaScript-based, derives from the Morpheus web application designed for matrix visualization and analysis (Gould, 2016). The back-end is written in R, with an OpenCPU server (Ooms, 2014) translating HTTP-queries from the client into R procedure calls.

The JavaScript client is responsible for the matrix visualization, as well as certain analysis methods. In particular, steps like subsetting the dataset, working with annotations, and basic matrix modification (e.g., log-transformation, scaling, etc.) have client-side implementation. Furthermore, the client supports additional visualization methods such as row profile plots, volcano plot, and others.

The analysis methods that require external data or algorithms are implemented in the form of the phantasus R package to be carried out on the server side. The operations include differential gene expression analysis, PCA, pathway analysis, and others. Commonly, these methods rely on functions that are already available in the existing R packages; for such methods, only wrapper R functions are implemented.

The OpenCPU server is a core component of the Phantasus back-end. The server provides an HTTP API for calling computational methods implemented in R. For each call, OpenCPU creates a new R environment with the required data, in which the method is then executed. OpenCPU can manage these R environments both in a standard single-user R session and, with the help of rApache, in a multi-user manner inside an Apache web server.

The transfer of large objects between the server and the client exploits a binary Protobuf protocol. The Phantasus back-end uses the protolite R package (Ooms, 2021) for object serialization and deserialization. The front-end relies on the protobuf.js module (Coe, 2020).

For further performance improvement, Nginx server is used to wrap the OpenCPU server. Nginx server caches the results of the OpenCPU method calls. If the same method with the same data is called again, the cached result can be returned without any additional computations. Furthermore, Nginx is used to serve static content and manage permissions.

## Data sources and data gathering

The main data source for Phantasus is the NCBI GEO database (Barrett et al., 2013). All of the GEO datasets are identified by a GSEnnnnn accession number (with a subset of the datasets having an additional GDSnnnnn identifier). However, depending on the type of dataset, the processing procedure is different.

The majority of gene expression datasets in the GEO database can be divided into two groups: microarray data and RNA-seq data. While the experiment metadata is available for all of the datasets, the expression matrices are provided only for the microarray datasets. Phantasus relies on the GEOquery package (Davis and Meltzer, 2007) to load the experiment metadata (for all datasets) and expression matrices (for microarray datasets) from GEO.

When a GEO RNA-seq dataset is requested by the user, Phantasus refers to precomputed gene counts databases available in the internal storage. In particular, data from ARCHS4 (Lachmann et al., 2018) and DEE2 (Ziemann et al., 2019) projects are used. Both of these projects contain gene counts and metadata for RNA-seq samples related to different model organisms including but not limited to mouse and human. For any requested RNA-seq dataset, the gene counts are loaded from a single database, whichever covers the highest number of samples.

Next, Phantasus stores gene annotation databases that are used to map genes between different identifier types. These databases are stored in SQLite format compatible with the AnnotationDbi R package (Pagès, 2022). Currently, only human and mouse databases are available, which are based on org.Hs.eg.db and org.Mm.eg.db R packages, respectively.

Pathway databases are stored to be used for GSEA. Currently, gene set collections include the GO biological processes database (Ashburner et al., 2000), the Reactome database (Gillespie et al., 2022), and the MSigDB Hallmark database (Liberzon et al., 2011) for human and mouse.

Finally, for faster access, Phantasus dataset cache is automatically populated by a large compendium of datasets. The automatic pipeline is Snakemake-based and consists of four steps.

First, the pipeline converts DEE2 files into ARCHs4-like HDF5 files. During this procedure, the expression values of runs provided by DEE2 are summed up to the sample level. The second step checks for which microarray platforms GEO contains a curated machine-readable annotation in annot.gz format. The third step tries to generate the machine-readable annotation for the rest of the microarray platforms from the annotations available in the SOFT format. Currently, this step has produced an additional 1300 annot.gz files. The last step goes over all of the microarray datasets with a machine-readable annotation and over all of the RNA-seq datasets with the counts available in ARCHS4 or DEE2. For each such dataset, the cached entry with all of the data and metadata is created and stored.

A snapshot of Phantasus internal storage is available at https://alserglab.wustl.edu/files/phantasus/minimal-cache. It contains preprocessed count files, automatically marked-up annotations, and gene and pathways databases. This snapshot can be used for a local Phantasus setup.

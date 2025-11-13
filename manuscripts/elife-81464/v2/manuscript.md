# Applying causal discovery to single-cell analyses using CausalCell

## Authors

- Yujian Wen<sup>1</sup>
- Jielong Huang<sup>1</sup>
- Shuhui Guo<sup>1</sup>
- Yehezqel Elyahu<sup>2</sup>
- Alon Monsonego<sup>2</sup>
- Hai Zhang<sup>3</sup> †
- Yanqing Ding<sup>4</sup> †
- Hao Zhu<sup>1</sup> ([ORCID: 0000-0001-7384-3840](https://orcid.org/0000-0001-7384-3840)) †

### Affiliations

1. Bioinformatics Section, School of Basic Medical Sciences, Southern Medical University Guangzhou China ([ROR:01vjw4z39](https://ror.org/01vjw4z39))
2. The Shraga Segal Department of Microbiology, Immunology and Genetics, Faculty of Health Sciences, Ben-Gurion University of the Negev Beer-Sheva Israel ([ROR:05tkyf982](https://ror.org/05tkyf982))
3. Network Center, Southern Medical University Guangzhou China ([ROR:01vjw4z39](https://ror.org/01vjw4z39))
4. Department of Pathology, School of Basic Medical Sciences, Southern Medical University Guangzhou China ([ROR:01vjw4z39](https://ror.org/01vjw4z39))
5. Guangdong-Hong Kong-Macao Greater Bay Area Center for Brain Science and Brain-Inspired Intelligence, Southern Medical University Guangzhou China ([ROR:01vjw4z39](https://ror.org/01vjw4z39))
6. Guangdong Provincial Key Lab of Single Cell Technology and Application, Southern Medical University Guangzhou China ([ROR:01vjw4z39](https://ror.org/01vjw4z39))

† Corresponding author

## Abstract

Correlation between objects is prone to occur coincidentally, and exploring correlation or association in most situations does not answer scientific questions rich in causality. Causal discovery (also called causal inference) infers causal interactions between objects from observational data. Reported causal discovery methods and single-cell datasets make applying causal discovery to single cells a promising direction. However, evaluating and choosing causal discovery methods and developing and performing proper workflow remain challenges. We report the workflow and platform CausalCell (http://www.gaemons.net/causalcell/causalDiscovery/) for performing single-cell causal discovery. The workflow/platform is developed upon benchmarking four kinds of causal discovery methods and is examined by analyzing multiple single-cell RNA-sequencing (scRNA-seq) datasets. Our results suggest that different situations need different methods and the constraint-based PC algorithm with kernel-based conditional independence tests work best in most situations. Related issues are discussed and tips for best practices are given. Inferred causal interactions in single cells provide valuable clues for investigating molecular interactions and gene regulations, identifying critical diagnostic and therapeutic targets, and designing experimental and clinical interventions.

## Introduction

RNA-sequencing (RNA-seq) has been used to detect gene expression in a lump of cells for years. Many statistical methods have been developed to explore correlation/association between transcripts in RNA-seq data, including the ‘weighted gene co-expression network analysis’ that infers networks of correlated genes (Joehanes, 2018). Since a piece of tissue may contain many different cells and the sample sizes of most RNA-seq data are <100, causal interactions in single cells, which to a great extent are emergent events (Bhalla and Iyengar, 1999), cannot be revealed by these statistical methods. Averaged gene expression in heterogeneous cells also makes causal interactions blurred or undetectable. Except for some annotated interactions in signaling pathways, most causal interactions in specific cells remain unknown (e.g. in developing cells undergoing rapid fate determination and in diseased cells expressing genes aberrantly).

Single-cell RNA-sequencing (scRNA-seq) has been widely used to detect gene expression in single cells, providing large samples for analyzing cell-specific gene expression and regulation. On statistical data analysis, it is argued that ‘statistics alone cannot tell which is the cause and which is the effect’ (Pearl and Mackenzie, 2019). Corresponding to this, causal discovery is a science that distinguishes between causes and effects and infers causal interactions from observational data. Many methods have been designed to infer causal interactions from observational data. For single-cell analysis, any method faces the three challenges – high-dimensional data, data with missing values, and inferring with incomplete model (with missing variables). The constraint-based methods are a class of causal discovery methods (Glymour et al., 2019; Yuan and Shou, 2022), and the PC algorithm is a classic constraint-based method. Testing conditional independence (CI, CI≠unconditional independence [UI]≠uncorrelation) between variables is at the heart of constraint-based methods. Many CI tests have been developed (Verbyla, 2018; Zhang and Peters, 2011), from the fast GaussCItest to the time-consuming kernel-based CI tests. GaussCItest is based upon partial correlations between variables. Kernel-based CI tests estimate the dependence between variables upon their observations without assuming any relationship between variables or distribution of data. These features of kernel-based CI tests enable relationships between any genes and molecules, not just transcription factors (TFs) and their targets, to be inferred. Thus, CI tests critically characterize constraint-based causal discovery and distinguish causal discovery from other network inferences, including ‘regulatory network inference’ (Nguyen et al., 2021; Pratapa et al., 2020), ‘causal network inference’ (Lu et al., 2021), ‘network inference’ (Deshpande et al., 2019), and ‘gene network inference’ (Marbach et al., 2012).

Kernel-based CI tests are highly time-consuming and thus infeasible for transcriptome-wide causal discovery. Recently other causal discovery methods are reported, especially continuous optimization-based methods (Bello et al., 2022a; Zheng et al., 2018). Thus, identifying the best methods and CI tests, developing reasonable workflows, developing measures for quality control, and making trade-offs between time consumption, network size, and network accuracy are important. This Tools and Resources article addresses the above issues by benchmarking multiple causal discovery methods and CI tests, applying causal discovery to multiple scRNA-seq datasets, developing a causal discovery workflow/platform (called CausalCell), and summarizing tips for best practices. Specifically, the workflow combines feature selection and causal discovery. The benchmarking includes 11 causal discovery methods, 10 CI tests, and 9 feature selection algorithms. In addition, measures for estimating and ensuring the reliability of causal discovery are developed. Our results indicate that when relationships between variables are free of missing variables and missing values, continuous optimization-based methods perform well. Otherwise, the PC algorithm with kernel-based CI tests can better tolerate incomplete models and missing values. Inferred relationships between gene products help researchers draw causal hypotheses and design experimental studies. The remaining sections describe the workflow/platform and data analysis examples, discuss specific issues, and present tips for best practices. The details of methods and algorithms, benchmarking results, and data analysis results are described in appendix files.

## Materials and methods

### Features of different algorithms

Causal discovery cannot be performed transcriptome-wide due to time consumption and the power of methods. A way to choose a subset of genes based on one or several genes of interest is feature selection. A feature selection algorithm combines a search technique and an evaluation measure and works upon one or several response variables (i.e. genes of interest). After obtaining a measure between the response variable(s) and each feature (i.e. variable, gene), a subset of features most related to the response variable(s) are extracted from the whole dataset. Using simulated data and real scRNA-seq data (Appendix 1—table 1), we benchmarked nine feature selection algorithms. The properties and advantages/disadvantages of these algorithms are summarized, with ‘+++’ and ‘+’ indicating the most and least recommended ones (Table 1; Appendix 2—figures 1–7).

**Table 1.**
 Performance of feature selection methods.


<table>
  <thead>
    <tr>
      <th>Algorithm</th>
      <th>Category</th>
      <th>Time consumption</th>
      <th>Accuracy</th>
      <th>Scalability</th>
      <th>Advantage/disadvantage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RandomForest</td>
      <td rowspan="3">Ensemble learning-based methods use many trees of a random forest to calculate the importance of features, then perform regression based on the response variable(s) to identify the most relevant features.</td>
      <td>+</td>
      <td>++</td>
      <td>++</td>
      <td rowspan="3">These algorithms are indeterministic (the same input may generate slightly different outputs). ExtraTrees and RandomForest perform better than XGBoost.</td>
    </tr>
    <tr>
      <td>ExtraTrees</td>
      <td>+</td>
      <td>++</td>
      <td>++</td>
    </tr>
    <tr>
      <td>XGBoost</td>
      <td>++</td>
      <td>+</td>
      <td>+</td>
    </tr>
    <tr>
      <td>BAHSIC</td>
      <td rowspan="3">The three are Hilbert-Schmidt independence criterion (HSIC)-based algorithms. HSIC is used as the measure of dependency between the response variable and features.</td>
      <td>+</td>
      <td>+++</td>
      <td>+</td>
      <td rowspan="2">BAHSIC and SHS are the best and second best.</td>
    </tr>
    <tr>
      <td>SHS</td>
      <td>+</td>
      <td>+++</td>
      <td>+</td>
    </tr>
    <tr>
      <td>HSIC Lasso</td>
      <td>++</td>
      <td>++</td>
      <td>++</td>
      <td>Inferior to BAHSIC and SHS.</td>
    </tr>
    <tr>
      <td>Lasso</td>
      <td rowspan="3">Lasso is a regression analysis method that performs both variable selection and regularization (which adds additional constraints or penalties to a regression model). Lasso, RidgeRegression, and ElasticNet are three regulation terms.</td>
      <td>+++</td>
      <td>+</td>
      <td>+++</td>
      <td rowspan="3">Inferior to BAHSIC and SHS. Accuracy is not high and scalability is poor.</td>
    </tr>
    <tr>
      <td>RidgeRegression</td>
      <td>+++</td>
      <td>+</td>
      <td>+++</td>
    </tr>
    <tr>
      <td>ElasticNet</td>
      <td>+++</td>
      <td>+</td>
      <td>+++</td>
    </tr>
  </tbody>
</table>

_# Time consumption is estimated upon simulated data (Appendix 2—figure 1). Accuracy is estimated upon simulated and real data (Appendix 2—figures 2–7). Scalability is estimated upon simulated data (Appendix 2—figure 2). Advantage/disadvantage is made upon accuracy together with algorithms’ other properties._

Many causal discovery methods have been proposed. Constraint-based causal discovery identifies causal relationships between a set of variables in two steps: skeleton estimation (determining the skeleton of the causal network) and orientation (determining the direction of edges in the causal network). The PC algorithm is a classic and widely recognized algorithm (Glymour et al., 2019). Causal discovery using the PC algorithm is different in that PC can work with different CI tests to perform the first step. We combined the PC algorithm with 10 CI tests to form 10 constraint-based causal discovery algorithms. The properties and advantages/disadvantages of the 10 algorithms are summarized, with ‘+++’ and ‘+’ indicating the most and least recommended ones (Table 2; Appendix 3—figures 1 and 2). In addition to constraint-based methods, there are other kinds of methods, including score-based methods that assign a score function to each directed acyclic graph (DAG) and optimize the score via greedy searches (Chickering, 2003), hybrid methods that combine score-based and constraint-based methods (Solus et al., 2021), and continuous optimization-based methods that convert the traditional combinatorial optimization problem into a continuous program (Bello et al., 2022a; Zheng et al., 2018). When benchmarking the four classes of methods, multiple simulated data, real scRNA-seq data, and signaling pathways were used to evaluate their performance (Appendix 1—table 1).

**Table 2.**
 Performance of causal discovery methods.


<table>
  <thead>
    <tr>
      <th>Methods</th>
      <th>CI tests</th>
      <th>Category</th>
      <th>Time consumption</th>
      <th>Accuracy</th>
      <th>Stability</th>
      <th>Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="10">PC GSP</td>
      <td>GaussCItest</td>
      <td>GaussCItest assumes all variables are multivariate Gaussian, which impairs GussCItest’s performance when data are complex.</td>
      <td>+++</td>
      <td>+</td>
      <td>+++</td>
      <td>Fast and inaccurate</td>
    </tr>
    <tr>
      <td>CMIknn</td>
      <td>Conditional mutual information (CMI) is based on mutual information.</td>
      <td>+++</td>
      <td>++</td>
      <td>+</td>
      <td>Fast and inaccurate</td>
    </tr>
    <tr>
      <td>RCIT</td>
      <td rowspan="2">Two approximation methods of KCIT (the Kernel conditional independence test).</td>
      <td>++</td>
      <td>++</td>
      <td>++</td>
      <td rowspan="2">Fast and moderately accurate</td>
    </tr>
    <tr>
      <td>RCoT</td>
      <td>++</td>
      <td>++</td>
      <td>++</td>
    </tr>
    <tr>
      <td>HSIC.clust</td>
      <td rowspan="3">Extra transformations make HSIC determine if X and Y are conditionally independent given a conditioning set. HSIC.gamma and HSIC.perm employ gamma test and permutation test to estimate a p-value.</td>
      <td>+</td>
      <td>++</td>
      <td>+</td>
      <td rowspan="3">Slow and accurate</td>
    </tr>
    <tr>
      <td>HSIC.gamma</td>
      <td>+</td>
      <td>+++</td>
      <td>++</td>
    </tr>
    <tr>
      <td>HSIC.perm</td>
      <td>+</td>
      <td>+++</td>
      <td>+</td>
    </tr>
    <tr>
      <td>DCC.gamma</td>
      <td rowspan="2">Distance covariance is an alternative to HSIC for measuring independence. DCC.gamma and DCC.perm employ gamma test and permutation test to estimate a p-value.</td>
      <td>+</td>
      <td>+++</td>
      <td>++</td>
      <td rowspan="2">Slow and accurate</td>
    </tr>
    <tr>
      <td>DCC.perm</td>
      <td>+</td>
      <td>+++</td>
      <td>+</td>
    </tr>
    <tr>
      <td>GCM</td>
      <td>The generalized covariance measure-based (also classified as regression-based).</td>
      <td>+</td>
      <td>++</td>
      <td>+++</td>
      <td>Slower than DCC.gamma</td>
    </tr>
    <tr>
      <td colspan="2">GES</td>
      <td>Score-based causal.</td>
      <td>++</td>
      <td>++</td>
      <td>++</td>
      <td>Fast and moderately accurate</td>
    </tr>
    <tr>
      <td colspan="2">DAGMA-nonlinear</td>
      <td>Continuous optimization-based.</td>
      <td>+</td>
      <td>++</td>
      <td>+++</td>
      <td>Performs well with complete models</td>
    </tr>
  </tbody>
</table>

_# Time consumption is estimated upon simulated data (Appendix 3—figure 1). Accuracy is estimated upon the lung cancer cell lines (Figure 2; Appendix 3—figure 2). Stability is estimated upon the relative structural Hamming distance (SHD, a standard distance to compare graphs by their adjacency matrix), which is used to measure the extent an algorithm produces the same results when running multiple times (Appendix 3—table 1). Advantage/disadvantage is made upon accuracy._

The results of benchmarking the 11 causal discovery methods and 10 CI tests show that when causal discovery is without the problems of incomplete models (i.e. ones that miss nodes or edges from the data-generating model) and missing values, nonlinear versions of continuous optimization-based methods (especially DAGMA-nonlinear) perform better than others (Bello et al., 2022a). When causal discovery is applied to a set of highly expressed or differentially expressed genes in an scRNA-seq dataset (which has both missing variables and missing values), the PC algorithm with kernel-based CI tests (especially DCC.gamma) performs well. Therefore, the CausalCell platform includes 4 causal discovery methods (PC, GES, GSP, and DAGMA-nonlinear) to suit different data, together with 10 CI tests and 9 feature selection algorithms.

### Developing the workflow/platform for causal discovery

The CausalCell workflow/platform is implemented using the Docker technique and Shiny language and consists of feature selection, causal discovery, and several auxiliary functions (Figure 1). A parallel version of the PC algorithm is used to realize parallel multi-task causal discovery (Le et al., 2019). In addition, the platform also includes the GES, GSP, and DAGMA-nonlinear methods. PC and GSP can work with 10 CI tests. Annotations of functions and parameters and the detailed description of a causal discovery process are available online.

![Figure 1.](https://cdn.elifesciences.org/articles/81464/elife-81464-fig1-v2.jpg)

**Figure 1.:** Multiple algorithms and functions are integrated and implemented to facilitate and compare feature selection and causal discovery.

### Data input and pre-processing

scRNA-seq and proteomics data generated by different protocols or methods (e.g. 10x Genomics, Smart-seq2, and flow cytometry) can be analyzed. CausalCell accepts log2-transformed data and z-score data and can turn raw data into either of the two forms. A dataset (i.e. the ‘case’) can be analyzed with or without a control dataset (i.e. the ‘control’). Researchers often identify and analyze special genes, such as highly expressed or differentially expressed genes. For each gene in a case and control, three attributes (the averaged expression value, percentage of expressed cells, and variance) are computed. Fold changes of gene expression are also computed (using the FindMarkers function in the Seurat package) if a control is uploaded. Genes can be ordered upon any attribute and filtered upon a combination of five conditions (i.e. expression value, percentage of expressed cells, variance, fold change, and being a TF or not). Since performing feature selection transcriptome-wide is unreliable due to too many genes, filtering genes before feature selection is necessary, and different filtering conditions generate different candidates for feature selection.

Batch effects may influence identifying differentially expressed genes. Since removing batch effects should be performed with raw data before integrating batches and there are varied batch effect removal methods (Tran et al., 2020), it should be performed by the user if necessary.

### Feature selection

Feature selection selects a set of genes (i.e. features) from the candidate genes upon one or multiple genes of interest (i.e. response variables). As above-mentioned, candidate genes are extracted from the whole dataset upon specific conditions because performing feature selection transcriptome-wide is unreliable. Based on the accuracy, time consumption, and scalability of the nine feature selection algorithms (Table 1), BAHSIC is the most recommended algorithm. The joint use of two kinds of algorithms (e.g. Random Forest+BAHSIC) is also recommended to ensure reliability. Feature genes are usually 50–70, but the number also depends on the causal discovery algorithms. Genes can be manually added to or removed from the result of feature selection (i.e., the feature gene list) to address a biological question specifically. The input for causal discovery can also be manually selected without performing feature selection; for example, the user can examine a specific Gene ontology (GO) term.

### Causal discovery

The PC and GSP algorithms can work with the 10 CI tests to provide varied options for causal discovery. In the inferred causal networks, direction of edges is determined by the meek rules (Meek, 1997), and each edge has a sign indicating activation or repression and a thickness indicating CI test’s statistical significance. The sign of an edge from A to B is determined by computing a Pearson correlation coefficient between A and B, which is ‘repression’ if the coefficient is negative or ‘activation’ if the coefficient is positive. In most situations, ‘A activating B’ and ‘A repressing B’ correspond to up-regulated A in the case dataset, with up- and down-regulated B in the case dataset compared with in the control dataset.

There are two ways to construct a consensus network that is statistically more reliable. One way is to run multiple algorithms (i.e. multiple CI tests) and take the intersection of some or all inferred networks as the consensus network (Figure 2). The other is to run an algorithm multiple times and take the intersection of all inferred networks as the consensus network (Figure 3).

![Figure 2.](https://cdn.elifesciences.org/articles/81464/elife-81464-fig2-v2.jpg)

**Figure 2.:** First, nine causal networks were inferred using the nine CI tests. Second, pairwise structural Hamming distances (SHD) between these networks were computed, and the matrix of SHD values was transformed into a matrix of similarity values (using the equation Similarity = exp(-Distance/2σ2), where σ=5). The networks of DCC.gamma, DCC.perm, HSIC.gamma, and HSIC.perm share the highest similarity. Third, a consensus network was built using the networks of the above four CI tests, which was assumed to be closer to the ground truth than the network inferred by any single algorithm. Fourth, each of the nine networks was compared with the consensus network. (A) The cluster map shows the similarity values (darker colors indicating higher similarity). (B) Shared and specific interactions in each algorithm’s network and the consensus network. In each panel, the gray-, green-, and pink-circled areas and numbers indicate the overlapping interactions, interactions identified specifically by the algorithm, and interactions specifically in the consensus network. There are 73 overlapping interactions between DCC.gamma’s network and the consensus network, and 33 interactions were identified specifically by DCC.gamma. Thus, the true positive rate (TPR) of DCC.gamma is 73/ (73+33)=68.9%. The TPRs of DCC.perm, HSIC.gamma, HSIC.perm, GaussCItest, HSIC.clust, cmiKnn, RCIT, and RCoT are 70.2%, 67.6%, 68.9%, 29.5%, 61.8%, 47.9%, 57.1%, and 56.6%, indicating that the two distance covariance criteria (DCC) CI tests perform better than others.

![Figure 3.](https://cdn.elifesciences.org/articles/81464/elife-81464-fig3-v2.jpg)

**Figure 3.:** Numbers on the vertical and horizontal axes represent the percentages of interactions in 1, 2, 3, 4, and 5 networks, respectively. (A) The results of PC+DCC.gamma. (B) The results of PC+DCC.perm. These results indicate that 78% and 64.3% of interactions occurred stably in ≥4 networks, suggesting that the inferred networks are quite stable.

If a scRNA-seq dataset is large, a subset of cells should be sampled to avoid excessive time consumption. We suggest that 300 and 600 cells are suitable for reliable inference if the input is Smart-seq2 and 10x Genomics data, respectively, the input contains about 50 genes, and genes are expressed in >50% cells. Here, reliable inference means that key interactions (those with high CI test significance) are inferred (Appendices 3, 4). More cells are needed if the input genes are expressed in fewer cells and if the input contains >50 genes. Larger sample sizes (more cells) may make more interactions be inferred, but the key interactions are stable (Appendix 3—figure 3). As HSIC.perm and DCC.perm employ permutation to perform CI test, the networks inferred each time may be somewhat different. Our data analyses suggest that interactions inferred by running distance covariance criteria (DCC) algorithms multiple times are quite stable (Figure 3).

Four parameters influence causal discovery. First, ‘set the alpha level’ determines the statistical significance cut-off of the CI test, and large and small values make more and fewer interactions be inferred. Second, ‘select the number of cells’ controls sample size, and selecting more cells makes the inference more reliable but also more time-consuming. Third, ‘select how a subset of cells is sampled’ determines how a subset of cells is sampled. If a subset is sampled randomly, the inferred network is not exactly reproducible (but by running multiple times, the inferred edges may show high consistency, see Figure 3). Fourth, ‘set the size of conditional set’ controls the size of conditional set when performing CI tests; it influences both network topology and time consumption and should be set with care. Since some CI tests are time-consuming and running causal discovery with multiple algorithms are especially time-consuming, providing an email address is necessary to make the result sent to the user automatically.

The performance of different PC+CI tests was intensively evaluated. First, we evaluated the accuracy, time consumption, sample requirement, and stability of PC+nine CI tests using simulated data and the non-small cell lung cancer (NSCLC) cell line H2228 and the normal lung alveolar cells (as the case and control) (Tian et al., 2019; Travaglini et al., 2020). Comparing inferred networks with the consensus network suggests that the two DCC CI tests are most accurate and most time-consuming, suitable for small-scale network inference. RCIT and RCoT, two approximated versions of the KCIT, are moderately accurate and relatively fast, suitable for large-scale network inference. GaussCItest is the fastest and suitable for data with Gaussian distribution (Figure 2; Appendix 3—figure 2). Second, we compared the performance of PC+DCC.gamma, GSP+DCC.gamma, and GES. The former two have comparable performance, and both are more accurate and time-consuming than GES (Appendix 3—figures 4 and 5).

### Verification of causal discovery

We used the five NSCLC cell lines (A549, H1975, H2228, H838, and HCC827), the normal alveolar cells, and genes in specific pathways to validate network inference by PC+DCC.gamma (Tian et al., 2019; Travaglini et al., 2020). First, upon the combined conditions of (a) gene expression value >0.1, (b) gene expression in >50% cells, and (c) fold change >0.3, we identified highly and differentially expressed genes in each cell line against the alveolar cells. Second, we applied gene set enrichment analysis to differentially expressed genes in each cell line using the g:Profiler and GSEA programs. g:Profiler identified ‘Metabolic reprogramming in colon cancer’ (WP4290), ‘Pyrimidine metabolism’ (WP4022), and ‘Nucleotide metabolism’ (hsa01232) as enriched pathways in all cancer cell lines, and GSEA identified ‘Non-small cell lung cancer’ (hsa05223) as an enriched pathway in cancer cell lines (‘WP’ and ‘hsa’ indicate WikiPathways and KEGG pathways). Many studies reveal that glucose metabolism is reprogrammed and nucleotide synthesis is increased in cancer cells. Key features of reprogrammed glucose metabolism in cancer cells include increased glucose intake, increased lactate generation, and using the glycolysis/TCA cycle intermediates to synthesize nucleotides. The networks inferred by PC+DCC.gamma capture these features despite of the absence of metabolites in these datasets. The networks of WP4022 also capture the key features of pyrimidine metabolism. In the networks of hsa05223, over 50% inferred interactions agree with pathway annotations. These results support network inference (Appendix 4).

### Evaluating and ensuring the reliability

Single-cell data vary in quality and sample sizes; thus, it is important to effectively evaluate and ensure the reliability of network inference. Inspired by using RNA spike-in to measure RNA-seq quality (Jiang et al., 2011), we developed a method to evaluate and ensure the reliability of causal discovery. This method includes three steps: extracting the data of several well-known genes and their interactions from certain dataset as the ‘spike-in’ data, integrating the spike-in data into the case dataset, and applying causal discovery to the integrated dataset (the latter two steps are performed automatically when a spike-in dataset is chosen or uploaded). The user can choose a spike-in dataset in the platform or design and upload a spike-in dataset. In the inferred network, a clear separation of genes and their interactions in the spike-in dataset from genes and interactions in the case dataset is an indicator of reliable inference (Appendix 4—figure 1). Some public databases (e.g. the STRING database, https://string-db.org/) can also be used to evaluate inferred interactions (Appendix 4—figures 2 and 3).

## Results

### The analysis of lung cancer cell lines and alveolar epithelial cells

Down-regulated MHC-II genes help cancer cells avoid being recognized by immune cells (Rooney et al., 2015); thus, identifying genes and interactions involved in MHC-II gene down-regulation is important. To assess if causal discovery helps identify the related interactions, we examined the five NSCLC cancer cell lines (A549, H1975, H2228, H838, and HCC827) and the normal alveolar epithelial cells (Tian et al., 2019; Travaglini et al., 2020). For each of the six datasets, we took the five MHC-II genes (HLA-DPA1, HLA-DPB1, HLA-DRA, HLA-DRB1, HLA-DRB5) as the response variables (genes of interest, hereafter also called target genes) and selected 50 feature genes (using BAHSIC, unless otherwise stated) from all genes expressed in >50% cells. Then, we applied the nine causal discovery algorithms to the 50 genes in 300 cells sampled from each of the datasets. The two DCC algorithms performed the best when processing the H2228 cells and lung alveolar epithelial cells (Appendix 5—figures 1 and 2).

The inferred networks also show that down-regulated genes weakly but up-regulated genes strongly regulate downstream targets and that activation and repression lead to up- and down-regulation of target genes. These features are biologically reasonable. Many inferred interactions, including those between MHC-II genes and CD74, between CXCL genes, and between MHC-I genes and B2M, are supported by the STRING database (http://string-db.org) and experimental findings (Figure 4; Appendix 4—figure 2; Castro et al., 2019; Karakikes et al., 2012; Szklarczyk et al., 2021). An interesting finding is the PRDX1→TALDO1→HSP90AA1→NQO1→PSMC4 cascade in H2228 cells. Interactions between PRDX1/TALDO1/HSP90AA1 and NQO1 were reported (Mathew et al., 2013; Yin et al., 2021), but the interaction between NQO1 and PSMC4 was not. Previous findings on NQO1 include that it determines cellular sensitivity to the antitumor agent napabucasin in many cancer cell lines (Guo et al., 2020), is a potential poor prognostic biomarker, and is a promising therapeutic target for patients with lung cancers (Cheng et al., 2018; Siegel et al., 2012), and that mutations in NQO1 are associated with susceptibility to various forms of cancer. Previous findings on PSMC4 include that high levels of PSMC4 (and other PSMC) transcripts were positively correlated with poor breast cancer survival (Kao et al., 2021). Thus, the inferred NQO1→PSMC4 probably somewhat explains the mechanism behind these experimental findings.

![Figure 4.](https://cdn.elifesciences.org/articles/81464/elife-81464-fig4-v2.jpg)

**Figure 4.:** Red → and blue -| arrows indicate activation and repression, and colors indicate fold changes of gene expression compared with genes in the alveolar epithelial cells.

### The analysis of macrophages isolated from glioblastoma

Macrophages critically influence glioma formation, maintenance, and progression (Gutmann, 2020), and CD74 is the master regulator of macrophage functions in glioblastoma (Alban et al., 2020; Quail and Joyce, 2017; Zeiner et al., 2015). To examine the function of CD74 in macrophages in gliomas, we used CD74 as the target gene and selected 50 genes from genes expressed in >50% of macrophages isolated from glioblastoma patients (Neftel et al., 2019). In the networks of DCC algorithms (Appendix 5—figure 3), CD74 regulates MHC-II genes, agreeing with the finding that CD74 is an MHC-II chaperone and plays a role in the intracellular sorting of MHC class II molecules. The network includes interactions between C1QA/B/C, agreeing that they form the complement C1q complex. The identified TYROBP→TREM2→A2M→APOE→APOC1 cascade is supported by the reports that TREM2 is expressed in tumor macrophages in over 200 human cancer cases (Molgora et al., 2020) and that there are interactions between TREM2/A2M, TREM2/APOE, A2M/APOE, and APOE/APOC1 (Krasemann et al., 2017).

### The analysis of tumor-infiltrating exhausted CD8 T cells

Tumor-infiltrating exhausted CD8 T cells are highly heterogeneous yet share common differentially expressed genes (McLane et al., 2019; Zhang et al., 2018), suggesting that CD8 T cells undergo different processes to reach exhaustion. We analyzed three exhausted CD8 T datasets isolated from human liver, colorectal, and lung cancers (Appendix 5—figure 4; Guo et al., 2018; Zhang et al., 2018; Zheng et al., 2017). A key feature of CD8 T cell exhaustion identified in mice is PDCD1 up-regulation by TOX (Khan et al., 2019; Scott et al., 2019; Seo et al., 2019). Using TOX and PDCD1 as the target gene, we selected 50 genes expressed in >50% exhausted CD8 T cells and 50 genes expressed in >50% non-exhausted CD8 T cells, respectively. Transcriptional regulation of PDCD1 by TOX was observed in LCMV-infected mice without mentioning any role of CXCL13 (Khan et al., 2019). Here, indirect TOX→PDCD1 (via genes such as CXCL13) was inferred in exhausted CD8 cells, and direct TOX→PDCD1 was inferred in non-exhausted CD8 T cells (although the expression of TOX and PDCD1 is low in these cells) (Appendix 5—figure 4). Recently, CXCL13 was found to play a critical role in T cells for effective responses to anti-PD-L1 therapies (Zhang et al., 2021b). The causal discovery results help reveal differences in CD8 T cell exhaustion between humans and mice and under different pathological conditions. The PDCD1→TOX inferred in exhausted and non-exhausted CD8 T cells may indicate some feedback between TOX and PDCD1, as on the proteome level, a study reported that the binding of PD1 to TOX in the cytoplasm facilitates the endocytic recycling of PD1 (Wang et al., 2019).

### Identifying genes and inferring interactions that signify CD4 T cell aging

How immune cells age and whether some senescence signatures reflect the aging of all cell types draw wide attention (Gorgoulis et al., 2019). We analyzed gene expression in naive, TEM, rTreg, naive_Isg15, cytotoxic, and exhausted CD4 T cells from young (2–3 months, n=4) and old (22–24 months, n=4) mice (Appendix 5—figures 5; Elyahu et al., 2019). For each cell type, we compared the combined data from all four young mice with the data from each old mouse to identify differentially expressed genes. If genes were expressed in >25% cells and consistently up/down-regulated (|fold change|>0) in most of the 24 comparisons, we assumed them as aging-related (Appendix 5—table 1). Some of these identified genes play important roles in the aging of T cells or other cells, such as the mitochondrial genes encoding cytochrome c oxidases and the gene Sub1 in the mTOR pathway (Bektas et al., 2019; Gorgoulis et al., 2019; Goronzy and Weyand, 2019; Walters and Cox, 2021). We directly used these genes, plus one CD4-specific biomarker (Cd28) and two reported aging biomarkers (Cdkn1b, Cdkn2d) (Gorgoulis et al., 2019; Larbi and Fulop, 2014), as feature genes to infer their interactions in different CD4 T cells in young and old mice. The inferred causal networks unveil multiple findings (Appendix 5—figure 5). First, B2m→H2-Q7 (a mouse MHC class I gene), Gm9843→Rps27rt (Gm9846), and the interactions between the five mitochondrial genes (MT-ATP6, MT-CO1/2/3, and MT-Nd1) were inferred in nearly all CD4 T cells. Second, many interactions are supported by the STRING database (Appendix 4—figure 3). Third, some interactions agree with experimental findings, including Sub1-|Lamtor2 (Chen et al., 2021) and the regulations of these mitochondrial genes by Lamtor2 (Morita et al., 2017). Fourth, Gm9843→Rps27rt→Junb were inferred in multiple CD4 T cells (both Gm9843 and Rps27rt are mouse-specific). Since JUNB belongs to the AP-1 family TFs that are increased in all immune cells during human aging (Zheng et al., 2020), Gm9843→Rps27rt→Junb could highlight a counterpart regulation of JUNB in human immune cells.

## Discussion

### Single-cell causal discovery

Various methods have been proposed to infer interactions between variables from observational data. As surveyed recently (Nguyen et al., 2021; Pratapa et al., 2020), many methods assume linear relationships between variables and the Gaussian distribution of data. These assumptions enable these methods to run fast, handle many genes and even perform transcriptome-wide prediction. However, our algorithm benchmarking results suggest that networks inferred by fast methods with these assumptions should be concerned.

Causal discovery infers causal interactions directly upon observations of variables without assuming relationships between variables and the distribution of data. Because genes and molecules have varied relationships in different cells, causal discovery better satisfies inferring their interactions than other methods. Causal discovery methods have reviewed recently (Glymour et al., 2019; Yuan and Shou, 2022), but workflows and platforms integrating multiple methods for analyzing scRNA-seq data remain rare.

Our integration and benchmarking of multiple methods (note that these methods are not for inferring causal relationships from temporal data) and analysis of multiple datasets generate several conclusions. First, although kernel-based CI tests are time-consuming (Shah and Peters, 2020), applying them to a set of genes is feasible. A set of genes can be generated by feature selection, by gene set enrichment analysis, or by manual selection. Second, the cost of time consumption pays off in network accuracy, as the most time-consuming CI tests generate the most reliable results. Thus, trade-offs between time consumption, network size, and network accuracy should be made. Third, causal discovery can infer signaling networks or gene regulatory networks, depending on the input. If genes encoding TFs and their targets are the input, gene regulatory networks are inferred. Fourth, dropouts and noises in scRNA-seq data concern researchers and trouble correlation analysis (Hou et al., 2020; Mohan and Pearl, 2018; Tu et al., 2019), but can be well tolerated by PC+kernel-based CI tests if samples are sufficiently large. Finally, using ‘spike-in’ data can effectively evaluate the reliability of causal discovery.

### Challenges of data analysis

Single-cell causal discovery also faces several challenges. First, causal discovery assumes there are no unmeasured common causes (the causal sufficiency assumption), but in real data latent and unobserved variables are common and hard to identify. Specifically, inferring interactions between highly expressed or differentially expressed genes is a case of causal discovery with incomplete models (i.e. models with missing variables from the data-generating model). In this situation, what are inferred are indirect relationships instead of direct interactions between gene products. Second, constraint-based methods cannot differentiate networks belonging to a Markov equivalent class (the causal Markov assumption). This can be solved partly by combined use of PC and DAGMA-nonlinear (which can better determine the direction of edges). Third, the following examples indicate that the lack of relevant information makes judging inferred interactions and relationships difficult. (a) TOX is reported to activate PDCD1 in exhausted CD8 T cells in mice (Khan et al., 2019), but whether CXCL13 is involved in (or required for) the TOX-PDCD1 interaction in exhausted CD8 T cells in humans is unclear, until recently CXCL13 is reported to play critical roles in T cells for effective responses to anti-PD-L1 therapies (Zhang et al., 2021b). (b) The differences in inferred networks in exhausted CD8 T cells from different cancers are puzzling, until a recent study reports that exhausted CD8 T cells show high heterogeneity and exhaustion can follow different paths (Zheng et al., 2021). (c) It is difficult to explain multiple genes encoding ribosomal proteins in the inferred networks in CD4 cells from old mice, until a recent study reports that aging impairs ribosomes’ ability to synthesize proteins efficiently (Stein et al., 2022).

### Limitations of the study

The time consumption of kernel-based CI tests disallows inferring large networks, and how this challenge can be solved remains unsolved. C codes may be developed to replace the most time-consuming parts of the R functions, but this has not been done.

### Tips for best practices

First, exploring different biological modules or processes needs careful selection of genes (Figure 5). When it is unclear what genes are most relevant to one or several target genes, it is advisable to run multiple rounds of feature selection using different combination of target genes as response variable(s). Second, when feature genes are identified by gene set enrichment analysis or upon highly expressed genes, PC+kernel-based CI tests perform better than continuous optimization-based methods, and the inferred networks consist more likely of indirect causal relationships instead of direct causal interactions. Third, BAHSIC and SHS are the best feature selection algorithms. Since selecting feature genes from too many candidates is unreliable, filtering genes upon specific conditions (e.g. expression values, expressed cells, fold changes) is necessary. Fourth, DCC.gamma and DCC.perm are the best CI tests working with PC. When building consensus networks, it is advisable to use the results of just DCC CI tests. Fifth, trade-offs between scale, reliability, and accuracy are inevitable. When examining many genes, RCIT/RCoT may be proper, and when examining large datasets, sub-sampling is necessary. For Smart-seq2 and 10x Genomics datasets, 300 and 600 cells are recommended for analyzing 50–60 genes expressed in >50% of cells. More cells are needed if more genes are selected and/or selected genes are expressed in fewer cells (e.g. 25%). Sixth, when it is unclear if a sub-sampled dataset is large enough, repeat causal discovery several times using different sizes of sub-samples. If the inferred networks are similar, the sub-samples should be sufficient. Seventh, using “spike-in” datasets helps measure and ensure reliability. Eighth, carefully inspect the potential influence of cell heterogeneity on causal discovery, and caution is needed when interpreting the results of heterogeneous cells.

![Figure 5.](https://cdn.elifesciences.org/articles/81464/elife-81464-fig5-v2.jpg)

**Figure 5.:** The red and gray dots within the four circles in the central cell indicate the four modules' core genes and related genes. Genes in different modules should be chosen as target genes when exploring different biological processes.

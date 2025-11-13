# Selecting the most appropriate time points to profile in high-throughput studies

## Authors

- Michael Kleyman<sup>1</sup>
- Emre Sefer<sup>1</sup>
- Teodora Nicola<sup>2</sup>
- Celia Espinoza<sup>3</sup>
- Divya Chhabra<sup>3</sup>
- James S Hagood<sup>3</sup>
- Naftali Kaminski<sup>5</sup>
- Namasivayam Ambalavanan<sup>2</sup>
- Ziv Bar-Joseph<sup>1</sup> ([ORCID: 0000-0003-3430-6051](https://orcid.org/0000-0003-3430-6051)) †

### Affiliations

1. Machine Learning and Computational Biology School of Computer Science, Carnegie Mellon University Pittsburgh United States
2. Division of Neonatology, Department of Pediatrics University of Alabama at Birmingham Birmingham United States
3. Division of Respiratory Medicine, Department of Pediatrics University of California San Diego United States
4. CARady Children’s Hospital San Diego San Diego United States
5. Section of Pulmonary, Critical Care and Sleep Medicine School of Medicine, Yale University New Haven United States

† Corresponding author

## Abstract

Biological systems are increasingly being studied by high throughput profiling of molecular data over time. Determining the set of time points to sample in studies that profile several different types of molecular data is still challenging. Here we present the Time Point Selection (TPS) method that solves this combinatorial problem in a principled and practical way. TPS utilizes expression data from a small set of genes sampled at a high rate. As we show by applying TPS to study mouse lung development, the points selected by TPS can be used to reconstruct an accurate representation for the expression values of the non selected points. Further, even though the selection is only based on gene expression, these points are also appropriate for representing a much larger set of protein, miRNA and DNA methylation changes over time. TPS can thus serve as a key design strategy for high throughput time series experiments. Supporting Website: www.sb.cs.cmu.edu/TPS

## Introduction

Time series experiments are very commonly used to study a wide range of biological processes. Examples include various developmental processes (Roy et al., 2010), stem cell differentiation (Sperger et al., 2003), immune responses (Yosef and Regev, 2011), stress responses (Gitter et al., 2013) and several others. Indeed, analysis of the largest repository of gene expression experiments, the Gene Expression Omnibus (GEO), determined that roughly a third of these datasets come from experiments profiling dynamic processes over time (Zinman et al., 2013).

While mRNA gene expression data have been the primary source of high-throughput time series data, more recently several other genomic regulatory features are profiled over time. These include miRNA expression data (Schulz et al., 2013), ChIP-Seq studied to determine TF targets (Chang et al., 2013) and several types of epigenetic markers including DNA methylation (Singer et al., 2014), histone modifications (Paige et al., 2012) and more. In fact, with the rise in our ability to perform such high-throughput time series analysis, many researchers are now combining a few or several of these time series profiling experiments in a single experiment (Chang et al., 2013; Buenrostro et al., 2015) and then integrate these datasets to obtain a better understanding of cellular activity.

While integrated analysis of high-throughput genomic datasets can greatly improve our ability to model biological processes and systems, it comes at a cost. From the monetary point of view, these costs include the increased number of Seq experiments required to profile all types of genomic features. While such costs are common to all types of studies utilizing high-throughput data, they can be prohibitively high for time series based studies since they are multiplied by the number of time points required, the number of repeats performed for each time point and the number of different types of data being profiled. Importantly, even if the budget is not an issue, the ability to obtain enough samples for profiling all genomic features at all time points may be challenging, if not completely prohibitive.

One of the key determinants of the experimental and sample acquisition costs associated with time series studies is the number of time points that are being profiled. In most studies, the first and last time point can usually be determined by the researcher (for example, the time from birth to full lung structural development and maturation in mice). However, the number of samples required between these two points and the sampling frequency (given a fixed budget) are often hard to determine based on phenotypic observations since the molecular events of interest may precede such phenotypic events. To date, sampling rates have largely been determined using one of two ad-hoc protocols. The first utilized uniform sampling across the duration of the study (Li et al., 2013) with the number of samples constrained by the available budget and samples. The second relied on some (conceived or real) knowledge of the process, often based on phenotypic observations. These studies, especially for responses though also for development, have often used nonuniform sampling (Schulz et al., 2013; Bar-Joseph et al., 2003a) though it is hard to determine if such sampling misses important molecular events between the sampled points.

Relatively, little work has focused so far on the selection of time points to sample in high throughput time series studies. Singh et al (Singh et al., 2005) and Rosa et al (Rosa et al., 2012) presented an iterative process which starts with profiling a small number of time points and then selects the next time point either based on an Active Learning method (Singh et al., 2005) or based on using prior related experiments (Rosa et al., 2012). Next the selected point is profiled and the process is repeated until a stopping criteria has been reached. Both of these methods require several iterations until the final time series is profiled, which can drastically lengthen the experiment time and can introduce additional biases making them less useful in practice. In addition, these methods employ a stopping criteria that does not take into account the full profile and also require that related time series expression experiments be used to select the point, which may be problematic when studying new processes or treatments.

Here, we propose the first non iterative method to address the issue of sampling rates across all different genomic data types. Our method starts by selecting a small set of genes that are known to be associated with the process being studied (while the full set is often unknown, for most processes a small set is usually known in advance). Next, we use a cheap array-based technology to sample these genes at a high, uniform rate across the duration of the study. Note that unlike standard curve fitting algorithms, a method for selecting time points for these experiments is required to accommodate over a hundred curves (for all genes) simultaneously, and we discuss various ways to formulate this as an optimization problem. To solve this optimization problems, we developed the Time Points Selection method (TPS), an algorithm that uses spline based analysis and combinatorial search to select a subset of the points that, when combined, provide enough information for reconstructing the values for all genes across all time points. The number of points selected can either be set in advance by the user (for example, based on budget constraints) or can be defined as a function of the reconstruction error. The selected time points are then used for the larger, genome-wide experiments across the different types of data being profiled.

To test and evaluate the method we applied it to study lung development in mice. Normal development of lung alveoli through the process of alveolar septation is a dynamic, coordinated process that requires the accurate spatial and temporal integration of signals. We currently lack a comprehensive understanding of the dynamic networks that govern normal alveolar septation. Thus, lung development can serve as an ideal test case for TPS since a variety of different time series genomic datasets are needed to enable accurate reconstruction of networks regulating this process. As we show, TPS was able to successfully identify time points for reconstructing the mRNA profiles of selected genes and these points improved upon uniform based sampling for such points. Further, we show that the set of points selected based on the analysis of this limited set of highly sampled mRNAs is also appropriate for sampling a much larger, unbiased, set of miRNA profiles as well as to determine the temporal protein levels of over 1000 proteins. Finally, we show that the mRNA samples can also be used to determine the optimal sampling points for a DNA methylation study of the same developmental process.

## Results

### The time points selection (TPS ) method

We developed TPS to select a subset of k time points from an initial larger set of n points such that the selected subset provides an accurate, yet compact, representation of the temporal trajectory. Figure 1 presents an overview of the method. TPS utilizes splines to represent temporal profiles and implements a cross-validation strategy to evaluate potential sets of points. Following initialization which is based on the expression values, we employ a greedy search procedure that adds and removes points until a local minima is reached (Materials and methods). The resulting set is then used for the larger genomic and epigenetic experiments.

![Figure 1.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig1-v2.jpg)

**Figure 1.:** Clockwise from top left. Given a dense sampling of a selected subset of genes (a) we select an initial set of points (b) using the initialization method described in the text. Next, we fit a spline to the selected points for each gene (c) and evaluate the error on all other points. We perform a greedy search process (d) which iteratively removes and adds points to improve the test data fit resulting in the final set of points (e). The reconstructed curves are fitted to all genes (f) and an overall error is computed and compared to the theoretical limit (noise) to determine the ability of the selected number of points to fit the data.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (Singh et al., 2005) which used an active learning method based on dynamic programming.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** The points labeled metricA, metricB, and metricC all use the dynamic initialization approaches, while the max distance points use static initialization.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig1-figsupp3-v2.jpg)

To test the usefulness of TPS , we used it to determine time points for a lung development study in mice. We first profiled the expression of 126 genes known or suspected to be involved in lung development using NanoString (See Appendix Methods for a list of the selected genes and the reason each was selected). We then used TPS analysis of these experiments to select a subset of time points for profiling the expression of a larger, unbiased, set of miRNAs. Finally, we have used TPS to design time series experiments to study DNA methylation patterns for a subset of the genes.

### TPS identifies subset of important time points across multiple genes

We have tested the performance of TPS by using it to select subsets of points ranging from 3 to 25 and evaluating how well these can be used to determine the values of non-sampled points. To determine the accuracy of the reconstructed profiles using the selected points, we computed the average mean squared error for points that were not used by the method (Materials and methods). The results are presented in Figure 2. The figure includes a comparison of our method with two baseline methods: a random selection of the same number of points and uniform sampling of points within the range being studied, a method that is commonly used for time series expression profiling as discussed above. We have also compared the performance of the different strategies for initializing the set of points as discussed in Appendix Method (sorting by absolute differences or by equal partition) and between different methods for searching for the optimal subset (simulated annealing, weighting genes by cluster size, and adding/removing multiple time points per iteration, Appendix Methods). Finally, Figure 2 also presents the repeat noise values which is the theoretical limit for the performance of any profile reconstruction method.

![Figure 2.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig2-v2.jpg)

**Figure 2.:** Error comparisons of TPS variants to uniform selection of points and noise. Absolute difference - Greedy iterative addition with absolute difference initialization (Algorithm 1, Appendix Methods). Simulated annealing - Iterating using simulated annealing with absolute difference initialization. Weighted error - Selection based on cluster rather than individual gene errors. See Appendix Methods for details.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig2-figsupp1-v2.jpg)

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** The 75% random data was created by replacing 75% of the gene time series with random value time series selected from a Gaussian distribution with mean 0 and standard deviation equal to the noise of the original data.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig2-figsupp3-v2.jpg)

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig2-figsupp4-v2.jpg)

As expected, we find significant performance improvement when using TPS when compared to randomly selected points. Importantly, we also see a significant and consistent improvement (for all sizes of selected time points) over uniform sampling highlighting the advantage of condition-specific sampling decisions. Sorting initial points by absolute values further improves the performance highlighting the importance of initialization when searching large combinatorial spaces. Simulated annealing, weighting, and multiple point selection improve performance as well. As the number of points used by TPS increases, it leads to results that are very close to the error represented by noise in the data (0.108) ( Figure 2—figure supplement 1).

Figure 3 presents the reconstructed and measured expression values when using TPS to select 13 time points (less than a third of the points that were profiled). Note that even though each of these genes has distinct trajectory and inflection points, the selected set of time points enable TPS to fit all quite accurately without overfitting (See Figure 3—figure supplement 1 and Figure 3—figure supplement 2 for figures of several other genes and for figures reconstructed by using the best 8 time points as determined by TPS , respectively).

![Figure 3.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig3-v2.jpg)

**Figure 3.:** (a). Pdgfra. , (b). Eln. , (c). Inmt.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig3-figsupp1-v2.jpg)

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig3-figsupp2-v2.jpg)

### Identified time points using mRNA data are appropriate for miRNA profiling

To test the usefulness of our method for predicting the correct sampling rates for other genomic datasets, we next profiled mouse miRNAs for the same developmental process. miRNAs have been known to regulate lung development (Sessa and Hata, 2013) and several miRNAs are differentially expressed during this developmental process (Williams et al., 2007). Several of these are also coordinately activated with various TFs to control specific transitions during development (Schulz et al., 2013). Thus, any large scale effort to model lung development would require the profiling of miRNAs as well. Unlike the mRNA dataset, which utilized prior knowledge to profile less than 1% of all genes, the miRNA dataset contained a much larger number of miRNAs ($6^00$). Thus, the miRNA data represent an unbiased sample providing information on whether using one type of genomic data can be helpful for determining rates for other types. In our analysis, we normalized miRNA values by variance mean normalization (Bolstad et al., 2003).

To test TPS on this dataset, we used the mRNA expression data to select time points and then used the miRNA expression values for the selected time points to reconstruct the complete trajectories for each miRNA. The results are presented in Figure 4. As can be seen, when using the points selected based on the mRNA data we achieve a much lower error when compared to the error resulting from using the same number of uniform or random points (p<0.01 for random based on randomization analysis) highlighting the relationship between the two datasets and the ability to use one to determine points for the other. More generally, even though the noise in the miRNA data is higher than for the mRNA dataset, relative ordering of the performance of each of the methods is similar to the mRNA results in Figure 2. This serves as a strong indication that mRNAs can serve as a general proxy for selecting time points for other genomic datasets. Figure 4b presents the error achieved when using the miRNA data itself to select the set of points (evaluated on the miRNA data). As expected, the performance when using the miRNA data itself is better than when using the mRNA data. However, when taking into account the inherent noise in the data the differences are not large. For example, when using the 13 selected mRNA points, the average mean squared error is 0.4312 whereas when using the optimal points based on the miRNA data itself the error is 0.4042.

![Figure 4.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig4-v2.jpg)

**Figure 4.:** (a) TPS reconstruction error when using the mRNA data to select time points for the miRNA experiments. Results of random and uniform selection as well as repeat noise error are also presented for comparison. TPS variants shown are the same two presented in Figure 2. (b) Error of splines with points selected by training TPS on the actual miRNA data itself, using the maximum absolute difference initialization.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig4-figsupp1-v2.jpg)

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig4-figsupp2-v2.jpg)

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (a) Comparison of the reconstruction error when using the points selected by TPS, uniform selection of points, and when using the same number of random points from the overall set of sampled points. (b) Error comparisons of TPSto noise, and various search and initialization options discussed in Methods.

Figure 4—figure supplement 1 presents the reconstructed and measured expression values for a few miRNAs based on time points identified using the mRNA dataset. As with the mRNA data, the ability to accurately reconstruct different miRNA profiles highlights the importance of selecting a global set of points that can fit all genes and miRNAs in our study.

We have also analyzed the performance of TPS when using the mRNA data to select sampling time points for profiling the levels of more than 1000 proteins. We observed results that are very similar to the results obtained for the miRNA time point selection. Specifically, the points selected by TPS lead to reconstruction errors that are lower than those observed for uniform sampling or for a random set of the same number of points further demonstrating the general applicability of our method. See Appendix Results for details.

### Using TPS to select time points for DNA methylation analysis

In addition to mRNA and miRNA expression data, epigenetic data have been increasingly studied in time series experiments (Talens et al., 2010; Schneider et al., 2010). To test the ability of the mRNA data to determine the appropriate points for DNA methylation analysis, we used targeted bisulfite sequencing to profile three CpG-enriched regions for 13 genes at 8 of the 42 time points used for the mRNA and miRNA studies (Materials and methods). We next applied TPS to the mRNA data of these 8 points to select the best subest of 4 points and compared the selected points to those that would have been selected using the methylation data itself. The 4 points identified using the mRNA data (0.5, 5, 15, 26) were exactly the same as the ones selected using the methylation data indicating again that mRNA data is a good proxy for the dynamics of the epigenetic data as well. Figure 5—figure supplement 1 presents the reconstructed splines over the identified points for several genomic methylation loci. Figure 5 presents the methylation and expression curves for 3 genes: Akt,1 Cdh11, and Tnc. These were the genes with the strongest negative correlation between their methylation and expression. As can be seen, in several cases we observed strong negative or positive correlations between the two datasets in the time points we used serving as another indication for the ability to use one dataset to select the sampling points for the other. See Figure 5—figure supplement 2 for correlation of all genes.

![Figure 5.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig5-v2.jpg)

**Figure 5.:** (a). Akt1. , (b). Cdh11. , (c). Tnc.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig5-figsupp1-v2.jpg)

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** The red circles are the Pearson correlation over all eight points and the blue triangles are the Pearson correlation for all subsets of 7 points.

## Discussion

Time series gene expression experiments are widely used in several studies. More recently, advances in sequencing and proteomics are enabling the profiling of several other types of genomic data over time. Here we focused on lung development in mice with the goal of identifying an optimal set of time points for profiling various genomic and proteomic data types for this process.

An important question is: Whether a better selection of time points really leads to observations that are missed when using an inferior set of points (even if the number of points is the same)? To answer this question we looked at several prior studies that profiled mouse lung development over time using various high throughput assays. Table 1 presents 9 representative studies and lists the biological data that was profiled and the time points that were used. As can be seen, while certain time points seem to be widely used across studies (for example, 7d) others were profiled in only one or two of the studies (2d, 10d, three weeks). This raises several issues. First, it is very hard to compare or combine these datasets (for example, protein levels were not profiled on day 7(Cox et al., 2007) whereas all mRNA levels were). It also makes it hard to determine if differences between DE genes or miRNAs between these studies are the result of differences in the underlying conditions studied (for example, when testing for mutants or treatments) or simply the result of different sampling. Finally, each of these studies may have missed key genes, proteins or miRNAs because of the sampling used restricting the ability of downstream analysis to use the data to model causal and regulatory events in lung development.

**Table 1.**
 Summary of prior high throughput lung development studies.


<table>
  <thead>
    <tr>
      <th>Reference</th>
      <th>Data types</th>
      <th>Selected time points (Days)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[Bonner et al., 2003]</td>
      <td>mRNA expression</td>
      <td>E9, E4, E17, 0, 7, 14, 28</td>
    </tr>
    <tr>
      <td>[Melén et al., 2011]</td>
      <td>mRNA expression</td>
      <td>E16, E18, 0, 7, 14, 28</td>
    </tr>
    <tr>
      <td>[Bhaskaran et al., 2009]</td>
      <td>microRNA expression</td>
      <td>E16, E19, E21, 0, 6, 14, 60</td>
    </tr>
    <tr>
      <td>[Dong et al., 2011]</td>
      <td>mRNA and microRNA expression</td>
      <td>E12, E14, E16, 0, 2, 10</td>
    </tr>
    <tr>
      <td>[Cox et al., 2007]</td>
      <td>Protein expression levels</td>
      <td>E12, E14, E18, 2, 14, 56</td>
    </tr>
    <tr>
      <td>[Schulz et al., 2013]</td>
      <td>mRNA and miRNA expression</td>
      <td>0, 4, 7, 14, 42</td>
    </tr>
    <tr>
      <td>[Cormack et al., 2010]</td>
      <td>mRNA expression</td>
      <td>0, 7, 14, adult</td>
    </tr>
    <tr>
      <td>[Mager et al., 2007]</td>
      <td>mRNA expression</td>
      <td>E15, E17, E19, E21, 1, 14, 84</td>
    </tr>
    <tr>
      <td>[Mariani et al., 2002]</td>
      <td>mRNA expression</td>
      <td>E18, 1, 4, 7, 10, 14, 21, adult</td>
    </tr>
  </tbody>
</table>

To illustrate these problems we compared the resulting curves using three of the sampling rates from Table 1 to the reconstructed curves obtained by using TPS to select the optimal 5 and 8 time points. For example, the points selected by Schulz et al. (2013) are 0, 4, 7, 14 and 28 (since 28 is last day in our analysis we used it instead of 42). In contrast, TPS selects 0.5, 6, 9.5, 19 and 28. As can be seen in Figure 6, important expression changes in key genes are missed by using the arbitrary points while the TPS points are able to correctly reconstruct these profiles even though the total number of points is the same (5). More globally, the error for the arbitrary set of selected points is much higher on average (Appendix 2—Table 4). Similar results are obtained for the other sampling rates used in the past (Figure 6, Appendix 2—Table 4) and when comparing TPS to iterative methods previously suggested for selecting the set of points to profile (Figure 1—figure supplement 1). This indicates that accurate selection of time points can have a large impact on the ability of the study to identify key genes and events. See also Appendix Results for a discussion about the importance of the differences between the TPS and prior work results for selected genes.

![Figure 6.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig6-v2.jpg)

**Figure 6.:** Dark green curves are the reconstructed profiles based on the points profiled by prior studies. Light green and red curves are based on the points selected by TPS . As can be seen, even when comparing results from using the same number of points, TPS can identify key events for some of the genes that are missed when using the phenotype based sampling rates. Subfigures a,b, and c are a piecewise linear ﬁt over points 0.5, 7.0, 14.0, 28.0 . Subfigures d,e, and f are a piecewise linear fit over points 0.5, 2.0, 14.0, 28.0. Subfigures g,h, and i are a piecewise linear fit over points 0.5, 4.0, 7.0, 14.0, 28.0.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/18541/elife-18541-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (a) Eln/P54320, (b) F13a1/Q8BH61, (c) Chil1/Q61362.

Our method relies on a very small subset of genes that are known to be involved in the process studied for the initial (highly sampled) set of experiments. While such set is known for several processes, there may be cases where very little is known about the biological process and so it may be hard to obtain such set. TPS can still be applied to determine sampling rates for such processes using a small random set of genes. To illustrate this we repeated the analysis presented in Results using only the measured values of 25% of genes in our original set and replacing the values for the other genes with random profiles. As we show in Figure 2—figure supplement 2, even when using such set, the time points selected by TPS greatly improve upon an arbitrary set of the same number of time points. Since in most time series experiments at least 25% of the genes are differentially expressed (and in several cases a much larger fraction, (Zhou et al., 2009; Shi et al., 2015) a random selection of genes is likely to exhibit similar results even for poorly understood processes.

Beyond the analysis of a specific type of data, several studies have now been profiling multiple types of genomic data over time. Such studies need to agree on a set of time points which would be common to all experiments so that these diverse types can be integrated to form a unified model (Chang et al., 2013; Roy et al., 2010). To date, the selection of such points relied on ad-hoc methods. The processes being studied were either sampled uniformly or based on prior knowledge. However, known properties of such systems were often been based on phenotypic observations which may not necessarily agree with the timing of molecular events. In addition, in many case studies of the same, or similar processes differed with respect to the time points that have been profiled. For example, early work on the analysis of cell cycle data in yeast utilized both uniform and nonuniform sampling (Spellman et al., 1998) and recent studies of circadian rhythms have followed a similar pattern (Storch et al., 2002; Ueda et al., 2002). Similarly, more recent analysis of responses to flu diverged widely in the (nonuniform) sampling rates that were used (Shapira et al., 2009; Li et al., 2011).

TPS addresses these problems by using a principled method for determining sampling rates. An important goal in the development of TPS was to enable it to be successfully applied to different types of biological datasets. As we show, a relatively inexpensive, gene centric, method provides a very good solution for RNA expression profiling as well as other types of data including miRNAs and DNA methylation. Thus, a combined experiment can be fully designed using our method.

While we evaluated TPS on several types of high throughput data, we have only tested it so far on data for a specific biological process (lung development in mice). While we believe that such data is both challenging and representative and thus provides a good test case for the method, analysis of additional datasets may identify new challenges that we have not addressed and we leave it to future work to address these.

TPS, including all initialization methods discussed, is implemented in Python and is available on the supporting website. We hope that as sequencing technology continues to advance, more and more studies would integrate diverse types of time series data and will utilize TPS in the design pipeline of their studies.

## Materials and methods

### mRNA and miRNA used in the study

To select the list of 126 genes used in the NanoString profiling we searched the literature for genes that have been linked to the following processes: (a) Cell type specification genes (e.g. alveolar type I epithelial, alveolar type II epithelial, any epithelial, basal, endothelial, mesenchymal, pericyte, fibroblast, monocyte), (b) genes known to be up or down regulated during septation, (c) genes known to be altered in DNA methylation during development, (d) genes known to be involved in septation, (e) genes known to be regulated by miRNA involved in septation, and (f) genes known to be regulated by DNA methylation during fibrosis. Appendix 2—Table 1 contains a list of the selected genes and the process for which they were selected.

For the miRNA set we used a commercially available, unbiased, array (the nCounter Mouse miRNA Expression Assay Kit, NanoString).

### mRNA and miRNA profiling and analysis

A total of 240 samples were isolated by Laser Capture Microscopy (LCM) from murine lung at multiple time points (E16.5, P.05 to P14 every 12 hr, and P15 to P28 every 24 hr). The samples were used to prepare total RNA. RNA extraction was performed by miRNeasy MicroKit (Qiagen) following the manufacturer’s protocol. RNA concentration and integrity were measured by using NanoDrop ND-2000 and 2200 Tape Station. A custom NanoString probe set (Reporter Code set and Capture Probe set) for 126 genes was designed and the nCounter Gene Expression Assay was performed using 50 ng total RNA. The data files produced by the nCounter Digital Analyzer were exported as a Reporter Code Count (RCC) file and data normalization was performed using the nSolver, the analysis software provided by Nanostring.

### DNA methylation analysis

Mouse alveolar lung tissues attached to LCM caps were stored at −80°C until processing. DNA was extracted using the ZR Genomic DNA-Tissue MicroPrep kit (Zymo Research). Incubation with Digestion buffer and proteinase K was done overnight at 55°C in inverted tubes. 13 genes were chosen for targeted NextGen bisulfite sequencing (NGBS): Igfbp3, Wif1, Cdh11, Eln, Sox9, Tnc, Dnmt3a, Akt, Vegfa, Lox, Foxf2, Zfp536 and Src, based on published data (Cuna et al., 2015). Targeted NGBS was done on samples collected at: E16.5, E18.5, P0.5, P1.5, P2.5, P5, P10, P15, P19 and P26. Multiplex PCR was performed using 0.5 units of TaKaRa EpiTaq HS (Takara Bio, Kusatsu, Japan) in 2x master mix. FASTQ files were aligned using open source Bismark Bisulfite Read Mapper using Bowtie2. Methylation levels were calculated in Bismark. Sites where the difference in methylation was less than 5% over the entire time period, those where there was a difference of >20% at a single time point and those with less than $3$ non zero values were removed from the analyses.

### Problem statement

Our goal is to identify a (small) subset of time points that can be used to accurately reconstruct the expression trajectory for all genes or other molecules being profiled. We assume that we can efficiently and cheaply obtain a dense sample for the expression of a very small subset of representative genes (here we use nanostring to profile less than 0.5% of all genes) and attempt to use this subset to determine optimal sampling points for the entire set of genes.

Formally, let $G$ be the set of genes we have profiled in our dense sample, $T={t_{1},t_{2},…,t_{T}}$ be the set of all sampled time points. We assume that for each time point we have $R$ repeats for all genes. We denote by $e_{g⁢t}^{r}$ be the expression value for gene $g\inG$ at time $t\inT$ in the $r$’th repeat for that time point. We define $D_{g}={e_{g⁢t}^{r},t\inT,r\inR$ as the complete data for gene $g$ over all replicates and time points $T$.

To constrain the set of points we select, we assume that we have a predefined budget $k$ for the maximum number of time points we can sample in the complete experiment (i.e. for profiling all genes, miRNAs, epigenetic marks etc. using high-throughput seq experiments). We are interested in selecting $k$ time points from $T$ which, when using only the data collected at these $k$ points, minimizes the prediction error for the expression values of the unused points. To evaluate such a selection, we use the selected values to obtain a smoothing spline (De Boor, 1978; Bar-Joseph et al., 2003a; Wahba, 1990) function for each gene and compare the predicted values based on the spline to the measured value for the non-selected points to determine the error. In our problem, $t_{1}$ and $t_{T}$ define the first and end points, so they are always selected. The rest of the points are selected to maximize the following objective 1:

Problem statement: Given $D_{g}$ for genes $g\inG$, the number of desired time points $k$, identify a subset of $k-2$ time points in $T∖{t_{1},t_{T}}$ which minimizes the prediction error for the expression values of all genes in the remaining time points.

### Spline assignments

Before discussing the actual procedure we use to select the set of time points, we discuss the method we use to assign splines based on a selected subset of points for each gene. There are two issues that need to be resolved when assigning such smoothing splines: (1) The number of knots (control points) and (2) their spacing. Past approaches for using splines to model time series gene expression data have usually used the same number of control points for all genes regardless of their trajectories (Subhani et al., 2010; Bar-Joseph et al., 2003b), and mostly employed uniform knot placements. However, since our method needs to be able to adapt to any size of $k$ as defined above, we also attempt to select the number of knots and their spacing. We do this by using a regularization parameter for the fitted cubic smoothing spline where number of knots is increased until the smoothing condition is satisfied (Wahba, 1990). The regularization parameter is estimated by leave-one-out cross-validation (LOOCV).

### TPS : Iterative process to select points

Because of the highly combinatorial nature of the time points, we rely on a greedy iterative process to select the optimal points as summarized in Figure 1 (See Appendix Methods for pseudocode).

There are three key steps in this algorithm which we discuss in detail below.

### Individual vs. cluster-based evaluation

So far, we assumed that error of each gene has the same contribution to the overall error. However, this assumption ignores the fact that the expression profiles of genes are correlated with the expression of other genes. To take the correlation between gene profiles into account, we also performed cluster based evaluation of genes where we analyzed the error by weighting each gene in terms of inverse of the numbers of genes in the cluster it belongs. This scheme ensures that each cluster contributes equally to the resulting error rather than each gene. We find clusters by k-means algorithm over time series-data by treating each gene as a point in $R^{T}$ space as well as over a vector of randomly sampled $T$ time points on fitted spline (Bishop, 2006). We use Bayesian Information Criterion (BIC) to determine the optimal number of clusters (Schwarz, 1978).

# Peer review - Round 1

Editors:
- Erica A Golemis, Fox Chase Cancer Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57116.sa1](https://doi.org/10.7554/eLife.57116.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The main strength of the work is combining into a single measure CRISPR and shRNA screening data from DepMap, and providing a very convenient interface to explore these data. The approach is well-considered, and the trade-off between streamlining the exploration vs increased difficulty in interpretation is reasonable. The web-based interface is easy to use, and most of the limitations in the data analysis are clearly described. As such, the tools could be used by the community investigating gene function.

Decision letter after peer review:

Thank you for sending your article entitled "shinyDepMap: A tool for browsing the Cancer Dependency Map reveals functional connections between genes" for peer review at eLife. Your article is being evaluated by three peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Maureen Murphy as the Senior Editor.

As you can see from the below comments, at least two of the reviewers identify potential significance in your study. However, all of the reviewers have identified multiple weaknesses in the submitted work, bearing on the capacity of the tool to yield a measurable benefit over what is currently available; the significance of the biological insights reported; and the clarity of the presentation.

Reviewer #1:

The main strength of the work is combining into a single measure CRISPR and shRNA screening data from DepMap and providing a very convenient interface to explore these data. The approach is plausible and the trade-off between streamlining the exploration vs increased difficulty in interpretation is reasonable. The web-based interface is easy to use, and most of the limitations in the data analysis are clearly described. As such, the tools could be used by the community and the paper deserves to be published after a revision.

The biggest problem with the paper itself is the way it is written, which appears to be in a big haste. Multiple terms are used to describe the same thing (like "dependency score" and "perturbation score"). Sometimes the sentences appear to have self-contradictions (like "The median cluster size is 6, 4, and 3 genes for small, medium, or large clusters, respectively"). References in text to figure panels are frequently not matching (e.g., the sentence "We developed a new gene dependency metric, termed "perturbation score" " refers to Figure 2B, which is just a set of violin plots showing "The perturbation score profiles of the same four genes as in A."). Words missing in sentences make them hard to understand e.g., in the sentence "such that the size of the 1st and 2nd largest clusters {less than or equal to} b (b = 2.26 in our case " the word "ratio" is missing). Grammar and word usage issues additionally hamper difficulty in understanding.

Perhaps most importantly, the document is really poorly structured with the definitions given after the analysis using the defined term was described, some of relevant logic found in Materials and methods section etc. While having the details of informatics analysis would be rather illuminating for the "average biology scientist", the paper still should be rewritten and streamlined to provide the better flow and eliminate the elements of sloppiness, including all points mentioned above across the main text, figures and figure legends.

1) Authors' definition "We defined non- essential genes such that they are not identified as essential from the earlier analysis using the perturbation scores of the 10 , 20 and 42 most sensitive cell lines, as well as not identified as promoting its growth using the scores of the 10 , 20 and 42 least sensitive cell lines." should be justified – why was it important to exclude also genes which appear to promote growth upon knockdown from the set of non – essential genes? How many of these genes were excluded?

2) DepMap genes may have designations as "Strongly Selective" and/or "Common Essential". What is the relation between genes identified as such in this study and in DepMap? A supplementary figure (Venn diagrams) and/or table may illustrate the overlap.

3) It is not quite clear what in Figure S1B is illustrated which would be not clear from S1A.

4) Selectivity is already a very vague notion, because it can arise from differences between cell types, or from the presence/absence of mutation in certain gene(s), etc. Median selectivity, used in Figure 4F, is trickier still, because different genes in the cluster may have different sources of selectivity. While Figure 4F is, indeed, a good way to illustrate a diversity of identified clusters, a word of caution would help to avoid overinterpreting the results.

5) In the application itself, Gene Clusters are very nicely presented in the Connectivity view. It would be very helpful to provide an option to save the underlying table with gene names and correlations (for example, to enable the subsequent use in Cytoscape). At the bare minimum, some way of exporting at least gene names in the cluster should be provided, apart from copying the whole table from "Clustered genes" view and then removing unused columns.

6) CRISPR data seems to dominate the perturbation score. How much different the clustering based on the perturbation score is if compared to using CRISPR data alone? Could any independent measure be provided to compare the sets of clusters? E.g., distribution of connectivity scores based on protein-protein interactions, or of enrichment scores?

7) In the application Gene Clusters , Correlation View, the names of the clusters can be discerned when the user zooms in. However, in the static view (Figure 1C, section 12) it should be indicated in the legend that the three vertical "lines" on the left are, in fact, the cluster labels.

Reviewer #2:

Shimada at al. present a combination CRISPR and shRNA screening data from DepMap and built user-friendly browser (https://labsyspharm.shinyapps.io/depmap) for the exploration of the dataset using their metric of efficacy and selectivity.

The efficacy is the "perturbation score" of the 10th most sensitive cell line for each gene, whereas selectivity is an ad-hoc measure that the authors define according to the dispersion of the efficacy between most sensitive and least sensitive cell lines. The app also allow to explore a clustering of the data computer with their algorithm ECHODOTS.

The DeepMap dataset is a very important resource to identify candidate targets and cancer dependency and efficient methods that allow exploration and analysis of these data are welcome. Unfortunately the paper of Shimada does not reach neither of these aims.

Overall the paper is very poorly written and very difficult to follow. It starts with the presentation of the shiny app for the 2,492 essential genes that they select with their method. I understand that the aim is to allow non-programmers to access the data, the problem is the kind of analysis supporting the plots that, I think, should much more improved.

The author claim to compute a novel method of the efficacy, a new methods to select genes which are selectively lethal for cell line, and also a novel clustering method. Unfortunately none of these methods is sufficiently justified by the authors of compared with the state of the art of at least the current literature. For example, they could have compared their selectivity method to the ADaM method reported in (Behan et al., 2019), moreover it is not clear why the efficacy score computed on the basis of the "perturbation score" is more robust of should be preferred with respect to other approach. Finding out how they defined the efficacy was a very difficult.

Regarding the novel clustering algorithm that they propose, it is very strange that the authors need to develop a novel clustering algorithms given the plethora of available methods in the literature. Why should they develop a new one and what limits of the current state of the art their algorithm should overcome it completely obscure. Moreover, from their description of the method I doubt it is really a clustering procedure at all.

There is no guarantee that rule they describe "It assigns two genes into the same cluster when the distance between the genes is smaller than epsilon" you have that each point belongs to just one cluster. The authors do not specify to what data the clustering is applied. CRISPR? shRNA? Both?

Moreover, the choice of the parameters is rather arbitrary and not discussed in the paper.

Overall, I suggest the authors to focus on what they think could be an improvement of the state of the art in at least one on the three areas (efficacy selectivity and clustering) and convince the reader that on what and why they are improving something.

Regarding the shiny app itself, it is a very basic exploratory tool. A very interesting improvement that could be useful for target identification and exploitation of synthetic lethality of to include genomic information to check if the cells depending on a specific gene share some common molecular features (mutations, copy number, pathways). This could for example be done using the efficacy as an independent variable and the molecular features as predictors in the cells depending on a specific gene.

Reviewer #3:

In this manuscript, Shimada et al. develop a tool called shinyDepMap to enable the non-expert bioinformatician to analyze cancer dependency datasets through a user friendly interface. This tool reports gene perturbation scores, which combines essentiality scores from shRNA and CRISPR based screens for various cell lines and utilizes network analysis to identify gene cluster and essential pathways in the various cancer cell types. Overall, this is a very useful tool to the community at large, especially those with little computational background – similar to cbioportal. It will likely be widely adopted however I have a few suggestions for improvement:

Overall the website is slow. I assume this is a test version, however if it is to be widely used, some effort will be needed to ensure it is able to meet the large bandwidth and demand. Ideally it should also be hosted in an independent weblink (e.g. cbioportal).

It would be helpful if in addition to the interactive graphs which are very helpful, if the tool would export data in PDF/JPG for publication purposes as well as a tabular format for each cell line/perturbation score. It is sometimes difficult to identify all key genes/cell lines simply by hovering over the graphs and it is helpful to be able to obtain the output in a table format.

It would be helpful if the perturbation scores can include a separate parameter to indicate whether the CRISPR and shRNA based essentiality scores significantly diverge. The authors explore this in some depth and report that their score is at least as good as the CRISPR screen, however it would be helpful to the user if they received some form of confidence score that indicates how well the two modalities agree/disagree. There are many reasons for discrepancy and it would be helpful to be aware of such a discrepancy when it exists.

While the authors perform robustness analysis when choosing their cutoff to define essential genes (10th most sensitive cell line) it is unclear still why they picked such a cutoff. Perhaps some additional explanation of the rationale would be helpful. Also in cancer types where there are more cell lines available would it be helpful to define the 10th percentile rather than the 10th cell line?

I find the selectivity analysis summarized in Figure 3E to be perhaps the most interesting biological insight from this paper. This is important therapeutically. However the way it is phrased, selectivity compares perhaps most likely different tumor types (i.e. a drug that's toxic to breast cancer cells is less toxic to sarcoma cells for example). Therapeutically this comparison is less valuable than comparing normal to transformed/cancer cell line for each histology or on a pan cancer level. If the data exists, it would be extremely helpful to recompute selectivity comparing cancer/non-cancer cells and reproducing Figure 3E for such a comparison.

Finally, it would be very helpful for the user to be able to select a subset of cell lines to perform pairwise analysis. For example if a user would like to ask what genes are essential for cell lines harboring a KRAS mutation vs cells without a KRAS mutation, having the ability to perform pairwise analysis and displaying the data for pre-selected cell lines based on a specific feature/histology would be extremely helpful and significantly expand the value of this tool. I realize that this would necessitate incorporating the mutational annotation and copy number annotation of each cell line but perhaps the effort would be well worth it if feasible.

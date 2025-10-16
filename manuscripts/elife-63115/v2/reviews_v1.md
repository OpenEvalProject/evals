# Peer review - Round 1

Editors:
- Chris P Ponting, University of Edinburgh United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63115.sa1](https://doi.org/10.7554/eLife.63115.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper is of interest to researchers seeking to use genetics in order to reposition drugs that improve lung function. The work highlights biochemical traits that could be targeted to modulate lung function. The analyses have been performed to a high level, with some of the most interesting and novel results being of modest statistical significance.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Genetic association and causal inference converge on hyperglycaemia as a modifiable risk factor for respiratory disease" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Bogdan Pasanuic (Reviewer #3).

Our decision has been reached after consultation among all the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Reviewers considered that the manuscript's focus on rapidly repositioning drugs to improve lung function is timely. They, however, remained unconvinced by some of the main claims and their novelty, and expressed concerns regarding the robustness of results that are based on border-line statistics. Replication and/or validation of the main results might have helped to convince the reviewers. Further consideration of other explanatory variables would also have provided greater robustness to the claims of causality.

Reviewer #1:

This paper seeks to use genetics to reposition drugs to improve lung function. A new pipeline is used to connect together several recent genetics methods: filtering traits on genetic correlations; refining with causality tests (LCV+MR); and then testing lung function and gene expression with PES and TWAS.

Overall, I am quite positive on the goals and core ideas in this paper. The focus on quickly repositioning drug to improve lung function is timely. However, the most interesting and novel results are statistically borderline. Methodologically, I do not see anything new in the paper.

1) There is not much evidence that the PES have enriched signal for lung function (Table 3). The primary PES analyses do not adjust for the overall PRS, hence do not establish Pharmagenic Enrichment, a PRS built on a random subset of SNPs would be expected to have a nonzero effect. The authors recognize this and perform secondary analyses conditional on the PRS to test for enrichment; however, this analysis has null results (Bonferroni-adjusted across 8 tests gives minimum p>.2).

(1a) I don't see any explanation of the permutation test used here, but the details wrt multiple PES thresholds and whether covariates and PRS are permuted as well as the PES are essential and can significantly change results.

2) The PYGB finding is very nice, but was previously found in a similar analysis (in the paper producing the summary stats used here, see Table 1 in Shrine et al., 2019, PMC6397078). This paper also identified the TGF-β superfamily signalling pathway. The observation that this gene can be putatively targeted by Sivelestat is novel (as far as I know) and potentially very exciting, however, this is not discussed much, and no validation is given for the gene-drug interaction, and no explanation is given to relate neutrophil elastase to glucose.

3) I believe the covid analysis assesses only glycemic pathways (Table 4), hence it is hard to evaluate whether the “prey proteins” are more enriched in glycemic pathways than in any other biologically meaningful pathways (further, in the Discussion, it is said that these genes are very pleiotropic). In the future, I think this analysis could be strengthened by testing the PES (or ordinary PRS) against measurements of these proteins in healthy samples, which would demonstrate the link from druggable (or general) glucose biology to the covid-relevant proteins. However, nontrivial effort would be required to integrate such pQTL summary statistics, though I believe such datasets are freely available..

(4a) The LCV paper recommends considering only tests with |GCP|>.6, this rules out the LCV test for FEV1-glucose, FEV1/FVC-HDL, or FVC-leptin. If there is a reason to deviate from the recommended practice, it should be explained.

(4b) Likewise, the MR analyses have only a very weak statistical signal (p=.02,.03): 1 this doesn't survive correction for testing two phenotypes (not to mention the implicit tests prioritized by rhog that were discarded based on LCV); 2 the LCV paper proves these tests are susceptible to inflation by genetic correlation; 3 I do not agree that horizontal pleiotropy has been ruled out, a priori it seems almost certain that many heritable traits (BMI, smoking, diet, exercise,.…) will causally effect both glucose and lung function, to some extent, and moreover you do show that AMT has near-significant TWAS effects on both smoking and glucose.

Reviewer #2:

In this study, Reay et al. used publicly available GWAS data with regards to lung function and biochemical traits to identify molecular mechanisms capable of improving lung function. There are several comments and questions:

1) Reay et al. identified multiple biochemical traits that could be targeted in order to modulate lung function including fasting glucose and fasting insulin levels as well as other glycaemic related pathways and traits. Of these traits they also identify four gene-sets overrepresented with proteins that interact with viral SARS-CoV2 proteins. However as mentioned by Reay et al., previous studies have already found glycaemic control in the form of diabetes to have an effect on both lung function [Klein et al. Diabet Med. 2010] as well as Covid-19 risk and severity [Yang et al., Int J Infect Dis. 2020 94:91-95.]. The results presented here are not groundbreaking on their own.

2) In addition, the authors have employed several statistical methods using existing datasets and performed a comprehensive analysis. However, all of the approaches are from literature, which limits the novelty of this study.

3) The benefit of using the framework proposed by Reay et al. is that it identifies potential new uses for existing drugs through the biochemical traits they modulate. This however means that the potential discoveries regarding drug repurposing are limited to only those compounds with known biochemical effects. Another limitation is the use of genetics data exclusively and not integrating more layers of information that might identify causal traits for any given disease. Various other approaches have extensively been reported before (e.g. Pushpakom et al. Nat Rev Drug Discov. 2019) which creates the question as to how this methodology can be edited in order to maximize the possible findings.

4) The authors claimed that "The correlation between the expression of genes within each pathway encompassed by the PES and the PES profiles themselves could provide further support for their biological impact". This is true when the expression data of the genes come from the relevant tissues. Here, the authors focus on lung function but performed "association between lung function PES and gene expression using RNA sequencing (RNAseq) on transformed lymphoblastoid cell lines (LCL)". My question is how is LCL relevant for lung function?

5) Another question is as to how these findings can be validated either in vivo or in vitro. Figure 5 shows a schematic representation on how treatment could be implemented but it is unclear if any validation experiments have been performed.

6) Throughout this study, the authors used three measurements of spirometry phenotypes for lung function. Then, the results and interpretation in this study should be limited to "lung function". However, the authors generalized their observations from "lung function" to "respiratory disease and respiratory infection". This can be misleading (too far-reaching). For example, lung function is often measured by dynamic spirometry which mostly reflects large airway function. However, respiratory disease like COPD is an inflammatory airway disease which affects the small airways in particular (DS Postma, NJEM, ‎2015). Furthermore, "respiratory infection" by bacterial and viral infection such as tuberculosis, influenza and coronaviruses may lead to completely different pathogenesis. It is hard to believe that hyperglycaemia will have causal effect on these respiratory diareses (infections).

7) For all candidate genes identified by TWAS analysis, they could be further prioritized by checking if they are differentially expressed in the lung between samples with and without impaired lung functions.

8) The authors stated "Probabilistic finemapping of these transcriptome-wide significant regions using a multi-tissue reference panel was then performed to prioritize whether these genes are likely causal at that locus". What is the reasoning behind the prioritization using “multi-tissue reference”? It is known that the majority of cis-eQTLs are shared across tissues, but how this could help to prioritize relevant genes?

Reviewer #3:

The manuscript by Reay et al. presents a set of comprehensive analyses of GWAS data to postulate the causal role of hyperglycemia in lung function. The authors perform a series of causal inference analyses on the GWAS data of several blood traits to identify genetically correlated traits that can be explained by a causal role; the authors then seek to identify drug repurposing targets through two complementary analyses, a polygenic risk score restricted to regions within druggable targets and a transcriptome-wide scan linking genetically predicted expression in blood and lung tissue to lung function. Overall, the manuscript leverages recently introduced sophisticate statistical methods and does a thorough job in stress testing the findings. The putative causal role of fasting glucose joint with putative target genes is an important addition to the field. My main comments relate to the robustness of the causal claims.

1) The MR analyses assume the blood traits (i.e. fasting glucose) are mediating lung function. Whereas several biological plausible avenues are given in the discussion for this assumption, it can certainly be the case that lung function is mediating fasting glucose (e.g., lung function causing overall body impairment which in turn causes changes in blood measurements). I strongly encourage the authors to perform analyses under this reverse causality assumption. In particular, the bivariate MR method of Pickrell NG 2016 would be relevant here.

2) As the authors describe in the Discussion section, wrong assumptions in the MR framework can invalidate the findings. The authors do a great job in assaying the impact of pleiotropy on the MR estimates using recently developed methods (LCV, MR-PRESSO etc); however the causal role of smoking is left ambiguous in the causal inference. Clearly smoking has a causal role on lung function, and GWAS of smoking reveals genetic correlates of smoking status (amount). Is there any impact of smoking on blood traits? Is smoking a collider in the causal diagram genetics -> fasting glucose -> lung function? The authors have access to GWAS of smoking and could leverage the MR toolkit to investigate causal effects of smoking on glucose.

3) The identification of drug repurposing tools using the PES score is inconclusive without some replication/validation. The PES is explaining a small proportion of variation in the trait making the interpretation of PES correlations subtle at best; e.g., it is hard to find a biological role for some of the gene-sets that show significance in Table 2. More importantly, it is unclear what is the null expectation of the PES-gene expression correlation analysis; that is, if PES is computed using random pathways (i.e. not specific to druggable pathways) and re-runs the analyses, what are the results? Or, reversely, if the authors perform the same analyses for a randomly chosen complex trait (e.g., height/bmi), what pathways show up in Tables 2/3?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Genetic association and causal inference converge on hyperglycaemia as a modifiable risk factor for respiratory disease" for consideration by eLife. Two of the three reviewers provided further comments on your manuscript and there followed extensive discussion among them and eLife Editors. We note that the third reviewer previously shared concerns of robustness of results based on border-line statistics and requested that the causality analysis needed to be improved. The evaluation was overseen by a Reviewing Editor and David James as the Senior Editor. The Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation. Nevertheless, the reviewers and editors emphasise that as currently written the work is not yet ready for publication.

Summary:

The authors used publicly available GWAS data with regards to lung function and biochemical traits seeking to use genetics to reposition drugs to improve lung function. The authors sought to identify drug repurposing targets through two complementary analyses: a polygenic risk score restricted to regions within druggable targets and a transcriptome-wide scan linking genetically predicted expression in blood and lung tissue to lung function. Reviewers valued the sophisticated approaches applied in this analysis although questioned the authors' statistical interpretations noting that some results were borderline significant.

Revisions:

The joint view of the reviewers and eLife Editors is that several of the reviewers' comments have been addressed adequately. Nevertheless, other reviewers' comments were not resolved by your revision, most importantly Points 1 and 4 of Reviewer 1. As a group we would be more supportive of the revision if the causality claims were to be toned down with appropriate caveats included throughout, and if the statistical results were to be more appropriately presented. The current version, without such changes, is not judged to be ready for publication.

We are content that you now acknowledge the LCV publication's recommendation that only tests with |GCP| > 0.6 are considered. However, your revision does not follow this recommendation unswervingly: e.g. "We acknowledge that the posterior mean GCP estimate for the FEV1 does not quite the threshold of > 0.6, and thus, the causal relationship was more rigorous with FVC". Moreover, your revision unnecessarily clouds this important issue: "|GCP| > 0.6 previously postulated to be evidence of a rigorous relationship". We do not support uneven application of an established threshold.

It is now acknowledged that some tests were not significant after correcting for multiple tests. Nevertheless, an unwarranted emphasis was sometimes placed on non-significant results, e.g. "However, this still suggested that there was a relationship between the Class B/2 secretin family receptor FVC PES and FVC beyond what is attributable to a genome-wide PGS" and "several gene-sets trended towards surviving correction". Similar problems identified among the MR tests and the adaptive choices for PRS p-value thresholds still need to be addressed. The MR and PES results have relatively weak statistical support and yet this is not reflected by an emphasis placed on them in the Abstract. We are of the view that marginally significant (or null) results can still provide a significant contribution to the field as long as their statistical support is reported appropriately. The manuscript will require changes to the application and interpretation of statistical tests throughout.

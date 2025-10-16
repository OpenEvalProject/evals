# Peer review - Round 1

Editors:
- Joris Deelen, Max Planck Institute for Biology of Ageing Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88768.3.sa0](https://doi.org/10.7554/eLife.88768.3.sa0)

This paper presents a valuable pipeline based on state-of-the-art analytical software that was used to study genetic pleiotropy between neuropsychiatric disorders. The presented evidence supporting the claims is convincing and now includes an appropriate comparison to previously published methods as well as a detailed exploration of the findings. The created pipeline can thus be used by researchers from diverse fields to study different combinations of diseases and traits.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88768.3.sa1](https://doi.org/10.7554/eLife.88768.3.sa1)

The authors investigate pleiotropy in the genetic loci previously associated to a range of neuropsychiatric disorders: Alzheimer's disease, amyotrophic lateral sclerosis (ALS), frontotemporal dementia, Parkinson's disease, and schizophrenia. The local statistical fine-mapping and variant colocalisation approaches they use have the potential to uncover not only shared loci but also shared causal variants between these disorders. There is existing literature describing the pleiotropy between ALS and these other disorders but here the authors apply state-of-the-art, local genetic correlation approaches to further refine any relationships.

Complex disease and GWAS is not my area of expertise but the authors managed to present their methods and results in a clear, easy-to-follow manner. Their results statistically support several correlations between the disorders and, for ALS and AD, a shared variant in the vicinity of the lead SNP from the original ALS GWAS. Such findings could have important implications for our understanding of the mechanisms of such disorders and eventually the possibility of managing and treating them.

The authors have built a useful pipeline that plugs together all the gold-standard, existing software to perform this analysis and made it openly available which is commendable. However, there is little discussion of what software is available to perform global and local correlation analysis and, if there are multiple tools available, why they consider the ones they selected to be the gold-standard.

There is some mention of previous findings of genetic pleiotropy between ALS and these other disorders in the introduction, and discussion of their improved ALS-AD evidence relative to previous work. However, detailed comparisons of their other correlations to what was described before for the same pairs of disorders (if any) is missing. Adding this would strengthen the impact of this paper.

Finally, being new to this approach I found the abstract a little confusing. Initially, the shared causal variant between ALS and AD is mentioned but immediately in the following sentence they describe how their study "suggested that disease- implicated variants in these loci often differ between traits". After reading the whole paper I understood that the ALS-AD shared variant was the exception but it may be best to restructure this part of the abstract. Additionally, in the abstract the authors state that different variants "suggests the role of distinct mechanisms across diseases despite shared loci". Is it not possible that different variants in the same regulatory region or protein-coding parts of a gene could be having the same effect and mechanism? Or does the methodology to establish that different variants are involved automatically mean that the variants are too distant for this to be possible?

These concerns were addressed in the revised version of this manuscript.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88768.3.sa2](https://doi.org/10.7554/eLife.88768.3.sa2)

Summary:

Spargo and colleagues present an analysis of the shared genetic architectures of Schizoprehnia and several late-onset neurological disorders. In contrast to many polygenic traits for which global genetic correlation estimates are substantial, global genetic correlation estimates for neurological conditions are relatively small, likely for several reasons. One is that assortative mating, which will spuriously inflate genetic correlation estimates, is likely to be less salient for late-onset conditions. Another, which the authors explore in the current manuscript, is that some loci affecting two or more conditions (i.e., pleiotropic loci) may have effects in opposite directions, or shared loci are sparse, such that the global genetic correlation signal washes out.

The authors apply a local genetic correlation approach that assesses the presence and direction of pleiotropy in much smaller spatial windows across the genome. Then, within regions evidencing local genetic correlations for a given trait pair, they apply fine-mapping and colocalization methods to attempt to differentiate between two scenarios: that the two traits share the same causal variant in the region or that distinct loci within the region influence the traits. Interestingly, the authors only discover one instance of the former: an SNP in the HLA region appearing to confer risk for both AD and ALS. This is in contrast to six regions with distinct causal loci, and twenty regions with no clear shared loci.

Finally, the authors have published their analysis pipeline such that other researchers might easily apply the same techniques to other collections of traits.

Strengths:

- All such analysis pipelines involve many decision points where there is often no clear correct option. Nonetheless, the authors clearly present their reasoning behind each such decision.

- The authors have published their analytic pipeline such that future researchers might easily replicate and extend their findings.

Weaknesses:

- The majority of regions display no clear candidate causal variants for the traits, whether shared or distinct. Further, despite the potential of local genetic correlation analysis to identify regions with effects in opposing directions, all of the regions for causal variants were identified for both traits evidenced positive correlations. The reasons for this aren't clear and the authors would do well to explore this in greater detail.

- The authors very briefly discuss how their findings differ from previous analyses because of their strict inclusion for "high-quality" variants. This might be the case, but the authors do not attempt to demonstrate this via simulation or otherwise, making it difficult to evaluate their explanation.

These concerns were addressed in the revised version of this manuscript.

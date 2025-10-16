# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, https://ror.org/02s376052 Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85126.sa0](https://doi.org/10.7554/eLife.85126.sa0)

In this important work, the authors present a sequence-based approach using transfer learning and Restricted Boltzmann Machines to predict antigen immunogenicity and specificity. The evidence and methodology are compelling. This work should be of interest to immunologists, computational biologists, and biophysicists.


---

# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, https://ror.org/02s376052 Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85126.sa1](https://doi.org/10.7554/eLife.85126.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Learning the differences: a transfer-learning approach to predict antigen immunogenicity and T-cell receptor specificity" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please streamline the manuscript, which is very complete and rigorous, but also quite long and sometimes intricate. In particular:

– In the Discussion, please emphasize the main conclusions regarding the performance of the method, by concisely explaining for the general reader in what cases it is better than existing methods and what new insights it can provide for immunology (see also Reviewer #1 and Reviewer #3's comments about this).

– The various comparisons to other methods are definitely important and useful, but they sometimes obscure the main points of the paper. We advise to state the conclusions of the various comparisons to other methods in the main text, but to put some of the details of these analyses in Supplement (see also Reviewer #2's comment about this).

2) Please consider including comparisons to transfer learning methods, as advised by Reviewer #3. If feasible, comparisons to general transfer learning tools would be interesting and could strengthen the evidence for broad applicability. If these comparisons are not feasible, please explain why.

Reviewer #2 (Recommendations for the authors):

General Questions

I will provide here some general questions that if addressed could, in my opinion, help improve the clarity of this article.

1. I found the formulation aimed to disentangle the background from selected features really interesting. The way the learning is done is that both datasets are known a priori and then the learning happens sequentially. But what if the datasets where the two generic and specific features are mixed? How would the learning happen in this case? If DiffRBM cannot be used in this situation then it is ok, but it would be good to discuss it as a limitation.

2. The paper mentions that the learning happened in an HLA-specific approach. Although advantages and disadvantages are presented throughout the paper, it would be good to address this important distinction in the discussion.

3. Although I understand this article's main goal is to present a technical solution to specific phenomena in immunology, after reading the manuscript I felt that more specific direct applications should have been discussed. How can the scientific community, take this approach that has been extensively validated and compared and translate it into potential therapeutic or scientific applications?

4. When describing contact prediction and the ranking of peptide positions, the result seemed quite encouraging, however, when one deals with such a small dataset (6-9 positions) then statistical significance becomes a relevant question. Can the authors also discuss this in the presentation of the results? This might help prove a more realistic representation of the predictive qualities of this side of DiffRBM.

5. In Figure 3G the authors estimate the mutational cost of peptides compared to experimental measures. The correlation although significant seems low to me r=0.47. Can the authors comment if this is a limitation or if in fact, other methods cannot reach better correlations than the one presented using DiffRBM?

Reviewer #3 (Recommendations for the authors):

The authors propose a novel model architecture called diffRBM, which is based on the original RBM papers [Hinton, 2002, Hinton and Salakhutdinov, 2006], by adding separate background and differential units and a specific training procedure, as described in section 5.1, opening a possibility to use this model for the transfer of learning.

To be interesting to the wide readership of eLife this paper should show novelty both in terms of the biology it describes and the(AI transfer of learning) tools. Especially as the tool's novelty is emphasized by the authors.

While the paper is very long and detailed it is still a bit unclear to us why other than being novel in its AI methods it is better or more revealing than existing (also non-AI) methods in terms of our understanding of TCR immunology.

We also have the following questions about the methodology:

1. Since it is a novel transfer of learning method, we would like to see a general comparison of this method with other transfer of learning methods on standard benchmarks, not only on the immunological data. Authors claim in section 2 that "… it could be applied to any data that has some distinctive features compared to a much larger pool of data endowed with the baseline properties". We also believe that such a method could be useful to a broader community of researchers. Also, by performing a comparison on standard benchmarks, the novelty of diffRBM could be highlighted more clearly, since it will be certain whether this model consistently achieves state-of-the-art results or not.

We suggest two directions:

1.1 Performing a comparison to the classical transfer of learning and domain adaptation papers, that provide generally good transfer of learning methods, used by a broad research community. Such papers also talk about the transfer of learning benchmark datasets. While most of the datasets are about image data, text-based datasets, more closely resembling biological data, can be found as well in related papers.

An example classical paper:

Adversarial Discriminative Domain Adaptation, Eric Tzeng et. al

1.2. Performing a comparison to the more recent transfer of learning and domain adaptation papers. While it is up to the authors to analyze and define the scope of applicability of the proposed diffRBM model, we can suggest selecting some of the recent papers and benchmark datasets from the links: https://paperswithcode.com/task/domain-adaptation; https://paperswithcode.com/sota/domain-adaptation-on-visda2017. Same comment about closeness to biological data is applicable here as well: it may be necessary to find more specific standard datasets, closely resembling the biological data, if diffRBM is supposed to work well specifically on such data domains.

2. On the other hand, when applied to immunological data (that is described in the paper), we also would like to see more models from the classical and recent transfer of learning papers to be compared to. So if applicable, adding classical and recent transfer of learning models from the above links to the comparison would be beneficial.

Note: If in fact, diffRBM is not widely applicable beyond specific immunological/sequence data – it would be nice to see a detailed analysis as to what properties of the immunological data make diffRBM applicable to it, and not to other data.

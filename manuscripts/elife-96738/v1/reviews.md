# Peer review - Round 1

Editors:
- Yamini Dalal, National Cancer Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96738.3.sa0](https://doi.org/10.7554/eLife.96738.3.sa0)

In the revised version of this important study, the authors present a convincing pipeline for insect genome regulatory annotation across 33 insect genomes spanning 5 orders. Despite technical limitations in the field owing to the lack of comprehensive knowledge of enhancer content in any system, the authors employ several independent downstream analyses to support the validity of their enhancer predictions for a subset of these genomes. Taken together, the revised results suggest that this prediction pipeline may have uses in identifying functional enhancers across large phylogenetic distances. Reviewers note caveats that an experimental validation is not yet available in the field to validate a large class of newly identified enhancers across such evolutionary distances, and other pipelines might be of use to compare. This work will be of interest to the computational genomics, evolutionary biology, and gene regulation fields.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96738.3.sa1](https://doi.org/10.7554/eLife.96738.3.sa1)

Summary:

The authors provide an genome annotation resource of 33 insects using a motif-blind prediction methods for tissue-specific cis-regulatory modules. This is a welcome addition that may facilitate further research in new laboratory systems, and the approach seem to be relatively accurate, although it should be combined with other sources of evidence to be practical.

Strengths:

The paper clearly presents the resource, including the testing of candidate enhancers identified from various insects in Drosophila. This cross-species analysis, and the inherent suggestion that training datasets generated in flies can predict a cis-regulatory activity in distant insects, is interesting. While I can not be sure this approach will prevail in the future, for example with approaches that leverage the prediction of TF binding motifs, the SCRMShaw tool is certainly useful and worth of consideration for the large community of genome scientists working on insects.

Weaknesses from the previous version were appropriately corrected in this revision, as the authors improved data availability including with genome annotation resources.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96738.3.sa2](https://doi.org/10.7554/eLife.96738.3.sa2)

Summary:

In this ambitious paper, the authors develop an unparalleled community resource of insect genome regulatory annotations spanning five insect orders. They employ their previously-developed SCRMshaw method for computational cross-species enhancer prediction, drawing on available training datasets of validated enhancer sequence and expression from Drosophila melanogaster, which had been previously shown to perform well across select holometabolous insects (representing 160-345MY divergence). In this work they expand regulatory sequence annotation to 33 insect genomes spanning Holometabola and Hemiptera, which is even more distantly related to the fly model. They perform multiple downstream analyses of sets of predicted enhancers to assess the true-positive rate of predictions; the independent comparisons of real predictions with simulated predictions and with chromatin accessibility data, as well as the functional validation through reporter gene analysis strengthen their conclusions that their annotation pipeline achieves a high true-positive rate and can be used across long divergence times to computationally annotate regulatory genome regions, an ability that has been largely inaccessible for non-model insects and now is possible across the many newly-sequenced insect scaffold-level genomes.

Strengths:

This work fills a large gap in current methods and resources for predicting regulatory regions of the genome, a task that has long lagged behind that of coding region prediction and analysis.

Despite technical constraints in working outside of well-developed model insect systems, the authors creatively draw on existing resources to scaffold a pipeline and independently assess likelihood of prediction validity.

The established database will be a welcome community resource in its current state, and even more so as the authors continue to expand their annotations to more insect genomes as they indicate. Their available analysis pipeline itself will be useful to the community as well for research groups that may want to undertake their own regulatory genome annotation.

Weaknesses:

The work here is limited by the field-wide lack of an independently validated set of tissue specific enhancers that could be used to directly benchmark this pipeline. The prediction of true positive enhancer identification rates and in vivo reporter gene assays offer some insight into the rates of successful prediction, but the output of SCRMshaw regulatory annotation should be regarded as another prediction-generating tool.

# Peer review - Round 1

Editors:
- Alan Talevi, National University of La Plata Argentina

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90532.3.sa0](https://doi.org/10.7554/eLife.90532.3.sa0)

This important study could potentially represent a step forward towards personalized medicine by combining cell-based data and a prior-knowledge network to derive Boolean-based predictive logic models to uncover altered protein/signaling networks within cancer cells. The level of evidence supporting the conclusions is solid, as the authors present analyses on independent, real-world data to validate their approach. These findings could be of interest to medical biologists working in the field of cancer, as the work should inform drug development and treatment choices in the field of oncology.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90532.3.sa1](https://doi.org/10.7554/eLife.90532.3.sa1)

The authors deploy a combination of their own previously developed computational methods and databases (SIGNOR and CellNOptR) to model the FLT3 signaling landscape in AML and identify synergistic drug combinations that may overcome the resistance AML cells harboring ITD mutations in the TKI domain of FLT3 to FLT3 inhibitors. I did not closely evaluate the details of these computational models since they are outside of my area of expertise and have been previously published. The manuscript has significant issues with data interpretation and clarity, as detailed below, which, in my view, call into question the main conclusions of the paper.

The authors train the model by including perturbation data where TKI-resistant and TKI-sensitive cells are treated with various inhibitors and the activity (i.e. phosphorylation levels) of the key downstream nodes are evaluated. Specifically, in the Results section (p. 6) they state "TKIs sensitive and resistant cells were subjected to 16 experimental conditions, including TNFa and IGF1 stimulation, the presence or absence of the FLT3 inhibitor, midostaurin, and in combination with six small-molecule inhibitors targeting crucial kinases in our PKN (p38, JNK, PI3K, mTOR, MEK1/2 and GSK3)". I would appreciate more details on which specific inhibitors and concentrations were used for this experiment. More importantly, I was very puzzled by the fact that this training dataset appears to contain, among other conditions, the combination of midostaurin with JNK inhibition, i.e. the very combination of drugs that the authors later present as being predicted by their model to have a synergistic effect. Unless my interpretation of this is incorrect, it appears to be a "self-fulfilling prophecy", i.e. an inappropriate use of the same data in training and verification/test datasets.

My most significant criticism is that the proof-of-principle experiment evaluating the combination effects of midostaurin and SP600125 in FLT3-ITD-TKD cell line model does not appear to show any synergism, in my view. The authors' interpretation of the data is that the addition of SP600125 to midostaurin rescues midostaurin resistance and results in increased apoptosis and decreased viability of the midostaurin-resistant cells. Indeed, they write on p.9: "Strikingly, the combined treatment of JNK inhibitor (SP600125) and midostaurin (PKC412) significantly increased the percentage of FLT3ITD-TKD cells in apoptosis (Fig. 4D). Consistently, in these experimental conditions, we observed a significant reduction of proliferating FLT3ITD- TKD cells versus cells treated with midostaurin alone (Fig. 4E)." However, looking at Figs 4D and 4E, it appears that the effects of the midostaurin/SP600125 combination are virtually identical to SP600125 alone, and midostaurin provides no additional benefit. No p-values are provided to compare midostaurin+SP600125 to SP600125 alone but there seems to be no appreciable difference between the two by eye. In addition, the evaluation of synergism (versus additive effects) requires the use of specialized mathematical models (see for example Duarte and Vale, 2022). That said, I do not appreciate even an additive effect of midostaurin combined with SP600125 in the data presented.

In my view, there are significant issues with clarity and detail throughout the manuscript. For example, additional details and improved clarity are needed, in my view, with respect to the design and readouts of the signaling perturbation experiments (Methods, p. 15 and Fig 2B legend). For example, the Fig 2B legend states: "Schematic representation of the experimental design: FLT3 ITD-JMD and FLT3 ITD-JMD cells were cultured in starvation medium (w/o FBS) overnight and treated with selected kinase inhibitors for 90 minutes and IGF1 and TNFa for 10 minutes. Control cells are starved and treated with PKC412 for 90 minutes, while "untreated" cells are treated with IGF1 100ng/ml and TNFa 10ng/ml with PKC412 for 90 minutes.", which does not make sense to me. The "untreated" cells appear to be treated with more agents than the control cells. The logic behind cytokine stimulation is not adequately explained and it is not entirely clear to me whether the cytokines were used alone or in combination. Fig 2B is quite confusing overall, and it is not clear to me what the horizontal axis (i.e. columns of "experimental conditions", as opposed to "treatments") represents. The Method section states "Key cell signaling players were analyzed through the X-Map Luminex technology: we measured the analytes included in the MILLIPLEX assays" but the identities of the evaluated proteins are not given in the Methods. At the same time, the Results section states "TKIs sensitive and resistant cells were subjected to 16 experimental conditions" but these conditions do not appear to be listed (except in Supplementary data; and Fig 2B lists 9 conditions, not 16). In my subjective view, the manuscript would benefit from a clearer explanation and depiction of the experimental details and inhibitors used in the main text of the paper, as opposed to various Supplemental files/figures. The lack of clarity on what exactly were the experimental conditions makes the interpretation of Fig 2 very challenging. In the same vein, in the PCA analysis (Fig 2C) there seems to be no reference to the cytokine stimulation status while the authors claim that PC2 stratifies cells according to IGF1 vs TNFalpha. There are numerous other examples of incomplete or confusing legends and descriptions which, in my view, need to be addressed to make the paper more accessible.

I am not sure that I see significant value in the patient-specific logic models because they are not supported by empirical evidence. Treating primary cells from AML patients with relevant drug combinations would be a feasible and convincing way to validate the computational models and evaluate their potential benefit in the clinical setting.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90532.3.sa2](https://doi.org/10.7554/eLife.90532.3.sa2)

Summary:

This manuscript by Latini et al describes a methodology to develop Boolean-based predictive logic models that can be applied to uncover altered protein/signalling networks in cancer cells and discover potential new therapeutic targets. As a proof-of-concept, they have implemented their strategy on a hematopoietic cell line engineered to express one of two types of FLT3 internal tandem mutations (FLT3-ITD) found in patients, FLT3-ITD-TKD (which are less sensitive to tyrosine kinase inhibitors/TKIs) and FLT3-ITD-JMD (which are more sensitive to TKIs).

Strengths:

This useful work could potentially represent a step forward towards personalised targeted therapy, by describing a methodology using Boolean-based predictive logic models to uncover altered protein/signalling networks within cancer cells.

Authors have validated their approach by analysing independent, real-world data

Weaknesses:

No weaknesses were observed by this reviewer for the revised version.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90532.3.sa3](https://doi.org/10.7554/eLife.90532.3.sa3)

Summary: The paper "Unveiling the signaling network of FLT3-ITD AML improves drug sensitivity prediction" reports the combination of prior knowledge signaling networks, multiparametric cell-based data on the activation status of 14 crucial proteins emblematic of the cell state downstream of FLT3 obtained under a variety of perturbation conditions and Boolean logic modeling, to gain mechanistic insight into drug resistance in acute myeloid leukemia patients carrying the internal tandem duplication in the FLT3 receptor tyrosine kinase and predict drug combinations that may reverse pharmacoresistant phenotypes. Interestingly, the utility of the approach was validated in vitro and using real-world data.

Strengths:

The model predictions have been validated in vitro and using external data.

This is a complex study, but readability is enhanced by the inclusion of a section that summarizes the study design, plus relevant figures. The availability of data as supplementary material and the availability of code in GitHub are also high points.

Weaknesses:

There are some apparent discrepancies between predicted and observed data that have been seemingly overlooked.

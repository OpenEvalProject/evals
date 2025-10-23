# Peer review - Round 1

Editors:
- Alfonso Valencia, Barcelona Supercomputing Center - BSC Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62148.sa1](https://doi.org/10.7554/eLife.62148.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This resource aggregates information on interactions from public immunological

(interleukins, checkpoints, and other immune modulators) data sets to facilitate the analysis of combinations of drug and ligands onto immune cell activation. The system, based on underlying random-forest classification to sort out experimental noise and reveal new properties, provides information at the level of general functional classes (enrichment analysis) associated to estimated error levels, within a user oriented graphical interface.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Deciphering the combinatorial landscape of immunity" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The paper describes an method to study interactions in a large immunological molecular system of ~30,000 interactions: The main hypothesis derived from the system is related with the immunological effects of TNFα on IFNβ.

There are a number of problems with the current submission. First, the proposed method has not been systematically validated beyond the arguments in this paper. The example chosen corresponds to a well-known system, e.g. TNF cytokines synergies, for which it is unclear how much the paper adds. In any case, to have a significant impact in biology a more challenging hypothesis , going beyond the already-known synergies of TNF, should be proposed and ideally, it would be followed by additional experiments. Only then the potential of the system will be demonstrated as actually able to uncover new biology.

While based on this criticism the paper will not be acceptable for publication, it might be considered if organized as a resource paper (A Tools and Resources article allows authors to publish the details of new experimental techniques, datasets, software tools, and other resources). It will be also possible to consider a future version of this work including a complementary validation of the method and experimental follow-up of the proposed models.

Reviewer #1:

The authors have developed an interesting resource with 30k interactions extracted from public immunological datasets (25 human and 7 murine combination treatment studies).

On this data set they apply a aggrupation and training strategy (random forest algorithm operating on what are called "logic principles" of the interactions) to differentiate single responses from combine ones (synergies) in a set of interleukins, checkpoints, and other immune modulators. The system works at a semi-qualitative level that takes into account the fluctuations and variability of the data, and provides an interpretation at the level of general functional classes (enrichment analysis).

The potentially more interesting innovation of the model is the systematic introduction of error levels. The most valuable asset is the collection of interactions from public data. The proposed machine learning technology, the biological analysis and the grouping of genes is also rather standard and simple. The visualization is nice and help to understand the results.

The key problem is that the method is not validated in any systematic way. The proposed experimental follow-up might be interesting from a biological point of view but cannot be considered systematic validation. It might be a nice tool for exploration but the information presented is not enough to consider it as a prediction system.

Other points are related with the way the methodology is presented, that is rather obscure when in practice it is very simple, i.e. functional inference is enrichment analysis, machine learning interaction classification is a random forest classifier, omic analysis is expression data, etc. While the main idea of combining and averaging results is not explained clearly.

My opinion is that this paper could be considered for publication if it can be presented as a resource for the exploration of immunological interactions based on the collected data, gene aggregation strategy and visualisation system. In this case, it would have to be written in a different way, clearly oriented to use of the system and providing the biological results as examples of use.

Reviewer #2:

In this article, Cappuccio et al. introduce a computational method to better assess the impact of combinations of drug and ligands onto immune cell activation. This is a problem of fundamental significance, both from the theoretical side (how to tackle the combinatorial complexity of immunological interactions?) and from the practical side (how to leverage this combinatorial complexity to maximize clinical perturbation?). There exist many experimental datasets that have attempted at reporting the transcriptional responses of cells under single and dual perturbations, yet, there does not exist a systematic framework to integrate, classify and leverage these datasets. This publication introduces a Synergistic/Antagonistic Interaction Learner (iSAIL) to tackle this issue and to publicize the method.

One of the key premises of this computational framework is that individual measurement can lead to inaccurate classification of molecular perturbations, because of limited signal/noise and/or saturation. However, when leveraging the large number of datasets already available, one can improve on this computational task and get a more accurate classification. Hence, the key novelty in this manuscript is presented in Figure 2 and 3 where the statistical framework is introduced. Again, the sobering experimental fact is that individual experiments (e.g. dataset acquired for a given cell type and/or a limited set of perturbation) can be misleading classifying how two molecular perturbations can combine. The computational framework proposed here use random-forest classification to sort out this experimental noise and reveal new properties.

Figure 4 and 5 present one example related to responses to IFN-b and TNF to highlight an emergent function of these cytokines as highly synergistic depending on the molecular/cellular context. One could question whether this method scales up to higher level of combinations of perturbations: given the exponential explosion when combining N drugs, how do the computational framework introduced here help in designing higher order of immunological perturbation?

Overall, this is a serious/robust study addressing an important issue in pharmacology and immunology. Additional details about the method would help the reader better grasp the novelty of the computational method but release of the iSAIL method on a website is making this criticism less stringent: experimentalists will be able to test the method directly and assess its usefulness. More specific comments/suggestions are listed below.

Detailed comments:

Results first paragraph: What is defined here as synergy and antagonism is not congruent with the classical definitions of these terms. One example of this is profile 4 in Figure 1—figure supplement 1, which shows that individual treatments inhibit expression of a particular gene, and that the combination of treatments enhances that inhibition. Classically, this would be considered synergism in the ability of inhibiting expression of that gene, but in your classification this is considered as antagonism, because the final expression levels are lower than the expected by additivity. In your previous paper (Cappuccio et al., 2015), your classification was in agreement with previous definitions, and this interaction was classified as "negative synergy". Unless you provide support and clear explanation for changing this nomenclature, I would recommend going back to the nomenclature used in Cappuccio et al., 2015, namely calling them "positive and negative interactions", rather than "synergistic and antagonistic interactions". Additionally, for cases were the combination interactions were not as dramatic as the few examples showed in the figures, or for profiles called "ceiling" or "floor", it is not possible to determine synergism or antagonism in the absence of dose-response curves obtained by -omics experiments (Chou et al., 2006). The absence of dose-response information would also be problematic for genes which regulation is not monotonic as a function of dose (Senthivel et al., 2016).

Referring to "emergent responses (see Figure 1—figure supplement 1 , profile 3)", make effect bigger in Figure 1—figure supplement 1 so it is clearer to see the differences between profile 3 and 7.

Referring to "would be aggregated with nominal synergistic effects due to frequent cellular or assay saturation, which have low biological significance (see Figure 1—figure supplement 1 , profile 7)”. Please explain better the text before the comma. I think in profile 7 you are referring to the "floor" profile, where background in the assay or basal levels of gene expression makes it look like synergistic, and in your current explanation you are referring to the "ceiling" profile, where saturation is the problem. You can write something similar as it appeared later in the paper regarding these interactions that are likely not meaningful: "represent range limitations of the assay or biological responses"

Multiple instances:

Please replace TNF-α with simply TNF. The former term is obsolete (there is no TNF-β…) and has been retired.

Figure 1: The panels for gene 2 and gene N could be permuted to maintain the hierarchy shown in the second column (synergistic > additive > antagonistic). The graphical rendition of drug interactions as slanted panel in the second column is hard to interpret: what do the authors want to highlight there?

Figure 2D: stimulat -> stimulate

Figure 2E: Specify which IFN.

Figure 5 legend: Include concentrations of IFN-β and TNF (these could be normalized to EC50 to make it easier to read and interpret -is the experiment done at saturation -ceiling-, at subdetectable levels -floor- or in linear regime ;around EC50)

Label the columns in panel c

Reviewer #3:

This study utilizes machine learning to examine gene expression datasets of immune stimulation and attempts to derive a universally applicable set of canonical responses. The basic approach dates back to the work of Janes et al. (Science 2005), which, incidentally, is not cited. My main concern centers on the need for a relatively large amount of data combined with synthetic data in order to obtain insights focused on well-studied interactions of TNF with other cytokines. Furthermore, I am unclear as to the true universal applicability of this approach, for the following reasons:

1) The authors mention that the datasets used involved multiple time points, but it is unclear how dynamics are being handled and modeled across these datasets. One would fully expect that in any extensive time course study of two stimuli, multiple outcomes (e.g. potentiation followed by tolerance or stimulation followed by suppression) would be observed. How can the algorithm then decompose such phenomena into a single characteristic response (i.e., does the algorithm treat each time point as a separate experiment, thereby losing true time-dependent interrelationships?)

2) The system chosen for validation, namely TNF + IFN-β, does not seem particularly novel. It has been appreciated for decades that TNF synergizes with other cytokines to produce an array of effects, including potentiation and tolerance as examples of preconditioning. A demonstration of a truly unexpected set of interactions between stimuli would have been more convincing.

3) The additional validation studies focused on VCAM1 also seem to be focused on relatively well-studied phenomena. Multiple other gene transcripts that appear more novel are not followed up.

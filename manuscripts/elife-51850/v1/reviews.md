# Peer review - Round 1

Editors:
- Nicola L Harris, Monash University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51850.sa1](https://doi.org/10.7554/eLife.51850.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript employs a metabolic model of the filarial nematode Brugia malayi to predict metabolic pathways used by the parasite at different lifecycle stages and within different environments. The work represents one of the first comprehensive investigations using metabolic modelling to predict essential reactions in a parasitic nematode and offers a potentially useful strategy for the development of new drugs targeting these important pathogens. The authors validate their work by predicting several druggable targets based on the model, and proceed to validate three of these reactions using already available drugs.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Modeling the metabolic interplay between a parasitic worm and its bacterial endosymbiont identifies novel drug targets" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Nicola L Harris as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: James B Lok (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Although reviewers agree the idea of using metabolic modelling approaches to identify novel drug targets for fillarial infection is of high interest, a number of deficiencies in the experimental rationale, modelling approach employed and communication of the rationale and outcomes were identified. In particular it was not clear why the authors did not choose the most recent work regarding C. elegans metabolic Reconstruction (WormJam: A consensus C. elegans Metabolic Reconstruction and Metabolomics Community and Workshop Series. Worm. 2017; 6(2): e1373939) The modelling of host conditions or the bacterium Wolbachia was felt to be insufficient in the current form.

Reviewer #1:

The manuscripts by Curran et al. employs a metabolic model of the filarial nematode Brugia malayi to predict metabolic pathways used by the worm at different lifecycle stages and within different environments. The authors then use the model to predict essential reactions useful for drug targeting and validated three of these reactions using already available drugs.

The work is both interesting and novel in that 1) new drug targets for Brugia are needed and valuable and 2) large scale metabolic modelling of a parasitic nematode has not been reported previously.

However as it stands a large amount of data is given and the rationale behind the experimental design is not always clear, making it difficult for the reader to determine how meaningful each dataset is. The manuscript could be greatly improved if more effort was made to restrict the data shown in the main figures related to environmental conditions (HOLG, LOLG, LOHG AND HOHG) to the those in that each lifecycle stage would be expected to actually encounter within the host. The relationship of each dataset to one another also needs to be commented on more clearly (for instance what environmental conditions were the predictions made in Figure 7 performed under?).

One of the most important figures in the manuscript is Figure 8 in which the ability of the model to predict drug targets was determined using adult worms. Given that the preceding sections of the manuscript focused heavily on determining the environmental factors influencing the model it would important to determine whether these same factors influence in the activity of the drugs. This could be achieved by performing the assays in cultures containing medium with different levels of glucose and under low or high oxygen conditions. This is particularly important given emerging data indicating that drug screening for anti-helminthics yields different outcomes when drugs are tested under high oxygen conditions (such as that employed in Figure 8) versus low oxygen conditions). Drugs should also be compared side by side in these assays to an “in use” anti-helminthic such as ivermectin.

Reviewer #2:

The paper presents the metabolic network model of a parasitic worm and its bacterial endosymbiont, and it uses this model to study the metabolic adaptations that allow the survival of the parasite. Metabolic models can be indispensable for the study of such complex systems, the interpretation of experimental data and the identification of drug targets.

The modeling effort presented in this manuscript suffers from major issues which make the present model(s) and their presentation unacceptable for final publication. When one uses a metabolic model, and any model, it is of fundamental importance to first assess the quality of modeling framework, before using the model for the analysis of experimental data. Otherwise, the results of the model-based analysis of the data are simply artifacts of the errors in the low-quality models.

The following are some of the major issues in the development and quality of the models in the manuscript.

* While many metabolites and nutrients are present in the worm cytosol, not all of them are available to bacterium. The conditional availability of the nutrients and metabolites will impact the conclusions about the physiology (and gene essentiality) of the bacterium.

* The model appears to be built based on a semi-manual curation. There are currently established methods and workflows that should be used (such as RAVEN). The authors should consider all these, discuss their capabilities and provide a justification why they are not using one of them. I think that couple of these methods have been optimized and any other procedure such the one followed here is at the best suboptimal.

* Within the established metabolic modeling workflows there is also the concept of "metabolic tasks" which defines the metabolic capabilities of the organisms and the ability of the model to fulfill these tasks. The authors must follow such workflow, define the metabolic tasks and assess the performance of their models with respect to these tasks. Otherwise, we cannot systematically evaluate the quality of the models.

* The model is using only two compartments of the host organism. This is already a major inefficiency of the models here. For every eukaryote that has been model with high quality additional other compartments have been considered (such as ER and nucleus) and their consideration has been shown to be important for capturing the physiology of the organism.

* It is not clear what is the information used for modeling transporters (Berg et al., 2002; not a proper citation and I have difficulty to find this with such limited and imprecise information). It is important to carefully consider which transporters across compartments and across cytosol and the bacterium are feasible. Careful consideration, curation, modeling and justification of the transporters is extremely important for the quality and the performance of the model.

* The authors ignore the most important "compartment" which is the environment of the human host. It has been shown in the past that modeling and properly contraining these interactions are essential for the evaluation of the models of parasites and on the use of these models for the analysis and interpretations of experimental data (e.g., PLoS Comput Biol. 2017 Mar; 13(3): e1005397 and PLoS Comput Biol. 2017 Mar; 13(3): e1005397.) For example the studies here should first identify what are the essential nutrients and what are the commonly and most probably used nutrients. The same applies also for modeling the nutrients available to bacterium (as mentioned earlier.)

* The authors use as a reference model the previously published model iCEL1273 for the worm E. elegans. However, the quality of this model is low and there is a later work for a consensus C. elegans metabolic Reconstruction (WormJam: A consensus C. elegans Metabolic Reconstruction and Metabolomics Community and Workshop Series. Worm. 2017; 6(2): e1373939) which should be consider. The authors should use this work as reference or provide a strong justification why they choose exclusive use iCEL1273, which is not of good quality.

* There is not a good analysis on the modeling of the bacterium Wolbachia. The choice of reactions is not justified, and again, there is not a clear procedure outlined for the reconstruction and modeling of the bacterium metabolic modeling.

* It also appears that important information on model development and statistics is missing. The only Supplementary File is an excel file with "Single knockout" data.

* The authors do not discuss the reversibility of the reactions and their thermodynamic feasibility. This is an essential procedure in model reconstruction and development, and it is well known and appreciated fact that reaction directionality has a significant impact in the performance of the model for flux estimation and gene essentiality analysis.

* The model simulations do not really offer a lot in our understanding of the physiology of the organisms. The authors could try to extract the import lessons from the simulations and communicate them in a more clear and informative way. However, and without a proper constraining and classification of the nutrient uptake fluxes, it is not possible to gain a clear understanding of the results presented here.

* It is very hard to assign significance in the essentiality analysis since the model reconstruction and the assignment of constraints has not been done properly and it has been justified in a convincing manner (as discussed above).

* The predictions discussed in the manuscript do not provide a sufficient validation of the model. Some of them could have been predicted without the use of the model. The small number of predictions does not provide enough evidence and confidence to support the claim the "metabolic model (in this manuscript) is a useful approximation of the worm”.

* It is not clear what are the methods used by the authors for the integration of transcriptomics and metabolomics data. There are exist many well established methods that are used for such integration and such method-based integration is the current standard in model reconstruction and analysis.

Reviewer #3:

This paper reports the development of a new computational model of intermediary metabolism in the lymphatic dwelling filarial nematode Brugia malayi. This model predicts metabolic flux through catabolic and biosynthetic pathways under varying conditions of oxygen tension and glucose availability in key life cycle stages of the parasite that infect the definitive host (post-infective L3, L4, Male and Females).

The paper has many strengths of a substantive nature, which are enumerated below. The paper is also very well written, and only a few minor changes are recommended in the text. The authors should give some attention to specific points about the presentation of Figures 1 and 2.

Substantive strengths

1) The metabolic model builds on others developed for Onchocerca and C. elegans. This is a logical approach and one that undoubtedly streamlined construction of the Brugia model.

2) Confidence in the fidelity of the model is engendered because it captures salient features of nematode metabolism, such as the switching between aerobic and anaerobic pathways, a predicted Crabtree effect under high oxygen and glucose, and use of glutamate to aspartate conversion to generate energy.

3) Great that the model predicts ability of the parasite to utilize aerobic and anerobic metabolism as it proceeds through various body compartments in its migration within the host.

4) The model prediction that glucose and oxygen are limiting factors in fitness of adult B. malayi is an interesting and worthwhile finding that could direct discovery of new compounds acting on energy metabolism.

5) Identification of scenarios where multiple redundant pathways are available to the parasite to achieve the same metabolic output also seems a very astute finding, as such pathways would presumably be less advantageous likely drug targets. ie. they are less likely to be essential.

6) Concordance between model predictions and actual metabolomics on extracts of staged parasites bolsters confidence in the model.

7) Through a process of in silico knockouts, the authors have predicted 99 enzymatic reactions that are essential. This demonstrates a crucial practical application of the model.

8) The authors definition of essential reactions as being ones whose disruption would

reduce predicted parasite biomass by 50% or more seems valid to this reviewer given that such a reduction in biomass would likely compromise the worms' ability to survive in the hostile environment of an immunocompetent host.

9) The "two hit" discovery from model simulations that two different reactions participate in pathways that lead to the same metabolite could facilitate the design of combination therapies that would greatly decrease the likelihood of drug resistance.

10) The authors used a rational and very practical scheme for identifying potential target pathways from among the 99 essential reactions predicted by the model. Criteria in this scheme included expression across multiple life stages, number and availability of existing inhibitors in the ChEMBL database and similarity to human homologs (presumably a detracting factor). Selected compounds from this list, targeting diverse pathways such as isoprenoid precursor biosynthesis, gluconeogenesis and purine metabolism, namely fosmidomycin, mdl-29951 and tenofovir, respectively, either decreased Wolbachia loads, and/or fecundity in cultured adult B. malayi. These results bolster confidence in the model's utility in identifying drug targets in Brugia spp, and perhaps in Wuchereria bancrofti as well.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for choosing to send your work entitled "Modeling the metabolic interplay between a parasitic worm and its bacterial endosymbiont identifies novel drug targets" for consideration at eLife. Your letter of appeal has been considered by a Senior Editor and a Reviewing editor, and we are prepared to consider a revised submission with no guarantees of acceptance.

Summary

The manuscripts employs a metabolic model of the filarial nematode Brugia malayi to predict metabolic pathways used by the worm at different lifecycle stages and within different environments. The authors then use the model to predict essential reactions useful for drug targeting and validated three of these reactions using already available drugs.

The work is both interesting and novel in large scale metabolic modelling of a parasitic nematode has not been reported previously and the reviewers agree that it offers information will be useful for the community, keeping in mind some major challenges when working with parasitic nematodes.

However it was felt that the demonstration of anti-filarial activity as shown for the three drugs is not sufficient validation of a genome scale model. The authors should detail under which model assumptions these validations will fail and state these as a calibration rather than a validation. Further validation should be provided as outlined under essential revisions below.

Essential revisions:

1) A combination of the following things should be provided as further validation of the model:

a) Predicted drugs being effective. At the current time it isn't possible to judge whether this is significant in absence of the knowledge regarding how the drugs tested were selected from the prioritized list? Details of how the three drugs were selected from the prioritized list should be provided (Presumably, the mentioned targets were not the only targets associated with these drugs in Chembl? If so, maybe listing the other associated targets in a supplement would be useful, since it is possible that it is some of those targets that may be involved in the activities observed)

b) Gene essentiality comparison with C. elegans. A proper comparison should be made inclusive of statistics. If the model predictions have significant enrichment of such genes, this would be helpful.

c) If there is data out there about wolbachia load in different stages, this could be another validation if it is consistent with what the model predicts in terms of optimal wolbachia load under different stage transcriptome-based constraints.

2) A few more cases of FBA's (and pFBA's) demonstrated utility in uncovering real biologically relevant insights should be included in the Introduction along with corresponding references.

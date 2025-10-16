# Author response - Round 1

Authors:
- David M Curran ([ORCID: 0000-0003-2749-869X](https://orcid.org/0000-0003-2749-869X))
- Alexandra Grote
- Nirvana Nursimulu
- Adam Geber ([ORCID: 0000-0003-3022-0525](https://orcid.org/0000-0003-3022-0525))
- Dennis Voronin
- Drew R Jones ([ORCID: 0000-0001-8732-9818](https://orcid.org/0000-0001-8732-9818))
- Elodie Ghedin ([ORCID: 0000-0002-1515-725X](https://orcid.org/0000-0002-1515-725X))
- John Parkinson ([ORCID: 0000-0001-9815-1189](https://orcid.org/0000-0001-9815-1189))

## Response text

DOI: [10.7554/eLife.51850.sa2](https://doi.org/10.7554/eLife.51850.sa2)

[Editors’ note: The authors appealed the original decision. What follows is the authors’ response to the first round of review.]

Although reviewers agree the idea of using metabolic modelling approaches to identify novel drug targets for fillarial infection is of high interest, a number of deficiencies in the experimental rationale, modelling approach employed and communication of the rationale and outcomes were identified. In particular it was not clear why the authors did not choose the most recent work regarding C. elegans metabolic Reconstruction (WormJam: A consensus C. elegans Metabolic Reconstruction and Metabolomics Community and Workshop Series. Worm. 2017; 6(2): e1373939) The modelling of host conditions or the bacterium Wolbachia was felt to be insufficient in the current form.

We would first like to thank you for taking the time to oversee the reviews of our manuscript. While we were obviously disappointed with your initial decision, in reading over the reviews, we became concerned that the decision may have been unduly influenced by the comments provided by reviewer 2 which (as we highlight below) we consider to be well off base for current expectations in the field. We note that the other two reviewers were very positive about the study, highlighting, in the case of reviewer 3, ten substantive strengths.

As you can appreciate, despite its global health importance, Brugia malayi remains an extremely challenging organism to work with. Consequently, unlike model organisms, or the experimentally tractable Plasmodium parasite, biochemical data for Brugia is greatly limited, an issue that perhaps is not apparent to reviewer 2. By attempting to crystalize current knowledge of Brugia metabolism, this study provides a valuable resource for the community that has been demonstrated to generate new hypotheses, including drug targets that we have successfully validated. We therefore politely suggest that the points raised by reviewer 2 do not reflect the current state of the field and, as we show below, we believe that each of their comments are readily addressable. We are therefore writing to request whether you would be willing to consider a revised version of our study which addresses each and every one of the comments raised by the reviewers.

Reviewer 2 expressed the following concerns:

1) It is not clear which metabolites are available to the worm and its endosymbiont which impact predictions

This is a common criticism of any metabolic model and reflects an incomplete knowledge of transport reactions between cellular compartments, particularly for non-model organisms. Such reactions are challenging to infer computationally and typically identified through biochemical studies. Here we chose to be conservative and included transport reactions as required by reactions assigned to the compartments. This is a standard approach used in the field has the potential to result in false negatives, but importantly, will not impact false positives. Hence any essential reactions we predict in such a model will remain essential irrespective of additional transport constraints.

2) The authors do not use established methods and workflows such as RAVEN or concepts such as metabolic tasks

We would politely point out that, as outlined by Machado et al. NAR 2018, our approach is equivalent to the many tools that use a bottom-up approach including: (i) annotate genes with metabolic functions; (ii) retrieve the respective biochemical reactions from a reaction database, such as KEGG (26); (iii) assemble a draft metabolic network; (iv) manually curate the draft model. Our approach has been applied to several reconstructions including: Song et al., 2013; Blazejewski et al., 2015; Cotton et al., 2016; International Helminths Genome Consortium Nature Genetics 2019). We would add that a key advance of our approach over other approaches is the use of more sensitive enzyme annotation tools to complete the first step. We can of course provide additional details concerning the construction of our model.

3) Unlike other eukaryotic models, only two host compartments are considered in the Brugia model and that, unlike other studies of parasites, the human host is ignored.

As noted above, Brugia is a challenging organism to work with and lacks the depth of knowledge available for other organisms to accurately assign metabolic reactions to specific compartments. We further note that the C. elegans model (iCEL1273) also features only two compartments. Regarding the comment concerning the human host, the reviewer cites a study (actually they cited the same study twice) to illustrate how additional data is used to improve a previously published model of Plasmodium metabolism. In the same way, we would expect that our initial model will be refined as new data becomes available.

4) The model simulations do not offer a lot of our understanding of the physiology of the organisms

This seems to be entirely contradicted by the ten substantive strengths outlined by reviewer 3 who appears to be more knowledgeable concerning Brugia physiology.

5) We compare our model to iCEL1273 which is deemed low quality and should compare to a later work

We were puzzled by this comment as the reviewer does not provide any evidence to support their claim that the quality of iCEL1273 is low. We were also initially puzzled by the suggestion to use the reconstruction referred to in WormJam: A consensus C. elegans Metabolic Reconstruction and Metabolomics Community and Workshop Series. Worm. 2017; 6(2): e1373939. This latter reference appears to report on a community effort to develop a metabolic reconstruction for C. elegans, but provides no link to any actual reconstruction. After some digging we found Witting et al. Frontiers in Molecular Biosciences 2018 which describes the integration of four previously published models including iCEL1273. We can of course compare our model to this new model in any revision. But perhaps more importantly this illustrates exactly the process of how initial metabolic reconstructions can be further embellished as new data comes in. However, this process cannot work if the initial models do not get published!

6) It is hard to assign significance to the essentiality analysis

As noted above, our model is conservative and we expect that we may have missed some essential reactions. Nonetheless we stand by our predictions of essential reactions: due to limitations in obtaining worms for these experiments, we were only able to target 3 reactions; satisfyingly we validated all three. This raises a key point, due challenges in obtaining worms for such experiments, resources such as the one presented are critical to help prioritize experiments for in vitroexperiments that rely on such a rare resource.

[Editors’ note: what follows is the authors’ response to the second round of review.]

Essential revisions:

1) A combination of the following things should be provided as further validation of the model:

a) Predicted drugs being effective. At the current time it isn't possible to judge whether this is significant in absence of the knowledge regarding how the drugs tested were selected from the prioritized list? Details of how the three drugs were selected from the prioritized list should be provided (Presumably, the mentioned targets were not the only targets associated with these drugs in Chembl? If so, maybe listing the other associated targets in a supplement would be useful, since it is possible that it is some of those targets that may be involved in the activities observed)

As requested we now provide more details concerning the prioritization strategy together with a full table (Subsection “Fosmidomycin, MDL-29951, and Tenofovir possess antifilarial activity” and Supplementary file 3).

“To validate the performance of our model, we selected a subset of reactions for targeted inhibition using known drugs. Of the 102 reactions predicted to be essential, 77 were associated with one or more genes (33 in the cytosol, 41 in Wolbachia, and 3 in the mitochondria). This subset was chosen because they were considered less likely to be model artifacts. Reactions were prioritized by considering their expression across different life stages, the number of inhibitors identified in the ChEMBL database (Gaulton et al., 2012; Davies et al., 2015; Gaulton et al., 2017), and the similarity to human homologs (see Supplementary file 2 for details). From this list we selected three inhibitors to validate our predictions through in vitro assays (Table 1), primarily based on their cost and availability from suppliers.”

b) Gene essentiality comparison with C. elegans. A proper comparison should be made inclusive of statistics. If the model predictions have significant enrichment of such genes, this would be helpful.

As recommended we performed a one-tailed Fisher's Exact Test comparing these sets, and calculated a p-value of 1.9E-11 (meaning the probability of finding 52 or more hits out of 71 choices by random chance is 1.9E-11).

“73% of the predicted iDC625 essential reactions overlap with the experimentally determined essential reactions of C. elegans (significance determined by one-tailed Fisher’s Exact Test; hypergeometric pvalue = 1.9E-11).”

c) If there is data out there about wolbachia load in different stages, this could be another validation if it is consistent with what the model predicts in terms of optimal wolbachia load under different stage transcriptome-based constraints.

As Wolbachia population dynamics have been well-studied in B. malayi (McGarry et al., 2004; Grote et al., 2017), we agree with the reviewer that one source of additional validation might be to calibrate our model to life stage-specific population sizes. However, it should be appreciated that our model is concerned with the total metabolic capacity of the bacterium which does not directly correlate with population size. Further, there is very little information available on the nutrients available in the environments occupied by many of the life stages, rendering it highly challenging to accurately model metabolically inert stages like L3 (Li et al., 2009). We include the above as new text in the manuscript:

“As Wolbachia population dynamics have been well-studied in B. malayi (McGarry et al., 2004; Grote et al., 2017), it is tempting to attempt to calibrate our model to life stage-specific population sizes. However, our model is concerned with the total metabolic capacity of the bacterium which may not correlate directly with population size, and there is very little known about the nutrients available in the environments occupied by many of the life stages, especially metabolically inert stages like L3 (Li et al., 2009).”

2) A few more cases of FBA's (and pFBA's) demonstrated utility in uncovering real biologically relevant insights should be included in the Introduction along with corresponding references.

We now provide more background and references on the application of FBA in the Introduction:

“Beyond the identification of essential genes and potential therapeutic targets, the analyses of metabolic reconstructions with FBA have been used to identify knowledge gaps and improve annotations in pathogens like Pseudomonasaeruginosa (Oberhardt et al., 2008) and Leishmania major (Chavali et al., 2008), improve bioreactor yields of non-vital compounds in Pseudomonasputida (Puchałka et al., 2008), explain the complex observed substrate specificities of Desulfovibrio vulgaris (Flowers et al., 2018), explain observed metabolic changes in the brains of patients with Parkinson’s disease (Supandi and van Beek, 2018), and even demonstrate the non-biomass related factors affecting tissues growing by cell expansion in tomato plants (Shameer et al., 2020).”

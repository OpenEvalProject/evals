# Peer review - Round 1

Editors:
- Hugo J Bellen, Baylor College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61590.sa1](https://doi.org/10.7554/eLife.61590.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Your work shows how SWIP-P1019R drives endo-lysosomal expansion (a phenotype associated Lysosomal Storage Diseases) and leads to cognitive-movement impairments in mice and humans. In addition, the WASH proteome will be a valuable resource for the community.

Decision letter after peer review:

Thank you for submitting your article "Genetic Disruption of WASHC4 Drives Endo-lysosomal Dysfunction and Cognitive-Movement Impairments in Mice and Humans" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Huda Zoghbi as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

All three reviewers agreed that Courtland et al. present and interesting and important aspect about the interactome of WASH complex in the brain. Their analysis of the effects of SWIP P1019R in endolysosomal pathway and in neurodegenerative disease is novel. All reviewers agreed that this manuscript does warrant publication in eLife. However, the following major concerns needed to be addressed.

A) The authors need to provide more information about their experimental design and data analysis to address the following concerns

Reviewer 1:

1) Why was WASH1 used as the fusion target for BioID? Is BioID2 alone a good control for this experiment? Had the authors considered using WASH1 with its N-terminal WASH assembly domain removed as a better control?

2) Why was SPS-MS3 not used as the mass spectrometry approach? More accurate data may have been achieved even with the application of FAIMS.

3) There are currently no plots of the data and the authors use a bespoke data analysis pipeline. It is not clear whether the experiment was successful and the results crucially depend on successful separation of the organelles. The paper is currently missing western blots to confirm separation of the organelles, upon which the analysis pipeline depends.

4) To the reader the power of using a spatial proteomics approach such as the LOPIT-DC method of Geladaki et al. seems to be a bit lost here. The authors need to be clear what added information this experimental design gives over simply just looking at changes in the total proteome. It is hard to reconcile the data with organelle re-localization without firstly showing total abundance changes between the MUT and wildtype, and secondly giving some indication that the necessary organelle resolution has been achieved (as above). This should be clarified in the text. For example, if a protein resides in more than one location, and there is a change in the abundance of this protein in one of these locations, this may manifest itself and a perceived change is localization.

5) Furthermore, if endosomal properties are changed as a result of the mutation it might result in the endosomal protein pelting at different speeds. This will complicate the statistical analysis because fractions cannot be compared like for like.

6) Was the final cytosolic (supernatant) fraction was discarded? If the abundance of the cytosolic pool of these proteins is changing then the observed results here could simply be due to that, rather than any interpreted changes at the endosome.

7) The Authors claim “In addition to highlighting the neuronal roles of WASH in CCC- and Retriever mediated endosomal sorting, our proteomics approach also identified protein modules 21 with increased abundance in SWIP P1019R mutant brain.” This is very confusing as the protein abundance change are not shown, what is known is that the more of the proteins is likely to be associated with a complex, but not the overall abundance of the complex components in the cell. These arguments persist throughout the Discussion section. If the authors take only a proportion of each fraction and this is not consistent across fractions or WT and MUT, then they do not know what the total abundance changes are.

B) Lack of important controls- the authors need to experimentally address these concerns.

Reviewer 1

1) The authors should confirm that the endosomal enriched fraction is the same in both WT and mutation experiments.

Reviewer 2

1) In their proteome data, the authors argue that 37 out of 255 modules exhibit significant differences in WT and MUT brains. These data indicates that in addition to endo-lysosomal modules, many other pathways are also affected in the MUT brains. These include endoplasmic reticulum (ER) module (M83), synaptic modules (M35 and M248) and many others that the authors did not specify…did the authors observe any defects in other organelles or cellular compartments, such as ER, mitochondria, synapse…etc?

2) Finally, in their TEM images in Figure 5, the authors argue that the electrical-dense inclusions in the cell bodies of MUT neurons are "visually" consistent with lipofusine accumulation. The authors need to use biochemical or histological methods to prove their point. This will significantly strengthen their arguments.

Reviewer 3

1) It would be beneficial if the authors could do some IPs with the WT and mutant SWIP vectors to validate the proteomic data

C) Concerns about their statistical methods and data analysis that needed to be addressed.

Reviewer 1

1) The analysis method used was chosen as previous approaches to deal with spatial proteomics data in the literature make use of well curated organelle markers. The authors claim that they did not have access to a robust set of marker lists, but other studies have used mouse neuronal cell lines (Itzhak DN et al., 2017) and also mouse ES cells (Christoforou. A et al., Nature Commun. 2016). These lists could easily have been adapted and used to visualize organelle separation using straightforward approaches such as PCA.

2) The analysis of the (spatial) proteomics data is currently not clear and there is some confusion. Firstly, edgeR was originally developed to handle RNA-sequencing data, not scRNA-sequencing data. Furthermore, RNA-sequencing data are indeed interpreted as counts and a negative binomial distribution is appropriate. This is not the case for proteomics data, as an integral under the isotopic envelope is involved in computing the intensity. Thus the analysis is not appropriate for the task. LIMMA, DEP, MSqRob, DeqMS, MSstatsTMT would all be appropriate methods.

3) The GLM framework for differential protein abundance between modules is not quite clear and the analysis is not quite correct. Instead of summarizing a module as the sum of the proteins, linear models should be fit on the data directly with a global module term and a factor for each protein. The protein factor will probably need to be encoded as a random effect. Lme4 and gam packages in R should be able to do this analysis. This section would gain a lot of clarity from some more precise descriptions.

4) From the figure it looks like the spatial proteomics data was normalized so that the max intensity in the most intense fraction is 1 – is that the case? Usually spatial proteomics data are normalized so that protein intensity sums to 1 across the fraction. I also find all the normalization and filtering for the TMT analysis quite confusing – a table might help with the desired effect in a column. Why did the authors not summarize peptides to proteins via the median or sum and then normalize so that proteins sum to 1 across the fractions?

5) There are no plots of the finally normalized spatial proteomics data to see whether the experiment was successful or not.

D) Overstated conclusions- the authors should tune down their argument or provide more data as suggested to support their conclusions.

Reviewer 1

1) The connection with human findings is a bit overstated. The findings suggest that the clinical phenotypes between humans and mice are similar. However, the mechanistic insights are only shown in mouse models. The text is slightly overstated and the mechanistic insights in humans should be toned down.

Reviewer 2

1) In their proteome data, the authors argue that 37 out of 255 modules exhibit significant differences in WT and MUT brains. These data indicates that in addition to endo-lysosomal modules, many other pathways are also affected in the MUT brains. These include endoplasmic reticulum (ER) module (M83), synaptic modules (M35 and M248) and many others that the authors did not specify. A major concern is that whether the endo-lysosomal dysfunction is the only factor that contributes to the behavioral defects? A rescue experiment can solve most of this concern. It has been shown recently the R33, a retromer chaperone, can strengthen retromer function and improves memory in a mouse model of AD (PMID: 31964406). The authors can consider testing this drug in their model.

Reviewer 3

1) The authors suggest that the WASH complex may not interact as closely with retromer as it does in other cells. This is a bold statement to make based on BioID and given the existing literature associated with the retromer-WASH axis. For example, the VPS35-D620N disruption of binding to FAM21. Could the authors expand on this? Is it possible that the retromer complex is not present in the proximity-based proteomics due to the use of WASHC1?

E) The authors need to comment on the following two suggestions.

Reviewer 3

1) Could the authors expand more on their result showing that many of the lysosomal protein interactors are enriched in the SWIP mutant condition compared to the WT when many of these proteins have been shown to be lost in neurodegenerative disease? Do the authors think that if they looked at longer aged animal they would see a drop as the lysosomes become impaired and that their model is looking at how the cells try to compensate for the endosomal dysfunction (ie early stages of neurodegeneration)?

2) It is interesting that the SWIP(P1019R) mutant mice exhibit such significant progressive motor deficits. The authors found no difference in the cleaved caspase 3 staining in the striatum but did they look at whether there was a loss of dopaminergic neurons in the substantia nigra pars compacta (or a loss of dopaminergic innervation or dopamine levels in the striatum) to account for these motor deficits? I would expect there to be a drastic loss of dopamine due to the significant motor deficits shown. Interestingly, SNCA is also present as an interactor of the WASHC1. Could the authors expand on whether they think α synuclein could therefore, also be playing a role (particularly as the authors also suggest an elevation of ER stress modulators in the SWIP mutant mice proteomics?)

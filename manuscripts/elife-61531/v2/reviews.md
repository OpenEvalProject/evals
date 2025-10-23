# Peer review - Round 1

Editors:
- Jeremy J Day, University of Alabama at Birmingham United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61531.sa1](https://doi.org/10.7554/eLife.61531.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript identifies a novel mechanism linking loss of Transformation/transcription domain-associated protein (TRRAP) to neurodegeneration and motor deficits in a mouse model. Overall, the compelling results highlight a regulatory pathway by which TRRAP, the transcription factor SP1, and histone acetylation interact to control expression of key microtubule associated genes, resulting in destabilized microtubule dynamics when TRRAP is deleted. Given the ties between TRRAP mutation and several human neuropathies, these findings have implications for uncovering novel disease mechanisms.

Decision letter after peer review:

Thank you for submitting your article "TRRAP-HAT modulates microtubule dynamics via SP1 signaling in brain homeostasis and neurodegeneration" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Huda Zoghbi as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This manuscript from Tapias, Larazo, et al., examines effects of neuronal deletion of the transformation/transcription domain associated protein (Trrap) gene. The authors show that Trrap deletion in Purkinje neurons of the cerebellum causes neurite retraction, progressive cell loss, and age-related motor control deficits. Similarly, deletion of Trrap in the cortex and striatum (using the forebrain-selective Camk2a promoter) results in widespread transcriptional dysregulation, specifically at genes containing SP1 transcription factor motifs. Consistent with SP1-mediated deficits in gene expression, Trrap deletion decreased SP1 activity at a luciferase reporter, and decreased SP1 binding and histone acetylation at Trrap target genes Stmn3 and Stmn4. Similar gene expression changes were observed after conditional Trrap deletion in neural stem cells. Finally, the authors report that overexpression of Trrap target genes Stmn3 and Stmn4 rescues effects of Trrap knockdown on neurite branching and length in primary cultured neurons.

Overall, the results identify a novel mechanism by which Trrap regulates neuronal function, and might contribute to neuronal development and potentially also neurodegeneration. Additionally, these results may have relevance to Trrap mutations in human patients.

While the results identify a potentially novel link between Trrap, SP1, and microtubule dynamics that support neruonal growth and function, the reviewers had several concerns with the current manuscript. First, the evidence that SP1 and histone acetylation mediates the effects of Trrap deletion is not sufficient to fully support the claims of the manuscript. Second, while the examination of different cell types is helpful and increases the ability to generalize effects of Trrap deletion, there are significant concerns about the timing of Trrap deletion in these models, and several of the results are not consistent with a neurodegenerative phenotype. We have suggested the following revisions to improve the manuscript.

Essential revisions:

1) The data presented in Figure 3G are intriguing, and are the main data in the paper to support a direct mechanistic link between Trrap and SP1 function. However, these results are based on a relatively underpowered experiment (n=3), with large error. The manuscript would be improved if this could be strengthened or bolstered by additional evidence. For example, the manuscript already contains H3ac and H4ac ChIP-seq data, which is used to infer effects mediated by SP1 at Trrap target genes. The authors might confirm this relationship by looking at the distribution of histone acetylation across SP1 sites in the genome (as well as specifically at Trrap DEGs). Similarly, it would be useful to show that Trrap is normally found at SP1 motifs for these genes in neurons (e.g. with ChIP). Likewise, although the ChIP data suggest that SP1 regulates STMN3 and 4 expression, this is not directly demonstrated. Does SP1 depletion alone influence their expression?

2) The authors argue that neurodegeneration linked with Trrap deletion is the result of altered transcription of SP1 targets through impaired SP1 activity caused by reduced acetylation. However, the overlap between hypoacetylated loci and SP1-regulated genes on a genome-wide scale was pretty low (subsection “Trrap-HAT mediates Sp1 transcriptional control of microtubule dynamic genes”, 11 genes), indicating that other factors may be at play. The authors validate their assertion by showing that Sp1 and AcH4 are reduced by Trrap deletion on target promoters (Figure 4E and F), but this study is lacking proper controls to show that these changes are selective for acetylation. Given that the authors argue that the effect is mediated by HAT activity (which is not measured but inferred based on known Trrap functions), it is important to exclude alternative explanations, such as non-specific effects of Trrap deletion on nucleosome density or other post-translational modifications. As such, studies in Figure 4D should be repeated for total H4 and also for another PTM that isn't directly regulated by Trrap. In addition, to validate the relevance of SP1 as a regulator of genes affected by Trrap function, an additional control would be beneficial – specifically, the authors could conduct ChIP for a TF that was not associated with genes affected by Trrap deletion in Figure 3F to show that changes in Figure 4F are specific for SP1 and acetylation.

3) The authors link SP1 with impaired microtubule function. They show microtubule-related terms in ontology analysis of differentially regulated genes that overlap in the striatum and the cortex, but not specifically for DEGs that contain SP1 binding sites. Although they do identify STMN3 and 4 as targets, it would be useful to see if these categories come out for SP1 regulated genes as a group. As authors point out, SP1 tends to have wide spread functions that influence many pathways, so it is important to exclude the possibility that microtubule-related functions affected by Trrap may be small compared to other pathways that are influenced more dramatically. Even if they are small, this finding is still of interest, but the conclusions need to be dampened.

4) While the manuscript claims that TRRAP-HAT modulates microtubule dynamics via SP1 signaling in brain homeostasis and neurodegeneration, the evidence for these assertions is relatively weak. The signaling pathway the authors found is based on the RNA-seq and ChIP-seq in the forebrain at P10 when postnatal brain development and maturation is still going on. Also, the role of TRRAP-HAT-SP1-STMN3/4 signaling in the neurodegeneration context is not validated since the cortical primary culture at DIV6-12 is also at developmental stage rather than fully matured stage. Therefore, while the manuscript begins with Purkinje neuronal degeneration by Trrap deletion, data in Figure 3 shows that the signaling pathway is more likely to be involved in the neural development. Similarly, the authors did not carefully confirm the effect of Trrap deletion on Purkinje neuronal development. In the PCP2-Cre line the authors used in this study, Cre expression starts at P6 (Zhang et al., 2004). Considering the cerebellum and Purkinje neuronal development is completed around at ~P20, it is difficult to exclude the possibility TRRAP-HAT-SP1-STMN3/4 signaling affect the Purkinje neuronal development rather than neuronal survival. Indeed, previous study showed that STMN3 is crucial for the formation and development of the Purkinje cell dendritic arbor (Poulain et al., 2008). These issues should be addressed in the manuscript, and if the authors cannot rule out neurodvelopmental effects, the specific claims regarding neurodegeneration should be removed.

5) The primary interest appears to be in investigating the role of Trrap in cerebellar neurodegeneration, and as such, they quantify phenotypes that are relevant to cerebellar function. However, mechanistic studies are conducted in the striatum and cortex. The argument for switching mouse models and brain regions was the scarcity of Purkinje cells in the Trrap-PC model, so they switch to CamKIIa Cre and striatum and cortex for mechanism. A search of the literature and Allen Brain atlas shows CamK2a expression in cerebellar cells, including Purkinje cells. Since there was no cell sorting performed to select for CamK2a cells in any of the brain regions examined, the experiments would presumably be able to be conducted in the cerebellum? Similarly, the authors use multiple cell types in cell culture studies, including cultured cortical neurons – why not use cultured cerebellar neurons?

6) Please clarify how the ChIP datasets in Figure 4E-F are compared between groups. Why is there no variability in the control group? For ChIP-qPCR data, it would be preferable to show the results as % of input, rather than binding enrichment. Additionally, while the sequences for ChIP-qPCR primers are provided, the authors should clarify where these primers target within the genome, and whether site contains a known SP1 motif.

7) The data showing siRNA-mediated Trrap knockdown (Figure 5—figure supplement 1A) is not convincing – summary data and statistical comparisons should be shown for manipulations as performed in the in vitro experiments. Similarly, it is not clear how transfection experiments would lead to robust knockdown. Typically, neuronal transfection experiments suffer from a very low efficiency, meaning that manipulations would only occur in a very small fraction of cells. If this is not the case here, data for transfection efficiency should be provided.

8) The Title of the manuscript should be revised to meet eLife guidelines. Specifically, the Title should avoid use of dashes, acronyms, or unfamiliar abbreviations (unless needed for scientific reasons). Please revise your Title with this advice in mind. Additionally, the Title and/or Abstract should provide a clear indication of the biological system under investigation (i.e., species name or broader taxonomic group, if appropriate). Please revise your Title and/or Abstract with this advice in mind.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "HAT cofactor TRRAP modulates microtubule dynamics via SP1 signaling in neurodegeneration" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Huda Zoghbi as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Hongjun Song (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our policy on revisions we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

In original manuscript, the authors identified a novel mechanism by which Trrap regulates neuronal function, with implications for neurodegeneration. Specifically, they show that loss of TRRAP results in neurite retraction, neurodegeneration, and motor deficits. They link these changes with activity of the transcription factor SP1 and with two downstream targets, Stmn3 and Stmn4, which are implicated in microtubule dynamics. Overall, these data present a novel regulatory pathway in regulating microtubule dynamics and provide a basis for uncovering the role of specific epigenetic factors in this process. Given the ties between TRRAP and several human conditions affecting neural conditions, these findings have implications for uncovering novel disease mechanisms.

In this revised manuscript, the authors made significant efforts to address all the concerns raised by previous reviews with new experiment, data re-analyses, and clarification in the text. The manuscript is significantly improved, and the new results support the author's interpretation that Trrap deletion alters SP1 binding and expression of STMN3 and STMN4. Notably, overexpression of STNM3 can rescue certain neurite growth deficits caused by Trrap deletion, in agreement with their model. Likewise, many conclusions have been appropriately toned down to match the experimental results or in light of noted caveats. However, some specific revisions are still critical prior to publication of the manuscript (outlined below).

Essential revisions:

1) Replace all figures with higher resolution images – the current versions appear pixelated upon zooming in to see details. Vector images are preferred where possible.

2) In relation to comment 4: Conclusions regarding neurodegeneration are still too strong and the answer provided in response to the reviewers is not fully reflected in the discussion of the revised manuscript.

3) The authors still do not address the lack of variability in control groups in several figures, including:

-Figure 4B – from blot images in Figure 4A, there seems to be sample variability in controls, but the individual data points look exactly the same. The same applies to Figure 5 – figure supplement 1A.

-Individual data points are shown for some graphs, but not for others. Individual data points should be included for all graphs.

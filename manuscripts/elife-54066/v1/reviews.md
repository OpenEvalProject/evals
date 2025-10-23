# Peer review - Round 1

Editors:
- Lynne-Marie Postovit, University of Alberta Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54066.sa1](https://doi.org/10.7554/eLife.54066.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper demonstrates a beautiful methodology for tracking tumour formation within 3D acinar structures, with single cell resolution. It also suggests that tumour formation may depend upon local interactions between transformed cells. The method described may be used to better understand the underpinnings of stochastic tumor evolution.

Decision letter after peer review:

Thank you for submitting your article "Tracking cells in a novel organoid model by light sheet microscopy reveals proximity effects in breast cancer initiation" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Richard White as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Anne Rios (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript by Jechlinger and colleagues combines a novel transgenic organoid model of breast hyperplasia with light-sheet microscopy in order to demonstrate that hyperplastic outgrowths occur most readily when transformed cells are adjacent to each other. Specifically, the authors compared early progression (hyperplastic growth and depolarization) in organoids wherein all versus only a subset of epithelial cells harbor the Neu and MYC driver mutations. Aided by time lapsed light-sheet microscopy and computational analyses, they surmised that the number of transduced cells in a cluster dictates progression, suggesting that special cues are likely required for cancer progression to occur. This work was reviewed by 2 experts and myself. One of the reviewers was notably an expert in the imaging and characterization of organoids, and thus able to comment on the technical aspects of this study, which given its focus, are the most important.

Overall, the reviewers felt that the paper describes an interesting tool that is accompanied by beautiful images and a fairly compelling analysis. However, in order to better justify the biological conclusions, additional experiments would be needed. These would include an analysis of cells which outgrow (versus those that do not). Such studies may include single cell RNA sequencing to determine how cells in clusters differ from those which are more isolated, as well as a more thorough assessment of polarity and consideration of microenvironmental cues such the concentration of myo-epithelial signals. Hence, the main issues raised by the reviewers related to the claims that a distinct number of initiator cells can explain tumorigenic clone expansion and that a proximity-controlled interaction or signaling network between different transformed cells is required for tumor outgrowth in a normal epithelium. In order to substantiate these claims, a number of experiments would have to be done. I would suggest, rather, that the claims are tempered and that the suggested technical revisions are completed.

Essential revisions:

1) Heterogeneities associated with the growth of organoids in general should be considered with additional controls: The authors cannot claim that you need interaction/cooperation between different transformed cells when the “organoid” with few activated cells clearly show an overall growth slower or even non-existent compare to the one with expansion of tumorigenic clones (organoid size, cell compactness). Differences of growth and growth advantage for some “organoids” while culturing is quite common. The authors should think of a comparison of growth dynamics of untransduced tissue and provide the initial volume in both conditions as well as assess the impact of proliferation differences between different organoids.

2) The idea that the initial cluster size dictates tumor formation should be better supported: If indeed tumor formation is dependent on the initial cluster size, this effect should also be detectable at single organoid level: A single organoid should have clusters formed by several cells that will give rise to a tumor and clusters formed by only 1 cell that will not give rise to a tumor. The authors should define such examples, and fit a model with random effect, where each organoid will be considered as random effect. This could as well exclude the possibility that the results are due to the fact that organoids have a differential growth capacity.

3) The AI approach should be strengthened and/or better articulated: In the logistic regression model used to assess which feature is responsible for the tumor formation, authors should include interaction effects between different features, which is not considered by the linear model used. As indeed the size of the organoids could influence the number of cells per cluster, etc.

4) The conclusions must be either softened or expanded upon (with experiments such as those outlined in the summary): Considering that the conclusion of the authors would be correct and that the tumor formation is solely dependent on the cluster size, please provide an explanation why is it independent of the interactions between cells of the same cluster. It would be logical to assume that cells have to be in close contact to exert an effect on each other.

5) The semantics regarding "organoids" should be addressed: The authors call “organoids”, the in vitro 3D culture they use. Not all 3D spheroids culture can be called “organoids”, it is essential first to examine if the 3D structures grown in culture resemble the original breast tissue (e.g. cell composition, geometry). Why not use the well-defined protocol developed for mouse organoid culturing where both main mammary epithelial cell types can be modelled (luminal and myoepithelial) (Jamieson, Dekkers et al., 2016)? The authors should either prove that their cultures can be called organoids or use the right protocol. It is of great importance as they are claiming they use a stochastic model. Looking at shape and polarity, I presume their organoids are luminal-enriched.

6) Studies regarding polarity should be strengthened: 3D z-stack and rendering should have been performed to make conclusive interpretation in Figure 2A about disrupted polarity and random lumen. 2D often lead to a wrong interpretation of architectural phenotypes. Moreover, the authors should expand the polarity analyses by measuring a number of polarity markers (ZO-1, Par3).

7) The authors should refine terminology related to localized transformation and/or perform the experiments that would allow them to suggest that transformation is in fact localized: The authors also claimed a model of localized transformation while what they did is random and low rate transformation using a doxycycline inducible model with lentiviral delivery of rtTA. It is a confusing claim as localized transformation implies you control the location. This can be performed with optogenetic technology. Alternatively, the terminology used should be refined.

8) Please ensure the supplementary figures are uploaded.

9) The authors should not suggest that a big-data analysis was conducted and/or should apply more robust analytical techniques: Authors claim that they do big-data analysis, however only 20 organoids are segmented and tracked. The authors should either provide a more robust analysis or change the semantics that are used in the paper.

Reviewer #1:

This manuscript by Jechlinger and colleagues combines a novel transgenic organoid model of breast hyperplasia with light-sheet microscopy in order to demonstrate that hyperplastic outgrowths occur most readily when transformed cells are adjacent to each other. Specifically, the authors compared early progression (hyperplastic growth and depolarization) in organoids wherein all versus only a subset of epithelial cells harbor the Neu and MYC driver mutations. Aided by time lapsed light-sheet microscopy and computational analyses, they determined that the number of transduced cells in a cluster dictates progression, suggesting that special cues are likely required for cancer progression to occur. Overall, this is an interesting tool, accompanied by beautiful images and a fairly compelling analysis. However, in order to solidify what is still mostly a descriptive finding, an analysis of cells which outgrow (versus those that do not) would be needed.

As indicated by the authors, single cell RNA sequencing should be done to determine how cells in clusters differ from those which are more isolated. Alternatively, key factors may be analyzed perhaps with IHC, to determine if there are tangible differences.

Reviewer #2:

This is an interesting paper using real time imaging and a retroviral based strategy to induce both the MYC/activated Neu in single cell. The core observation is that clusters of oncogenes expressing mammary epithelial cells go on to form tumors whereas single cell isolates do not. The authors conclude that adjacent normal cells (untransduced cells) negatively inhibit tumor outgrowth. In general, the data presented support the author's conclusions. However, the authors should address the following issues before publication.

1) Although the data indicate that single cell expressing both oncogenes have normal polarity, using a number of polarity markers (ZO-1, Par3) can the authors exclude subtle alterations in polarity program.

2) What impact would co-cultivation of myoepithelial cells have on the observed tumor dynamics.

Reviewer #3:

Alladin et al. proposed a stochastic breast tumor doxycycline inducible system using mouse breast 3D cultures to establish lower cell transformation rate. They performed lightsheet time-lapse imaging together with tracking analysis to examine clone expansion overtime after transformation. The authors claimed that distinct number of initiator cells can explain tumorigenic clone expansion. In addition, they suggest that a proximity-controlled interaction or signaling network between different transformed cells is required for tumor outgrowth in a normal epithelium. I have serious concerns about this claim and even if the claim is correct, the paper does not provide any explanation for such a phenomenon. Please see my comments below, I hope it may help improve your manuscript.

– The authors cannot claim that you need interaction/cooperation between different transformed cells when the “organoid” with few activated cells clearly show an overall growth slower or even inexistent compare to the one with expansion of tumorigenic clones (organoid size, cell compactness). Differences of growth and growth advantage for some “organoids” while culturing is quite common. The authors should think of a comparison of growth dynamics of untransduced tissue and provide the initial volume in both conditions as well as assess the impact of proliferation differences between different organoids.

– If indeed tumor formation is dependent on the initial cluster size, this effect should also be detectable at single organoid level: A single organoid should have clusters formed by several cells that will give rise to a tumor and clusters formed by only 1 cell that will not give rise to a tumor. The authors should define such examples, and fit a model with random effect, where each organoid will be considered as random effect. This could as well exclude the possibility that the results are due to the fact that organoids have a differential growth capacity.

– In the logistic regression model used to assess which feature is responsible for the tumor formation, authors should include interaction effects between different features, which is not considered by the linear model used. As indeed the size of the organoids could influence the number of cells per cluster, etc.

– Considering that the conclusion of the authors would be correct and that the tumor formation is solely dependent on the cluster size, please provide an explanation why is it independent of the interactions between cells of the same cluster. It would be logical to assume that cells have to be in close contact to exert an effect on each other.

– The author call “organoids”, the in vitro 3D culture they use. Not all 3D spheroids culture can be called “organoids”, it is essential first to examine if the 3D structures grown in culture resemble the original breast tissue (e.g. cell composition, geometry). Why not use the well-defined protocol developed for mouse organoid culturing where both main mammary epithelial cell types can be modelled (luminal and myoepithelial) (Jamieson, Dekkers et al., 2016)? The authors should either prove that their cultures can be called organoids or use the right protocol. It is of great importance as they are claiming they use a stochastic model. Looking at shape and polarity, I presume their organoids are luminal-enriched.

– 3D z-stack and rendering should have been performed to make conclusive interpretation in Figure 2A about disrupted polarity and random lumen. 2D often lead to a wrong interpretation of architectural phenotypes.

– The authors also claimed a model of localized transformation while what they did is random and low rate transformation using a doxycycline inducible model with lentiviral delivery of rtTA. It is rather confusing claim as localized transformation implies you control the location. This can be performed with optogenetic technology.

– Important to mention: No supplementary figures were uploaded.

– Authors claim that they do big-data analysis, however only 20 organoids are segmented and tracked, this is misleading. The authors should either provide a more robust analysis or change the semantics that are used in the paper. Also, few terabytes per organoid imaged…I may advise to consider other imaging technologies such as confocal that will give better images for less data generated.

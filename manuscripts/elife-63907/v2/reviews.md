# Peer review - Round 1

Editors:
- Claude Desplan, New York University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63907.sa1](https://doi.org/10.7554/eLife.63907.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Your paper profiling the large diversity of chick retinal neurons taking advantage of single-cell mRNA sequencing is novel and exciting and this dataset published in eLife will be an important resource for retina scientists. Furthermore, the comparison with the mouse retina is of great interest and the variation among the retinal ganglion cells might represent a fundamental process by which species adapt to their visual environment.

Decision letter after peer review:

Thank you for submitting your article "Single cell profiling identifies 136 cell types in the chick retina" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Marianne Bronner as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tom Baden (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

The three reviewers found your paper novel and exciting and they are anxious to see it published in eLife as this will be an important resource for the field. Furthermore, the comparison with the mouse retina is of great interest and the variation among the retinal ganglion cells might represent a fundamental process by which species adapt to their visual environment.

However, there are a few points that you will need to address before the paper can be published, most of which should only require editorial work or bioinformatic processing.

– Present a much better description of the technical processing the scRNA seq data.

– Address the question of cell type: All reviewers feel that you have not demonstrated that you have identified 136 cell types as several could be cell states. One way to address this would be to add a pseudotime analysis to make sure that the “cell types” are not different cell states.

– The cell types that differ between species might be due to the very different stages of development of the various retinas. Showing a UMAP of all ages aggregated together would address this point.

– You should also fix the referencing to other papers that appears to be lacking.

We will be expecting a revised version soon and the field will then be able to enjoy these results.

Reviewer #1:

The manuscript "Single cell profiling identifies 136 cell types in the chick retina" by Yamagata and colleagues represents a new transcriptomic atlas of the chicken retina. It explores the diversity of cell types in the avian retina, describing the functional significance of this vast diversity in terms of cell morphology, connections and spatial organization within the retina. Using a CRISPR-based assay, they show the position of the various cell types and their corresponding morphologies. Finally, the authors describe the regionalization of specific populations of glial cells in their respective identities. Overall this manuscript is an extensive documentation combining in silico exploration with in vivo validations. It is an impressive resource that will be extremely valuable to the field. While the experimental design of the study is correct and in general the data appears technically rigorous, the Results section lacks clarity in the way the data are presented, and more importantly, it does not provide sufficient information on the methods and the parameters used for the single-cell analysis. Altogether their findings appear convincing and provide an impressive resource on which the community will be able to generate new hypotheses in the field.

1) The central point that is made by the authors regards the number of cell types in the avian retina. Based on previous reports in other species, this number may be expected. But how much of the diversity one can observe in amacrine and bipolar cells is related to the transitional states of the same cell type? Also, the authors mention 10 clearly immature clusters: could these correspond to CMZ-derived or CMZ cells? Finally, even if the retina at E18 is histologically mature, some of the cells in mature clusters may be closer to full maturation than others, in particular when it comes to synapse refinement and pruning. Was this taken into account? A first step into this investigation would be to rank the cells with pseudotime alignment method (such as Monocle).

2) To what extent is the number of cell types related to i) the number of single-cells sequenced (have you controlled whether you are close to saturation?) ii) the stages used to evaluate them (E12-E18) and iii) the clustering technique (this latter was difficult to assess due to insufficient description) ?

3) Why is there no dimensionality reduction visualization of the main dataset? We see these cells aggregated with other species only in Figure 10, but nowhere can we appreciate the distinction between the main classes. Thus, it is hard to assess to what extent these classes are distinct.

4) The manuscript, presented as a resource, occasionally lacks clarity in its presentation, especially in the first pages of the Results section (Figures 1 and 2).

5) The main concern is the lack of detail in the Materials and methods section, in particular on the single-cell analysis (QCs, etc). The clustering appears to be correct, but it would be valuable to add how filtering and hierarchical clustering were performed. Also, a clarification of the rationale for the maximisation procedure used to distinguish cell types would be useful. Same for the thresholds used.

6) Regarding the data availability, the link provided does not work:

"https://singlecell.broadinstitute.org/single_cell/study/SCP1159"

7) The Introduction and Discussion are well written but poorly referenced, especially when it comes to the multi-species comparison. As this study adds to an increasing body of work on single-cell retina, it seems important to refer to the previous work (unless the number of references is limited?).

Reviewer #2:

In their manuscript "Single cell profiling identifies 136 cell types in the chick retina", Yamagata, Yan and Sanes present the first transcriptomic atlas of an avian retina. The manuscript delivers pretty much what it says on the tin: a (probably almost) complete parts-list of the chicken retina, with 6 photoreceptor types, 4 HCs, >20 BCs, >40 RGCs and close to 60 ACs – alongside Muller glia. Each of these comes with a hit-list of molecular markers than could be used to genetically target them in the future, and some are in fact confirmed in the study using their novel eCHIKIN approach.

Beyond this, the authors also compare their results from chicken to their previous results from mouse as well as species of primate including humans and find interesting links between cell classes and types. Overall, their results confirm several long-held notions, for example that avian retinas are among the more complex ones out there, that retinal cell homology works incredibly well on the retinal input side (especially HCs seem to be amazingly conserved!), while this works less well on the RGC side – possibly hinting that evolution will more readily tweak the retinal output than the input?

Finally, the work is technically excellent, the manuscript is written clearly and succinctly, and referencing is adequate.

Overall, there is a lot to like, and really nothing to dislike. As a lab that is actively investigating vision in chicks (and other species), I can attest first-hand that this dataset is incredibly useful and interesting, and I enthusiastically support publication in eLife.

Reviewer #3:

In this descriptive study the authors use scRNA-Seq to profile ~40,000 cells from the embryonic chick retina and compare them to similar datasets generated from mouse, human, and macaque. As the authors point out, the chick retina is a long-used model for retinal development and recently another paper described scRNA-Seq on the chick retina in the context of multi-species functional studies of retinal regeneration (Hoang et al., 2020). An additional study (Tegla et al., 2020) also performed scRNA-Seq of the chick retina to probe the function of developmental transcriptional programs. The field does not however have a well-documented single cell atlas of the chick retina. This current study represents such a resource that will be an important reference for the field moving forward.

1) Throughout the paper the authors associate the concept of single-cell cluster with the concept of cell type. Given that the number and size of clusters can be dynamically changed depending on analysis parameters, I would strongly recommend that the authors avoid using the term "cell type", except where this is well supported experimentally (e.g. by demonstration of a cell-mosaic arrangement of marker expression). This term is especially misleading in the title, which might more accurately be "a single cell atlas of the developing chick retina".

2) The description of the scRNA-seq analyses is really insufficient to permit replication or in some cases interpretation of the data. The authors need to give more details with regard to the specific parameters used for each analysis.

3) The authors should provide additional evidence that comparing cell classes and types between the embryonic chick retina to that of the more mature mammalian retinas is experimentally justified. Could it be that they are seeing a greater diversity of cell types in the chick retina because they are considering a greater diversity of transitional states? These multi-species comparisons would be greatly strengthened by addition of a dataset from the mature chicken retina.

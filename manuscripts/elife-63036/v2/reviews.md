# Peer review - Round 1

Editors:
- Mani Ramaswami, Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63036.sa1](https://doi.org/10.7554/eLife.63036.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The work describes a novel and robust method to determine differentially expressed genes in specific classes of Drosophila olfactory sensory neurons (OSNs) using the Targeted DamID technique. This is valuable as it provides an approach that can be used to profile transcriptions in cell types in the antenna that are difficult to isolate and purify. Through such an analysis and additional experiments to determine the function of some OSN-specific mRNAs, this study not only provides an important resource for the OSN field (especially for Drosophila and mosquito researchers) but also provides mechanistic insight into the determination of specific OSN classes, and how they are segregated into specific glomeruli.

Decision letter after peer review:

Thank you for submitting your article "Targeted molecular profiling of rare cell populations identifies olfactory sensory neuron fate and wiring determinants" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Utpal Banerjee as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tony D Southall (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

Arguello et al. report comprehensive transcriptional (and chromatin accessibility states) profiles for individual classes of Drosophila olfactory sensory neurons (OSNs), uncovered using the Targeted DamID technology. Seven individual IR-expressing OSN classes (Ir64a, Ir31a, Ir75a, Ir75b, Ir75c and Ir84a) were profiled by using IR-specific GAL4 drivers to control the expression of Dam (CATaDa) or Dam:Pol II (TaDa) which indicate chromatin accessibility and RNA polymerase II occupancy respectively. The data correlates well with what is already known about these OSNs and complement two other studies in Current biology and in BioRxiv, which use single-cell RNAseq to profile mRNA expression in individual OSNs. They describe differentially expressed transcription factors and cell surface molecules and follow up nicely with a functional analysis of the transcription factor pdm3, which is expressed specifically in Ir75a OSNs and the cell adhesion molecule fmi, expressed in most Ir expressing OSNs except for Ir75a and Ir84a. These studies show developmental functions consistent with their differential expression (documented in adults): most interesting that mutations in fmi are associated with disruption of glomerular organization for all coeloconic OSNs.

Overall, the study is of high technical quality and will be appreciated by a broad audience for its technical breakthrough and available datasets. Not only does this study provide an important resource for the OSN field (especially for Drosophila and mosquito researchers) but also provides mechanistic insight into the determination of specific OSN classes, and how they are segregated into specific glomeruli. Also, the successful application of Targeted DamID, in this context, emphasises its effectiveness for profiling small and difficult to access populations of cells in vivo.

There are however, several points that should addressed before publication.

Essential revisions:

Readers would benefit from detailed comparisons of the data presented here with adult OSN single cell profiling data from the Luo lab (McLaughlin et al., 2020) and a previous study published in Current Biology early 2020. While carefully comparing and contrasting these results with the Luo preprint, the authors should acknowledge and discuss inconsistencies such as expression of odorant binding proteins, which are presented as originating from support cells of olfactory sensilla (in this study) versus some being expressed by OSNs (McLaughlin et al. study). Also, the Discussion needs to be modified as the scRNAseq seems to be feasible for adult OSNs (McLaughlin et al. study).

The focus on Pdm3 and Fmi in the last part of the manuscript (Figures 5-7) does address the functional significance of their continued, heterogeneous expression in adult OSNs. Attempts to knockdown the expression of these genes in adult OSNs failed to yield significant phenotypes. In fact, the observed cell fate or wiring phenotypes require knocking down the genes in all OSNs at much earlier developmental stages (using peb-GAL4) than the time points when the datasets were generated. The Results and Discussion sections should be revised to clearly acknowledge that these experiments, though well designed and executed, do not connect to the TaDa datasets which pertain to adult expression (see also points 9 and 10). That said, the study is strong and interesting enough even with the first five figures.

The authors may consider revising the title to eliminate the focus on neuron fate and wiring given that the TaDa datasets are generated from adult OSNs but there is no obvious phenotype when knocking down Pdm3 and Fmi in adult OSNs.

Figure 1D and E: The DamID plots in Figure 1D and E look strange – why are there sloped boxes representing the data? Is this due to it representing the sequencing reads rather that the binned average per GATC fragment? Ideally, DamID data should only be displayed as the binned signal per GATC fragment (the regions between GATC sites), as this is the maximum resolution of the system.

It is not clear from the figure legend (Figure 1D and E) whether the read depth is normalised, and if so, how it was normalised.

The approximate positions of the GATC sites (would be good if they were exact) do not appear to always align with the distinct boundaries within the data, which would be at GATC sites.

Are there signature genes for each OSN class profiled other than the IRs themselves? Can these genes be statistically identified and provided as a list?

Figure 1—figure supplement 1 – it is very difficult to read the receptor names. Can the panels be rearranged (maybe by making the columns narrower), so that the receptor names are larger? How do the authors reconcile expression of ORs and GRs to be expressed in adult OSNs? One explanation by the authors is that these sensory receptor genes reside within introns or genomic regions that also have other genes known to express in neurons. Can the authors do an in situ hybridization to confirm that indeed some OR/GR genes are co-expressed with IRs?

Looking at the fmi mutant phenotype it seems like mostly the effect starts at 24 hours with defasciculated axons around future antennal lobe. A discussion of this should be added to the Discussion. Can the authors provide more discussion on how they envision Fmi working to regulate OSN projections in the antennal lobes?

It also seems like many of the OSNs analyzed in the coeloconic sensilla seem to have a defect. How do the authors reconcile this with the differential expression of fmi in IR expressing OSNs? It seems like the wiring of Ir84a and Ir75a OSNs also look affected even though they do not express fmi? is this non-autonomous? We note that reverse MARCM using regular fmi alleles could answer this. Or if RNAi needs to be used maybe a gal4 that is expressed early in Ir84a OSNs? In any event, this should be acknowledged as an issue remaining to be resolved.

Subsection “Targeted DamID of OSN populations”, the finding of low RNA PolymeraseII occupancy upstream of Ir93a versus high protein expression: Maybe a mention of TaDa not as effective for profiling low abundance gene expression?

In Figure 6E, it seems like early and wide spread knock down of pdm3 results in Ir75a OSNs to be converted to Ir75b OSNs, which leads to an increased glomerular volume targeted by Ir75b OSNs. What happens to projection patterns in the experiment presented in 6G where RNAi knock down of pdm3 is driven by Ir8aGAL4, which leads to OSNs that co-express Ir75a and Ir75b?

The representation of the CATaDa data in Figure 3 gives a false impression of the resolution of the data – it should be binned per GATC fragment.

Figure 5B – it would be good to see some statistical tests for these data.

Materials and methods (“TaDa sample preparation”): Should indicate the sex of the experimental flies.

# Peer review - Round 1

Editors:
- Genevieve Konopka, University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59928.sa1](https://doi.org/10.7554/eLife.59928.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Defining and naming brain cell types has been a long-standing challenge in neuroscience. New high-throughput techniques have facilitated the generation of many large datasets that detail multi-modal information about cell types. This manuscript presents a system for a generalizable nomenclature that can be applied to the mammalian brain. The system will permit researchers to compare their own cell-type data with other published datasets and facilitate consistent cell-type naming.

Decision letter after peer review:

Thank you for submitting your article "Cell type nomenclature for the mammalian brain: Development and application of a systematic, extensible convention" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Genevieve Konopka as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Catherine Dulac as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Fenna Krienen (Reviewer #2); Joseph D Dougherty (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

All reviewers were in agreement that this paper presents some potential ways of tackling an important problem. However, we think there are some aspects of the paper that could be improved for clarity and to make it accessible to a broad audience. The new policy at eLife is to write a summary of essential revisions for the authors when a revised manuscript is warranted and not necessarily send the authors the full reviews.

Our essential revisions include: (1) more details on the immediate use of the system and potentially a step-by-step guide-it definitely seems like this system needs to be much more user friendly even for programmers; (2) how this approach would work without a reference set and ultimately the plan for oversight of such a reference; and (3) how to apply this across species, regions, and modalities.

Even though the new policy is not to send the full reviews, the reviewers each had some useful ideas and nuances about the essential revisions so we are also attaching them here. We do not expect you to address each and every one of these points/comments but rather take them into consideration as you address the essential revisions.

Reviewer #1:

This paper provides an important foundation to develop a universal nomenclature system for vertebrate cell types in single-cell sequencing studies. Similar to efforts to establish gene nomenclature guidelines, this resource is necessary to improve comparisons between datasets and species. As the authors note, any useful system will need to be widely agreed upon and adopted by scientists, and this paper is a good step in initiating that process. I have some general comments on the manuscript and the system that could be implemented. However, I imagine that there might be further modifications that would occur after publication of this manuscript.

1) The glutamatergic nomenclature scheme is neocortical-centric. The "layer" designation should really be a regional specification. For example, "L2/3 IT 4" could have a prefix indicating neocortex like "N L2/3 IT 4." This could allow for expansions including layers in non-neocortical regions, like hippocampus (e.g., "H L2"), or non-layered regions of the pallium like the claustrum (e.g., "C IT"). This would also enhance applicability for non-mammalian brains lacking layered organizations.

2) Glutamatergic cell types across broad vertebrate taxa (e.g. reptiles, birds, mammals) cannot be universally compared to layer-specific nomenclature in mammals because neocortical organization is unique to mammals. Therefore, a universal reference taxonomy must be supplied independently for each major grouping, and homologies can be suggested by, but not defined from, nomenclature. In general, it would be best to emphasize that similarities in cell types are not necessarily indicative of homologies for those cell types. A better description of how one might deal with cell types that diverge across species might be warranted.

3) At some point, the integration of spatial information (other than layers, such as dorsal or ventral) into single-cell sequencing experiments may become commonplace. This nomenclature scheme should be able to incorporate a spatial component if this information proves meaningful, similar to how the authors describe the use of electrophysiological data.

4) The taxonomy ID format CS[YYMMDD][#] is generally fine but note that a four-digit year notation would remove date ambiguities and is in line with universal date formats (ISO 8601).

5) "Cell set label" seems superfluous when "Cell set accession ID" can sufficiently identify each unique cell group. The distinction between identifying "neuron" versus "non-neuron" does not seem to provide enough meaningful information to warrant a separate identity. Table 1 already mentions that this label may be redundant.

6) How/ what steps will be taken to vet the data to include in the taxonomy? As the authors mention there are so many groups generating single cell data but not all of these datasets are of great quality – especially for a naming convention. Will BICCN do this? I imagine the HCA folks might only take care of human data or certain model systems? Who will be in charge of defining the reference cell types?

7) How will the batch differences (lab, sequencing method, machine) be handled?

8) It was mentioned that the same mapping and clustering technique will be applied for all datasets. -Is it possible that certain datasets might be more amenable to "tweaks" in a pipeline rather than a one size fits all approach?

Reviewer #2:

This manuscript presents a proposal for a generalizable cell type nomenclature convention system for the mammalian brain. How to define and name brain cell types is a longstanding issue; there is currently no standard convention. The recent explosion of large, single cell datasets based on molecular measurements (RNA, epigenetics) means there is both an opportunity to gain detailed and often multi-modal information about cell types, as well as a need to reconcile nomenclatures across studies. As such, this article presents a thoughtful, implementable system for a standardized nomenclature, as well as a discussion of some infrastructure and governance considerations that would facilitate widespread community adoption.

1) I read this project as having two components: (A) an immediately implementable nomenclature system (with associated code for end-users to run on their own data), and (B) a proposal outlining possible infrastructures that would support 'alignment' of community data to reference(s) and linking cell type information across studies (including the need for computational infrastructure, governance). I think there should be better motivation for why (A) should be adopted without (B). The authors state that the schema will be "immediately useful" but an end-user may not see the practical advantage over their own in-house conventions (unless/until there is a reference, governance, ontology with controlled values, etc).

2) Practically speaking, the article (or at least the github repo) should also clearly state what best-practices adoption of (A) would look like before a data repository is established, i.e. which outputs or terms are used in figures and tables, should full outputs be included as supplementary data (spreadsheets) in manuscripts etc. The schema introduces quite a few new terms and conventions and I think you have to be more explicit for how end-users should incorporate it in their own work. This could be achieved by more detailed examples as well as guidance in the github (note I ran the code using the supplied MTG dataset but did not try applying it to new data. Authors might consider adding vignettes that take in common algorithm outputs, e.g. output from Seurat, 10X cell ranger pipeline etc).

3) Multiple examples of applying the nomenclature schema to published datasets are given. I wonder whether it would be more effective to focus on one dataset. Figure 1 (human transcriptomic MTG data) and Figure 2 (mouse transcriptomic VISp data) largely do the same work, though they are displayed and formatted differently, which is a bit confusing. Figure 5 presents an example of creating a reference from the data in Figures 1 and 2, but several aspects are not clear: in (B), how are the preferred aliases named, (C) does "Human types" = cell set labels in Figure 1B, (D) how are the lines that visually link the modalities derived, and how are they formally represented in the nomenclature system. The final example (multi-modal, multi species comparison of cortical area M1) is also complex as it contains multiple datatypes as well as a derived 'reference', but as currently presented is not very effective in showing how the nomenclature is applied or how taxonomies are linked. I wonder whether it would be more effective to focus either on the taxonomies presented in Figures 1, 2 and 5, or alternatively on this large M1 study, and fully unpack how to apply and visually represent the schema with just one of these. Alternatively, one could start with toy examples that illustrate the process before applying to real data (again one might be better than several).

4) Creating or using a reference is not explicitly part of the proposed nomenclature schema, but clearly has great utility in terms of linking taxonomies (Figure 5 and 6). The authors could consider describing in more detail the considerations they have made in forming such cross dataset or cross species references. How do user-generated references fit in the proposed system – can the same classification system be applied (i.e. each reference has a taxonomy ID, each cluster has a cell set accession ID) or are there other metadata that should be included? Authors might consider a separate figure devoted to applying the nomenclature schema to a derived reference (e.g. unpacking something like Figure 5B).

5) If I understand correctly, cell set aliases can be based on seemingly very different types of evidence, including (1) quantitative alignment to a reference, (2) user inference based on observation of shared features such as marker genes (i.e., both datasets have Chodl+ cluster, so it is probably the same), and (3) inference based on prior knowledge (an ME cell set that has a location and electrophysiological profile consistent with chandelier cells is aliased to a transcriptomic cell set named "chandelier"). These are really different types of evidence and perhaps should be controlled or distinguished in the system.

Reviewer #3:

This paper is a thoughtful contribution to a tough problem and represents a reasonable step in the right direction. I think it would fit well with eLife and form the basis for beginning of better cross-paper curation of scRNAseq data and other related datasets. It is not the full solution, but is careful in its claims and I think will be an important part of the conversation towards those larger solutions. I have some moderate recommendations for revisions.

1) For cell set accession IDs, they may want to include a '.' between the CS191012 and the unique number for the cell set, and then just iterate the numbers up (.1, .2, .3, … .12 … .10000). The current scheme will max out at 1000 cell sets. That might seem like a huge number now, but someone soon will do 10x on the whole body in one paper and need more than 1000 cell sets.

2) I don't have the bandwidth at the moment to do this as a reviewer, but I would recommend they consider approaching 2-3 labs outside of their group (i.e. external Beta testers) and have them try to enter on of their datasets into this structure using the GitHub code and see how it goes, using only this paper and the associated materials as instructions and iron out any wrinkles or misunderstandings that emerge. If you want this to roll out smoothly, you want researchers' first experiences trying it to be positive to help promote wide adoption.

3) I would recommend adding a section (or perhaps a supplement) that is a clear checklist of what to do as an end researcher who might want to adopt this. If you've convinced me to do this with my data, what are the explicit and actionable recommendations for what I should do? Is this meant to be like submitting your data to GEO? Where any paper publishing a scRNAseq dataset will adopt this standardized approach to naming as the simultaneously upload their taxonomy to a particular database in a standardized format, and put a link in their Materials and methods section? I feel like this is not quite proposing that (as no such database was highlighted, though they highlight the need for one). Or rather is the hope that anyone who generates a scRNAseq dataset will provide their taxonomy in a standard file format as a supplement to their paper? If so, defining a file type (a .txon file or something?) that you are recommending everyone generate and add as supplement might be what you are championing. Explicitly naming that filetype(s) and making that recommendation might help. (If so, is that something that could be rolled into standard analysis packages – e.g. Seuret? That would lower the barrier to adoption) Or is this more like just trying to have everyone agree to use standardized gene names when they mention them? But not necessarily provide supplementary files. Like just being careful how you format your writing and figures like how I should use Pvalb for mouse genes and PVALB for human and PVALB for the protein, and not PV, PVA, etc? Anyway, I just wanted more concrete recommendations of what our expectations as authors (and as reviewers) ought to be for adoption of this standard.

As a starting point, perhaps just recommending a defined file type generated by the code (the .txon file) be included as a supplement is a reasonable recommendation at this time.

Basically, overall I think this paper is making an important and timely contribution. It did a good job of explaining their solution to addressing some of the challenges for annotating these datasets, but stopped just short of a concrete guide on how one could implement it in the near term.

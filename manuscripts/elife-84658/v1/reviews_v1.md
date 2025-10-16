# Peer review - Round 1

Editors:
- Martin Graña, https://ror.org/04dpm2z73 Institut Pasteur de Montevideo Uruguay

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84658.sa0](https://doi.org/10.7554/eLife.84658.sa0)

Focused on host-pathogen interactions, this valuable study presents a useful resource for unifying language(s) and rules used in biology experiments, with a new ontology and tool called PHI-Canto. The framework enables using UniProtKB IDs to curate proteins and eventually derive 'metagenotypes', an important concept that may incidentally help shrinking proliferating names and acronyms for genes, processes, and interactions. This important framework builds on established standards and methods and was rigorously tested with a variety of publications, providing a system that may eventually capture complex information hidden in the data, such as metagenotypes.


---

# Peer review - Round 1

Editors:
- Martin Graña, https://ror.org/04dpm2z73 Institut Pasteur de Montevideo Uruguay

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84658.sa1](https://doi.org/10.7554/eLife.84658.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A framework for community curation of interspecies interactions literature" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Meredith Schuman as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Lorena Etcheverry (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Specify where the contributions go, how curation is done, and how they are made available.

2. Describe or reference the complete data model behind annotations, namely: concepts, methods, eventual algorithms, as well as formats for information storage and retrieval.

3. Expand on how data display and interoperability are implemented, for example, to link related information from new and existing publications. Address the possible use of graph representation to link complex information. (See more detailed comments from Reviewers 2 and 3.)

4. Explain why PHIDO has been generated rather than using existing disease terminologies (such as Mondo or DO).

5. The authors should briefly comment on the possible extension of this approach beyond pathogen-host interactions, which could increase the broader relevance of the study.

Reviewer #1 (Recommendations for the authors):

Many readers may wrongly think they will find tones of centralized information about, e.g. their present-day favorite gene. This does not seem to be the case, leading to a related question: where do the contributed curations go and how are they made available? Is there a final control from within the resource team to filter wrong curations due to bad procedures, or even directly fraudulent data treatments?

On the model extension side, feeding on new interactions proposed by users: it is not clear what kind of follow-up would be made in order to encompass the usage with appropriate growth and amelioration. Are there plans for this? Also, given that most authors are in the industry, a short statement about conflicts of interest would be desirable. Related to this, it is not clear to the reader if new, useful added curations obtained by a user, will be added to the resource and made publicly available. In an ideal world, the ten examples forming the basis of the resource should grow to thousands. I might be missing something, though.

Reviewer #2 (Recommendations for the authors):

Given my area of expertise, I am not in a position to assess the relevance of the work from a biological point of view. However, I feel that some points relating to data management and problem modeling deserve some comment.

In particular, there is no mention of the complete data model of each annotation or the formats in which this information is stored. This omission is probably because this is part of the Canto project. Still, to make this publication self-contained, it would be desirable to include this information or at least a reference to it, especially to measure the changes required.

Something that would also improve the work is more detail on how to use or visualize the data generated. Although there are a few brief lines in the section on "Display and interoperability of data", Figure 4 raises the question of how the system will behave in cases where there are already curated publications that refer to the pathogens and hosts of the new publication to be curated. It would be desirable that they are not treated in isolation but that the system allows them to be linked and then navigated in the network resulting from curating a set of publications.

Finally, in the introduction to the paper, the authors make the reckless assertion that manual biocuration is the only way to reliably represent information about functions and phenotypes. I would question this assertion given the current state of the art in LNP tools. While it is likely that, in many cases, automated annotation or curation using these techniques will not yield such accurate results, I believe it would be desirable to explore these techniques. It is also possible to think of hybrid human-in-the-loop systems where automatic techniques assist experts and simplify repetitive tasks. I believe that the paper should at least include a discussion of these issues.

Reviewer #3 (Recommendations for the authors):

Here are some specific points of confusion, questions, or suggestions for improvement:

Page 5 of the manuscript (page 6 of the full pdf):

– Lines 103-105 talk about changes in pathogenicity and virulence. It would be useful to readers to have a brief explanation of how these differ from each other and why one only applies to the pathogen while the other can apply to either the host or the pathogen.

– bottom of the page talks about "annotation types". The term "annotation type" seems to be used in a way that allows confusion with the entity being annotated. I believe that the authors intend to say that gene, genotype, and metagenotype are types of biological features (to use their term) that are annotated within PHI-Canto, each with its own set of accompanying annotation types as outlined in Table 1. If that is the correct interpretation, then I suggest modifying the text to make this more explicit with a particular focus on the sentence on lines 111-113.

Page 6 of the manuscript

Line 114 – "curators use annotation extensions" is referenced to a GOA paper. Perhaps then the sentence should specify that GO annotation curators use annotation extensions or indicate the reference is an example of this practice, using "e.g." perhaps.

Page 11 of the manuscript

Last paragraph – the text mentions that ECO terms are used to capture evidence. However, the annotation examples in Appendix 1 appear to use a combination of GO evidence codes and terms/phrases that are related to ECO term names. If ECO is being used, why not use the ECO term ids and/or term names across the board?

Page 12 of the manuscript

Top of page – what is the relationship between PHIDO and other existing disease ontologies such as Mondo or DO?

Figure 5

The NCBI taxonomy is listed in the databases section, however, it is more of a cv – it's certainly not a database like UniProtKB or PHI-base are. The Evidence and Conclusion Ontology is mentioned in the text but is not in the list of OBO Ontologies. The curated list of strains (line 247, page 11) is not shown as a PHI-base CV, although perhaps the list of strains is stored in the form of the mapping file that is shown in the figure. Is that the case? If so, then perhaps rename that box to make that more clear.

Table 1

– In the gene section, GO annotation type – are the host species and symbiont species extensions meant to indicate the interacting species? Or the species from which the gene comes? I'm assuming it means the interacting species, but this could be made more explicit.

– In the genotype section under "single species phenotype" should it not say "(Pathogen phenotype or Host phenotype)" rather than "and"?

Appendix 1

– In general, I find the header/spacing organization made it difficult to follow where one part ended and the next began. Perhaps giving letters to the sections starting "If you have…" such that there would be Section 1A, 1B, etc. might help. Also perhaps the use of some indentation so that separate sections referring to each publication will be easier to see.

– Section 1, the section on "If you have a metagenotype phenotype recording "a pathogen effector' (corresponds to footnote 5 in table 2)" – annotations for PMID:31804478: I'm confused why in the gene level GO process annotations that the gene is annotated to the specific child GO:0052034 'effector-mediated suppression of host pattern-triggered immunity', however, when the 'protein binding' and 'enzyme inhibitor activity' GO function annotations are made, the part_of annotation extension is to a grandparent of GO:0052034 that is GO:0140590 'effector-mediated suppression of host defenses. I would have thought that the part_of annotations would have been to GO:0052034. Why is this not the case?

Table 1 and Appendix 1 – both refer to the example paper involving mutualism. By definition, in a mutualist relationship, neither partner is a pathogen as disease is not caused. I realize this issue is likely beyond the scope of this paper to discuss, but I wonder about the inclusion of this annotation in the PHI resource since it does not involve a pathogen. Is it because the species has been seen to be a pathogen in other cases? Or is it that PHI includes some non-pathogenic interactions as well? If the first case, it brings to bear how to define something as a pathogen when (as is true for almost all organisms that cause disease in another organism) it only causes disease in some situations and not others (which is of course relevant to the host-pathogen-environment disease triangle mentioned in the text and Figure 1). If it is the second case, might it make sense to think about the scope of the resource as related to its name? Since mechanisms of colonization are often shared between pathogens and beneficial commensals alike, including annotations for symbionts beyond known pathogens would be useful. However, if these are regularly included, more prominent statements to that effect made on the PHI website and in publications would inform users.

# Peer review - Round 1

Editors:
- Peter Rodgers, eLife United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52614.sa1](https://doi.org/10.7554/eLife.52614.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Wikidata as a FAIR knowledge graph for the life sciences" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by the eLife Features Editor (Peter Rodgers). The following individuals involved in review of your submission have agreed to reveal their identity: Chris Mungall (Reviewer #3).

The reviewers have discussed the reviews with one another and the Features Editor has drafted this decision to help you prepare a revised submission. We hope you will be able to submit the revised version within two months.

SUMMARY

The manuscript describes the life sciences component of the Wikidata knowledge base, which combines multiple disaggregated knowledge/databases into a single source enabling integrated querying. The authors describe the process for keeping Wikidata up to date, and they describe compelling use cases showing the power. Although there are many efforts in the life sciences to create integrated knowledge bases / knowledge graphs, Wikidata is unique in the breadth, scope, and in the community/crowdsourcing aspects. It is an increasingly important resource in the biomedical landscape, and the manuscript provides a clear description of the authors' significant efforts in building this component of the resource. However, the manuscript would benefit from addressing a number of issues in greater detail - see below.

ESSENTIAL REVISIONS:

1. An argument is made that Wikidata combines centralized and distributed approaches. This is an interesting concept. It would be important to know the relative importance of those two approaches. In other words, what proportion of edits is centralized (bots) and what proportion is distributed (contributors). Authors repeatedly refer to the fact that anyone is empowered to add new content, but how much of this potential is realized, and how this compares to other Wiki projects, e.g., Wikipedia?

2. Performance metrics and measurable assessment are often missing from the description of the applications. For example, when the process of translation of identifiers from various databases is described, no information is provided if the translation is done deterministically or probabilistically, how it is done algorithmically, how the performance can be evaluated (AUC ROC?), how Wikidata compares to other systems (e.g., UMLS). It is admirable that the authors admit that "Wikidata is certainly not complete with respect to identifier mappings...", but readers would benefit from knowing more about the proportion of mappings available and those not, and how this differs across databases integrated within Wikidata.

3. In such a broad overview, including multiple use cases, some selectivity in the presentation of examples is probably inevitable. This is understandable. Yet one can make those choices more informed, and offer, in addition, examples less favorable to the system (Wikidata), and in this way provide a balanced assessment. For example, on pages 10-11, for the purpose of disease diagnosis, annotations from the Human Phenotype Ontology (HPO) were compared to combined HPO + Wikidata annotations. However, comparison to only one set of annotations with respect to only one disease could be uninformative. At least, performance should be evaluated against a set of different randomly selected diseases.

4. An argument is made that the "Wikidata is among the most FAIR biomedical resources available". What are the other resources, and how Wikidata compares to those resources with respect to the four FAIR criteria?

5. The FAIR principles do not address the issue of completeness, as they were designed for datasets which are inherently self-contained and presumably complete with respect to the experiment/study. For biomedical knowledge bases (KBs), especially warehouse-style, a key question is: how complete is the KB? How often will my queries have false negatives? (Of course, KBs are always incomplete due to both knowledge and curation gaps. However, it is still important to provide users a sense of the areas in which there are major gaps, for example due to inability to integrate a key resource due to licensing).

An example is on figure 1: there are only 636 disease to symptom/phenotype associations. This is a very small amount, when compared to reference resources like the Human Phenotype Ontology. This may have negative consequences for applications built around Wikidata, causing people to lose trust. Another example is in the subset of genes imported - from 200 species. What determines the set of species included? Are there performance implications in including all genes in all species?

Of course, this is a difficult challenge for any KB, and completeness is not expected. I would still recommend a section that acknowledges and addresses this, addressing questions such as:

- how is a user best able to determine whether a portion of Wikidata is complete enough for their use case

- what is the process for deciding what is included vs excluded?

6. Identifier merging details: The identifier mapping use case is well articulated, but some details are omitted. Some identifier mapping resources store pairwise mappings without privileging any one resource. Wikidata is more like UMLS, in which they mint a new concept ID for the unified concept, and map everything to this. The challenge with this scheme is deciding on the criteria for lumping and splitting. Many source mappings are not 1:1, which can lead to excessive merging when these are traversed transitively

- For bot-derived entities, what is the algorithm for doing this?

- Is one source (e.g. NCBI gene) taken as canonical?

Additionally, it would be useful to see a stricter comparison with sources like bridgedb, in terms of completeness and consistency.

7. Trustworthiness of curation: The strength of Wikidata is in the crowdsourcing of knowledge. While this can be scaled up more easily due less of a need for funded curators, the downside is that the information may be less accurate and reliable. The paper provides good evidence of reliability via the disease cross-referencing experiment, in which 99% of 2030 crowd-sourced mappings were reviewed and accepted.

I am a little skeptical of the generalizability of these results. Mappings are generally quite easy and can be done with reasonable reliability by an automated string-matching process (with some caveats). It would be useful to know more about how many different people contributed to the 2030 (was it one person running a script)?

Refinements to the ontology structure are harder, and it's not clear how often these were incorporated. The mapping results are still a nice example, but they need to be qualified more, and there should be more discussion on reliability.

8. Phenomizer analysis: It's not clear if there is circularity in the Phenomizer analysis:

- were there publications that incorporated the case reports that were then annotated? Was this controlled for?

- What happened on 2018-09 when the HPO-only semsim score jumps? Were the WD annotations incorporated into HPO? Or was this independent annotation? The subsequent drop is curious.

9. Some lines read as if written for a grant proposal, e.g., "Wikidata has a proven track record for leveraging...", "Wikimedia Foundation... has a long track record of developing and maintaining..." see Introduction. In many instances, Wikidata is presented as "unique". Please reword such sentences/passages.

CODE/DATA

The Phenomizer analysis can't be reproduced at the moment, as the curated case reports with HPO IDs are not made available. Additionally, the settings for Phenomizer should be made available, also Phenomizer provides p-values, it would be useful to see this in the analysis results.

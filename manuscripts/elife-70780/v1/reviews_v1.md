# Peer review - Round 1

Editors:
- David A Donoso, https://ror.org/02b4apg34 Escuela Politécnica Nacional Ecuador

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70780.sa0](https://doi.org/10.7554/eLife.70780.sa0)

Rutz et al. describe the LOTUS initiative, an open science database that contains over 750,000 referenced structure-organism pairs. Present both the data that they have made available in Wikidata, as well as an interactive web portal, LOTUS provides a powerful platform for mining literature for published data on structure-organism pairs. The strength of this initiative lies in the effort the authors had put in creating a database that is both reproducible and usable. The result is thus a complete and user-friendly product that will respond to people's needs.


---

# Peer review - Round 1

Editors:
- David A Donoso, https://ror.org/02b4apg34 Escuela Politécnica Nacional Ecuador

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70780.sa1](https://doi.org/10.7554/eLife.70780.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The LOTUS Initiative for Open Natural Products Research: Knowledge Management through Wikidata" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Charles Tapley Hoyt (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. Please notice you count with detailed comments from three reviewers. While all of them see potential in your ms, we encourage you to provide a meaningful revision and detailed point-by-point response to criticism.

Essential revisions:

1) Reviewers would like to see the authors clarify the scope of their work and address to what extent this database will provide the community with a comprehensive database of structure organisms pairs, that is actually useable to answer research questions. This could be achieved by adding concrete examples of how these data could be used to help readers/reviewers understand the scope.

2) Reviewers think the manuscript provides missing or incomplete documentation on the LOTUS processes and software, especially in terms of reproducibility of results. Providing open access to source code and data is an important first step, and additional (challenging!) steps are needed to help others independently build, and use, the provided software/data.

3) The authors have yet to provide compelling evidence of how their continuously managed (and updated) resources can be reliably cited in scholarly literature and incorporated in scientific workflows. In order to study and reference Wikidata, a versioned copy needs to be provided: Wikidata is updated constantly, and these constant stream of changes make it hard for others to verify results extracted from some older version of the Wikidata corpus unless a versioned copy is provided.

Reviewer #1 (Recommendations for the authors):

“A third fundamental element of a structure-organism pair is a reference to the experimental evidence that establishes the linkages between a chemical structure and a biologicl organism and a future-oriented electronic NP resource should contain only fully-referenced structure-organism pairs.”

Typo in "biologicl"

“Currently, no open, cross-kingdom, comprehensive, computer-interpretable electronic NP resource links NP and their producing organisms, along with referral to the underlying experimental work”.

missing "that"

"KNApSAck currently contains 50,000+ structures and 100,000+ structure-organism pairs. However, the organism field is not standardized and access to the data is not straightforward".

This is the first opportunity in the manuscript to describe in more detail the perils of previous databases, especially the mess that is KNApSAck, which you have no choice but to work on because of its ubiquity.

“NAPRALERT is not an open platform, employing an access model that provides only limited free searches of the dataset”.

There's an awful lot of praise for this database given that it is directly antithetical to the manuscript. Please provide further commentary contrasting the work in NAPRALERT (particularly, about its shortcomings as a closed resource) to LOTUS.

“FAIR and TRUST (Transparency, Responsibility, User focus, Sustainability and Technology) principles”.

If you really want to go down the buzzword bingo, I'd suggest making a table or going in depth into each point. These acronyms are, in my opinion, effectively meaningless from a technical perspective, so it falls on the authors of the paper who want to use them (as you are no doubt pressured to do in the modern publishing landscape) to define them and qualify their relevance to your more practical goals.

“…any researcher to contribute, edit and reuse the data with a clear and open CC0 license (Creative Commons 0).”

This is a really interesting point considering you have taken information from several unlicensed databases and several that have more permissive licenses. How do you justify this?

“The SSOT approach consists of a PostgreSQL DB that structures links and data schemes such that every data element has a single place”.

Why is Wikidata not the single source of truth? This means that the curation and generation of this dataset can never really be decentralized- it will always have to be maintained by someone who is the maintainer of the PostgreSQL database. What are the pros/cons for this?

“The LOTUS processing pipeline is tailored to efficiently include and diffuse novel or curated data directly from new sources or at the Wikidata level.”

This sentence is confusing

“All stages of the workflow are described on the git sites of the LOTUS initiative at https://gitlab.com/lotus7 and https://github.com/mSorok/LOTUSweb”

Later this became a problem for code review. Why are the code all in different places? There are "organizations" both on GitLab and GitHub to keep related code together. Further, putting code in a personal user's namespace makes it difficult to for potential community involvement, especially if the user becomes inactive. Also a matter of opinion, but most science is being done on GitHub. Using GitLab will likely limit the number of people who will interact with the repository. Highly suggested to move it to GitHub.

“All necessary scripts for data gathering and harmonization can be found in the lotus-processor repository in the src/1_gathering directory."

The reference to "SI 1 Data Sources List" does not include the actual license information in the table, but rather links to READMEs (which may not stay stable for the life of the manuscript). This should explicitly state which license each database has. Further, it seems a bit disingenuous since some of these links point to README pages that state there is no license given, such as for Biofacquim (and several others)

https://gitlab.com/lotus7/lotus-processor/-/blob/main/docs/licenses/biofacquim.md

How can you justify taking this content and redistributing it under a more permissive license?

Further, this table should contain versioning information for each database and a flag as to whether it is still being maintained, whether data can be accessed as a dump, and if there is a dump, if it is structured. Right now, the retrieval column is not sufficient for describing how the data is actually procured.

Can you cross-reference these databases to Wikidata pages? FAIRSharing pages? I'm sure following publication in the near- or mid-term, more of these databases will go down permanently, so there should be as much information about what they were available with this publication.

Small suggestion: right align all numbers in tables.

“This process allowed us to establish rules for automatic filtering and validation of the entries. The filtering was then applied to all entries.”

Please explain this process, in detail (and also link to the exact code that does it as you have done in other sections)

“Table 1: Example of a referenced structure-organism pair before and after curation”.

Would like some discussion of the importance of anatomical region in addition to organism. Obviously, there is importance in the production of the NP in a given region. This is highly granular and makes the problem more difficult, but even if you don't tackle it, it has to be mentioned.

Further, why is the organism not standardized to a database identifier? Why are the prefixes to go along with these ID spaces not mentioned (InChI-key for structure, DOI for reference, and what for organism?) Maybe one of the confounders is that there are many taxonomical databases for organisms with varying coverage – this should be addressed. On second pass through the review, I noticed this was described a bit more in the methods section, so this should be linked. Further, it's actually not clear even by the end of the methods section what identifiers are used in the end. Are Wikidata Q identifiers the single unifying identifier in the end?

“Figure 2: Alluvial plot of the data transformation flow within LOTUS during the automated curation and validation processes.”

Looks like more things are rejected than kept. What about having a human curator in the loop? Or should poorly curated stuff be thrown way forever? There was a small mention about building a human curation system, but I don't think this had the same focus.

“The figure highlights, for example, the essential contribution of the DOI category of references contained in NAPRALERT towards the current set of validated references in LOTUS”.

Is this to say LOTUS is constructed with the closed data in NAPRALERT? Or the small portion that was made open was sufficient?

“…any researcher has a means of providing new data for LOTUS, keeping in mind the inevitable delay between data addition and subsequent inclusion into LOTUS.”

How likely do you think users will be to contribute their data to LOTUS, when there are many competing interests, like publishing their own database on their own website, which will support their own publication (and then likely go into obscurity)?

Ultimately, this means there should be a long-term commitment from the LOTUS initiative to continue to find new databases as they're published, to do outreach to authors (if possible/necessary), and to incorporate the new databases into the LOTUS pipeline as a third party. This should be described in detail – which organizations will do this/how will they fund it?

“For this, biological organisms were grouped into four artificial taxonomic levels (plants, fungi, animals and bacteria).”

How? Be more specific about methodology including code/dependencies

“Figure 6: TMAP visualizations of the chemical diversity present in LOTUS. Each dot”.

This color scheme is hard to interpret. Please consider using figure 6 in https://www.nature.com/articles/s41467-020-19160-7 to help pick a better color scheme.

“The biological specificity score at a given taxonomic level for a given chemical class is calculated as the number of structure-organism pairs within the taxon where the chemical class occurs the most, divided by the total number of pairs.”

Have you considered the Kullback-Leibler divergence (https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence) which is often used in text mining to compare the likelihood of a query in a given subset of a full corpus? I think this would also be appropriate for this setting.

“This specificity score was calculated as in Equation 2:”

This is a very similar look to the classic Jaccard Index (https://en.wikipedia.org/wiki/Jaccard_index; which is skewed by large differences in the size of the two sets) and the overlap coefficient (https://en.wikipedia.org/wiki/Overlap_coefficient). I think the multiplication of the sizes of the sets will have the same issue as Jaccard index. What is the justification for using this non-standard formulation? Please comment if the conclusions change from using the overlap coefficient.

Since this is supporting Figure 7, a new way to explore the chemical and biological diversity, and you previously wrote the huge skew in organisms and taxa over which information is available, it would be important to comment on the possible bias in this figure. Were you trying to make the point that the NPClassifier system helps reduce this bias? If so, it was unclear.

“As LOTUS follows the guidelines of FAIRness and TRUSTworthiness, all researchers across disciplines can benefit from this opportunity, whether the interest is in ecology and evolution, chemical ecology, drug discovery, biosynthesis pathway elucidation, chemotaxonomy, or other research fields that connect with NP.”

This was emphatically not qualified within the manuscript. The expansions for FAIR and TRUST were given, but with no explanation for what they are. Given that these are buzzwords that have very little meaning, it would either be necessary to re-motivate their importance in the introduction when you mention them, then refer to them throughout, or to skip them. That being said, I see the need for authors to use buzzwords like this to interest a large audience (who themselves do not necessarily understand the purpose of the concepts).

“This project paves the way for the establishment of an open and expandable electronic NP resource.”

By the end of the conclusion, there was no discussion of some of the drawbacks and roadblocks that might get in the way of the success of your initiative (or broadly how you would define success). I mentioned a few times already in this review places where there were meaningful discussions that were overlooked. This would be a good place to reinvestigate those.

Methods

I'm a huge opponent to the methods section coming after the results. There were a few places where the cross-linking worked well, but when reading the manuscript from top to bottom, I had many questions that made it difficult to proceed. The alternative might not be so good either, so I understand that this likely can't be addressed.

“Before their inclusion, the overall quality of the source was manually assessed to estimate, both, the quality of referenced structure-organism pairs and the lack of ambiguities in the links between data and references.”

How was quality assessed? Do you have a flowchart describing the process?

“Traditional Chinese Medicine (TCM) names, and conversion between digital reference identifiers, no solution existed, thus requiring the use of tailored dictionaries.”

How were these made? Where are the artifacts? Is it the same as the artifacts linked in the later section? Please cross link to them if so.

“All pre-translation steps are included in the preparing_name function and are available in src/r/preparing_name.R.”

For this whole section: why were no NER methods applied?

“When stereochemistry was not fully defined, (+) and (-) symbols were removed from names.”

Given the domain, this seems like a huge loss of information. Can you reflect on what the potential negative impacts of this will be? This also comes back to my other suggestion to better motivate the downstream work that uses databases like LOTUS – how could it impact one of those specific examples?

“After full resolution of canonical names, all obtained names were submitted to rotl (Michonneau et al., 2016)”.

missing reference.

Overall

Thanks for writing such a nice manuscript. I very much enjoyed reading it.

In direct conflict with all of the other things that could improve this manuscript, it's also quite long already. Because it reads easily, this wasn't too much of a problem, but use your best judgement if/when making updates.

Reviewer #2 (Recommendations for the authors):

Overall well written with few errors.

page 14:

"Targeted queries allowing to interrogate LOTUS data from the perspective of one of the three objects forming the referenced structure-organism pairs can be also built."

Should be "can also be built"

Some of the figures after page 68 appear to be corrupted.

Reviewer #3 (Recommendations for the authors):

Thank you for submitting your manuscript. Your approach to re-using an existing platform (e.g., Wikidata) in combination with carefully designed integration and harmonization workflows has great potential to help make better use of existing openly available datasets.

However, I was unable to complete my review due to my inability to reproduce (even partially) the described LOTUS workflows. I did, however, appreciate the attempt that the authors made to work towards meeting the eLife data access policies:

from https://submit.elifesciences.org/html/eLife_author_instructions.html#policies accessed on 5 Aug 2021 :

"[…] Availability of Data, Software, and Research Materials

Data, methods used in the analysis, and materials used to conduct the research must be clearly and precisely documented, and be maximally available to any researcher for purposes of reproducing the results or replicating the procedure.

Regardless of whether authors use original data or are reusing data available from public repositories, they must provide program code, scripts for statistical packages, and other documentation sufficient to allow an informed researcher to precisely reproduce all published results. […]"

I've included my review notes below for your consideration and I am looking forward to your comments.

re: "LOTUS employs a Single Source of Truth (SSOT, Single_source_of_truth) to ensure data reliability and continuous availability of the latest curated version of LOTUS data in both Wikidata and LNPN (Figure 1, stage 4). The SSOT approach consists of a PostgreSQL DB that structures links and data schemes such that every data element has a single place."

Single source of truth is advocated by authors, but not explicitly referenced in statements upserted into Wikidata. How can you trace the origin of LOTUS Wikidata statements to a specific version of the SSOT LOTUS postgres db?

re: Figure 1: Blueprint of the LOTUS initiative.

Data cleaning is a subjective statement: what may be "clean" data to some, may be considered incomplete or incorrectly transformed by others. Suggest to use less subjective statement like "process", "filter", "transform", or "translate".

re: "The contacts of the electronic NP resources not explicitly licensed as open were individually reached for permission to access and reuse data. A detailed list of data sources and related information is available as SI-1."

The provided dataset references provide no mechanism for verifying that the referenced data was in fact the data used in the LOTUS initiative. A method is provided for versioning the various data products across different stages (e.g., external, interim, processed validation), but README was insufficient to access these data (for example see below).

re: "All necessary scripts for data gathering and harmonization can be found in the lotus-processor repository in the src/1_gathering directory. All subsequent and future iterations that include additional data sources, either updated information from the same data sources or new data, will involve a comparison of the new with previously gathered data at the SSOT level to ensure that the data is only curated once."

re: "These tests allow a continuous revalidation of any change made to the code, ensuring that corrected errors will not reappear."

How do you continuously validate the code? Periodically, or only when changes occur? In my experience, claiming continuous validation and testing is supported by active continuous integration / automated testing loops. However, I was unable to find links to continuous testing logs on platforms like travis-ci.org, github actions, or similar.

re: "LOTUS uses Wikidata as a repository for referenced structure-organism pairs, as this allows documented research data to be integrated with a large, pre-existing and extensible body of chemical and biological knowledge. The dynamic nature of Wikidata fosters the continuous curation of deposited data through the user community. Independence from individual and institutional funding represents another major advantage of Wikidata."

How is Wikidata independent from individual and institutional funding? Assuming that it takes major funding to keep Wikidata up and running, what other funding source is used by Wikidata beyond individual donations and institutional grants/support?

re: "The openness of Wikidata also o ers unprecedented opportunities for community curation, which will support, if not guarantee, a dynamic and evolving data repository."

Can you provide example in which community curation happened? Did any non-LOTUS contributor curate data provided by LOTUS initiative?

"As the taxonomy of living organisms is a complex and constantly evolving eld, all the taxon identi ers from all accepted taxonomic DB for a given taxon name were kept. Initiatives such as the Open Tree of Life (OTL) (Rees and Cranston, 2017) will help to gradually reduce these discrepancies, the Wikidata platform should support such developments."

Discrepancies, conflicts, taxonomic revisions, and disagreements are common between taxonomies due to scientific differences, misaligned update schedules, and transcription errors. However, Wikidata does not support organized dissent, instead forcing a single (artificial) taxonomic view onto commonly used names. In my mind, this oversimplifies taxonomic realities, favors one-size-fits-none taxonomies, and leaves behind the specialized taxonomic authorities that are less tech savvy, but highly accurate in their systematics. How do you imagine dealing with conflicting, or outdated, taxonomic interpretations related to published names?

"The currently favored approach to add new data to LOTUS is to edit Wikidata entries directly. Newly edited data will then be imported into the SSOT repository. There are several ways to interact with Wikidata which depend on the technical skills of the user and the volume of data to be imported/modi ed."

How do you deal with edit conflicts? E.g., source data is updated around the same time as an expert updates the compound-organism-reference triple through Wikidata. Which edit remains?

"Even if correct at a given time point, scientic advances can invalidate or update previously uploaded data. Thus, the possibility to continuously edit the data is desirable and guarantees data quality and sustainability. Community-maintained knowledge bases such as Wikidata encourage such a process."

On using LOTUS in scientific publications, how can you retrieve the exact version of Wikidata or LOTUS resource referenced in a specific publication? In my understanding, specific Wikidata versions are not easy to access and discarded periodically. Please provide an example of how you imagine LOTUS users citing claims provided by a specific version of LOTUS SSOT to Wikidata.

"The LOTUS initiative provides a framework for rigorous review and incorporation of new records and already presents a valuable overview of the distribution of NP occurrences studied to date."

How can a non-LOTUS contributor dissent with a claim made by LOTUS, and make sure that their dissent in recorded in Wikidata or other available platforms? Some claims are expected to be disputed and resolved over time. Please provide an example of how you imagine dealing with unresolved disputes.

"Community participation is the most e cient means of achieving more comprehensive documentation of NP occurrences, and the comprehensive editing opportunities provided within LOTUS and through the associated Wikidata distribution platform open new opportunities for collaborative engagement."

Do you have any evidence to suggest that community participation is the most effective way to achieve more comprehensive documentation of NP occurrences? Please provide references or data to support this claim.

"In addition to facilitating the introduction of new data, it also provides a forum for critical review of existing data, as well as harmonization and veri cation of existing NP datasets as they come online."

Please provide example of cases in which a review led to a documented dispute that allowed two or more conflicting sources to co-exist. Show example of how to annotate disputed claims and claims with suggested corrections.

How do imagine using Wikidata to document evidence for a refuted "compound-found-in-organism claimed-by-reference" claim?

"Researchers worldwide uniformly acknowledge the limitations caused by the intrinsic unavailability of essential (raw) data (Bisson et al., 2016)."

Note that FAIR does not mandate open access of data, only suggests vague guidelines to find, access, integrate and re-use possibly resources that may or may not be access controlled.

If you'd like to emphasize open access in addition to FAIR, please separately mention Open Data / Open Access references.

re: "We believe that the LOTUS initiative has the potential to fuel a virtuous cycle of research habits and, as a result, contribute to a better understanding of Life and its chemistry."

LOTUS relies on the (hard) work of underlying data sources to capture the relationships of chemical compounds with organisms along with their citation reference. However, the data source are not credited in the Wikidata interface. How does *not* crediting your data sources contribute to a virtuous cycle of research habits?

re: Wikidata activity of NPImporterBot

Associated bot can be found at:

https://www.wikidata.org/wiki/User:NPImporterBot

On 5 Aug 2021, the page https://www.wikidata.org/wiki/Special:Contributions/NPImporterBot

most recent entries included a single edit from 4 June 2021

https://www.wikidata.org/w/index.php?title=Q107038883&oldid=1434969377

followed by many edits from 1 March 2021

e.g.,

https://www.wikidata.org/w/index.php?title=Q27139831&oldid=1373345585

with many entries added/upserted in early Dec 2020

with earliest entries from 28 Aug 2020

https://www.wikidata.org/w/index.php?title=User:NPImporterBot&oldid=1267066716

It appears that the bot has been inactive since June 2021. Is this expected? When does the bot become active?

re: "The Wikidata importer is available at https://gitlab.com/lotus7/lotus-wikidata-importer. This program takes the processed data resulting from the lotusProcessor subprocess as input and uploads it to Wikidata. It performs a SPARQL query to check which objects already exist. If needed, it creates the missing objects. It then updates the content of each object. Finally, it updates the chemical compound page with a "found in taxon" statement complemented with a "stated in" reference."

How does the Wikidata upserter take manual edits into account? Also, if an entry is manually deleted, how does the upserter know the statement was explicitly removed to make sure to now re-add a potentially erroneous entry.

In attempting to review and reproduce (parts of) workflow using provided documentation, https://gitlab.com/lotus7/lotus-processor/-/blob/7484cf6c1505542e493d3c27c33e9beebacfd63a/README.adoc#user-content-pull-the-repository was found to suggest to run:

git pull https://gitlab.unige.ch/Adriano.Rutz/opennaturalproductsdb.git

However, this command failed with error:

fatal: not a git repository (or any parent up to mount point /home)

Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).

Assuming that the documentation meant to suggest to run:

git clone https://gitlab.com/lotus7/lotus-processor,

the subsequent command to retrieve all data also failed:

$ dvc pull

WARNING: No file hash info found for 'data/processed'. It won't be created.

WARNING: No file hash info found for 'data/interim'. It won't be created.

WARNING: No file hash info found for 'data/external'. It won't be created.

WARNING: No file hash info found for 'data/validation'. It won't be created.

4 files failed

ERROR: failed to pull data from the cloud – Checkout failed for following targets:

data/processed

data/interim

data/external

data/validation

Is your cache up to date?

Without a reliable way to retrieve the data products, I cannot review your work and verify your claims of reproducability and versioned data products.

Also, in https://gitlab.com/lotus7/lotus-processor/-/blob/7484cf6c1505542e493d3c27c33e9beebacfd63a/README.adoc#user-content-dataset-list, you claim that the dataset list was captured in xref:docs/dataset.tsv. However, no such file was found. Suspect a broken link with correct version pointing to xref:docs/dataset.csv.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The LOTUS Initiative for Open Knowledge Management in Natural Products Research" for further consideration by eLife. Your revised article has been evaluated by Anna Akhmanova (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues (particularly those of Reviewer 2) that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

I'm quite happy with the authors' responses to my previous review. Thank you for addressing mine and the other reviewers' points carefully.

Reviewer #2 (Recommendations for the authors):

Rutz et al. describe the LOTUS initiative, a database which contains over 750,000 referenced structure-organism pairs. Present both the data which they have made available in Wikidata, as well as their interactive web portal (https://lotus.naturalproducts.net/). provides a powerful platform for mining literature for published data on structure-organism pairs.

The clarity and completeness of the manuscript has improved significantly from the first round to the second round of reviews. Specifically, the authors clarified the scope of the study and provided concrete, and clear examples of how they think the tool should/could be used to advance np research.

I think the authors adequately addressed reviewer concerns regarding the documentation of the work and provide ample documentation on how the LOTUS initiative was built, as well as useful documentation on how it can be used by researchers.

Strengths:

The Lotus initiative is a completely open source, database built on the principles of FAIRness and TRUSTworthiness. Moreover, the authors have laid out their vision of how they hope LOTUS will evolve and grow.

The authors make a significant effort to consider the LOTUS end-user. This is evidenced by the clarity of their manuscript and the completeness of their documentation and tutorials for how to use, cite and add to the LOTUS database.

Weaknesses/Questions:

1) The authors largely addressed my primary concern about the previous version of the manuscript, which was that the scope and the completeness of the LOTUS initiative was not clearly defined. Moreover, by providing concrete examples of how the resource can be used both clarifies the scope of the project and increases the chances that it will be adopted by the great scientific community. In the previous round of reviews, I asked "if LOTUS represents a comprehensive database". In their response, the authors raise the important point that the database will always be limited by the available data in the literature. While I agree with the authors on this point and do not think it takes away from the value of the manuscript/initiative, I think a more nuanced discussion of this point is merited in the paper.

While the authors say that the example queries provided illustrate that the LOTUS can be used to answer research questions, i.e. how many compounds are found in Arabipsis. However, interpreting the results of the query are far more nuanced. For example, can one quantitively compare the number of compounds observed in different species, or families based on the database (e.g. do legumes produce more nitrogen containing compounds than other plant families)? Or do the inherent biases in literature inhibit our ability to draw conclusions such as this? I like that the authors showcase the potential value of using the outlined queries as a starting place for a systematic review, as they highlight in the text. However, I would like to see the authors discuss the inherent limitations with using/interpreting the database queries given the incompleteness of NP exploration.

2) On page (16?) the authors discuss how the exploration of NP is rather limited, citing the fact that each structure is found on average in only 3 organisms, and that only eleven structures per organism. How do we know that these low numbers are a result of incomplete literature or research efforts and not due to the biology of natural products? For example, plant secondary metabolites are extremely diverse and untargeted metabolomics studies have shown that any given compound is found in only a few species. There is likely no way of knowing the answer to this question, but this section could benefit from a more in-depth discussion.

3) I do not understand Figure 4. I would like to see more details in the figure legend and an explanation of what an "individual" represents? Are these individual publications? Individual structure-organism pairs? Also, what do the box plots represent? Are they connected to the specific query of Arbidosis thaliana/B-sitosterol? If they are there should only be a value returned for the number of structures in Arabidopsis thaliana, rather than a distribution. Thus, I assume that the accumulation curve and the box plots are unrelated, and this should be spelt out in the figure legend or separated into two different panels.

4) On page 5 the authors introduce/discuss COCONUT. I am confused about how exactly COCONUT is related to or different from LOTUS. Can you provide some more context, similar to how the other databases were discussed in the preceding paragraph?

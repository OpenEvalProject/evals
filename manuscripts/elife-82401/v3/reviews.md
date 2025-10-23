# Peer review - Round 1

Editors:
- Matthew Redinbo, https://ror.org/0130frc33 The University of North Carolina - Chapel Hill United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82401.sa0](https://doi.org/10.7554/eLife.82401.sa0)

This paper provides important advances in utilizing chemical, metagenomic and enzyme mechanistic insights into the roles gut microbiota play in health-related chemical conversions. The authors convey results from a series of convincing studies that outline the utility of their computational platform, one that will be useful to both specialized microbiome researchers as well as a broad audience of scientists interested in the numerous ways non-host enzymes impact host biology.


---

# Peer review - Round 1

Editors:
- Matthew Redinbo, https://ror.org/0130frc33 The University of North Carolina - Chapel Hill United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82401.sa1](https://doi.org/10.7554/eLife.82401.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A novel in silico method employs chemical and protein similarity algorithms to accurately identify chemical transformations in the human gut microbiome" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Wendy Garrett as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Michael Zimmermann (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Additional non-experimental validations must be performed to support the conclusions drawn by the manuscript

2) At least one experimental validation must also be provided to establish the usefulness of this tool.

3) The manuscript frequently claims superiority over existing methods, but this is not supported by the necessary additional validations requested above.

Reviewer #1 (Recommendations for the authors):

The following should be addressed prior to consideration for publication.

1. The manuscript is far too repetitive in terms of its goals and its claims of success. These claims are clear from the Abstract and Introduction, and should not be revisited throughout the text.

2. More information should be given about the granularity present in the EC code (as noted first in the text on line 85) toward the goals stated. Are EC codes sufficient to select enzyme orthologs within an overall class? For example, would specific Azoreductases be selected by this tool (e.g., a Class I vs. Class II), or would AzoR be the output? This is important for several reasons. First, EC classifications are typically broad (e.g., glycoside hydrolase family 1 has many thousand orthologs in the gut microbiome), and within such classifications many, many distinct orthologs are present. The authors should be clear about what their tool produces and, perhaps even more importantly, what it does NOT produce.

3. How did MetaCyc filter from its ~18K reactions to the nearly ~9K employed?

4. What are the limitations of MetaCyc? Even 9K sounds like a lot, but given ~10 million unique proteins in a conservative estimation of the gut microbiome, those factors (even if only 10% are enzymes) are likely to catalyze more than 10,000 reactions.

5. The statement on lines 214-5 that the data in Figure 3B that "there is much variation in this relationship" appears to be a massive understatement. Figure 3B appears to contain much more information than the authors are considering. To name just one, what is the nature of the cluster between 0.2-0.4 on the x-axis and ~0.2 on the y-axis?

6. On line 281, an output from SIMMER is stated to provide a list of the "top 20" ranked MetaCyc reactions. Is this good enough? The manuscript claims that this tool will provide information that will allow researchers to focus their hypotheses, but if the "right answer" is only 5% of the "possible answers" provided, that is pretty unfocused and does not support the (highly, highly) repeated claims of clean deliverables proffered by the authors.

7. There appears to be package version conflicts for the majority of the conda dependencies specified in SIMMER.yml, such that implementing command-line SIMMER is not straightforward as described in the manuscript or on the github page. This needs to be corrected and β-tested so users can successfully use the tool locally in a command-line manner.

8. An additional "real world" example should be explored to examine the success of this tool. Two suggestions are PMID 31663730 or the very recently published PMID 35953888. In both cases, cleavage of glucuronides is examined from human drugs. However, very unique and hard-to-predict types of glucuronidases are identified in each case, and these unique orthologs are due to the distinct linkage of the glucuronide to the parent drug molecule. Would SIMMER be able to identify these orthologs?

Reviewer #2 (Recommendations for the authors):

A few suggestions to improve and clarify the manuscripts.

1) Related to comment 1) in the 'public review': presenting how many false positive hits per prediction are generated by SIMMER, belonging to how many EC classes, sub-classes, etc. together with the truly positive results would benefit the interpretation of results. Also, the rank position of the true positive prediction in the prediction list should be reported, and not only its presence, since only the top enzyme annotations are used as queries for the protein similarity search of potential gut bacterial enzymes. Especially the potential impact of the presence of several EC classes (eventually biasing the hypothesis generation process before experimental validation) should be assessed.

2) Related to comment 2) in the 'public review': due to the different input formats between SIMMER, MicrobeFDT, and DrugBug, it would be useful to demonstrate that SIMMER has at least comparable performances to the other tools when their input format is used (i.e., substrate fingerprint only).

3) Related to comment 5) in the 'public review': a revision of the text is needed to clarify terms and avoid the readers' confusion. Already in the title, the method is described as being able to "identify chemical transformations in the human gut microbiome"; however, SIMMER requires a fully chemically characterized biotransformation (in terms of substrate, (co-factors), and products) as input (and is therefore not able to identify new biotransformations). The text should be modified to highlight that SIMMER identifies and characterizes the enzymatic reaction of known biotransformation. On the same note, please also revise lines 81-82, 358-359, 480-481, and 531-532 accordingly.

4) The website version of SIMMER could be easily tested; it's intuitive, although a more extensive description of Output headers could help the user understand the results better. It was not possible to create the conda env after cloning the github repo ("Solving environment: failed" error)

5) As showcased in Figure4—figure supplement 1, additional filtering steps might be needed to filter the SIMMER enzyme list to a relevant subset (e.g., before in vitro validation). The authors should consider adding a plug-in to both the command line and online version of the tool so that these filtering steps could potentially be applied by the users as well. This might benefit especially experimentalist users, who might not be comfortable with running several additional filtering steps via cli.

6) More detailed results might improve the understanding of the reported examples. E.g., it is unclear how SIMMER could not accurately predict EC number for brivudine transformation (Line 197), but correctly predict BT_4554 as being responsible for the reaction. Reporting SIMMER output for this query as supplementary material would help the user navigate the examples better.

7) In the example describing dexamethasone biotransformation, the authors should describe the SIMMER predicted enzyme(s) in more detail (predicted EC number, sequence, etc.) since it (they) reportedly does not correspond to the already described DesAB gene.

8) When quantification of SIMMER predicted enzymes is performed in metagenome samples (see for example Lines 427, 430, 545), it is unclear what association is performed: is this the quantification of only the first (i.e., top scoring) predicted enzyme in the sample or is it the quantification of several different SIMMER enzymes in the same sample? If the latter, how are quantification results from different enzymes collapsed together?

Reviewer #3 (Recommendations for the authors):

I am most concerned about major overstatements related to the performance and validation of SIMMER resource predictions.

"We show that SIMMER predicts the chemistry and responsible species and enzymes for a queried reaction with high accuracy."

The validation of SIMMER predicted enzyme-drug interactions utilizes metagenomic data from a single donor stool sample in which drug metabolism was demonstrated. Other samples used as 'validation' have only 16S rRNA gene sequencing.

Their analysis, identifying microbial taxa via 16S in fecal samples that demonstrated metabolism of a drug does not support the claim that SIMMER "predicts the chemistry and responsible species and enzymes". There is no experimental or computational enzymatic validation; rather the authors infer from taxonomic representation in 16S data that the enzymes they predict metabolize the drug must be present in the bacteria found in the drug-metabolizing fecal samples. This validation is several steps removed from identifying "responsible species and enzymes". This sentence in the abstract is thus a major overstatement of their results.

"Bacterial species containing these enzymes are enriched within human donor stool samples that metabolize the query compound."

To discuss this point further; that bacterial species purported to contain specific enzymes are enriched in stool samples that metabolize a compound is insufficient to validate that SIMMER has identified microbiome enzymes that metabolize a drug. Saying that you see species increase in abundance that you think have enzymes that can metabolize a drug is far removed from their claim that they can identify specific microbiome enzyme-drug interactions.

In a later discussion of microbiome metabolism of dexamethasone, the authors state: "These results indicate that species level information alone is not enough to predict chemical transformations in a microbiome sample, but with SIMMER, knowledge of responsible enzymes can recapitulate a sample's potential for therapeutic degradation." However, using species-level information alone is precisely what they did in their 16S-based validation set. This point needs to be clarified.

Finally, they refer to these entirely computational validation approaches as "experimental validation" of SIMMER, which is inaccurate. Based on eLife precedent, I strongly advise experimental validation of at least one of their predicted novel enzyme-drug interactions.

Regarding sequence similarity/chemical similarity, a foundational component of the resource:

"SIMMER was created with the assumption that chemically similar reactions are mediated by sequence similar enzymes"

It would be helpful for the authors to consider the work of the Babbitt, Gerlt, Almo, and Jacobsen labs:

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3249080/

"From a survey of structurally characterized superfamilies, almost 40% are functionally diverse, i.e. different members catalyze reactions with different EC numbers (4). Thus, trivial annotation transfer by sequence homology is often not sufficient to assign function."

The authors' assertion that enzyme sequence similarity is sufficient to identify chemically similar reactions is also not well supported by experimental studies on enzyme families that metabolize drugs in the human gut.

In studies of Cgr2, a member of a microbiome drug-metabolizing enzyme family that was deeply characterized by the Turnbaugh and Balskus labs, sequence-based clustering was unable to resolve biochemical functioning.

https://elifesciences.org/articles/33953

"At all thresholds at which Cgr2 remained connected to other protein sequences, all characterized enzymes within the SSN were co-clustered, precluding the resolution of unique biochemical functions at this cutoff. "

In Figure 3B one can see the issues with protein percent identity as a metric for functional similarity. The use of a linear model is likely not appropriate here given the substantial variability in the relationship between reaction distance and percent identity. However, it is clear that the statement "reactions with similar chemistry are conducted by sequence similar enzymes" is not upheld in much of their data. As an example, in the range of identity that they are using (27% identity, per the methods) there is a large spread in reaction distances.

These nuances in sequence-function relationships that can confound microbiome drug metabolism studies are critical to deal with in such analyses and they are one reason that other resources that seek to identify microbiome-drug interactions utilize a variety of sources of evidence to assess the likelihood of specific microbiome-drug interactions.

As the authors note, each of these current tools to predict microbiome-drug interactions has limitations. For SIMMER, the major limitation, which is only briefly alluded to, is the need for a user to already know both substrate and product. As the authors note, publications experimentally characterizing microbiome-drug interactions often utilize parent compound loss as the marker for microbiome drug metabolism.

Knowing and providing the substrates and products requires chemical knowledge that could also be used to identify the type of reaction that is being carried out. This makes the SIMMER resource harder to use for users without that chemical knowledge, which is where the other resources that the authors use as a comparison (BugDrug, MicrobeFDT) may be more helpful.

Additional comments

The authors should indicate how many different modifications are represented in the 88 reactions that were queried to evaluate how well the resource works at predicting novel drug-metabolizing enzymes.

It is unclear if the SIMMER resource covers greater chemical space than the other resources. Database size does not necessarily correlate with chemical diversity. An explicit comparison of chemical space should be quantified and compared across all resources.

The authors do not represent the goals of the other resources that they use as comparisons accurately; these resources take different approaches to identify microbiome-drug predictions. As an example, the "Direct query" of the MicrobeFDT resource yielded 3/4 "correct" predictions, why does Table 1 not include this accuracy metric?

It would be helpful for the authors to discuss the limitations of MetaCyc and the representation of enzymes involves in anaerobic degradation reactions that would be expected in the gut.

The authors need to make available and searchable their data connecting microbiome taxa, enzymes and predicted drug metabolism, this would greatly broaden the utility of the resource to the community.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "SIMMER employs similarity algorithms to accurately identify human gut microbiome species and enzymes capable of known chemical transformations" for further consideration by eLife. Your revised article has been evaluated by Wendy Garrett (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below.

Reviewer #3 (Recommendations for the authors):

I am satisfied that the authors have carried out key validations of the SIMMER tool, including experimental characterization of a SIMMER prediction, the metabolism of methotrexate by hydrolases.

I ask that the authors credit prior research demonstrating that methotrexate is metabolized by hydrolases (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5082436/). They extend prior work on methotrexate here by showing strain-level characterization of MTX metabolism, a valuable addition to our understanding of drug metabolism by gut microbes.

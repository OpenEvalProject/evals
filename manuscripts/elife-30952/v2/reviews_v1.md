# Peer review - Round 1

Editors:
- Agnieszka Chacinska, University of Warsaw Poland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.30952.045](https://doi.org/10.7554/eLife.30952.045)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Transcriptomic and proteomic landscape of mitochondrial dysfunction reveals secondary coenzyme Q deficiency in mammals" for consideration by eLife. Your article has been favorably evaluated by a Senior Editor and three reviewers, one of whom, Agnieszka Chacinska (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Antoni Barrientos (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

In this manuscript by the Larsson's group, the authors report on global consequences of mtDNA expression dysfunction in the mouse heart. The comprehensive analysis, including transcriptomics, proteomics and metabolomics, of five mitochondrial pathology models with conditional heart-specific mutations in imitochondrial proteins is presented. Their main novel finding is related to the global down-regulation of CoQ biosynthetic enzymes, which appears to occur on a post-transcriptional level, as well as reduced tissue CoQ levels.

The reviewers found the study impressive and of high quality, ideally suited as a resource paper and of immense value for researchers and clinicians. Below are some constructive critiques on the presentation and interpretation of the data.

Essential revisions:

In terms of experiments, the reviewers agreed that protein abundance, inferred from MS, should be verified using ELISA or Western blot on a small handful of proteins, including the representatives of those proteins that change and do not change. Furthermore, citrate synthase activity (a parameter used in clinics) as a measure of mitochondrial abundance should be tested.

Several additional computational analyses need to be performed.

- Accuracy of protein fold-change inference.

Differential expression analyses typically identify a relatively small set of changing transcripts/proteins against the backdrop of a much larger set of unperturbed ones. In this setting, a change in the relative fraction of reads/spectra mapping to a transcript/protein can be assumed to derive primarily from a change in its own abundance rather than from the cumulative effects of changes in the abundance of many other transcripts/proteins.

However, the mito-proteome data presented here shows more than half of mito-localized proteins in almost every KO model are differentially expressed. Wholesale remodeling of the mitochondrial proteome is certainly biologically plausible in these KO models, but it raises some concerns about the accuracy of inferred fold-changes for individual proteins. In particular, the highly abundant OXPHOS proteins are strongly depleted in all KO models – drastically changing the composition of the mito-proteome and potentially elevating the fractional representation of remaining proteins with no underlying change in their abundance. The fact that authors identify sets of proteins that change coordinately in a consistent direction across KO models is reassuring, and suggests the main thrust of the signal they report is unlikely to be confounded. To increase readers' confidence that individual protein changes are accurate and comparable the authors should also show i) the distribution of protein abundances and the distribution of control/KO fold-changes for all proteins in each mouse model, ii) show plots relating the abundance of proteins and their fold-changes, to rule out that originally low-abundance proteins are artifactually inflated in KOs. An MA-plot could achieve this goal, but perhaps the x-axis should be the mean abundance in the control only rather than mean abundance across all samples.

- Systematic bias in protein sampling.

Authors should perform some analyses to check if their proteomics pipeline systematically misses or under-represents certain classes of proteins, such as low-abundance proteins, hydrophobic vs. charged, membrane-bound vs. free. The selection of column, the MS data capture sequence, etc. can influence this sampling. This can be easily done by taking the entire MitoCarta2.0 collection, and breaking it up into two disjoint sets, those MitoCarta2.0 proteins detected (set 1), and those MitoCarta2.0 proteins that are not detected (set 2). Then the cumulative distribution function (cdf) of pI, hydrophobicity, RNA-seq abundance, can be plotted for set 1 versus set 2. Such a plot will reveal any systematic biases in their proteomics datasets, again helping to showcase its strengths and weaknesses.

- Visualization of transcription factor targets.

The paper puts a prominent focus on the Atf4 and c-Myc transcription factors as orchestrators of the response to mitochondrial dysfunction but none of the figures breaking up genes into categories includes a category such as "Atf4 target" or "c-Myc target". Target annotations can be obtained from the literature (e.g., Han et al. 2013, for Atf4).

It seems likely that categories such as "apoptosis", "degradation and stress response", "tRNA charging", and "mitochondrial 1C pathway" – which happen to show the strongest transcript/protein correlation – all include numerous targets of these transcription factors. Thus, the key trend is driven by their joint transcriptional regulation rather than the disparate functional categories. Authors are encouraged to find a way to incorporate this into at least one of their "gene category" figures, and perhaps into the volcano plots as well.

Along this line of analysis, it would be interesting to discuss the consequences for the cell if these transcriptional responses would be abolished? Would the respiratory dysfunction be rather accelerated (because less of oxphos protein synthesis) or less severe, less oxphos protein synthesis or less "secondary responses", related to stress, such as the increase in mitochondrial proteases?

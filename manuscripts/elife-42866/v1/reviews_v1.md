# Peer review - Round 1

Editors:
- Peter Turnbaugh, University of California, San Francisco United States

Reviewers:
- Peter Turnbaugh, University of California, San Francisco United States

## Review text

DOI: [10.7554/eLife.42866.021](https://doi.org/10.7554/eLife.42866.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your article entitled "The gut chemical landscape predicts microbe-mediated biotransformation of foods and drugs" for peer review at eLife. Your article has been evaluated by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, with strong expertise in microbiome research, analytical chemistry, and comparative genomics, respectively, and the evaluation has been overseen by Wendy Garrett as the Senior Editor.

There was a consensus that the identified topic represents a major gap in scientific knowledge and the toolkit established here could provide a valuable resource to the microbiome community. These findings could have broad implications for the field and provide the inspiration and framework for the development of more sophisticated follow-on algorithms. However, the reviewers also raised multiple technical considerations that limited our enthusiasm for publication at this time.

The full reviews are attached below and I have briefly summarized the major concerns here.

1) Lack of computational or experimental validation. The specific examples mentioned as potential future directions do not help that much in evaluating the overall reliability of the predictions made by this approach. The authors should consider whether or not there are suitable gold-standards; for example, the >50 drugs that are already known to be metabolized by human gut bacteria. Alternatively, they could use as positive controls structural analogs like altretamine and melamine, to see if these chemical pairs always result in similar predictions. The authors might also test if their unbiased clustering recapitulates established chemical classes. In addition to these more global analyses of specificity, sensitivity, and precision, we would like to see at least one of the novel predictions validated experimentally (if possible within the time frame).

2) Structural similarity could be misleading. The major caveat to this approach is that overall similarity can be thrown off by differences in parts of the molecules that are irrelevant for the enzymatic activity. This can lead to false positives (compounds with similar overall structure but differences in the relevant sub-structure) and false negatives (compounds with different R groups but the same core chemical motif). While solving this problem may be beyond the scope of this analysis, we would like to see it acknowledged and some analysis to determine how big a problem this is for the current set of predictions.

Numerous research groups work in this area with a higher degree of sophistication, and likely accuracy, than this paper describes (see citations from reviewer 2). Each of the tools above allows compounds to be linked to reactions; none are mentioned in this paper; and none of them rely on simply using a chemical fingerprint as the likelihood that a drug would participate in a chemical reaction. Chemical fingerprints are not intended for asserting that a molecule would be compatible with a chemical reaction. If we understand the algorithm correctly, we don't think it is appropriate for scoring biochemical-reaction promiscuity. We recommend completely overhauling this part of the algorithm.

In the examples that the authors show, leucovorin is strongly clustered with ambenonium which differ in structure. Similarly, metformin and atretamine are very different molecules – even though they are rich in Nitrogen. Furthermore, not every chemical moiety can be undone-just because a molecule has a methyl group doesn't mean that it can be demethylated.

3) Clustering by toxicity could also be misleading. The logic here is not clear, since there could be many reasons for why two molecules show the same toxicity profile – most of which will have nothing to do with the microbiome or with metabolism more broadly. For example, two completely different antidiabetic drugs may have the same side effect, hypoglycemia. A diuretic and a smooth muscle relaxant may have the same side effect, hypotension, etc.

4) ECs are broad groups of enzymes that do not adequately capture substrate preferences. It's unclear to us how the EC analysis would be used in practice. For example, let's consider the case of altretamine and N-demethylases. These enzymes are widespread in bacterial genomes and have broad substrate scope as a family. Which one (if any) can metabolize the drug? Just because an enzyme has an EC annotation of ligase, hydrolase, oxidoreductase, doesn't mean that a molecule with certain functional groups can be a substrate to it. It doesn't even mean that it is correctly annotated.

Reviewer #1:

Guthrie and Kelly present an interesting structure-based analysis of food and drugs with the goal of predicting gut microbial biotransformation. This dataset has great potential as a resource to the community. The major problem is the lack of either computational or experimental validation, making it unclear how reliable the inferences are, and thus limiting their utility. There are also some concerns about the assumptions made by this method that could lead to false positives and false negatives.

Major issues:

1) Lack of validation. While I really enjoyed reading the specific examples mentioned as potential future directions, they do not help that much in evaluating the overall reliability of the predictions made by this approach. The authors should consider whether or not there are suitable gold-standards; for example, the >50 drugs that are already known to be metabolized by human gut bacteria. Alternatively, they could use as positive controls structural analogs like altretamine and melamine, to see if these chemical pairs always result in similar predictions. The authors might also test if their unbiased clustering recapitulates established chemical classes. In addition to these more global analyses of specificity, sensitivity, and precision, I would like to see at least one of the novel predictions validated experimentally.

2) Structural similarity could be misleading. The major caveat to this approach is that overall similarity can be thrown off by differences in parts of the molecules that are irrelevant for the enzymatic activity. This can lead to false positives (compounds with similar overall structure but differences in the relevant sub-structure) and false negatives (compounds with different R groups but the same core chemical motif). While I realize that solving this problem is beyond the scope of this analysis, I would like to see it acknowledged and some analysis to determine how big a problem this is for the current set of predictions.

3) ECs are broad groups of enzymes that do not adequately capture substrate preferences. It's unclear to me how the EC analysis would be used in practice. For example, let's consider the case of altretamine and N-demethylases. These enzymes are widespread in bacterial genomes and have broad substrate scope as a family. Which one (if any) can metabolize the drug?

4) The section on antibiotics (subsection “MicrobeFDT identifies food derived compounds and non-antibiotic therapeutic drugs with putative antimicrobial properties”) was interesting, but doesn't fit the scope of this paper. Need to either remove this section or reframe the goal of this study. I'd vote for the former, since it is currently lacking in novelty or experimental validation.

Reviewer #2:

The manuscript, "The gut chemical landscape predicts microbe-mediated biotransformation of foods and drugs", herein referred to as "this paper", describes a creative computational link between drugs, metabolites, genes and microbes. The narrative on the importance of linking the compounds we eat whether drugs or from food with the reactions in the gut performed by microbes is almost worth publishing on its own. It was enjoyable to read such a well thought out and presented essay on this topic. In regards to the actual research described in the paper, I have two major concerns: the validity of their major claims and using chemical fingerprint as a proxy for reactivity given alternative approaches.

To see if other eLife manuscripts contained more or less validation of computational methods, I searched eLife for "chemical fingerprint". There were 43 results. Of these, the following three are in the same general area as this paper.

– Prediction of enzymatic pathways by integrative pathway mapping: https://doi.org/10.7554/eLife.31097

– Systematic integration of biomedical knowledge prioritizes drugs for repurposing: https://doi.org/10.7554/eLife.26726

– Digitizing mass spectrometry data to explore the chemical diversity and distribution of marine cyanobacteria and algae: https://doi.org/10.7554/eLife.24214

In these three prior manuscripts, the amount of validation varies quite a lot. "Prediction of enzymatic…" includes enzymology, crystallography, and metabolomics to validate their method for a specific pathway; "Systematic integration…" uses only out-of-sample validation set; and "Digitizing mass spectrometry…" uses the identification of a single novel compound to suggest validation of the overall method. My initial reaction to this paper was that its an important application of a creative idea, but the degree to which the network they've built is validate is insufficient. However, in comparison to the prior papers in eLife, I think the amount of validation in this paper is only slightly lower than what is already in the journal. Testing the predictions of their network would be a significant endeavor.

Nevertheless, this paper makes the following claims:

"Together, our resource identifies novel gut microbiome-mediated metabolic activity and associated adverse responses that can be used to identify targets for experimental validation and to generate new hypotheses about microbe-drug-diet interactions in human health and disease. We demonstrate the utility of this resource with the following three novel insights into microbial drug metabolism and human health."

And the following speculations:

"We propose uninvestigated microbiota mediated metabolisms that may drive toxicity of therapeutic drugs, we highlight non-antibiotic compounds that may have antimicrobial properties, and we identify drug-food interactions with microbial enzymes that may influence drug efficacy and microbiome function."

For all claims made in the paper, my belief is that a validated approach should be used. Therefore, I recommend the authors validate their approach prior to making such claims. In the scope of this journal, speculation and suggestion is ok as long as it is worded appropriately.

I'm worried about relying on a chemical fingerprint to assert that a drug would react in place of a metabolite in a known biochemical reaction. Numerous research groups work in this area with a higher degree of sophistication, and likely accuracy, than this paper describes. I am aware of the following works, but there are likely many more.

– in vivo/In Silico Metabolites Database (IIMDB)

– RetroPath and RetroRules (http://www.jfaulon.com/)

– MINEs: open access databases of computationally predicted enzyme promiscuity products for untargeted metabolomics

– MAGI: (https://magi.nersc.gov)

– ATLAS of Biochemistry: A Repository of All Possible Biochemical Reactions for Synthetic Biology and Metabolic Engineering Studies

– Nontargeted in vitro metabolomics for high-throughput identification of novel enzymes in Escherichia coli. Nature Methods (2016)

Each of the tools above allows compounds to be linked to reactions; none are mentioned in this paper; and none of them rely on simply using a chemical fingerprint as the likelihood that a drug would participate in a chemical reaction. Perhaps the most directly applicable to this paper would be RetroPath/RetroRules. It uses a considerably more elegant means to assert that a drug would participate in a reaction. Chemical fingerprints are not intended for asserting that a molecule would be compatible with a chemical reaction. If I understand your algorithm correctly, I don't think it is appropriate for scoring biochemical-reaction promiscuity. I recommend completely overhauling this part of the algorithm.

Reviewer #3:

In the submitted manuscript, Guthrie and Kelly propose a resource (MicrobeFDT) that constructs interacting networks of drugs, endogenous, and dietary molecules based on their structural similarity, known toxicities, and possible metabolizing enzymes.

The manuscript was written in a very convoluted manner, with intertwined logic, design, and results (and even literature references), making it difficult to follow. There is very limited detail about the approach itself and actual analyses. The authors describe three main tasks:

1) Define the chemical space of xenobiotics that the human microbiome is exposed to. They use similarity in chemical substructure to achieve this goal, based on previously developed algorithms and metrics. In the one example that the authors show, leucovorin is strongly clustered with ambenonium – which is clearly a problem! Similarly, metformin and atretamine are very different molecules – even though they are rich in Nitrogen!

2) Cluster molecules based on their reported toxicities. The logic here is not clear, since there could be many reasons for why two molecules show the same toxicity profile – most of which will have nothing to do with the microbiome. For example, two completely different antidiabetic drugs may have the same side effect, hypoglycemia. A diuretic and a smooth muscle relaxant may have the same side effect, hypotension, etc.

3) Identify biochemically relevant and functionally plausible microbe-compound interactions. This section was not clear at all to the reviewer. Even the essence for how microbial enzymes are linked to the network of molecules is not described clearly. In one section, the authors mention: "structure-activity filtering, the user establishes the search target based on prior knowledge of structure-activity relationships (for example, a compound with a methyl group that is susceptible to microbial methylases)". Why would a methylated compound be susceptible to methylases? Maybe it is a typo and the authors meant demethylases? Even in this case, the logic is very unclear. Not every chemical moiety can be undone, and just because a molecule has a methyl group doesn't mean that it can be demethylated. Also, there is a fundamental misunderstanding here for the basics of biochemistry. Just because an enzyme has an EC annotation of ligase, hydrolase, oxidoreductase, doesn't mean that a molecule with certain functional groups can be a substrate to it. It doesn't even mean that it is correctly annotated. Basing conclusions on these general annotations is meaningless.

Overall, the reviewer does not see the value of the tool developed here, based on fundamental issues with the logic of the design itself, as well as a lack of clarity in the description of the method and analysis performed. The examples listed in the text are either obvious (e.g., glucoronidated molecules will probably get deglucoronidated) or completely speculative (steroids are antibiotics), despite being "supported" by cherry-picked citations.

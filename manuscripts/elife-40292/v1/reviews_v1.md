# Peer review - Round 1

Editors:
- Patrick Hsu, Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40292.023](https://doi.org/10.7554/eLife.40292.023)

In the interests of transparency, eLife includes the editorial decision letter, peer reviews, and accompanying author responses.

[Editorial note: This article has been through an editorial process in which the authors decide how to respond to the issues raised during peer review. The Reviewing Editor's assessment is that all the issues have been addressed.]

Acceptance notification:

Prof Telford and colleagues have greatly improved their thoughtful manuscript exploring the limitations and key experimental/analytical parameters of CRISPR-based recorders for lineage tracing, and appropriately addressed the reviewers' comments. Importantly, this study now includes an expanded assessment of lineage accuracy, false positive and negative reconstruction events, and choice of cell lineage inference method. This is a very useful addition to the field that informs optimized design of next-generation CRISPR recorders.

Decision letter after peer review:

Thank you for submitting your article "Is it possible to reconstruct an accurate cell lineage using CRISPR recorders?" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a guest Reviewing Editor, and the evaluation has been overseen by Aviv Regev as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Aaron McKenna and Jay Shendure co-reviewed as Reviewer #3. The other reviewers remain anonymous.

The Reviewing Editor has highlighted the concerns that require revision and/or responses, and we have included the separate reviews below for your consideration. If you have any questions, please do not hesitate to contact us.

As you will see, the reviewers agree this work is a valuable addition to the rapidly growing field of CRISPR recorders and lineage tracing. They also each raise concerns about the results presented and their interpretation. In particular, there was clear consensus about the appropriate definition of and requirements for "accurate" lineage reconstruction, justification of the tree reconstruction algorithms used, and the methodologies used for analysis of editing in Drosophila target arrays. Reviewer 2 also has specific suggestions for the title. We hope these points will be straightforward to assess in a revised manuscript.

Separate reviews (please respond to each point):

Reviewer #1:

There has been an explosion in CRISPR lineage tracing studies over the past few years. However, assessing the "accuracy" of these reported lineage reconstructions is difficult because the correct lineage is typically unknown. In this study, the authors primarily use computational approaches, along with some experimental data in Drosophila embryos, to assess various parameters that affect reconstruction accuracy, such as mutation rate, cell division rate, mutational diversity, and others.

Some thoughts for the authors to consider: From a practical perspective, what is accurate enough? In an experiment where the "real" tree is unknown, how do the investigators determine the appropriate parameters? Are some CRISPR recorder designs fundamentally better than others, and does this study suggest a better approach?

Major comments:

1) Recently, there was a systematic follow up to van Overbeek et al., 2016, by Leopold Parts at the Sanger (Allen BioRxiv 2018), which used a large dataset to provide an indel distribution prediction tool. It would be very interesting to consider this for specific target sequences, and discuss "optimized" spacer sequences for CRISPR recorders that have higher mutational diversity than others.

2) The rationale for assuming that CRISPR recorders generate irreversible target mutations is unclear. For example, there can be a "back rate" where a mutated target that creates a single base indel can still be recognized by Cas9 after a cell division.

3) Why is neighbor-joining chosen over parsimony (and over several other possible algorithms?) This should be elaborated on. Can the authors leverage their insights to improve these reconstruction algorithms to specifically address the challenges of CRISPR recorders?

4) The chosen definition of "accuracy" seems to be problematic because it does not generally discriminate between false positive and false negative reconstruction events. This is briefly considered in Figure 7 but should be expanded.

5) The authors show that setting the correct mutation rate matters. How can mutation rates be matched to the rate of cell division when the rate or interval of cell divisions is unknown/itself variable (e.g. in a tumor)? This would be worth discussing.

Reviewer #2:

The manuscript "Is it possible to reconstruct an accurate cell lineage using CRISPR recorders?" uses simulations and some experimental data to conduct a thorough exploration of the parameters governing the accuracy of CRISPR lineage tracing. They define and sweep four key parameters for two types of CRISPR recorders: number of targets, mutation rate, mutational character states, and dropouts. This work is important and valuable to a growing community exploring the potential of CRISPR recorders. It provides a path for future optimization of these type of lineage tracing tools. For the most part, the writing and figures are clear and informative. I have five major concerns listed below.

1) The provocative title in the form of a question is somewhat misleading – is the answer yes? The manuscript doesn't explicitly answer this question. I would suggest a more accurate title, for example "design specifications for more accurate CRISPR recorders."

2) I have two concerns with the term "accuracy."

First concern: The authors should be explicit upfront about their definition of the term accuracy, which includes both false positives and false negatives. I would argue that false positives (wrong branchpoints) are worse than false negatives (i.e. missing branchpoints). Can't an "accurate" tree have missing branchpoints but no wrong branchpoints? The authors briefly describe this distinction, but only at the very end of the Results section and then calculate these subscores of "accuracy" only for the SOLID sequencing approach. I would appreciate a longer discussion of this definition and scoring at the beginning of the results, and FP/FN calculated and reported for all simulations.

Second concern: Generally speaking, how accurate do we need CRISPR recorders to be? The authors set a high bar: complete and accurate lineage tracing of a 65,000 cell tree. Is 4% or 14% (the final "scores" given to MEMOIR and GESTALT) good enough for many scientific applications? It is certainly better than nearly all existing lineage tracing techniques, from which we have learned a great deal about biology. I would appreciate a discussion of why 100% complete and accurate trees are such an important goal, and what we can still learn from less accurate trees.

3) I am concerned about three library prep or filtering steps in the sequencing of the Drosophila target site array that are not clearly explained in the text, which may reduce the number of character states used in all following simulations:

a) To call character states – why only use 9bp flanking the target site instead of simply aligning each read to unedited sites? I would assume that this would eliminate some character states.

b) If I understand Figure 4A, the authors use a primer that sits directly on the PAM -mutational outcomes that disrupt any bases within the PAM presumably would not be captured by the PCR and sequencing. Can the authors discuss the impact of this?

c) Why merge 140 rare character states into a shared state (state 60)? This would obviously lead to tree errors. Why not treat these just as all other character states? The authors write that this was "for convenience," but I'm not sure why this is convenient and it seems to be a potential source of false positives.

I believe other papers have shown a higher number of potential character states, and I'm concerned these steps listed above may impact the simulations.

4) The authors, as they admit, use "the most pessimistic estimate" of the frequency of dropouts. It is entirely possible to have two cuts within a cell cycle result in two edits instead of a dropout. Have the authors considered explicitly using their own experimental data (even with library prep caveats), or the GESTALT data, to simulate dropout rates? Since this assumption dramatically impacts accuracy, it would seem important to be careful about how to model dropouts.

5) Choice of tree reconstruction algorithm matters. In their own simulations, Parsimony appears more successful that Neighbor Joining (Figure 2—figure supplement 1). However, this was never stated explicitly in the text, and there is no discussion of algorithm selection and its impact on accuracy. While NJ was selected for obvious reasons (speed), the authors should provide a clear discussion of other options and their impact on tree accuracy.

Minor Comments:

1) GESTALT cell culture approach also used a similar strategy of an array of off-targets and 1 guide RNA, and should be cited when discussing the fly array design, along with the caveats associated with this approach (poor editing at many off targets).

2) The MEMOIR paper extensively considers accuracy of tree reconstruction, including comparisons to reference trees. These data and discussions should be mentioned and referenced in this paper.

Reviewer #3:

In this manuscript, Salvador-Martínez and Grillo et al. present a simulation study of newly developed CRISPR lineage tracing technologies. The authors do a good job of setting up the problem, explaining their choices of various parameters and assumptions, and adding experimental data in Drosophila to reinforce these choices. This work will be a valuable addition to a quickly advancing field, particularly as a reality check on the extent of organismal engineering that will likely be required to achieve near-complete, accurate trees by this class of methods. Our first major comment is about the tone of the paper, while our our additional major comments primarily relate to alternative measures that should be evaluated that strike more of a balance between strict accuracy and the general conservation of tree topology. Additionally, some basic flaws in the experimental design and analysis of editing outcomes in Drosophila should be addressed before publication.

1) A first major comment is that the measure of accuracy used throughout the paper is very conservative, and more generally the tone that is struck in many parts of the paper is (we feel) overly conservative. Although strict accuracy and completeness are of course goals worth shooting for, they are not prerequisites these kinds of experiments to achieve biological insights. For example, lineage relationships between cell types might well be accurately inferred from the general topology of a tree that contained inaccuracies or uncertainty near its tips. For any new technology, proof-of-concept studies are just that -- proof-of-concept, and it's always been clear that significant additional engineering would be (and still is) required to maximize the value of these methods. This point does not detract from the value of the simulations presented in this paper. A more optimistic take on the same results is that it is possible to reconstruct large trees with reasonably high accuracy (great!), but it will require the introduction of at least 50 targets (and ideally several hundred targets), tuning of the mutation rate (although the broad plateau presented in Figure 2D is rather encouraging), and careful consideration of variable cell division rates. These conclusions and other analyses presented in the paper provide important guidance for the field (and a reality check against short term thinking), but the paper often slips into a negative tone that in our view is inconsistent with the results themselves (e.g. the fact that conditions are identified where reconstruction with 99% accuracy is achieved; subsection “Optimising cell lineage reconstruction for in situ sequencing with 2, 4 or 16 character states” paragraph six). We urge the authors to: (a) make it clearer, from the beginning of the paper, the extent to which accuracy as defined here is a highly conservative definition, relative to what might be required to achieve biological insights from trees reconstructed from GESTALT or related methods. (b) strike a more balanced tone, with less emphasis on what is not possible using the systems as reported in their proof-of-concept implementations, and more emphasis on the path forward, i.e. the extent to which further engineering (more targets, reducing inter-site deletion, tuning of mutation rate, etc.) is required to get the most out of these methods.

2) The simulation of CRISPR-based lineage tracing technologies in the first section (Figure 2) focuses on accuracy with Robinson-Foulds, but should include characterization with the clonal reconstruction measurements (FP / FN analysis). These measurements are used later in the MEMOIR simulation section, and many people will be interested in this use of lineage tracing technologies for this purpose. A mention or comparison to other distance metrics might be more appropriate, see https://www.ncbi.nlm.nih.gov/pubmed/21383415 or the review https://www.ncbi.nlm.nih.gov/pubmed/25378436

3) You show higher accuracy with maximum parsimony approaches, but use neighbor-joining throughout the paper. A strong justification of this choice is important, as this appears to be a strong bias against the methods you're evaluating.

4) Robinson-Foulds is a distance metric, and here you've normalized it to an accuracy over [0-100%], which is not detailed anywhere in the paper. Details in the Materials and methods section would improve the clarity of the paper.

5) Counting 9mers is a bit liberal for determining editing outcomes from the FAST target sequencing. Given the known double-stranded break location and repair outcomes, most mutational outcomes should be centered at, or overlap the cutsite. By including all of the 9 proximal bases, the captured editing diversity will include sequencing errors and PCR errors. This shouldn't affect the overall profile of editing outcomes, but will increase the number of mutations, and should be mentioned. This is made apparent by the elevated mutation rates in the untargered column of Supplementary Table 1 in Supplementary file 1, as some of the more active off-targets have changes in bases believed to strongly obstruct Cas9 binding (bases that are very close the PAM sequence).

6) Also the location of the primer (Figure 4) precludes find deletions that extend downstream into the PAM sequence. This eliminates the detection of mutations that extend 3' of the cutsite, and will deflate the diversity of editing you see. This is a major bias, and could also affect the FAST off-target results.

7) It's been shown that very large deletion frequency decreases with the distance between two cutsites (https://www.ncbi.nlm.nih.gov/pubmed/24907273). it would be worth including in the dropout simulations, or at least mentioning an alternative model with decreasing dropout efficiency at larger distances.

8) It would be good to characterize the accuracy of genotype collapsed trees (https://www.ncbi.nlm.nih.gov/pubmed/29474671) which aim to reduce the number of false branch points (branch points introduced by the tree bifurcation requirement, not mutations).

9) In the SOLiD simulation section (for Figure 7) it's unclear what sequence would be used for the primer, and how often that binding sequence would be obstructed by deletions in its target sequence. Some more details here would be helpful.

Minor Comments:

Fourth sentence of the Abstract should probably say approaches (you profile at least two).

Abstract: not all terminal branches are fully differentiated cells.

Introduction paragraph two: there's probably a better phase than “simple cases” (it was quite the effort, which you mention further on).

Introduction paragraph eight is a bit strong. Certainly simulations will inform future synthetic recording systems, but the assumptions and simplifications of simulation might prevent finding the optimal solution without more true biological validation.

Subsection “Optimising cell lineage reconstruction for in situ sequencing with 2, 4 or 16 character states” paragraph nine: shouldn't "double the number of reads per target" be "double the read length" or "double the number of cycles"?

Really beautiful figures all through the supplement, but the most minor change, add " + theme_classic()" or similar to the R command for Figure 2—figure supplement 1.

Additional details are needed in the experimental section about the PCR reaction.

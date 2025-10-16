# Peer review - Round 1

Editors:
- Dominique C Bergmann, https://ror.org/00f54p054 Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72601.sa0](https://doi.org/10.7554/eLife.72601.sa0)

Quantitative imaging has become a mainstay of modern cell and developmental biology. This article reports major advances in the image analysis software package MorphGraphX (MGX). MGX2.0 includes new tools for precise quantitation of cellular behaviors, such as cell division and expansion, within the context of positional information in the growing organs. This article is the go-to resource for current and future users of MGX to learn the power of the software package, with which they can quantify the spatiotemporal dynamics of the growth and development of living organisms.


---

# Peer review - Round 1

Editors:
- Dominique C Bergmann, https://ror.org/00f54p054 Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72601.sa1](https://doi.org/10.7554/eLife.72601.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "MorphoGraphX 2.0: Providing context for biological image analysis with positional information" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Detlef Weigel as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Roeland MH Merks (Reviewer #2); Naomi Nakayama (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) All reviewers agree that MGX2.0 is a powerful suite of tools that can be of use to many researchers in the plant and developmental biology fields, but all felt it is more appropriate for a "Tools and Resources" manuscript and suggest that the revision be submitted as such.

2) Even for a tools and resources manuscript, it would be nice to clarify what novel findings MorphGraphX can reveal with the new updates. Did you find something counterintuitive or previously unknown/unexpected because of the precision quantification? Did using these data result in different outcomes with a computational model, for example? Such an example will be a strong incentive for why these updates warrant another major publication.

3) More detail on how the data must be generated to make it suitable for use in MGX2.0, such as explicit parameters for input image quality, is required. MGX1.0 had fairly strict standards for input. Have these standards changed? Also, in the last 10 years, many post-acquisition programs exist to "clean-up" noisy image data (e.g. ilastik workflows). Are these packages compatible with MGX2.0?

4) Provide more clearly organized workflow overviews. It is impressive how many analysis tools are available, but so much information is overwhelming. Even as experienced users of MGX1.0, (Rev 1), it was challenging to follow what tools were being applied to what questions and tissues. To reach both beginner and expert MGX users, we suggest including a table that summarizes the approaches and applications described in the paper.

5) To help get users started with MGX2.0, (1) present the software availability more prominently along the software availability sections; (2) add to each figure a set of instructions/a protocol for reproducing the figure using MGX2.0 as part of the supplements. At least for one of these a highly detailed step-by-step set of instructions would be highly useful; the next figures could build upon these.

6) The Results section is challenging to read and needs some restructuring. Specifically (1) the figures are described out of order, and most figures are scattered in different main text sections. Consolidate the order of the information according to the messages of each figure or rearrange figure panels; (2) The basic procedure of the software use is introduced in the middle (Line 360-370), but this should be in the introduction or beginning of the results; (3) multiple organ and tissue types are juxtaposed in the examples, of making the text difficult to follow. Some context and background will be needed to flesh out why it's important to quantify specific morphogenetic events in the mutants or markers chosen as examples.

7) Please clarify the novelty of this report beyond the other publications on MorphGraphX in the past five years (e.g., Montenegro-Johnson et al., 2015; Montenegro-Johnson et al., 2019; Strauss et al., 2019).

Specific examples of these general points about organization and narrative are found in the three reviews. Please consider these specifics as you address the required changes noted in #1-#7.

Reviewer #1 (Recommendations for the authors):

Items that must be addressed

– Image quality required. It is unclear whether there are any changes in regard to the input data (image quality/step size) required for the processes described. Even if there are no changes it is unclear for those new to using MorphographX and could lead to disappointment. A short paragraph on input data would be of great help.

– Tomato meristem. The paragraph about auxin in tomato meristems (line 299-308) is confusing and could do with some clarification. The conclusion is too strong for the data presented. The authors should either rephrase OR present experiments in which manipulations took place OR cite previous work that adds to the presented data.

– Workflow overview. The paper provides a great overview of new workflows introduced in MorphographX 2.0. Because there is so much information, it can be overwhelming. We suggest including a table that summarizes the approaches and applications described in the paper. This would allow beginner and expert users to see all that is on offer in an efficient way.

Items recommended to take into consideration

– Intended audience. We are assuming the intended audience are plant biologists that either have experience using MorphographX or are interested in using the software in the future. With that assumption it would be useful to clarify some terms as they might be unclear for readers. Such as Bezier splines/surface. In addition other sections provide detail that is confusing rather than clarifying (eg line 775-795 will cause many readers to get lost just before reaching the end of the story).

– Central story. One of the strengths of the story is the many different tissues used in the story. However, this also sometimes hinders the coherence/flow. We realize this is probably not realistic for this story but for future stories the authors could consider picking one central story to revisit at the start of each section before diving into other tissues/applications.

– Segmentation. There are many new functions in MorphographX 2.0, how did any previously existing applications change? Most importantly, did the segmentation/merging change at all? Manual correction of segmentation errors is the most time-consuming step for many casual users.

– Figures/story structure. Figures and story don't use the same story structure which gets confusing in the first half of the story. The story only partially discusses figures at first and then gets back to them with one section moving between figures 2, 5 and 4 and the next section discussing parts of figure 3. For the reader this is confusing as (1) when first encountering the figure they might try to understand the figure as a whole, thus viewing all the panels while only several are discussed and then (2) they are later directed to jump between figures+pages to follow the story which is quite impractical. There is no simple solution, but we encourage the authors to consider either restructuring some earlier figures.

– Plot axes. Putting the dependent variable on the x-axis of many of the plots is visually pleasing and matches the orientation of many samples. But it can be confusing to many readers who are used to seeing the dependent variable on the y-axis.

– Advanced geometric analysis. This section if the least coherent and most difficult to follow. Obviously, there are analyses that cannot have a whole section that should be discussed. A short introductory sentence in this section might help make that clear so readers are not looking for logic that is not there. In addition, some of the paragraphs should be shortened or rewritten. They are currently both long and confusing.

– Exploded views/3D visualization. The paragraph describing 3D visualization (line 683-699) describes difficulties with 3D visualization and possible solutions. From the text it's not entirely clear how this works in MorphographX 2.0. Can certain bundles of cells be unselected/made invisible when navigator/exploring segmentation? What are the limits of these approaches? Exploded views might work great for young embryos but less well for larger tissues.

– Comparison to comparable software. MorphographX 2.0 is a great tool. It would be great to have its applications/strengths (discussed in line 762 onwards) put into context compared to other similar tools (Ilastik, etc).

Additional questions we had about the authors visions. These do not need to be addressed for the paper to be meaningful, but they were questions that immediately came to mind when reading this. If the authors want to add to the nascent sections describing future applications, below are some things that may be of interest to a plant development audience.

– Cells as nodes in networks. This is touched upon and sounds interesting. Do the authors imaging visualizing cell networks in cytoscape? In addition to the one story mentioned, do you imagine other applications?

– Positional + gene expression data. The importance of positional information in addition to other large datasets such as expression data is mentioned several times. How do the authors imagine that this information could be integrated in the future?

Reviewer #2 (Recommendations for the authors):

To help get users started, it would be helpful to (1) present the software availability more prominently along the software availability sections; (2) add to each figure a set of instructions/a protocol for reproducing the figure using MorphoGraphX, e..g as part of the supplements. At least for one of these a highly detailed step-by-step set of instructions would be highly useful; the next figures could build upon these.

I am a Mac user and have not been able to download and try the software yet, so perhaps instructions are in the source code package.. However,. I tried clicking the "Get Help" link on the MorphoGraphX main page, but the link is broken. In any case it would help if it is more clearly communicated to readers that they can do all of these cool analyses themselves, and give them instructions or directions to step-by-step instructions for performing the analyses themselves.

Reviewer #3 (Recommendations for the authors):

It is a manuscript with beautiful visual figures, reporting a widely useful open-source image analysis tool. However, I strongly recommend that further improvement before publication especially around the below points.

1) I found the Results section confusing – restructuring would be helpful.

– The figures are described out of order, and most figures are scattered in different main text sections. Can you consolidate the order of the information according to the messages of each figure? Perhaps the figures should be rearranged?

– The basic procedure of the software use is introduced in the middle (e.g., information in Line 360-370 should be in the introduction or at the beginning of the results?).

– The Results section illustrates multiple types of organs in a juxtaposition. This makes it a little difficult to follow. At least include enough information (e.g., what is bdl, DR5, etc.) for the particular cases of the development of these organs so that the readers can appreciate why it is important to quantitate specific morphogenetic events in these mutants or with these markers.

2) What is the article type? The manuscript does not seem to report a major new finding of a biological phenomenon; hence, it is more suitable as a tools and resources paper rather than a research article?

3) Even for a tools and resources manuscript, it would be nice to clarify what novel findings MorphGraphX can reveal with the new updates. Did you find something counterintuitive or previously unknown/unexpected because of the precision quantification? Did using these data result in different outcomes with a computational model, for example? Such an example will be a strong incentive for why these updates warrant another major publication.

4) Please clarify the novelty of this report beyond the other publications on MorphGraphX in the past five years (e.g., Montenegro-Johnson et al., 2015; Montenegro-Johnson et al., 2019; Strauss et al., 2019).

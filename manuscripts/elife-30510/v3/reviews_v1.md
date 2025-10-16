# Peer review - Round 1

Editors:
- Jay Rajagopal, Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.30510.018](https://doi.org/10.7554/eLife.30510.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Automated cell type classification in intact tissues by single-cell molecular profiling" for consideration by eLife. Your article has been evaluated by a Senior Editor and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

While all three reviewers agree that the techniques presented in this manuscript are valuable to the community, all three note there is no substantive biological advance in terms of new knowledge. Furthermore, the imaging data requires improvement as below and low-level transcript detection might add to this paper that should be published in a methods journal. Additionally, novel markers and their expression pattern should be described even in a methods paper.

Reviewer #1:

In this study, Nagendran et al. validate the use of an improved version of RNA in situ hybridization that they name PLISH, which utilizes rolling circle amplification rather than the proprietary amplification procedures commercially available (i.e. RNAScope, ViewRNA, etc.), thus providing an accessible tool for the broad scientific community. They demonstrate sensitivity and specificity of PLISH, as well as an application in tissue as opposed to only cultured cells.

However, they make many claims that are not supported by the data and are not particular improvements on previous technology. For example, PLISH puncta in tissues are not on par with IF, and do not offer any subcellular resolution. They go on to use a clever approach to multiplexing and image analysis that overly complicates the presentation of a few data points attempting to mimic the computational approaches necessary for scRNASeq data. The novelty suggested in the cover letter with regard to new cell types is not reflected in the manuscript or the data.

This work is much better suited to a methods journal, as there is no exploratory work, and only validation and confirmation of what was already known. Overall, PLISH seems to be a poor-man's RNAScope/ViewRNA/etc… without the commercialization and therefore cost. While this is a great thing, some of the technical terms thrown around seem to be an attempt to differentiate PLISH from technologies upon which it is only building, not pioneering.

1) Pixels in tissue images look highly saturated/blurry, even DAPI – why?

-Does not help support claims of superior resolution/is not subcellular.

2) PLISH gives puncta, as described, in cells, but looks like weak IF in tissues with no clear subcellular resolution (which is a major claim in the Introduction).

3) Scale bars need to be in every separate image, especially in diseased vs. normal e.g. Figure 2.

4) Dotted lines outlining relative structures, such as basement membrane/lumen, would make it easier to follow.

5) Define "technical terms" if this is to be "biologist friendly" – "imager oligonucleotide" is not clear without a search in the Materials and methods. Workflow in Figure 4 is not readily apparent or obvious. As a major aspect of PLISH, this would be easier appreciated if described more thoroughly.

6) Usage of terms like "barcode" and "imager nt" make something that is not complex much more complicated and "jargon-y" than necessary. "RCA followed by hybridization of a fluorescently labeled nt probe" would be much simpler.

7) The inclusion of number of cells (2900) and visualization of the data in tSNE plots deceivingly equates PLISH to a sequencing approach, rather than a standard snapshot visualization tool.

8) Higher mag images are needed for Figure 3A-C to support the claim that this is "on par with IF" – the current images are not on par with IF and hardly support the presence of a putative BASC, while the IF in Figure 4—figure supplement 2E is much clearer.

9) Figure 3DE – what is the "other"? How does is fit in with what we already know, since these are a set of well-characterized genes? Should rework the text/figure in 3D to better lead into the application of this aspect of PLISH in Figure 4.

General comments:

Overall, this is a highly technical paper that defines a tool. The authors clearly realize this, as they have filed a patent on PLISH. The concept is interesting and its application has great potential, yet it is not as excitingly novel as the text implies. While indeed an improvement on current technologies, this is fit for a methods report rather than a scientific article. The data are confirmatory rather than exploratory, and serve mainly as tool validation.

The focus on BASCs does not help the authors' case, as these are a controversial cell type not found in humans, and the IF images were more convincing than the PLISH data.

If the authors tackled more profound and subtle questions with PLISH, and in human samples (such as identifying the human BASC), then this would be less a tools paper and more a scientific article.

Finally, the overall tone describing this technology is overly ambitious and exceedingly strong. While this is fantastic work at method development and optimization (as well as creating accessibility), it falls short of being an original research article. The cover letter overstates the novelty.

Reviewer #2:

This manuscript tackles an important question: how to obtain spatial information about RNA expression in a high-throughput fashion. It presents a technique the authors call PLISH which is an improved variation of the "in situ sequencing" technique published in 2013. The manuscript convincingly demonstrates that in cultured cells the PLISH technique can detect a variety of transcripts which are expressed at different levels and that PLISH detection levels correlate extremely well with FPKM values obtained by RNA-seq. In addition, they provide proof-of-principle that in tissue sections their technique can be used in a multiplex fashion to detect highly-expressed transcripts with very good specificity e.g. the blocking of the Scgb1a1 signal by antisense oligos, but not scrambled oligos, in Figure 1F is very impressive given how highly Scgb1a1 is transcribed.

Beyond Figure 1, the additional experiments presented all show that the PLISH technique works well in mouse and human lung sections (which are complex tissues) when highly-expressed mRNAs are detected.

However, no biological insights are presented. For example, Figure 2 shows that the technique basically works in formalin-fized paraffin embedded human samples using extremely highly expressed transcripts, but these results had previously been obtained by immunostaining so no biological insights are presented. Note: the cell shape changes that are described in the text for SpC+ cells are not visible in the image on the merged pdf.

The analysis of adult mouse lungs – Figures 3 and 4 is a bit disappointing. This is solid proof-of-principle that the PLISH technique works. However, these transcripts are all highly expressed – no real biological insights are gained at all here. To publish in eLife I would at least expect to see low level transcripts detected, or some new biology, in addition to the proof of principal work shown here. No prior evidence springs to mind as to what the 2 types of club cells could be – prox and dist, but this change in B-actin could be purely structural to do with cell size/shape in different parts of the airways.

"Proper" analysis of a tissue section using probes to transcripts that are thought to be expressed at low levels, in addition to highly expressed genes such as Sftpc, is required. Plus some biological insight.

Reviewer #3:

The present study by the Desai lab shows the development of a proximity ligation in situ hybridization technology and its use to examine various cell type markers in the mouse and human lung. The technique appears to work well and if employed correctly could enhance studies on human tissue samples where histology is possible but isolation of single cells is limited. One limitation of the current study is that it does not extend our understanding of lung cell heterogeneity as most if not all of the markers examined have already been extensively characterized in the lung.

1) Much of the histology shown is at far too low of a magnification to assess the patterns of expression. The authors should provide high mag pictures in all situations, especially for the alveolar region as it is difficult to assess where the positive cells are located. Use of 3D reconvolution (i.e. IMARIS) would be helpful.

2) It would be nice for the authors to show data from some new novel markers that were isolated from the current study. This would provide novel insight into how this technique has advantages over other techniques.

3) A lot of the co-staining is difficult to assess. These data may be helped by higher mag imaging.

4) In the scRNA-seq experiment, was this done on whole lung cell suspension or Epcam+? It is not mentioned in the paper that I can see.

5) Many of the figures need better annotation. It’s very hard to interpret what some of the panels are trying to convey.

# Peer review - Round 1

Editors:
- Mohan K Balasubramanian, https://ror.org/01a77tt86 University of Warwick United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76249.sa0](https://doi.org/10.7554/eLife.76249.sa0)

This manuscript reports important quantitative results on cytokinetic nodes using fission yeast as a model. Using an Airyscan microscopy the authors develop images with ~ 140 nm resolution and estimate ~ 190 cytokinetic nodes per cell prior to actomyosin ring assembly. The work also describes important conclusions on scaling parameters, all of which will help refine quantitative models of cytokinesis.


---

# Peer review - Round 1

Editors:
- Mohan K Balasubramanian, https://ror.org/01a77tt86 University of Warwick United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76249.sa1](https://doi.org/10.7554/eLife.76249.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "The number of cytokinesis nodes in mitotic fission yeast scales with cell volume" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Dimitrios Vavylonis (Reviewer #3). The Reviewing and Senior Editors were not involved in the peer review, but oversaw the discussions and drafted the final letter.

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

There was a great deal of enthusiasm from all three Reviewers and the editors for a compelling and quantitative elucidation of aspects of cytokinesis and in particular quantitation of cytokinetic nodes. However, three major concerns have been raised about 1. the concept of unitary nodes and the differences between the dimmer cytosolic spots is unclear and some pitfalls in the approach and interpretations were raised. Furthermore, as in the attached files that Reviewer 1 has prepared based on the raw data, there is concern about counting errors and how the cytosolic fluorescent spots are differentiated from membrane localized "unitary nodes". 2. The extent of broad interest in the work beyond the fission yeast community and 3. the somewhat unclear epistasis between cdr2, pom1 in cytokinetic node establishment and how these relate to mitotic nodes.

In addition to the specific comments reproduced verbatim from the three Reviewers, the following issues were raised during the discussion between the Reviewers and RE.

We all have now looked at Reviewer 1's files, as well as the raw data provided by the authors. We all agree that the unusual intensity fluctuations of the background should be discussed. From this analysis, it seems that roughly, 8/10 ROIs would correspond to what we can reliably call nodes (being close to the membrane and stationary structures with signal over several z slices). But 2/10 ROIs seem to be in the cytoplasm. This observation could imply some counting errors (not sure how much, maybe 20%?). Then there is the separate issue of possibly *not* counting bright nodes because they may have considered them not to be unitary (they say "We searched for dim spots" on line 680).

Reviewer #1 (Recommendations for the authors):

Cytokinesis nodes are plasma membrane-associated assemblies of multiple proteins including myosin-II and play key roles in fission yeast cytokinesis by nucleating actin polymerization at the cell equator and promoting assembly and contraction of the contractile ring. However, due to technical limitations, a definite count of cytokinesis nodes has been missing. In this manuscript, Sayyad and Pollard employed Airyscan confocal microscopy, which allows live fluorescent observation with higher spatial resolution than spinning disk confocal microscopy, and detected cytokinesis nodes in a smaller size than previously observed using Blt1-mEGFP as a marker. They coined these dim spots they detected "unitary nodes" and claimed that they are the basic units of the cytokinesis nodes and the previously reported nodes are their assemblies.

There are problems in the analysis of the data from the Airyscan confocal microscopy. The definition of the new terminology "unitary nodes" is unclear. As seen in Figure 2A, dim fluorescence spots are detected throughout the cell. Although they are in general dimmer than the "unitary nodes" marked by dotted circles, some of them are comparable. This is not simply due to the artificial impression of overlapping signals by the maximum z-projection, as confirmed by 3D perspective view of the original data NodeBroadband.czi (overview.mov generated by annotate_nodes.ijm script, refer to the blue arrowheads in summary PDF, in eLife's dropbox: https://www.dropbox.com/sh/gbay207esrvzs78/AADramgOx_7Q0oUck8kmoiexa?dl=0).

The difference between the dim "unitary nodes" and the cytoplasmic dimmer spots is not obvious. Indeed, 2 out of 10 ROIs on the sample image provided by the authors reside slightly inside the cell, clearly not on the cortex or cell membrane as the others do. These non-cortical spots are inconsistent with the widely accepted picture of the cytokinesis nodes. Spots with similar intensities can be found throughout the cell, including the polar regions. In summary, according to their intensities, there are at least three classes of Blt1 spots (1) dimmest spots found everywhere, (2) the dim spots on the equatorial cortex ("unitary nodes"), and (3) brighter equatorial spots observable by spinning disk confocal microscopy (conventional nodes). However, distinguishing between the class 1 and class 2 spots doesn't seem to be trivial and has not been sufficiently detailed in the current manuscript.

It is also unclear what the authors' interpretation of the class 1 spots is. They look different from typical background signal, which is usually derived of rapidly diffusing GFP-tagged molecules, cleaved free GFP molecules, or other endogenous molecules (auto-fluorescence), and appears noisy but largely uniform with some temporal and spatial fluctuations. The class 1 spots could be artifacts of Airyscan microscopy or real Blt1-GFP signals that represent the monomer or assemblies in a smaller size than the "unitary nodes" (class 2 spots). If the former was the case, this would raise a question about the nature of the class 2 spots, the dimmest of which are comparable to the brightest of the class 1 spots. If the latter was the case, the authors would need to explain how they remain sufficiently immobile during image acquisition and reconsider the appropriateness of their method of background subtraction. This would also question the suitability of the word "unitary". In either case, clearer and more objective criteria for distinguishing between class 1 and class 2 spots, which can ideally be executed by automation, should be provided.

The term "unitary nodes" contains strong implications that this is the basic, indivisible unit of the nodes and that the brighter nodes are the assembly of them. In Figure 2D, a histogram of their intensity distribution and the Gaussian fitting to it were displayed as supporting evidence for their monodispersity. However, a statistical test for normality is missing. A proper test such as the Kolmogorov-Smirnov (K-S) test and the Shapiro-Wilk test is necessary.

One of the possible criteria for the "unitary nodes" would be the localization at the cell cortex as the authors implicitly assume. An appropriate marker for the plasma membrane or the cell wall would provide a solid reference for this.

To clarify the points raised above, 3D distribution of Blt1 was reconstituted from the provided data, NodeBroadband.czi, by a custom ImageJ/Fiji script (annotate_nodes.ijm script) and exported as 'overview.mov'. The signals that are comparable to the 'unitary nodes' and slightly brighter than the dimmest cytoplasmic spots can be found in the polar regions as well (blue arrowheads in summary.PDF). 10 ROIs in Node_RoiSet.zip were marked by color. The 3D reconstruction of the equatorial broad band region (nodes.mov) and its maximum y-projection (projection along the long cell axis, nodes_max_prj.tif) indicate that 2 of them (magenta) are not on the cell surface. Please find these files at https://www.dropbox.com/sh/gbay207esrvzs78/AADramgOx_7Q0oUck8kmoiexa?dl=0.

The FFT of an image depends both on the microscope and the sample. To compare the abilities of different microscopy techniques, ideally, the same sample should be observed. The cells in Figure 1A (Airyscan) and 1C (spinning disk) don't look like the same cell. What does the diagonal line lowering towards the right in Figure 1B represent? A (dim) structure that exists only in the Figure 1A 'CR' not in Figure 1C 'CR'? Or, an artifact by Airyscan microscopy?

What are the magenta signals in Figure 1C?

Reviewer #2 (Recommendations for the authors):

This paper studies cytokinesis nodes, which are precursors of the cytokinetic ring in fission yeast S. pombe cells. The project addresses a timely question in the field, and the authors' data support their conclusion that the number of nodes scales with cell size.

Overall, the study fits with past work in the field and strengthens the model that node number scales with cell size. The conceptual advance beyond these past studies appears limited, and in several places the conclusions are not sufficiently supported by the data. I also have some concerns regarding the new method for estimating node number as discussed below.

Strengths:

1. In the Introduction and the Discussion section, the authors do an excellent job of comprehensively discussing previous studies that have investigated how nodes scale with cell size.

2. Several unexpected results reveal novel layers of node regulation that can be studied in the future. For example, nodes were more dispersed in small wee1-50 cells and size scaling of nodes was altered in wide rga4∆ cells. Since these two mutants are shorter that other cells examined, it suggests that some unidentified mechanism related to cell length is altering the known node regulatory system.

Weaknesses:

1. The paper mostly confirms previous studies that also showed node number scaling with cell size. The authors have done a nice job of using small and large mutants to increase the range of cell sizes beyond previous work, but the conclusion remains very similar. I would also note that some aspects of node positioning and density appear to break down at the extreme sizes – e.g. node distribution changing in small wee1 and rga4 mutants, and node density failing to scale with cell size in large cdc25-22 mutants. These exceptions seem potentially very interesting but are not explored.

2. Figure 2: I am concerned that the authors' new method for counting the number of nodes may not be accurate, which has implications for many conclusions in the paper. In short, the authors identify the dimmest population of Blt1-mEGFP nodes and define this population as "unitary" nodes. They then measure total Blt1-mEGFP fluorescence in mid-cell and assume that this entire fluorescence is comprised of unitary nodes. They suggest that brighter nodes are multimers of unitary nodes, but this assumption may not be correct based on many past studies in the field that have shown a range of node sizes. The authors even state "the fluorescence intensities of these spots ranged from very bright to dim" (line 142). Since all quantification in the paper relies on this assumption, it becomes a major caveat. In addition, Blt1 appears to be a peripheral membrane protein such that it might not all be contained in nodes. Can the authors be sure that the mid-cell region lacks diffuse Blt1 proteins that are diffusing around between nodes? Their signal would be attributed to unitary nodes based on the methods described. I don't mean to suggest that the authors' method is definitively "wrong," but rather it carries some heavy assumptions and caveats that leave me uncertain about the resulting data.

3. Figure 3: The authors show that the number of nodes scales with cell volume and with cell length across a range of sizes (except for rga4 mutant). Given that size involves many parameters including volume, length, surface area, etc, I am confused that the major conclusion and title of the paper specifies that nodes scale with "volume." Recent studies from the groups of Fred Chang and Martin Howard have shown a role for cell surface area as opposed to volume or length in node pathways. The authors may have missed an opportunity to extend their results by comparing and contrasting how nodes scale with different aspects of cell size/geometry. As presented, this major conclusion of the paper does not extend beyond previous studies and perhaps overstates the importance of cell volume, limiting the overall impact of the work.

4. Figure 3K: The authors conclude that node density in the cell middle does not scale with cell size. However, the graph appears to be driven by the elongated cdc25-22 mutant measurements. To my eye, it looks like node density scales with cell length in all other strains but then does not scale specifically in the cdc25-22 mutant. It is important because the authors' conclusion contrasts with previous studies in the field (e.g. Pan et al., 2014).

5. Figures 4-5: These figures examine how node number scales with Pom1 concentration using Blt1-mEGFP as the marker for nodes. However, the role of Pom1 on nodes appears to be through Cdr2, which is not imaged in these experiments. In addition, the earlier figures in the paper focused on mitotic cells whereas these figures and the role of Pom1 are on interphase cells. This combination makes it hard to connect results on Pom1 with the earlier results in the paper.

6. Figure 6: The authors conclude that when Cdr2 concentration is increased, it results in smaller cells and more nodes. However, the actual experiment shows that restoring Cdr2 expression into a cdr2 deletion mutant restores cell size and node regulation. I do not see data indicating that Cdr2 overexpression reduces cell size below wild type levels. Instead, the data support the expected conclusions for restoring the function of a deleted gene.

7. The authors conclude that Pom1 and Cdr2 do not act directly on cytokinesis node number but instead act indirectly by influencing cell size. This conclusion is confusing because nodes act to regulate cell size at mitosis prior to their role in cytokinesis. The authors discuss some of the pathways connecting these proteins to cell size in the Discussion, but it becomes confusing as interphase nodes and cytokinesis nodes are not fully distinguished in the discussion. If I understand their logic correctly, their main point is that interphase nodes controlled by Cdr2 and Pom1 do not influence the number of cytokinesis nodes later in the cell cycle. If this is correct, then I might suggest clarifying the text.

I found the logic of the Discussion section hard to follow at times. The authors make a number of interesting points but might consider consolidating some of their conclusions.

Reviewer #3 (Recommendations for the authors):

Using quantitative Airyscan microscopy, Sayyad and Pollard present detailed measurements of the number of cytokinetic nodes, the scaling of their number with cell size, as well as concentration of Pom1 and Cdr2. This work is a great contribution to quantitative studies of cytokinesis and more broadly to regulation of cell size. It's an invaluable resource for the development of mathematical models of cytokinesis and cell size regulation.

I am very enthusiastic about this work but I have a few comments to consider.

1) Node counting method. The counting of node numbers is based on calibrating the intensity of unitary nodes. This results in a number of nodes for WT cells that is considerably larger (~ 200) than earlier estimates, even by Laplante et al. who used single molecule super-resolution microscopy to measure ~140 cytokinetic nodes in cdc25-22 cells.

While Laplante et al. concluded that both WT and cdc25-22 arrested and released cells have the same number of nodes, in this paper (Figure 3H) as well as in Vavylonis et al. (2008), cdc25-22 cells were found to have more cytokinetic nodes as compared to WT. If the estimate of WT nodes in Laplante et al. needs to be revised downwards, to resolve this apparent disagreement, such a change would make the difference in node number counting between this paper and earlier studies even larger.

Evidence for unitary nodes comes the observed quantization of node intensities by Akamatsu et al. (2017) who fitted histograms of node intensities by multiple Gaussians. However, histograms with small number of data per bin show fluctuations that may appear as peaks, which change depending on the bin width. I am sure that Akamatsu et al. were very careful in their analysis, but I couldn't find how this issue of binning fluctuations was dealt with in their paper. The current paper does not attempt to reproduce the quantization seen by Akamatsu et al. (which could also have provided the intensity of unitary nodes).

Given the above comments, I am concerned that the intensity distribution of what are considered unitary nodes in Figure 3G might reflect the tail of a broader intensity distribution (representing a larger variation of node intensities whether unitary or not), which is cut off by a selection procedure. This might result in overcounting of nodes.

2) Is the microscope's PSF varying significantly along distance from slide, and if so, should this be accounted for when measuring the total intensity of the broad band through sum projection?

3) Scaling of nodes with volume versus area. The scaling of number of nodes with volume is emphasized in this work. However Pan et al. (2014) had reported that Cdr2 and cell size at division scales with surface area, see Figure 6 in that paper. I was confused on whether the measurements between these two papers are in disagreement or else if they reflect different phenomena. Could an area scaling be related to how cells such as rga4Δ that have different diameter deviate the most from the trend line in Figure 3H? (Incidentally, it's hard to observe different diameters between WT, rga4Δ and rga2Δ in the images of Figure 3B,D,E). Some explicit discussion would be helpful.

4) Use of unbiased statistical/data clustering methods might provide a more reliable unitary node calibration method. An alternative approach could be to be more conservative in terms of absolute node numbers and instead present the results in relative terms.

5) Figure 1 shows a comparison between Airyscan and confocal images to indicate the improved resolution of Airyscan. However, both of these images appear to have less signal to noise and resolution as compared to prior published confocal images of nodes with similar fluorophores. So the improvement in resolution is not superficially obvious.

6) The authors make the general assumption that unitary cytokinetic nodes are similar in terms of composition and stoichiometry. Can the authors discuss the implications of this assumption through the paper? For example, do all Blt1 nodes become cytokinetic nodes and how is stoichiometry preserved when Cdr2 concentration is varied (is the Blt1 to Cdr2 ratio in nodes constant?).

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting the paper entitled "The number of cytokinesis nodes in mitotic fission yeast scales with cell volume" for consideration at eLife. Your article and your letter of appeal have been considered by a Senior Editor, BRE member (Mohan Balasubramanian), and three Reviewers (including Dimitris Vavylonis). We regret to inform you that we are upholding our original decision. The Reviewers have put in an enormous amount of time in evaluating your rebuttal letter as well as looking closely at the primary data.

The Reviewers and editors are enthusiastic about the new approach of using Airyscan to investigate node architecture, properties, and scaling. However, the Reviewers have raised many similar questions, which require new experiments and / or analysis of existing data.

Should you be able to carry out the necessary experiments / analyses, eLife will be able consider the manuscript as a new submission (sent to the same three Reviewers).

Please find below the comments made by the Reviewers to your rebuttal letter and the revised manuscript.

Reviewer 1:

I have read the authors' rebuttal and remain concerned about limited impact and significance of the work. I was unable to access the revised manuscript, which is referenced in the rebuttal letter, but the changes and responses seemed clear from the point-by-point response. There are 3 main concerns that are unchanged from the initial submission (and I would also note that the authors did not really address several of my other comments).

1. The authors have measured total blt1-mEGFP signal in the cell middle, and then assumed that all of this signal is comprised of single, unitary nodes. Based on this assumption, they estimate the number of nodes in the cell middle. This approach relies heavily on two major assumptions: (a) that all blt1-mEGFP signal is contained in nodes, and (b) that all nodes are the same size. The important concern is that the authors have not in fact counted the number of nodes, but rather they have estimated their numbers based on a method that relies heavily on assumptions. A major claim in the paper is improved node counting over past publications, but there appear to be just as many caveats in the methods in the current paper as in past publications.

2. Regardless of differences in the methods of counting, the current paper reaches the same conclusion as past publications: node number scales with cell size. Node number scaling with cell size is an interesting correlation that fits with past publications, but the functional significance of this scaling for cytokinesis is not investigated limiting the impact of the work. Do large cells need more nodes to form a functional cytokinetic ring? What are the differences in assembly of a cytokinetic ring formed by fewer nodes (i.e. small cell) versus a ring formed by more nodes (i.e. large cell)? Without functional investigation into this scaling, the overall impact of the work is limited.

3. Several pieces of data show that node number and node density do not simply scale with cell size. rga4 mutants do not scale node number with cell volume compared to wild type, and cdc25-22 do not scale node density with cell volume. The fact that these mutants break the scaling properties means that nodes do not simply scale with cell size. To extend beyond the previously published conclusion that node number scales with cell size, the authors could have investigated why these mutants lose scaling and what is means for cytokinetic ring assembly. Without such investigation, the impact of their work is limited to supporting past conclusions on these structures.Reviewer 2:

I read the paper and modified my review as follows. I have included a dropbox link to an image (that could be provided through eLife dropbox link, thought it doesn't matter since I have provided my name).

The authors have addressed many of my questions and the paper is now much clearer in terms of the assumptions underlying this work. I am still however similarly concerned regarding the node counting method.

The identification of dim nodes as unitary ones, as the authors describe in their response, relies heavily on the findings of Akamatsu et al. who reported quantization of node intensities.

For example, it is stated on line 180: "We interpret the dim nodes as unitary nodes, while the brighter nodes consist of two or more unitary nodes" and on line 707: "We searched for dim spots and marked their 708 X-Y positions. Then we inspected the fluorescence along the Z-axis at these X-Y positions in 40 Z- slices. To qualify as a unitary node, a spot had to satisfy two conditions: (1) the fluorescence of a spot was present within a circle 12 pixels (~0.5 µm) in diameter; and (2) the fluorescence of a spot was present in 7 or fewer consecutive Z-slices with a peak in the middle slice and diminishing towards both sides"

From these statements I understand that the authors did not include bright nodes in the intensity distributions (such as in Figure 2D), even if they satisfied conditions (1) and (2) because these bright nodes were considered to be multiples of unitary nodes. I assume this is why the intensity distribution in Figure 2D does not have a long tail at high intensities, unlike the intensity distributions of Akamatsu et al. or Figure S6 of Laplante et al.

Now superficially, the number of data points in the histograms of Akamatsu et al. seem to me to leave some room for ambiguity with respect to interpreting the high intensity tail as integer multiples of unitary node intensity. To better illustrate this simple point, that may have been unclear in my first review, I attach graphs showing how 150 points (similar to the 138 node counts in Akamatsu) picked from a singly-peaked distribution may appear as multiple peaks as a result of fluctuations:

https://www.dropbox.com/s/suti2gz9ovgmfyw/histogram.pdf?dl=0

One could also argue that the fact that the width of intensity distribution in Figure 2D is comparable to its average indicates that the node size is not very tightly regulated, leaving room for other interpretations (for example node formation though nucleation and growth and a continuous size distribution with a long tail above a minimal nucleus).

Perhaps the authors could verify or critically reexamine the unitarity of nodes, which is so central in this work, in the light of the improved microscopy method. That may include quantifying brighter nodes (along the lines of Akamatsu) as well as the low intensity signal (such as measurements of signal to noise).

Reviewer 3:

I regret that I used the same pair of colors (green and magenta) in my summary.pdf for Blt1 and Sad1 signals, respectively, in the NodeBroadband.czi panel (top left) and for ROIs on the cortex and inside the cytoplasm, respectively, in the other panels. However, as clearly indicated in the PDF (The caption "Blt1 channel" + color coding of the ROIs in the ROI manager, i.e., ROIs "0032-0271-0078" and "0033-0285-0077" in magenta while others in green ) and in the ImageJ/Fiji script, to analyze the node positions, only the Blt1 channel was used. As in the maximum z-projection of the original stack overlaid with the ROIs defined by the authors ("rois_on_max_prj+sad1.png", to be shared via the Editorial office), all the ROIs defined by the authors are clearly distinguished from the two Sad1 peaks, which mark the spindle pole bodies. To make this point even clearer, the Sad1-RFP signals were overlaid in red on a 3D reconstruction as well ("nodes+sad1.mp4" movie, to be shared via the Editorial office).

In the rebuttal, as to the unitarity of the cytokinesis nodes, the authors refer to the FPALM analysis in Laplante et al. (2016). In principle, this technique can detect only a structure that is sufficiently immobile during the data acquisition. In Materials and methods of this paper, they wrote "Clusters of localized emitters distributed around the equator of the cells were manually selected from the reconstructed FPALM images into two different categories, face views and side views. Broad bands of nodes formed during prophase, and nodes remained stationary until node movements began during metaphase. For broadband nodes (prophase/metaphase cells), nodes were cropped from images reconstructed from 5,000 frames (25 s)." Neither clear criterion for the 'clusters' nor the raw data of FPALM was provided. Being immobilized within the small region (~100 nm) for a few seconds might be too selective. We can't exclude a possibility that smaller clusters resize on the cortex, though diffusing more rapidly than the level that can be recognized as 'clusters'.

In contrast, Airyscan can potentially capture smaller and moving clusters. Although it takes ~11 s or longer to scan a full volume of 22 µm x 22 µm x 6.8 µm (40 z slices), voxels close to each other can be completed in a shorter time (eg. < 1 s). Blt1 spots that are comparable to or slightly dimmer than those picked up by the authors as unitary nodes are found all over the cortex including the polar regions that were used as the background by the authors. Some of them were marked with blue arrows in my summary.pdf and their nature was questioned in my public review. However, this was not addressed in the rebuttal. No clear logic to treat them as just background was provided (although it might be described in the correct, revised manuscript).

As to the statistical test of Figure 2D

As stated in the paper, we used the D'Agostino-Pearson test which is more versatile and powerful than the Kolmogorov-Smirnov (K-S) test or the Shapiro-Wilk test for normality. Please see line #225

I can't make a definite comment on this as the revised manuscript is not available. However, if the authors are referring to the same sentence as the lines 209 to 211 in the original manuscript, this is not addressing my point about Figure 2D. This sentence is about Figure 2E, in which a test was done for the normality of the number of total nodes calculated as the ratio of the total fluorescence to the fluorescence per unitary node.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "The number of cytokinesis nodes in mitotic fission yeast scales with cell size" for consideration by eLife. Your article has been reviewed by 3 peer reviewers (with no conflict of interest in any way), and the evaluation has been overseen by a Reviewing Editor (not one of the three Reviewers) and Anna Akhmanova as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Dimitrios Vavylonis (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. Please note that we have taken the very unusual step of inviting a further revision, and please note that this round of revision will be final. We hope that all points will be addressed satisfactorily since the Reviewers have spent an enormous amount of time on the review on multiple occasions. If you prefer not address some of the points of the reviewers in full, please seek publication elsewhere.

Please note that 2 of the 3 the Reviewers have stated that your revised manuscript did not address the key points. I have looked at the comments and agree with the Reviewers that there are two major issues (along with some minor issues) that remain ambiguous and therefore affect the strength of your conclusions and the extent of advance. Although Reviewer 1 was satisfied, in further discussion they mentioned the following agreeing with the unresolved issue of background correction.

Reviewer 1 comment during discussion:

I was myself mostly satisfied because the new analysis of brighter nodes does not show a long tail. So I thought that this means there is a characteristic average Blt1 node size (which may be called a "unitary node") even if the distribution of specks at low intensities is not measured accurately.

However, there are caveats, as explained by your reviews and I don't know how to explain it any better. I further realize that my short statement regarding evidence for unitary nodes was too strong and probably incorrect. So I would just like to say in my review:

"The revised analysis in Figure 2D, which now includes brighter nodes shows that these nodes have intensities within a certain range. The average intensity of this distribution can be called a "unitary node" so this addresses the main concern I had."

The issue of background correction and its dependence on cell size (and a possible solution by Reviewer 3) seem important to address.

Essential revisions:

1. Please note that addressing the point # 2 raised by Reviewer 3 is essential for the strength of the conclusions and should be performed.

2. Please also address points # 2-7 by Reviewer 2. Although they seem numerous, I have gone through the list. Most of these pertain to giving more information, reanalysis of data and the use of the most appropriate statistical treatments.

Reviewer # 1:

The revised analysis in Figure 2D, which now includes nodes of all intensities, provides additional support, and is consistent with prior evidence, for unitary nodes, as explained in the response letter. This addresses the main concern I had.

I have a comment regarding the "dim specks" (that could possibly be cytoplasmic oligomers) mentioned in Response to Reviewer 3. The authors mention that these specks were not confused with the brighter unitary nodes. It was not clear to me if this is true because the dim specks did not satisfy the two node criteria (fluorescence within 12 pixels and 7 or fewer consecutive Z-slices with a peak in the middle slice), or else if their intensity was smaller than the first bin in Figure 2D, or both.

Reviewer #2:

In the previous rounds, we pointed out various problems in data analysis and the limited impact of the work. Unfortunately, these were not substantially improved in this version. As detailed below, it is unclear whether the scaling of the node numbers with cell size is real. Insights into the mechanism of scaling or into the functional role of this phenomenon on cytokinesis are still missing. Please refer to slides in my 'problems.pdf', shared here: https://drive.google.com/file/d/1CdsqS3PgZNmfpZvgD_p4ZL6Z5UL1VZJf/view?usp=sharing.

The authors' response to the Reviewer 1 (second round, I was Reviewer 3) prompted me to look into the background and the method of measuring the fluorescence intensity of the 'unitary nodes' more carefully. The fluorescence intensity of a small node was measured by the intensity in a circular ROI of 12-pixel diameter on the sum stack of 7 slices (3 below and above the target node). The background was corrected by subtracting the mean of the equivalent ROIs arbitrary set near the cell tip on the same sum stack. The fact that both the cell diameter and the cytoplasmic background are not uniform along the cell axis make the background correction highly unreliable.

1.Geometry of the cell

According to the trace of the cell periphery in "background_RoiSet.zip", the diameter of the cell near the cell tips, where the background was measured, is smaller (~2.7 µm) than that at the equator (~3.7 µm). A circular ROI of 12-pixel diameter in the sum stack of 7 slices corresponds to a cylinder of ~0.5 µm diameter and ~1.2 µm height. For a node at the top of the cell, the corresponding background volumes near the tips are largely outside of the cytoplasm (page1 of 'problems.pdf Geometrical problem 1). This underestimates the background intensity. On the other hand, for a node on the midplane of the cell, the corresponding background volume is entirely inside the cytoplasm (page2 Geometrical problem 2). This overestimates the background intensity. These effects are not negligible because the raw background intensity varies between 1000 to 2000 depending on the depth of the z-slices while the peak raw intensity of the nodes is 3000~4000 (page 5 of 'problems.pdf').

2.Variability of the cytoplasmic signal and measurement of the node intensity and the node number.

Apart from the granularity, the cytoplasmic Blt1-GFP signals in the cell in "NodeBroadband.czi" marked with "background_RoiSet.zip" and "Node_RoiSet.zip" show significant variation along the cell axis. This can be demonstrated both by reslicing the cell volume and measuring a circular ROI at the center of the cell (page 3 of 'problems.pdf') or by line-profiling in the sum projection of the central 7 slices (z=23~29, page 4 of 'problems.pdf'). In addition to the large fluctuation due to the cytoplasmic spots, there is a clear trend that the cytoplasmic signal increases towards the cell equator. To make the situation more complicated, the intensity drops in the region corresponding to the nucleus around the equator.

The intensity of the cylindrical ROI put on the empty space outside of the cell (z=1~7) is 770 +/- 30 (mean +/- SD) (page 6 of 'problems.pdf'). In the central 7 slices (z=23~29), the intensity of the background ROIs set by the authors (green) is 2010 +/- 360. This increases to 2740 +/- 480 closer to the equatorial (magenta, still outside of the broad equatorial band) and 3050 +/- 610 at the periphery of the nucleus (yellow). These are not negligible in comparison with the raw intensity of the nodes 4170 +/- 690 (min. 3280 ~ max. 5510).

The authors reasoned usage of the ROIs near the cell tip as the regions without brighter spots. However, this is not an ideal choice because the intensity for background correction should be taken from the region with a similar level of the background. The authors' method will systematically underestimate the background signal. If the background was measured near the equator avoiding the cortical signals such as the ROIs in the perinuclear region (yellow on page 6 of 'problems.pdf'), we would get the WT node intensity, in the worst case, ~50% smaller than those reported in the current manuscript. Using the background ROIs near the cell tips also introduces unnecessary uncertainty that might vary depending on the cells and on the positioning of the ROIs.

This problem becomes more serious when we compare the strains with different cell sizes. Consistent with the above observation, Blt1-mCherry in Figure 4B outside the equatorial band shows a rather constant decrease towards the poles. The gradient seems to be common across different strains (page 7 of 'problems.pdf'). This suggests that the bigger the cell size, the lower the background signal measured near the poles. This would result in a larger over-estimation of the total intensity of Blt1-GFP in the broad equatorial band in larger cells. Dividing this with the intensity per node, which is largely constant across the strains (Figure 3G), would result in the size-dependent over-estimation of the node number. In other words, the scaling of the node number might just be an artifact of the cell size-dependent under-estimation of the background.

An additional twist is the drop of the cytoplasmic signal at the equator due to exclusion by the nucleus. Although this effect might be less significant than the cell size-dependent drop of the background measured near the cell tips, its influence on different measurements should be checked.

2.1 What is the variety of the background in the same strain and across the strains? Provide the raw data.

2.2 How stable the current results are against the selection of the background ROIs closer to the equator in the wild-type or at the same distance from the equator for inter-strain comparison?

2.3 Check the influence of the drop of Blt1-GFP signal at the nucleus on various measurements

3.Dimmer spots on the cell surface

Criteria for the 'unitary node' by the authors are "To qualify as a unitary node, a spot had to satisfy two conditions: (1) the fluorescence of a spot was present within a circle 12 pixels (~0.5 μm) in diameter; and (2) the fluorescence of a spot was present in 7 or fewer consecutive Z-slices with a peak in the middle slice and diminishing towards both sides." However, these are not sufficiently specific for unanimously identifying the 'unitary nodes'. Near the spots hand-picked as 'unitary nodes' by the authors (or at an equivalent cortical position), there are spots that are significantly dimmer but satisfy these criteria (pages 8 to 13 of 'problems.pdf', 'Dimmer cortical spots, example' 1~6). The majority of them are brighter than the background signals (at least those in the volumes defined by the authors near the cell tips) (pages 14 and 15 of 'problems.pdf').

3.1 Why were they excluded from the node measurement?

3.2 Analysis in Figure 2 should be done, including these dimmer spots on the cell surface.

3.3 Whether the node counting based on the intensity of 'unitary node' is still valid needs to be reconsidered.

3.4 If the authors insist on excluding the dimmer spots, more strict (but reasonable and not arbitrary) criteria for the 'unitary nodes' should be provided (although, to be honest, I doubt the concept of 'unitary node', see below).

4.Statistical test for normal distribution

The D'Agostino-Pearson normality test uses the skewness and kurtosis of the distribution (https://en.wikipedia.org/wiki/D%27Agostino%27s_K-squared_test). It is not suitable to examine whether the samples are from a normal distribution or a sum of multiple normal distributions. As shown on page 16 of 'problems.pdf', with the simulated samples from combined two normal distributions (not normal as a whole), the D'Agostino-Pearson test fails to reject the null hypothesis of normality while the Shapiro-Wilk test properly detected the deviation from the normality and rejected the null hypothesis (R script in page 17 of 'problems.pdf').

The Shapiro-Wilk test and the Kolmogorov-Smirnov test were explicitly suggested in my first review (based on the above simulation, the Shapiro-Wilk test seems to be more appropriate for our case). I suspect that the authors might have obtained p-values < 0.05 with these tests, indicating that the distribution is not likely normal. This would provide another line of reason to doubt the existence of the 'unitary node'.

4.1 Provide the raw data behind Figure 2D and 2E including both the raw node intensity and the background measurements so that other people can examine them

5.Distributions of fluorescence intensities of small nodes in mutant strains

Although "The distributions of intensities Blt1 fluorescence of cytokinesis nodes were similar (around 2500 AU) in wild-type cells (Figure. 2C) and three of the experimental strains (Figure. 3G)." (line 292-4), none of the histograms in Figure 3G look like a normal distribution.

5.1 Why aren't they normally distributed?

5.2 What would they look like if the dimmer spots on the cell surface were included?

5.3 Provide the raw data behind Figure 3G-K so that other people can examine them

6.Unitarity of the 'unitary nodes'

The spots on the cell surface dimmer than the 'unitary nodes' hand-picked by the authors were indeed observed also in the FPALM image in Figure S2 of Laplante (2017). There were smaller clusters of emissions marked by arrows (pages 18 of 'problems.pdf'), which were excluded from the analysis without any reasoning.

Moreover, even within the data of the clusters that the authors believed to be 'unitary nodes', there is a clear sign of heterogeneity. The distributions of the numbers of emissions per cluster show a long tail, which contains ~30% or more clusters. This indicates that, in addition to the dimmer clusters that were not counted as 'nodes', there exist significant heterogeneities even among the hand-picked 'nodes'. It is not clear what "Nodes in the tail were seen only in long reconstructions (25 s), not in short reconstructions (5 s)." (page E5880 Laplante (2017)) means without the real data for the short reconstructions.

The concept of 'unitary node' might be supported if the brighter spots were able to be explained as integer multiples of unit intensity. In Akamatsu (2017), the authors argued that the distributions of fluoresce intensity of the interface nodes can be better fitted by multiple Gaussian distributions than by continuous log-normal distributions. However, the fitting was done by setting the amplitudes, SDs, and means for each of the Gaussian distributions as free parameters (9 or 12 parameters for 3 or 4 Gaussians, respectively). This is simply wrong since there must be restrictions both on the means and SDs. The mean and SD of the n'th peak (m_n and s_n, respectively) should follow m_n = m_1 x n and sd_n = sd_1 x square root of n. A simple comparison of the goodness of fit with the other distribution that has only a limited degree of freedom (the log-normal distribution has only 2 parameters) is non-sense. The comparison between the statistical models should have been done based on an appropriate estimator such as the Akaike information criterion (AIC) (https://en.wikipedia.org/wiki/Akaike_information_criterion). With a simulation https://www.dropbox.com/s/suti2gz9ovgmfyw/histogram.pdf?dl=0, Reviewer 2 raised a valid example of artificial appearance of multimodality from a log-normal distribution.

Considering all the points discussed so far, i.e.,

-Unexplained exclusion of smaller clusters in the analysis of FPALM data (Laplante (2017))

-The long tail towards the bigger clusters even among the selected '(unitary) nodes' (Laplante (2017))

-Inappropriate statistical analysis of the distribution of the intensity of the nodes with a long tail (Akamatsu (2017))

-The intensity of the spots picked by the authors as 'unitary nodes' from the Airyscan images doesn't seem to follow a normal distribution (Figure 2D and Figure 3G),

evidence for the 'unitary node' is pretty weak. We can't exclude a possibility that there is no such thing as 'unitary node' but the nodes are rather amorphous aggregates of proteins as illustrated on page 20 of 'problems.pdf'. A critical re-examination of the author's own past data must be done.

7.Nature of the dotty cytoplasmic signal

The authors responded, "The processing of Airyscan images increases the contrast of these dim inhomogeneities". It remains as a black box what image processing was done as the only information provided is "To increase signal-to-noise ratio and resolution, acquired images were processed by 3D Airyscan filter strength 7.0 with Zen Black software."

7.1 Clarify the principle of the filter with an appropriate reference and specify the parameter settings (Is 'strength 7.0' sufficient? What does this mean?)

7.2 Does this processing preserve the linearity of the fluorescence signal?

7.3 Why are the grayscale levels so small? Only a range 0 to <~30 in 0-65535 grayscale levels was used.

Reviewer #3:

The revised manuscript demonstrates a correlation between cell size and the number of cytokinetic node precursor structures. This conclusion supports and extends previous studies in the field. The strengths of the work are balanced by some limitations that have been expressed in earlier reviews and remain largely unresolved:

(1) The overall impact of the work is limited because it reaches the same conclusion as previous work. As the authors have pointed out, their current work moves beyond previous studies in two ways: (a) they examine these node structures during cytokinesis whereas previous studies examined them during interphase using different markers; and (b) authors have used cell size mutants to extend the range of sizes examined. However, the overall conclusion is the same as earlier work. It is also worth noting that several of the size mutants (wee1-50, rga4D, and cdc25-22) do not follow similar size-scaling properties, but these potentially interesting differences remain unexamined.

(2) The major conclusions of the paper rely on the number of cytokinetic nodes present in different cells, but the authors have not actually counted the number of nodes. Their methods for estimating the number of nodes rely on several tenuous assumptions and have raised concerns from all of the reviewers at each stage of review. It is not definitively known if Blt1 nodes are all the same size (referred to as 'unitary nodes' in the paper). It is also not known if all plasma membrane-bound Blt1 in the cell middle is contained in nodes, or alternatively if there is membrane-bound Blt1 diffusively localized in this region outside of nodes. Both 'unknowns' leave me concerned about the accuracy of the numbers presented. I would like to propose a potential solution to this problem. The authors discuss the improved ability of airyscan imaging to resolve unitary nodes within the broad band. They could use their high-resolution images to count Blt1 nodes from the same images, and then present these numbers as a 'proof-of-principle' that node number scales with cell size by 2 separate analyses (counting versus their current estimations). The counting method would underestimate due to areas with multiple, unresolved unitary nodes; but similar scaling should be observed. It would not be necessary to reanalyze all strains/images this way, but perhaps just wild type and some cdc25-22 cells to establish a similar scaling trend by both methods.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The number of cytokinesis nodes in mitotic fission yeast scales with cell size" for further consideration by eLife. Your revised article has been evaluated by Anna Akhmanova (Senior Editor), a Reviewing Editor (Mohan Balasubramanian), and the Reviewers. Thank you for sending the further revised manuscript, and we apologize for the delay in its review due to travel schedules of the editors and the Reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below. Please note that Reviewer 3 (an imaging expert with absolutely no conflict of interest) has invested an enormous amount of their time and raised many points mostly about data analysis and statistics that we would like you to answer. Since this paper is very strongly based on quantitative data analysis, addressing these concerns is essential to support the conclusions.

The authors expressed concerns about the reviews. Specifically, they "note that the critique from reviewer #2 has expanded for a third time to include not just questions about the paper under consideration but also published work from our lab and other groups". This remark does not accurately reflect the peer review history of this manuscript. The issues around the unitarity of the 'unitary nodes' have been a concern from the beginning. The possibility of the appearance of pseudo-multimodality from log-normally distributed data was suggested by Dr. Vavylonis upon reviewing the first rebuttal. In the second revision, the authors referred to Laplante et al., 2016 "we must emphasize that the strongest evidence for the unitary node concept comes from the FPALM super-resolution of Laplante et al. (Laplante et al., 2016) not confocal data.", instead of seriously reconsidering the reasonable possibility raised by Dr. Vavylonis. This prompted reviewer #3 to look into Laplante 2016 and Akamatsu 2017 more carefully and led to identification of an an issue common to the current work, i.e., dimmer cortical signals of 1/3~1/2 intensities (or a number of localized emissions) of the 'unitary nodes'. The authors' objection thus does not appear justified.

The authors' strategy to support the unitarity of the 'unitary nodes' is to distinguish the slightly dim spots from the 'unitary nodes' and combine them with the much dimmer cytoplasmic specks. However, as detailed below, their arguments are not sufficiently strong and appear subjective. Please note that a newly cited, recent paper, Bellingham-Johnstun et al. (2021), whose corresponding author is the same person as the first author of Laplante et al. (2016), carefully and reasonably avoided the term 'unitary node'.

Furthermore, there arises a new issue of data handling. The numbers of the various cell types analyzed for this version are different from those in the previous versions (WT: 24 reduced to 21, wee1:24 to18, rga2: 23 to ?, cdc25: 32 to 31, rga4: 18 to 17). There was no mention or explanation of this significant change while the new look of the distributions in Figure 3G was attributed to the change in the background correction.

Issue 1 Geometry of the cell

"The background fluorescence was 9% higher next to the broad band than at the tips of the cells, but subtracting this higher value reduced the average intensities per node by only ~5% and the total intensity of the node broad band by only 13%." (page 4 of the rebuttal)

This is quite different from what the reviewer measured and presented to the authors in the previous round. One would need to look at the raw data. Was the image data of a cell presented by the authors an exception?

Issue 2 Variability of the cytoplasmic signal and measurement of the node intensity and the node number

The reviewer pointed out the difficulties in handling the background signal (1) large fluctuation and (2) systematic decrease towards the cell tips.

The regions closer to the equatorial zone used in this version are better than the regions near tips, addressing the point 2 to some extent although, as was previously mentioned, the cytoplasmic signals are even higher in the perinuclear region next to the equatorial cortex.

To draw a conclusion that the fluctuation is small, the line scans were shown in Figure R2. The authors claimed that the signal along the cell edge (green) containing the nodes is much higher (51{plus minus}21 AU, mean{plus minus}sd) than the cytoplasm (14{plus minus}5 AU). This itself is correct. However, this doesn't support that the background fluctuation is small relative to the intensity of the 'unitary nodes' since the major peaks (60~90 AU) on the green profile in Figure R2B correspond to the clusters of the many 'unitary nodes' (please refer to page1 of problems2.pdf). The spot measured as a 'unitary node' (ROI 0025-0270-0044, arrow) corresponds to a minor peak of ~30 AU, which is comparable to the fluctuations of the blue profile. They brought the intensity of the clusters of 'unitary node' when discussing the intensity of individual 'unitary nodes' relative to the background fluctuation.

The authors tried to explain the difference between their claim and the reviewer's analysis "Our measurement of background fluorescence (blue curve, in Figure R2B) differed from the reviewer's analysis in two ways: (1) They did not subtract the background outside cells from the image, so the background intensity is higher in their analysis; and (2) their ROI extended outside the tips of the cell, where the fluorescence is lower." In addition to the above issue, both the remarks miss the point. As to (1), firstly, subtraction of the common background (outside of the cell) doesn't influence the comparison between the peak of the 'unitary node' and the fluctuation of the cytoplasmic background. Secondly, in the previous review, when discussing the mean levels of the cytoplasmic background, they were standardized with the background outside the cell set to 0 and the mean node intensity set to 1 and pointed out that the cytoplasmic background levels vary 33% to 64% of the mean intensity of the 'unitary nodes' depending on the location with large spreads. As to (2), the line ROI was simply set from one end to another end of the outline of the cell defined by the authors, which seems to be overlapping with the other cell on the righthand side.

Issue 3 Dimmer spots on the cell surface

A concern was raised about the criteria to spot the 'unitary nodes' by picking up just slightly dimmer spots observed next to the 'unitary nodes' on the equatorial cortex, which were not counted by the authors. The authors responded to this by measuring the dim specks that are found everywhere and are easily distinguishable from the 'unitary nodes' (~170 AU, ~15 times dimmer). However, the key point was how one can define criteria that distinguish those just slightly dimmer spots the reviewer picked up from the authors' 'unitary nodes'. This was because, if it was difficult, (1) this would question the concept of the 'unitary node' and (2) this would affect the average intensity of the 'unitary nodes' and hence the node counts. The authors' argument using much dimmer cytoplasmic specks is out of focus. The authors' argument based on the minimal contribution of the dim specks to the overall signal in the broad band doesn't address these problems.

They also made comments on the spots the reviewer picked up. 5 of 8 spots were rejected because "Spot x is small and the fluorescence is limited to 2-3 Z-slices" However, these are ad-hoc and highly subjective criteria as we still find in the Methods section "To qualify as a unitary node, a spot had to satisfy two conditions: (1) the fluorescence of a spot was present within a circle 12 pixels (~0.5 μm) in diameter; (2) the fluorescence of a spot was present in 7 or fewer consecutive Z-slices. with a peak in the middle slice and diminishing towards both sides.". Note the terminologies, "within" and "7 or fewer consecutive Z-slices". They also commented on Spot 1 "Spot 1 looked like two spots together in both the X-Y and X-Z-slices, so we did not count it as a node." However, this is also the case for the ROI 0016-0244-0082 on the same z-slices, ROI 0018-0306-0104 and 0019-0249-0116, which have irregular, non-circular appearances (pages 8-10 of problem.pdf shared previously).

The node is a structure with a diameter of less than 100 nm. The observed spots are the convolution of the geometry of fluorescent proteins and the point spread function of the microscope, followed by deconvolution. The major factor that determines the size of a spot is the intensity of the fluorescence. The exclusion based on the size of the spot is almost equivalent to the exclusion by the fluorescence intensity, which is proportional to the number of the tagged molecules.

Issue 4 Statistical test for normal distribution

It was admitted that the proper test rejected that the distribution of the intensity of the 'unitary nodes' follows a Gaussian distribution unless an additional selection is introduced. This is consistent with the uncertainty and subjectiveness of the criteria for the 'unitary nodes' discussed above. Anyway, the reason for the change in the number of cells needs to be clarified. Does the original dataset pass the normality test after the same manipulation (cutting the long tail)?

It is difficult to understand why the authors insist on the normal distribution. Akamatsu (2017) showed a distribution of Blt1 with a similar spread, which was fit with multiple Gaussian. Figure 2D can easily be fit with multiple Gaussians as well (page 2 of the Reviewer problems2.pdf)

In this version, there are two different Figure 2D histograms, one on page 9 and the other on page 55. They are different in bins centered on 3000 and 3500 (arrows in page 3 of problems2.pdf) in addition to those centered on 5000, 5500, 6000, and 6500. This difference must influence the Gaussian fitting with the nodes whose intensity was less than 4600 A.U. However, the two curves of Gaussian fitting seem to be identical (both annotated as "2300{plus minus}900"). Something is wrong here.

Issue 5 Distributions of fluorescence intensities of small nodes in mutant strains

The authors claim that the distributions in the current Figure 3G follow a normal distribution based on the Shapiro-Wilk test, attributing this change to the new analysis with the background ROIs adjacent to the node broad band. However, the number of the cells analyzed is quite different from the previous versions (24 cells to 18 cells in an extreme case). Why were some data silently omitted? Can we get the same results with the original set of cells?

Issue 6 Unitarity of the 'unitary nodes'

The authors accepted that, by FPALM, they had detected clusters smaller (or less number of localized emissions) than the 'unitary nodes' but excluded them from their analysis. They rationalize the omission of these smaller clusters by arguing (1) they are distributed across the entire surface and (2) some of them are not on the flat surface. However, these arguments are weak. As for (1), it is true that there are small clusters across the entire cell surface (Laplante 2016 Figure 1A, an enhanced image on page 4 of problems2.pdf). However, they are much smaller/dimmer than those the reviewer previously spotted in Figure S2E, and the similar ones in Figure 1A found in the equatorial zone with roughly about a half the density of those marked as the 'unitary nodes' (indicated by arrows on page 4 of problems2.pdf). Much smaller clusters everywhere are not a good reason to exclude the slightly smaller clusters (with about a half the number of localized emissions of the 'unitary node') found next to the 'unitary node' in the equatorial cell cortex. As for (2), the dimmer clusters spotted are within 500 nm from those scored as nodes containing one or two 'unitary nodes'. Is the curvature of the cell surface so steep?

Issue 7 Nature of the dotty cytoplasmic signal

Thank you for the detailed answers. Why don't you cite Korobchevskaya et al. (2016) in the Introduction?

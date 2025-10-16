# Peer review - Round 1

Editors:
- Oliver Hobert, https://ror.org/00hj8s172 Columbia University, Howard Hughes Medical Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77918.sa0](https://doi.org/10.7554/eLife.77918.sa0)

This paper very nicely tackles a methodological problem in aligning different types of datasets (EM and light microscopy) to image embryonic nervous system development in the nematode C. elegans. The paper is important from a methodological standpoint, and also provides novel insights into nervous system development that will be of general interest.


---

# Peer review - Round 1

Editors:
- Oliver Hobert, https://ror.org/00hj8s172 Columbia University, Howard Hughes Medical Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77918.sa1](https://doi.org/10.7554/eLife.77918.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Cross-modality Synthesis of EM Time Series and Live Fluorescence Imaging" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor (Oliver Hobert) and Claude Desplan as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Andrew D Chisholm (Reviewer #1).

All three reviewers agree that this is very nice work that we would like to see published in eLife. However, all three reviewers feel that the manuscript would very much profit from significant editorial revisions that emphasize the biological findings more and also contextualizes a number of these findings more effectively. You are also much encouraged to move material from the Supplement into the Main text, particularly those figures that provide novel biological insight. You will find below a quite extensive list of suggestions for editorial changes and we encourage you to consider them well.

Reviewer #1 (Recommendations for the authors):

Some issues in the presentation of the manuscript could be improved prior to publication. There appears to be mis-numbering of the supplemental figures and/or their callouts in the text. Although I have a theory as to the correct numbering, this created considerable confusion in the review.

The cell identification in the EM datasets is a combination of manual identification and automated identification based on the alignment algorithm. The manual identification process could be clarified, as it is extensive (140-240 manual IDs per data set). Table S5 summarizes some 'landmarks' used in pre-alignment, could the authors expand on what makes these neurons or other cells 'distinctive/distinctively shaped'? This table might be of more utility if fully written out at the single-cell level. It would be worth explaining what constitutes the 'ground truth' for these manual IDs.

Presentation and wording:

(1) The title states 'cross modality synthesis' of EM and FM imaging, however elsewhere it may be more accurately described as 'image alignment' or 'cross modality analysis'.

(2) Why is the EM data a 'pseudo time series? Pseudotime implies that the time dimension is inferred from non-temporal data, yet the EM data form a sparse time series (4 time points, though described as 'dense' in results).

(3) What is the definition of 'breakout' in the context of neurite growth?

(4) The C. elegans-specific term 'hypoderm' is not widely used; for a general audience 'epidermis' can be used as it means the same thing.

Reviewer #2 (Recommendations for the authors):

Strengths

– This is a first attempt for a combined study of C. elegans embryos by fluorescent and electron microscopy, by aligning – registering images without the use of correlative electron microscopy.

– This study introduces a landmark-based alignment assigning identities from a set of labeled data to unlabeled data, with co-optimization of unstable landmarks contributing to accuracy.

– This work provides a comprehensive analysis that largely supports and sometimes expands on previously studied processes of neuropil and sensory channel formation in C. elegans embryos.

– The authors provide publicly available data of their EM sections in webKnossos open resource, which is provided in amenable form can be very advantageous for the community.

Weaknesses

– The technical strength of the approach compared to others is not sufficiently demonstrated. There is a sparse actual assessment of the method's robustness/variability across samples and in comparison to other methods, in terms of data acquisition/analysis. Including comparative analysis of EM sample replicates for each time point, and comparisons across alternative methodologies (algorithms, electron microscopy) will allow substantiating the approach's superiority and its feasibility for future large-scale use, suggested by the authors in the study.

– Regarding data accessibility, the study sometimes lacks a detailed, comprehensive presentation of data acquisition, analysis, and underlying assumptions/caveats. This refers to instances such as the use of landmark fluorescent markers with multicellular expression to follow single-cell processes, the image registration/cell-identification using landmarks with expression patterns that are not presented in detail, explanations about process tracing and verification in EM sample analysis. The authors invite for community curation/ feedback of a publicly available EM resource, yet the provided resolution and formats (in terms of cell identification, tracing) may not facilitate curation.

– The study sometimes lacks comprehensive, inclusive contextualizing of new findings in relation to knowledge previously published by the authors and by other specialists. That refers to discussed developmental events of lineage progression guiding sample analysis, and findings of excretory pore and neuropil formation, pioneer-neuron concepts, amphid channel assembly.

I list my comments in order of appearance in the manuscript, which should be addressed for publication.

Suggestions for improved or additional experiments, data or analyses:

86-87 "As part of the effort to test and demonstrate the feasibility of EM time series acquisition[…]": The authors should discuss any potential variability/ differences arising from using different EM techniques to analyze different timepoints 1,2 and 3,4. Since the two techniques are used "to demonstrate feasibility" it appears key to discuss (later in the manuscript) the comparison of the two approaches in terms of their use in such project, i.e. effort/ implementation of sample preparation/data analysis, the influence of resulting resolution/stitching to cell identity registration, other pros/ cons. More importantly, if a single embryo is analyzed per timepoint, this would be one of my main critiques of the manuscript. At least 2 samples per timepoint will allow assessing the method's feasibility, robustness, reproducibility, variability.

92 "sparsely expressed cell membrane marker […] (Figure 1b, S1)": For the detailed understanding of C. elegans specialists, the authors should provide in supplementary data the exact lineage-derived expression pattern of used markers similarly to the Lineagomics project (https://epic.gs.washington.edu/), or else cite studies that provide these.

160-162 "Correlated cell identities […] using individual cells/nuclei as landmarks": It appears key that the authors present the variability in cell/nuclei positioning across embryos (and for different cell types) used for FM-lineaging. Especially given the use of these positions as landmarks on a single EM sample per timepoint.

165 "Based on timing of known developmental events in the FM series, the aligned EM data are timed": What are the known developmental events? This is not adequately or comprehensively explained. The authors should expand as necessary for a broader audience.

168 "We assess the accuracy of the correlated cell identities": Here and elsewhere in the manuscript, it appears important to compare the accuracy of cell identification and process tracing to other techniques of identification in electron microscopy studies such as CLEM, connectomics studies, or studies of EM-FM registration in other organisms (i.e. in Vergara, 2021 where nuclear-alignment results in 99.0% accuracy and stepwise image registration uses STAR Methods).

187-190 Figure 3g: "auto-fusion of the excretory canal, duct, pore and gland cell.": The images and notions concerning this topic and data should be explained in detail. Text and images lack context and details necessary even to C. elegans readers (unless they are specialists of this structure). Relevant studies should be discussed and cited (Soulavie et al., 2017,PMID: 29717108).

201 "These results are deposited on webKnossos.": The accessibility of the data is commendable. The authors are encouraged to explain what possibilities of annotations/ data-browsing are allowed in the interface. Given the study emphasizes describing fine cell morphologies, providing images with higher resolution and traces of the studied cells/processes across sections would allow better data visualization and integrating community work/ feedback.

215 "appear around the bean stage and a ring around the pharynx becomes visible by the comma stage": Earlier paper showing this should be cited here (Rapti et al., 2017, PMID: 28846083).

246 Figure 4c: "NR showing pioneers, entry points, the approximate extent at bean and comma."

Given there is one schematic in 4c, it is unclear if it corresponds to bean or comma. This should be explained. Entry points/growth can be different between bean and comma stages, being 25min apart.

246,262, 272 The authors often use the term pioneers to denote early growing neurites in the specific entry points. However, in other neuroscience studies including C. elegans studies (also cited by the authors), the term pioneers is used for early entering axons that are functionally important for entry of others. AVJ-AVD (referred to as supralateral commissure pioneers) ASH, RIB, and AWC (referred to as amphid commissure pioneers) have not been shown functionally important. The authors should refer to early entering neurites and not pioneers. Otherwise, pioneer roles should be established with ablation/functional studies, or other studies showing functional importance should be cited accordingly.

252 "Figure 4e: Each dot represents a single neuron or small cluster of neurons. (lim-4:red, unc-86:green, zag-1:blue, ttx-3:magenta, egl-13:cyan, cnd-1:black, ceh-37:gray, ceh-10:purple).": The expression patterns of the used labels are missing here, or please indicate the published source.. Given their expertise in lineaging, it is important that the authors provide (supplementary) the lineage-related expression pattern of used markers as in Lineagomics project (https://epic.gs.washington.edu/). Secondly, at least some of these reporters do not label single cells (i.e. mgIs18, Table S4 labels AIY but also SMDD as per Bertrand and Hobert, 2009; Rapti et al., 2017). Moreover, many of these labels used (Table S4) appear to be non-integrated arrays (egl-13, ceh-37, zag-1, lim-4?) and thus are prone to mosaicism. It is unclear if/how the breakout times of specific neurons are identified in the single-cell resolution. In FM, are these identified by lineaging these markers and identifying processes in single-cell resolution? In EM, are these identified through registration of cell identities and EM-tracing of single-cell axons? The authors should explain. Replying to the above is key to allow contextualizing the findings with other published information on neuropil assembly, for a better understanding of the reader.

255 and 260 "Figure 4f […] Number of neurites visible in g across the EM series.": The authors should explain in detail what each dot represents in EM timepoints: is this the total number of neurites organized in bundles or also includes single neurites visible across EM sections? Does it refer to neurites across the whole embryo or the ones contributing to the NR neuropil? In the latter case, are the NR-contributing neurites defined by cell identities or by tracing in the NR?

279-280 "a sensory structure that is open to the environment […] The dendrites grow via a distinctive mechanism, a collective retrograde extension": Authors should cite earlier papers demonstrating this structure by EM, including in embryos! (Ward et al., 1975,PMID: 1112927; Oikonomou, et al., PLoS Biol. 2011) (Low et al., Development, 2019, PMID: 30683663). The first paper demonstrating the mechanism of retrograde extension should also be cited (Heiman, Shaham, 2009, PMID: 19344940). I find it puzzling that these are missing.

281 “Formation of the embedded opening and elaboration of dendrite morphology occur in embryogenesis but are less understood.”: In fact, mechanisms of the channel’s formation are significantly studied. A series of relevant publications investigate this process, with mechanistic findings (Perens and Shaham, 2006 PMID: 15935778; Oikonomou, et al., PLoS Biol. 2011 PMID: 21857800; Oikonomou et al., 2012 PMID: 22138055; Wang et al., 2017 PMID: 28803967; Bacaj, Lu, Shaham, 2008 PMID: 18245347; Low et al., 2019, PMID: 30683663). These should be discussed and cited.

361 "Last but not least, our post hoc correlation of EM and FM data provides a useful alternative to true correlative EM. Correlative EM is a powerful, but complex to implement […]": For this first demonstration of cell identification with post hoc FM-to-EM correlation, it appears important to validate the method with CLEM of one sample. An embryo expressing a cell landmark marker with sparse labeling (i.e. Pttx-3) could be prepared by correlative EM so as to identify the labeled cells (AIY,SMDD) by CLEM labeling and by the new co-optimization algorithm. This will allow evaluating the accuracy of nuclei estimation. It should be hopefully feasibly, given the author's previous expertise/use of Correlative EM (Kolotuev et al., 2009, PMID: 19807690; Kolotuev et al., 2012,PMID: 22857930; Burel et al.,2018, PMID: 29802150).

339 "While our study is focused on the wild type, one could use live FM to build the appropriate ensemble models to analyze mutants": Using this methodology to study mutants is an exciting perspective! Yet, WT-mutant comparisons require analysis of more than a single individual per genetic condition. The study in its current form does not allow to evaluate the feasibility of larger-scale usage. Also, EM analysis of one sample per condition/timepoint does not inform on possible variability across samples of one timepoint. Performing EM analysis of a second sample for at least one timepoint per technique will allow addressing the issues.

341-343 "We present the image data and identity annotation of our correlated EM series as an accessible public resource […] seed of a community effort that we hope will fully validate annotation"

The public accessibility of the resource is commendable. It would be important to understand what type of data-browsing and annotations are allowed by the interface and the resolution of the data provided. In order for effective browsing, 3D data could be available with the identified cell identities annotated on the data. Process tracing of the identified cells could also be provided on the browsed/ downloadable data. In order for validation and future use of this resource by the community, the data would need to be provided in a downloadable format with the required resolution.

354 "The data-driven modification in the co-optimization algorithm further facilitates such a vision for automated alignment and annotation of complex brain images.": It is unclear to the broader audience to which degree this is feasible, what advances the current method requires. The authors should explain what limitations or difficulties may be faced for the implementation of the approach in more complex images.

Figure S7d "socket cell over three successive frames in the same cnd-1 promoter"

By Lineagomics (https://epic.gs.washington.edu/) cnd-1 is expressed in many more cells than the amphid socket, including cells partaking in the amphid channel (AMsh sheath, AWC, ASG). AMso and AMsh could be imaged distinguishably by performing mosaic experiments or photoconversion or using less broad promoters. If not, it is unclear how the authors distinguish in FM between processes of all these cells in Figure 5d and Figure 7d, given the FM resolution. Because of this, it is unclear what the FM imaging is adding to the EM data and conclusions. The authors should explain.

Recommendations and corrections for text and figures:

62 "EM studies [contributed to] principles of structural organization"

Despite this being a more comprehensive study of embryonic tissues by EM, few past studies in C. elegans embryos contributed principles of structural organization (Soulavie et al., 2017, PMID: 29717108, Rapti et al., 2017, PMID: 28846083, Low et al., 2019, PMID: 30683663). It appears appropriate that such studies are cited here.

98 “we use the nuclear positions, which are also annotated for the EM series, as the common reference (i.e., a Rosetta stone)”: Authors should expand and explain adequately/ comprehensively as necessary for a broader audience.

185 Aligning color-codes to use the same in Figure 3e and b-c-d, will allow the following cell identities.

189 EM images can be shown both with and without color-coding to better visualize cell fusion.

213 “The NR emerges in the later half of embryogenesis”: Earlier paper showing this should be cited here (Rapti et al., 2017, PMID: 28846083).

217 “even neurite topography through combinations of two-color imaging”: Earlier studies with C. elegans two-color FM imaging of neurites (including in the embryo!) can be cited (Heiman, Shaham, 2009, PMID: 19344940, Rapti et al., 2017, PMID: 28846083, Moyle et al., 2020, PMID: 33627875)

220 “We scan through EM data to identify neurites, and backtrace them to soma”: The authors should explain the exact approach used for process tracing (manual, semi-/ automatic, etc).

240-250 Figure 4b-4e. Color-coding is not consistent between models, FM, EM images, i.e. sublateral pioneers are red in Figure 4b EM but light blue in Figure 4c, and Plim-4 which labels sublateral pioneers is red in Figure 4e. Consistent color-coding would help the reader.

Figure 4c, S5a It is unclear if the drawn arrows’ length is proportional to the actual neurite total growth (across EM sections of the same embryo)? For example, what is the relative length of SIA/SMD and ASH, in the model (Figure S5a) and in the actual EM (Figure S5f,g)?

268-271 “comparing the left- and right-side behavior of the first cells to grow into the NR, namely SIADL/R and SMDDL/R, suggests strong symmetry in behavior. Both sides have broken out at the bean stage, with similar-sized outgrowths […] their tips meet precisely beneath the midpoint of the ALA […].”

This is in line with previous studies, indicating such symmetries and ALA’s position, these studies should be cited (Rapti et al., 2017, PMID: 28846083; Insley and Shaham, 2018, PMID: 29590193; Moyle et al., 2021, PMID: 33627875). In order to establish symmetry beyond previous observations, it appears key to providing quantitative data, calculating the length of bilateral processes by tracing them in EM series.

282 The first paper demonstrating this dynamic process should be cited (Heiman, Shaham, 2009, PMID: 19344940).

Figure S5B Shading of EM figure in Box b doesn’t allow neurite visualization. Also (box B), how it is distinguished whether neurons extend neurites or have elongated cell bodies? It would help to provide the EM images with and without color-coding (and larger sizes) to facilitate visualization.

274 “It is not clear […] if there is signaling to coordinate between the two sides.”

Some mechanisms related to the regulation of left-right symmetry of axon guidance are studied in Grossman, Giurumescu, Chisholm, 2013, PMID: 23979582. The paper should be cited.

Figure S3, S4, S5, S6, S7 are mislabeled, 2 figures are abelled S3 and legends do not correspond. Also, scale bars are missing in many supplementary figures and when present, there is no reference of scale bar size in the legend. These should be corrected accordingly.

411 Some alignment of 1.5/2fold AT-EM data (available in webKnossos) is “jittery”, may any additional image registration help eliminate this, for the better visualization of data?

Reviewer #3 (Recommendations for the authors):

The method is well-executed and thoroughly explained, and this manuscript shines in the temporal and spatial precision by which developmental processes are uncovered and described as a result. However much of these biological discoveries were buried in the supplementals. To create more relevance and excitement for this journal’s audience, the authors should re-write parts of the manuscript, with a stronger emphasis on what the limitations of current imaging methods are, what cross-modality analyses improve upon, and particularly by bringing focus to the biological discoveries and putting them into the main article.

In addition to the inherent challenges of EM-FM cross-comparison, in this article, the cross-modality alignment method overcomes two distinct issues: the challenges associated with manual annotation of embryo developmental EM series; as well as integration of spatial resolution of EM with the temporal resolution with FM. These concepts are briefly mentioned in the introduction and throughout the article, but do not become apparent to a non-specialist reader until the end. These current challenges should be further emphasized in the introduction when describing these imaging methods to highlight the benefits of the analysis method presented.

Note: supplemental figures are mis-numbered (there are two Figure S3s, and the following figures do not match figure captions). I will refer to supplemental figures as they are numbered in the figure captions.

Most of Figures S5, S6 and S7 should be integrated into or added as additional main figures. These data beautifully highlight both the temporal and spatial resolution achieved by the cross-modality method used.

How is “adjacency” defined between nuclei that are not physically touching? Are there specific parameters for what distance between cell nuclei counts as adjacent?

Line 236: what is meant by “breakouts observed in the EM at the comma stage span an hour?”. Is this referring to lack of temporal resolution? This statement is confusing because Figure 4e and Table S4 referenced doesn’t seem to show this to be the case.

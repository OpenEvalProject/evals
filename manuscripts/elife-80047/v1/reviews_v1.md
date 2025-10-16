# Peer review - Round 1

Editors:
- Sjors HW Scheres, https://ror.org/00tw3jy02 MRC Laboratory of Molecular Biology United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80047.sa0](https://doi.org/10.7554/eLife.80047.sa0)

This paper describes a new software tool: SmartScope, for automated screening of cryo-EM grids. SmartScope can also perform automated data collection on suitable grids, including with beam-image shifts and tilted stage geometries. If it works in practice as advertised in the paper, then it will be a highly useful tool for the field, especially if other groups would also contribute to its open-source and modular code.


---

# Peer review - Round 1

Editors:
- Sjors HW Scheres, https://ror.org/00tw3jy02 MRC Laboratory of Molecular Biology United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80047.sa1](https://doi.org/10.7554/eLife.80047.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Automated systematic evaluation of cryo-EM specimens with SmartScope" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Sjors HW Scheres as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Kenton Swartz as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Arjen J Jakobi (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All three reviewers agreed that the software described in this paper would be a highly useful addition to the field and are in support of publication.

1) A table summarising the data acquisition parameters and data collection statistics should be provided.

Strong encouragements:

1) The reviewers praise the authors for their intention to make the code available to the community and encourage them to do so as soon as possible.

2) Besides providing the source of the smartScope program on github, the authors are also encouraged to provide the labelled raw training data for the convolutional neural networks. Public repositories like Zenodo or EMPIAR could be used.

3) The 3 reviewers each make useful suggestions to improve the manuscript below. Although these are not essential for acceptance, the authors are encouraged to give this serious consideration.

Reviewer #1 (Recommendations for the authors):

All Supplementary Figures should become supplements to one of the main figures.

Reviewer #2 (Recommendations for the authors):

The paper is in my opinion very well structured with clear figures and procedure steps. In general, I really enjoyed reading it and I am willing to test it soon. Of course, a work of this type passes the real test when it starts being used by the community. I believe that SmartScope will be used as there are no other fully automated solutions for grid screening.

From the description in the text, the software appears to be quite solid and the authors have pretty much answered in the text itself any questions that were coming to my mind while reading. In short, this manuscript is very detailed, easy to follow in a logical mind flow, and takes into consideration all aspects of specimen screening and data acquisition. From my side, the article is publishable as it is.

Some more detailed comments:

Line 143: SmartFlow is bound to serialEM, will it be possible to couple it to EPU for example, which is widely used, or other software used for the collection of diffraction data? How dependent is on serialEM 4.0? Will SmartScope be maintained as serialEM develops?

Line 153: Is there a minimal magnification that has to be used for the window clustering to work properly? Can the authors include some comments/guidelines on this?

Line 175: Do I understand correctly that some images are also taken in the carbon, or at the carbon/ice interface to evaluate the distribution of particles?

Line 179: I would simplify the procedure to gain time, at least for relatively short exposure times. Probably not in all cases frames alignment and CTF estimation are necessary, to view the stability of the new microscopes equipped with autoloader. However, it is probably better to have these options while running the automatic screening e.g. overnight.

Line 221: Out of full completeness the authors might comment on how their algorithm to maximise target coverage while minimising numbers of groups compares to the same procedure in EPU. There the BIS applied can be changed. Is that possible in SmartScope?

The fact that SmartScope can perform BIS collection on tilted specimens in a correct way is great.

For the evaluation of the network organisation part, I have asked the opinion of an expert colleague, who commented:

Line 237: I don't quite understand what the authors mean with: "bundles a webserver and the main imaging workflow". I assume the webserver is for interacting with the program and the "main imaging workflow" is what runs on the worker if installed on separate computers, but it would be better to make it a bit more clear.

The Singularity container image is convenient and good that it's versatile enough to be installed on separate systems.

Line 245: Why do both the web server and the worker need to have access to a shared disk? Does the worker write and the web server only reads the results to display to the user? What kind of information is stored in the database?

248: The object store can be accessed via the Amazon S3 API. It's a nice feature for exporting data to "the cloud". Maybe the author should clarify a bit what are the full advantages that one can get from such a setup?

Supplementary 43: "communicate with each other using Socket or SSH connections" Do they mean HTTP? In the graph, there is no mention of SSH connections, only HTTP.

Reviewer #3 (Recommendations for the authors):

Points for consideration:

– The introduction describes many important concepts and limitations in the preparation of cryo-EM specimens and in screening/data collection, but only sparsely cites, and if, very general reviews on these topics. The reader may benefit if the authors would more specifically refer to the excellent primary literature on these topics.

– In addition to their YOLO-based hole finder, the authors may consider mentioning that the open and modular approach of their software allows integration with approaches such as e.g. virtual maps in Py-EM, which could extend the reach of their method to more sophisticated screening/targeting scenarios and different sample supports.

– The micrograph pre-processing routines implemented in SmartScope currently involve frame alignment and CTF estimation. The authors may consider including the possibility of image denoising workflows such as those implemented in data pre-processing pipelines (Warp, Scipion, SPHIRE, CryoSparc Live, …), which can be useful tools for rapid selection of suitable imaging areas, in particular if particles are small.

– The authors comment on the screening mode statistics from the operation of SmartScope in their facility. From their facility projects, are there statistics available on how many cases the screening procedure followed by automated, targeted data collection lead to successful structure determination, and how this compares to manual screening and subjective targeting on the same sample? This could be insightful.

– The authors mention that data collection of human mitochondrial DNA polymerase involved tilting of the specimen in a subset of the dataset to improve angular sampling. It would be useful to show angular distribution plots for the data excluding and including the tilted images to illustrate this was required and how automation by SmartScope can help detect and mitigate such problems on the fly.

– A table summarising the data acquisition parameters and data collection statistics should be provided.

– It is laudable that the authors make their software and models publicly available. It would be more useful to have the repository public open at the moment of preprint posting so as to give reviewers the possibility to also screen review code. The data availability statement contains a remark of disclosure of data upon reasonable request. It is unclear what this statement means, and which requests are considered reasonable; these data can be useful for other academic projects following related but complementary approaches, as well as comparison and benchmarking. I encourage the authors to make raw ML data available through public repositories such as Zenodo, and to deposit raw micrographs at EMPIAR.

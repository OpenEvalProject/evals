# Peer review - Round 1

Editors:
- Robert H Singer, Albert Einstein College of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08494.025](https://doi.org/10.7554/eLife.08494.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Spatially Coordinated Dynamic Gene Transcription in Living Pituitary Tissue" for peer review at eLife. Your submission has been favorably evaluated by Jim Kadonaga (Senior editor), a Reviewing editor, and two reviewers.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

The Reviewers find the work of interest, in particular that the spatial relationship of cells within a tissue may lead to a common basis for expression. However they feel that there are some obscure analyses and the text in ambiguous in parts. One reviewer "found the work deficient in terms of the quantitative and theoretical analysis". The other thought that" the primary contribution of this paper may be the relationship between this stochastic process and the integrated production from the tissue" but that this was not clearly developed. In both cases, some extensive revisions - in particular, more rigorous text and analysis - will be necessary before it can be considered further.

Reviewer #1:

The authors investigate the temporal and spatial variability in gene expression between individual cells, in the context of a mammalian tissue. Specifically, the expression of prolactin in rat pituitary slices, both in the adult and during development. Pursuing questions of stochasticity and of cell-cell communication in the complex context of a multicellular tissue has the potential for significant insights, and some of the data presented by the authors is quite interesting, but I found the work deficient in terms of the quantitative and theoretical analysis (which the authors describe as "sophisticated", paragraph four, Introduction). The standard for such analysis is quite high, even for studies in mammalian tissues, as demonstrated e.g. by the recent work from Halpern et al. in mouse liver (Molecular Cell 2015; cited by the authors).

Specific points:

1) The authors analyze their temporal fluorescence data using a theoretical stochastic model, to extract the parameters of gene activity. However, the validity of the model is not challenged by testing that it can successfully reproduce the experimental data. Nowhere do we see a plot with direct comparison between an experimental observable and its predicted value from the model. Thus what we have is a "forward only" process where experimental data is fed into an algorithm, to produce estimated parameters, without the critical feedback from model to experiments. This dramatically diminishes the value of the theoretical analysis.

2) On a related note, it is unclear what was learned from the model that was not already in the experimental data. In particular, the temporal and spatial correlations in expression, and how those change during development, are evident from the straightforward analysis of the data, and it was not obvious that the model sheds any additional light on these findings.

3) Besides the theoretical model, the quantitative analysis of data was itself quite flawed in a number of instances. Examples:

i) "fluorescence activity showed a clear deviation from a white noise process indicating a pulsatile transcriptional behavior". Why would the expectation be of "white noise"? And why would deviation from white noise indicate pulses? This is very unclear.

ii) The cell-cell correlations in Figure 2B-ii show an increase at large distances. This is probably an artifact, since it can be seen in the randomized control as well, but the presence of this trend is suspicious-could it indicate a flaw in the correlation calculation, e.g. in normalizing for the number of cell pairs?

Reviewer #2:

In this study by Featherstone and coworkers, the authors use single-cell imaging to look at prolactin expression in rat pituitary tissue. Expression is measured via a GFP reporter driven by the prolactin promoter in the context of a transgenic BAC. From these fluorescence time traces, the authors reconstruct transcriptional dynamics through a statistical inference model. Single-cell imaging of prolactin promoter activity in cells in culture and the inference model have been published previously by some of the authors. The novelty in this work lies in performing these measurements in a pituitary tissue slice. Although this approach has some caveats (inference of transcription dynamics from protein time-series, transgenic regulation, tissue slices, etc.), my opinion is that it is overall a reasonably faithful approximation of the actual endogenous regulation of this promoter in a tissue context. In that sense, it is a major technical advance. I am unaware of any other studies that look at stochastic gene regulation with this resolution in tissue. The major conclusions they reach are that the prolactin promoter is pulsatile in tissue, the pulsatility changes during development, and that cells show local coordination by means of adherens and gap junctions.

Overall, the data is of very high quality, and the analysis seems sound. What is missing, in my opinion, is biological insight into the functioning of this promoter in the context of the gland. However, I believe the authors have this understanding and may have even tried to convey it, but this referee didn't quite grasp the implications. It is possible that a revised manuscript with some restructuring and slightly re-directed analysis would make this message more appropriate for the broad readership of eLife.

1) My main criticism is on the nature of the developmental progression, gene output, and spatial coordination. The authors present a series of observations about all three, but I suggest that it would be more biologically insightful to integrate these observations to describe the overall output of prolactin from the tissue. Does overall output increase during developmental stages? If so, does this output result from more cells (i.e. greater density) or changes in the pulsing? If cells are pulsing in synchrony, would the overall output also display pulsatile production from the gland? It is tempting to conclude form the authors' data that cells have some sort of fixed prolactin regulatory circuit, but as the gland matures, more cells result in higher levels of output, and this output becomes dynamically synchronized through cell-cell communication. Is this correct? Or am I misunderstanding the data? Here, the quantitative modeling would be immensely valuable, perhaps allowing one to extrapolate from the tissue slices to the function in vivo.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your work entitled "Spatially Coordinated Dynamic Gene Transcription in Living Pituitary Tissue" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jim Kadonaga as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

As you can see the reviewers are still unsure of your presentation of the significance of the results and their treatment in the manuscript. In their discussion they have stated that the work does not advance enough from previous published work. eLife requires that the manuscript reports on significantly new observations. Whether this manuscript is accepted will depend on how you can bring out the broader significance of your observations to their satisfaction.

Summary and essential revisions:

In this revision by Featherstone et al., the authors have made some textual and organizational changes to the manuscript to better convey the biological meaning. However, I still find the manuscript lacking in its appeal to a broad audience or even a narrower gene expression readership. It just doesn't go quite far enough in my opinion in generating new insight into the developing pituitary gland. Although I am strongly attracted to the approach the authors have developed, it seems to be an extension of their previous work in this area, published in a series of papers which observe the pulsatility, the change during development, and the refractory period (Harper, JCS, 2010; Featherstone, JCS, 2011; Harper, PLoS Bio, 2011). Here, they have refined their model of the underlying dynamics using a statistical inference method. They conclude that transcription dynamics do not obey a simple telegraph process but do not go beyond this phenomenology, nor do they dissect the functional consequences.

The real advance in this paper is the observed spatial coupling between individual cells and the finding that this spatial coupling changes over development. This coupling, which occurs over a length scale of ~ 30 μM, is perturbed by limited trypsin digestion. This finding is indeed an interesting one, but does it rise to the level of a self-sufficient story? And could it not be delivered in a more compelling way? In summary, I find the work to be technically accomplished, but my overall impression is that they have not spelled out clearly the significant advance in our biological understanding.

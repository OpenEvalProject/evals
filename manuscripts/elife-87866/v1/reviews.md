# Peer review - Round 1

Editors:
- Genevieve Konopka, https://ror.org/05byvp690 University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87866.3.sa0](https://doi.org/10.7554/eLife.87866.3.sa0)

This study presents an important tool for tracking the connectivity of neurons in mouse and potentially other mammals using a combined approach of barcoded rabies virus libraries and spatial transcriptomics. The data supporting the technique are convincing, the validation against known anatomical knowledge is rigorous, and the authors advance the techniques by combing them in vivo. Overall, this is a very good paper describing a technique for tracking neural circuits.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87866.3.sa1](https://doi.org/10.7554/eLife.87866.3.sa1)

In this preprint, Zhang et al. describe a new tool for mapping the connectivity of mouse neurons. Essentially, the tool leverages the known peculiar infection capabilities of Rabies virus: once injected into a specific site in the brain, this virus has the capability to "walk upstream" the neural circuits, both within cells and across cells: on one hand, the virus can enter from a nerve terminal and infect retrogradely the cell body of the same cell (retrograde transport). On the other hand, the virus can also sometimes spread to the presynaptic partners of the initial target cells, via retrograde viral transmission.

Similarly to previously published approaches with other viruses, the authors engineer a complex library of viral variants, each carrying a unique sequence ('barcode'), so they can uniquely label and distinguish independent infection events and their specific presynaptic connections, and show that it is possible to read these barcodes in-situ, producing spatial connectivity maps. They also show that it is possible to read these barcodes together with endogenous mRNAs, and that this allows spatial mapping of cell types together with anatomical connectivity.

The main novelty of this work lies in the combined use of rabies virus for retrograde labeling together with barcoding and in-situ readout. Previous studies had used rabies virus for retrograde labeling, albeit with low multiplexing capabilities, so only a handful of circuits could be traced at the same time. Other studies had instead used barcoded viral libraries for connectivity mapping, but mostly focused on the use of different viruses for labeling individual projections (anterograde tracing) and never used a retrograde-infective virus.

The authors creatively merge these two bits of technology into a powerful genetic tool, and extensively and convincingly validate its performance against known anatomical knowledge. The authors also do a very good job at highlighting and discussing potential points of failure in the methods.

Unresolved questions, which more broadly affect also other viral-labeling methods, are for example how to deal with uneven tropism (ie. if the virus is unable or inefficient in infecting some specific parts of the brain), or how to prevent the cytotoxicity induced by the high levels of viral replication and expression, which will tend to produce "no source networks", neural circuits whose initial cell can't be identified because it's dead. This last point is particularly relevant for in-situ based approaches: while high expression levels are desirable for the particular barcode detection chemistry the authors chose to use (gap-filling), they are also potentially detrimental for cell survival, and risk producing extensive cell death (which indeed the authors single out as a detectable pitfall in their analysis). This is likely to be one the major optimisation space for future implementations of this barcoding approach.

Overall the paper is well balanced, the data are well presented and the conclusions are strongly supported by the data. Impact-wise, the method is definitely going to be very useful for the neurobiology community.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87866.3.sa2](https://doi.org/10.7554/eLife.87866.3.sa2)

Although the trans-synaptic tracing method mediated by the rabies virus (RV) has been widely utilized to infer input connectivity across the brain to a genetically defined population in mice, the analysis of labeled pre-synaptic neurons in terms of cell-type has been primarily reliant on classical low-throughput histochemical techniques. In this study, the authors made a significant advance toward high-throughput transcriptomic (TC) cell typing by both dissociated single-cell RNAseq and the spatial TC method known as BARseq to decode a vast array of molecularly labeled ("barcoded") RV vector library. First, they demonstrated that a barcoded RV vector can be employed as a simple retrograde tracer akin to AAVretro. Second, they provided a theoretical classification of neural networks at the single-cell resolution that can be attained through barcoded-RV and concluded that the identification of the vast majority (ideally 100%) of starter cells (the origin of RV-based trans-synaptic tracing) is essential for the inference of single-cell resolution neural connectivity. Taking this into consideration, the authors opted for the BARseq-based spatial TC that could, in principle, capture all the starter cells. Finally, they demonstrated the proof-of-concept in the somatosensory cortex, including infrared connectivity from 381 putative pre-synaptic partners to 31 uniquely barcoded-starter cells, as well as many insightful estimations of input convergence at the cell-type resolution in vivo. Collectively, this work will establish a cornerstone for future advancements in rabies-barcode technology.

This revised version incorporates imaging data to assess the stringency of identifying the starter cells in comparison with conventional protein-based detection methods. Additionally, it encompasses insightful discussions concerning potential limitations and offers perspectives on future improvements. The method section is systematically subdivided with subsection numbers, facilitating the cross-referencing of the corresponding sections in the main text and figure legends. I posit that adopting this stylistic approach as the standard for manuscripts delineating innovative methodological strides would be prudent. The clarity of the figure legends has been significantly enhanced, contributing to a more accessible understanding of the figure panels. In sum, this manuscript is articulate and thorough, epitomizing scientific rigor.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87866.3.sa3](https://doi.org/10.7554/eLife.87866.3.sa3)

The manuscript by Zhang and colleagues attempts to combine genetically barcoded rabies viruses with spatial transcriptomics in order to genetically identify connected pairs. The major shortcoming with the application of a barcoded rabies virus, as reported by 2 groups prior, is that with the high dropout rate inherent in single cell procedures, it is difficult to definitively identify connected pairs. By combining the two methods, they are able to establish a platform for doing that, and provide insight into connectivity, as well as pros and cons of their method, which is well thought out and balanced.

The authors did a nice job of addressing my comments which mainly centered around the presentation of data, specificity, and wording.

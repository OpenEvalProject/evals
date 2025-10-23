# Author response - Round 1

Authors:
- C Shan Xu ([ORCID: 0000-0002-8564-7836](https://orcid.org/0000-0002-8564-7836))
- Kenneth J Hayworth
- Zhiyuan Lu
- Patricia Grob
- Ahmed M Hassan
- José G García-Cerdán
- Krishna K Niyogi
- Eva Nogales ([ORCID: 0000-0001-9816-3681](https://orcid.org/0000-0001-9816-3681))
- Richard J Weinberg
- Harald F Hess

## Response text

DOI: [10.7554/eLife.25916.033](https://doi.org/10.7554/eLife.25916.033)

[…] Reviewer #1:

[…] I have a few more substantial concerns with respect to the presentation of the work:

1) I find it rather unfortunate for a methods paper to first have to go through some documentations of methodological success in which without first being introduced to the methodological advances it is not totally obvious where the improvements of the author's method lie. I suggest inverting the description and starting by clearly stating the methodological innovations and their relative significance for throughput, image quality and stability. I would be thrilled to learn about this in an instructive way and then at the end be convinced by successful applications of the methods.

Reviewer makes an important point, leading us to reconsider the order of presentation. We agree that a traditional "methods" paper should begin with descriptions of methodological innovations followed by results. The problem is that the manuscript is directed toward multiple audiences. The majority of our readership is likely to constitute biologists, who are more interested in the new capabilities of our FIB-SEM system and “the clear and well-documented absolute superiority of the imaging results” (reviewer #2), rather than the nitty-gritty details of the engineering. Accordingly, we felt it best to leave the overall structure as is. Nevertheless, reviewer's point is legitimate. Accordingly, we have added an overview of the technological improvements of this work at the beginning of “Results and Discussion”, to provide readers with a clear picture of the novelty of our work relative to prior arts. Readers who are especially interested in the technical aspects can now find detailed descriptions in a later part of the manuscript and supplemental materials.

2) The methods are by far not sufficiently detailed. In particular, it would not be possible to reproduce the system as it is described right now. For example – and this is just one of many examples – the computation of the focus index used to do inline image auto optimization (subsection “In-line image auto-optimization”, second paragraph), is only sloppily described, formulae are missing. Similarly, the prompt pausing and seamless restart automated control system is not described to any reproducible detail. It is in my view mandatory for a methods paper to provide all insights and details such that other labs could rebuild and use this system. I think it is also absolutely required to provide all the code used in these systems as a supplementary code base which I could not find in this submission.

We agree that some of the methods are not sufficiently detailed for a typical biology lab to replicate the FIB-SEM system presented in the paper. We have revised the “FIB-SEM system customization for continuous long-term acquisition” section to include more detailed descriptions. For example, the formula to calculate the focus index has been added, and description of the software implementation of prompt pausing and seamless restart has been expanded. However, most of the customization is through software control which is not itself innovative, but instead represents a specific implementation of standard engineering techniques. For example, statistical process control methods are common practice in industrial production environments. There are many ways to implement or tailor the control bands, based on end user’s specific need. Therefore, we only pointed out this is one of the many aspects one should include, without going into the exact details of our implementation. Focus index, for another example, is a generic index number to describe how “sharp” an image is. It too can be calculated in many different ways. Binding et al. presented yet another elegant method for this purpose in their work which we have cited. Concordant with HHMI Janelia's mission, our engineering solutions are open, and we encourage interested outsiders to email us or visit our facility to gain independent expertise.

3) A clear description of the methodological advances as requested in point 1 is also important because some of the results as presented here are actually not novel; e. g. the authors re-introduce the hot-knife-method which they have published before in Nature Methods. It should be absolutely clear that this is not a new contribution of this paper, even if it of course goes along with expanding the imaging range in the third dimension. Similarly, the closed loop control of the FIB beam is an original contribution by Boergens and Denk – this is cited properly, but still it would be very important to know upfront which innovations are the author's and which are extensions or usage of existing methods. As another example: reading the results one cannot judge the effect of detector optimization on imaging speed. In a methods paper, this should be possible, it's (potentially) a key result.

We have revised the manuscript to include an overview of the technological improvements of this work at the beginning of the paper. In this section, we distinguish novel developments versus prior arts (such as the hot-knife method and closed-loop control of the FIB beam), which are now explicitly identified and referenced.

In summary, again, this is an important development, but as presented I cannot fully judge its advances in a precise and detailed way.

Reviewer #3:

[…] Just a few suggestions for improvement of the text:

1) The authors mention multiple "failure modes" during operation of the FIB, for which different strategies were devised. It would be useful to list all these "failure modes" in table, with the appropriate solution and an estimate of the contribution of each of these failure modes during an example run.

Figure 9 has been added to outline typical failure modes with different frequencies of occurrence. Corresponding customized solutions were also included.

2) A method for calculation of SNR is introduced. Here the SNR is proportional to the difference in detected electrons from membrane and cytoplasm. It is however unclear how pixels are classified as membraneous or cytoplasmic.

The derivation of detected electrons from membrane and cytoplasm is a somewhat subjective manual operation. We have added Figure 12—figure supplement 1 to explain the details. For example, in order to obtain electron counts of membranes in Figure 12d threshold red level was manually adjusted until about 50% of the cell membranes (outer boundaries) were covered in red. Assuming the membrane electron counts have a particular distribution, such threshold value would represent the median (also the mean if it is Gaussian) of that distribution. Similarly, the cytoplasm electron counts are obtained by a green threshold so that about 50% of the interior cell area (excluding mitochondria) are covered in green, approximately the median of electron counts originating from the cytoplasm. Due to non-uniformity and other issues, this approach is only an estimate. The comparison, though not rigorous, serves to demonstrate the changes in SNR as a function of sample bias voltage. In addition, it serves as an experimental reference for our Monte Carlo simulations.

3) In Section 2 Detection efficiency model, the modeling shows that at a bias of +600V the path of 50eV secondary electrons (red) are shown to be deflected back to the stage. It would be useful to show that beyond the 600V bias, a further increase in bias will in fact start attracting higher-energy back scattered electron away from the detector, as is noticed experimentally in Figure 9.

Reviewer is correct. We have added “However, further increase in bias beyond +600 V would reduce signal intensity as backscattered electrons are pulled away from the detector or even back onto the sample, depending on their energy. This prediction is consistent with experimental results shown in Figure 12b” at the end of Section 2 “Detection efficiency model” (old Figure 9 becomes Figure 12 after renumbering).

4) Regarding the paragraph about competing methods in the Introduction, it would be better to slightly change the wording to make clear that these statements are about the current state-of-the-art. (One can't rule out further progress in the future.)

We agree. We have revised to the manuscript to read “In contrast, the current state-of-the-art technologies based on diamond knife sectioning or diamond knife block-face removal, lose consistency when attempting z steps between adjacent images below 20 nm.”

# Peer review - Round 1

Editors:
- Jameel Iqbal, Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67660.sa0](https://doi.org/10.7554/eLife.67660.sa0)

This paper explores a novel approve to sorting cells without the use of fluorescent labeling using a light diffraction method called ghost cytometry. This paper first demonstrates this capability with commercial cell lines and then sorting hematopoietic cells from a patient sample.


---

# Peer review - Round 1

Editors:
- Jameel Iqbal, Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67660.sa1](https://doi.org/10.7554/eLife.67660.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "In silico-labeled ghost cytometry" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Mone Zaidi as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Gregory R. Johnson (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Address all the comments from the two reviewers; there are concerns regarding applicability and limitations brought up by both reviewers.

2) Reviewer two noted that the presentation could be improved to enhance readability.

Reviewer #1:

This novel technique provides a method of cell sorting without the conventional use of fluorescent probes which can effect cell viability. They also showed that ghost cytometry can differentiate between live and apoptotic cells giving a more accurate reflection of cell viability. Retaining specimen viability is particularly important for obtaining cell lines and for therapeutic applications such BM transplant or CAR T therapy.

This paper also demonstrates the ability to generate an accurate white cell differential which could have diagnostic utility to potentially replace manual counts which has interobserver biases. However, this paper did not demonstrate the capacity to differentiate B and T cells, count blasts or detect pathologic hematopoietic cells. It would be interesting to see if this platform could identify cells of different levels maturity as hematopoietic pathologies lie all along the maturation spectrum.

While separating cells at different levels of maturation was demonstrated in cell lines, this is differentiating undifferentiated cells from terminally differentiated cells and does not demonstrate intermediate stages of differentiation.

CD34 should probably have been added to the flow panel to demonstrate if ghost cytometry can count blasts. A white cell differential is incomplete without this capacity.

Another marker that would have been helpful would be using CD138 for plasma cells. Plasma cells are known to be inaccurately counted by flow cytometry. Demonstrating an accurate plasma cell count on ghost cytometry compared to a manual differential could have provided a potential area of superiority diagnostically of ghost cytometry compared to flow cytometry.

The white cell differential was also only done on one patient. Having several patient samples should have been used to validate this method.

Reviewer #2:

Flow cytometry typically relies on images and/or multiple chemical labels to identify cellular phenotypes. By training a machine-learning based model on a ground-truth labeled dataset, Ugawa et al. demonstrate that some cellular phenotypes can be accurately determined from a one-dimensional waveform of a cell passing through a field of structured illumination without the use of chemical labels. In combination with ultra-fast cell sorting this method opens the door for tasks where sorted cells may be utilized for downstream applications where staining is undesirable. This manuscript adds to growing number of applications of "in silico labeling" where machine-learning models can be utilized to predict chemical labels from unlabeled samples.

Overall, the approach is well described and the results are promising. The authors evaluate their methods with diverse tasks, but the evaluation procedure may not reflect real-world deployment of such a method.

The manuscript demonstrates the performance of several cell-phenotype classification tasks. After sample preparation, the cells are stained and cell-phenotype labels are assigned according to gates based on ground-truth stain read-out, whereas cells falling outside of the gates are discarded. The labels of the gated cells, in conjunction with their GMI signals are used as training and test data for the machine learning models, and the test results are reported. "Discarded" cells based on the ground-truth stains are not represented in the classification results. If a model were trained and applied to a new sample, those "discarded" populations will be presented to the classifier. The evaluation presented here likely would not reflect the performance of the model relative to a new sample.

As described in the methods, the training and test data are derived from the same sample. If such a model were to be implemented, intra-experiment variation may play a significant role in the accuracy of these results. It is therefore difficult to determine how this method would function when deployed in other settings.

I feel that several points may be addressed to significantly improve the manuscript:

The inclusion of a "discarded" label in the classification results, or otherwise address the "discarded" population problem. Without such, it is very difficult to evaluate the results presented here.

Evaluation of whether the model would generalize well to new samples.

It is not clear what the limitations of this method are. Are there applications where iSGC falls flat? Can we apply multiple models from different data to a new application?

Overall the discussion of flow versus image cytometry (starting at line 60) could be improved. Some claims are without reference, and discussions about the time scales of signal analysis in flow and image cytometry would be useful for more general audiences.

Some of the claims about future applications of these methods seem very strong. It would be useful to provide perspectives from other manuscripts that support discussion of future applications.

There are some compression artifacts in the scatter plot figures that make them difficult to read.

It may be worth considering a more colorblind friendly or perceptually-uniform color map for figures as well.

The "b" in the description of figure 5 should be a "(B)"

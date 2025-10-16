# Peer review - Round 1

Editors:
- Edward D Janus, University of Melbourne Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52938.sa1](https://doi.org/10.7554/eLife.52938.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript describes a methodology to analyze platelet (and leukocyte) aggregates that utilizes microfluidics, optofluidic time-stretch microscopy and convolutional neural network analysis. The manuscript presents data that the technique can distinguish activation by four platelets agonist – ADP, collagen, U46619 and TRAP-6.

Decision letter after peer review:

Thank you for submitting your article "Intelligent classification of platelet aggregates by agonist type" for consideration by eLife. Your article has been reviewed by Aleksandra Walczak as the Senior Editor, a Reviewing Editor, and two reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors present a novel deep learning based method to classify platelet aggregation based on various agonists using high-throughput imaging. The sample preparation and the advantages of the procedure is well explained. The capture images are used to train and eventually classify images of platelet aggregates.The manuscript presents data that the technique can distinguish activation by four platelets agonist – ADP, collagen, U46619 and TRAP-6.

A number of questions have been raised. We invite you to submit a revised version addressing these.

Essential revisions:

1) Data are presented for three healthy subjects. One donor has a different pattern than the rest. The authors interpret this as showing that the test could have diagnostic utility. But all three donors where healthy, thus I interpret this as variation in the test. There is no other assessment of the variation amongst normals.

2) Endothlelial TXA2 receptors are cited (subsection “Demonstration of the iPAC”) as a mechanism of one effect from U46619, but they studied studied blood, which likely has, if anything, a very small amount of circulating endothelial cells.

3) It is unlikely that a platelet will ever see a single agonist in circulation. This is not discussed. Collagen-induced activation of platelets results in ADP and TXA2 release. They tested all three of those agonists. Some consideration of these combinations would aid in the feasibility of this novel technology. Similarly, platelets circulate in an environment with locally produced inhibitors (NO, prostacyclins, ADPases). Their effect has not been assessed, and this can be substantial (see Cattaneo et al., 2007).

4) Platelets circulate in vivo where the calcium concentration is 2 mM. The studies are done in citrated plasma where the calcium concentration is far lower. Studying platelets at artificially low calcium concentrations has, in the past, led to artifactual findings. Other anticoagulants could be used.

5) Was there additional activation of the platelets when they were spun on the gradient?

6) In deep learning network used for classification what is the need for the up-sampling layer (decoder part)? The decode part reconstructs the image. Is this reconstructed image being used anywhere? Why is the classifier layer at the CNN bottleneck not sufficient for classification?

7) The authors mention that crops from the actual image containing the cells are used for classification. However, how these crops are generated is a big question. Are they manually cropped from the image or some automated technique is used to obtain the cropped regions, specifically during testing phase?

8) The classification accuracy for the TRAP-6 in both confusion matrix of Figure 3 is low in comparison to the others. Is there any explanation on why so? Is there any class imbalance during training phase? How many total images were used for training and how mane images were there in each class?

9) Accuracy of which data is shown in Figure 3A and 3C?

10) A more elaborate explanation on what can be seen in the images in Figure 1—figure supplement 3 will be good. Also, can the images be shown at same pixel size/scale?

11) Has the classification accuracy been compared with any other multi-class classification method from literature?

12) As I understand, the classifier is trained using brightfield images. If the fluorescence images being used to capture any extra information for classification?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Intelligent classification of platelet aggregates by agonist type" for further consideration by eLife. Your revised article has been evaluated by Aleksandra Walczak (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) Comment 2: Please change "endothelial TXA2 receptors" to "TXA2 receptors" to avoid confusion.

2) In response to comment 3, the authors did not address this concern about the lack of locally produced inhibitors (NO, PGI2, ectoADPases etc): "Similarly platelets circulate in an environment with locally produced inhibitors (NO, prostacyclins, ADPases). Their effect has not been assessed, and this can be substantial (see Cattaneo et al., 2007)."

3) In response to comment 4, the authors appear to misstate Cazenave et al., 2004 which says "Citrate is the preferred anticoagulant for blood collection,.…. however, this method has certain disadvantages. In particular, the PRP preparation has a limited stability (no longer than 2 hours) and contains plasma proteins, including enzymes. In addition, human platelet-rich plasma (PRP) prepared from blood collected into trisodium citrate (3.8% w/v) has a depressed ionic calcium concentration, which can cause platelet aggregation and release of substances during centrifugation (2). To overcome these different problems, a centrifugation technique has been developed for the isolation and washing of platelets from human or rodent blood anticoagulated with acid-citrate-dextrose (ACD). The cells are resuspended in a physiological buffer under well-defined conditions, notably the presence of plasmatic ionic calcium concentrations (2 mM) and the absence of coagulation factors or other plasma components". Thus, physiological calcium (2 mM) needs to be added back to the platelet suspension to avoid artifacts. If the authors wish to study platelet-rich plasma, an alternate non-calcium chelating anti-coagulant, such as PPACK could be used.

Please make textual changes to your manuscript to indicate these caveats to your data.

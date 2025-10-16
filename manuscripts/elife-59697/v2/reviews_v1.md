# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Developmental Biology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59697.sa1](https://doi.org/10.7554/eLife.59697.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study presents a convolutional neural network (CNN) model for predicting ribozyme activity from primary sequence, based on measured regulatory activities of tens of thousands of ribozymes with diverse sequence features. The model trained on these sequences can be used to predict the regulatory activities of ribozymes containing ligand responsive aptamers (aptazymes).

Decision letter after peer review:

Thank you for submitting your article "A convolutional neural network for the prediction and forward design of ribozyme-based gene-control elements" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Detlef Weigel as the Reviewing and Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Natarajan Kannan (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The authors present attempts to build a convolutional neural network (CNN) model for predicting ribozyme activity from primary sequence. The authors started by measuring the regulatory activities of tens of thousands of ribozymes with diverse sequence features. A model trained on these sequences was used to predict the regulatory activities of ribozymes containing ligand responsive aptamers (aptazymes) for five different ligand:aptamer pairs. Experimental validation allowed for the identification of ribozyme switches for four aptamers.

The reviewers all appreciated the general approach, but raised concerns about the overall performance of the CNN, which might be caused by overfitting in the NN model and lack of ligand-binding experiments in high-throughput experiments. A related weakness that the CNN is not compared to other, more straightforward machine learning methods.

Essential revisions:

1. There is considerable indication that the NN model is overfitting. This is reflected from its dramatic performance drop when applying to the sTRSV hammerhead ribozyme and large variation of R2 (0.7 to 0.46) for 4-structure fold cross-validation.

2. The input coding of the NN model assumes that the 3D structures of all the library sequences are the same, which is almost certainly not the case. This is perhaps one of the main reasons for the poor generalization ability of the NN model. Related to this, the encoding of ribozyme structures assumes that LoopI and LoopII are always aligned in the same manner. It is unclear if this is a valid assumption and how this would impact the predictions. A further issue might be the predicted secondary structure, which is only about 70% correct, or that multiple folds are possible for the same RNA sequence. It is unclear how this is encoded in the model and whether aptamers of different folds (Y-loop for example) are represented in the training datasets. Along similar lines, have the authors considered encoding features of the ligand along with aptamer sequences? This might improve overall accuracy and account for the low performance observed for some aptamer ligand pairs such as the neomycin aptamers in the current model.

3. The authors perform a comprehensive comparison of the performance of a lasso model with CNN and show that the CNN model consistently performs better, even on ribozymes with novel loop structures. However, use of the CNN and the sole comparisons with the lasso model are not well justified. The authors should include comparisons with other methods such as SVM, random forest, or perhaps even ensemble methods.

4. Have the authors considered the following explanation for why their method has limited success: If the aim is to increase the activation ratio, the high-throughput experiments should include the experiments in the presence of ligands. Seeking sequences of low gene-regulatory activities and hoping for high activation ratios will not work as this paper shows.

5. The authors use a wide range of loop lengths and features to construct libraries for training and initial testing of their model, but find that their algorithm does not work as well for complex libraries. Did the authors try training their model on complex libraries including the libraries of 174,080 ribozyme sequences paired with aptamers? If not, this might be worth trying out.

Other points:

1. The introduction section and the significance value of the manuscript is primarily focused on RNA switches. Although the goal of the study was to facilitate finding ribozyme switches, the CNN was not very successful at doing so, beyond a few switches. The authors should revisit their narrative to focus on the background and applicability of the major outcome of their tool: finding regulatory ribozymes.

2. While the application of CNN for ribozyme design is very interesting, the "back-box" nature of the models precludes a direct application of these methods for ribozyme engineering and design. From the results, it is unclear what specific sequence and conformational features are contributing to the observed accuracy in predicting ribozyme activity. The authors should expand on the "explainable" aspects of their model to substantiate their design/engineering claims.

3. In the introduction, the authors refer to previously developed software for identifying RNA switches. It is unclear how the machine learning approach described here is better at predicting RNA switches than previously developed software tools pointed out by the authors. In fact, the other softwares identify more switches. The authors should bring out the benefits of using their algorithm over others.

4. By saying "However, none of the computational design tools described to date are based on gene regulatory platforms that function across a broad range of organisms.", it is implied that the current manuscript is also focused on finding broad-range switches. However, the new aptazymes described have been tested only in Yeast. It will make the manuscript better if the authors could test some of the high performing switches in human or other model organisms.

5. The abstract and the end paragraph of introduction mention different number of aptamer switches that were identified. 5 in the abstract and 4 in introduction and later sections.

6. At multiple places in the manuscript the authors attribute the lack of ligand dependent switch responsiveness to impermeability of the cells to specific ligands. There is however no direct evidence for this reasoning. In some cases, these statements also lack references, for example "…including the ability of tetracycline to more efficiently cross the cell membrane."

7. Several parts of the result section describe data without referring to the associated table/Figure.

8. "The method starts by using the RNA secondary structure prediction program RNAstructure (21) to determine the sequence of loops I and II of the ribozyme (Figure 3A)." What exactly is meant, as RNAstructure employs sequences to predict secondary structure?

9. "Next, the sequences of the two loops are analyzed to determine the nucleotides and their positions in the loops". Not clear. If the sequence is known, would their positions in the loops be known?

10. How are stem-loop interactions used as input in the 3-D image? Where does the interaction information come from? Was the input mapping onto the known 3D structure of hammerhead ribozymes? What about other ribozymes, do the authors input their 3D structures as well? Can the method be applied to a ribozyme with unknown 3D structures?

11. Is the average expression for 15 ribozymes shown in Figure 6A significantly different in the presence or absence of ligands? Box plots in Figure 6A needs p-values.

12. Since Figure 6B is a reanalysis of data shown in Fig6A, it can be moved to supplementary. Figure 6A will be more informative if the points were connected between the two box plots so the readers can observe switch in activity for every plotted ribozyme.

13. The high R-squared values (0.91 and 0.82) in Figure 4B are a bit surprising considering the poor fit especially in the head and tail regions. The authors need to check their fit and R-squared calculations. Likewise, R-square values reported in supplementary Figure 1A (0.92) and 1B (R-squared = 0.94) needs to be cross checked for accuracy.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A convolutional neural network for the prediction and forward design of ribozyme-based gene-control elements" for further consideration by eLife. Your revised article has been evaluated by Detlef Weigel (Deputy Editor) and two outside experts.

The manuscript has been improved but there is a smallish remaining issue that should be addressed:

Mean squared errors of the test set are still at least three times larger than those of the training set (Figure 3—figure supplement 1). Thus, the method is clearly biased toward the training set and it is not that clear how generalisable it is. It is a bit difficult to understand why this should be an advantage rather than a negative. In any case, please discuss and emphasize in the abstract and in the Discussion section, so that the reader has a clear sense of the limitation of the technique.

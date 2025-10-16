# Peer review - Round 1

Editors:
- Aleksandra M Walczak, École Normale Supérieure - PSL France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87949.3.sa0](https://doi.org/10.7554/eLife.87949.3.sa0)

In this valuable study, the authors use deep learning models to provide solid evidence that epithelial wounding triggers bursts of cell division at a characteristic distance away from the wound. The documentation provided by the authors should allow other scientists to readily apply these methods, which are particularly appropriate where unsupervised machine-learning algorithms have difficulties.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87949.3.sa1](https://doi.org/10.7554/eLife.87949.3.sa1)

The authors present a number of deep learning models to analyse the dynamics of epithelia. In this way they want to overcome the time-consuming manual analysis of such data and also remove a potential operator bias. Specifically, they set up models for identifying cell division events and cell division orientation. They apply these tools to the epithelium of the developing Drosophila pupal wing. They confirm a linear decrease of the division density with time and identify a burst of cell division after healing of a wound that they had induced earlier. These division events happen a characteristic time after and a characteristic distance away from the wound. These characteristic quantities depend on the size of the wound.

Strengths:

The methods developed in this work achieve the goals set by the authors and are a very helpful addition to the toolbox of developmental biologists. They could potentially be used on various developing epithelia. The evidence for the impact of wounds on cell division is compelling.

The methods presented in this work should prove to be very helpful for quantifying cell proliferation in epithelial tissues.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87949.3.sa2](https://doi.org/10.7554/eLife.87949.3.sa2)

In this manuscript, the authors propose a computational method based on deep convolutional neural networks (CNNs) to automatically detect cell divisions in two-dimensional fluorescence microscopy timelapse images. Three deep learning models are proposed to detect the timing of division, predict the division axis, and enhance cell boundary images to segment cells before and after division. Using this computational pipeline, the authors analyze the dynamics of cell divisions in the epithelium of the Drosophila pupal wing and find that a wound first induces a reduction in the frequency of division followed by a synchronised burst of cell divisions about 100 minutes after its induction.

Comments on revised version:

Regarding the Reviewer's 1 comment on the architecture details, I have now understood that the precise architecture (number/type of layers, activation functions, pooling operations, skip connections, upsampling choice...) might have remained relatively hidden to the authors themselves, as the U-net is built automatically by the fast.ai library from a given classical choice of encoder architecture (ResNet34 and ResNet101 here) to generate the decoder part and skip connections.

Regarding the Major point 1, I raised the question of the generalisation potential of the method. I do not think, for instance, that the optimal number of frames to use, nor the optimal choice of their time-shift with respect to the division time (t-n, t+m) (not systematically studied here) may be generic hyperparameters that can be directly transferred to another setting. This implies that the method proposed will necessarily require re-labeling, re-training and re-optimizing the hyperparameters which directly influence the network architecture for each new dataset imaged differently. This limits the generalisation of the method to other datasets, and this may be seen as in contrast to other tools developed in the field for other tasks such as cellpose for segmentation, which has proven a true potential for generalisation on various data modalities. I was hoping that the authors would try themselves testing the robustness of their method by re-imaging the same tissue with slightly different acquisition rate for instance, to give more weight to their work.

In this regard, and because the authors claimed to provide clear instructions on how to reuse their method or adapt it to a different context, I delved deeper into the code and, to my surprise, felt that we are far from the coding practice of what a well-documented and accessible tool should be.

To start with, one has to be relatively accustomed with Napari to understand how the plugin must be installed, as the only thing given is a pip install command (that could be typed in any terminal without installing the plugin for Napari, but has to be typed inside the Napari terminal, which is mentioned nowhere). Surprisingly, the plugin was not uploaded on Napari hub, nor on PyPI by the authors, so it is not searchable/findable directly, one has to go to the Github repository and install it manually. In that regard, no description was provided in the copy-pasted templated files associated to the napari hub, so exporting it to the hub would actually leave it undocumented.

Regarding now the python notebooks, one can fairly say that the "clear instructions" that were supposed to enlighten the code are really minimal. Only one notebook "trainingUNetCellDivision10.ipynb" has actually some comments, the other have (almost) none nor title to help the unskilled programmer delving into the script to guess what it should do. I doubt that a biologist who does not have a strong computational background will manage adapting the method to its own dataset (which seems to me unavoidable for the reasons mentioned above).

Finally regarding the data, none is shared publicly along with this manuscript/code, such that if one doesn't have a similar type of dataset - that must be first annotated in a similar manner - one cannot even test the networks/plugin for its own information. A common and necessary practice in the field - and possibly a longer lasting contribution of this work - could have been to provide the complete and annotated dataset that was used to train and test the artificial neural network. The basic reason is that a more performant, or more generalisable deep-learning model may be developed very soon after this one and for its performance to be fairly compared, it requires to be compared on the same dataset. Benchmarking and comparison of methods performance is at the core of computer vision and deep-learning.

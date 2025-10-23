# Peer review - Round 1

Editors:
- Gordon J Berman, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.95709.3.sa0](https://doi.org/10.7554/eLife.95709.3.sa0)

This useful study introduces a deep learning-based algorithm that tracks animal postures with reduced drift by incorporating transformers for more robust keypoint detection. The efficacy of this new algorithm for single-animal pose estimation was demonstrated through comparisons with two popular algorithms. The strength of evidence is solid but would benefit from consideration of issues in multi-animal tracking. This work will be of interest to those interested in animal behavior tracking.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95709.3.sa1](https://doi.org/10.7554/eLife.95709.3.sa1)

Summary:

The authors present a new model for animal pose estimation. The core feature they highlight is the model's stability compared to existing models in terms of keypoint drift. The authors test this model across a range of new and existing datasets. The authors also test the model with two mice in the same arena. For the single animal datasets the authors show a decrease in sudden jumps in keypoint detection and the number of undetected keypoints compared with DeepLabCut and SLEAP. Overall average accuracy, as measured by root mean squared error, generally shows generally similar but sometimes superior performance to DeepLabCut and better performance compared to SLEAP. The authors confusingly don't quantify the performance of pose estimation in the multi (two) animal case instead focusing on detecting individual identity. This multi-animal model is not compared with the model performance of the multi-animal mode of DeepLabCut or SLEAP.

Strengths:

The major strength of the paper is successfully demonstrating a model that is less likely to have incorrect large keypoint jumps compared to existing methods. As noted in the paper, this should lead to easier-to-interpret descriptions of pose and behavior to use in the context of a range of biological experimental workflows.

Weaknesses:

There are two main types of weaknesses in this paper. The first is a tendency to make unsubstantiated claims that suggest either model performance that is untested or misrepresents the presented data, or suggest excessively large gaps in current SOTA capabilities. One obvious example is in the abstract when the authors state ADPT "significantly outperforms the existing deep-learning methods, such as DeepLabCut, SLEAP, and DeepPoseKit." All tests in the rest of the paper, however, only discuss performance with DeepLabCut and SLEAP, not DeepPoseKit. At this point, there are many animal pose estimation models so it's fine they didn't compare against DeepPoseKit, but they shouldn't act like they did. Similar odd presentation of results are statements like "Our method exhibited an impressive prediction speed of 90{plus minus}4 frames per second (fps), faster than DeepLabCut (44{plus minus}2 fps) and equivalent to SLEAP (106{plus minus}4 fps)." Why is 90{plus minus}4 fps considered "equivalent to SLEAP (106{plus minus}4 fps)" and not slower? I agree they are similar but they are not the same. The paper's point of view of what is "equivalent" changes when describing how "On the single-fly dataset, ADPT excelled with an average mAP of 92.83%, surpassing both DeepLabCut and SLEAP (Figure 5B)" When one looks at Figure 5B, however, ADPT and DeepLabCut look identical. Beyond this, oddly only ADPT has uncertainty bars (no mention of what uncertainty is being quantified) and in fact, the bars overlap with the values corresponding to SLEAP and DeepPoseKit. In terms of making claims that seem to stretch the gaps in the current state of the field, the paper makes some seemingly odd and uncited statements like "Concerns about the safety of deep learning have largely limited the application of deep learning-based tools in behavioral analysis and slowed down the development of ethology" and "So far, deep learning pose estimation has not achieved the reliability of classical kinematic gait analysis" without specifying which classical gait analysis is being referred to. Certainly, existing tools like DeepLabCut and SLEAP are already widely cited and used for research.

The other main weakness in the paper is the validation of the multi-animal pose estimation. The core point of the paper is pose estimation and anti-drift performance and yet there is no validation of either of these things relating to multi-animal video. All that is quantified is the ability to track individual identity with a relatively limited dataset of 10 mice IDs with only two in the same arena (and see note about train and validation splits below). While individual tracking is an important task, that literature is not engaged with (i.e. papers like Walter and Couzin, eLife, 2021: https://doi.org/10.7554/eLife.64000) and the results in this paper aren't novel compared to that field's state of the art. On the other hand, while multi-animal pose estimation is also an important problem the paper doesn't engage with those results either. The two methods already used for comparison in the paper, SLEAP and DeepPoseKit, already have multi-animal modes and multi-animal annotated datasets but none of that is tested or engaged with in the paper. The paper notes many existing approaches are two-step methods, but, for practitioners, the difference is not enough to warrant a lack of comparison. The authors state that "The evaluation of our social tracking capability was performed by visualizing the predicted video data (see supplement Videos 3 and 4)." While the authors report success maintaining mouse ID, when one actually watches the key points in the video of the two mice (only a single minute was used for validation) the pose estimation is relatively poor with tails rarely being detected and many pose issues when the mice get close to each other.

Finally, particularly in the methods section, there were a number of places where what was actually done wasn't clear. For example in describing the network architecture, the authors say "Subsequently, network separately process these features in three branches, compute features at scale of one-fourth, one-eight and one-sixteenth, and generate one-eight scale features using convolution layer or deconvolution layer." Does only the one-eight branch have deconvolution or do the other branches also? Similarly, for the speed test, the authors say "Here we evaluate the inference speed of ADPT. We compared it with DeepLabCut and SLEAP on mouse videos at 1288 x 964 resolution", but in the methods section they say "The image inputs of ADPT were resized to a size that can be trained on the computer. For mouse images, it was reduced to half of the original size." Were different image sizes used for training and validation? Or Did ADPT not use 1288 x 964 resolution images as input which would obviously have major implications for the speed comparison? Similarly, for the individual ID experiments, the authors say "In this experiment, we used videos featuring different identified mice, allocating 80% of the data for model training and the remaining 20% for accuracy validation." Were frames from each video randomly assigned to the training or validation sets? Frames from the same video are very correlated (two frames could be just 1/30th of a second different from each other), and so if training and validation frames are interspersed with each other validation performance doesn't indicate much about performance on more realistic use cases (i.e. using models trained during the first part of an experiment to maintain ids throughout the rest of it.)

Editors' note: None of the original reviewers responded to our request to re-review the manuscript. The attached assessment statement is the editor's best attempt at assessing the extent to which the authors addressed the outstanding concerns from the previous round of revisions.

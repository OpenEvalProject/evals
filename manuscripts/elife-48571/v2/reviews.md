# Peer review - Round 1

Editors:
- Timothy O'Leary, University of Cambridge United Kingdom

Reviewers:
- Josh W Shaevitz, Princeton University United States

## Review text

DOI: [10.7554/eLife.48571.032](https://doi.org/10.7554/eLife.48571.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "DeepFly3D, a deep learning-based approach for 3D limb and appendage tracking in tethered, adult Drosophila" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Josh W Shaevitz (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Both reviewers agreed that this tools and resources article can potentially be of use to the field. By automating pose tracking a large amount of data can be extracted from experiments, enabling new scientific questions to be addressed.

However, a number of key issues with the current study were identified and outlined in the reviewer comments below. In summary, the current manuscript:

1) Lacks a comprehensive discussion of how experimental choices, e.g. camera number, affect tracking error

2) Reports a very large tracking error using a much larger training set than current state-of-the-art 2D tracking algorithms. This needs to be accounted for.

3) Lacks some key references in the field and comparison with other approaches.

Reviewer #1:

Günel et al. report the development of a new toolkit to perform 3D pose estimation on tethered flies. While the toolkit is certainly bound to find utility, there are not major computational advances or insights within the work. While deep learning approaches for animal pose estimation is a "young field" in neuroscience/ethology (i.e. (Pereira et al., 2019, Mathis et al., 2018, Nath et al., 2019), it would be important for the authors to clarify their contribution in light of this. Namely, the authors should clearly discuss the major points that potential users care about: (1) accuracy of the tool, (2) amount of data required to train networks, if required, (3) speed, and (4) usability.

While DeepFly3D provides very nice user interfaces for the toolkit, it does suffer in the other three main categories.

1) Accuracy. The authors report a 13.9-pixel error on 480 by 920 images, and consider the PCK to be 50 pixels, which is nearly as long as a leg segment – not the width! I would argue this is far too lenient of a threshold. Additionally, two points the authors need to address (1) The RMSE would be more meaningful with an estimate of the human labeling variability (i.e. what is the best the network could do?), and (2) why, given so much training data, is the performance not as accurate as other approaches (LEAP, DeepLabCut)?

i.e. in reference to:

– "… 480× 960 pixels. The test dataset included challenging frames and occasional motion blur to increase the difficulty of pose estimation. For training, we used a final training dataset of 37,000 frames, an overwhelming majority of which were first automatically corrected using pictorial structures. On test data, we achieved a Root Mean Square Error (RMSE) of 13.9 pixels"

– The error is quite a bit larger than other animal pose estimation approaches, i.e. on 480x640 on 3D freely moving flies DeepLabCut used ~560 frames with ~4-pixel error on 682 × 540 frames. LEAP: ~500 images to achieve ~3-pixel error on 192 × 192-pixel frames with flies. While I appreciate that a direct comparison is not fully straightforward, and the authors do not use "easy" points to compute the pixel error, the authors absolutely should discuss/address this point.

2) The amount of data. As this network was trained on ~37K images, it is likely expected that the end-user will use these authors pre-trained network or the human pre-trained network. Namely, creating a large dataset seems infeasible when other options exist that require much less data. Namely, DeepLabCut reports 50-200 for most applications, and LEAP requires only ~500-1,500, which is nearly a factor of 10 less images to match similar performance (I understand that 2K are hand-labeled, while the rest are not, but even that is a 4X increase over the best method, i.e. DeepLabCut). Thus, the amount of training data for the performance is very high, given current alternatives. These limitations should be discussed.

3) Speed. There is no report of the speed of the network, thus the authors should benchmark the performance on video analysis speed (only network training time is reported).

4) Since the authors needed a lot of labeled data, making this a most useful as a specialized network for tethered flies, i.e. much like OpenPose has specific networks for hands (which they could clarify). Therefore, if they provide the network weights they should show the network is useable for other labs data.

5) 3D pose in the literature. The authors do not discuss Nath et al., which is a 3D extension of DeepLabCut (bioRxiv Nov 2018, and Nature Protocols, 2019) and given it's a small field, the authors should not claim theirs is the first to do 3D pose. Beyond deep learning multiple 3D pose estimation papers exist in Neuroscience (ie. Mimica et al., 2018 – Efficient cortical coding of 3D posture in freely behaving rats).

Therefore language like this should be modified:

"However, algorithms for reliably estimating 3D pose in such small animals have not yet been developed.…"

"However, these measurements have been restricted to 2D pose in freely behaving animals"

"We demonstrate more accurate unsupervised behavioral embedding using 3D joint angles rather than commonly used 2D pose data. Thus, DeepFly3D enables the automated acquisition of behavioral measurements at an unprecedented level of resolution for a variety of biological application"

(also here "resolution" should be edited; it is not that DeepFly3D is more accurate than other alternatives.)

However, I do think these authors have a nice solution, so I do find it very fair that they state they have an alternative 3D approach, (and can highlight the advantages) solution to multi-camera estimation in body- or head- fixed animals. However, again, sparse bundle adjustment is not a new technique, so the authors should discuss this in light of the literature.

6) "Here we present DeepFly3D, a software that infers the 3D pose of tethered, adult Drosophila-or other animals-using multiple camera images" – they don't quantify performance for other animals, so this should be dropped from the Abstract.

7) "DeepLabCut provides a user-friendly interface to DeepCut, a state-of-the-art human pose estimation network" (DeepCut should be DeeperCut, which is different than DeepCut).

8) "Calibration without targets" is misleading. The authors do calibrate; they just use the rigid body of the fly that has set distances per limb segment. To note, this isn't always doable for other animals/videos, again another argument to drop the random "this can be used for anything" language…

Reviewer #2:

The manuscript by Gunel et al. describes a new tool for 3D pose tracking that automatically combines multiple 2D images from different viewing angles while also learning the camera model. There has been a flurry of recent papers that use deep neural networks to track pose in 2D images. This manuscript improves on these by generating 3D positions for each body part that is tracked using a combination of various algorithms that have been developed for human pose tracking. In addition, the authors provide a simple GUI that allows for part labeling and prediction correction. Overall the paper is well written and the most aspects of the system described and justified.

My only major issue is that the experimental setup is not discussed or motivated. In particular, I would like to see more information about the choices/requirements for the number of cameras and other considerations. Why do the authors use 7 cameras? I assume that with fewer cameras you get more error/occlusions/etc. Can you investigate these effects quantitatively? How should a researcher choose the number of cameras (recording from 7 cameras in synch is difficult)?

In addition, I would suggest that the authors show the distribution of 3D localization errors. Is this isotropic? Is it the same for all body parts (the Discussion subsection “Learning the parameters” suggests not)?

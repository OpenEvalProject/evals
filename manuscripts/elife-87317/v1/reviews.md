# Peer review - Round 1

Editors:
- Kianoush Nazarpour, University of Edinburgh United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87317.3.sa0](https://doi.org/10.7554/eLife.87317.3.sa0)

This paper's importance lies in its integration of movement and contextual information to control a virtual arm for individuals with upper-limb differences. The provided evidence convincingly demonstrates the approach's feasibility for manipulating a single object shape in different orientations within a virtual environment. However, additional improvements are needed for this proof-of-concept neuro-model to fulfil practical requirements.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87317.3.sa1](https://doi.org/10.7554/eLife.87317.3.sa1)

Segas et al. present a novel solution to an upper-limb control problem which is often neglected by academia. The problem the authors are trying to solve is how to control the multiple degrees of freedom of the lower arm to enable grasp in people with transhumeral limb loss. The proposed solution is a neural network based approach which uses information from the position of the arm along with contextual information which defines the position and orientation of the target in space. Experimental work is presented, based on virtual simulations and a telerobotic proof of concept.

The strength of this paper is that it proposes a method of control for people with transhumeral limb loss which does not rely upon additional surgical intervention to enable grasping objects in the local environment. A challenge the work faces is that it can be argued that a great many problems in upper limb prosthesis control can be solved given precise knowledge of the object to be grasped, its relative position in 3D space and its orientation. It is difficult to know how directly results obtained in a virtual environment will translate to real world impact. Some of the comparisons made in the paper are to physical systems which attempt to solve the same problem. It is important to note that real world prosthesis control introduces numerous challenges which do not exist in virtual spaces or in teleoperation robotics.

The authors claim that the movement times obtained using their virtual system, and a teleoperation proof of concept demonstration, are comparable to natural movement times. The speed of movements obtained and presented are easier to understand by viewing the supplementary materials prior to reading the paper. The position of the upper arm and a given target are used as input to a classifier, which determines the positions of the lower arm, wrist and the end effector. The state of the virtual shoulder in the pick and place task is quite dynamic and includes humeral rotations which would be challenging to engineer in a real physical prosthesis above the elbow. Another question related to the pick and place task used is whether or not there are cases where both the pick position and the place position can be reached via the same, or very similar, shoulder positions? i.e. with the shoulder flexion-extension and abduction-adduction remaining fixed, can the ANN use the remaining five joint angles to solve the movement problem with little to no participant input, simply based on the new target position? If this was the case, movements times in the virtual space would present a very different distribution to natural movements, while the mean values could be similar. The arguments made in the paper could be supported by including individual participant data showing distributions of movement times and the distances travelled by the end effector where real movements are compared to those made by an ANN.

In the proposed approach users control where the hand is in space via the shoulder. The position of the upper arm and a given target are used as input to a classifier, which determines the positions of the lower arm, wrist and the effector. The supplementary materials suggest the output of the classifier occurs instantaneously, in that from the start of the trial the user can explore the 3D space associated with the shoulder in order to reach the object. When the object is reached a visual indicator appears. In a virtual space this feedback will allow rapid exploration of different end effector positions which may contribute to the movement times presented. In a real world application, movement of a distal end-effector via the shoulder is not to be as graceful and a speed accuracy trade off would be necessary to ensure objects are grasped, rather than knocked or moved.

Another aspect of the movement times presented which is of note, although it is not necessarily incorrect, is that the virtual prosthesis performance is close too perfect. In that, at the start of each trial period, either pick or place, the ANN appears to have already selected the position of the five joints it controls, leaving the user to position the upper arm such that the end effector reaches the target. This type of classification is achievable given a single object type to grasp and a limited number of orientations, however scaling this approach to work robustly in a real world environment will necessitate solving a number of challenges in machine learning and in particular computer vision which are not trivial in nature. On this topic, it is also important to note that, while very elegant, the teleoperation proof of concept of movement based control does not seem to feature a similar range of object distance from the user as the virtual environment. This would have been interesting to see and I look forward to seeing further real world demonstrations in the authors future work.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87317.3.sa2](https://doi.org/10.7554/eLife.87317.3.sa2)

Segas et al motivate their work by indicating that none of the existing myoelectric solution for people with trans-humeral limb difference offer four active degrees of freedom, namely forearm flexion/extension, forearm supination/pronation, wrist flexion/extension, and wrist radial/ulnar deviation. These degrees of freedom are essential for positioning the prosthesis in the correct plan in the space before a grasp can be selected. They offer a controller based on the movement of the stump.

The proposed solution is elegant for what it is trying to achieve in a laboratory setting. Using a simple neural network to estimate the arm position is an interesting approach, despite the limitations/challenges that the approach suffers from, namely, the availability of prosthetic hardware that offers such functionality, information about the target and the noise in estimation if computer vision methods are used. Segas et al indicate these challenges in the manuscript, although they could also briefly discuss how they foresee the method could be expanded to enable a grasp command beyond the proximity between the end-point and the target. Indeed, it would be interesting to see how these methods can be generalise to more than one grasp.

One bit of the results that is missing in the paper is the results during the familiarisation block. If the methods in "intuitive" I would have thought no familiarisation would be needed. Do participants show any sign of motor adaptation during the familiarisation block?

In Supplementary Videos 3 and 4, how would the authors explain the jerky movement of the virtual arm while the stump is stationary? How would be possible to distinguish the relative importance of the target information versus body posture in the estimation of the arm position? This does not seem to be easy/clear to address beyond looking at the weights in the neural network.

I am intrigued by how the Generic ANN model has been trained, i.e. with the use of the forward kinematics to remap the measurement. I would have taught an easier approach would have been to create an Own model with the native arm of the person with the limb loss, as all your participants are unilateral (as per Table 1). Alternatively, one would have assumed that your common model from all participants would just need to be 'recalibrated' to a few examples of the data from people with limb difference, i.e. few shot calibration methods.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87317.3.sa3](https://doi.org/10.7554/eLife.87317.3.sa3)

This work provides a new approach to simultaneously control elbow and wrist degrees of freedom using movement based inputs, and demonstrate performance in a virtual reality environment. The work is also demonstrated using a proof-of-concept physical system. This control algorithm is in contrast to prior approaches which electrophysiological signals, such as EMG, which do have limitations as described by the authors. In this work, the movements of proximal joints (eg shoulder), which generally remain under voluntary control after limb amputation, are used as input to neural networks to predict limb orientation. The results are tested by several participants within a virtual environment, and preliminary demonstrated using a physical device, albeit without it being physically attached to the user.

Strengths:

Overall, the work has several interesting aspects. Perhaps the most interesting aspect of the work is that the approach worked well without requiring user calibration, meaning that users could use pre-trained networks to complete the tasks as requested. This could provide important benefits, and if successfully incorporated into a physical prosthesis allow the user to focus on completing functional tasks immediately. The work was also tested with a reasonable number of subjects, including those with limb-loss. Even with the limitations (see below) the approach could be used to help complete meaningful functional activities of daily living that require semi-consistent movements, such as feeding and grooming.

Weaknesses:

While interesting, the work does have several limitations. In this reviewer's opinion, main limitations are: the number of 'movements' or tasks that would be required to train a controller that generalized across more tasks and limb-postures. The authors did a nice job spanning the workspace, but the unconstrained nature of reaches could make restoring additional activities problematic. This remains to be tested.

The weight of a device attached to a user will impact the shoulder movements that can be reliably generated. Testing with a physical prosthesis will need to ensure that the full desired workspace can be obtained when the limb is attached, and if not, then a procedure to scale inputs will need to be refined.

The reliance on target position is a complicating factor in deploying this technology. It would be interesting to see what performance may be achieved by simply using the input target positions to the controller and exclude the joint angles from the tracking devices (eg train with the target positions as input to the network to predict the desired angles).

Treating the humeral rotation degree of freedom is tricky, but for some subjects, such as those with OI, this would not be as large of an issue. Otherwise, the device would be constructed that allowed this movement.

Overall, this is an interesting preliminary study with some interesting aspects. Care must be taken to systematically evaluate the method to ensure clinical impact.

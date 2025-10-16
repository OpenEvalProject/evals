# Peer review - Round 1

Editors:
- Eve Marder, Brandeis University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29315.017](https://doi.org/10.7554/eLife.29315.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Computer assisted detection of axonal bouton structural plasticity in in vivo time-lapse images" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Eve Marder as the Senior Editor and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Sen Song (Reviewer #1); Albert Cardona (Reviewer #2). A further reviewer remains anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors proposed new algorithms to analyze in vivo two-photon time-lapse images for axonal bouton structural plasticity and validated the method against EM reconstructions of the same tissue. The manuscript reports on a new method for quantifying synaptic boutons in light-microscopy images of fluorescently labeled axons, and validates the method and parameter choices by using correlative light-electron microscopy, providing the nanometer-scale reconstruction of axons and synaptic surfaces of the micrometer-scale light-microscopy images. The method models sources of variability, both controllable and non-controllable, while also acknowledging and including the inherent ambiguity of synaptic boutons in predicting the presence of a synaptic surface (not all boutons house synapses or, as the author's put it, postsynaptic densities). The normalization approach is appropriate and accurate, and its structure reveals the careful, neuroanatomy-based reasoning that led to its design. The method applies to both small varicosities and varying imaging conditions, including low-intensity and low-contrast conditions, and reports a precision and recall good enough that, together with the modeling of variability and the ability to track varicosities over time on the same axons, essentially sets the stage for fully-automated estimation of synaptic weights from light-microscopy images of brain tissue for chronic studies.

Essential revisions:

1) One of the issues that arose during the review is that some of your previously published methods are inaccessible without paying exorbitant fees to other publishers. Consequently, please include all of the methods you used in detail here, so that this paper stands alone and exists in the OPEN ACCESS world with all of its methods. eLife does not restrict the space that can be used for methods, so it will be a service to the community to have the methods here. Among specific issues raised by the reviewers:

a) There is an insufficiently detailed EM fixation and counterstaining protocol: no concentrations given for aldehydes, osmium, uranyl acetate, and no specifications on the individual steps.

b) More detail on the trace optimization method.

c) No open source code repository is reported, which would be critical to distributing the software to facilitate the application of this novel method and provide commit hashes for reference when reporting the use of the method, towards ensuring reproducibility of results. Attaching the source code to the paper is an old practice from when public source code repositories were rare or hard to setup, and while the practice ensures archiving of the source code, it is not conducive to further corrections, extensions or modifications. Which source version control repository hosts the code, and what hash / commit number corresponds to the attached code zip file? This is critical for eLife publication!

2) Please address the issue of whether the laplacian of gaussian filter for detection of boutons introduces biases in estimating bouton intensities. Figure 4 addresses some of those issues, but the profile intensities there are after several further steps of processing. This issue need to be explored in a bit more depth by perhaps comparing with some other methods. Address how the parameters were chosen for the LOG filter.

3) One reviewer says, "The detection of putative boutons based on the Backward-Stepwise Subset Selection method is also novel. I think the fitting of foreground peaks using a variable size gaussian filter is a very good idea. But I am less convinced of fitting the background peaks also with Gaussian functions. There is no a priori reason why the background is also peaky. Have the authors explored other functions for fitting the background. What is the physical intuition of the background peaks?"

4) For the shaft intensity, why did you choose the positions where the boutons were present for measurement? It seems more intuitive to measure from areas which are devoid of boutons. The current method seems more like an average bouton intensity. Normalizing the image by this kind of quantity suffers from one drawback, which is if a large fraction of boutons are gained or lost, this might lead to a bias.

5) Fitting the bouton gain and loss functions using a probabilistic function is a very good idea. But it is not very clear how this could benefit final biological measurements and interpretation. Is it useful for taking/getting more meaningful interpretation for different amounts of measurement noises? Some discussion of this would be useful.

6) The correlation with EM looks quite good, but is it better than previous methods? Some comparison would be useful.

Optional: One reviewer felt that one potential way to increase the impact is to demonstrate its robustness for data previously published by other labs. Other reviewers did not feel this was necessary, but we wanted you to think about this.

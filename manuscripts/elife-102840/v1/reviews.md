# Peer review - Round 1

Editors:
- Richard Naud, University of Ottawa Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.102840.3.sa0](https://doi.org/10.7554/eLife.102840.3.sa0)

This important paper takes a novel approach to the problem of automatically reconstructing long-range axonal projections from stacks of images. The key innovation is to separate the identification of sections of an axon from the statistical rules used to constrain global structure. The authors provide compelling evidence that their method is a significant improvement over existing measures in circumstances where the labelling of axons and dendrites is relatively dense.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.102840.3.sa1](https://doi.org/10.7554/eLife.102840.3.sa1)

Summary:

The authors introduce a novel algorithm for the automatic identification of long-range axonal projections. This is an important problem as modern high-throughput imaging techniques can produce large amounts of raw data, but identifying neuronal morphologies and connectivities requires large amounts of manual work. The algorithm works by first identifying points in three-dimensional space corresponding to parts of labelled neural projections, these are then used to identify short sections of axon using an optimisation algorithm and the prior knowledge that axonal diameters are relatively constant. Finally, a statistical model that assumes axons tend to be smooth is used to connect the sections together into complete and distinct neural trees. The authors demonstrate that their algorithm is far superior to existing techniques, especially when a dense labelling of the tissue means that neighbouring neurites interfere with the reconstruction. Despite this improvement, however, the accuracy of reconstruction remains below 90%, so manual proof-reading is still necessary to produce accurate reconstructions of axons.

Strengths:

The new algorithm combines local and global information to make a significant improvement on the state-of -the-art for automatic axonal reconstruction. The method could be applied more broadly and might have applications to reconstructions of electron microscopy data, where similar issues of high-throughput imaging and relatively slow or inaccurate reconstruction remain.

Weaknesses:

There are three weaknesses with the algorithm and manuscript.

(1) The best reconstruction accuracy is below 90%, which does not fully solve the problem of needing manual proof-reading.

(2) The 'minimum information flow tree' model the authors use to construct connected axonal trees has the potential to bias data collection. In particular, the assumption that axons should always be as smooth as possible is not always correct. This is a good rule-of-thumb for reconstructions, but real axons in many systems can take quite sharp turns and this is also seen in the data presented in the paper (Fig 1C). I would like to see explicit acknowledgement of this bias in the current manuscript and ideally a relaxation of this rule in any later versions of the algorithm.

(3) The writing of the manuscript is not always as clear as it could be. The manuscript would benefit from careful copy editing for language, and the Methods section in particular should be expanded to more clearly explain what each algorithm is doing. The pseudo code of the Supplemental Information could be brought into the Methods if possible as these algorithms are so fundamental to the manuscript.

Comments on revisions: I have no further comments or recommendations.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.102840.3.sa2](https://doi.org/10.7554/eLife.102840.3.sa2)

The authors have addressed my comments in this revised version of their manuscript. PointTree is an improved method for the reconstruction of neuronal anatomy that will be useful for neuroscientists.

In this manuscript, Cai et al. introduce PointTree, a new automated method for the reconstruction of complex neuronal projections. This method has the potential to drastically speed up the process of reconstructing complex neurites. The authors use semi-automated manual reconstruction of neurons and neurites to provide a 'ground-truth' for comparison between PointTree and other automated reconstruction methods. The reconstruction performance is evaluated for precision, recall and F1-score and positions. The performance of PointTree compared to other automated reconstruction methods is impressive based on these 3 criteria.

As an experimentalist, I will not comment on the computational aspects of the manuscript. Rather, I am interested in how PointTree's performance decrease in noisy samples. This is because many imaging datasets contain some level of background noise for which the human eye appears essential for accurate reconstruction of neurites. Although the samples presented in Figure 5 represent an inherent challenge for any reconstruction method, the signal to noise ratio is extremely high (also the case in all raw data images in the paper). It would be interesting to see how PointTree's performance change in increasingly noisy samples, and for the author to provide general guidance to the scientific community as to what samples might not be accurately reconstructed with PointTree.

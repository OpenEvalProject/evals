# Peer review - Round 1

Editors:
- Albert Cardona, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.99848.4.sa0](https://doi.org/10.7554/eLife.99848.4.sa0)

This important work presents a self-supervised method for the segmentation of 3D cells in fluorescent microscopy images, conveniently packaged as a Napari plugin and tested on an annotated dataset. The segmentation method is solid and compares favorably to other learning-based methods and Otsu thresholding on four datasets, offering the possibility of eliminating time-consuming data labeling to speed up quantitative analysis. This work will be of interest to a wide variety of laboratories analysing fluorescently labeled images.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99848.4.sa1](https://doi.org/10.7554/eLife.99848.4.sa1)

The manuscript now compares the WNet3D quantitatively against other methods on all four datasets:

Figure 1b shows results on the mouse cortex dataset, comparing StarDist, CellPose, SegResNet, SwinUNetR against self-supervised (or learning-free methods) WNet3D and Otsu thresholding.

Figure 2b shows results on an unnamed dataset (presumably the mouse cortex dataset), comparing StarDist, CellPose, SegResNet, SwinUNetR with different levels of training data against WNet3D.

Figure 3 shows results on three datasets (Platynereis-ISH-Nuclei-CBG, Platynereis-Nuclei-CBG, and Mouse-Skull-Nuclei-CBG), comparing StarDist, CellPose against WNet3D and Otsu thresholding.

It is unclear whether the Otsu thresholding baseline was given the same post-processing as the WNet3D. Figure 1b shows two versions for WNet3D ("WNet3D - No artifacts" and "WNet3D"), but only one for Otsu thresholding. Given that post-processing (or artifact removal) seems to have a substantial impact on accuracy, the authors should clarify whether the Otsu thresholding results were treated in the same way and if Otsu thresholding was not post-processed. Figure 2a would also benefit from including the thresholding results (with and without artifact removal).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99848.4.sa2](https://doi.org/10.7554/eLife.99848.4.sa2)

The authors have now addressed the most important points, and they include more comprehensive evaluation of their method and comparisons to other approaches for multiple datasets.

Some points would benefit from clarification:

- Figure 1B now compares "Otsu thresholding", "WNet 3D - No artifacts" and "WNet 3d". Why don't you also report the score for "Otsu thresholding - No Artifacts"? To my understanding this is a post-processing operation to remove small and very large objects, so it could easily be applied to the Otsu thresholding. Given the good results for Otsu thresholding alone (quite close F1-score to WNet 3d), it seems like DL might not really be necessary at all for this dataset and including "Otsu thresholding - No artifacts" would enable evaluating this point.

- CellPose and StarDist perform poorly in all the experiments performed by the authors. In almost all cases they underperform Otsu thresholding, which is in most cases on par with the WNet results (except for "Mouse Skull Nuclei CBG"). This is surprising and contradicts the collective expertise of the community: good CellPose and StarDist models can be trained for the 3D instance segmentation tasks studied here. Perhaps these methods were not trained in an optimal way. Seems unlikely that it is not possible to get much better CellPose or StarDist models for these tasks (current versions are on par or much worse than Otsu!), as I have applied both of these models successfully in similar settings. Specifically, it seems unlikely that the developers of CellPose or StarDist would obtain similarly poor scores on the same data (note I am not one of the developers).

The current experiments still highlight an interesting aspect: the problem of training / fine-tuning these methods correctly on new data and the technical challenges associated with this. But the reported results should by no means be taken as a fair assessment of the capabilities of StarDist or CellPose.

Please note that I did not have time to test the Napari plugin again, so I did not evaluate whether it improved in usability.

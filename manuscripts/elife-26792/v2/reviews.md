# Peer review - Round 1

Editors:
- Christian S. Hardtke, University of Lausanne , Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26792.023](https://doi.org/10.7554/eLife.26792.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Live tracking of moving samples in confocal microscopy for vertically grown plant roots" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Hardtke as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

In principal, the reviewers found the set-up reported in your manuscript useful. However, they are concerned about its scope as a resource at this point and would like to see further improvements and documentation:

While there was consensus that a resource should be rather easily implemented/applied, the conversion to a vertical microscope is not straightforward (and probably would result in loss of warranty for confocal systems). Yet, as this is of course unavoidable here, at least the tracking part should become easier to implement and we therefore would like to ask you to provide the software in an open format.

Please discuss the limitations of the set up in more depth and make each aspect very transparent such that it is truly informative for the community.

An important point is that the resource should demonstrate that its use leads to new insight into root development beyond what was previously possible. This might be achieved by a more in depth analysis of KNOLLE behavior, or by additional pertinent experiments. For example, can it be used to follow markers in inner tissue layers across time?

For details, refer to the reviews below, and please also address all other points brought up by the reviewers.

Reviewer #1:

This is an exciting and innovative manuscript which addresses a key imaging obstacle in plant biology. While other solutions to the extended imaging of gravity-sensitive roots have been provided previously, this work provides significant advances beyond these enabling this to be achieved for far greater time periods.

The text is clearly written and the methods are well described. The quality of the videos provided is outstanding.

Concerns with the manuscript lie principally within the experimental validation of the technology, and a couple with the method itself.

In order to encourage this technology to be adopted, it would be preferred to have the software work in the freely available Octave software as opposed to MatLab. This would remove a financial obstacle in the form of licence-based software. In a best case scenario the existing code will run seamlessly within Octave.

The extent to which plants are experiencing a hypoxic response under agar within the Lab-Tek chambered coverglass should be examined. Imaging the ADH1::GFP reporter would answer this. Knowing whether plants are experiencing hypoxia will impact the interpretation of data obtained using this technology.

More detail on the novel insights arising from imaging KNOLLE would strengthen this part of the text.

DII and gravity stimulation has been performed previously using a periscope in the PNAS paper "Root gravitropism is regulated by a transient lateral auxin gradient controlled by a tipping-point mechanism". This and differences between what is observed here and what has been reported previously requires further detailed discussion.

Verification of cell tracking in zebrafish through some form of quantification is lacking. A clear validation of the method and the ability to derive novel insight into this biological process is missing.

Reviewer #2:

Von Wangenheim and coworkers describe a vertical confocal setup and developed a custom software for automatic tracking of moving/growing objects. The authors very nicely explain how to convert a "normal" confocal into a vertical one. They have supplied all the needed information for the transformation and for the construction of the rotation stage, illumination setup and the scripts to implement the TipTracker software. They have used this system to show that it can give high resolution information on cell differentiation, division and gravitropic responses. Although all experiments are performed to the highest standards and the data is represented in a beautiful and clear manner, to me it falls short to be considered as a resource. The conversion to a vertical confocal system is not straightforward and needs experts in optics and also experienced workshops. This is not readily available for most laboratories. Also when comparing the manuscript to other resource papers such as Barbier de Reuille et al., 2015 and Rabe et al., 2016 this manuscript will have less impact on the community as in my opinion is it limited to only a few groups. It might be an idea to expand the Tiptracker idea also to light sheet microscope setups. I feel that in its current state it falls short of being a resource for the community.

Reviewer #3:

The authors present a methodology how to convert an upright confocal microscope into vertical imaging system where the growth and movement of biological samples can be tracked and recorded in a high resolution.

Imaging in vertical orientation facilitates studying of gravity responding samples in their natural orientation e.g. plant root tips.

The article describes in detail how to adapt the upright microscope for its new function. Additionally, the authors provide a tracking program that enables the process of long time-course scanning to be automated for several samples at the same time. Importantly, the authors provide also the information on how to provide good light necessary for undisturbed growth.

This methodology will facilitate more accurate studies of gravity influenced processes in the growing root.

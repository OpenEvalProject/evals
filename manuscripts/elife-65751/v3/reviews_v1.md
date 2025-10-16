# Peer review - Round 1

Editors:
- Mackenzie W Mathis, EPFL Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65751.sa1](https://doi.org/10.7554/eLife.65751.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Claudi et al., present a new tool for visualizing brain maps. In the era of new technologies to clear and analyze brains of model organisms, new tools are becoming increasingly important for researchers to interact with this data. Here, the authors report on a new python-based tool for just this: exploring, visualizing, and rendering this high dimensional (and large) data. Moreover, the authors provide rendering performance benchmarking, open source code, and extensive documentation. We believe this tool will be of great interest to researchers who need to visualize multiple brains within several key model organisms, and is written such that it can be adopted rapidly by the neuroscientific community.

Decision letter after peer review:

Thank you for submitting your article "Brainrender: a python-based software for visualizing anatomically registered data" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Kate Wassum as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Juan Nunez-Iglesias (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1) All reviews highlight some additional information required regarding usability (which file types are already supported out of the box, computational resources, run times, minimal example code in methods, how hard/easy is it given one's level of coding, etc.). We agreed these are critical. Please address each of these concerns.

2) 2 of 3 reviewers mention the need for citations of dependencies, so please address both reviewer #1 and #2's specific comments on this below.

3) Lastly, please consider revising the Conclusion/Discussion section. Some text feels redundant, and this space could be used to discuss limitations and future expansions more directly. Each review highlights some very nice strengths and some limitations, so please consider the recommendations when you edit this section.

Please include a key resource table if you have not already done so.

Reviewer #2 (Recommendations for the authors):

The paper does a great job of describing the need for this new software, as well most of the capabilities of the software. I did wonder specifically which file formats, other than.obj and.stl, were supported. Specifically, in subsection “Design principles and implementation”, it would be good to introduce at least one sentence about the exact IO capabilities of brainrender “out of the box”, as well as noting that the full scientific Python ecosystem can provide support for other formats. In fact, a whole section/paragraph about how to import data from custom file formats (e.g. a.czi file?) would be most welcome. I expect the first question of many readers will be "how do I get my data into this to try it out?"

The whole Conclusions section felt rather redundant. Even though this is common in scientific writing, I'd remove most of it, reduce it to one sentence, and instead elaborate on "limitations and future directions". I expect the authors can certainly come up with more ideas there (e.g. IO plugins?), as well as existing bugs (e.g. Video 4 has some distracting flickering on the electrodes – it's unclear to me whether this is expected, but I suspect not). Additionally, I recommend using this section to point out that readers can and should get involved with future development. The line "We welcome any user to.…" should be a paragraph in future directions rather than a one-liner in the Materials and methods. "We welcome users to submit bug reports and feature requests on our GitHub issues page, as well as usage questions on image.sc. Further, given the completely open source nature of the software, we especially welcome users who would like to help us improve the software for their use case…" In my experience, most biologists don't see themselves as capable of doing this, and most of those are wrong, so this is a good space to dispel that notion.

As an aside, the references need work. Many are incomplete, including two from this paper's co-authors (Tyson 2020a/b). Additionally, although NumPy is appropriately cited, several other packages are not:

– matplotlib is used for its colormaps; this should be mentioned in the methods and matplotlib cited.

– Jupyter is used for documentation and the Scene has some Jupyter compatibility, but Jupyter is not cited. Citation info for Jupyter appears to be discussed in this github comment: https://github.com/jupyter/jupyter/issues/190#issuecomment-721264013

– Pandas is used but not cited.

– I notice napari is used but only for its theme – I'd say it's appropriate to not cite it. Indeed, I would recommend the authors remove that dependency and instead copy the very small amount of information that they need from it.

A good resource for citation info in the scientific Python ecosystem is found here:

https://www.scipy.org/citing.html

I would also recommend naming NumPy specifically in the Materials and methods section (as well as the above packages), as I initially missed that the authors had appropriately cited it – just buried under the generic "standard python packages"

Finally, although there is a screenshot of the brainrender UI, *and* the supplementary videos show renderings created with brainrender, there is not a screen-captured video demonstrating the brainrender UI being used to generate a video. I would suggest including one as part of the supplementary materials, as that is something that many readers will be looking for – it is very hard to convey the usability of GUI software using text alone.

All in all, those are all easily fixed points and would encourage publication of the paper.

Reviewer #3 (Recommendations for the authors):

1) Emphasize the importance and difficulty of having accurately registered data. In our experience, this is the hardest part of the process, and it is just lightly discussed as a requirement for using the tool.

2) They state that it is easy to incorporate another atlas through the brainreg software, which can then be used with brainrender. As mentioned, it is our opinion that this is not a straight-forward task and that it would require significant programming skills to implement. Please provide more direction about how this can be done and what the constraints are.

3) One of the stated advantages of this software is the ability to visualize multiple types of data and data from sources that are external to the atlas generators. Such visualizations can potentially be used to reveal consistency and/or novelty across data types. However, ultimately you would want to be able to measure these differences. Including examples about how to extract and compare features across data types and then visualize those differences with brainrender would strengthen the paper.

4) The snapshots of code presented as figures don't add much to the manuscript. Consider highlighting how-to videos instead.

5) As stated in earlier comments, some of the functionality is not clear, particularly for people unfamiliar or new to 3D visualization or coding in general. Even experienced developers would benefit from specs for the various input data types, for example. A little more explanation, particularly in cases where the interface is different (such as with the helper functions used to make some actors), can greatly improve the user experience.

6) Though the purpose of this tool is not to develop a registration algorithm for anatomical reference atlases, or to perform data analysis, we view these steps as the most difficult and necessary steps in this process. 3D rendered data visualizations are informative, but not meaningful without accurate registration to begin with and without quantitative analysis to back it up. As they point out in the introduction, other, similar tools (natverse, MagellanMapper) have both visualization and analysis capabilities.

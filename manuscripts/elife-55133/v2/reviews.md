# Peer review - Round 1

Editors:
- Peter Rodgers, eLife United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55133.sa1](https://doi.org/10.7554/eLife.55133.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Imaging in Biomedical Research: An Essential Tool with No Instructions" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by the eLife Features Editor (Peter Rodgers). The following individuals involved in review of your submission have agreed to reveal their identity: Claire Brown (Reviewer #1); Elisabeth M Bik (Reviewer #3).

Summary:

This paper brings attention to the ongoing problem of lack of detail in the Materials and methods section of paper to reproduce imaging experiments. The authors do a nice study of some select literature to highlight the breadth and depth of the problem. This is an important issue that needs to be discussed in the community and dealt with and this article will help push towards correcting the problem in the field. However, a number of points need to be addressed to make the article suitable for publication.

Essential revisions:

1) The Appendix should include a clear definition of what counted as an "image" for this paper. Where Western blots or other non-microscopy photos included in this definition? Did the authors count line graphs, flow cytometry panels, or spectra as "image" or not?

Here are three examples to illustrate how the short definition of an image for this paper does not appear to match the data provided in the Source data file:

# DOI:10.1016/j.bpj.2018.12.008 is listed to include 2 images in 7 figures. But I would not be able to know which 2 were counted as images. Figure 2 and 3 contain microscopy photos, but Figures 4 and 5 also appear to contain some imaging data, albeit not a real photo but more a spectrum? Which ones were counted as an image?

# DOI:10.1038/s41590-018-0203-2 has 5 figures with images. Some panels of those figures were microscopy images, but others were immunoblots. Were both types of images evaluated for this paper or only the microscopy photos?

# DOI:10.1083/jcb.201710058 has 8 figures with photographic images, not 7 as listed in the Source Data File. That might suggest that the authors did not include Figure 4 (which has Western blot photos but not microscopy photos) in their analysis, and that they mainly focused on microscopy photos.

2) Because it is not clear what the authors counted as an "image", it is also not clear what was counted as the amount of text in the methods devoted to images. For example, if a paper contained both immunoblots as well as microscopy photos, did the authors only look for the microscopy paragraphs in the Methods, or were the immunoblot (Western blot) paragraphs also counted? Often, Western blot imaging is not described in the Methods because it is not very important how a photo is made, and a smartphone camera might suffice. For microscopy, the settings and details are much more important than for Western blots. It would be helpful if the Introduction / Discussion would better clarify that this paper focused on settings for microscopy photos, not on those for other types of photos. The examples in the Appendix were very helpful to clarify, but already defining this at the beginning of the paper would be better to avoid confusion.

3) The paper lists that 185 articles containing images were evaluated, but in the legend of Table 1, suddenly 4 papers with MRI images are removed. This is not mentioned in the main text. It would be better to describe (e.g. in the Appendix) that MRI images were not included in the definition of 'images' and list 181 as the total of papers analyzed or to include them in all analyses.

4) There is mention of the importance of sample preparation in the examples provided about EM microscopy and how that was evaluated but little is mentioned about optical microscopy and sample preparation. This is very important for quantitative and reproducible fluorescence imaging as well. Details that are important include catalog numbers and lot numbers for reagents and validating staining methods or functionality of tagged proteins.

The manuscript would be strengthened considerably if the authors could extend their analysis of the 240 papers in their sample to determine how rigorous and detailed they are when it comes to sample preparation. If this is not possible, the authors should mention the importance of reporting the details of sample preparation at appropriate places in their manuscript, and acknowledge that the percentages for imaging methods that they quote do not include sample preparation.

5) Similarly, image analysis is mentioned but not covered in detail. I think it is critical to document image analysis steps. Without this imaging experiments cannot be reproducible. Details that are important include data providence, the importance of retaining raw image data, the importance of documenting each analysis step including software versions and operating system. The OMERO figure software could be mentioned here as it offers data analysis tracking including for multiple people manipulating the same data set.

As in the previous point, the manuscript would be strengthened considerably if the authors could extend their analysis to include image analysis. If this is not possible, the authors should mention the importance of reporting the details of image analysis at appropriate places in their manuscript, and acknowledge that the percentages for imaging methods that they quote do not include image analysis.

6) The authors identify that incomplete reporting of imaging methods is a problem that a number of members of the community must address, including imaging facilities and journals. Having checklists is a great start. A preliminary checklist for critical image acquisition parameters should be included as a supplemental material for this publication. Perhaps the list of metadata pulled from images with the methodsJ plugin has that information already? Also, the parameters for image analysis (described above) should be included in the checklist. What else might journals do besides checklists (maybe use AI to screen the Materials and methods section for minimal criteria during the submission process?) And what more could core facilities of national and international communities (such as BINA and ABRF) do (maybe develop and disseminate training programs for researchers and reviewers?)

7) Another key stakeholder that is only briefly mentioned is the microscope manufacturers. They need to be guided and encouraged to include significant metadata as part of acquired images and make that information accessible to the end user on multiple different software platforms. A comment on this is needed in the discussion.

8) The authors mention funders as enforcers. Please expand on this - what could funders do to improve the reporting of imaging methods in papers?

9) A large part of the challenge in this field is to raise awareness. This article does just that. So it is also important to point people to a range of emerging resources in this area. Suggestions include:

# OMERO should be mentioned as a potential resource for centralized data management, accessibility and sharing.

# I would also suggest you reference work being done in this area by the 4D Nucleome project: "Minimum Information guidelines for fluorescence microscopy: increasing the value, quality, and fidelity of image data" The 4DN-OME model extension and metadata guidelines: https://arxiv.org/abs/1910.11370

# The brain microscopy initiative is asking for feedback on image metadata standards they are developing. https://brainmicroscopyworkspace.org/feedback.

# BioImage Archive is meant to be a repository for published microscopy image data sets so they can be used by the broader microscopy community. https://www.ebi.ac.uk/about/news/press-releases/bioimage-archive-launch

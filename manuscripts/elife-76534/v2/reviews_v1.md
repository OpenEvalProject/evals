# Peer review - Round 1

Editors:
- Albert Cardona, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76534.sa0](https://doi.org/10.7554/eLife.76534.sa0)

Datasets in volume electron microscopy have been growing fruit of the labor of the combined efforts of sample preparation specialists and electron microscopy engineers. A missing piece has been a method for the automation of the composition of continuous volumes out of collections of individual image tiles capable of handling the growing scales of the datasets. Pushing the boundaries of what is possible, this work illustrates how a successful approach looks like, demonstrated by its application to cubic millimeter volumes imaged at nanometer resolution. All being said, this work is but step 1 of a two-step process, whereby first a coarse but mostly correct alignment is computed, and then a refinement step using more local cues and with existing methods is applied, setting the stage for the subsequent automated reconstruction of neuronal arbors and their synapses from which to infer a cellular connectome.


---

# Peer review - Round 1

Editors:
- Albert Cardona, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76534.sa1](https://doi.org/10.7554/eLife.76534.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A Scalable and Modular Automated Pipeline for Stitching of Large Electron Microscopy Datasets" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Albert Cardona as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Ignacio Arganda-Carreras (Reviewer #2); Christian Tischer (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please make more clear and visible that the current framework, while impressively handling enormously large collections of image tiles, requires additional fine alignment for use in e.g., cellular connectomics.

2) Please could you elaborate on how the achieved registration accuracy relates to what would be needed to solve the scientific task.

Reviewer #2 (Recommendations for the authors):

In general, the paper is easy to read and the main ideas are easy to follow. However, some sections seem too technical for a non-expert audience and might benefit from adding some definitions (as a glossary or maybe footnotes). For example, in the "Software infrastructure supporting stitching and alignment" section: "It includes REST APIs for clients to GET/POST images […]", "[…] backed by a MongoDB document store that contains JSON tile specifications […]"

Regarding reproducibility, although the effort on providing open source solutions is remarkable, some documentation on how to set up the full pipeline would be greatly appreciated by the community, especially for a more modest or toy example. So far, the main site of the project (https://github.com/AllenInstitute/asap-modules) reads "We are not currently supporting this code, but simply releasing it to the community AS IS but are not able to provide any guarantees of support, as it is under active development. The community is welcome to submit issues, but you should not expect an active response.". While understandable, this is discouraging for all the potential users and it lessens the impact of the paper.

Nothing is mentioned about the specifics of the hardware resources needed to process each of the datasets. Indeed, it is not clear if the same exact computing power was used in all cases. Including those details would help the readers have a better idea of the scale of the problem being addressed and also of its requirements.

In Figure 2, maybe a shaded box including "ASAP" (or ASAP modules) should appear to clarify which components belong to it.

In Table 1, the total size of the datasets without overlap is a bit confusing. Does it involve full stitching/registration or is it simply the size without repeated pixels?

In Figures 4, 5 and 7, some of the fonts are really small and hard to read, please enlarge them.

In Figure 6c, adding an arrow to the blood vessel text would help the non-expert eyes.

In Table 2, it would be very interesting to see an estimation of the time spent in proofreading and quality control tasks, thus showing the degree of automation of the process. Also, in that caption it reads " The stitching time for all the datasets include" where it should read " The stitching time for all the datasets includes".

On page 16, where it reads "A description of these tools are as follows;" the sentence should end with a colon.

Reviewer #3 (Recommendations for the authors):

Software

1. ASAP-modules: The documentation is missing. It looks like the CI-generated docpages still refer to "render-modules", which seems to be deprecated/old.

2. The installation is not straight-forward. It requires adding deprecated Qt4 (700MB of extra downloads) libraries to support building an old (>3 years) opencv dependency, which is a lengthy procedure. Many dependencies are not available through the standard installation procedure (python setup or pip) but require manual intervention or actively downgrading installed packages using conda. It would be great if the installation could be simplified.

3. em_stitch: We could not find documentation or installation/usage tutorials for this software. The manuscript introduces this software as a stand-alone version of the alignment workflow, an interested reader will therefore likely start by exploring this software. Thus, an accessible tutorial including sample data will be very helpful. If em-stitch does not offer the full functionality to align "small" tiled datasets, a tutorial for setting up a simple pipeline (using the applicable tools) for a small example dataset would be very useful to someone interested in implementing the pipeline.

General remarks regarding the manuscript

1. The order in which the pipeline is presented is slightly confusing as it does not fit with the logical progress of tasks. While PointMatch determination and quality of the Solve step is shown in Figure 4, the QC determined by PM and resulting analysis in acquisition quality is shown afterwards in Figure 5.

2. What is the data resulting from running the pipeline? We assume it is a cloud-stored volume in N5 format to be visualised using Neuroglancer, but this does not become clear in the article. Does the pipeline also support outputs in different formats? (Sub-region as Tiff stack for local analysis in "traditional" software, OME-Zarr,..)

3. In line with our suggestion in the "Public Review" we suggest expanding Figure 1a such that the individual images are visible, e.g. such that one could appreciate the lens corrections, and include screenshots such as presented in Figure 3 and 6, as well as conceptual drawings such as in Figure 5a. The content of Figure 1b could then come later in the article, e.g, in a section on the "software stack and implementation details". Essentially separating example data and concepts (new Figure 1) from implementation details (Figure X). We also suggest just showing one of the options in Figure 1a(dddd) to have more space for the aforementioned additions from the other figures. Like this we would hope that the first part of the publication could provide an attractive overview of the concepts as well as some examples for a broader audience.

Detail questions regarding the manuscript:

1. QC: The metrics used for quality control are not entirely clear. Is it purely the number of PointMatches and their deviation for each tile pair?

2. What is a typical manual intervention for tackling miss-alignments? How is it done in practice? How exactly does the mentioned "parameter optimization" work?

3. Figure 5b-e: The actual shape of the distributions is not discussed in the text, thus a table with median, min, max may be sufficient for the main text and the distributions could go to the supplement. Would it be possible to give the residuals (also) in nm instead of pixels? This would make it easier to judge whether the accuracy is sufficient for connectomics.

4. Figure 6: Is this a rough or fine alignment (compared with Suppl. Figures1-3)? If it depicts only the rough aligned data, please provide an idea of how the final result looks like.

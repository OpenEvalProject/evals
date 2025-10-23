# Peer review - Round 1

Editors:
- Robert P Zinzen, Max Delbrück Centre for Molecular Medicine Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65372.sa1](https://doi.org/10.7554/eLife.65372.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Thank you for submitting your article "Image3C: a multimodal image-based and label independent integrative method for single-cell analysis" for consideration by eLife…. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Didier Stainier as the Senior Editor.

Both reviewers have agreed that your submitted manuscript is a valuable contribution to the field of label-free assessment of complex cellular mixtures and should be published given some crucial revisions.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Compare and contrast Image3C with other label-free phenotyping approaches, an issue raised by all reviewers.

2) The software should be made more accessible for the general user.

3) Please address the concerns regarding the assignment post CNN being "unsupervised", which was raised by both reviewers.

4) Address other options for Image3C workflow tasks (e.g. feature extraction, image processing, clustering, etc.). – At a minimum, explain the choices more critically

Also, please address further comments below and correct/clarify figures as appropriate (see comments)

Reviewer #1 (Recommendations for the authors):

– Given this is a tool and resource paper, I think more attention should be placed in making the software accessible to the general users. In the github page, there are multiple mentions of 'If on site at SIMR' (which I assume refer to the Stower Institute for Medical Research), which did not inspire confidence that this tool is designed for use by a wide audience.

– Can the authors compare and clarify the contribution of Image3C against other label-free single cell image-based phenotyping systems?

– Since there are many choice of algorithms in each step of the pipeline, such as feature extraction, image processing, clustering, etc. Have the authors performed a comparison of several sensible methods to show that their choice is the most suitable? At the minimum, the authors should explain their choice more critically.

Reviewer #2 (Recommendations for the authors):

The authors present a convincing argument for the use of imaging flow cytometer data in profiling and comparing complex cell mixtures, such as dissociated tissues. I especially appreciated the application of Image3C to separate datasets from fish (D. rerio WKM) and a non-model system (Hemolymph from the apple snail): Not only do they present consistent clustering, but also the emergence of phagocytes upon infection. I can appreciate that Image3C is not only applicable without a host of established reagents, but that it might add an additional layer based on cell morphology, rather than pure transcriptomics (or genome accessibility) – these layers of information may be complimentary, which I suggest the authors make a point of.

The code is largely available (except the steps using proprietary software), which is good. However, I believe the code is currently too disjointed to be useful to a non-expert. The workflow currently involves steps using the Amnis IDEAS package, followed by custom scripts in R, followed by VorteX (I believe in Java) followed by more scripts in R, followed by optional classification using CNNs in python, with a side branch of operations using commercial flow cytometry software (FCSexpress). I think it would be advisable to somehow package this assemblage of scripts into a more accessible and user-friendly package. For example, open source packages like FlowCore might be integratable.

Along the same lines, are there any alternatives for depending on the specific instrument (Amnis ImageStream Mark2) and the proprietary IDEAS software?

As is, I was unable to test the packages for lack of instrument-specific data, software.

Sample data should be provided together with a testable, streamlined software package as well.

The authors have not sufficiently contextualized published work on label-free extraction of informative image features. Nor have they compared Image3C performance !

The authors should highlight and illustrate the reproducibility of the data across independent data sets (assuming this is true) – After going through the Materials and methods, I realized that several replicates were generated for each data set. Supplemental figures attest to that.

I am still not clear on how exactly cell type identities were assigned to the FDL clusters. It is my understanding that a lot of prior knowledge (and corresponding studies) was (were) necessary for assignment. As such, analysis using Image3C may be less useful for assessing cell type complexity, but rather for changes therein. The claim of "cell types are identified by de novo clustering" should then be toned down.

Furthermore, the statement that

"…this produces a CNN-based cell classifier 'machine' used to quantify subsequently acquired image-based flow cytometry data and to compare cellular composition of samples across multiple experiments, in a high-throughput and unsupervised manner…„

is utterly bewildering to me. The CNN utilized cluster features as assignment guides. I believe that this is supervised by definition."

I was unable to sufficiently evaluate some of the figures, in particular the imaged cell arrays in various channels. In many cases the levels are such that signal I have to assume to be there is not visible. This is particularly true for the Phagocytosis assay, where DHR and CTV signal should be visible. Also, in these cases a direct comparison with sister cluster cells should be shown.

Check labels (especially in supplemental figures) for clarity (e.g. "Single and Nuc" in S3?)

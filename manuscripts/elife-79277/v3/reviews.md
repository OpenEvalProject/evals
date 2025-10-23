# Peer review - Round 1

Editors:
- Laurence Tudor Hunt, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79277.sa0](https://doi.org/10.7554/eLife.79277.sa0)

This is an important, methodologically compelling paper. It describes a powerful new online software platform for analysing data from naturalistic fMRI studies. The paper describes both the philosophy behind and intended usage of the software, and offers several examples of the types of results that can be computed using publicly available datasets. It will provide an important new tool for the open neuroscience community who are seeking to perform standardised and reproducible analyses of naturalistic fMRI datasets.


---

# Peer review - Round 1

Editors:
- Laurence Tudor Hunt, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79277.sa1](https://doi.org/10.7554/eLife.79277.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Neuroscout, a unified platform for generalizable and reproducible fMRI research" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Laurence Hunt as the Reviewing Editor and Tamar Makin as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Emily Finn (Reviewer #1); Christopher Baldassano (Reviewer #2); Eugene P Duff (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All reviewers were in agreement that Neuroscout will provide a valuable tool to the neuroimaging research community, that the structure of the platform is a novel one (that offers unique functionality not currently available on other Open Neuroimaging platforms), and that the manuscript is well-written. Following discussion with the reviewers we agreed that, while the authors should provide a point-by-point rebuttal to the reviewers' comments below, the three areas that should receive the highest priority in revising the manuscript are:

1) Provide slightly more in the way of assistance/help for users who are completely new to the platform to ensure that they can 'get started' without encountering errors – e.g. two of the reviewers (#2 and #3) attempted to use the platform but encountered errors when getting started, which could easily put off new users from adopting Neuroscout.

2) Discuss more extensively whether there are plans for further expansion/what the ultimate 'scope' of the project is beyond GLM specification. In particular, provide a specific discussion of how exactly the authors/developers see the software evolving over the short-, medium-, and long-term, and any plans they have in place to ensure continued development and promote a robust user community. Of course, it's hard to predict uptake with any new software platform, and this manuscript is an important step in publicizing the platform, but where do we go from here? Will there be a dedicated developer or team of developers moving forward? If so, how do they plan to prioritize and execute new features -- i.e., top-down decisions about important extensions (more detail on what these are?) versus bottom-up responses to user requests? If not, how will the authors/original developers ensure the continued health of the software? What kind of user support/promotion will exist -- passive usage monitoring? regular user surveys? active mailing/discussion lists? hackathons? etc. etc.

3) Address some of the specific technical questions about how Neuroscout handles certain aspects of the GLM, as highlighted in particular by reviewer #1.

Reviewer #2 (Recommendations for the authors):

The Neuroscout platform and the manuscript are very impressive, and I have no comments on how the presentation of the material could be improved.

I attempted to perform an analysis in Neuroscout as part of my review and was not successful. I was able to set up a simple analysis which successfully validated and compiled. To run the analysis, I first tried using Docker, as recommended. When doing so, I was prompted to enter my username and password for github.com. This was confusing to me since a github login was not discussed as part of this system. Entering my github credentials produced an error, since "Support for password authentication was removed on August 13, 2021. Please use a personal access token instead."

I also tried to run the analysis via singularity. The command recommended in the documentation was "singularity pull oras://ghcr.io/neuroscout/neuroscout-cli:" which yielded the error "FATAL: While pulling image from oci registry: failed to get checksum for //ghcr.io/neuroscout/neuroscout-cli:master: no layer found corresponding to SIF image". I instead built a singularity image from docker using "singularity build neuroscout.simg docker://neuroscout/neuroscout-cli" which ran successfully. To run the singularity image, the documentation incorrectly left out the second "run" argument to the command, but after adding that in and running "singularity run --cleanenv neuroscout.simg run [id] testns/" the analysis started. Unfortunately, I then hit the same github issue described above and did not know how to troubleshoot the issue.

The fact that analyses must be run locally is understandable since it greatly decreases the cost and complexity of running the Neuroscout website. However, it could increase adoption of the platform if a cloud-based execution option were available in some form – I'm unsure if there are options for easily spinning up free (or low-cost) cloud instances that could allow users without local computing resources to run analyses.

There is a sentence in the manuscript that I did not understand: "Interestingly, these effects were robust to phonological and orthographic covariates, suggesting that the involvement of VWFA in language comprehension may not be specific to reading." This sentence is referring to a study that is described as a "reading experiment", so I do not understand how the results could show that VWFA is involved in tasks besides reading.

Reviewer #3 (Recommendations for the authors):

The manuscript is prepared to a high standard. I have a number of recommendations:

– It would be nice to see more of a review of similar attempts at web analysis platforms and related software – possibly including those outside of imaging.

– Furthermore, general readers may appreciate a little more of a survey of the open fMRI analysis ecosystem that this is based upon, in the intro/results. Possibly further more detailed schematic figures could help.

– The description of the platform as "end-to-end" might be qualified – for me it produced unrealistic expectations for the breadth of the analyses that could be specified.

– More discussion on how this tool will be maintained and developed, including mechanisms for community contributions to its various elements.

– The example analyses were well chosen, but I sometimes lost track of what they were demonstrating.

– My attempt to access the analyses on binder seemed to fail.

– There was also a possible typo in the git command when I tried to pull a dataset ("fatal: repository 'https://github.com/neuroscout-datasets/SemanticNarrative-/' not found'").

– I think the manuscript would be strengthened with a broader discussion of future possibilities and goals for the tool. For example, more detail on the challenges of moving beyond naturalistic stimuli, and extension to modalities other than fMRI.

– Some discussion of the inferential challenges related to the re-analysis of datasets could be warranted.

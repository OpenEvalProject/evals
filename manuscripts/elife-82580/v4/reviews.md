# Peer review - Round 1

Editors:
- Morgan Barense, https://ror.org/03dbr7087 University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82580.sa0](https://doi.org/10.7554/eLife.82580.sa0)

Hebart et al., present a landmark, multimodal massive dataset to support the study of visual object representation, including data measured from functional magnetic resonance imaging, magnetoencephalography, and behavioral similarity judgments. The compelling, condition-rich design, conducted over a thoughtfully curated and sampled set of object concepts will be highly valuable to the cognitive/computational/neuroscience community, yielding data that will be amenable to many empirical questions beyond the field of visual object recognition. The dataset is accompanied by quality control evaluations, as well as examples of analyses that the community can re-run and further explore for building new hypotheses that can be tested with such a rich dataset.


---

# Peer review - Round 1

Editors:
- Morgan Barense, https://ror.org/03dbr7087 University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82580.sa1](https://doi.org/10.7554/eLife.82580.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "THINGS-data: A multimodal collection of large-scale datasets for investigating object representations in brain and behavior" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Floris de Lange as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Talia Konkle (Reviewer #2); Enrico Glerean (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

In our consultation session, we were all in agreement that this work is excellent. Each reviewer offers a slightly different perspective, and you can see their full feedback in context below. In general, the revisions we view as essential are as follows:

1. Providing more clarity to the open code, within what is possible given your skillset (i.e., we are not asking you to become software engineers).

2. We thought that the paper might be more impactful if some of the potential applications were highlighted and described in more detail (per Reviewer 1). We wish to emphasize that no new analyses are required unless you wish to conduct them.

3. Providing additional clarity on some of the methods, as requested by the reviewers.

In addition, each reviewer offered some additional comments, which we hope you will consider as you revise the manuscript.

Reviewer #1 (Recommendations for the authors):

My feedback below does not affect the authors' main conclusions and I see all these as addressable with a revision.

1. One important strength of this work is that it reveals fMRI datasets with few participants (n = 4) that can be replicable and reliable. Given recent discussions related to replication issues for certain types of studies (e.g., brain-wide associations), I wonder if the authors may wish to highlight the replicability of their work more directly. For example, it may be useful to define "exemplary analysis" (e.g., mentioned on pg 16) in the introduction and then describe that nearly a dozen neuroimaging results were replicated in the author's approach.

2. An additional paragraph in the discussion describing the strengths and weaknesses of THINGS relative to existing datasets may be needed. For example, the authors report analyses focused on ventral visual stream regions. Do the authors think that their dataset can be used to study other brain regions such as the prefrontal cortex or anterior temporal lobes that may be also involved in object recognition?

3. In general, I thought the authors could have been clearer in terms of the potential new insights this dataset can offer the field. For example, the authors mention "…THINGS-data will serve as an important resource for the community, enabling novel analyses to provide significant insights into visual object processing…" – pg. 3, and a series of research directions focused on methodology, e.g.: "including information-based multivariate decoding at the image and category level, data-driven visualization of response patterns across space and time, large-scale hypothesis testing by evaluating the reproducibility of previous research findings, revealing the relevance of the neuroimaging datasets for learning about behavioral similarity judgments, and regression-based fusion of MEG and fMRI data for uncovering a spatiotemporally-resolved information flow in the human brain as validation and extension of existing findings.." – pg. 15.

To clearly showcase the importance and impact of THINGS-data, I wonder if it may be needed to conduct an additional exploratory analysis that is not conditional upon a previous replication or alternatively, speculate in the Discussion the potential theoretical insights that may be gleaned from future work using THINGS.

4. Eye-tracking data was collected and reflects an additional source of behavioral data with which to relate to neural measures. Yet the authors mention this data only once in the introduction and once in the methods and do not report any results other than briefly in the Supplemental. Perhaps related to the above, I wished to see more elaboration, either through additional analysis or a discussion on how eye-tracking data can be used in a future study.

5. The authors suggest that correlating RDMs between MEG and fMRI is indirect and introduces additional assumptions (pg. 14). As these assumptions are never described, I am left unclear with how and what exactly about the authors approach can account for this potential problem.

6. Why does the number of dimensions capturing human similarity judgments increase with dataset size in Figure 3, especially related to the author's previous work (e.g., the original 49 dimensions from THINGS)?

Reviewer #2 (Recommendations for the authors):

For the behavioral measures, I wasn't entirely sure I followed some of the statements you made-e.g. you estimated a saturation at 4.5M trials, but wouldn't you have to run more trials to confirm this saturation effect? Also, the idea that you might not need more data to get changes in embedding dimensionality seemed slightly at odds with the subsequent points that participant-specific modeling is more reliable and lead to new insights (are their participant-specific dimensions? Not entirely sure how these were related, and also to within-category triads). Importantly, for me, I think these points are not key to the value of the behavioral similarity measures for the THINGs dataset. Really for me the key results are about data reliability-and you have it, and that these images are the same as the neural data so can now be linked to brain/meg data… wide open frontiers here. For me, exactly how it relates to and extends your prior work is interesting but almost in the same way as the other demonstrative analyses you conducted… there is more work to do to dig deeper into this. (And that's exciting!).

Style comments related to the narrative arc of the results. TOTALLY OPTIONAL, feel free to do none of these. No need to even reply.

– For me, the level of the method detail early in the Results sections was a bit too deep (e.g. describing the ICA denoising procedures and ridge regression approach; talking about the "edge fraction and high-frequency content"). For me, this level of detail in the results detracted just a little bit from the flow, because I didn't quite understand it and I had an easier time when I read the extended methods, and saw Sup Figure 10. Similarly, you report head motion parameters for the brain datasets in the main text and figures, but I also think these graphs could also be relegated to the Supplement. I found results like Sup Figure 2--better reliability after denoising--to be the key data I was looking for regarding your choices.

The 66-dimensional embedding of the behavioral Results section comes in between fmri/meg data reliability and fmri/meg decoding. I think you were going for reliability/data quality measures for all 3 datasets, then results of richer analyses. But I'm wondering if maybe you can think of decoding quality as part of data quality, and keep those fMRI/EEG sections together more? Or, maybe signpost this Results section organization more?

Reviewer #3 (Recommendations for the authors):

I do not have major concerns to raise for this manuscript, however, I strongly believe that the work presented would be even more valuable if the code attached to the manuscript could be improved for clarity and follow "good enough" standards for research software (https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510). I know that software is not yet a valuable academic output compared to manuscripts, but I believe that the impact that will have on the community – along with the shared data – will be beyond the results and descriptions of this manuscript. In the list of comments below, I outline a minimal set of improvements to make the software more reusable. I am aware that researchers are not expected to be software engineers and I do understand if some of the requests might be too difficult, so please do as much as you can according to your skills.

List of improvements for the attached software

1. Licenses

Licenses are important because they let future users know if they can re-use your code. There are two zip files for the code in your manuscript. One contains licenses of the used packages and license for your code, the other did not mention any license. Please add at least a license for your code. If you are unsure, I recommend Apache 2.0 https://www.apache.org/licenses/LICENSE-2.0

2. README

Currently, there is a readme in PDF in one zip file describing the MEG scripts. There is no readme for the fmri part. There is no readme for the other zip file. Please include a REAME file in each of the two repositories (a text file is better than PDF, in general use PDF only for figures. Any text can be a text file). The readme file should list all files included in the repository and a short explanation of what they do

3. Folder structure

right now there is a mixture of scripts/results/other files to prepare containers/other files from other packages all in the same folder. Please consider separating the files into meaningful subfolders. There are no rules beyond the "good enough practices" paper linked above. At least separating results/derivative files from the code would be helpful.

4. Dependencies:

there are no dependencies listed. You need to specify which version of Matlab was used, you need to add the environment.yaml file for the conda environment that you activate in one script (if you are unsure please rune "conda env export > env.yml" after activating that environment). You need to confirm that all python scripts were run with that environment (conda activate is only present in the reconall script). You need to include the version of docker you used and the version of neurodocker. Since docker and/or neurodocker might change in the future, it would be recommended to also add the docker image you obtained to the repository or push it to dockerhub for people to reuse your docker images without needing to build them.

5. Testing and how to run

You need to document how a user can run and test the scripts themselves. For example, I have noticed that the script assumes that the BIDS (?) data should be located at a few parent subfolders. You could reconsider simplifying the work of the users, create a subfolder "BIDS" and tell the user to put there the data from neurovault and make your scripts point to the BIDS subfolder.

6. Accepting contributions and improvements from the community + version control

This is totally optional: right now it is difficult for a member of the community to recommend changes to your code because your code is not stored in a version control system (github, gitlab, etc). Please consider storing the code on github (or gitlab) and engage with your community of users by encouraging them to improve your code, and add future analysis to the same repository. In the long run, your repository (along with the dataset) could be a very valuable resource for the community, especially if you start getting contributions and code from future reuses of the data. Furthermore, by using a git repository you will also have the added benefits of version control of your software. Unlike manuscripts, the software is dynamic and so are the data, you can keep on improving some of your analysis or functions or just make the code more reusable by other scientists and the changes made will be documented automatically by the git system.

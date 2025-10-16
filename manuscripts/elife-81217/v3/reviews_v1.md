# Peer review - Round 1

Editors:
- Saad Jbabdi, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81217.sa0](https://doi.org/10.7554/eLife.81217.sa0)

This article is an important contribution to the field of neuroimaging. The paper proposes a deep neural network for brain extraction and an approach to training the network that generalises across domains, including species, scanners, and MRI sequences. The authors provide convincing evidence that their approach works for a varied set of data, protocols, and species.


---

# Peer review - Round 1

Editors:
- Saad Jbabdi, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81217.sa1](https://doi.org/10.7554/eLife.81217.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A generalizable brain extraction net (BEN) for multimodal MRI data from rodents, nonhuman primates, and humans" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Floris de Lange as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Emma C. Robinson, PhD (Reviewer #1); Jason P Lerch (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The one major point raised by reviewer 2 appears to me to be the most important to properly address, as it appears the method did not work well on the reviewer's own data, casting doubt on the generalisability of the approach- the main selling point of the paper.

Reviewer #1 (Recommendations for the authors):

I recommend that the paper is largely ready for publication in its current form.

Reviewer #2 (Recommendations for the authors):

The major point I'd like to see the authors discuss is when BEN needs to be retrained on different input data and discuss techniques to improve generalizability. In the examples given and weights provided they suggest that, for example, 7T and 9.4T T2w mouse data needs different networks. This is somewhat surprising to me and suggests that the networks might be overfitting to their input data. My own tests (as described in the public review) also suggest that even subtle changes to out-of-sample data quickly degrade performance.

Secondly, I find that the narrative in places overstates the importance of their work, primarily since in my opinion the community has created multiple brain masking algorithms in different species that work well. Three examples include:

1) Line 17: the claim that brain extraction in animals is not fully automated; the relatively simpler brains, especially in rodents, means that image registration-based approaches to segmenting brains is quite successful and has been implemented in multiple toolkits. Similarly, the claim that the performance of registration-based methods is limited is at odds with the data.

2) It is not clear to me why the authors would expect FSL or FreeSurfer to work on rodents out of the box, given that the algorithms were never tuned for non-human brains (as far as I am aware). Their inclusion for animal brain segmentation tasks thus appears to be a bit of a straw man.

3) I also found Figure 7 and the related arguments about why BEN is necessary a bit odd; any decent registration/segmentation pipeline would incorporate brain masking, so the comparison of with and without masking is also a false contrast. There are lots of interesting ideas in this manuscript that it does not need these types of strawman arguments, so I would suggest removing this section entirely or alternately comparing the inclusion of BEN for masking as compared to alternate pipelines with masking included as well.

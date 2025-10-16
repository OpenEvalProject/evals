# Peer review - Round 1

Editors:
- John T Serences, https://ror.org/0168r3w48 University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80990.sa0](https://doi.org/10.7554/eLife.80990.sa0)

The current manuscript presents a computational model of numerosity estimation. The model relies on center-surround contrast filters at different spatial scales with divisive normalization between their responses. Using dot arrays as visual stimuli, the summed normalized responses of the filters are sensitive to numerosity and insensitive to the low-level visual features of dot size and spacing. Importantly, the model provides an explanation of various spatial and temporal illusions in visual numerosity perception.


---

# Peer review - Round 1

Editors:
- John T Serences, https://ror.org/0168r3w48 University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80990.sa1](https://doi.org/10.7554/eLife.80990.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Neurocomputational principles underlying the number sense" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: David Charles Burr (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

There was general enthusiasm for the topic. However, we all agreed that the paper lacked a clear differentiation from earlier work by Dehaene and Changeux (1993). Those authors used a slightly different architecture, but there are many similarities and the present paper did not clearly articulate what novel insights/predictions the current model brings to the table. The authors will need to clarify these novel insights – to the extent possible – and will likely need to make some direct comparisons between the current model and older models. If the authors opt to revise and resubmit, the paper will be sent back to the original two reviewers to evaluate in the context of older work.

Reviewer #1 (Recommendations for the authors):

1. "As applied to early vision, this strong winner-take-all mechanism is implausible, as the model would suggest that visual cortex only knows that dots exist, without knowing the size or the location of the dots" (page 3; 3rd paragraph) - this is not true. In the Dehaene and Changeux model, the lateral inhibition in the DoG layer does implement a strong winner-take-all mechanism, however, the size and locations of the dots are still encoded in its output. The locations are topographically encoded, and the locus of activity within the DoG layer encodes (i.e., which filters are activated) encodes dot size. Therefore, the model does not imply that the visual cortex is agnostic to dot size and location. Subsequent stages of the model are indeed primarily concerned with numerosity and not affected by dot size or location, just as is the case for the model in the current manuscript.

2. "Critically, unlike connections between layers, such as with the pooling layers of AlexNet, divisive normalization occurs within a layer (e.g., between center-surround units) through recurrent activation" (page 4; 2nd paragraph) - AlexNet also uses a very similar form of divisive normalization within the convolutional layers (local response normalization). This form of divisive normalization has also been used before in a number of models.

3. The findings in Fig. 3 and Fig. S3 concerning the changes in the model response under different conditions should be backed by appropriate statistical tests.

4. Using the term "driving input" to refer to the rectified output of the convolutional layer is somewhat confusing. Perhaps it would be clearer to use the term "unnormalized response" or something similar.

Reviewer #2 (Recommendations for the authors):

I would very much like to see this published and make a few suggestions.

I would drop the paragraph about Paul et al. It is misleading, and not very relevant (as you indeed point out).

They cite the fact that numerosity modulates the pupil response as an example of low-level interaction. I think this is misleading. Although the pupil response is indeed a very basic reflex, it is modulated by high-level processes. It does not imply early computation of numerosity. I think the Collins reference is equally shakey.

Also, it would be useful to test the extremes of a model. For example, we know at very high densities that the rules of numerosity estimation change: what happens to the model there?

Finally, abbreviations should be defined: Sz, Sp, and N are not defined until methods, which makes the text difficult to follow. These should be defined on first use, and probably also in the caption to figure 2.

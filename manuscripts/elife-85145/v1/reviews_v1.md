# Peer review - Round 1

Editors:
- Frederik Graw, https://ror.org/00f7hpc57 Friedrich-Alexander-University Erlangen-Nürnberg Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85145.sa0](https://doi.org/10.7554/eLife.85145.sa0)

Russell et al. study and reveal compelling evidence for potential sequence-based factors that may drive VDJ trimming, a mechanism involved in VDJ recombination that shapes adaptive immune repertoire generation. The work is based on a rigorous statistical comparison of logistic regression models to reveal the role and function of cutting enzymes in shaping T- and B-cell receptor diversity which could provide fundamental new insights into these processes.


---

# Peer review - Round 1

Editors:
- Frederik Graw, https://ror.org/00f7hpc57 Friedrich-Alexander-University Erlangen-Nürnberg Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85145.sa1](https://doi.org/10.7554/eLife.85145.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Statistical inference reveals the role of length, breathing, and nucleotide identity in V(D)J nucleotide trimming" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Betty Diamond as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Thierry Mora (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Your manuscript addresses an important topic and interesting approach to foster our understanding of processes relevant to immune repertoire generation. However, there were several aspects identified during the review process that would require major revisions to support or adapt the claims made. In particular, this affects the following essential revisions:

Essential revisions:

1) A rephrasing or additional support for the claim to provide mechanistic insights which seem to be overstated. Based on the fact that only statistical models are used, there is currently no real indication of mechanistic or quantitative insight into the involved processes.

2) An extensive restructuring and rewriting of the manuscript to clarify the focus of the paper (see comments of reviewer 3, e.g. regarding the extended methods section)

3) Improved explanation of the model, as well as several details concerning the statistical analyses

Reviewer #1 (Recommendations for the authors):

Really great work and very interesting. My recommendations are mostly questions and some suggestions.

– The text is really dense (especially when you talk about and compare all the different models tested). Can that somehow be shortened and made more concise?

– Maybe it's mentioned somewhere, but how many sequences were in train and test datasets? Have you performed subsampling studies to understand at what sequence number your models become stable?

– You only use unselected sequences. If you had used productive sequences, would the results have been dramatically different?

– You are somehow splitting the datasets by V gene distance. How would the results have looked like with a random train/test split?

– Figure 3a, 4a what's the statistical significance between curves? I rarely see error bars (if at all) in any of the figures. To what extent are your results dependent on just sampling once?

– You use the term mechanism a lot. The title is also quite strongly worded ("reveal role of"). To what extent is this justified given that you "only" perform statistical modeling and no experimental investigations? To what extent are you sure that your models are really a reflection of biology (causal)?

Reviewer #2 (Recommendations for the authors):

DNA breathing: At the end of the day, what is used in the model is the GC content on both sides of the cut site. While I recognize this has been shown to be associated with breathing, I think the authors should remain more factual about their conclusions, and stick to the observation that GC content is predictive in the abstract and introduction, writing about breathing only as a possible interpretation rather than a solid result. It would be both more precise and clearer – I struggled to understand what the paper actually showed until I reached the bottom of page 5, where the proxy for breathing is finally explained.

The model definitions are quite complex, and a cartoon of the DNA sequence, with the overhang, cut site, etc, would be very much needed to better explain the geometrical configuration of the model and the notations, as in the first Figure. It could help answer some of the following questions which confused me: which part of the sequence is subject to the PWM? Which part of the sequence is included in the sequence breathing counts on the 3' and 5' sides? Why are there 3 (and not 4, or 2) parameters in the sequence-breathing part of the model? Relatedly, why not combine distance with breathing parameters (i.e. are they redundant)? When does the 3' overhang start (we learn later it's at +2)? What is DNA shape? From what reference point is the length of deletion n counted? I'm aware there are such cartoons in the Methods, but they should be shown earlier and combined in a clearer manner, to display the definitions of the models and notations directly on the cartoon rather than painstakingly explained in the captions.

Methods: The methods are way too long for what they aim to explain: 25 pages, with a 5-page long table of notations! I would strongly recommend simplifying them to make them more readable. I will readily admit that I didn't comb through them with as much care as I would have liked, partly for lack of time, partly because I didn't feel I would learn much more from them than I already understood from the main text. I suspect very few readers will. The paper would be greatly improved by reducing its length, but also by providing key details and explanations in the Results section, to make it more self-contained.

Training set: From the methods, it appears that the Emerson dataset is first processed by IGoR to sample from the posterior distribution of scenarios. This non-obvious but essential step should be made clear in the description of the training data in the Results section.

I was also wondering why the authors didn't directly take the V-gene-dependent deletion probability distribution provided by IGoR, which (at first sight) should be strictly equivalent to sampling from that posterior distribution while being much easier. If you restrict to a single V gene, sampling scenarios and just sampling from the IGoR-provided distribution of deletion lengths for that V gene are exactly the same thing, by definition of the EM algorithm. Could you please explain that choice?

# Peer review - Round 1

Editors:
- Mark CW van Rossum, University of Edinburgh , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.10989.021](https://doi.org/10.7554/eLife.10989.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Demixed principal component analysis of neural population data" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Essential revisions:

As you will see from the individual reports below, there were rather divergent views on your manuscript. While we are not asking for additional analysis, we are asking for editorial revisions to make the method and its novelty more apparent.

We are asking for a major rewrite that 1) defines the method better 2) clarifies the difference and similarities with earlier dPCA approaches, 3) the interpretation of the results. Being a methods paper we feel that the presentation is particularly important. Also publication/public presentation of the code is a necessary requirement for eLife publication (this can be any of a number of public and maintained sites).

We are treating this as a Tools and Resources paper, as it is really a data analysis Methods paper, and should have been submitted under the TR heading.

Reviewer #1:

This paper is about an algorithm to analyze neural activity in response to experimental manipulations of various factors such as time, stimulus property, and behavioral response. There is a new technique proposed and discussed in the context of previous methods. The results of the different methods do not look all that different.

The main issue I have with the paper is that the method is described 3 times in 3 separate sections (Results, Methods, supplement), with increasing level of detail, but seemingly inconsistently in concept and notation. It is therefore very hard to make sense of it all.

At the end of the day it seems that the novel idea advocated here is rather simple: find a set of projections of the raw data which explain most of the variance in the mean response (mean over all trials and factors while holding one factor fixed). This in turn seems to be simply solved, for each factor separately, by an existing algorithm known as "reduced rank regression".

Complicating the description, the authors seem to have at least 3 algorithms which they call dPCA. First, one they proposed in 2011 under that exact title. Then, a second, apparently the new one, which is based on a cost function that was not entirely clear in the first reading in the Results section, but became clear only after reading the supplement. There is a third "approximate" version suggested, which concatenates the eigenvectors of the covariance for each mean response. (Is that what is called Naive demixing (Figure 12)?) They seem to argue at one point that this approximate method gives similar results to the superior new technique.

The methods seem to have all in common in their goal of explaining the covariance of the mean responses (mean across the factors, and at times, mean across trials) with a few dimensions. There is much talk about an additive model similar to what is used in conventional MANOVA, where the total data is explained as a sum of means across various combinations of factors. Though I don't see that this is necessary to motivate the dimensionality reduction proposed here, it does lead to comparison with yet one more technique. With the current presentation, I find it hard to keep it all straight.

In Figure 12 the various methods are then finally compared to each other, but as stated below, the performance metric presented there left me confused, just when I thought I knew what is going on. Importantly, the traces presented there don't seem all that different to each other. So then, what is the main new contribution of this paper?

Reviewer #2:

This manuscript gives a discursive presentation of how a new version of remixed principal component analysis (dPCA-2015) may be used to analyze multivariate neural data. The presentation is, I believe, complete enough that a user could reconstruct, from zero, the analysis method and the particulars of data pre-processing, etc. It is well-written and logical. The method itself is a nice compromise between a principal component approach to data analysis and a MANOVA-like approach. In particular, components are easily visualizable and the manuscript figures do a nice job of showing, at a glance, the results from fairly sophisticated experiments.

Other than a number of small textual changes that I would suggest, and one reference, I think this manuscript is in publishable form.

Reviewer #3:

This paper describes a statistical method, demixed-PCA, for finding low-dimensional "interpretable" structure in trial based neural recordings. In many cases, neurons exhibit "mixed selectivity", meaning that they exhibit tuning to multiple experimental variables (e.g., the visual stimulus and the upcoming decision). dPCA differs from PCA in that it tries to find a low-dimensional projection that separates ('demixes') the tuning to different kinds of variables. The paper applies dPCA to four different datasets from monkey PFC and rat OFC, and shows that it recovers structure consistent with previously reported findings using these datasets.

The paper is interesting and this technique is likely to be of considerable interest and importance to the field, particularly given recent interest in mixed selectivities in different brain areas. However, I have some concerns about novelty and about the intended contribution of this paper. A similar demixing approach has been described previously in Machens 2010 and Brendel 2011 (which was a NIPS paper, so perhaps shouldn't be counted against the novelty of this one since it's only a conference proceedings paper). But it would be helpful to describe a little bit more clearly the intended contribution. Is this just the journal-length writeup of the NIPS paper? How does the method described differ from that in the 2010 Frontiers paper?

It would also be nice to spell out a little bit more clearly what scientific insights the method is likely to provide (or indeed, provides for the datasets being analyzed here). It seemed that for each dataset, the paper mostly says that dPCA confirmed the findings in the original paper. But if that's the case, why do we need dPCA? What can we learn by analyzing data with this method that we didn't already have access to using the analysis methods from those papers?

I have two other high-level comments:

1) I think the authors don't do enough to describe how they decided which components to include when setting up the model. Presumably this is a choice made before running the method, i.e., how to map the elements of the experiment onto discrete conditions. How did the authors solve this problem, and how should potential users go about solving it when applying the method to new datasets. For example, why don't we have "reward" components for any of the datasets considered here? How did you decide which interaction terms to include in the first place? In the olfactory data, did you include different components for each mixture or just one for each mixing component? What are the keys to setting up the analysis? Are there any exploratory data analysis techniques that the authors used to make these decisions?

2) For a methods paper like this, providing code should be a mandatory requirement for publication. Please say something about where to find an implementation, so that would be users can try it out.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Demixed principal component analysis of neural population data" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior editor), a Reviewing editor, and three reviewers. The manuscript has been greatly improved but there are some smaller remaining issues outlined below.

Reviewer #1 (General assessment and major comments (Required)):

This manuscript is like night and day compared to the previous version. I barely recognize the material any more. It is so much clearer that it makes me much more confident that this is all sound and well. I can hardly believe that these were the same authors.

Reviewer #1 (Minor Comments):

A few places where I got stuck were for example:

Equation 4 in subsection “Core dPCA: loss function and algorithm”, why can one separate the quadratic term like this? Also not clear why stefs 1-3 minimize this cost function, but I trust that all this is in the cited paper, though I could only retrieve the Izenman (1975) paper, which looked like yet more work to answer my questions.

Similarly, second equation in subsection “Unbalanced data”, why can one separate the square into two terms? and why can one replace Xnoise by C1/2noise? and why is XPSTH=X tilde?

In general I have to say that, while the issue of balancing the data is intuitively clear, the corresponding math seems cumbersome, but again, this may be my lack of time.

Reviewer #2 (General assessment and major comments (Required)):

The revised manuscript is acceptable for publication.

Reviewer #3 (General assessment and major comments (Required)):

I thank the author for the detailed reply to the original review comments, and the revised manuscript is substantially improved. I have a few lingering technical comments and questions, but overall I think the paper is now suitable for publication.

Reviewer #3 (Minor Comments):

Figure 1K: not entirely clear what principal components these are, i.e., why are there multiple traces per component? I guess this is because the authors have taken the principal components of the rows of the X matrix (i.e., each of which contains the PSTH of a single neuron for all components). This is a slightly odd choice: I would have thought one would take PCA of the PSTHs, which is closer in spirit to the dPCA and other methods discussed here, so that each component is just a length-T vector (i.e., where T is the number of time bins in the PSTH). I guess this is ok as is, but you should add something to the text or the caption to clarify what these are (e.g., each principal component is a PSTH across all conditions). This seems a little bit confusing, however, because the dPCA components you'll show later aren't the same size. (Or am I misinterpreting the figure, and what you're showing is instead the projection from all conditions on each PC?)

Indeed, the two components from Figure 1e explain only 23% of the total variance of the population firing rates and the two components from Figure 1h explain only 22% (see Methods). Consequently, a naive observer would not be able to infer from the components what the original neural activities looked like.

This seems a little bit uncharitable to the Mante et al. paper. After all, the regression model used by those authors did indeed have an "untuned component" for each neuron (referred to as Β-0), they simply didn't do anything with these components when it came time to construct a low-d projection that captured information about the stimulus and decision variables. But one could certainly have performed a dimensionality reduction of the Β_0's if one were interested in capturing information about time. So, in my view, while this passage is technically correct, I would encourage the authors to rephrase it to be slightly less disparaging to Mante et al. They simply weren't interested in the coding of time, so the fact that they don't capture those components is a choice about what variables to include more than a fundamental limitation of the method.

"where averaging takes place over all irrelevant parameters." A bit unclear – could use an extra sentence unpacking what this means.

"The overall variance explained by the dPCA components (Figure 3c, red line) is very close to the overall variance explained by the PCA components (black line).": Why does PCA only get 80% of the variance? Is this because you've determined that the last 20% belongs to the noise component?

Figure 3 caption: "Thick black lines show time intervals during which the respective task parameters can be reliably extracted from single-trial activity". Does this mean a pseudotrial with 832 neurons? Start of this section mentions the # of neurons but I think it's important to say it here in the Figure caption what this means. (Presumably, if you have enough neurons recorded then single-trial decoding becomes perfect?)

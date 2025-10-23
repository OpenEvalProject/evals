# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62574.sa1](https://doi.org/10.7554/eLife.62574.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Malaguti and ten Wolde combine analysis of sensing limits for time-varying signals with previous work on resource allocation to minimize the costs of sensing. The work makes a solid contribution towards understanding the principles of resource allocation, and the conclusion that E. coli chemotaxis is optimized for shallow gradients should stimulate further discussion and work.

Decision letter after peer review:

Thank you for submitting your article "Theory for the optimal detection of time-varying signals in cellular sensing systems" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Detlef Weigel as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Malaguti and ten Wolde combine analysis of Mora-Nemenman (PRL 2019) on Berg-Purcell type sensing limits for time-varying signals with previous work of one of the authors (ten Wolde, PNAS 2014) on resource allocation to minimize the costs of sensing. The previous work discussed tradeoffs for the costs of sensing a constant signal. Here it is extended to time-varying signals (modeled as colored-noise Gaussian). Although the authors exaggerate the novelty of their analysis, they make a solid contribution towards understanding the principles of resource allocation. The conclusion that E. coli chemotaxis is optimized for shallow gradients seems reasonable and should stimulate further discussion and work. Despite flaws in establishing context, the paper deserves publication

Revisions for this paper:

While enthusiastic about the results in the manuscript, the reviewers found that there are issues involving claims of novelty, and the overall presentation of mathematical results that will need considerable revision.

1) The novelty of their analysis is exaggerated.

The basic problem of optimally estimating the state of a time-varying signal probed by noisy measurements is textbook material for engineers. Here, because everything is linearized about an operating point and because noise is approximated as Gaussian, there is an exact analytic theory going back to Kalman and Bucy in 1961. The result underlies the Mora-Nemenman analysis (although they, too, did not reference that work for the Gaussian approximation used for their concrete results) and that done here. In engineering, the general problem optimally estimating a stochastic signal via noisy measurements was already considered by Kolmogorov and Wiener in the 1940s and formulated in the time domain, for linear systems driven by white noise (the approximation used here) by Kalman and Bucy.

It is a weakness that the connections are not mentioned specifically by referencing. Appealing to known results not only underlines how different disciplines often need to tackle the same problems, it allows for the use of textbook results and can shorten a paper. As a corollary, authors who map their problem onto known results should not be penalized for doing so, when the application is new and important (as here).

2) Specific sentences have language that seems exaggerated, in the light of historical work on filtering theory:

"Our theory is based on a new concept, the dynamic input-output relation pτr(L)."

- Dynamical models (with dynamical input-output relations) are a central element of filtering theory.

".Our theory reveals that the sensing error can be decomposed into two terms [sampling (sensing) error and dynamical error]."

- The framework of filtering theory assumes noisy measurements of stochastic signals.

"Our theory illuminates how the optimal design depends on the timescale of the input τL."

- The statement is true but should be framed in the context of other work, including in systems biology / biophysics, which comes to the same conclusion. For example, the work of Laughlin in 1981, and later Nemenman and Bialek, show that the input-output "gain function" should be adapted to the statistics of the input (including time scales of variation). Bialek's 2012 Biophysics book discusses many examples.

3) In its present form, the paper will be essentially unreadable by the vast majority of the eLife readership; the writing style is more appropriate to the Physical Review than to eLife. Indeed, much of the paper is written like a technical note that builds on previous work (Berg/Purcell, etc.) without sufficient explanation for the general reader. This criticism extends to the explanations of the underlying model, the lack of definition of terminology, and the notation.

Here are but a few examples of the points above. The authors are encouraged to rethink the entire presentation de novo for maximum improvement.

a) The definition of a "push-pull" network should be given in the paper.

b) For the purpose of readability by a diverse audience some care should be taken to define technical terms explicitly (e.g. "Markovian"), and to explain various statements more clearly. Appearing so early in the paper, such condensed statements will be off-putting to the general reader.

c) The whole notation of "inverting the mapping" that is central to the theory is not well-explained.

d) Regarding notation: consider, for example, the caption of Figure 2 and Equation 1, in which there is the quantity σ2p̂tr|L . This is simply too complicated, and its meaning will be utterly opaque to the general reader.

4) In many ways it seems that if the authors presaged the development of the theory by indicating the run-and-tumble context early on it would help the reader to understand the precise motivations behind their lengthy calculations, and to give an idea of the time scales.

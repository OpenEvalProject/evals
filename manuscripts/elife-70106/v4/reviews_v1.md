# Peer review - Round 1

Editors:
- Aleksandra M Walczak, École Normale Supérieure France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70106.sa1](https://doi.org/10.7554/eLife.70106.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The paper presents a new and interesting method for inferring the growth dynamics of bacteria from noisy single-cell data and applies this to C. glutamicum. The method which is original, is promising for other systems.

Decision letter after peer review:

Thank you for submitting your article "Single-cell growth inference of Corynebacterium glutamicum reveals asymptotically linear growth" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The work is nicely executed and it should be published in eLife. Generally the method is potentially more notable than the result, so strengthening the method's validation is a good idea. There are two main remaining issues (please also see the reviewer comments below and address all of them):

1. The issue of whether seeing non-exponential growth is a notable result in itself as advertised in the paper, especially in light of recent work by Bruggeman's group (Biphasic Cell-Size and Growth-Rate Homeostasis by Single Bacillus subtilis Cells, Current Biology 2020) that shows non-exponential growth for the well-studied model bacterium B. subtilis. This example of non-exponential growth is not discussed at length in the paper under review.

2. Regarding the analysis method, it would be useful to spell out the central novelty and the method should be validated more appropriately. For example, in Bruggeman's paper cited above they used a different analysis method (growth rate vs. age plot) that seems to work well, and the two methods were not compared or discussed.

Reviewer #1 (Recommendations for the authors):

This is an interesting study, with a strong method, but also nice results for the specific system. Here are a few points where the authors could improve the manuscript:

Main issues:

– Change the text to remove the repeated references to the consensus of exponential growth, this is likely less dominant than claimed here. E.g. abstract, on p. 2 bottom, p.4 line 80 ("universality") etc.

– Add some analysis to test whether linear growth continues into the phase where the first cells have started to divide. I imagine that removing the earliest dividing cells before the elongation rate determination should give the opportunity to analyze the remaining ones for a longer time. This could be done successively, and while the growth rate would be reduced as more and more cells are removed, one should see that growth rate remains constant up to later times.

Reviewer #2 (Recommendations for the authors):

Some comments:

1. The trend of elongation rate at birth seems to be different for different mutants. Figure 5A shows that in C. glutamicum divIVA:divIVA-mCherry the elongation rate is higher for cells with longer size at birth. Can the authors comment on this and how this is to be interpreted within their model?

2. Similarly, could the authors explain why the asymptotic linear elongation rate is smaller in C. glutamicum divIVA:divIVA-mCherry such cells as compared to WT using the RAG model?

3. In Figure 7, the authors seem to compare the birth length distribution obtained from theory and experiment. However, the fitness advantage or disadvantage of a longer-tailed distribution is unclear. In my opinion, the section can be removed from the main text for a better reading of the paper.

[Editors' note: What follows are minor comments after acceptance.]

Reviewer #2 (Recommendations for the authors):

The authors have done a good job of addressing the comments and I find the paper adequate for publication in eLife. I would like to raise a potential issue with the agreement of the model and data implicated by Author response image 1 of the response letter: In the biorxiv paper referenced in the updated version (by Kar et al.), a plot of the form of Author response image 1 is shown to be linear (y=x) both for exponential and linear growth. It therefore seems that for the model of growth proposed in the work (exponential crossing to linear) one would also obtain a simple y=x dependence. However Author response image 1 shows significant deviations from such dependence, suggesting that the proposed model might be inconsistent with the data?

# Peer review - Round 1

Editors:
- James M Berger, https://ror.org/00za53h95 Johns Hopkins University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71911.sa0](https://doi.org/10.7554/eLife.71911.sa0)

The present work is important for using innovative computational approaches and biochemical analyses to help to explain how hexameric peptide translocases and unfoldases belonging to AAA+ ATPases couple nucleotide turnover to directed chain movement. The work sheds light on understanding not only normal, processive translocation but also how the motors can operate with a defective subunit.


---

# Peer review - Round 1

Editors:
- James M Berger, https://ror.org/00za53h95 Johns Hopkins University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71911.sa1](https://doi.org/10.7554/eLife.71911.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "An Empirical Energy Landscape Reveals Mechanism of Proteasome in Polypeptide Translocation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by David Ron as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Gregory R Bowman (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All three referees felt that the paper is extremely technical and difficult to follow for those who are not computationalists or steeped in the minutia of AAA+ unfoldases. They also noted that it is unclear how the findings advance the conceptual or mechanistic understanding of AAA+ unfoldases beyond what is currently accepted in the field. These criticisms were counter-balanced by a sense that there is novelty and impact in the findings that have the potential for broad appeal. In addition to the specific comments noted below, the general writing and organization of the manuscript need to be substantially improve to more clearly describe the computational approach and the data analysis, and to better frame the explanatory power, impact and novelty of the results.

Reviewer #1 (Recommendations for the authors):

Page 6 and methods. Is it legitimate to exclude the chemical energy of ATP from the calculations?

P. 7. Concerning the statement "…we made the simplifying assumption that all six ATPases share an identical set of parameters. This assumption does not contradict the experimental finding of functional disparity among the six ATPases". What is the evidence for this claim?

Many parts of section II are dense with jargon and difficult to follow for the non-specialist. The language of this section should be simplified and clarified. Blanket statements and assumptions need to be accompanied with supporting evidence and arguments.

P. 7 and Figure 3B. There is ample evidence of cooperativity between nucleotide and substrate binding throughout AAA+ ATPases; i.e., the presence of peptide can alter the affinity for ATP and ADP and vice versa. However, it appears that the measurement of the nucleotide binding affinities was carried out using substrate-free (no peptide) proteosomes. How can the authors know that the values they obtained are relevant to when the ATPases are in a translocation state? And if these values are critical for estimating bridge energies, how can one be sure that these estimations have not thus been miscalculated?

Figure 2C. What is to be made of the observation that the TDETTT configuration leads to extremely low free energies only for states 3 and 8? This outcome could be taken to imply that the FEL analysis is being biased by the starting models; i.e., because the models were based on ED2, which is in state3 and not far off from state 8. Is there a counterargument for this concern?

Figure 3. Many of the labels, particularly in panels B and C, are too small to be legible.

Reviewer #2 (Recommendations for the authors):

I'm impressed by the ambition of the manuscript – to provide a full quantitative mechanistic model of proteasomal protein degradation. The experimental approach is very sophisticated and overall well thought through. However, I was unable to assess the quality of the data and reliability of the conclusions because I felt that the interpretation of the results and was not given enough room. In addition, I am not convinced that the conclusions discussed provide novel insights into the mechanism of the proteasome.

Reviewer #3 (Recommendations for the authors):

I expect other high energy states are present (and may even be important) but have low enough probability that this model still performs well. For example, the authors ignore states with more than 3 open interfaces. Presumably they are present, but I expect at much lower probabilities. Could the authors comment on how much lower probability these conformations would have than those included in the model, and how reasonable ignoring them is on that basis? It would also be useful to acknowledge that there may be other high-energy intermediates (e.g. as the PL1 loops move) that would be important to consider to explain the effects of specific mutations.

Assuming all the subunits have identical behavior does remarkably well. I'm curious how much asymmetry one could introduce without qualitatively changing the model (e.g. keeping the dominant states and transitions). I think an exhaustive study is beyond the scope of this work, but I would be curious to see a little bit of data. For example, would the depiction in Figure 6 look more or less the same if each interface had a different energetic separation between the open/closed states? E.g. I could imagine having a different e_b parameter for each interface, where each is chosen by multiplying the constant used so far by a random factor between 0.5 and 2. It should be easy to do this many times. Ideally the authors could make a statistical statement on how sensitive the topology is across this distribution of models, but even showing some examples to give a qualitative sense of the variability in an SI figure would probably be sufficient for this first paper.

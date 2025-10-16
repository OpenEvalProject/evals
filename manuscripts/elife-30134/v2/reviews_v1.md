# Peer review - Round 1

Editors:
- Wenying Shou, Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.30134.039](https://doi.org/10.7554/eLife.30134.039)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Incomplete inhibition of HIV infection results in more HIV infected lymph node cells by reducing cell death" for consideration by eLife. Your article has been evaluated by Wenhui Li (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Jackson et al. mathematically predicted and experimentally demonstrated that in lymph node cells, intermediate antiviral (anti-HIV) drug concentrations can allow infected cells to live longer by reducing multiplicity of infection. Thus, intermediate drug concentration can presumably facilitate the persistence of HIV. The result is interesting and can have clinical implications.

Reviewer #1's concern is quite substantial. Other reviewers agreed to this concern. "I strongly believe that infection probability r and death probability q should be measured experimentally. This is to eliminate fitting parameters and to ensure quality of the model."

Comments from Reviewers 2 and 3 are attached.

Reviewer #2:

The studies presented by Sigal et al. examine the interrelationship between cell death and the number of DNA copies of HIV that are detected per individual infected cell. Previous studies from a number of groups, including Sigal's, have indicated that cell-to-cell infection leads to infected cells with a higher number of integrated proviruses. The single cell PCR data provided by Sigal et al. support a hypothesis that the cell-to-cell infection not only leads to higher copy number of proviruses, but also generally leads to more rapid cell death. Using drugs or antibodies at low levels that do not fully inhibit infection, they found that low levels of inhibition paradoxically can give rise to a larger number of surviving infected cells. They also appear to find lower rates of cell death under conditions of partial inhibition. The studies are generally well conceived, and the results generally support the conclusions. The overall quality of the data could be improved by showing additional controls and increasing the numbers of cells analyzed to enhance the confidence in the copy number estimates. On the cell death front, it would be helpful for their hypothesis to show a time course with the cell death depicted over time. Lastly, an important detail not mentioned, is whether the use of lymph node cells is critical or not for the phenotypes that they describe. The study may have implications for the establishment of viral reservoirs in the context of poorly controlled infection or infections with some degree of drug resistance.

1) The authors use the ACH2 cell line to test the ability of their assay to detect single copy integrations. Why do they only spread each cell over 4 wells in control studies as opposed to the 10 wells used in their experimental studies? The rationale for using different dilution schemes should be explained. A comparison of the efficiency of PCR at the different dilutions would also be informative.

The ACH2 cell line yields fewer than 1 copy per cell, which may be a limitation of the PCR assay, but also could be reflective of heterogeneity in a cell line that is assumed to be clonal and a uniform karyotype. It is not described how recently the ACH2 cell line that they are using has been cloned. Repeating the ACH2 studies with a subclone would be beneficial.

Figure 2 would be more informative if it showed the results of both cell-free virus infection versus coculture infection. The numbers of cells analyzed in Figure 2C (n=34) does not appear sufficient to provide a robust sense of the distribution of the DNAs in the infected cells. Is this a bimodal distribution? Histogram comparison of cell-free should also be used for comparison.

2) Figure 4.

What happens with partial antibody inhibition of cell-free infection? These studies should be performed with infection from cell-free virus. To further test their hypothesis partial inhibition of cell-free infection should only decrease infected cells.

3) Figure 5.

As controls for cell death measurements, the viability of the uninfected control lymph node cells, treated and untreated, should also be illustrated. In the literature lymph node cells (mostly tonsilar) are very prone to cell death, and it is important to understand to what extent they are measuring virus-induced cell death. In addition, a time course of the cell death observed in the infections may would also be helpful to evaluate their hypothesis that the increase of infected cells in the partially treated cells is due to increased infected cell survival – i.e. decreased death.

4) Are the phenotypes described in the primary lymph node cells also observed for peripheral blood lymphocytes? Or are there differences between the peripheral blood versus the lymph node T cells.

Reviewer #3:

This is an interesting and worthwhile paper that examines the effects of incomplete inhibition of HIV infection with reverse transcription inhibitors. The experimental results presented are in accordance with model predictions. However, the presentation of the model should be improved as detailed below. Also, I found the labeling and numbering of the supplemental figures confusing. I have no substantial concerns and this the paper should be published after minor revision.

1) The terms and concepts in the paper are not clearly defined. In the first paragraph of the Results, you mention each donor to target transmission. It is not clear what a transmission is. Does it refer to viral entry of either a free virus or a virus (or genome) by cell-to-cell transmission? It needs to be defined. Second define what you mean by infection. Does a cell have to produce virus to be considered infected? Does the virus have to integrate or is it sufficient to simply reverse transcribe? Is a latently infected cell an infected cell in your model? Also, when you say drug therapy increases the number of live infected cells do you mean live productively infected cells, live HIV DNA+ cells, etc.

2) The assumption that all transmissions have equal probabilities to infect target cells seems to ignore the possibility that some virions carry defective genomes while others do not. This does not seem realistic. In your experimental system is the ratio of HIV RNA to TCID50 close to one so you can ignore defective particles?

3) You assume productive infection and death are independent events. While the events may be independent the probability of death is certainly not independent of whether a cell is productively infected or not. Further the probability of death is time dependent. The probability a cell dies one hour after viral entry (infection?) is clearly quite different than the probability it dies days after infection. You may want to define q as the probability a cell has died by time t after infection and the same for Pλλ where t is 2 days or 4 days for your various experiments.

4) Results, second paragraph. You claim antiretroviral drugs reduce the number of infecting virions. This implies that by infecting you must mean the virus reverse transcribes. In standard viral dynamic models the effects of ART are to reduce the infection probability, i.e., r in your model not λ. Thus it is important to clarify your definitions.

5) You introduce the drug effect as a constant d in the second paragraph of the Results. Later in the paper you make reference to IC50 and Hill coefficients for the drug. These need to be tied together in an explicit manner. In viral dynamic modeling the effectiveness of a drug, epsilon, (eps) is introduced where eps=1 is a 100% effective drug, e.g. stops all reverse transcription, and where eps=0 means the drug has no effect. Then a pharmacodynamic model is used to relate eps with the drug concentration, C, e.g. eps= C^n/(IC50^n + C^n). Thus rather than λ/d you could model the drug effect by (1-eps)λ and use the above formula to link the effect to drug concentration. See for example, Canini and Perelson, 2014. Equation 3 in your manuscript accomplished the same, but the above seems more straightforward.

6) Results, fourth paragraph. When you measure the number of reverse transcribed copies of viral DNA I assume you are measuring both integrated and unintegrated DNA – please state this explicitly as later you seem to imply you are measuring integrated DNA, e.g. Results, sixth paragraph.

7) The current work focuses only on reverse transcriptase inhibitors. Model therapy uses combination therapy including integrase inhibitors and protease inhibitors. Expanding the discussion of the clinical implications of this work to include combination therapy would be worthwhile.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Incomplete inhibition of HIV infection results in more HIV infected lymph node cells by reducing cell death" for consideration by eLife. Your article has been favorably evaluated by Wenhui Li (Senior Editor) and three reviewers, one of whom, Wenying Shou (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal his identity: Alan Perelson (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We want you to address the following comments. Note that we are not asking you to do further experiments. For the sake of record-keeping, we are enclosing all comments.

Reviewer #1:

I am satisfied with their measurements.

In general, I suggest breaking up long sentences (especially the one in Abstract, also the end of the third paragraph in the Introduction) for readability. Sentences that last more than three lines are generally more difficult to read than shorter sentences.

Reviewer #2:

The authors have very rigorously addressed the critiques by performing new experiments and modifying the text. The response to the reviews is particularly comprehensive and thorough. The resulting new data are supportive of the original model and hypothesis. The authors should be commended.

Reviewer #3:

In this revised version on the paper the authors have clarified their definitions by incorporating a supplemental table and additional text describing their model. However, this clarification has raised the following issues that need to be resolved:

1) As defined in the Results, λ is the number of infection attempts, where one attempt is measured as one HIV DNA copy. Thus, λ is an integer. The formula, Equation 1, makes sense when λ is an integer. However, what is determined experimentally is not the integer number of DNA copies but rather the mean number of copies per cell, which is not necessarily an integer. To make sense Equation 1 should be reformulated as a conditional probability of a cell being infected and alive given x attempts, call this P(I | x). What I believe the authors want is the probability of a cell being infected and alive, which is then P(I) =Sum P(I |x) (p(x)), where p(x) is the probability of having x infection attempts, and the sum is over all non-negative values of x. One could then assume, for example, that the number of attempts is Poisson distributed with mean λ. Then the resulting formula for P(I) would involve the mean value of the number of attempts. A better choice would be the empirical distribution that the authors measured. Note that what is actually measured is the number of infected cells that are alive at a certain time, i.e. P(I), and the mean number of attempts, what I called λ above.

2) According to the model q should be independent of the number of attempts. Can this be tested by using different drug concentrations, which would vary the mean number of attempts? If you already have experimental data on this, then include them. Otherwise, just discuss it.

3) In the original manuscript where Equation 1 was derived the authors assumed q was independent of r. In the second paragraph of the Results the authors say q is the probability of a cell to die post reverse transcription, which seems more sensible to me. Under the original assumption of q and r being independent, a cell in which the attempt was unsuccessful would have the same probability of dying as a cell in which reverse transcription succeeded. With q now defined as in the second paragraph of the Results, the fundamental formula given by Equation 1 may not be correct and deserves a more thorough discussion. I think the fundamental process being described is that at each attempt a cell is either infected with probability r, or not infected with probability 1-r. If it is infected, i.e. had a successful reverse transcription, then with probability q it remains alive and with probability 1-q it dies. Assume there are x attempts. Let z be the number of cells infected after x attempts. Then z is binomially distributed, i.e. z= Bin (x,r). Further, if we are interested in the number of cells infected and alive after x attempts, then P(I|x) = Sum_z=1 to x (x choose r) r^z (1-r)^(x-z)(1-q)^z, where the factor (1-q)^z is the probability of a cell surviving after each of the z infections. Simplifying, P(I|x) = [r(1-q) + (1-r)]^x, which is not the same as Equation 1. The number of attempts, x, is again random and as above one can convert this conditional probability into P(I) by assuming a Poisson (or some other distribution such as the empirically measured one) for the number of attempts p(x).

4) In Supplementary file 1 the authors say the way they measure the probability a cell is alive after λ attempts is by computing the concentration of cells alive with λ attempts divided by the concentration of cells alive with no transmissions. However, since the concentration of cells alive with no transmissions can approach zero as time goes on it is clear that this fraction need not be less than 1. Also, as noted above the authors need to use conditional probabilities and derive formulas that involve the mean number of attempts. I would suggest they compute the ratio of the probability a cell is infected to the probability a cell in not infected and alive, which is what they measure, and see if they can derive a formula for q.

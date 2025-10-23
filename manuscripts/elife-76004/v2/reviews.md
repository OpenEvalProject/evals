# Peer review - Round 1

Editors:
- Kayla Sprenger, https://ror.org/042nb2s44 Massachusetts Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76004.sa0](https://doi.org/10.7554/eLife.76004.sa0)

This paper will be of interest to scientists within the fields of statistical and biological physics, immunology, and vaccinology. The mathematical/statistical framework is rigorously constructed based on key concepts from population genetics and high-throughput viral genetic sequence data. The results provide important insights into the failures of past treatment regimens with broadly neutralizing antibodies to suppress viral escape in clinical trial participants. The results also present exciting and highly testable predictions of improved treatment strategies for combatting HIV through passive bnAb immunization.


---

# Peer review - Round 1

Editors:
- Kayla Sprenger, https://ror.org/042nb2s44 Massachusetts Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76004.sa1](https://doi.org/10.7554/eLife.76004.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Design of an optimal combination therapy with broadly neutralizing antibodies to suppress HIV-1" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Kayla Sprenger as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Miles Davenport as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The text should be modified to more clearly convey the novelty of the current work, and to better place the current work within the context of the existing literature on bnAb therapy design both from an experimental and computational perspective. Specifically, the conceptual advances that this work offers in terms of methodology and/or success in therapy design over past studies should be made more clear, and additional citations/discussion of existing literature is warranted.

For example, combination therapy with more than two bnAbs vs. fewer has long been shown to be more effective in suppressing early rebound. A suggestion is to note this fact and discuss the benefits of clinical corroboration of the model's results – i.e., that this corroboration provides a basis for using the model to interrogate new bnAbs (for which DMS data is available), and/or the combinatorial explosion of higher order cocktails for which we cannot possibly test all combinations.

2) Related to the above note, the non-independence of bnAbs is an important point that should be discussed/acknowledged as a potential shortcoming of the model.

3) As presented, the deep mutational scanning data is not convincing in its ability to fully characterize the spectrum of escape mutations, given the typical inability of DMS data to probe the low-frequency variants that primarily mediate rebound. More work needs to be done here to ensure/make clear that the predictive power of the approach is strong in this regard.

4) More discussion should be focused around specific use cases of the work. Particularly, since the framework is most predictive for early rebound times, it should be emphasized that the results from this work would best translate to, e.g., the design of short term suppressive treatments, rather than therapy efficacy over longer timescales, which would require a more complete characterization.

5) More discussion of how the predicted fitness costs compare to the older fitness landscape work would be useful context in the discussion.

Reviewer #1 (Recommendations for the authors):

General comments/questions:

In the Abstract (and Discussion), it is stated that bnAbs may serve as an alternative strategy to antiretroviral therapy against HIV, yet in the Introduction it is stated that augmenting antiretroviral therapy with bnAbs may be a fruitful strategy against HIV. Perhaps highlight the more promising approach of the two for consistency?

Line 52 states that prior work on designing bnAb therapies did not consider viral dynamics, yet the following sentence appears to give theoretical examples of just this ("dynamics of viremia"). Was the first sentence referring to prior experimental work?

In general, I find the paragraph in the Introduction between lines 52-72 to be a bit unfocused; what are the authors wishing to communicate here? Specifically, regarding lines 58-72, it seems like one could skip straight from line 57 to 73 and it would flow just as well.

Line 93: are the authors referring to cancer cells, or cancer-causing pathogens? Do such extensive longitudinal sequence datasets also exist for resistant bacteria and cancer-causing pathogens as for HIV, that would enable translation of this approach to those settings?

Line 106-107, Equation 1 appears to model the virus population size as a function of time (N(t)), rather than the rebound time explicitly (perhaps reword slightly?).

Line 119: in defining the actual rebound time, T=-γ^-1*logx, it would seem that this is a constant, since γ is a constant, and x is also an inferred constant. If this is correct, why is equation 1 needed? Likely, I am just missing something here!

Line 135: it might be helpful to talk more physically about what is meant by the 'birth' and 'death' of a variant (variant completely dies out? Or the variant population declines as a result of bnAb infusion?). Does a single amino acid mutation move a variant a to another type b?

Line 155: Is not the mutation rate of HIV well known already? Is the rate inferred by the authors in line with past estimates?

Line 156-157: The authors state that the 'fastest process in the dynamics…is the growth rate of susceptible viruses". Should this not say 'resistant viruses", since γ = 1/3 days-1 vs. 3 days-1 for susceptible viruses, or "slowest process"?

Line 174: "mutational target size" is not very intuitive for me. I know it is defined later on lines 211-213, but perhaps this can be summarized or stated more intuitively here, as well as in the Discussion?

Lines 178-182: the authors propose to infer mutation and fitness characteristics of escape-mediating HIV variants via sequence data. Work out of Arup Chakraborty's lab at MIT comes to mind on developing HIV fitness landscapes. Would this not offer the same information for parameterizing the birth-death model? Perhaps the potential relevance/connection between those past works and the current work could be briefly discussed.

In the section on 'Diversity of the viral population', it seems counterintuitive to me that characterizing only synonymous mutations as a measure of neutral genetic diversity would allow one to determine the 'chance to observe a rare (e.g., resistant) mutation' (line 185), since this implies a change in the amino acid sequence of the protein. I must not be thinking about this correctly; can the authors please clarify this for me?

Lines 222-223: The footprint of a bnAb is often larger than the actual epitope, which may contain both variable and conserved sites (e.g., the CD4 binding site). Thus, bnAbs must bind to both residue types. Given this, why do the authors expect HIV escape mutations to be intrinsically deleterious for the virus (implying they occur mostly at conserved sites), vs. occurring at the nearby variable sites that bnAbs also contact? For example, the following paper, https://www.pnas.org/content/115/4/E564, states that "Even for the relatively "conserved" CD4 binding-site region, only mutations at some residues are predicted to incur large fitness costs upon mutations."

Line 314: what do the authors classify as 'early rebound'? Below 56 days?

Line 330-332: the first part of this statement makes sense to me (that fitness-limiting bnAbs like PGT151 are best against high-diversity viral populations), but I am not certain about the second part. Wouldn't fitness-limiting and mutation-limiting bnAbs be equally good against low-diversity viral populations?

Lines 378-379: Might it be possible for the authors to speculate on how the exclusion of the dynamics of Ab concentration and IC50 neutralization during treatments could affect their results/conclusions?

Reviewer #2 (Recommendations for the authors):

In Appendix 1, the authors might consider coloring the resistant and susceptible amino acid identities based on the data source (DMS, patient-derived, crystallography).

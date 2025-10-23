# Peer review - Round 1

Editors:
- Mark Jit, London School of Hygiene & Tropical Medicine, and Public Health England , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.09520.012](https://doi.org/10.7554/eLife.09520.012)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Mapping residual transmission for malaria elimination" for peer review at eLife. Your submission has been favorably evaluated by Prabhat Jha (Senior editor), Mark Jit (Reviewing editor), and two reviewers, one of whom, John Drake, has agreed to reveal his identity.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

The reviewers and the Reviewing editor agreed that your paper takes a unique approach to modelling malaria transmission – that of linking cases with likely transmission pairs or groups. While similar approaches have been taken with viral respiratory illness (and likely other pathogens that we are not aware of) this appears to be the first application to a vector borne disease. It is sophisticated but not overly complicated and represents an important benchmark on the path to developing better analytics to guide and document the success of malaria elimination programs in sub-Saharan Africa. The analysis appears sound and internally consistent.

There are a few issues that we would like you to address, listed below. In addition, we normally require that modelling papers in eLife make their data openly accessible. Please could you tell us of your arrangements for this, or otherwise justify why you are not able to do so.

1) Can any indication of the temporal stability of the map of Rc be given? It is essential to know if the apparently smoldering foci are stable and therefore targets of intervention, or variable and therefore blanket control measures are all that is tractable.

2) We are not clear what view you have of the number of undetected cases or what effect that might have on their map. Presumably it is theoretically possible that all the Rcs are, in fact, several fold higher and case detection frustrates the exercise?

3) How much transmission might be asymptomatic? Swaziland was previously at higher transmission intensity and therefore many adults may be able to tolerate parasitaemia without becoming unwell.

4) When results on pairs of cases are presented in one figure then probabilities are assigned. However elsewhere and in the text the implication is made that a dichotomy has been made between cases that are linked and single cases – how have you moved from continuous probability to a dichotomy?

5) Genetic testing would be a more definitive way of distinguishing linked from unlinked cases. Can you comment on the likely utility of their modelling approach once genetic testing is available?

6) Is the "smoldering transmission" reflective of long-term transmission in the absence of imported cases, or does it require an imported case every so often to keep it smoldering?

7) Fine-grained needs a definition (pixel size? Or is it a point-process with pixelation simply for presentation purposes?).

8) There is a confluent area of high Rc in the North East. In the rest of the country there are occasional dots of high Rc scattered around. What is the possibility that these would have arisen by chance? The model implies very multiple comparisons. If a simulation was carried out where the episodes were randomly distributed through the population then how often would one see a "spike" of red colour in the map just due to chance?

9) If immigrants tend to go to the same places and at the same time (e.g. because they are all being recruited to work in the same factory) then that would increase the likelihood that the two cases would spuriously be associated in time and place despite not having a transmission cycle. Would that source of spurious linkage be accounted for in the migration data that was used?

10) Is there an issue with spatial autocorrelation (Figure 2 and zero inflated negative binomial regression)? Were the errors inspected? (In general, regression diagnostics, including differences in AIC values among models, have not been reported.)

11) What are the units in Tables 1 and 2? Were data centered and scaled prior to fitting GAMs? In my experience, this sometimes improves performance.

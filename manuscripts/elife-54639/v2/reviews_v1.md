# Peer review - Round 1

Editors:
- Philip A Cole, Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54639.sa1](https://doi.org/10.7554/eLife.54639.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study applies the FRESCO computational method to dramatically enhance the thermal stability of a dehydrogenase enzyme that has potential importance in the biotransformation of industrially relevant compounds. The use of X-ray crystal structural analysis of the optimized enzyme helps explain its exceptional properties. This study serves as an excellent model for what is possible in the thermal engineering of proteins using computational design.

Decision letter after peer review:

Thank you for submitting your article "Approaching boiling point stability of an alcohol dehydrogenase through computationally-guided enzyme engineering" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Reviewing/Senior Editor Philip Cole. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is an interesting paper that describes the successful application of FRESCO, a computational method for protein stabilization previously reported by the authors, for the stabilization of an alcohol dehydrogenase. Upon screening > 150 computationally selected mutations and combining the most stabilizing ones, the authors were able to obtain a 51 °C stabilization compared to the parent enzyme, which is an impressive achievement. By removing a stabilizing but deleterious mutation, the authors were able to achieve a significant level of stabilization without losing catalytic activity. This work encompasses a significant amount of work and the results are relevant and important. The structural analyses on the evolved variant nicely complement the characterization studies.

Essential revisions:

– The authors should clarify how accessible FRESCO is to the scientific community in terms of cost and technical aspects

– Have the authors determined the ee values for a range of substrates for their most thermostable enzyme? One worries that in the process of incorporating these mutations, stereochemical selectivities associated with the wt enzyme may be reduced or otherwise altered.

– All tables and graphs except Figure 5 are missing error bars. These should be included.

– "Since we suspected the S197E mutation to be problematic concerning coenzyme binding, based on the structural observations (Figure 3C),...". This is an important point that could be explained more clearly. It is not obvious from the Figure 3C why the S197E mutation should be deleterious for cofactor binding. Due to effect of mutation on the flexibility of the loop? What insights do the MD simulations provide into that? The E197 neg charge could cause electrostatic repulsion with phosphate of NADPH, but what is distance from E197 and the cofactor? And isn't E197 neg charge neutralized by interaction with Arg R18, as discussed in the manuscript? The electrostatic repulsion effect could be probed by comparing/contrasting activity of WT and mutant using NADH.

– "The initial FRESCO calculations and predictions for ADHA had a good hit rate: of the tested 177 mutations, 57 had a stabilizing effect of > 1 °C." This number should be adjusted considering error in Tm measurement (+/- 1C). Because of the error, it seems more appropriate to indicate # of mutants with DeltaTm> 2degC as significant.

– There is barely any reference to literature related to the use of computational design for enzyme stabilization. Below are some relevant papers that should be mentioned/cited (among others):

Malakauskas and Mayo, 1998; Bjørk et al., 2004; Korkegian et al., 2005; Gribenko et al., 2009; Borgo and Murphy, 2012; Bednar et al., 2015; Moore et al., 2017; Shah et al., 2007; Murphy et al., 2002.

Depending on the outcome of a thorough literature search, the authors might wish to revise the statement, "of all studies on stabilization of enzymes or proteins to date, to the best of our knowledge".

– Re: "The structure of ADHA bound to NADP+ unveils a well-defined catalytic pocket". This seems to be contradicted by the note in Figure 1 that the nicotinamide moiety is disordered.

– There is an unclear methodology aspect of the (probably too brief) introduction to FRESCO. At the outset it was not clear to what extent the coenzyme was included in the folding free energy or MD calculations. Near the end of the paper the authors say, "the employed computational algorithms (Rosettaddg and FoldX) cannot take into account the flavin-protein interactions (Wijma et al., 2018)." Completely omitting the coenzyme during ddG and MD calculations is a surprising enough action that the authors should be very explicit in the methods description.

– Another methodology clarification request. It is not clear whether visual inspection occurred for the 478 design models, the 478 MD simulations, or the 478 MD simulation final snapshots. The length of the MD simulations is either not mentioned or not sufficiently prominent.

– It is unclear if there was a quantitative threshold used to filter undesirable mutations? Similarly, when choosing 2 or 3 out of 4 beneficial mutations, how was the choice made? algorithm or biophysical intuition? Similarly, was the final roster of 177 mutations based on an unbiased, quantitative cutoff?

– Currently the comparison between panels A and B for "Figure 3. Michaelis-Menten" is awkward, since not only are there scale changes in both axes but also a unit change that might be overlooked.

– Re: "The interaction it would have with R18, when in the context of the other introduced mutations, was impossible predict". You mean to say, "impossible to predict", but might not more sampling reveal the new favored conformation? This seems like an excellent test case for developing improved FRESCO methods.

– The 6TQ8 difference between R-work and R-free is 10%, which seems rather large. We worry that there might be a significant level of bias in that model. The wwPDB validation report seemingly backs this up as a concern.

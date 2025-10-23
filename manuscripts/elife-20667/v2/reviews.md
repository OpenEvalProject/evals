# Peer review - Round 1

Reviewers:
- Daniel Segre, Boston University , United States

## Review text

DOI: [10.7554/eLife.20667.012](https://doi.org/10.7554/eLife.20667.012)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Design principles of autocatalytic cycles constrain enzyme kinetics and force over-expression at flux branch points" for consideration by eLife. Your article has been reviewed by four peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aviv Regev as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Frank Bruggeman (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This article addresses a very interesting and fundamental question about the nature of autocatalytic cycles within cellular metabolic networks, namely whether the existence and stability of steady states in such cycles imposes constraints on the kinetic parameters of the reactions involved. Starting from simple reactions, and gradually looking at slightly more complicated cases, the authors identify general rules that enzymes should follow in order for the autocatalytic cycles to support a stable flux.

All four reviewers agreed that the article is well written and original, and that it provides insightful and valuable results that would be in principle worth presenting to the audience of eLife. However, they also requested a number of important clarifications and revisions, as listed cumulatively below:

Essential revisions:

1) In the equation for "fa", there is no mention of the bisubstrate nature of the reaction. It is understood that the authors consider A constant, which seems a reasonable assumption to start with (though it may be interesting to entertain simple alternatives, e.g. as a constant influx of A – see also next point). However, it is not completely obvious that, even if the kinetic parameters relative to A in the M.M. equations are incorporated into the constants of the equation as shown, the bisubstrate nature of the reaction would not affect the generality of the conclusions drawn throughout the paper.

2) Both in the simple model, and in the extended ones, the authors consider A to be constant. This can be a convenient assumption for the simple model, but makes conclusions for realistic models less relevant, since consumption of A (lowering its level to a critical amount) can be an important part of the system's dynamics. The authors should either explore this alternative possibility, or provide a justification for why this would not be expected to affect significantly the main conclusions.

3) Even though the simple example that is treated in the paper nicely sets the stage and helps the reader in understanding the analytical approach, it is based on irreversible enzyme kinetics only. How do the requirements for proper functioning change when the reactions are catalysed by product-sensitive and reversible kinetics? Does product sensitivity prevent loss of stability? How does the displacement from thermodynamic equilibrium of the enzymes at the branch point influence the stability?

4) Allosteric regulation, within or onto, the autocatalytic subnetwork can also improve the robust functioning of the autocatalytic subnetwork. Have the authors analysed this? What did they find? This is particularly relevant in relation to the remark, which suggests that enzyme expression adjustment -- so, in fact rate adjustment -- can always lead to a non-zero, stable steady state. If so, then is it true that allosteric regulation could always lead to a steady state? Could one then make predictions about the kinetic design of autocatalytic cycles based on their allosteric control?

5) In subsection “Stability analysis for multiple-reaction cycles”, the authors mention that the affinity of the branch reaction to the intermediate metabolite of the cycle it consumes must be lower than the affinity of the corresponding recycling reaction of the cycle. Is this statement really correct, given that it is based on either a unscaled sensitivity (dv/ds and not dlnv/dlns) or a saturation degree, which generally also depend on the expression levels of the enzymes, i.e. their Vmaxs?

6) The theoretical predictions could and should be tested more strictly. Although the experimental results that are discussed are consistent with the predictions from the mathematical analysis, they could have alternative explanations. Low saturation of enzymes with their substrates is not uncommon in metabolic networks, and a number of hypotheses have been put forward to explain the apparently wasteful investment in high enzyme concentrations. See for instance refs. [1-6], not to mention some from this manuscript's authors. In fact, while according to the theory a single branching enzyme being less saturated than the cycle enzyme consuming the same substrate would warrant stability, the experimental data point to most of the branching enzymes being less saturated than the cycle enzymes, which makes the concern about alternative explanations pertinent. The authors may thus wish to discuss these potential alternative explanations, and explain why they eventually don't apply. As a negative control, the authors may wish to examine if enzymes branching from non-autocatalytic cycles tend to be more saturated with substrates from the cycle than those branching from autocatalytic cycles.

7) If lower expression of the enzymes catalyzing reactions that branch out from autocatalytic cycles leads to higher production rates of metabolic precursors, one would expect a negative correlation between the cellular abundance of some of these enzymes and growth rate. This prediction should be relatively straightforward to test based on published quantitative proteomics datasets. Again, a comparison with enzymes branching from non-autocatalytic cycles could be made as control.

8) An examination of the regulation of the branching enzymes may also provide additional support for the theory. E.g., these enzymes may be subject to competitive inhibition (to increase the apparent KM) under conditions where there is a higher demand for the cycle's intermediates.

9) It would also be very useful to have experimental data showing that forcing a lower activity or higher saturation of key branching enzymes would cause instability as predicted. However, this may require dedicated experiments, and should not be viewed as a necessary condition for acceptance.

10) While most of the paper seemed clearly written and unambiguous, several statements in the Introduction are imprecise or unclear. (a) One confusing aspect is the ambiguity between collectively autocatalytic systems and autocatalysis of their components. The component of a system that is collectively autocatalytic is in general not autocatalytic. Thus the statement in the second sentence of the Introduction is inaccurate. In fact, the authors themselves contradict that statement in paragraph two of the Introduction. (b) The authors mention that "autocatalytic systems have an inherent potential to be unstable as their operation changes the amount of their components". This last part of the sentence could be true for many other non-autocatalytic dynamical systems, so it is not clear that this statement is justified. (c)The concept of a system being catalytic "with respect to something" is not clearly defined (and, perhaps, unnecessary for clarifying the concept of a purely metabolic autocatalytic cycle); (d) It is not clear how the statement at the end of paragraph two ("Therefore….") follows as a logical consequence of the prior statement.

11) In the interest of reproducibility, the authors should provide supplementary material tables containing the data used for deriving Figure 6, as well as a description of how exactly the data was processed to generate the final flux estimates.

References

[1]. Weiss, S.L., Lee, E.A. & Diamond, J. (1998) Evolutionary matches of enzyme and transporter capacities to dietary substrate loads in the intestinal brush border. Proceedings Of The National Academy Of Sciences Of The United States Of America, 95, 2117-2121.

[2]. Suarez, R.K., Staples, J.F., Lighton, J.R.B. & West, T.G. (1997) Relationships between enzymatic flux capacities and metabolic flux rates: Nonequilibrium reactions in muscle glycolysis. Proceedings Of The National Academy Of Sciences Of The United States Of America, 94, 7065-7069.

[3]. Staples, J.F. & Suarez, R.K. (1997) Honeybee flight muscle phosphoglucose isomerase: Matching enzyme capacities to flux requirements at a near-equilibrium reaction. Journal of Experimental Biology, 200, 1247-1254

[4]. Salvador, A. & Savageau, M.A. (2003) Quantitative evolutionary design of glucose 6-phosphate dehydrogenase expression in human erythrocytes. Proceedings Of The National Academy Of Sciences Of The United States Of America, 100, 14463-14468

[5]. Salvador, A. & Savageau, M.A. (2006) Evolution of enzymes in a series is driven by dissimilar functional demands. Proceedings Of The National Academy Of Sciences Of The United States Of America, 103, 2226-2231

[6]. Eanes, W.F., Merritt, T.J.S., Flowers, J.M., Kumagai, S., Sezgin, E. & Zhu, C.T. (2006) Flux control and excess capacity in the enzymes of glycolysis and their relationship to flight metabolism in Drosophila melanogaster. Proceedings Of The National Academy Of Sciences Of The United States Of America, 103, 19413-19418

[7]. Tibor Gánti (2003) "The principles of life" Oxford, Oxford University Press

[8]. Semenov, S.N., Kraft, L.J., Ainla, A., Zhao, M., Baghbanzadeh, M., Campbell, V.E., Kang, K., Fox, J.M. & Whitesides, G.M. (2016) Autocatalytic, bistable, oscillatory networks of biologically relevant organic reactions. Nature, 537, 656-660.

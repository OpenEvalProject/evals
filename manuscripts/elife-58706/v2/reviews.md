# Peer review - Round 1

Editors:
- Michael T Laub, Massachusetts Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58706.sa1](https://doi.org/10.7554/eLife.58706.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Although aminoglycosides are important, clinically relevant antibiotics; the precise mechanism by which they kill bacteria has remained unclear and somewhat controversial. This paper uses clever imaging approaches based on a voltage-sensitive reporter to provides evidence that their bactericidal activity stems from a hyperpolarization of the inner membrane of cells rather than affecting uptake, or at least rather than affecting only uptake.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Membrane voltage dysregulation, not uptake, underlies bactericidal activity of aminoglycosides" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The reviewers each highlighted the general importance of the work and the notion that this work may be revealing an important new angle on aminoglycoside mechanism of action. However, there were significant concerns raised about whether the calcium transients were simply correlated with cell death or truly causal. And precisely how calcium transients would, at a mechanistic level, result in cell death was unclear. These concerns are laid out in some detail in the individual reviews provided below and we hope they will be helpful to the authors.

Reviewer #1:

This paper tackles an important and interesting problem, namely why aminoglycosides are bactericidal. Relying largely on a GCaMP6 reporter that is a calcium sensor, the authors provide some data to support a claim that aminoglycosides trigger hyperpolarization of the cell, which is ultimately lethal. Although this represents an intriguing new angle on aminoglycoside mechanism of action, I thought some of the results were overinterpreted and at the end of the paper I'm still left wondering (i) how aminoglycosides lead to the purported increase in ATP that the authors think drives reverse action of the F1Fo ATPase to produce hyperpolarization and (ii) how hyperpolarization ultimately kills cells.

1) Figure 2D: It definitely seems like low pH reduces transients, but the authors should verify that there is, in fact, less killing by aminoglycosides in this low pH environment.

4) For the results in Figure 3E, the authors argue that there's no correlation between GTTR uptake and calcium transients, but there seems to be some sort of pattern in which GTTR uptake increases after a long burst of transients, i.e. toward the end of each trace shown. So, I'm not fully convinced there's no relationship.

3) "However, single cell data showed the initiation of transients and the uptake of PI were not correlated. The catastrophic transients started before dye uptake in all observed cells." But couldn't it be that catastrophic transients arise more easily than PI uptake but that both are reporting on aminoglycoside-induced membrane defects?

4) I guess I don't really understand why pH and protonophore CCCP both diminish transients and aminoglycoside efficacy. Do these treatments prevent hyperpolarization or aminoglycoside uptake or something else? I can see why CCCP likely prevents hyperpolarization by dissipating the PMF, but then shouldn't acidic pH conditions exacerbate not rescue the effects seen?

5) The increase in CFU in Figure 4E following addition of CCCP at 1 hr is not particularly large – it looks like an increase of only 2-3 fold. Given the central importance of this experiment to the model, I'm worried about overinterpretation of modest effect sizes here.

6) In Figure 5 I think it's essential for the authors to measure ATP concentration in a more direct way than their fluorescent reporter, which doesn't seem to have a particularly large dynamic range.

7) Why do large calcium transients kill cells?

8) I don't really understand why aminoglycoside increase ATP levels as hypothesized based on the results in Figure 5. If it's just a matter of inhibiting translation, then shouldn't a bacteriostatic antibiotic like chloramphenicol show a similar increase in ATP?

Reviewer #2:

In the manuscript by Bruni et al., from Kralj's lab, the authors proposed that aminoglycoside bactericidal action arises from dysregulated membrane potential. The authors used a genetically encoded calcium sensor previously developed in Bruni et al., 2017.

The Introduction is very short and could contain more information about what is known on aminoglycoside uptake (EDP-I and II, PMF, feed forward loop,… Taber et al., 1987).

The results are interesting, provocative and conceptually new. However, clarifications, controls and new experiences are needed to support their conclusions.

Essential revisions:

My main concern is that the authors consider the uptake as an aminoglycoside mechanism of action. This point of view leads to surprising conclusions as in the title of the paper:

“Membrane voltage dysregulation, not uptake, underlies bactericidal activity of aminoglycosides.”

For me, aminoglycoside act on ribosomes, so uptake is essential, without uptake no death. The authors use a fluorescent gentamicin (GTTR) to track the uptake and observe that the calcium transients appear before the drug uptake. Is GTTR fluorescence detection sufficiently sensitive for this type of experiment?

It will be interesting if the authors could use their tools (GCaMP6, GTTR) in the conditions previously used in others studies to support their conclusions: adding chloramphenicol to block translation and EDP-II step; used PMF altered strains (nuo sdh, Fe-S biosynthesis) and Gm-resistant strain.

In the same vein, the authors need to clarify the impact of low pH, anoxic medium and CCCP (subsection “Aminoglycosides induced catastrophic calcium transients”), these three conditions are known to decrease PMF (essential for aminoglycoside uptake). Instead, the authors talk about "environments that diminish aminoglycoside efficacy".

The most surprising result is that even in presence of CCCP, the ribosomes are still dissociated with aminoglycoside, leading to the conclusion that voltage is not necessary for aminoglycoside uptake. Is it possible to detect GTTR fluorescence in the presence of CCCP?

In all experiments, the GCaMP6 fluorescence tends to increase even before adding drugs. Given that previous study of the same lab have shown that using agarose pad lead to a voltage-induced calcium flux via a local mechanical environment, it will be essential to represent in a same figure the control without aminoglycoside. Even though in the text (subsection “Aminoglycosides induced catastrophic calcium transients”) this comparison is made.

Reviewer #3:

Bruni and Kralj present data supporting that bactericidal activity of aminoglycosides relies on membrane voltage dysregulation. Specifically, the authors describe an interesting observation of fast calcium fluctuations in E. coli, under the addition of aminoglycosides that correlates with cellular death. Driven by this observation, they perform additional experiments and conclude that aminoglycosides increase ATP concentration inside bacterial cells, which reverses the F1Fo-ATPase activity, causing hyperpolarization and eventually cell death. Together, this work provides a better understanding of the bactericidal mechanism of antibiotics, which is very significant. In general, I found the paper meaningful, but I have major concerns regarding the main claims, and specifically regarding the proposed mechanism of action.

Essential revisions:

1) The authors claim that the increased cellular ATP reverses the activity of the F1Fo-ATPase generating a hyperpolarized state of the cell. While I agree with the authors that reverse activity of F1Fo-ATPase can cause hyperpolarization, it is unclear to me if this is the only, or even the major mechanism of hyperpolarization upon aminoglycoside treatment. The authors present two lines of evidence to argue their point: ATPase knockout mutants and mgtC expression data.

My first concern with the author's claims is that while some ATPase knockouts show a reduction of aminoglycosides action, there is no single mutant that abolishes the effect (changes in mean SD of calcium transient or recover CFUs). This is in contrast to the results where the authors truly abolish the hyperpolarization through other means such as CCCP or pH. This discrepancy suggests the possibility that the reverse activity of F1Fo-ATPase may not by the sole cause, or even the major cause of the hyperpolarization.

Second, the expression of MgtC eliminates the bactericidal activity of aminoglycosides. MgtC is a magnesium ion transporter, and thus it is also plausible to think that increased magnesium ion uptake prevents hyperpolarization.

2) Contrary to the authors claim, I could not find evidence in the manuscript to support that the catastrophic calcium transients are the direct cause of cell death. Even more, the fact that any cell that experienced calcium transients in the untreated condition did not divide, but did also not die (Introduction), provokes the question whether calcium transients are the true cause of death.

The authors would be better off, stating the relationship between calcium transients and cell death as a correlation rather than causation. However, if the authors choose to stick with their claim of causality, they have to show that calcium transients itself are sufficient to kill the cell, regardless of potential other effects related with hyperpolarization. Perhaps the authors could use a specific calcium chelator, such as BAPTA, to prevent calcium transient and therefore cellular death?

Below I detail my major concerns regarding the claimed mechanism of action:

- One of the most important results in this manuscript is that some ATPase knockouts affect calcium transients. To show the change between these mutants and WT strain, the authors measured differences in the mean GCaMP6 SD signal. My problem is that the measurements for different knockouts were done at different time points (Figure 5D top and bottom. See Table 1). I don't think that this is the proper way of comparing strains. It is unclear why the authors chose this strange comparison.

- Why is there so much variation of the GCaMP6 signal between WT replicas? For example, the same Figure 5D, and Figure 2—figure supplement 4C, Supplementary igure 5A, and 5E. In some cases, the variation between different WT replicas could be even larger than the difference between ATPase mutants and the WT strain.

- Furthermore, shouldn't the ATP concentration decrease if F1Fo-ATPase keeps hydrolyzing ATP?

- It is also not clear why the atpC knockout should have a higher membrane potential than WT. In the discussion, the authors do not mention anything about atpC.

- The authors do not mention why calcium transients (and possibly increase in ATP concentration) are not observed in other antibiotics that also impair ribosomal activity, such as chloramphenicol?

- Importantly, GCaMP6 signal doesn't report directly on the membrane potential. Therefore, to determine whether hyperpolarization induces a positive feedback on gentamycin uptake, it would be necessary to use a more direct membrane potential reporter, such as the one the authors used for their other measurements.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Membrane voltage dysregulation driven by metabolic dysfunction underlies bactericidal activity of aminoglycosides" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Wendy Garrett as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Daisy Lee (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

This paper examines the mechanism of killing by aminoglycoside antibiotics, providing evidence that their bactericidal activity stems from a hyperpolarization of the inner membrane of cells rather than affecting uptake, or at least rather than affecting only uptake. This revised version of the manuscript was deemed substantially improved by the reviewers and they are each enthusiastic about the work and the prospect of publishing it in eLife. However, one of the reviewers raised a couple of important points about the role of ATP and the reversal of ATP synthase that the authors should address, either by providing additional data or by adjusting the language in the papers and the claims made.

1) The revised manuscript still does not include an experiment addressing aminoglycoside uptake. Did the authors have any alternative to replace GTTR?

2) It is unclear what 'by metabolic dysfunction' in the title means. Do the authors mean increased intracellular ATP? While the abstract claims that 'the hyperpolarization arose from altered ATP flux', it is hard to understand why or how F1Fo ATPase reverts its action only when the membrane potential is high enough (inside is more negative), not in the other way around (inside is not as negative – it seems to me it's better to revert the action in this case since then they can increase the membrane potential to the normal level through reverting it…).

3) Throughout the data, it seems that the membrane potential plays a critical role in exerting bactericidal effects. While ATPase mutants and the mgtC expressing strain presented here likely have altered membrane potential without any antibiotic treatment, I couldn't find data showing their basal membrane potential level compared to the WT. Without the basal membrane potential data, it is impossible to discern if the phenotypes of the mutants are due to their basal membrane potential differences or by the author's main claim in the abstract. It would be very valuable if the authors can provide the basal membrane potential level of mutants compared to WT, CCCP added case, and/or pH6.5 case in the study.

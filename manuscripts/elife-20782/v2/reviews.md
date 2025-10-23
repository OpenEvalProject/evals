# Peer review - Round 1

Reviewers:
- David Kleinfeld, University of California, San Diego , United States

## Review text

DOI: [10.7554/eLife.20782.017](https://doi.org/10.7554/eLife.20782.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Vocal development in an integrated biological landscape" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Reviewing Editor David Kleinfeld and Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: David Golomb (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The development of vocalization proceeds at many physiological levels and includes changes in the geometry of the vocal tract, changes in the strength of respiratory and laryngeal muscles, changes in neuronal drive, and changes in the nature of feedback based on maturity and social interactions. The authors use computational and theoretical methods to model this process for the development of marmoset calls. A key realization is the need for a hierarchical model that progressively changes one aspect of the vocal system, e.g., geometry of the tract, until the desired target call remains out of bounds, at which point changes in a different set of physical parameters, e.g., muscular strength, occur. This approach is conjectured to mimic the changes that occur in development under evolutionary pressures.

Essential revisions:

All reviewers and the Reviewing Editor appreciate the importance of your approach. Reviewer #1 has some straightforward queries about the mathematics. However, the less mathematically savvy reviewer, #2, had difficulty in understanding your procedure. We encourage you to carefully edit the manuscript. I would suggest that the PI have neuroethology colleagues read the manuscript before resubmission. Further, the Reviewing Editor feels that terms need to be thoroughly explained, e.g., be explicit about the notional of a landscape in terms of the optimization procedures, spell out the machinations of Jayne's softmax procedure, etc.

Please address all of the issues in the two reviews below. Please heed the call of the second reviewer – a well-known expert in animal vocalization and someone that you would wish to comprehend and espouse on your work.

Reviewer #1:

The authors combine theoretical, computational and experimental methods to explain how the sound made by marmoset monkeys shifts from immature "cry" to mature "phee". A biomechanical model of voice production is described in "Material and methods". In contrast to the usual structure of research paper, its analysis is carried in that section. The derivation of the mechanical model, based on normal form transformation, is explained in the Appendix. The modification of model parameters, from those that lead to "cry" to those that lead to "phee", is described in the Results section. It is assumed that the two parameters, air pressure (α) and vocal fold tension (β) are equal and have both a value theta. A cost function of theta is defined, and several variations of this cost function, each one with more terms than the previous one, are examined. The most elaborated cost function accounts for the biomechanical, muscle and neural factor but not for the social factor.

The major experimental results and a brief description of the model appeared in a previous publication by the same group (Takahashi et al., Science, 2015). The derivation of the model using normal form analysis and the material about the cost function are new and justify a new publication where a simple model is used to explain development of animal behavior. I like the fact that the authors report what the model cannot explain changes in amount of parental feedback. There are several points that need rewriting or clarification.

1) Subsection 4.12, "Properties of the biomechanical model" describes results, and should therefore be moved the Results section, together with Figure 9. This inclusion will make the Results section more coherent more clear to read.

2) α and β are used as bifurcation parameters. In reality, they vary with time (for example, in Fig, 8). What is the dynamics of α and β during vocal activity (not the long-time scale of development)?

3) The authors assume that α=β=theta, and claim that "other choices of α and β that include the three types of calls yield similar results (subsection “2.3 Development of the vocal tract”). In contrast, Figure 9 shows that when α is reduced, the system undergoes a Hopf bifurcation (for large enough β), whereas when β is reduced, the system always undergoes a saddle-node bifurcation that yields slow limit cycles. Therefore, I'd expect that varying α has different effects than varying β.

4) I do not understand the role of the grey lines representing eta in Figure 3F.

Reviewer #2:

When I received the manuscript "Vocal development in an integrated biological landscape", by Teramoto et al., I thought I would be capable of writing a report. After reading the manuscript in detail, I am afraid I can only evaluate parts of the material.

The manuscript deals with the development of vocalizations in marmosets, and starts with a generic statement which is difficult to disagree with: "Vocal development is the adaptive coordination of the vocal apparatus, muscles, respiration and the nervous system". The authors then propose a way to translate Waddington's landscale metaphor into a quantitative way to address this developmental question.

My main problem with the manuscript is the abysmal difference between the sound, solid and rigorous treatment of the dynamics of the vocal apparatus, with the highly metaphoric ways in which the physiological instructions are treated. I have no way to evaluate these last parts of the work.

In my opinion, the "softmax action selection rule" as a way to predict the probability of uttering a cry, subharmonic sound or a phee call is at the antipodes of the detailed way in which the normal form of the equations for the vocal organ dynamics' is treated, and I have a hard time in putting all these abysmally different strategies together.

If a partial evaluation is of any use, the analysis of the vocal fold dynamics is excellent and sound. And of course, the general idea of the work, with its intention to cover the problem in an integrated way, intellectually appealing.

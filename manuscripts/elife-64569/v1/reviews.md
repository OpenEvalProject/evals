# Peer review - Round 1

Editors:
- Jennifer L Raymond, Stanford University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64569.sa1](https://doi.org/10.7554/eLife.64569.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study provides a rigorous, systematic analysis of 3D translational and rotational self-motion signals in the posterior cingulate and retrosplenial cortex. Strengths of the study include the comparison across brain areas; the experimental design to distinguish the contribution of vestibular, visual and other cues to the neural responses; and the modeling approach used to analyze the data.

Decision letter after peer review:

Thank you for submitting your article "Robust vestibular self-motion signals in macaque posterior cingulate region" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jennifer L Raymond as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Tirin Moore as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jean Laurens (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This manuscript characterizes the vestibular signals carried by neurons in the posterior cingulate cortex and restrosplenial cortex. The PPC has long been implicated in conveying self-motion signals to the navigation system. However, previous work did not disentangle the contribution of various sensory modalities to this function. The present study uses controlled visual and vestibular stimuli to demonstrate a strong pattern of vestibular responses in PPC, with weaker self-motion signals in RSC. The experiments are systematic and rigorous, with appropriate controls and comparisons across conditions. The manuscript could be improved by several changes in the way the results are analyzed and presented to facilitate comparison of vestibular signaling across regions of the cortex, including previously published results. The work provides foundational knowledge of that should be of interest to scientists studying sensory coding as well as those interested in spatial navigation.

Essential revisions:

1. The key question is not whether the vestibular responses are "significantly better" fit with a PVAJ model compared with VA-only model (which is roughly what BIC measures), but how much the various components influence the neuron's responses. Partial coefficient of correlation would be better suited than BIC to describe how various components contribute to neuronal responses.

2. The reviewers found the analysis of temporal tuning to be confusing, and thought it would be better to omit that analysis and go straight to the VA model.

3. The rationale for using non-linear rather than linear spatial tuning functions was not clear. Using a linear function would have the dual advantages of reduced chance of overfitting and allowing comparison with published results from other cortical areas (Laurens et al., eLife 2017).

4. The model allowed varied delay between the different components; this choice was not well justified, and lines 550-552 of the Discussion indicate that the inclusion of this delay affected the results. Please elaborate on this in the Results section, providing information about the delays obtained in the model fits, and more adequate justification of the choice of a varied temporal delay.

5. The source of the data from the MSTd is not clear. Were these neurons also recorded for this study? Or if data was used from another study, it should be clearly stated which study and the methods for recording these data.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Robust vestibular self-motion signals in macaque posterior cingulate region" for further consideration by eLife. Your revised article has been reviewed by 3 reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Tirin Moore as the Senior Editor.

Summary:

The point-by-point response indicates that the authors seriously considered the input from the reviewers. Unfortunately, some of the major concerns raised remain largely unresolved.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. Better address the concerns raised about the inclusion of a variable and lengthy delay for each signal in the model, and assumptions about which delays are longer

2. Do a more complete partial correlation analysis

3. Address concerns about overfitting

Reviewer #1:

The point-by-point response indicates that the authors seriously considered the input from the reviewers. Unfortunately, two of the major concerns raised remain largely unresolved.

I am particularly concerned about the inclusion of variable delays for each temporal component in the model. The range of relative delays between V and A components is quite broad, with many fits up to 300 ms. The authors describe that these delays are "reasonable", but without justification, and I am not persuaded that delay is reasonable for a vestibular signal, even at higher levels in cortical processing. Moreover, it is not clear why the figures show the relative delays between temporal components, rather than the absolute delay fit by the model for each component-P,V,A,J, and I am worried that those delays may be even longer and less plausible. Notably, the delays for the VA vs PVAJ models are different, with many shorter delays for the latter, suggested something is amiss with this element of the model, particularly in the VA model. Finally, in the supplementary figures showing results when a fixed delay was used (Figure 8-Supp 1 and Figure 10-Supp2), the legends do not make it clear that is what is being shown, or what the fixed delay was.

The rationale provided in the manuscript for using nonlinear rather than linear fits has not been extended at all. The point-by-point response indicates that the authors tried the linear model. It would be instructive to include in the manuscript documentation of shortcomings of the linear model, and what is gained by adding the nonlinearity.

Reviewer #2:

In this revision, the authors have addressed our comments, but with varying degree of success. For instance:

– The partial correlation analysis performed in response to comment 1 is not based on 3D model fits. Instead, they performed separate analysis is based on only 1 motion direction (which won't represent the contribution of different components accurately if their spatial tuning are not aligned). Furthermore, this analysis doesn't take the delays of various components into account. Furthermore, this analysis is presented in a very superficial manner (Figure 10S1). Overall, they performed an un-insightful partial correlation analysis and then added two main figures to present the PVAJ model: this makes the manuscript more complicated for little benefit.

– The authors didn't really shorten or eliminate the analysis of temporal tuning (as suggested in comment 2 to streamline the manuscript) but merely moved ten lines to Methods.

– Regarding the delays between various components (comment 4), they added histograms of these delays in Figure 8D and Figure 10E. However, these histograms show that these delays are always positive, e.g. they assumed that V always lags A (the axis label in these panels is ambiguous, btw). This assumption is justified in the text as follows: "the velocity time was set to lag the acceleration time because vestibular velocity signal is supposed to be an integral from the acceleration quantity" (lines 289-291).

Unfortunately, this is mathematically incorrect: first, just because velocity is the integral of acceleration doesn't imply that it "lags" it (except in special cases e.g. using sinusoids); those are completely different notions. Second, even if velocity did lag acceleration, this fact would already be represented by the shape of the temporal components used to fit the model, and imposing a positive delay between acceleration and velocity would still be incorrect. Likewise, the authors assume that position lags velocity for the same incorrect reason (lines 372-374) and that jerk lags acceleration with a justification which is quite incomprehensible (lines 371-372).

In principle, I can appreciate that having variable delays may be justified; for instance if different neuronal pathways conveying different dynamic components converge onto a cortical neuron. On the other hand, I have reservations about this method as it may promote overfitting. In any case, if the authors introduce variable delays, then they must allow each delay to be positive or negative since there is no justification for doing otherwise.

– On the other hand, they addressed a number of other issues correctly.

Overall, I find the current revision a little disappointing: the manuscript has become more complicated (two new figures) and, even though some issues were corrected, new were raised. Yet, I think that this work may be important enough to consider publication if these issues can be addressed in a new round of corrections.

Reviewer #3:

I think the authors have addressed the majority of points raised by the reviewers quite well.

They expanded their PVAJ to VA model comparison by partial correlation analysis, confirming the results they initially saw by only using BIC.

The reworked figures are better to read and understand and the data is a lot clearer in its representation.

The descriptions are clearer now and missing parts were added to the method section.

However, the main text still needs some editing in terms of language/grammar.

Examples:

line 171 about half neurons – about half of the neurons

Line 226 instead from other cues – instead of from other cues

Regarding the fixed versus varied lag:

It should be added to the figure legends when it shows fixed lag. Also, from visual inspection, the fixed delay does not necessarily look like a worse fit (at least for the PVAJ model, Figure 10D and Figure10—figure supplement 2), how was this quantified?

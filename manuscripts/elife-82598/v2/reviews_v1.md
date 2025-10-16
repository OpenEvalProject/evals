# Peer review - Round 1

Editors:
- J Andrew Pruszynski, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82598.sa0](https://doi.org/10.7554/eLife.82598.sa0)

This study provides valuable findings about how brain machine interfaces cope with changes in context, an important consideration for deploying such devices in the real world. The evidence supporting the claims is solid, and the findings will be of interest to motor neuroscientists and engineers developing brain machine interfaces.


---

# Peer review - Round 1

Editors:
- J Andrew Pruszynski, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82598.sa1](https://doi.org/10.7554/eLife.82598.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The Impact of Task Context on Predicting Finger Movements in a Brain-Machine Interface" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Andrew Pruszynski as the Reviewing Editor and Tamar Makin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Christian Éthier (Reviewer #1). We apologize for the delay in returning these reviews.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Provide a convincing explanation as to why the two BMI experiments (Figure 5A and B) gave different results. This is an important consideration as it forms the basis for a key conclusion of the study. This likely requires further data analysis.

2. The authors need to dive deeper into their data, specifically that which surrounds contextual shifts and the associated adjustment. There is a lot left on the table here that could broaden the scope and impact of the present study. All reviewers raise this point. For example, Reviewer 3 asks whether this adjustment reflects a 're-aiming' strategy. Again, this likely requires further data analysis.

3. The authors should provide a clearer description of how the present findings, which are in a very limited and narrow set of conditions, further BMI design principles in general. That is, how do the authors think the present results acquired in a limited context will generalize to the much wider set of contextual shifts that would be encountered in the real world.

4. There are a number of typos and general quality concerns with respect to the figures and the associated captions that are at the level that negatively influence the interpretability of the study and its findings. Specific suggestions are provided by the individual reviewers but a thorough revision is required in this respect.

Reviewer #1 (Recommendations for the authors):

A figure with pictures or drawings of the manipulandum in different context would be useful to better understand the experiment. Same for the virtual task/virtual hand. I'm not sure what the monkey

Perhaps the main body of the manuscript should contain a few words about what it means for channels to be 'tuned'. What criterion? Same for the definition of "changing activity".

On line 205 and Figure 2: if the spring resist flexion, why does the monkey activate is extensor muscle during flexion? To resist flexing too much? In this condition, is there tonic extensor muscle activity at the beginning of the trials? Moreover, this change in extensor and flexor synergy means that the monkeys not only scale their muscle activity for a different load, but seem to change their motor strategy. The different contexts thus require a non-linear change in muscle activity, but require more or less the same kinematics. How this impacts the decoders ability to generalize should be discussed.

Line 252-253: "This overall lack of change was surprising…" I fail to see how changing the hand configuration should impact online BMI performance. Because of differences in afferent, proprioceptive activity reaching the motor cortex? If the task is purely virtual, and the decoder good, the monkey can simply continue to try doing the "normal" task, rely on virtual feedback and should succeed. The "plant" in this case, does not change. It would be good to clarify if and how this was really an unexpected result.

Line 312: it would be helpful if the "window" was described here within the main manuscript

Figure 7: make it clear in the axes labels of panel C that "component 1 activation" refers to the first context-dependent component, not the first PC.

Methods line 561: indicate that the rotation is the direction of wrist flexion.

Reviewer #2 (Recommendations for the authors):

1. The authors state that BMI performance was minimally affected by context shifts because the animals were able to make fast adjustments online. However, they do not really dig into this adjustment. I recognize that there are only a few adjustment trials per context shift, but given the number of days and shifts on some of those days, I would imagine one could still examine the process of this adaptation in some detail. There are some nice examples of this in the literature, for example Golub et al. 2018 "Learning by neural reassociation" and Athalye et al. 2018. "Emergence of Coordinated Neural Dynamics Underlies Neuroprosthetic Learning and Skillful Control".

This seems like a missed opportunity to shed light on what cognitive strategies and/or neural tuning shifts. That in turn would lead to a more satisfying deeper story, which right now is essentially "neural activity changes between contexts, but BMI performance is okay, whew!".

2. As I alluded to in my summary statement, the difference in results between Figure 5A and 5B are quite substantial; the decoder trained off-context was quite a bit worse, and my view is that the current writing does not bring this finding to sufficient attention (e.g., the next paragraph starts with "To help explain how the monkeys were able to adjust to different contexts so well…"). A convincing explanation of why the two BMI experiments gave different results was not provided, but would be helpful for establishing confidence in the key conclusion. Rather, there's a greater focus on the lack of detrimental effect in figure 5A. To further explain my perspective: if this was a decoder innovation paper, a 32.6% improvement in times to target would be a big deal! So the performance decrease observed (and the asymmetry in what decoder+context mismatch is or is not compensated for) seems noteworthy. The Discussion should address this result, compared to the current "In both cases, the monkeys adjusted for the new context as quickly as they adjusted to normal online BMI trials."

3. Figure 1C – can the authors comment on why they think there are rather different changes in peak velocity between the two monkeys in response to the same experimental manipulations (e.g., opposite sign effect for flexion in the wrist condition)?

4. Lines 259-260 "This indicates that during the off-context online trials they adjusted and moved their hand differently to account for the context change". Couldn't it also be that they tried to move their hand the same as in the normal context (i.e., send the same descending motor command, with correspondingly the same firing rate patterns that the decoder picks up on and decodes "normally"), but the mechanical perturbation (e.g., springs) resulted in different hand movements. Said another way: imagine the (hypothetical, thought-experiment) scenario where there's no sensory feedback and the monkey is doing this all open-loop using whatever strategy they learned for the normal condition BCI. How are your Figure 4D results different from what we'd expect in this scenario?

5. Line 371-372: "In both cases, the monkeys adjusted for the new context as quickly as they adjusted to normal online BMI trials". Where was this shown? This sounds like a quantitative statement about how quickly performance reached the same level; but in the two-model (Figure 5b) tests off-context performance was substantially worse. And, I don't think the rate of adaption to normal BCI blocks was reported anywhere? Perhaps the authors meant something else and can rephrase to clarify?

6. Results are mostly consistent across both monkeys, but not every experiment or analysis is available from both muscles (e.g., EMG was only recorded from monkey N). While all the necessary information is present in the manuscript (e.g., via tables, figure legends, methods), I think the manuscript could be more clear in the main text to clarify which results are one-monkey results and which are two-monkey results. This helps the reader better assess the strength of evidence for each finding.

Reviewer #3 (Recommendations for the authors):

I have a number of specific.

1) It was not very easy to visualize what exactly the manipulandum was or what the effects of the springs were. A methods figure, perhaps as supplemental information would be useful. Related to this, it was not clear what the actual biomechanical effect of the springs were. Did they resist motion at specific joints, or across the entire digit. Can you also provide some details on the relative scale of the change in force (9.5N) to the range of grasp forces that normally be applied by the animal, or that would typically be applied in this task?

2) Based on the comment in the public review about whether M1 represents or generates movements, I would make two potential suggestions. You could simplify/reduce this text and streamline the introduction, or you could weave this idea and narrative throughout the manuscript, returning to it in the discussion. As it stands, this potentially important idea is raised, but then largely ignored for the rest of the paper.

3) In Figure 1D, what is the explanation for significantly increased activity in finger extensors during flexion in the spring context? Is this evidence of increased digit stiffness? If so, this could have interesting effects on population activity, as there is some evidence that stiffness control might be encoded in the cortex.

4) The method of calculating the Acquisition Time was not clear. Specifically, please provide a clearer description of how each dot in figure 4C and 5C are calculated. In the text description of 4C and 5C, it was difficult to interpret the text regarding which differences were significant and which were not, and what the differences in the text were referring to. For example, in Lines 263-266, it states that Monkey N had a short adaptation time (p = 0.002) and that Monkey W did not (p=0.22). I can't tell what exactly this is referring to in Figure 4C. Lastly, around line 290-292, it is stated that monkey W had no significant adaptation period. While I understand that the median z-score was close to 0, the range of z-scores in all cases in Figure 4C and 5C are very large. Were these randomly distributed across time? Was there a pattern? Can you say anything at all about the range of the z-scores themselves?

5) In the text, Figures 4D and 5D are discussed before 4C and 5C. Consider reorganizing the text or figure layout.

6) Regarding Figures 4D and 5D, is it possible to examine the distributions of the correlations in the normal and off-context trials and show this as error bars on each point? Can you statistically test whether the correlations really were different from each other to help support the claims in lines 280-290?

7) Throughout the discussion, it would be helpful to refer back to specific figures to support claims about the results of the manuscript.

8) The description of SBP data processing is unclear around Lines 497 and 504. What does it mean to sum the samples and track the quantity of samples? Please elaborate on what was done.

9) EMG channel differencing is unclear. On Lines 512-514, it sounds like you just did the difference of the 2 channels, which is fine. Was this done digitally after the fact? Please explain. This may help clarify the statement about also recording the 'partner' electrode.

10) Line 517: Provide additional details on the bandpass filter. What was the type and order of the filter?

11) Line 645: How common were unsuccessful trials?

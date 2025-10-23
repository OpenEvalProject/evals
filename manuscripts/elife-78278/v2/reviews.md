# Peer review - Round 1

Editors:
- Dan FM Goodman, https://ror.org/041kmwe10 Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78278.sa0](https://doi.org/10.7554/eLife.78278.sa0)

This important study combines behavioral data from guinea pigs and data from a classifier model to make a compelling case for which auditory features are important for classifying vocalisations. This study is likely to be of interest to both computational and experimental neuroscientists, in particular auditory neurophysiologists and cognitive and comparative neuroscientists. A strength of this work is that a model trained on natural calls was able to predict some aspects of responses to temporally and spectrally altered cues.


---

# Peer review - Round 1

Editors:
- Dan FM Goodman, https://ror.org/041kmwe10 Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78278.sa1](https://doi.org/10.7554/eLife.78278.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Vocalization categorization behavior explained by a feature-based auditory categorization model" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Dan FM Goodman as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Andrew King as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Patrick Krauss (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The statistical analysis seems to be underpowered. Reviewer #2 makes a suggestion for another approach.

2. The data and models do not seem to be sufficient to support some of the stronger claims made in the manuscript. Please revise the language.

Reviewer #1 (Recommendations for the authors):

I think this is a really nice paper. I love the approach and personally find the conclusions interesting and compelling. I think maybe the case for the strength of the predictions is somewhat overstated and the manuscript would be improved by toning that down a bit and acknowledging rather than explaining away divergences between model and data.

In figure 4, the R2 values are both 0.939. Can you confirm that this isn't an error? It seems surprising that they should have this identical value. Might be good to double-check that.

In figure 6, the model seems to perform best for a time stretch value not equal to 1. This seems surprising. Any thoughts on that?

In figure 7, what is being tested for the model? ISI drawn from same-category or other-category (chimeric)? Maybe show both separately? Generally, it's a bit hard to work out what's going on in this figure.

In figure 8C the decrease in performance of the model is referred to in the text as "only a slight decrease in d'" but this doesn't seem very consistent with what looks like quite a large decrease in the figure.

In the methods, for the tempo manipulation, could you explain more what the method is? I guess it is some sort of pitch-preserving transformation that is built into Audacity, but without knowing how that software works it's hard to know what's going on here.

Reviewer #2 (Recommendations for the authors):

I have concerns about the statistical analysis of the behavioral data and the main conclusions drawn from the study. A major weakness in the current manuscript is the statistical approach used for analyzing the behavior which is in all cases likely to be underpowered – given that the absence of an effect (e.g. pitch roving) is often taken as a key result, a more rigorous approach is needed (see below for detailed points). This could either take the form of Bayesian statistics which the likelihood of a significant effect or a null effect can be distinguished from an inconclusive effect (my guess is most tests run on 3 animals will be inconclusive) or better a mixed effect model in which the binary trial outcome is modelled according to e.g. the call type, pitch shift/temporal modulation with the individual GP as a fixed effect. This is likely to be a more sensitive analysis and the resulting β coefficients may be informative and may enable a more direct comparison to the model output (if the model is run on single trials, like the GP, then the exact same analysis could be performed on different model instantiations). It would also be possible to combine all animals into the same analysis with the task as a factor.

In terms of the interpretation; the classifier is essentially only looking at the spectrum (few of the statistics that e.g. Josh McDermott's group has identified as critical components of natural sounds are captured, such as frequency or amplitude modulation). This approach works for these highly reduced two-choice discriminations that can essentially be solved by looking at spectral properties, although the failures of the model to cope with temporal manipulations suggest its overfitting to the trained exemplars by looking at particular temporal windows. From the spectrograms it is clear that the temporal properties of the call are likely to be important – e.g. the purr is highly regular; a property that is maintained across different presentation rates, likely explaining why the GPs cope fine with short rates. Many of the findings here replicate Ojima and Horikawa (2016) – this should be stated explicitly within the manuscript. The behavioral data here are impressive but I'm not really sure what we should take away from the manuscript beyond that, except that for an unnaturally simple task an overly simple frequency-based classifier can solve the task in some instances and not others.

Detailed comments

Figure 3 – what is the performance of the trained exemplars here? From the other figures I guess a lot higher than for the generalization stimuli; it looks like performance does take a hit on novel exemplars (possibly for GPs and the model?). The authors should justify why they didn't present stimuli as rare (and randomly rewarded) probe stimuli to assess innate rather than learned generalization.

Figure 5. – segment length analysis – here the GP is much better at short segments. The model and the GP show a clear modulation in performance with segment length that is not picked up statistically due to an underpowered analysis. These data should either be analysed as a within animal logistic regression or an across animal mixed effect model. This could combine all 6 animals, with the task as a factor.

Figure 6 – again, repeated measures anova on 7 conditions in 3 animals (χ2); the fact that the p-value is >0.05 means nothing! The real question – is the model quantitatively similar (could be addressed by assessing the likelihood of getting the same performance by generating a distribution of model performance on many model instantiations and then asking if the GP data falls within 95% of the observed values) or is it qualitatively similar? – for example show the same variation in performance across different call rates. In F the GP performance is robust across all durations, with a gradual increase in performance from the shortest call durations. In contrast the model peaks around the trained duration. In E both the model and the GP peak at just less than 1x call duration, but the model does really poorly at short durations. To me, this isn't 'qualitatively similar'.

Figure 7 – why use the term chimeric in this figure and nowhere else? Are they not just the random ISI as in the second half of the figure?

Figure 8 – I'm surprised at how poorly the model does on the reversed chuts. Again, the lack of a significant difference here cannot be used as evidence for equivalent performance.

Figure 12 – I think I possibly don't understand this figure – how can the MIFs well suited for a purr vs chut distinction be different from a chut vs purr distinction? Either this needs elaboration or I think It would make far more sense to display chuts and whines (currently supplemental figure 12). Moreover, rather than these rather unintuitive bubble plots, a ranked list of each feature's contribution to the model, partial dependence plots, and individual conditional expectation plots would answer the question of which model features most contribute towards a guinea pig call categorization.

The model classifies the result based on weighted factors such as spectrotemporal information but does not consider specific biological neuronal networks that underly this categorization process. Moreover, the authors assert that intermediate-complexity features were responsible for call categorization; this assertion is expected as all MIFs selected are based on the inputted spectrotemporal data. In other words, the features in the classifier model could arguably said to be mid-complex as all vocalizations could be said to have inherent complexity. Together, the conclusions that the authors draw that this model could represent a biological basis for call categorization seem really to reach beyond the data; the model fits some aspects of the training set well but does not causally prove that GPs learn specific frequencies to represent calls early in their lives.

Reviewer #3 (Recommendations for the authors):

This is a great study! I appreciate the approach to complementing behavioral experiments with computational modelling.

Considering the temporal stretching/compressing and the pitch change experiment: it remains unclear if the MIF kernels used by the models were just stretched/compressed to compensate for the changed auditory input. If so, the modelling results are kind of trivial. In this case, the model provides no mechanistic explanation of the underlying neural processes. This issue should at least be addressed in the corresponding Results section and might be an interesting cornerstone for a follow-up study.

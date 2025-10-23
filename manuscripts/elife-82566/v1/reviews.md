# Peer review - Round 1

Editors:
- John T Serences, https://ror.org/0168r3w48 University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82566.sa0](https://doi.org/10.7554/eLife.82566.sa0)

Schütt and colleagues introduce a new method for statistical inference on representational geometries based on a cross-validated two-factor bootstrap that allows for generalization across both participants and stimuli while allowing the fitting of flexible models. In a series of elegant simulations and empirical analyses on existing datasets, the authors validate the method statistically. The work provides a fundamental and compelling advance for the analysis of representational geometries.


---

# Peer review - Round 1

Editors:
- John T Serences, https://ror.org/0168r3w48 University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82566.sa1](https://doi.org/10.7554/eLife.82566.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Statistical Inference on Representational Geometries" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The authors appear to get lost in details and some of the key methods are hard to find in the Methods section. This will make the paper hard to follow for those not super familiar with the analysis approach.

Expanding the section on testing for the presence of information would be very useful to broaden the appeal.

Expanding the discussion and exposition of the generalizability of the statistical tests (see Reviewer #1).

Reviewer #1 (Recommendations for the authors):

Schütt and colleagues introduce a new method for statistical inference on representational geometries based on a cross-validated two-factor bootstrap that allows for generalization across both participants and stimuli while allowing the fitting of flexible models. In a series of elegant simulations and empirical analyses on existing datasets, the authors validate the method statistically.

Strengths:

– The authors are clearly experts on the methods, and the statistical approach significantly improves upon the state of the art of existing methods in terms of generalization across participants and stimuli.

– There is a potential for this method to not only become a new standard for analyses of representational geometries but to be applicable to different methodological approaches that not only aim at generalizing to new participants but also to new stimuli.

– The treatment of the topic is very thorough, with both extensive simulations as well as validation using functional MRI and calcium imaging data.

– The authors introduce a number of complex yet highly informative and useful new methodological advances, such as the (re)discovery of Spearman rho_a for improved comparison of dissimilarities as compared to Kendall's tau_a.

Weaknesses:

– Overall, while the introduction starts off very nicely, the manuscript ends up being rather difficult to read. The authors appear to get lost in details in the main text. Other critical methodological details are buried in the Methods section. Specifically, the key methodological advance, the two-factor bootstrap, is barely explained in the main text, and in my reading, it is never mentioned what data are bootstrapped (i.e. original data, rows and columns in the RDM, individual cells in the RDM).

– The authors assume a lot of knowledge from the reader, often referring to very recent work or preprints in a matter-of-fact kind of way. While this can be seen as a strength and highlights the timeliness of the work, the constant mix of more established and recent methods makes it much harder for the reader to understand what is actually introduced in this work. This separation is solved nicely in the introduction but does not appear to continue into the Results section.

– Representational similarity analysis is recommended by the authors to be used for model comparison. However, a very common, probably even more common, use case is to test for the presence of information (i.e. is the representational similarity > 0), which, however, is only briefly discussed.

– The validity of the T-test based on bootstrap estimates for tests against chance seem to assume a null distribution for individual model-data comparisons that is centered around zero. However, negative similarities cannot be explained by population variance in the population null distribution, which is currently not discussed by the authors.

Are the claims of the authors justified?

– For comparisons between models, the claims of the authors clearly seem to be justified and reflect an important advance in the state-of-the-art statistical evaluation of representational geometries.

– That said, I believe that it is important to clarify the open statistical issue of generalizability to the population.

1. I really enjoyed reading this manuscript and believe it will make an important contribution to the field. That said, the authors introduce a lot in this work that is only indirectly related to the statistical analysis framework, and as a consequence, the manuscript is currently quite dense and hard to follow. I think that this manuscript would benefit strongly from a much more focused treatment of the key aspects (the introduction of the new method) and a reduction of the emphasis on advanced methods that are not key to this work (such as the use of reweighting and neuronal population sampling approaches, to name only a few).

I think the issue is that given the flexibility of analyzing representational geometries with RSA, the authors try to be as general as possible and try to encompass all possible use cases in their writing. In addition, the specific use case for a cross-validated two-factor bootstrap seems to be fitting flexible models, which alone is already quite advanced. I know this is difficult to solve, so I would like to provide one specific recommendation for making the manuscript easier to digest: it would perhaps help to first provide the reader with a quick run-through, without justifying all steps in detail but only summarizing the approach and the basic motivation for it. Then a more thorough treatment, including relevant parts from the methods section that explains the motivation behind the two-factor bootstrap could follow, again followed by extensive validation. This is just one suggestion for improving clarity.

2. Given the very common use of RSA for testing the presence of effects, rather than model comparison, I think the impact of this work would be strengthened if the authors expanded on their specific use case, even if it is comparably simple (they call this "simple dependence test", which is perhaps a little confusing to the reader).

3. RSA measures the match of one or more model RDMs with a data RDM. For a test against chance, without very specific biases, a negative representational similarity should not be found empirically for subjects and only for a subset of stimuli. Any such effects should thus only be caused by measurement noise or by stimulus variability. I am wondering to what degree this affects the ability to carry out valid inferences against the null at the population level. See Allefeld et al. (2016) for the treatment of a similar problem with decoding accuracies.

4. The introduction would benefit from a better motivation of the method. It seems as if the authors discuss previous work on RDMs but then jump to the introduction of the new method. Did no other method exist before? What were the issues with these methods, and what is the gap that needs to be filled? This would help the reader better understand why they should be reading this work.

5. While valid, the approach appears to be rather conservative, producing very low false positive rates. Are false negatives not a potentially problematic issue in that respect?

Reviewer #2 (Recommendations for the authors):

This paper addresses a major question in computational neuroscience by proposing a novel methodology to test models to explain behavioral/brain data that generalize across conditions and subjects using bootstrapping.

The experiments reported validate the claims of the authors. The methodology is applied and analysed in different available datasets.

I found particularly helpful and thorough the tests with the simulations. However, I found that the reported analysis is focused mainly on the newly proposed method, and this could bring a wider perspective into the picture.

It is with such simulated data that I believe a deeper discussion and possibly adding a comparison to existing methods, such as vanilla RSA and/or linear encoding methods could be reported to support the final discussion on the limitations of such existing methods. This would allow showcasing in which cases this method reveals new conclusions and has lower false positive rates, or in which cases there which method is limited to the experimental paradigm used to obtain the data (e.g., how many participants, repetitions, and conditions).

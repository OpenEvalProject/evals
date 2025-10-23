# Peer review - Round 1

Editors:
- Timothy O'Leary, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56265.sa1](https://doi.org/10.7554/eLife.56265.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Progress in understanding cellular and circuit mechanisms that underpin neural function depend on us being able to reconstitute key computations and high level functions from models that consist of simpler, biologically motivated building blocks. This requires choosing parameters in a model, yet even in the simplest models there tends to be a degenerate relationship between model parameters and its overall emergent function. Bittner and colleagues present a computationally tractable method for inferring parameter distributions that are consistent with an emergent property of interest and demonstrate its use in a variety of well-known circuit models, and show that the method compares favourably with state of the art sampling and parameter identification methods.

Decision letter after peer review:

Thank you for submitting your article "Interrogating theoretical models of neural computation with deep inference" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and John Huguenard as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Mark S. Goldman (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The editors have judged that your manuscript is of potential interest, but as described below significant additional work is required before it can be considered for publication. Adequate revisions may require extensive work and we ordinarily avoid passing a manuscript to a second round of review on this basis. However, we have made changes in our revision policy in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Bittner and colleagues introduce a machine learning framework for maximum entropy inference of model parameter distributions that are consistent with certain emergent model properties, specified by the investigator. The approach is illustrated on several models of potential interest.

Reviewers were broadly enthusiastic about the potential usefulness of this methodology. However, the reviews and ensuing discussion revealed several points of concern about the manuscript and the approach. The full reviewer comments are included below. The main concerns are summarized as follows.

Essential revisions:

1. The methodology is not adequately explained. Both the body text and methods section present a somewhat selective description that is very hard to follow in places and should be checked and rewritten for clarity, completeness, notational consistency and correctness.

2. The computational resources required to use this method are not adequately benchmarked. For example, the cosubmission (Macke et al) reported wall clock time, required hardware and iterations required to produce results by directly comparing to existing methods (approximate bayesian computation, naive sampling, etc.) Without transparent benchmarks it is not possible to assess the advance offered by this method.

3. The extent to which this method is generally/straightforwardly applicable was in doubt. It seemed as though a significant amount of computation was required to do inference on one specified property and that the computation would need to be run afresh to query a new property. The methodology in the cosubmission (Macke) made clear that computation required for successive inferences is 'amortized' during training on random parameters. Moreover, EPI seemed less flexible than the cosubmission's approach in that it required a differentiable loss function. The complementarity and advantages of this approach as opposed to the cosubmission's approach are therefore unclear.

4. Some examples lack depth in their treatment (see reviewer comments) and in some cases the presentation is somewhat misleading. The STG example is not in fact a model of the STG. The cosubmission (Macke) uses a model close to the original Prinz et al. model, which is a model of the pyloric subnetwork. It would be instructive to benchmark against this same model, including computation time/resources required. Secondly, the subsequent example (input-responsivity in a nonlinear sensory system) appeared to imply that EPI permits 'generation' and testing of hypotheses in a way that other methods do not. All the method really does is estimate a joint distribution of feasible parameters in a specific model which is manually inspected to propose hypotheses. Any other method (including brute force sampling) could be used in a similar way, so any claim that this is an integral advantage of EPI would be spurious. Indeed, one reviewer was confused about the origin of these hypotheses. While it is helpful to illustrate how EPI (and other methods) could be used, the writing needs to be far clearer in general and should clarify that EPI does not offer any new specific means of generating or evaluating hypotheses.

5. There is a substantial literature on parameter sensitivity analysis and inference in systems biology, applied dynamical systems and control that has been neglected in this manuscript. The manuscript needs to acknowledge, draw parallels and explain distinctions from current methods (ABC, profile likelihood, deep learning approaches, gaussian processes, etc). The under-referencing of this literature deepened concerns about whether this approach represented an advance. DOIs for a small subset of potentially relevant papers include:

https://doi.org/10.1038/nprot.2014.025

http://doi.org/10.1085/jgp.201311116

http://doi.org/10.1016/j.tcs.2008.07.005

http://doi.org/10.3182/20120711-3-BE-2027.00381

http://doi.org/10.1093/bioinformatics/btm382

http://doi.org/10.1111/j.1467-9868.2010.00765.x

http://doi.org/10.1098/rsfs.2011.0051

https://doi.org/10.1098/rsfs.2011.0047

http://doi.org/10.1214/16-BA1017

https://doi.org/10.1039/C0MB00107D

6. One of the reviewers expressed concern that the work might have had significant input from a senior colleague during its early stages, and that it might be worth discussing with the senior colleague whether their contribution was worthy of authorship. The authors may take this concern into account in revising the manuscript.

7. Finally, please also address specific points raised by the reviewers, included below.

Reviewer #1:

General Assessment: The authors introduce a machine learning framework for maximum entropy inference of model parameters which are consistent with certain emergent properties, which they call 'emergent property inference'. I think this is an interesting and direction, and this looks like a useful step towards this program. I think the paper could be improved with a more thorough discussion both of the broad principles their black box approach seeks to optimize, as well as the details of its implementation. I also think the detailed examples should be more self-contained. Finally I find this work to be somewhat misrepresented as a key to all of theoretical neuroscience. This approach may have some things to offer to the interesting problem of finding parameter regions of models, but this is not the entirety of, nor really a major part of theoretical neuroscience as I see it.

Other concerns:

(1) Maximizing the entropy of the distribution is not a reparameterization invariant exercise. That is, results depend on whether the model parameters contains rates or time constants, for example. I wonder if this approach is attempting to use a 'flat prior' in some sense which has the same reparameterization issue? Can the authors comment?

(2) I don't think this is a criticism of the work, but instead of the writing about it: I find the introductory paragraphs to give a rather limited overview of theory as finding parameters of models which contain the right phenomenology.

(3) I am somewhat familiar with the stomatognathic circuit model, and so that is where I think I understand what they have done best. I don't understand what I should take away from their paper with regards to this model. Are there any findings that hadn't been appreciated before? What does this method tell us about the system and or its model?

(4) I don't follow the other examples. Ideally more details should be given so that readers like myself who don't already know these systems can understand what's been done.

(5) In figure 2C, the difference between the confidence interval between linear and nonlinear predictions is huge! How much of this is due to nonlinearities, and how much is due to differences in the way these models are being evaluated?

Reviewer #2:

This is a very interesting approach to an extremely important question in theoretical neuroscience, and the mathematics and algorithms appear to be very rigorous. The complexities in using this in practice make me wonder if it will find wide application though: setting up the objective to be differentiable, tweaking hyperparameters for training, and interpreting the results; all seem to require a lot from the user. On the other hand, the authors are to be congratulated on providing high quality open source code including clear tutorials on how to use it.

1. Training deep networks is hard. Indeed the authors devote a substantial amount of the manuscript to techniques for training them, and note that different hyperparameters were necessary for each of the different studies. Can the authors be confident that they have found the network which gives maximum entropy or close to it? If so, how. If not, how does that affect the conclusions?

2. Interpreting the results still seems to require quite a lot of work. For example, from inspecting Figure 2 the authors extract four hypotheses. Why these four? Are there other hypotheses that could be extracted and if not how do we know there aren't? Could something systematic be said here?

3. Scalability. The authors state that the method should in principle be scalable, but does that apply to interpreting the results? For example, for the V1 model it seems that you need to look at 48 figures for 4 variables, and I believe this would scale as O(n2) with n variables. This seems to require an unsustainable amount of manual work?

4. There are some very particular choices made in the applications and I wonder how general the conclusions are as a consequence. For example, in Equation 5 the authors choose an arbitrary amount of variance 0.012 – why? In the same example, why look at y=0.1 and 0.5?

Reviewer #3:

This paper addresses a major issue in fitting neuroscience models: how to identify the often degenerate, or nearly degenerate, set of parameters that can underlie a set of experimental observations. Whereas previous techniques often depended upon brute force explorations or special parametric forms or local linearizations to generate sets of parameters consistent with measured properties, the authors take advantage of deep generative networks to address this problem. Overall, I think this paper and the complementary submission have the potential to be transformative contributions to model fitting efforts in neuroscience. That being said, since the primary contribution is the methodology, I think the paper requires more systematic comparisons to ground truth examples to demonstrate potential strengths and weaknesses, and more focus on methodology rather than applications.

1) The authors only have a single ground-truth example where they compare to a known result (a 2x2 linear dynamical system). It would be good to show how well this method compares to results from, for example, a direct brute force grid search of a system with a strongly non-elliptical (e.g. sharply bent) shaped parameter regime and a reasonably large (e.g. 5?) number of parameters corresponding to a particular property, to see how well the derived probability distribution overlaps the brute force grid search parameters (perhaps shown via several 2-D projections).

2) It was not obvious whether EPI actually scales well to higher dimensions and how much computation it would take (there is one claim that it 'should scale reasonably'). While I agree that examples with a small number of parameters is nice for illustration, a major issue is how to develop techniques that can handle large numbers of parameters (brute force, while inelegant, inefficient, and not producing an explicit probability distribution can do a reasonable job for small #'s of parameters). The authors should show some example of extending to larger number of parameters and do some checks to show that it appears to work. As a methodological contribution, the authors should also give some sense of how computationally intensive the method is and some sense of how it scales with size. This seems particularly relevant to, for example, trying to infer uncertainties in a large weight matrix or a non-parametric description of spatial or temporal responses or a sensory neuron (which I'm assuming this technique is not appropriate for? See point #4 below).

3) For the STG-like example, this was done for a very simple model that was motivated by the STG but isn't based on experimental recordings. Most of the brute force models of the STG seek to fit various waveform properties of neurons and relative phases. Could the model handle these types of analyses, or would it run into problems due to either needing to specify too many properties or because properties like "number of spikes per burst" are discrete rather than continuous? This isn't fatal, but would be good to consider and/or note explicitly.

4) The discussion should be expanded to be more specific about what problems the authors think the model is, or is not, appropriate for. Comparisons to the Goncalves article would also be helpful since users will want to know the comparative advantages/disadvantages of each method. (if the authors could coordinate running their methods on a common illustrative example, that would be cool, but not required).

5) Given that the paper is heavily a (very valuable!) methods paper for a general audience, the method should be better explained both in the main text and the supplement. Some specific ones are below, but the authors should more generally send the paper to naïve readers to check what is/is not well explained.

– Figure 1 is somewhat opaque and also has notational issues (e.g. omega is the frequency but also appears to be the random input sample).

– For the general audience of eLife, panels C and D are not well described individually or well connected to each other and don't illustrate or describe all of the relevant variables (including what q0 is and what x is).

– In Equation 2 (and also in the same equation in the supplement), it was not immediately obvious what the expectation was taken over.

– The authors don't specific the distribution of w (it's referred to only as 'a simple random variable', which is not clear).

– It was also sometimes hard to quickly find in the text basic, important quantities like what z was for a given simulation.

– The augmented Lagrangian optimization was not well explained or motivated. There is a reference to m=absolute value(mu) but I didn't see m in the above equation.

– Using mu to describe a vector that includes means and variances is confusing notation since mu often denotes means.

– It would be helpful to have a pseudo-code 'Algorithm' figure or section of the text.

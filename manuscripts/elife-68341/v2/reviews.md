# Peer review - Round 1

Editors:
- Marc Lipsitch, Harvard TH Chan School of Public Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68341.sa0](https://doi.org/10.7554/eLife.68341.sa0)

This is an excellent and elegant example of what theory can do at its best in epidemiology: it takes a widely observed phenomenon that is an ‘embarrassment’ (my word) to current theories; proposes a parsimonious explanation that is plausible for the phenomenon by extending the existing theories in a specific way; and makes a plausible case for the importance of the mechanism in explaining key features of the data. In this case, the embarrassing phenomenon is long periods of very slowly changing incidence/prevalence, and the modification to theory is incorporation of dynamic social heterogeneity. This should stimulate much further work in the field. Congratulations to the authors.


---

# Peer review - Round 1

Editors:
- Marc Lipsitch, Harvard TH Chan School of Public Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68341.sa1](https://doi.org/10.7554/eLife.68341.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Stochastic social behavior coupled to COVID-19 dynamics leads to waves, plateaus and an endemic state" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jennie Lavine (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. From the editor: This seems to be a very important theoretical advance.

It is written like a physics paper, and will provide unnecessary (stylistic, terminologic) obstacles to infectious disease modelers trying to understand and build on it. Strongly encourage you to find someone in the field that will use this kind of work post-COVID and have them help you explain what you have done. Major examples:

– p. 6 is very hard going. What is an "immunity factor"? This is not a biology word. Do you really mean attack rate? That is not the same as the number of people infected per day, and the heterogeneity in it is just hard to understand. Please, for the sake of your citations and longevity of this paper, translate it into epidemiology with the help of someone who would be a reader in the more applied field.

2. Please clarify and strengthen the claims of explanatory power.

A principal concern about the paper is the implicit claim that the model explains the epidemiological patterns of COVID-19 in the United States during summer and fall 2020.

The authors fit their model to US death data by estimating parameters related to the degree of mitigation as a function of time M(t), as well as some seasonality parameters affecting R0 as a function of time. It is not clear whether baseline R0 was also estimated, since it is not listed as a fixed.

As the authors point out, monotonically increasing R0M(t) in a standard well-mixed SIR far from herd immunity would result in a single peak that overshoots the (ever-increasing) HIT. In the authors' fitted model, deaths in fact initially decline in the northeast and midwest before rising again, and the epidemic in the south displays two peaks separated by a trough.

But it is not clear this is a particularly convincing demonstration of the correctness of a model as an explanation for the observed dynamics. Official distancing policies may have monotonially become more lax over the period June 1 through to, e.g., the fall. But restrictions were tightened in winter in response to surges, and there was clear signal of behavioral response to increasing transmission that seems unlikely to have been mere regression to the mean.

In the model, the mitigation function is fitted; no actual data on deliberate versus randomly- varying behavior change is used. Given clear empirical signals of synchronous and deliberate response to epidemiology, modulated by social factors (Weill et al., 2020), a persuasive demonstration that consideration of random behavioral variation is necessary and/or sufficient to explain observed US COVID-19 dynamics would need to start from mobility data itself, and then find some principled way of partitioning changes in mobility into those attributable to random variation versus deliberate (whether top-down or bottom-up) action.

3. A further main concern is that the central result of transient epidemiological dynamics due to transient concordance of abnormally high versus low social activity-stems from the choice to model social behavior as stochastic but also mean-seeking. While is this idealization plausible, it would be valuable to motivate it more.

In other words, the central, compelling message of the paper is that if collective activity levels sometimes spike and crash, but ultimately regress to the mean, so will transmission. The more that behavioral model can be motivated, the more compelling the paper will be.

4. Line 48: It seems to me that the dynamic heterogeneity you incorporate does involve feedback from the current number of infections through the dependence of h(t) on J(t), which might act as a form of knowledge-based adaptation. Please explain this point and include a biological description of how you generated the h(t) term.

5. How sensitive are the qualitative results to different values of τs?

6. Line 68: DIV(2020) – this citation is not in the references. Given that you also cite this for the data you plot, please include more details on where the data come from.

7. Line 222: The emergent long time constant seems to depend only on τs and k0 – is that correct? I would have thought the relaxation might also be affected by how rapidly the disease spread (i.e., M*J). This time scale is interesting and of relevance to public health measures, as it suggests when we might be reaching a sustainable plateau. Can you explain this in more detail?

Reviewer #1 (Recommendations for the authors):

1. Formal analysis and interpretation should better link the main text and the appendix In general, I would encourage the authors to link their formal model analysis in the Appendix more explicitly to the main text results. When a result is presented in the main text, the reader should be pointed to its derivation or justification in the appendix.

Similarly, to aid the less mathematical reader, it would be nice to interpret equations like S2 somewhat more when they are stated. For S2, for example, one could point out that the C(τ)ai(t) term reflects the individual's probability of infecting others conditional on having been infected τ units of time ago, while the ai(t − τ)Si(t − τ)J(t − τ) term reflects the probability that they were in fact infected τ units of time ago. With that in mind, I might adjust the notation slightly to highlight this by moving the J(t − τ) term into the average (though of course it can be factored out, as it does not depend on i) and grouping the two sets of terms in parentheses.

Moreover, having done the hard work of obtaining exact and/or approximate analytical results for their model, the authors should interpret these expressions more for the reader. e.g. the result about the HIT and λ in Equation 6 should be interpreted more in terms of the capacity for persistent heterogeneity to suppress the herd immunity threshold below the well-mixed case, and the contribution of even transient heterogeneity to determining the effective HIT.

2. Model definition. When introducing mathematical results and concepts in the main text, please make an explicit link to the corresponding Appendix derivations.

3. Code. In line with eLife guidelines, it would be good to provide the code used for model fitting, numerical solutions of differential equations, and stochastic simulations.

4. Undefined parameter γ Where is the parameter γ coming from in Equations S35 and subsequent? It is never defined. The other terms seem correct. Is this a holdover from a previous parametrization?

5. Model fitting. Model fitting procedures used to generate Figure 6 should be described in more detail in the appendix, and code should ideally be provided.

Reviewer #3 (Recommendations for the authors):

Line 48: It seems to me that the dynamic heterogeneity you incorporate does involve feedback from the current number of infections through the dependence of h(t) on J(t), which might act as a form of knowledge-based adaptation. Please explain this point and include a biological description of how you generated the h(t) term.

Line 68: DIV(2020) – this citation is not in the references. Given that you also cite this for the data you plot, please include more details on where the data come from.

How sensitive are the qualitative results to different values of τs?

Line 222: The emergent long time constant seems to depend only on τs and k0 – is that correct? I would have thought the relaxation might also be affected by how rapidly the disease spread (i.e., M*J). This time scale is interesting and of relevance to public health measures, as it suggests when we might be reaching a sustainable plateau. Can you explain this in more detail?

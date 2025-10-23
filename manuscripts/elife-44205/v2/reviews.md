# Peer review - Round 1

Editors:
- Katia Koelle, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.44205.024](https://doi.org/10.7554/eLife.44205.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Phylodynamic theory of persistence, extinction and speciation of rapidly adapting pathogens" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom served as a guest Reviewing Editor, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript analyzes a model of virus evolution in a host population in response to accumulating immune memory in previously infected individuals. The main result is a phase diagram that delineates qualitatively different modes of evolution (rapid extinction, strain proliferation, and metastable traveling fitness wave dynamics) as a function of evolutionary and epidemiological parameters.

Essential revisions:

The reviewers all agreed that the presented analyses were thorough and that the results were interesting. However, they also felt that several essential revisions were required:

1) The manuscript makes use of an existing status-based SIR model when mapping epidemiological dynamics on to the traveling wave evolutionary model. This model, first, should be explained in greater detail and with more clarity in the manuscript text. Further, this multi-strain model is one of two general types of multi-strain models (the other being a history-based model formulation). Are the phase diagram results robust to other SIR model formulations, including history-based formulations and the model formulation by Lin et al., 2003? Previous relevant work (Ballesteros et al. PLOS One) indicates that this might not be the case.

2) Text should be added to refer to several previous analyses that focus on very similar questions. Of particular importance is incorporating (to a much greater extent, both in the Introduction and starting around Equation 6) text that relates to the results presented recently in Rouzine and Rozhnova, 2018, ensuring that the overlap and the differences between these two analyses is accurately described. Koelle et al., 2011,) and Andreasen and Sasaki, 2006, also address similar questions about how certain epidemiological factors (population size, breadth of cross-immunity, etc.) affect whether and how quickly antigenic diversification will occur. The results presented here should be compared to those found earlier, even if these former approaches do not consider explicitly a traveling wave model. Finally, the way in which the epidemiological dynamics are mapped to fitness and how cross-immunity is quantified is identical to the approach outlined in Luksza et al., 2014, and this paper therefore needs to be cited, most notably in the context of Equations 1-3 and 4.

3) The mathematical conditions for the mapping onto fitness waves should be made more precise. This mapping is used throughout to describe the endemic regime. However, the traveling fitness wave formalism is derived under more specific assumptions, namely, the coexistence of many small-effect mutations (which corresponds to large values of q). Some parts of the phase diagram clearly fall outside this regime. While it may still be permissible to extend the asymptotic formulae, this should be discussed. We suggest to mark the boundary of the many-mutations regime, say, given by the condition U_b \gtrsim s, as a dotted line in the phase diagram.

4) In the Discussion, it would be important to emphasize that the metastability of the endemic regime is a result of the specific assumptions of this model and to discuss potential biological effects that alter the phase diagram. In particular, much work has been devoted to discuss mechanisms that stabilize the TW regime, e.g. the ideas of short-term broad cross-immunity (Ferguson et al., 2003, or random fitness components (Tria et al., 2005).

[Editors’ note: further revisions were requested before acceptance.]

Thank you for sending your article entitled "Phylodynamic theory of persistence, extinction and speciation of rapidly adapting pathogens" for peer review at eLife. Your article is being evaluated by two peer reviewers, and the evaluation is being overseen by a guest Reviewing Editor and Patricia Wittkopp as the Senior Editor.

The primary concern stems from details that are now provided in the revised manuscript that you submitted. Given these new details, reviewer #2 is particularly concerned that the epidemiological model does not incorporate infection histories appropriately, such that the results of this analysis do not advance the literature. The reviewer's request is that you re-do the entire analysis, using an epidemiological model structure that is appropriate. We would like to give you an opportunity to respond to this request, given the set of highly divergent approaches for modeling multi-strain dynamics.

Finally, the second reviewer requested that his/her entire initial review is transmitted in full. We will follow up shortly on the transmission of this entire review, as well as those from the two other reviewers.

We appreciate the value of simplified models; however, our previous comments we designed primarily towards making the simplifying assumptions explicit and to embed the epidemiological model better into the context of previous work on the subject, which we also discussed in the review consultation. Both issues are not yet adequately addressed in the current revision, and we regard the following points as essential for publication of this manuscript:

1) The assumptions underlying the epidemiological model, in particular with respect to the applicability to influenza, should be made explicit. It is not clear to us whether the model used here is indeed a generalization of previous models, as claimed. Specific points:

a) Some justification should be given for the steps leading from a general multi-strain immunity model to their Equations 1 – 3, e.g. along the lines of Rozhnova and Rouzine. For example, the authors could try to estimate, by the order of magnitude, the error of this approximation, at least, in a simple population configuration.

b) Equation 3 should be linked to the underlying dynamical model.

c) We also note again that the first application of this model to influenza data analysis (Lukza et al., 2014), which contains a very similar form of the equations and discusses their application to influenza, should be acknowledged in the context of Equations 1 – 3.

2) A quantitative comparison of the results of this paper to Bedford et al., 2012, and to Rozhnova and Rouzine should be given, for example in a supplementary figure. Specifically:

a) The fraction N_inf/N and average selection coefficient \σ, which allow the mapping to traveling wave theory, should be compared with previous work.

b) Also, it remains important to quantify the behaviour of the number of competing strains in the phase diagram (Figure 3B, C) in some fashion (see previous comment 3). The authors map the line q=1. Their reply otherwise refers to Figure 5, but it is not clear to us to which numbers q this refers to in Figure 3 (e.g., where is the locus q=10). Figure 3B, C shows two quantities as formulas in white font which we are not sure to which lines they refer to; please clarify and give units and numbers for these quantities.

Reviewer #2:

Unfortunately, not tracking the history of individual patients, i.e., not classifying patients according to previous infecting strains, is not a biologically correct approach, even though it has been done by two groups. This is not how the immune system works. One must track the memory cells from, at least, last infection. Virus infecting an individual reacts to memory in that individual, and not in other individuals. The oversimplification changes the results substantially and cannot be relied upon. For example, the turnover rate of population should not be an important parameter of the model. The dependence of the speed on parameters changes as well. We cannot be sure about the rest.

To avoid huge phase space, the simplest meaningful approximation is to track the last infection of an individual, i.e., to introduce the recovered uninfected individuals density and classify then according to memory cells left from their last infecting strain. One can show that older infection are a small correction. Then, consider multiple dimensions (analytically or numerically does not matter) and demonstrate that one-dimensional path arises automatically. After 1D path is assured, solve the 1D model analytically. Rouzine and Rozhnova did exactly that, in the case of the long-range immunity. Their multi-dimensional simulation is located in the end of Results and Supplementary Information. I also recommend to consult the previous numeric work of Bedford.

Therefore, I have to insist that the authors redo the work properly, with tracking the last memory of infection in individual. Otherwise, no numeric comparison is possible and cannot be in the future used for data comparison.

The original review follows for the authors' information:

The manuscript analyzes a model of the virus evolution in a host population due to accumulating immune memory in previously infected individuals. The authors use the SIR model by Gog et al., 2002, to map it to results of the traveling wave theory of evolution. If the cross-immunity between the virus and the memory is long-range, the authors demonstrate that the virus persists indefinitely. The state is a Red Queen process, a never-ending chase between virus and immune system in the antigenic space. If the cross-immunity is short-range, they find out that persistent infection is either unstable or splits into new states. An effective selection coefficient which makes the mapping to traveling wave possible is calculated.

The topic of the manuscript is important and the problem is challenging. The novel part of this work, compared to a recent paper on the same topic (below), is the comparison between long-range and short-range cross-immunity, and predicting the existence of a phase diagram of various behaviors including instability and oscillations.

I have some questions regarding the choice of the initial model, the sensitivity of results to its assumptions, and the connection to the previous work, as follows:

Major comments:

1) The SIR model is not explained in the manuscript, not the original paper by Gog et a. My questions are as follows.

a) According to my understanding, a typical infection is a stochastic event. An individual exposed to virus is either infected, at the systemic level, or not. If the individual is infected, the virus reaches high loads, causes a strong immune response, leaves high numbers of memory cells, and can be transmitted with appreciable probability to another individual. If the exposed individual is not infected at the systemic level, none of these events takes place. The probability of each of the two outcomes, given the exposure dose, depends on the presence of memory cells left from the previous infections, and their genetic distance from the infecting strain. Is this the scenario that the authors had in mind?

b) The model in MS considers a population structured into recovered and infected individuals classified by genetic variants of memory cells and virus, respectively. Are these population groups mutually excluding. What is their sum, the total population?

c) Can the authors draw a multi-compartment flow diagram of the model in supplement to show the processes they have included in the model?

d) An average adult person is infected by influenza virus more than once during lifetime. Indeed, between 4% and 20% individuals are infected annually. Therefore, all infections occur in previously infected (recovered) individuals. Yet, I do not see any infection of recovered individuals in model's equation. Who is infected then? This is especially confusing given that memory cells left from previous infections are the force that drives virus evolution.

f) What is the meaning of the exponential term in susceptibility S?

2) After Gog et al., 2002, Lin et al., 2003 have proposed an alternative, more transparent SIR model. Rouzine and Rozhnova, 2018 (RR) mapped that model to the traveling wave theory.

a) How does the change to Lin et al.'s version of SIR would affect the results on the stability of infection and the oscillatory states?

b) What is the difference with RR's results in the long range immunity case?

Additional comments:

3) In contrast to authors' statement, neither them nor RR's included the fluctuations of population size. If the authors implied that RR substituted the total population size instead of infected population to the traveling wave theory, they are mistaken: RR did the same rescaling.

4) The main difference between two models is in the choice of the initial SIR model (see above). RR considered the case of long-range cross-immunity only.

5) I would write the equations for the effective selection coefficient and for the rescaling of population size in separate lines, since they are important mapping formulas.

Reviewer #3:

The revised version has adequately addressed most of the comments, except the following:

I still think it would be relevant to quantify the behaviour of the number of competing strains in the phase diagram (Figure 3B, C) in some fashion (see previous comment 3). The authors map the line q=1. Their reply otherwise refers to Figure 5, but it is not clear to me to which numbers q this refers to in Figure 3 (e.g., where is the locus q=10). Figure 3B, C shows two quantities as formulas in white font which I am not sure to which lines they refer to; please clarify and give units and numbers for these quantities.

With this amendment, I think the paper is ready for publication.

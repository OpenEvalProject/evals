# Peer review - Round 1

Editors:
- Armita Nourmohammad, University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97350.3.sa0](https://doi.org/10.7554/eLife.97350.3.sa0)

This important study provides a new perspective on how human immunity shapes the antigenic evolution of pathogens. By combining theory and simulation the authors make a compelling case for the importance of eco-evolutionary interactions in population-level virus-host dynamics, which arise due to coupling between the dynamics of immune memories and viral variants. Although the work does not propose improved data-driven viral forecasting methods, it makes a conceptual contribution that advances the field's understanding of this problem's intrinsic difficulty.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97350.3.sa1](https://doi.org/10.7554/eLife.97350.3.sa1)

In this work, the authors study the dynamics of fast-adapting pathogens under immune pressure in a host population with prior immunity. In an immunologically diverse population, an antigenically escaping variant can perform a partial sweep, as opposed to a sweep in a homogeneous population. In a certain parameter regime, the frequency dynamics can be mapped onto a random walk with zero mean, which is reminiscent of neutral dynamics, albeit with differences in higher order moments. Next, they develop a simplified effective model of time dependent selection with expiring fitness advantage, and posit that the resulting partial sweep dynamics could explain the behaviour of influenza trajectories empirically found in earlier work (Barrat-Charlaix et al. Molecular Biology and Evolution, 2021). Finally, the authors put forward an interesting hypothesis: the mode of evolution is connected to the age of a lineage since ingression into the human population. A mode of meandering frequency trajectories and delayed fixation has indeed been observed in one of the long-established subtypes of human influenza, albeit so far only over a limited period from 2013 to 2020. The paper is overall interesting and well-written.

In the revised version, the authors have addressed questions on the role of clonal interference by new simulations in the SI, clarified the connection between the SIR model and vanishing-fitness models, and placed their analysis into the broader context of consumer resource dynamics.

However, the general conclusion, as stated in the abstract, that variant trajectories become unpredictable as a consequence of the SIR dynamics remains somewhat misleading. Two aspects contribute to this problem. (1) The empirical observation of ``quasi-neutrality', i.e. the absence of a net frequency increase inferred as an average of many trajectories at intermediate frequencies, does not imply that individual trajectories are neutral (i.e., fully stochastic and unpredictable) over the time span of observation. Rather, it just says that some have a positive and some have a negative selection coefficient over that time span. (2) As stated by the authors, the observation of average quasi-neutrality is indeed incompatible with the travelling wave model, where initially successful new variants are assumed to retain a fixed, positive selection coefficient from origination to fixation. This observation also limits predictions by extrapolation, where a positive selection coefficient inferred at small frequency is assumed to remain the same at later times and higher frequencies. However, predictions derived from Gog and Grenfell's multi-strain SIR model, as used by several authors, do not make the assumption of fixed selection coefficients and incorporate trajectory-specific, time-dependent expiration effects into their model predictions. This distinction remains blurred throughout the text of the paper.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97350.3.sa2](https://doi.org/10.7554/eLife.97350.3.sa2)

In this work the authors present a multi-strain SIR model in which viruses circulate in a heterogeneous population with different groups characterized by different cross-immunity structures. They reformulate the qualitative features of these SIR dynamics as a random walk characterized by new variants saturating at intermediate frequencies. Then they recast their microscopic description to an effective formalism in which viral strains lose fitness independently from one another. They study several features of this process numerically and analytically, such as the average variants frequency, the probability of fixation, and the coalescent time. They compare qualitatively the dynamics of this model to variants dynamics in RNA viruses such as flu and SARS-CoV-2

The idea that vanishing fitness mechanisms that produce partial sweeps may explain important features of flu evolution is very interesting. Its simplicity and potential generality make it a powerful framework. As noted by the authors, this may have important implications for predictability of virus evolution and such a framework may be beneficial when trying to build predictive models for vaccine design. The vanishing fitness model is well analyzed and produces interesting structures in the strains coalescent. Even though the comparison with data is largely qualitative, this formalism would be helpful when developing more accurate microscopic ingredients that could reproduce viral dynamics quantitatively.

This general framework has the potential to be more universal than human RNA viruses, in situations where invading mutants would saturate at intermediate frequencies.

The qualitative connection between the coarse-grained features of these vanishing fitness dynamics and structured SIR processes offers additional intuition relevant to host-pathogens interactions, although as noted by the authors other ecological processes could drive similar evolutionary patterns. The additions in the revised manuscript, substantiating more thoroughly the connection between the SIR and the vanishing fitness description, are important to better appreciate the scope of the work.

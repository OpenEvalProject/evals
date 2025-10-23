# Peer review - Round 1

Editors:
- Qiang Cui, Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.93099.4.sa0](https://doi.org/10.7554/eLife.93099.4.sa0)

In this potentially important study, the authors report results of QM/MM simulations and kinetic measurements for the phosphoryl-transfer step in adenylate kinase. The results point to the mechanistic proposal that the transition state ensemble is broader in the most efficient form of the enzyme (i.e., in the presence of Mg2+ in the active site) and thus a different activation entropy. With a broad set of computations and experimental analyses, the level of evidence is considered solid by some reviewers. On the other hand, there remain limitations in the computational analyses, especially regarding free energy profiles using different methodologies (shape of free energy profiles with DFTB vs. PBE QM/MM, and barriers with steered MD and umbrella sampling) and the activation entropy, leading some reviewers to the evaluation that the level of evidence is incomplete.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93099.4.sa1](https://doi.org/10.7554/eLife.93099.4.sa1)

Summary:

This study investigated the phosphoryl transfer mechanism of the enzyme adenylate kinase, using SCC-DFTB quantum mechanical/molecular mechanical (QM/MM) simulations, along with kinetic studies exploring the temperature and pH dependence of the enzyme's activity, as well as the effects of various active site mutants. Based on a broad free energy landscape near the transition state, the authors proposed the existence of wide transition states (TS), characterized by the transferring phosphoryl group adopting a meta-phosphate-like geometry with asymmetric bond distances to the nucleophilic and leaving oxygens. In support of this finding, kinetic experiments were conducted with Ca2+ ions at different temperatures and pH, which revealed a reduced entropy of activation and unique pH-dependence of the catalyzed reaction.

Strengths:

A combined application of simulation and experiments is a strength.

Weaknesses:

The conclusion that the enzyme-catalyzed reaction involves a wide transition state is not sufficiently clarified with some concerns about the determined free energy profiles compared to the experimental estimate. (See Recommendations for the authors.)

Comments on revisions:

While the authors have made some improvements in clarifying the manuscript, questions still remain about their conclusion regarding the wide-TS, which appears this may be a misinterpretation of the simulation results. Also, they should clearly point out the large discrepancies between DFTB QM/MM and PBE QM/MM results (shape of free energy files) and also between steered MD and umbrella sampling results (barriers). Another question is the large change in activation entropy (between the reaction with and without divalent cations). This difference may be difficult to attribute sorely to the difference in the reaction geometries near TS.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93099.4.sa2](https://doi.org/10.7554/eLife.93099.4.sa2)

Summary:

The authors report results of QM/MM simulations and kinetic measurements for the phosphoryl-transfer step in adenylate kinase. The main assertion of the paper is that a wide transition state ensemble is a key concept in enzyme catalysis as a strategy to circumvent entropic barriers. This assertion is based on observation of a "structurally wide" set of energetically equivalent configurations that lie along the reaction coordinate in QM/MM simulations, together with kinetic measurements that suggest a decrease of the entropy of activation.

Strengths:

The study combines theoretical calculations and supporting experiments.

Weaknesses:

The current paper hypothesizes a "wide" transition state ensemble as a catalytic strategy and key concept in enzyme catalysis. Overall, it is not clear the degree to which this hypothesis is fully supported by the data. The reasons are as follows:

(1) Enzyme catalysis reflects a rate enhancement with respect to a baseline reaction in solution. In order to assert that something is part of a catalytic strategy of an enzyme, it would be necessary to demonstrate from simulations that the activation entropy for the baseline reaction is indeed greater and the transition state ensemble less "wide". Alternatively stated, when indicating there is a "wide transition state ensemble" for the enzyme system - one needs to indicate that is with respect to the non-enzymatic reaction. However, these simulations were not performed and the comparisons not demonstrated. The authors state "This chemical step would take about 7000 years without the enzyme" making it impossible to measure; nonetheless, the simulations of the nonenzymatic reaction would be fairly straightforward to perform in order to demonstrate this key concept that is central to the paper. Rather, the authors examine the reaction in the absence of a catalytically important Mg ion.

(2) The observation of a "wide conformational ensemble" is not a quantitative measure of entropy. In order to make a meaningful computational prediction of the entropic contribution to the activation free energy, one would need to perform free energy simulations over a range of temperatures (for the enzymatic and non-enzymatic systems). Such simulations were not performed, and the entropy of activation was thus not quantified by the computational predictions. The authors instead use a wider TS ensemble as a proxy for larger entropy, and miss an opportunity to compare directly to the experimental measurements.

Comments on revisions:

Overall, I do not think the authors have been able to quantitatively support their conclusion, and the qualitative support is somewhat weak. This makes the interpretation of the computational results somewhat speculative. Nonetheless, comparison was made for models with and without divalent ions, and the experimental data is valuable.

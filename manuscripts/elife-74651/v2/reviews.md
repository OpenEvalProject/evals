# Peer review - Round 1

Editors:
- Tatyana O Sharpee, https://ror.org/03xez1567 Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74651.sa0](https://doi.org/10.7554/eLife.74651.sa0)

This work analyses how meaningful connections develop in the nervous system. The authors study the dissociated neuronal cultures and find that the information processing connections develop after 5–10 days. The direction of the information flow is influenced by neuronal bursting properties: the early bursting neurons emerge as sources and late bursting neurons become sinks in the information flow.


---

# Peer review - Round 1

Editors:
- Tatyana O Sharpee, https://ror.org/03xez1567 Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74651.sa1](https://doi.org/10.7554/eLife.74651.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Early lock-in of structured and specialised information flows during neural development" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please add results with additional methods as suggested by Reviewer 1.

2) Please expand the dataset to other publicly available data as suggested by Reviewer 2.

Reviewer #1 (Recommendations for the authors):

The submitted manuscript is well-structured and clearly written. In addition to the interesting and solid results presented in this paper by applying the continuous-time TE estimator on in vitro neural cultures, the reviewer is aware of the importance of developing accurate tools for the quantification of connectivity and information flows designed specifically for spike train data.

I suggest the acceptance of the manuscript for publication after the following comments are addressed:

A. Authors discovered interesting properties of developing neuronal networks showing that during bursting periods specific network nodes are engaged in specialized computational roles such as those of transmitters, receivers or mediators of information flow. Nevertheless, in order to investigate with full accuracy these specialized computational roles of neurons, it would be better to apply multivariate TE network inference (as the authors briefly discuss in lines 417-422), so as to elucidate the effects that nodes not involved in a bivariate analysis can have on the detection of these roles (especially that of mediator should be affected by spurious causality effects). Since the Authors have developed exactly this multivariate tool in their recent work, I wonder why such an approach has not been followed in this work, and how the presented results would change if a truly multivariate perspective to spike network analysis was undertaken.

B. The same dataset was analyzed by other researchers using various connectivity metrics, including also the same approach undertaken here. For instance, reference [64] employed the same continuous-time estimator of TE on the same data of dissociated neural cultures analyzed here, while other works [x, y] applied more standard metrics on these data, providing similar views about how these neuronal populations develop as a network across different stages of maturation. Reference and comparison to previous works is recommended to better place the present work in the context of the existing literature and to better understand the novelty and specificity of the results obtained.

[x] L. Minati et al., "Connectivity influences on nonlinear dynamics in weakly-synchronized networks: Insights from rossler systems, electronic chaotic oscillators, model and biological neurons," IEEE Access, vol. 7, pp. 174 793-174 821, 2019.

[y] J. H. Downes et al., "Emergence of a small-world functional network in cultured neurons," PLoS Comput. Biol, vol. 8, no. 5, p. e1002522, 2012.

C. The authors demonstrated the intrinsic early lock-in feature also in a model network of Izhikevich neurons, bringing this putative mechanism in a more general context. Still, it would be interesting to understand from a more detailed description how the different nature of biological and model neurons (MUA Vs. SUA) affects the underlying information flow.

D. Lines 88-89: Authors should provide the reason why and how they selected four cultures instead of analyzing all available 'overnight spontaneous dense' dataset of eleven cultures, and why the daytime spiking activity was discarded from the analysis ('daily spontaneous dense' dataset).

Reviewer #2 (Recommendations for the authors):

In this study the authors tackle the important problem of assessing information flow changes in developing neuronal cultures. They have previously developed a method that is the state of the art for information flow inference and apply it here to an existing dataset. But as mentioned in the public review, more data and analyses might be needed to validate their findings.

Main recommendation

I believe that this is an important work of wide interest for the systems and network neuroscience community. But the amount of data used is insufficient. Specially given that the publicly available dataset used is much richer. From the 2 used batches already, there's 5 and 6 cultures, with at least 15 different time points. Several more batches, with other firing patterns and densities are also present.

The work nicely demonstrates that neurons tend to assume the specialized computational roles of either transmitters, receivers or mediators of information flow, depending on burst position, i.e., early, middle and late bursters behave respectively as transmitters, mediators and receivers. A main strength of the work is the tool used for the analysis, i.e. a continuous-time estimator of the transfer entropy (TE) which was demonstrated in a recent work by the same authors to be far superior than the traditional discrete-time approach to TE estimation on neural data. The main weakness identified relies on a limited reference to previous literature analyzing the same publicly available data, and usage of insufficient dataset.

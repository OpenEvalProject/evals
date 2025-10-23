# Peer review - Round 1

Editors:
- Pierre Sens, Institut Curie, PSL Research University, CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56429.sa1](https://doi.org/10.7554/eLife.56429.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This is a combined experimental-theoretical investigation of transcription in development using elegant experimental methods and a comprehensive theoretical analysis. The aim is to distinguish between computational models predicting the transcriptional output of a developmental gene from time-varying concentrations of transcription factors. Based on quantitative comparisons between live-cell imaging measurements of transcription in the fly embryo and the predictions from three classes of computational models, the authors conclude that the data can only be accounted for by a non-equilibrium scheme describing the progression towards 'accessible' chromatin state as a multi-step process driven by transcription factors Bicoid and pioneering factor Zelda.

Decision letter after peer review:

Thank you for submitting your article "Quantitative dissection of transcription in development suggests transcription factor-driven chromatin accessibility" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Anatoly Kolomeisky (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Both reviewers and the Reviewing editor found the paper very interesting, thought provoking, and very well written. We are convinced that a non-equilibrium approach to transcription is very important. Your experimental approach is elegant and the data are of high quality. There is need for additional experiments. However, reviewers raised concerns about the novelty of your findings, and questioned certain modelling hypotheses. These important issues must be satisfactorily addressed before a decision regarding publication can be made. In our opinion, this can be done without additional wet lab experiments, and within a reasonable timeframe.

As the editors have judged that your manuscript is of interest, but as described below that major revisions are required, in particular regarding modelling and discussion, before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This is a combined experimental-theoretical investigation of transcription in development using elegant experimental methods and a comprehensive theoretical analysis.

The aim is to distinguish between computational models predicting the transcriptional output of a developmental gene from time-varying concentrations of transcription factors. Based on quantitative comparisons between live-cell imaging measurements of transcription in the fly embryo and the predictions from three classes of computational models, the authors conclude that the data can only be accounted for by a non-equilibrium scheme describing the progression towards 'accessible' chromatin state as a multi-step process driven by transcription factors Bicoid and pioneering factor Zelda.

Essential revisions:

Novelty and context

1) The novelty of the work in comparison with exiting studies reaching similar conclusions must be clarified. In particular in comparison [Dufourt et al., 2018] in which a different gene is studied, but within the same organism, in the same nuclear cycle and controlled by the same pioneering factor Zelda.

2) The Discussion must be extended to put the results in a broader context of existing literature. Non-equilibrium view on transcriptional regulation has been discussed before. is presented as new, although these ideas have been around and studied for a number of years already. See for instance Coulon et al., 2013, and discuss the parallels with the studies cited therein, which points to the same mechanisms of step-wise, irreversible, TF-driven progression of chromatin state towards a Pol II-accessible configuration.

Dufourt et al., 2018; Fritzsch et al., 2018; Coulon et al., 2013.

Further data analysis

3) The data seem under-exploited: The authors have access to single-cell information but only analyze ensemble-average traces. This is surprising since the model they put forward is intrinsically stochastic (governed by a few rate-limiting steps). Signatures of such stochastic behavior should be clear in the data. For instance: Given that the model posits that transcription starts after m=5 equivalent first order reactions, then a key prediction is that the first appearance of the MS2 signal among all individual traces at a given position along the embryo should be Gamma-distributed (with shape parameter m=5). Even if the first appearance of the MS2 spot is a noisy measurement, this should be measurable (as in [Fritzsch et al., 2018] Figure 4A) and the authors already have this data at hand.

Concerns regarding the model

3) In the equilibrium MWC model (Figure 2A), Zelda, although being a pioneering factor, is not represented as such. Here it acts by binding the 'accessible' state, hence simply by keeping chromatin from closing. Instead, a pioneering factor should be able to bind in the 'inaccessible' state and make this state unfavorable (e.g. weight = exp(∆_chrom / kT) * z * w_{z,chrom} with w_{z,chrom } > 0). How would this more realistic scenario affect the conclusions?

4) The model (Equation 6) essentially assumes that bicoid and zelda act independently, and in an additive manner. Is this supported by data? Does transcription happen without bicoid, ,as Equation 6 suggests. If the two factors act simultaneously, one would expect the rate π=[Bicoid][Zelda]. If they act sequentially, one would expect π=[Zelda][Bicoid]c1[Zelda]+c2[Bicoid]. The use of Equation 6 must be justified better, and the difference between the different possible microscopic scenario should be checked numerically and discussed.

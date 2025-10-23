# Eelbrain, a Python toolkit for time-continuous analysis with temporal response functions

## Authors

- Christian Brodbeck<sup>1</sup> ([ORCID: 0000-0001-8380-639X](https://orcid.org/0000-0001-8380-639X)) †
- Proloy Das<sup>2</sup> ([ORCID: 0000-0002-8807-042X](https://orcid.org/0000-0002-8807-042X))
- Marlies Gillis<sup>3</sup> ([ORCID: 0000-0002-3967-2950](https://orcid.org/0000-0002-3967-2950))
- Joshua P Kulasingham<sup>4</sup>
- Shohini Bhattasali<sup>5</sup> ([ORCID: 0000-0002-6767-6529](https://orcid.org/0000-0002-6767-6529))
- Phoebe Gaston<sup>1</sup>
- Philip Resnik<sup>6</sup>
- Jonathan Z Simon<sup>6</sup> ([ORCID: 0000-0003-0858-0698](https://orcid.org/0000-0003-0858-0698))

### Affiliations

1. University of Connecticut Storrs United States
2. Stanford University Stanford United States
3. KU Leuven Leuven Belgium
4. Linköping University Linköping Sweden
5. University of Toronto Toronto Canada
6. University of Maryland, College Park College Park United States

† Corresponding author

## Abstract

Even though human experience unfolds continuously in time, it is not strictly linear; instead, it entails cascading processes building hierarchical cognitive structures. For instance, during speech perception, humans transform a continuously varying acoustic signal into phonemes, words, and meaning, and these levels all have distinct but interdependent temporal structures. Time-lagged regression using temporal response functions (TRFs) has recently emerged as a promising tool for disentangling electrophysiological brain responses related to such complex models of perception. Here we introduce the Eelbrain Python toolkit, which makes this kind of analysis easy and accessible. We demonstrate its use, using continuous speech as a sample paradigm, with a freely available EEG dataset of audiobook listening. A companion GitHub repository provides the complete source code for the analysis, from raw data to group level statistics. More generally, we advocate a hypothesis-driven approach in which the experimenter specifies a hierarchy of time-continuous representations that are hypothesized to have contributed to brain responses, and uses those as predictor variables for the electrophysiological signal. This is analogous to a multiple regression problem, but with the addition of a time dimension. TRF analysis decomposes the brain signal into distinct responses associated with the different predictor variables by estimating a multivariate TRF (mTRF), quantifying the influence of each predictor on brain responses as a function of time(-lags). This allows asking two questions about the predictor variables: 1) Is there a significant neural representation corresponding to this predictor variable? And if so, 2) what are the temporal characteristics of the neural response associated with it? Thus, different predictor variables can be systematically combined and evaluated to jointly model neural processing at multiple hierarchical levels. We discuss applications of this approach, including the potential for linking algorithmic/representational theories at different cognitive levels to brain responses through computational models with appropriate linking hypotheses.

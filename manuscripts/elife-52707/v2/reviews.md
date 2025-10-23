# Peer review - Round 1

Editors:
- Alfonso Valencia, Barcelona Supercomputing Center - BSC Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52707.sa1](https://doi.org/10.7554/eLife.52707.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper proposes provides further evidence in support of the correlation between transcriptional profiles induced by drugs as predictor of drug synergies. A simple idea that was supported by the NCI-DREAM Drug Synergy Prediction Challenge. The RNAseq time profiles of Tamoxifen and Mefloquine, together with the one of the TM combination, are used to validate the hypothesis in two cell lines (MCF7 and LNCaP).

The paper deals adequately with the scarcity of experimental data to test the model (i.e. additional RNAseq longitudinal datasets), the difficulties with the possible toxic effect of the drug at certain doses and the possible activation of phospholipidosis by the two tested drugs.

The results are, interpreted in terms of the specific activation of the underlying gene regulatory networks as the mechanism underlying drug synergies. Based on these ideas an initial drug synergy prediction algorithm is proposed.

Decision letter after peer review:

Thank you for sending your article entitled "The transcriptomic response of cells to a drug combination is more than the sum of the responses to the monotherapies" for peer review at eLife. Your article has been evaluated by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kathryn Cheah as the Senior Editor.

The general concept of in-depth analysis of drug combination effect on expression in a few cell lines for a few drug is interesting and offers an alternative to large shallow studies with multiple drugs in many cell lines. The technical developments for the prediction of drug synergy are also very interesting and of potential general value. The key problem that require your input, as detailed below, are with the selection of the drugs and the deduction of the associated interpretation of the mechanism of action.

The reports below point out that tamoxifen and mefloquin, even if widely used, are well known lysosomotropic drugs used in very high concentrations. This represents problems of toxicity and implicates mechanisms that might have more to do with the biology of lysosomes that with any proposed mechanism. As detailed below, it is quite possible that the observed transcriptional response will be more directly related to a general lysosomal stress response than to a specific mechanisms of action of the drugs.

I have to add, that the journal's principles are against asking to include additional drugs, with more precise molecular mechanisms of action and well characterised off target profiles. In the study, since even if it will be an obvious solution will represent an amount of work beyond what is reasonable to ask in a revision.

Therefore, before taking a decision I would like to read your rebuttal to the issues raised above: drugs used in toxic concentrations and mechanisms of action related with unspecific lysosomal toxicity.

At the same time it will be good to hear your response to the rest of the questions below, including software accessibility.

Reviewer #1:

Thank you for the opportunity to review the manuscript from Diaz et al. The authors take on an important and unanswered scientific challenge in trying to predict and understand drug synergies from single drug transcriptomic observations. While I do have some comments to the manuscript I'm overall positive to the undertaking and the manuscript.

My only major concern is that data and source code is not available for peer review. It does say in the first page that this is to be made available but I could not find this.

A few general remarks:

– Drugs with more precisely described mechanisms of action could have been chosen to more intuitively rationalize over the discoveries.

– Code for reproducing analyses should be provided.

– How would the authors explain the contradictory observation that drug with somewhat similar gene expression profiles tend to act synergistically, while drugs with very similar gene expression profiles (e.g. two doses of the same drug) tend to not act synergistically, according to the bliss criterion?

Reviewer #2:

This is a good paper that describes investigation of drug combination effect on expression in a few cell lines for a few drug combinations. Efforts are made to predict drug synergy and efforts are made to show that their ideas generalize to other datasets; both of these efforts strengthen the paper.

I had trouble with the flow of the paper (the structure globally, not the writing locally), and how different components of the study were introduced. Overall I felt that the order of discussion points in the Introduction and early Results sections led to alternating ideas of what the paper contained. I had to read nearly half the paper before sorting it out. For example, you start by saying many general things that imply the study encompasses many drug combinations, then you discuss how you sacrifice breadth for depth and focus on M, T, and W, then you discuss correlations and results on larger datasets. All of this fits together, but a more compact summary/guide to the structure of the paper very early in Introduction could help guide the more casual reader (as even this detail oriented reader got a bit confused).

You introduce the study with much unneeded text about being first. Just focus on findings. Language about timeline linked to order does not last (as new studies emerge), change this language to date-linked and prior-study linked statements. This reviewer is not worried about novelty or being first for such an important topic that could well tolerate comparative studies and replication of results.

A lot rests on Figure 7A, but I do not find the relationship all that convincing.

Although Figure 2E has many data points it is based on your limited set of drugs and essentially one synergistic combination. This seems underpowered.

Is there a mix up in labeling Figure 1C, if not I am missing something, as the predictions don't seem to line up with what I expect given the text.

Reviewer #3:

The manuscript addresses an open and important problem in the field of pharmacology that is how to predict synergistic drug combinations and what are the mechanisms behind the synergy. The authors decided to focus on three drugs: Tamoxifen, Mefloquine and Withaferin and tested dose response of these drugs either alone or in pair-wise combinations and performed in depth transcriptomics studies at different time points. One of the main conclusions of the manuscript is that drugs with transcriptional responses that are correlated tend to be synergistic. Mechanistically the authors try to explain synergy as a caused by transcription factor cascades that are activated only in synergistic drug combinations.

My major concern is that two of the three drugs used, that is Tamoxifen and Mefloquine are well-known lysosomotropic drugs (see references below) that accumulate in lysosomes, especially at the very high concentrations as the ones used in this study, inducing large transcriptional changes. Also, it has been already reported that lysosomotropic drugs, including mefloquine, tend to have correlated expression profiles (Sirci et al., 2017). Also, somewhat troubling is that the only consistently synergistic combination was TM that is two lysosomotropic drugs at large dosages. The authors never mention property such as lysosomotropism and phospholipidosis but they really need to address this point and refer to the relevant literature (see below for some suggestions).

The authors try to address the problem that the synergistic effect they observed may be due to a dosage issue and not to the drug combination, so they treated the 25μM concentration of T in cells as synergistic of 5μM and 20μM and they indeed observed an EOB of 31.5 but not that high as the TM combination with EOB of 99.3. The TM combination, however, is 20μM T and 10μM M (if I understood correctly) so the total dosage is 30μM and it would have been nice to see the effect of T monotherapy to this concentration (and not to 25μM).

Unfortunately, despite the important problem and in depth analyses, the use of these two lysosomotropic drugs at this very large dosages makes the whole work less generic and a less appealing.

Also the overall conclusion that correlated transcriptional responses are a good predictor of synergy, is not that original as the authors themselves stated in the Introduction, similar conclusions were drawn in the DREAM challenge.

Useful references that should be cited in the manuscript:

Nioi et al., 2007; Ellegaard et al., 2016; Nadanaciva et al., 2011; Sirci et al., 2017; Petersen et al., 2013.

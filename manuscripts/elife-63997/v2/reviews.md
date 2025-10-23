# Peer review - Round 1

Editors:
- Elizabeth A Miller, MRC Laboratory of Molecular Biology United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63997.sa1](https://doi.org/10.7554/eLife.63997.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Quantitative glycoproteomics reveals substrate selectivity of the ER protein quality control sensors UGGT1 and UGGT2" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Elizabeth A Miller as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by David Ron as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: John C Christianson (Reviewer #2); Roberto Sitia (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

All reviewers were enthusiastic about the topic and quality of the work, which will make a substantive contribution to the chaperone and quality control community. However, reviewers had some good suggestions that would broaden the impact of the findings to the more general secretion/trafficking community.

Reviewers 1 and 2 both felt that the analysis of UGGT substrates could be deepened and the representation of the data improved. This would improve the utility of the dataset in terms of understanding of potential mechanisms of engagement and prediction of additional substrates. Specifically, we request further analysis of potential local determinants as suggested by reviewer 2 – domain structure, predicted disorder, etc.

Reviewers 1 and 3 had concerns about the pulse-chase experiments that should be addressed.

Finally, reviewer 3 raises a good point that the folding trajectory of clients might be altered by the absence of ALG6, which would impact recovery as UGGT substrates. Toning down the quantitative nature of the conclusions is probably warranted.

Reviewer #1:

UGGT has largely been studied using model substrates and non-physiological conditions. Here the Hebert lab uses a quantitative proteomics approach to define the full spectrum of endogenous substrates. On the whole the data seem very solid, the topic is important, and this seems like it will be a good resource for the community, but I think the overall impact is could be improved by addressing 2 specific concerns:

1) Figure 4: I question whether these density plots are a good way to present the data. Why not simple scatter plots that show the aa length for the different substrates. Related to this, it's not clear how "significance" was determined. In 4B, the number of glycans might be artifactually high in the UGGT substrate pool because of the nature of the GST purification. The authors claim that since substrates with few glycans were also detected, this isn't a concern, but I think sample bias can't be so simply ignored. Related to this, aa length of substrates may be similarly related to no. of glycans. Correcting for this might be possible.

2) Figure 5: The pulse-chase of IGF-R is essential to show that substrate fate is impacted by UGGT action. But the pulse-chase experiments shown are somewhat difficult for me to interpret. In the UGGT -/- conditions I don't see much mature form at all, certainly not increasing over time as the precursor would mature. Instead, I see decrease of the precursor, which might indicate degradation? This might amplify the impact and should be considered.

Reviewer #2:

This work by Adams and colleagues describes the identification of native client repertoires of the ER chaperones UGGT1/2 family of glucosyltransferases, to better understand the key roles played during glycoprotein biogenesis. The work is well-conceived and executed, while being conveyed in a clear and concise manner. Bioinformatic analysis of identified clients leads the authors to suggest UGGT1 and 2 may prefer different clients with different localisations, topologies and structures. Data on some identified examples (e.g. IGF-1R, ENPP, HEX B) dissects the steps in maturation and role played by UGGT1/2 to provide some mechanistic insight but would benefit from a bit more detail. However, these new data do open up the possibilities to better understand the scope of selective responsibilities of reglucosylation by UGGT1 and UGGT2 to govern the maturation efficiency within the glycoproteome.

The authors' clever scheme to isolate UGGT1/2 clients using a combination of CRISPR-edited cell lines and lectin-based affinity purification together with quantitative proteomics appears quite powerful and allows them to isolate and identify selectively dependent client proteins, an obviously valuable dataset. A shortcoming might be that the features determined as preferential for UGGT1/2 focus on the whole protein are not particularly specific, which leaves the reader wanting a bit more in depth analysis to draw out some potential "local" determinants. While analyses of the clients using UniProt defined features is certainly valid, it means the analysis and predictions are limited and not as detailed as they could have been.

1) It is not clear to this reviewer whether, in the example candidates studded with multiple glycosylation sites, whether it is always a single (or the same) glycan that determines engagement by UGGT1 or 2, or whether it varies and is rather, dependent upon the folded state of the protein. In lieu of performing detailed glycan analysis on clients, perhaps this could be discussed.

2) Moreover, are all glycosylation sites utilised in these clients or only some and does that influence UGGT1/2 engagement? Perhaps the authors might address this as an aspect that might help understand selective recognition by UGGT1 or 2.

3) In regard to the UGGT1/2 clients identified, are there intrinsic or local folding/maturation features that makes them more frequently in need of reglucosylation than the rest of the glycoproteome? If so, what might that feature be, if not something general like a TMD. Perhaps the authors could further assess the domain structures of clients, or the relative position of glycans within them to add an additional dimension. As a reader, I would like to better understand why these proteins and not the other 97% of glycoproteins enter this route of maturation.

4) Could UGGT activity play a determinant role in multimer assembly, say for the composition of the hexosaminidase dimer, for example where UGGT2 KO cells that reduce efficient trafficking of the HEX B subunit but not HEX A? Does this bias the composition and consequently function? More generally, could the activities of UGGT1/2 offer a point of modulation for multimer composition? The authors raised the point of the impact of the UPR in the Discussion, which might be relevant.

5) The authors report that 70% of UGGT1 clients are Type I membrane proteins, but relative to the total number of Type I proteins in the glycoproteome, this number is relatively small. Why these proteins and not the remaining Type I's? Are there unique structural features, folding trajectories or glycan positions that provide some clue as to why these are preferentially engaging UGGT1? (slight reiteration of point 3)

6) If the 3-fold change cut-off is progressively lowered (or raised), how long do the UGGT1/2 "preferences" outlined still hold true?

Reviewer #3:

In this clearly written manuscript, Adams et al. set up an ingenious system to identify the clients of UGGT1 and UGGT2. The former is known to act as a folding sensor in the ER lumen adding a glucose moiety to non-native glycoproteins so as to reinsert them in the calnexin/calreticulin cycle. It was not known whether UGGT2 has a role in living cells, and how this would differ from UGGT1.

Key to success was the use of CRISPR to generate cells lacking ALG6, an enzyme in the pathway that generates the oligosaccharide precursors to be transferred to certain asparagines in nascent glycoproteins. In the presence of glucosidase inhibitors, ALG6KO cells accumulated mono-glucosylated proteins only if UGGT1 and/or UGGT2 were present.

An elegant -omic comparison of mono-glucosylated proteins in WT, UGGT1KO, UGGT2KO and double knock outs, allowed the authors to demonstrate that i) both enzymes have activity in vivo; ii) they share some clients; ii) UGGT2 has preferential activity towards small, soluble proteins destined to endo-lysosomes, iii) UGGT1 prefers instead larger plasma-membrane proteins.

As a quantitative and qualitative characterization of the UGGT1-2 clientele is of general interest, the data deserve publication.

Altogether, the data support the conclusions taken. In this reviewer's opinion, however, there is a conceptual problem that the authors should consider and discuss. In the absence of ALG6, glycoprotein substrates are not able to bind calnexin and calreticulin before being glucosylated by the preferred UGGT. As this might shift the folding pathway, many potential clients of UGGT1 or 2 could go undetected. So, in all likelihood the proteins identified are indeed clients of either enzyme, but the quantitative conclusions should be softened and adequately discussed.

Figure 3. Somehow surprisingly, immunoblotting of the whole cell lysates reveals no significant differences in the mature/pro-form ratios in any of the three clients analyzed. This is hard to reconcile with the pulse-chase experiment shown for IGF-1R.The authors may wish to comment about this discrepancy.

Despite sustaining the conclusions taken by the authors, the gels shown in Figures 3I, 3M and 5E are of rather low quality. An effort to improve the aesthetics of the experiments is worth. In Figure 5, a one-hour pulse is quite long to follow the folding of a glycoprotein. A shorter pulse might reveal more details.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Quantitative glycoproteomics reveals substrate selectivity of the ER protein quality control sensors UGGT1 and UGGT2" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Elizabeth A Miller as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by David Ron as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: John C Christianson (Reviewer #2); Roberto Sitia (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

Secretory and membrane proteins are subject to strict quality control, driven in part by engagement with the lectin/chaperone system of the endoplasmic reticulum. Here, the authors have devised an elegant strategy to systematically identify clients that engage either of two separate glycosyltransferases that regulate engagement with this pathway. This analysis provides insight into properties that govern quality control and provide a framework for understanding how protein folding influences secretion.

Revisions:

With apologize for not catching the specific points mentioned by reviewer 1 below, we ask for textual changes that address these concerns. To be clear, we are not asking for additional experiments to be performed, although you may have data from the ALG6/UGGT1/2-/- cells already, which would speak to point no. 1. If not, then perhaps you could include an acknowledgement that alternative pathways may contribute, or an explanation of why that is unlikely to be the case.

Reviewer #1:

The revised version is improved and addresses my previous concerns. On re-reading, however, I was struck by a couple of things that might be addressed by the authors textually. Alternatively, I may have missed something…

First, it seems that it would be a good idea to repeat the mass spectrometry in an ALG6/UGGT1/2-/- triple KO/KD condition to know that hits recovered in the UGGT single mutants are not non-specific or arising from some redundant enzyme. This is shown in Figure 3 for specific substrates, so it may not be an issue, but it seemed to me to be a potentially important control.

Second, I seem to be missing something with regard to the hits recovered from the ALG6 KO cells versus those with the UGGT enzymes also KO'ed. I would have thought that the ALG6 proteome should encompass all UGGT hits, with smaller numbers of proteins recovered from the single mutants (and none recovered from a double). Yet, there are fewer proteins in the ALG6 -/- calnexin-precipitated proteome. What am I missing? Is this important?

Finally, in the analysis presented in Figure 4 (which is much easier to interpret now) I wonder if it's worth separating out the lysosomal N-glycoproteome given that the authors claim UGGT clients are more likely to be lysosomal proteins. If one just considers the lysosomal cohort of N-glycome, does this profile more closely resemble the UGGT proteome?

None of these are essential points, but might strengthen an already interesting study.

Reviewer #2:

The revised manuscript has taken on board the comments and suggestions of this reviewer to a satisfactory degree. While it would be desirable for the authors to have been able to say more about the determinants for client selectivity by UGGT1/2, this is a complex question and arguably beyond the scope of the current work. The quality of the images and graphs has been improved to better represent the data presented. Moreover, the authors have now included additional statements and/or paragraphs to clarify their results which were unclear or ambiguous. At present, the manuscript will be a valuable resource for the scientific community.

Reviewer #3:

In this reviewer's opinion, the authors provided satisfactory answers to the criticisms raised to the original version, and the data sustain the conclusions reached.

One can always improve the aesthetics of a paper, but there is a moment in which the information package can be considered sufficiently complete. This seems to be the case for this study.

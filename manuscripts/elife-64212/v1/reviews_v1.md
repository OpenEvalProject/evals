# Peer review - Round 1

Editors:
- Martin Eilers, University of Würzburg Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64212.sa1](https://doi.org/10.7554/eLife.64212.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Loss of MGA mediated Polycomb repression promotes tumor progression and invasiveness" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Martin Eilers as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kevin Struhl as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

The reviewers agreed that the paper provides strong in vivo data for a tumor-suppressive role for Mga in lung carcinogenesis. The authors are convincing that MGA is important in oncogenesis. We note here that MGA is highly understudied (~200 publications) in and of itself despite its involvement with the MYC network for oncogenesis (~41,000 publications at the current time). Given a protein of 3000 amino acids, the number of potential protein partners and PTMs that might modify its tumor suppressor functions are staggering. However, the reviewers also noted that a previous paper has addressed the same topic and the novelty of the data presented here needs to better explained and additional experiments are needed to strengthen and expand the new aspects.

There are several loosely articulated stories here, but the reader does not come away with a clear take-home message. No particular oncogenic pathway is intensively explored or elucidated. MGA seems to be quite a general tumor suppressor, so is there a reason to focus experiments on lung vs. colon adenocarcinomas, or are these convenient models to explore general MGA action? The PRC1.6 story is interesting, but it is not integrated into a general description of MGA action. We think the authors buried the lede here; the take home message should be that there are multiple, perhaps independent mechanisms for tumor suppression embedded in MGA; these mechanisms should be clearly enumerated and the evidence for each supported. As presented, there is little attempt to separate or coordinate the various anti-oncogenic functions and contributions of the different domains of MGA-T-box, bHLH, or DUF480. Just considering the bHLH domain, there are multiple possibilities for MGA to disturb the MYC-network and suppress oncogenesis. The actin protrusions seem to be related to DUF480 but unrelated to PRC1.6; they probably relate with the observations about migration, wound healing and EMT (and so may also be relevant for T-box functions). I would suggest a serious re-write to identify, organize and reinforce their story(ies).

1. It seems that the investigation of publicly available datasets is essentially identical to the Schaub et al.. analysis and not new data. If the authors want to maintain this, they would need to better explain what is new. One important piece of information that seems to be missing is whether the mutations are homozygous or heterozygous. So data on MGA and MYC protein expression in human tumors would greatly strengthen this part.

Inspections of the MGA mutations on cBio portal reveals broad tissue specificity of tumors, well beyond lung and colon adenocarcinomas-in view of this range there is really no need to justify the choice of tumors, only to be wary whether differences in expression of MGA targets truly reflect MGA versus the tissue as the source of a non-pathogenic difference. Looking at the distribution of the mutations within MGA, I disagree with the assertion that DUF480 is a hotspot. The only lukewarm to hot spot in the protein seems to be the bHLH region. The other mutations are rather evenly distributed throughout the protein. This does not mean that they are not pathogenic, more likely it indicates a broad range of contributory motifs and domains. I suspect that there is a lot of interesting and important biology throughout these 3000 residues.

2. Conceptually, one would like to know whether tumor development in an MGA-delete situation depends on MYC. One would also like to know whether the polycomb complex that is assembled by MGA is tumor-suppressive. Therefore, the authors should perform a similar analysis as they did for MGA (introduce sgRNAs into the lung models) and score the phenotypes they get. Both experiments could be done in cell lines established from this model and either in vitro (that would allow a mechanistic analysis, e.g. RNA seq) or upon re-transplantation. This would also prevent simply reporting negative results.

3. The interpretation of the VENN diagram and the heatmaps in Figure 5A,B is somewhat uncertain. If one plots these for MYC, occupancy often simply parallels occupancy by RNAPII, so essentially being bound by MYC simply says the promoter is open/active. Is this the case for MGA and its complex partners? Or is there a specificity in binding? The authors should do RNAPII ChipSeqs in these cells, preferentially +/- MGA, and then show these alongside (and plot a correlation between MYC, RNAPII and MGA occupancy).

Along these lines, it is hard to understand how one obtain the extreme p-values shown in figure 5E and 5H, I would challenge this. If the authors want to maintain this, they should not use ENCODe data, but simply determine what genes are active in the cells (e.g. what promoters are bound by RNAPII) and then use those as background list and calculate P-values for overlap between MYC, MAX and E2F6.

Based on the description, the ChIPSeq analyses are not spike-normalized and I could not find information about the number of repeats. If it is n=1, the authors need to find a way to exclude that the differences are due to experimental variation.

4. The authors use the term "Empty" vector for their sgMGA -CRISPR-cas-Cre lentivirus without the sgRNA. This is confusing-what they mean is minus-sg; the vector is hardly "empty". While it would have been nice to have a non-targeting sgRNA just to ensure that no part of the phenotype reflects off-target or non-specific effects of CRISPR-CAS or CRE-expression, at least they should make clear in the text what is the difference between the vectors.

5. The methods describing the observation and quantitation of the actin protrusions are a bit sparse. The interpretation relating DUF480 with actin protrusions and with gene expression separate fromPRC1.6 is hard to follow and sparsely supported.

6. Contrary to what is stated in the manuscript, to my eye MAX is reduced in LOU-NH-91.

7. The KP mouse models are driven by activated RAS called RASV12G but not MYC. Is MYC amplified in these models? I was struck by the finding in Figure 5 and comment that whether MGA is present or not, MYC will drive tumor growth. Some lung adenocarcinomas acquire MYC amplification. Do the human lines used in the experiments have MYC amplified?

It is unclear to me whether MAG loss and MYC amplification are mutually exclusive or correlated? The authors should comment as to whether MGA is required or not in MYC amplified tumors.

8. Does MGA-MAX compete with MYC-MAX to bind the E boxes, and if so, would enforced expression of MYC in the tumors reverse the phenotype? It would be good for the authors to define MAG as the MAX-Gene associated protein.

9. While the title states that "Loss of MGA mediated polycomb repression..", I would add atypical or non-canonical polycomb to the title to distinguish is from the other better known PCR2 and PCR1 complexes.

10. The authors use PRC1.6 rather than PCFG6-PRC1 used by Llabata. The authors should make sure in the text that is refers to the same complex.

11. Figure 4 panels 4B and 4, MGA antibody shows multiple bands. A cleaner blot will help. Is MGA expressed as spliced variants or is the antibody dirty?

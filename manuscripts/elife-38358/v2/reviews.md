# Peer review - Round 1

Editors:
- Aleksandra M Walczak, École Normale Supérieure France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38358.042](https://doi.org/10.7554/eLife.38358.042)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Human T cell receptor occurrence patterns encode immune history, genetic background, and receptor specificity" for consideration by eLife. Your article has been reviewed by Arup Chakraborty as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Yuval Elhanati (Reviewer #1); Bram Gerritsen (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper develops a statistical framework to study the links between TCR co-occurrence patterns, HLA-association strength, and TCR sequence similarity based on the previously published dataset of Emerson et al., 2017. This is an advanced analysis that goes beyond simple V-D-J rearrangement statistics, corrects for baselines and identifies correlations between HLA type and TCR motifs.

The reviewers and the editor agree that the paper develops a statistically sound framework, which leads to interesting insights. However, the reviewers raised a number of comments that must be addressed before publication. Specifically, the experts in the field found the paper difficult to read and often unclear. The combination of previously known results and facts and new results make it hard to capture the main finding and the main new results of the study. The authors should also discuss potential biases that may influence their result.

Essential revisions:

1) A significant concern with the paper is related to readability. Especially for the non-expert, the paper is heavy with specific terms and acronyms and are difficult to follow. And even to researchers in the field, the long paragraphs detailing the analysis are hard to parse.

I suggest to try and break down the analysis more, and using some more clear definitions in the main text. Especially useful might be a cartoon or chart, displaying the connection between the occurrence matrix M, the HLA alleles and the clustering analysis. It will be very helpful to "see" the main connections used in the paper such as P_{CO}, P_{HLA} and the clusters.

It's also hard to follow the different stages of the analysis with similar names, such as HLA-associated TCRs and HLA restricted clustering. Maybe this can be better explained in the outline.

2) The bulk of the analysis focused on a small fraction (about 1:1000) strongly HLA-associated TCRs found. That only few TCRs ended up in clusters might be due to the strict selection criteria (FWER 0.05, DBSCAN parameters) and/or limitations of the dataset, such as unsorted cells, lacking an α chain, and insufficient sequencing depth. Might many TCRs be missed because different HLA-alleles may display the same antigen (weakening the HLA-association)? Given how restrictive HLA-association seems to be, causing many expanded TCRs to be missed, it might be interesting to cluster on expansion index (I_exp) and co-occurrence. This way more of the TCRs in the dataset could be informative for immune history.

3) Several critical factors, such as the extent of the influence of common pathogen exposure on the observed HLA-mediated alterations of the TCR repertoire and a complete lack of TCRα sequencing data, can bias the results and require re-considering the set of conclusions reported. The presence of both HLA and common pathogen (CMV in the latter case) imprinting was previously reported with exactly the same dataset in Emerson et al., 2017. The authors focus their study on HLA-restricted TCRs, obtaining results that follow in an obvious way from the Emerson et al. study. For example, it has been clear for some time by sorting and sequencing antigen-specific populations that MHC restriction is detrimental in obtaining specific TCRs from a given donor. Moreover, the association between MHC alleles and TCR sequences was previously described in Sharon et al., 2016. The authors should update their manuscript to make clear the novel findings of their study and separate them from miscellaneous observations and replications of previous results.

4) The authors use unsorted T-cells, so one would expect that the most evident process that shapes TCR repertoires is the HLA restriction of response to common pathogens. For examples, almost 95% of population is positive for the Epstein-Barr virus, meaning that a trace of EBV epitopes restricted to MHCI and MHCII alleles will dominate across the observed repertoire. If a donor doesn't have an HLA allele to present a given epitope there will be no corresponding clonal expansion. Less studied (and thus more interesting) aspects of the TCR repertoire formation, such as thymic selection in the context of specific HLAs and the influence of individual V/J allelic variants, are not covered.

5) Grouping TCRs by associated pathogens is misleading in the context of the analysis of HLA-restricted repertoires. In case two epitopes are presented by the same HLA and come from different species it is more reasonable to group TCRs by them, rather than group TCRs specific to a pair of epitopes presented by distinct HLAs and coming from the same species. Authors should be more precise when annotating the set of TCRs in case they analyze the effects of MHC restriction.

6) The authors do not consider TCRα chain sequences for most of their analysis. However, they may be detrimental for explaining MHC restriction effects in a large number of settings, for example:

- Recent studies such as Culshaw et al., 2017 and Cole et al., 2009 show a substantial germline bias coming from Vα segment usage patterns in antigen-specific responses that allow a large set of TCRβ sequences.

- The inference of MAIT TCR clusters is trivial given TCRα sequencing data.

- Authors report on TCRs that show no MHC association and state that "TCRs with HLA promiscuity may be especially interesting from a diagnostic perspective, since their phenotype associations may be more robust to differences in genetic background.". These TCRs may be strongly associated with MHC via their α chain.

The authors should show, based on available datasets (e.g. PairSEQ by Howie et al., and single-cell data), that their findings hold when considering the pairing of TCRβ chain sequences with several potential TCRα chain sequences.

7) The authors also ignore the fact that they operate with populations that were not sorted for CD4/8 markers. In fact, in current setting authors cannot show that a given TCR that is found to be associated with a given MHCI/II allele originates from either T-killer or T-helper cells. Authors should estimate (e.g. by comparing their associated sequences with known CD8/CD4 variants) how many of their MHC-associated TCRs are misattributed to wrong MHC class. The authors only find a significant association with MHC class II β chain position 70. Given the fact that they've checked various MHC class I and MHC class II α positions, will the significance hold when applying multiple testing correction? Otherwise, the result may be less general than the results reported by Sharon et al., 2016 and expected to be encountered by chance given the number of tested MHC residues.

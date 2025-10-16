# Peer review - Round 1

Editors:
- Caroline Colijn, https://ror.org/0213rcc28 Simon Fraser University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82538.sa0](https://doi.org/10.7554/eLife.82538.sa0)

This paper is a comprehensive, quantitative, and robust overview of the global, European, and French genomic epidemiology of SARS-CoV-2 in the first year of the pandemic. It contributes methodological advances in maximum likelihood phylogeography, using multiple scales and providing a simulation-based validation. The results show two distinct patterns of SARS-CoV-2 exchange events between the first and second half of 2020, with Europe being involved in most intercontinental exchanges: France experienced viral introductions primarily from North America and Europe during the first wave, while the second wave saw limited intercontinental movement and a significant contribution of the virus from Russia into Europe.


---

# Peer review - Round 1

Editors:
- Caroline Colijn, https://ror.org/0213rcc28 Simon Fraser University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82538.sa1](https://doi.org/10.7554/eLife.82538.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Phylodynamics of SARS-CoV-2 transmissions in France, Europe and the world during 2020" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Christopher JR Illingworth (Reviewer #1); Angela McLaughlin (Reviewer #3).

As is customary in eLife, the reviewers have discussed their critiques with one another. What follows below is the Reviewing Editor's edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision clearly marked in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Essential revisions:

Both reviewers and the Editor think that this is an important study that presents interesting findings about the spread of SARS-CoV-2 in France and in Europe, and are positive about the work's eventual publication. However, the reviewers brought up important considerations, including methodological concerns, that need to be addressed in a revised version. Following the consultation with the editor and reviewers, we would welcome a revised version that addresses the substantial methodological comments. In summary:

(1) Sampling: there are two questions. One is about the number of sequences and the number of deaths (both reviewers commented on this), as opposed to the number of infections; whether the correlation (sequences to deaths) is an artefact of the method used (Rev 1) and whether it validates the analysis (Rev2). In addition, since deaths and infections can be reported differently in different places, what is the impact of having different sampling fractions in different geographies? this could be addressed by looking at the robustness of the inferences to different choices of relative numbers of sequences from different regions

(2) Downsampling to < 1000 sequences, bootstrapping and adding: We were all concerned about the small individual datasets and the assumption that adding the results would generate the correct numbers of viral movements. After all, why this number of replicates – why not add after 5000 or 800 or some other number of replicates? Also, there are some instances where the same introduction event would be detected in many replicates, and somewhere it would be missed in most of them, so it's not clear that it's additive. Other authors have averaged, in similar analyses (but since each replicate might miss some events, averaging might not be). Given that this analytical method has the advantage that much larger numbers of sequences are tractable to analyze, the authors should analyze substantially larger datasets.

(3) The fast clock assumption has the potential to bias the analysis; a number of other related methodological issues were raised by reviewers. These should be addressed.

(4) Quantitative descriptions of the results and their variability should be included in the results (for example, the importation rate). This will aid in articulating the public health interpretation and relevance, which reviewers also note would add interest and weight to the paper.

Reviewer #1 (Recommendations for the authors):

The method is described as 'original' but line 377 implies that the same method was used to study data from Canada. Please clarify what is new about the approach used here relative to previous studies.

It is stated in line 65 that existing phylogenetic tools cannot include the large datasets generated by projects such as the international COVID sequencing effort. However, researchers on the COG-UK project generated a tree of sequences comprising hundreds of thousands, if not millions of sequences (https://www.cogconsortium.uk/priority-areas/data-linkage-analysis/public-data-analysis/). It would be helpful to clarify what can and cannot be achieved with which phylogenetic methods.

The positive correlations observed between the number of deaths and the number of sequences in a dataset (Figure 2) is a reassuring check but seems to be a direct artefact of the methods, whereby the number of deaths was used to determine the number of sequences. I suggest including these plots in supplemental material.

I would value more explicit information in the Methods section about how data from the inferences performed on different bootstrapped samples was combined.

The link to the stated GitHub repository did not work at the time I tried it.

Reviewer #2 (Recommendations for the authors):

L97: Figure comments: It is recommended to add an annotation for the date delineation of the two COVID waves analyzed in the main graphic. The legend should report how reproduction rate was calculated, and this should be clearly described in the methods. Relatedly, L447-448: state exact dates instead of 'mid' and 'late' months. Applies in results as well.

L106: Although the authors say that sequences are representative of 'sars-cov-2 infections', they then describe the comparison to deaths. Did the authors also compare case incidence to deaths and separately, to sequences over time? Need to better justify the use of deaths rather than new diagnoses. It would help the reader if there was also a presentation of cases over time in addition to deaths that could be done for example in Figure 1.

L114;L124;L209;L287,L465: Regarding the discarding of sequences from geographies that were underrepresented in the sequence set – how would the results be expected to change if these geographies were not discarded? They would be perhaps less likely to be sampled as well as represented in the ancestral nodes due to low representation, but they might have indicated additional nuances to the French regional transmission patterns.

Also, in the methods, what was the threshold by which the authors decided if a region was too underrepresented to be included? L404: what percent of cases and/or deaths were associated with the administrative regions that were excluded due to low or no sequences in each wave?

L115: Need to clarify how many sequences per phylogeny in the results. Were sequences sampled by geography randomly or proportionally to the relative number of deaths over time? Were the sampled sequences distributed uniformly over time or proportionally to deaths over time? Were sequences sampled entirely at random?

L133: Were sequences masked for problematic sites, i.e. due to homoplasy and likely sequencing errors, as identified by Nicola de Maio and group, prior to the phylogenetic inference? This is important and standard in these analyses; if the authors performed masking of problematic sites it is important to mention in the methods. If masking of problematic cites was not performed then this should be done and the analyses repeated during revision.

L156: why is the analysis delineated into periods in mid-July when the authors state here that the second European wave started in October? The delineation of epidemic waves and studied periods needs to be clarified and justified.

L161-165; L237-240; 374-376: the positive correlation between intra-territory transmission events and the estimated number of deaths does not convincingly validate the method, because this is what would be expected even in the presence of remaining bias. Why not total transmission in relation to deaths? Lastly, the authors have shown deaths are also associated with sequences, therefore this does not distinguish model accuracy from reflecting the relative inclusion of sequences.

L378: McLaughlin et al. 2022 used maximum likelihood ancestral reconstruction, but did not sum across replicates; rather, they averaged across replicates. Also, it would be good to include a couple other references as well that a similar approach, as well as the origins of the method algorithms (Pupko et al., 2000, Cunningham et al., 1998)

There are multiple instances in the Results section where relative flows are discussed for different geographies or over time, but only in a qualitative rather than qualitative manner. Please quantify rate estimates and/or relative changes/differences (as the authors did on L296 and L321) in other places. L186: 'at similar rates'. L192: 'quite similar'. L225: 'sequentially – and drastically – increased…'. L233: 'drastic'. L245: 'drastic'. L266: 'steep increase'. L268: 'sharp increase'. L294 'much more'. L308: 'a bit lower'.

L279: it is speculative that government measures had varying success rates based on the analyses conducted and presented in this manuscript.

L275; and generally: The manuscript would benefit from more discussion or stratification of which Pango lineages or Nextstrain clades dominated particular transmission types and routes in the two waves.

L299: Normally, Spearman rank correlation can be appropriately performed when there are 10 or more observations, here, as written the correlation has been performed with only three measurements – please clarify or rectify this.

L430; Supplementary: The GISAID identifiers should be a separate appendix and the authors need to follow the GISAID recommendations for inclusion of a table acknowledging labs for each sequence.

L443-446: What is missed by not conducting all three analyses together? How much international origin among a given region in France, for example?

L470: The inclusion of earlier diversity from the first wave in the trees for the second wave is laudable, however, how did the authors ignore transmission events involving those context sequences when analyzing the second wave in terms of intra- vs inter-territory transmission? Precisely how this was done needs to be clarified in the manuscript.

L480: How were trees rooted? This is an important omission and should be clearly specified in methods.

L483: how could the use of a strict clock rate have impacted the results? Employing model selection and describing in methods to justify would be valuable. If the authors have already performed model selection then clear description in the results is warranted.

L486: in regards to Figure 6-Figure supp 1 on estimating versus fixing the clock rate, the authors should move some of the text in the legend into the main results to better explain why the authors fixed a strict clock rate. Also, the reader may wonder to what extent the issue encountered with early node dating and long branches might have been related to specifying a strict instead of relaxed clock. Thus, please elaborate on this in the results.

Generally in the figure supplement legends, any interpretations of the plots should be moved into the Results section.

It would be informative to contextualize the authors' results within the literature available to date by having a more thorough comparison to other papers on the genomic epidemiology of SARS-CoV-2 in Europe in the Background and/or Discussion; for example, Worobey 2021, Hodcroft 2021, and Huisman et al. 2022.

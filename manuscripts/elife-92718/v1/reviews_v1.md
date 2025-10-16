# Peer review - Round 1

Editors:
- Daron Standley, https://ror.org/035t8zc32 Osaka University Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.92718.sa0](https://doi.org/10.7554/eLife.92718.sa0)

This study provides an important systems analysis of antibody repertoires across multiple lymphoid organs, demonstrating significant clonal overlap following repeated immunizations. The findings show that strong humoral responses lead to a high degree of repertoire consolidation, correlating with antigen specificity and B-cell migration between organs. The evidence is convincing, with deep sequencing and network analyses strongly supporting the conclusions.


---

# Peer review - Round 1

Editors:
- Daron Standley, https://ror.org/035t8zc32 Osaka University Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.92718.sa1](https://doi.org/10.7554/eLife.92718.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "The physiological landscape and specificity of antibody repertoires is consolidated by multiple immunizations" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Betty Diamond as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Tomoharu Yasuda (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions (for the authors):

Considering that many biologists are supposed to be interested in this manuscript, authors should try to make the manuscript more easily be understood by the readers. From this points, reviewer request two types of revision. First, bioinformatics analysis should be tried to be more easily understood for readers. Second, authors should discuss the several important points raised by the current analysis.

Reviewers describe requests (in the recommendations for the authors).

In regard to the first point, additional comments of (1), (2) of the reviewer 1, comments (1), (4), (7), (8) of the reviewer 2, and comment (2) of the reviewer 3 should be carefully revised.

In regard to the discussion points, authors should discuss comments (3), (5), (6), and (9) of the reviewer 2, and comments (1) and (4) of the reviewer 3.

Reviewer #1 (Recommendations for the authors):

In this study, the authors did in-depth systems analysis of IgG antibody repertoire in immunized mice, and beautifully demonstrated that a limited number of shared clones become dominant in multiple lymphoid organs. However, clonal expansion of antigen-specific memory B cells by multiple immunization, and migration of memory B cells and plasmablasts from one lymphoid tissue to others are known. Extent of clonal expansion of shared clones may depend on immunization protocols that may affect distribution of the antigen to multiple lymphoid organs as the authors discussed. Therefore, the conclusion of this study may not be generalized without testing other immunization protocols.

In this study, the authors showed expansion of overlapping clones across multiple lymphoid organs after repeated immunization. The authors raised distribution of antigens to multiple lymphoid organs and migration of antigen-activated B cells as possible mechanisms for generation of overlapping clones.

It is known that memory B cells are present in circulation as well as various lymphoid organs and home to lymph nodes, and expand by immunization. These previous findings showed migration of memory B cells to different lymphoid organs and their clonal expansion after multiple immunization. Plasmablasts are also known to migrate from spleen and lymph nodes to bone marrow. Therefore, presence of overlapping clones in multiple different lymphoid organs may not be surprising. Although the authors claim a surprisingly high degree of repertoire consolidation, characterized by highly connected and overlapping B-cell clones across multiple lymphoid organs after repeated immunization, extent of clonal expansion may depend on immunization protocols. Overall, it is not so clear what is the novel findings in this study, and whether the findings of this study can be applicable to vaccination in human.

Additional comments

(1) This study generally lacks statistical analyses. Statistical analyses are required when the authors compare two samples and describe that one is lower or higher than the other.

(2) Some figures are similar but different, and how and why they are different are not clearly indicated. Examples are Figure 3c and Supplemental Figure 4b.

Reviewer #2 (Recommendations for the authors):

By examining the post-vaccination BCR repertoires in specific lymphoid organs, Csepregi and coworkers provide a fresh look a migration patterns of specific B cell clones. They attempt to convey a vast amount of information through various statistical metrics and data visualization methods developed for repertoire analysis. While this analysis may be a bit heavy and, perhaps even overwhelming, the experimental demonstration that antigen specificity correlates with inter-organ migration convincingly justifies their analysis methods. While the internal consistency of the wet and dry data was impressive, there appears to be room for drawing upon previous work in the literature.

• Summary of what the authors were trying to achieve

This work contains an in-depth analysis of BCR repertoires at the level of multiple lymphoid organs upon vaccination. The results are primarily comprised of bulk sequence analysis, but a single cell sequence dataset is also presented. Moreover, yeast display is used to select antigen binders, and a strong correlation between antigen specificity and inter-organ sharing is observed.

• Major strengths and weaknesses of the methods and results

The main strength was the connection between the first part of the paper (repertoire sharing across organs) and the second part (antigen specificity).

Weaknesses: The bioinformatics analysis is very detailed and took a while to digest. Some of the graphs seemed overly complex for what is actually a pretty intuitive set of results.

• An appraisal of whether the authors achieved their aims, and whether the results support their conclusions

I think that, with the inclusion of the antigen specificity, the authors met or exceeded their aims.

• Likely impact of the work on the field, and the utility of the methods and data to the community

This approach should work for other mouse studies. The antigen specificity aspect may work for human antibody discovery using PBMCs. If sampling is an issue, perhaps pooling of different vaccinated donors' sequence data can be used.

• Any additional context you think would help readers interpret or understand the significance of the work

The data visualization is challenging and probably could use a tutorial. This was my only serious criticism of the work-that I spent a lot of time trying to understand the bioinformatics figures.

I appreciate the novelty and significance of this work, and my impression is overall quite positive. The main area where I see room for improvement is in the descriptions of the bioinformatics analysis. My reading slowed down a lot as I tried to digest some of the figures. It would be nice if the reader could grasp the point of these figures without struggling to understand what is being plotted.

1. Diversity and organ size. You mention that lymph nodes are less diverse but also smaller than the other organs. Since you show, further down in the paragraph, that not only the raw numbers but also the distribution of clone size is skewed toward dominant clones in the LN, it might be helpful to explicitly state that the observed diversity in LN can not explained by their smaller size.

2. Figure 1d. After I worked out what the colors meant, the figure was quite clear. There is a lot going on in the figure: clones are ranked by size, and then binned as noted in the legend, and then the population, as a proportion is plotted. Some explanation to this effect rather than jargon like "repertoire space" or "repertoire polarization" would have helped me a lot.

3. In figure 1e, the difference between 1x (left) and 3x (right) is striking. You refer to this phenomenon as "physiological consolidation". One interpretation is that migration has simply mixed the B cells within the 3x mice creating a more homogeneous repertoire across organs within given mouse than in the 1x cohort. But why do the spleen and BM cluster together in the 1x cohort? Is it correct that this similarity in 1x BM/spleen is not due CDRH3 but to CDR1-2/framework?

4. In figure 2, I found the pie charts to be a little confusing. The colors did not make sense to me. The largest 1x-B aLN-L cluster is mostly orange, which, according to the legend, means "spleen" and "BM". Is the fact that the "aLN-L" color (light blue) does not appear in the pie chart due to there being only 1 or a few aLN-L sequences?

5. Figure 2 is yet another unfamiliar (to me) way of representing data that slowed me down. For example, I could not understand why you say: "in cohort-3x mice clones were frequently shared across lymphoid organs, particularly the lymph nodes (Figure 3a)." Does "frequently shared" refer to the line thickness?

6. You observed "we found that lineage trees of all cohort-3x mice had a significantly higher proportion of transitions both from spleen to bone marrow, and from bone marrow to spleen". It would be helpful from a reader's perspective to put this and other similar observations into context of prior literature. Is this expected? Surprising?

7. In Figure 4, it was hard to distinguish between blue/green colors

8. In Figure 5d, it appeared as if some of the CDRH3 sequences with a given mouse were quite similar. I'm curious as to whether there was convergence across mice. If you compute the clonotype overlap between two mice and then quantified this overlap overall (as a fraction of all clonotypes) and as a fraction of all binders, do you see that the binders overlap more?

9. Could you comment on the extent to which the paired BCR CDRH3 repertoire overlaps with the bulk data? I'm wondering how many of the binders were observed in the 10x dataset.

Reviewer #3 (Recommendations for the authors):

Performing the systemic profiling of antibody repertoires across multiple organs within the same individual is important to understand how immune response is regulated to fight against pathogens. In the manuscript entitled "The physiological landscape and specificity of antibody repertoire is consolidated by multiple immunizations", the authors tried to analyze antibody clonality and dynamics upon RS virus antigen immunization to mice by comparing between early time point, 1x immunization, and later time point, 3x immunization. I understood a major finding of this study is a repertoire consolidation across organs after multiple immunizations. Such phenomenon was explained by clonal migration across multiple lymphoid organs, which is directly correlated with antigen specificity. It is interesting and seems important findings contribute to progress in the research field.

The following points should be addressed or improved:

1. p4, Figure 1b, and c; Values of "Unique clones per organs" and "Unique clones per mouse" maybe both mislead readers. Unique clones per organ in Figure 1b is probably not the number per organ. Is not it just counts per input of the arbitrary number of templates from each organ? In addition, how authors were able to calculate unique clones per mouse in 1c? Please clarify the process and reason for calculated values for the accuracy of data.

2. p5, line 144-149; Figure 1d, For the analysis of clonal expansion, authors show clonal frequency rank in which profiles of LN or SP/BM are oppositely changed. However, it makes me hard to interpret data because of the missing unimmunized mouse organ profile. Authors should provide the clonal proportion of unimmunized ones to judge where the baseline is, otherwise, the conclusion here can be speculative.

3. p33 Supplementary Figure 2a; This is not kind for general readers to understand what really figure means. What do Evenness values and α values mean? How should we interpret data to understand the difference between cohort-1x and cohort-3x?

4. Figure 4a and supplementary Figure 2C; Authors described in the method section that Balb/c mice were used in the study. In contrast to C57BL/6 strain, immunoglobulin genes of Balb/c strain have not been well-sequenced, and therefore the database is not completed. Roughly 40% of Ig genomic region is still missing. In IMGT database, many of Balb/c IGHV sequences are not or partially identified. Are authors really sure that SHM was counted on Balb/c reference sequences, not on B6 or other strain? Otherwise, counts and data will be wrong.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The physiological landscape and specificity of antibody repertoires is consolidated by multiple immunizations" for further consideration by eLife. Your revised article has been evaluated by Betty Diamond (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

The strength of this study is a systems-based approach that included deep and single-cell sequencing, bioinformatic and statistical analysis, and high-throughput antibody specificity screening to comprehensively profile antibody repertoires from six distinct lymphoid organs. The weakness of this study is that it does not consider the binding properties of major BCR clones, such as affinity for antigen, or the clonal selection of B cells that are broadly reactive to diverse viral variants.

1. The authors properly addressed my concerns by adding untreated mouse profiles, descriptions, figure legend, and updating the analysis based on recently published reference data that strengthened the conclusion of this study and is beneficial for readers.

2. For Figure 1b, "Unique clones per organ" in the y-axis is misleading. I recommend changing the axis such as "Number of unique clones per 135,000 IgG cDNAs".

3. For Figure 1c, "Unique clones per mouse" in the y-axis is misleading. I recommend changing the axis such as "Number of unique clones from 6 organs".

Reviewer #3 (Recommendations for the authors):

In this study, the authors did in-depth systems analysis of IgG antibody repertoire in immunized mice, and demonstrated that a limited number of shared clones become dominant in multiple lymphoid organs. Although migration of memory B cells is known, the authors beautifully demonstrate consolidation of the antibody repertoire across different lymphoid organs by multiple immunization. Because the changes in antibody repertoire by immunization may depend on immunization protocols, it is not yet clear whether the findings in this study can be generalized.

In the point-to-point response to the concern of this reviewer on the novelty of the study, the authors listed several findings described in this manuscript as novelty, and mentioned that they edited the manuscript accordingly. However, the introduction and Discussion sections are not much changed. Could the authors make it clear how they edited the manuscript accordingly?

The authors did statistical analyses in some of the data. However, the analyses in Figure 1b, Supplementary Figure 1C, Supplementary Figure 2b and Supplementary Figure 4b are not appropriate. There are more than three data (bars) in each figure, and the authors discuss the comparison of more than three data in the result section. Therefore, the authors should have analyzed the data by multiple comparison test.

# Peer review - Round 1

Editors:
- Joris Deelen, https://ror.org/04xx1tc24 Max Planck Institute for Biology of Ageing Cologne Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73420.sa0](https://doi.org/10.7554/eLife.73420.sa0)

This paper presents a new DNA methylation-based biomarker of aging: DunedinPACE. This biomarker is an updated version of DunedinPOAM, which was designed by the same group of authors to track an individual's Pace of Aging. It takes into account an additional measurement occasion (collected 20 years after inclusion) and only includes the most reliable DNA methylation probes, i.e. probes with little variation between technical replicates. DunedinPACE shows improved performance when compared to DunedinPOAM and can be used to complement previously generated DNA methylation-based biomarkers, such as GrimAge.


---

# Peer review - Round 1

Editors:
- Joris Deelen, https://ror.org/04xx1tc24 Max Planck Institute for Biology of Ageing Cologne Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73420.sa1](https://doi.org/10.7554/eLife.73420.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Quantification of the pace of biological aging in humans through a blood test: the DunedinPACE DNA methylation algorithm" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Joris Deelen as the Reviewing Editor and Reviewer #3, and the evaluation has been overseen by Jessica Tyler as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Matthew Suderman (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The reviewers all agree that it is unclear what the added value of DunedinPACE is over the previously generated DundinPOAM and, even more, the widely used GrimAge methylation biomarkers. This should be discussed more thoroughly and will require some additional analyses (see individual review reports).

2. The discussion between the reviewers also brought forward that the work by Levine and colleagues (doi: https://doi.org/10.1101/2021.04.16.440205), although shortly mentioned in the introduction, has not sufficiently been taken into account by the authors. This preprint has several implications for the current manuscript. First, the currently used methylation biomarkers, including GrimAge, will soon be updated using the correction proposed by Levine et al. and will outperform the versions used in the current manuscript. Thus, the iterative improvement in DunedinPACE vs DunedinPoAm may be the only relevant comparison. Second, the current manuscript uses test-retest of individual CpG probes to refine DunedinPACE. However Levine et al. show strong evidence that this strategy may improve performance for a single clock (e.g. better performance in DunedinPoAM to DunedinPACE) but that this may not generalize to other clocks. Rather, technical variability was best improved by PCA to extract a 'shared signal' vs individual CpGs. At minimum, the authors should consider various approaches to reduce technical reliability rather than focus solely on individual CpGs, including creating a methylation biomarker using principal components.

The authors should also address the additional points mentioned in the individual review reports below.

Reviewer #1:

This study details development of an improved iteration of a DNA methylation biomarker based on Pace of Aging measures developed in healthy, primarily Caucasian adults up to age 45 years in the highly unique longitudinal Dunedin Study. The new methylation biomarker is DunedinPACE; the predecessor DunedinPoAm was reported in Belsky et al. 2020 eLife 9,354870.

Strengths

The key contribution of this study is to address limitations in previous methylation biomarkers: (1) Pace of Aging measures now encompass a 20-year time span vs 12 years in Dunedin study; (2) training population includes adults up to 45 years (vs 38 years); and (3) methylation model is restricted only to probes that meet a minimum threshold for test re-test reliability.

1. DunedinPACE has good test-retest reliability, which is highly relevant to biomarker performance in clinical studies and interventions testing.

2. Not unexpectedly, the test-retest reliability is stronger for the new DunedinPACE vs. earlier DunedinPoAm, possibly owing to introduction of minimum probe reliability thresholds, though this is not explicitly tested.

3. The analyses presented generally follow established tests of criterion and construct validity across a set of cohort studies previously used to develop its predecessor DundedinPoAm (see Belsky et al. 2020 eLife 9,354870). The parallel strategy makes the seemingly complex set of validation studies a relatively straightforward comparison across biomarker iterations.

4. The effect sizes in cross-cohort validation analyses are larger for DunedinPACE relative to the foundational DunedinPoAm, and the effect sizes meet (GrimAge) or surpass effect sizes for other existing DNAm biomarkers. This supports strength of the new PACE biomarker iteration relative to most others.

5. Conclusions are generally well supported by data and authors refrain from extraneous discussion.

Weaknesses

1. Though several key limitations in DunedinPACE's predecessors were addressed, it is unfortunate that readers are not provided details regarding their relative contributions to overall biomarker performance.

2. It would be highly informative for future biomarker development to know if and to what extent population characteristics (cohort, age, or duration of observations for Pace of Aging measure) drive improved performance of DunedinPACE vs. DunedinPoAm relative to test-retest reliability or duration of longitudinal observation.

3. DunedinPACE performed similarly (reported effect sizes) to GrimAge, yet this equivalence is not addressed in discussion or conclusion. It is unclear under which conditions should one biomarker be prioritized over another if effect sizes are similar.

4. Forced language regarding DunedinPACE as a proxy for Pace of Aging muddles results presentation and section headings; this may inadvertently misrepresent select analyses.

5. Remaining concerns and suggestions are to improve readability, clarify nomenclature, and strengthen presentation of results, and do not influence primary conclusions or implications.

Title:

6. The title is regurgitated from the eLife 2020 publication but with a modification after the colon. This tedious for query building, search engines, and reference lists. The authors should thus consider adapting it.

Contribution of individual iterative changes:

7. To address individual contributions of each of the prior limitations, the authors could consider supporting analyses to address:

• Ddoes the inclusion of persons who are 45 years and now exhibiting detectable declines in health / function improve performance of the methylation biomarker, or is the time span (12 vs 20 years) the key determinant for calibration for improved performance?

– Potential approach: restrict model to population aged 32-45 years (~12 years, but older) and compare performance to current DunedinPACE and previous DunedinPoAm.

• Is minimum reliability threshold the key to improved performance or characteristics of the population used to calibrate the methylation biomarker?

– Potential approach: (a) revisit DunedinPoAm – restrict the existing biomarker to probes meeting reliability threshold, or (b) release test-retest reliability restrictions for probes included in DunedinPACE and evaluate.

Implications:

8. DunedinPACE is an iterative change to DunedinPoAm; clearly showing how each of these changes impact the resultant model bolsters significance.

9. DunedinPACE is tested head-to-head with previous derivations of DNAm clocks, but without insight regarding if or how changes leading to DunedinPACE could be introduced to rebuild better a GrimAge, PhenoAge, etc.

10. If primary determinant of improved performance is including aged >45 years, what does this mean for generalizability of clocks tuned in young/healthy population to trials in older adults or those in poorer health.

11. If analyses show that duration of longitudinal observation is key (20 years vs 12 years), then would future Dunedin derivations be expected to consistently outperform the previous versions and what would this mean for durability of the DunedinPACE as a biomarker?

GrimAge:

12. Addressing GrimAge vs DunedinPACE similarity in effect sizes may require some speculation, but would aid reader interpretation of results and could be simply handled with a short sentence or two in discussion.

Language – DunedinPACE as Pace of Aging Proxy:

13. Language referring to DunedinPACE and Pace of Aging is sometimes confusing, which could be attributed to the forced representation of DunedinPACE as a proxy for Pace of Aging.

• This results in instances of merged language (pg 12 "DunedinPACE Pace of Aging").

• The Results section and headings also suffer from forced association (marketing over reporting findings?). Examples:

– (Results pg 9) "DunedinPACE is indicates faster Pace of Aging in Chronologically Older Individuals." Results in text and Figure 3A show association with chronological age.

– (Results pg 10) "DunedinPACE shows faster Pace of Aging in individuals measured to be…" Forcing reference to Pace of Aging makes the heading cumbersome ("DunedinPACE is associated with other epigenetic clocks, measures of biologic age, and self-rated health").

– Authors are recommended to use simplicity and clarity throughout results and save comment about DunedinPACE as possible a proxy for Pace of Aging for the discussion.

Results, Text and Figure 3 Alignment:

– Page 9-10. "DunedinPACE indicates faster Pace of Aging in Chronologically Older.."

– The text opens with a sentences about mortality risk, but the only figure referenced is association with chronological age in Understanding Society study (Figure 3 Panel A). Recommend to omit or move to mortality risk references to Results section on NAS.

– The second paragraph provides information about exposure histories across birth cohorts. These results distract from the flow of results reporting in Figure 3 and subsequent section. While within-individual change may be supportive they are not essential and detract from readability.

For consideration (not mandatory): Naming Conventions

14. One improvement of DunedinPACE is the name; it is much easier to read / say compared with DunedinPoAm. However, would "PACE" or "PACEm" be sufficient? Adding "Dunedin…" seems to suggest that DunedinPACE or DunedinPoAm are specific to the foundational study of origin compared with GrimAge or PhenoAge.

15. "Faster" and "Slower" are used repeatedly to refer to higher vs. lower DunedinPACE (single-timepoint) compared to Pace of Aging (time component included). Using "faster" or "slower" may be appropriate for a Pace-proxy unlike most clocks. But referring to change in single timepoint DunedinPACE as "faster" is confusing, even if it is proposed as a proxy for Pace of Aging

Reviewer #2:

Although the paper is well-written, findings are not presented in a way that allows the reader to answer the most important question of the paper: how does DunedinPACE compare to DunedinPOAM? Little can be concluded from the improved performance in the Dunedin study data from which DunedinPACE and DunedinPOAM were both derived. In independent datasets, performance appears to be almost identical. Test-retest evaluations in the Sugden dataset similarly are difficult to interpret because probe reliability was calculated using the Sugden dataset.

In all evaluations using data used to derive DunedinPACE, authors should clearly state the potential for inflated performance. This is particularly true for comparisons with DundinPOAM which was trained on a subset of DunedinPACE data and previously published aging estimates Horvath/Hannum/Phenoage/Grimage trained entirely on external data.

Reviewer #3:

The manuscript by Belsky and colleagues reports the development of an improved methylation biomarker based on longitudinal health data (Pace of Aging) from the Dunedin Study. The authors have now used an additional wave of measurements and excluded methylation probes with low reliability based on recent publications. They subsequently associated their improved biomarker, which they called DunedinPACE, with many different health-related outcomes, such as physical functioning, morbidity and mortality. They show that DunedinPACE shows comparable results as GrimAge, a methylation biomarker based on mortality.

The major strength of the study is that the authors have managed to improve their previous methylation biomarker (DunedinPoAm) by adding additional data. They also show that DunedinPACE does reasonable well when associated with health-related outcomes. However, it is unclear what the added value of DunedinPACE is in comparison to GrimAge, because it does not outperform this previous biomarker in its association with any of the outcomes. Moreover, the provided data on the most relevant health-related outcomes, i.e. morbidity and mortality, is limited and it is unclear if the methylation biomarker would outperform other omics-based biomarkers (i.e. metabolomics and proteomics).

– The authors should highlight the added value of DunedinPACE in comparison to GrimAge. It looks like they do equally well in the analysis they performed, so what would be the advantage of using DunedinPACE over GrimAge, given that the latter is already widely used.

– The authors should also look at cause-specific mortality and morbidity to see if DunedinPACE reflects general health or is specific to one major disease, e.g. cardiovascular disease.

– The authors should test the predictive ability of DunedinPACE, ideally in comparison to currently used clinical biomarkers and biomarkers based on other omics data (see PMID: 34145379 and PMID: 31431621). If a direct comparison is not possible, the existence of these non-methylation biomarkers should still be mentioned, including their effect sizes for morbidity/mortality (if available).

– The authors should test the association of DunedinPACE with morbidity and mortality in different age-groups (i.e. stratify their data) to make sure the associations are not driven by early-life morbidity and mortality.

– It would be interesting if the authors can provide a biological interpretation (e.g. functional annotation / genetic association analysis) of the CpGs that are included in the DunedinPACE biomarker, as already done for some of the other (methylation-based) biomarkers (see for example PMID: 34187551 and PMID: 34038024).

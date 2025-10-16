# Peer review - Round 1

Editors:
- Bavesh D Kana, https://ror.org/03rp50x72 University of the Witwatersrand South Africa

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79981.sa0](https://doi.org/10.7554/eLife.79981.sa0)

The authors perform a Transposon-Sequencing screen to determine bacterial factors (including receptors) important for infection by two phages in the model bacterium Corynebacterium glutamicum. Using their established high-density transposon library, they identify genes required for infection with the phages Cog and CL31. They also identified a spontaneous phage-resistant mutant that led to the discovery of a gene involved in mycolic acid synthesis. Overall, the work is of broad interest to scientists in the field of cell wall biogenesis, phage infection, and bacterial cell biology.


---

# Peer review - Round 1

Editors:
- Bavesh D Kana, https://ror.org/03rp50x72 University of the Witwatersrand South Africa

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79981.sa1](https://doi.org/10.7554/eLife.79981.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Phage resistance profiling identifies new genes required for biogenesis and modification of the corynebacterial cell envelope" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Bavesh Kana as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: William R Jacobs (Reviewer #1) (co-reviewed by Brianna Weiss); Marc Bramkamp (Reviewer #2); Carol Gross (Reviewer #3) (co-reviewed by Horia Todor).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Although the authors’ experimental design is fundamentally sound, there is the possibility of “jackpotting”, which could affect their results, particularly in the uninfected control experiment. If the authors’ Tn-seq library is ~200,000 strains, and they don’t plate at 10-100x fold access of colonies, then any given strain (regardless of its phenotype) may or may not be represented in the output of the experiment, causing false phenotypes to be ascribed to genes based on chance. This is particularly problematic for the uninfected control, where the authors choose to dilute the culture 1000-fold to mimic the number of colonies that survive infection. They may be better served by plating the whole culture on the plates, to ensure adequate representation of the library. Part of the reason for this concern is that an overwhelming majority of statistically significant hits (something like 80-90%) appear to confer susceptibility rather than resistance (source data Figure 2) – something the authors’ experimental design should not be able to measure. The lack of accurate representation of distributions of strains in the starting culture also calls into question the quantitative differences presented in the results.

a. L138. Where the authors describe their initial experimental design it would be helpful to add more details. What is the size of the Tn library? What is the coverage in their experiment? Approximately how many colonies are recovered on the plates after phage infection and in the uninfected control?

b. It is important to know how the number of colonies on the plates compares to the number of reads in the experiment. In the analysis of most HT screens, one implicitly assumes that each read corresponds to 1 cell, hence each read can be treated as statistically independent. This assumption is critical to the statistical methods used to analyze this data. By scraping a plate of colonies (which may be required for efficient phage infection), the authors potentially violate this assumption (since the number of cells → the number of colonies, are the actual statistically independent entities in the experiment). Does this assumption hold (or approximately hold) for the screen? If not, a different statistical method should be used to determine p-values.

2. The authors’ Tn-seq methodology is different from previously published HT-phage screens (e.g. Mutalik et al., 2020 and Rousset et al., 2018). Whilst it is clear that plating the infected cells has advantages, this rationale will not be clear for most people’performing such experiments. Please explain the rationale for the experimental protocol:

a. Why did the authors plate the cultures after initial phage absorption instead of allowing them to remain in liquid?

b. How reproducible are the authors’ Tn-seq results? The SRA ascension shows multiple replicates but this is not described in the manuscript nor reflected in the supplementary data. Given the potential for bottleneck and jackpotting effects in this assay, some measure of reproducibility is important for interpreting the results (see point 1).

c. L587 “Significant hits with fewer than 10 insertions on each strand were manually removed.” Why did the authors choose this criterion? Almost all of the genes they removed have very asymmetric distributions (e.g. in the Cog experiment, cgp3051 has 47853 fwd reads and 6 rev reads). Asymmetric distribution of insertions suggests that overexpression of downstream genes has an important (positive or negative) effect. This is a worthwhile pursuit, and many automated analysis pipelines can disambiguate these effects, including those developed in the Walker Lab (e.g. doi: 10.1038/s41589-018-0041-4). These genes shouldn’t be thrown away when they are arguably some of the most informative hits!

3. There is a somewhat extensive phylogeny of M. smegmatis phages (phagesdb.org). Are the phages that the authors work on related to any of these phages? If so, what cluster do they map to? What is the host range of other phages in that cluster? If not, may be worthwhile to mention that these are quite distinct from other studied phages.

4. Given that cgp_0475 was a strong hit in the Tn-seq, why was it not identified in the previous chemical genomics experiments from the lab (https://doi.org/10.7554/eLife.54761)?

5. Is there any relationship between the growth rate of the mutants and their phage susceptibility? This can be analyzed using the authors’ previous studies of this library.

6. The information on the localization of AhfA is sparse. In the discussion the authors speculate about a cytosolic localization, however, this is not proven.

7. In general, there were no p values relating to the statistical significance of any of the data presented, please address this (also highlighted in minor points below)

8. Figure 8 was not entirely supported by the data, especially Figure 8A which either could be improved with better images that support the claims.

Reviewer #1 (Recommendations for the authors):

– In Figure 1: the figure legend for section D, the phage adsorption assay, is mislabeled.

– Based on how Figures 1B and 1C are written, it would make more sense to switch these two figures in the final print.

– In the text explanation of Figure 4D, I would put (ECOI) after “Efficiency by which Cog formed centers of infection..” as it would make quick understanding of the Y axis of figure 4D easier.

– For figures 6C and D, I would quantify the percentage differences in phage adsorption between wild-type and knockout Cglu cells.

– Figure 8 could be strengthened with a better figure design, or images for 8A, as it did not entirely support the claims the authors made.

– In Figure 8: the figure legend for Figure 8C, TLC analysis of lipids.. is mislabeled and should say C, not D.

– What is the reason for using Cog and CL31 specifically beyond the fact that they infect Cglu?

– Line 79 should read “reversible”.

– Line 123 should read “possibly due to its role”.

– Line 124 should read “Sanger sequencing”.

– Line 125 should read “gene in the altered plaque”.

– Line 362 should read “reveal phage receptors”.

– Line 380 should read “ infection suggests that”.

– The SNPs in clg55 of the CP CL31s, are those the main differences you see in the CP CL31s vs wt? Anything else it could be?

– The CP CL31 with the clg55 SNPs is separate from the lab-adapted CL31 which shows similar plaque heterogeneity if I’m reading this right and the cause of the heterogeneity in the lab-adapted strain was not looked into. Why not look for those or similar SNPs?

– Do you know what about Cog and CL31 is different that would necessitate these different pathways? Obviously, they seem to bind different receptors, anything else? This may be out of the scope of your work, but I think knowing the phage differences that relate to different ways of exploiting the bacteria could be helpful in creating ways through the envelope.

– I mentioned these in public feedback but I’d like to see you address any changes in the lab strain (if you think there are any) that may have impacted results and also back up your significance of creating antibiotics with this info a little better.

Reviewer #2 (Recommendations for the authors):

Congratulations to both authors on this nice story!

The only extra experiment that I would like ’o suggest is the (sub-)cellular localization of AhfA. The authors speculate in the discussion about cytoplasmatic localization. It would be nice to really determine that by cell fractionation or imaging methods.

Reviewer #3 (Recommendations for the authors):

This is a well-presented manuscript with important conclusions, both about phage requirements and mycolic acid synthesis, with a significant follow-up of important hits.

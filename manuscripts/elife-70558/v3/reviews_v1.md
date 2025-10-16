# Peer review - Round 1

Editors:
- Zacharias Kontarakis, ETH Zurich Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70558.sa0](https://doi.org/10.7554/eLife.70558.sa0)

This manuscript describes the addition of a short tag on the Cas9 nuclease as a means to improve genome editing efficiency. Importantly, the authors have tested their approach on several genomic targets, model organisms, and Cas9 derivative engineering tools. Overall, these findings support the possible general applicability of this tag for improving the outcomes of a wide range of modern Cas9 based applications, including Base Editors. Adding to a recent report of improving Prime Editing by optimising the NLS, this paper reinforces the notion that there is still unexplored space in altering genome engineering activity in a modular way.


---

# Peer review - Round 1

Editors:
- Zacharias Kontarakis, ETH Zurich Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70558.sa1](https://doi.org/10.7554/eLife.70558.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "hei-tag: a highly efficient tag to boost targeted genome editing" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Zacharias Kontarakis as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Didier Stainier as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Benchmark hei-tag activity against the state-of-art genome engineering tool in each experiment (see reviewer comments – also comparison to RNP use in fish is highly desirable).

2) Provide heiCas9 editing data across multiple targets/gRNAs, ideally showing diverse characteristics (e.g. genomic location, sequence, activity).

3) Edit manuscript to clearly describe the strengths and weaknesses of the "hei-tagging" method.

Reviewer #1 (Recommendations for the authors):

I have a few concerns regarding the way the authors structure and present their claims:

1) One of the main take home messages (based on the Abstract) is that the hei-tag boosts the activity of a "wide variety" of genome editing tools. Even though the BE data are promising, the manuscript could use more examples (e.g. prime editors, that have been used in zebrafish – Petri et al., 2021). Can the hei-tag make editing possible in cases where it is undetectable with the state of the art tools?

2) Throughout the manuscript, the authors use only a handful of guides. Adding more examples, especially using guides that show a range of efficiencies with the non-hei-tag Cas9 would provide a better description of the strengths and limitations of the hei-tag.

3) What is the rationale of using the Cas9 from Hwang et al., and not the zebrafish codon optimised Cas9 from Jao et al?

4) Why do the authors use the GeneArt nuclease as a "state of the art" for the cell culture? What other tags are included in this nuclease? We can see that the worse score in Fig1d comes from JDS246. Not having the hei-tag is only one difference between JDS246 and heiCas9. One other is that heiCas9 lacks the FLAG (Myc-Cas performs already pretty well, however zebrafish data are not shown). How does GeneArt Cas9 compare in that respect? Such information should be presented to readers.

5) In Figure 1, what do the single guide results look like? Boosting deletion outcomes using two guides is not the same as boosting activity of single guide editing. Is the activity of both guides improved? Are they just being brought at the same level? Did the authors use sequencing to analyse what happened at the DNA level?

6) The hei-tag could be affecting editing outcomes, rather than ON target activity. In Figure S1, it is clear that the frequency of the in frame -15 allele is reduced, while overall efficiency in not dramatically affected. Changing the editing profile by using different nucleases (variants) is not the same as boosting efficiency in KO. The in-frame indels could be favored in other sites, thus reducing KO-score (if out of frame are regarded as desired outcome).

7) Generally, it is advised to use NGS data for strong claims about editing efficiency.

8) If ON-target activity is boosted, increased OFF-target activity is of concern, especially in cell culture when editing accuracy and precision are key. Since the main focus of the authors is not mammalian cell culture or therapeutic applications, they should at least be clear about this limitation.

Generally, the manuscript would be strengthened by including more examples of editing tools (desirable, but not absolutely required), include analyses of more guides (required), add sequencing data wherever possible (highly advised), adequately discussing strengths and limitations of the hei-tag (required), presenting some NGS data (recommended), toning down some "generalised" claims (unless more supporting data are provided).

Reviewer #2 (Recommendations for the authors):

Several reports in zebrafish have shown that Cas9/gRNA complexes injections can reach gene editing up to 100% in F0 embryos including when targeting multiple loci at the same time (See for instance Wu et al., 2018 and Kroll et al., 2021). In light of these impressive results the utility of the present method for the fish community is overstated at best without mentioning these points anywhere in the discussion.

The authors should attempt to compare the injection of heiCAS9 protein as this is the current preferred and most efficient method in the fish community.

In the present manuscript is not clear what is the purpose of the Myc tag in the construct. This is not used at all to visualize protein localization or purification. Do the authors believe that the addition of Myc increases Cas9 activity? If not giving that this is a method paper they should demonstrate the utility in this specific contest.

The zebrafish experiment lacks the comparison of the heicas9 with the most efficient myc-Cas9 leading to an overestimation to the improved efficiency of the construct.

Finally methodological papers based on a single locus are difficult to appreciate as they may be influenced by "the gambler's luck" (i.e. the chosen locus cold be a fortunate pick). These results should be extended to other genes as it's standard in the field (see the two publications above).

Finally the base editor experiment are equally strongly biased. The comparison with BE4-Gam is not representative of the current state of the art were several reports using ancBE4Max (See for instance Carrington et al., 2020, Zao et al., 2020 and Rosello et al., 2021) show highly improved results. In lights of these papers the statement "Notably, in heiBE4-Gam injections, for each of the three cytosines in the base editing window, the C-to-T transition rate was higher than 60%, a level never observed in BE4-Gam injected embryos" is not true as similar or higher level of C to T conversion have been reported. Again this a comparison with ancBE4Max should be extended to multiple loci.

Reviewer #3 (Recommendations for the authors):

1. In the abstract, the authors introduced factors that leave room for the improvement of gene editing efficiency in CRISPR/Cas9 tools: (1) nuclear localization signal -citing Cong et al., 2013; and (2) protein tags for "immediate detection or straight-forward purification" and linkers to "avoid steric hinderance impacting on activity" -citing Zhang et al., 2014. However, such conclusions were never made in either of the originally cited papers. Cong et al., did not compare the editing activity with and without a NLS signal. On the contrary, there are partial evidence indicating that Cas9 protein may not require an NLS to assist import into the nucleus (Hu et al., G3, 2018). In Zhang et al., it was suspected that the addition of a flag or myc tag changed the charge distribution of the Cas9 protein, thus increasing its specificity and efficacy. No statement was made about the purification or the linker. It is OK to introduce the relevant background, but I find it problematic to misinterpret the cited literature to show conclusions they did not make.

2. The authors used modified version of NLS in the hei-tag construct to facilitate early nuclear targeting, while a straight-forward way to make nuclear-targeted Cas9 available in the cell is to directly inject the (nuclear-targeting) Cas9 protein. The authors should either provide this control experiment, or clarify why they only chose to build RNA-based systems.

3. It is widely known that the gRNA design is a critical factor affecting the gene editing efficiency. While hei-tag shows an increased bi-allelic editing efficiency than the control constructs, it is not clear whether this boost is universal with different targeted genes and different sgRNA designs.

4. JDS246-Cas9 was chosen as the baseline construct to evaluate the boost of editing efficiency. Given this was a construct originally made for mammalian cells, it is not clear whether it represents the state-of-art editing techniques, especially in zebrafish. While it is unrealistic to test all the available tools, other systems have been reported with high bi-allelic editing efficiency specifically in zebrafish should be introduced as a control (e.g. Jao et al., 2013, PNAS -disclaimer: the reviewer was not a maker of this tool).

5. In the base-editing experiments, the injected fish showed various level of eye-pigmentation colors, in contrast to the knockout experiment where cells devoid of pigment appear in patches on the eye. The authors should provide an explanation of why this is the case and justify why the pigmentation level has to be quantified differently in Figure 3 than Figure 1.

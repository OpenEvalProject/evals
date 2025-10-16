# Peer review - Round 1

Editors:
- Magnus Nordborg, Austrian Academy of Sciences Austria

Reviewers:
- Magnus Nordborg, Austrian Academy of Sciences Austria
- Nicholas H Barton, Institute of Science and Technology Austria Austria
- Joachim Hermisson, University of Vienna Austria

## Review text

DOI: [10.7554/eLife.39702.041](https://doi.org/10.7554/eLife.39702.041)

In the interests of transparency, eLife includes the editorial decision letter, peer reviews, and accompanying author responses.

[Editorial note: This article has been through an editorial process in which the authors decide how to respond to the issues raised during peer review. The Reviewing Editor's assessment is that all the issues have been addressed.]

Thank you for submitting your article "Signals of polygenic adaptation on height have been overestimated due to uncorrected population structure in genome-wide association studies" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Magnus Nordberg as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Mark McCarthy as the Senior Editor. The following individuals involved in review of your submission have also agreed to reveal their identity: Nicholas H Barton (Reviewer #2); Joachim Hermisson (Reviewer #3).

The Reviewing Editor has summarized the major concerns shared by all reviewers, and we have also included the separate reviews below for your consideration.

If you have any questions, please do not hesitate to contact us.

Summary:

This is one of two papers demonstrating that published signals of selection on human height cannot be replicated in the recently released UK Biobank data, apparently because these signals were caused by confounding population structure that is absent in UK Biobank data.

Major concerns:

We were struck by how both papers focus on spurious signals of selection rather than the underlying cause, which is that the GWAS effect-size estimates are confounded. The former is a somewhat esoteric question, but the latter may have enormous implications for much of human genetics, and these papers are likely to be heavily cited because of this. However, the papers seem to go out of their way to avoid discussing this topic. Of course we are not the authors, but, for the record, it looks odd.

Furthermore, the papers seem to suggest that confounding is not present in the UK Biobank data, but isn't it more likely that the magnitude is simply smaller?

Both papers also present evidence that a sib-based study by Robinson et al., 2015, that was meant to eliminate confounding did no such thing. This is disturbing, and while we understand that identifying the reason may be beyond the present papers, the general implications should again probably be discussed.

Finally, this paper often seems stream-of-consciousness: it lacks detailed explanations as well as a coherent outline, making it very difficult to follow unless you are a specialist in the field. We urge the authors to explain better for a general audience.

Separate reviews (please respond to each point):

Reviewer #1:

This one of at least two papers appearing simultaneously and reaching exactly the same conclusion. It is well written.

The only thing that surprises me about this paper is that it, as well as the other one I have seen, focuses on the relatively obscure issue of whether height has been under selection, tiptoeing around the much bigger issue (the elephant in the room) that the reason the claims for selection do not stand is that the GWAS estimates of effect sizes are biased because of population structure. It is not just the selection signals that do not replicate, but the polygenic scores. I'm not surprised, but, as you know, there are probably at least a hundred papers out there that are based on the infallibility of LD score regression and genomic prediction. I understand the need for caution before attacking this edifice, but I nonetheless think some clarification is unavoidable.

Reviewer #2:

This paper identifies a discrepancy between signs of selection estimated from UK Biobank data, compared with previous studies, and suggest that those earlier signals were caused by subtle stratification in the data. This is a useful contribution to an important question. I have only minor comments (below), but overall, urge the authors to try to rewrite the text to make it more accessible to those not immersed in the field. I find it hard to make specific suggestions, but it comes across as a list of statistical tests, without enough flow to carry the reader along with the argument. Admittedly, given the quite intricate arguments, this is not easy to do.

Minor Comments:

Why should one believe that using the first 15 PC corrects for stratification? Even this is somehow traditional in the field, it needs explanation, since the failure of the correction is the key point of the paper.

Figure 1B: – The x axis needs to be labelled. More important, Spearman's correlation seems far too small, given that by eye, the points follow the linear regression rather well. This may be related to the large values seen at the right of each figure, fitting a single regression is clearly inappropriate. There needs to be a test which separates these two sets of points in some way: as it stands the significance test is just not appropriate.

Figure 3: – b in the figure should be β. Also, there is a paragraph break before "The patterns" which makes it hard to work out what is main text and what is caption.

Figure 4: – I do not understand what the "six summary statistics" are here.

Discussion section: – The concluding paragraph seems too weak, especially the sentence "In no way..". Surely the point of the paper is to "question the statistical methodology.… in polygenic tyests for adaptation", since that methodology seems to give spurious results? It is also not at all clear how much the stratification implied here influences effect size estimates in GWAS.

Paragraph five of subsection “Polygenic scores”: Does the distribution in fact follow a β?

Reviewer #3:

Both manuscripts by Berg et al. and Sohail et al. present thorough and insightful analyses with highly relevant results for current and future GWAS studies. Even prior to publication, the manuscripts have considerable impact. They will be widely read and cited. I do not think that further analyses are needed, with the potential exception of the third point below. All other points concern the discussion, in particular the guidance for further research that will surely emerge from these studies.

How safe are results based on the UK Biobank data?

This refers to the weak signals reported (with much caution) in the present studies, but also to potential future results on other traits. You recommend using data "such as UKB" and we will certainly see many more studies based on this resource. I would therefore appreciate a more specific discussion of risks connected to this particular data set.

1) Stratification even within the UKB-GB data: It is well known that height and socioeconomic status are correlated in modern societies (e.g. BMJ 2016; 352:i582), and social status correlates with descent. In the UK, both factors are also geographically stratified, with people living in the north of the country having lower socioeconomic status and shorter stature, on average, than those in the south. Furthermore, the percentage of Anglo-Saxon admixture varies across the UK. How could these factors influence results based on UKB data, both here and otherwise?

2) Potential influence of GxE interactions: The manuscripts focus (for good reason) on issues connected with stratification. However, if polygenic scores depend on the environment (e.g., due to countergradient variation), GxE interactions are an alternative confounding factor. Importantly, use of a homogeneous detection panel (to avoid stratification), such as UKB-GB, could increase these effects. Maybe this should be briefly discussed in the context of the present results and mentioned as a necessary caveat also for future studies that use detection panels from narrow geographic regions.

What, exactly, causes the problems with the previous data?

3) There seem to be two relevant differences of the GIANT data relative to UKB: 1) UKB is much more homogeneous and 2) GIANT is a meta-study, collecting summary statistics from many sources that are individually corrected for stratification. One would like to know better which factor is decisive. This could be further addressed by combining summaries from sub-samples of the "UKB-all" data in an artificial meta-study.

4) The Robinson et al., 2015 GWAS: Sib-based studies are done to avoid / minimize stratification effects and the Robinson 2015 data have been used as a proof of robustness in several previous studies. The fact that you find clear signs of stratification is sobering and one would like to know what has gone wrong. You may not currently have any explanation and this is fair enough. However, the discussion should be clearer and say upfront that results based on these data cannot be trusted until we understand the issues.

Minor Comments:

a) You use 11 different summary statistics, with partly inconsistent naming strategy. I had to look up names in the methods part a number of times. I think this can be improved. Maybe even use the same names as Berg et al. where the summaries are identical.

b) The switch from 1000 genomes to POPRES complicates comparison between figures. If there are advantages of POPRES, why not use it throughout? This holds, in particular, for the test of the latitudinal slope, which would be more convincing with many populations rather than just 4 from the 1000 genomes data.

c) Figure 4: "The overdispersion signal disappeared entirely when the UK Biobank family based effect sizes were used": Is this due to the smaller sample size of the sib data or due to residual stratification issues in UKB? This could be tested using a sub-sample from UKB of the same size as the sib data.

d) Figure 3 legend: "suggesting that tSDS shift at the gw-significant SNPs is not driven by population stratification": only true for stratification due to this particular axis.

Additional data files and statistical comments:

All necessary information is provided and the UKB sib data is on Dryad. I think the other newly generated GWAS data should go there, too.

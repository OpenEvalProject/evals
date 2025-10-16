# Peer review - Round 1

Editors:
- Peter J Turnbaugh, University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72801.sa0](https://doi.org/10.7554/eLife.72801.sa0)

Not everyone colonized by C. difficile has gut symptoms, but the reasons why are unclear. This article uses the combination of sequencing and mass spectrometry to compare patients with or without symptoms, revealing links between specific gut bacteria and diet, which could lead to diet or bacterial treatment or prevention strategies.


---

# Peer review - Round 1

Editors:
- Peter J Turnbaugh, University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72801.sa1](https://doi.org/10.7554/eLife.72801.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Multi-omics investigation of Clostridioides difficile-colonized patients reveals protective commensal carbohydrate metabolism" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Peter J Turnbaugh as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Gisela Storz as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Need to discuss the ability to exclude alternative hypotheses, including variations between C. difficile strains, dietary intake, differences in host physiology, and bile acid production/metabolism. The former seems like a critical point – are these individuals colonized by similar strains of C. difficile? Are they all toxin positive? It is critical to test if C. difficile from the Cx+/EIA- samples are actually capable of producing toxin. This is important to discern whether there are facets of the microbiome/metabolome which turn toxin off in Cx+/EIA- samples or if C. difficile in these patients have mutations which make them unable to produce toxin.

2) Given the compositional nature of the sequencing data it is possible that differences in C. difficile are responsible for some of the observed differences in community structure. Please mask C. difficile reads and re-run the key analyses to check if they hold up.

3) Please discuss the literature precedent for C. difficile growth on different carbohydrates and ideally include data for the type strain.

4) Please check if the conclusions are impacted by removing the Cx+/EIA- samples with metagenomically undetectable C. difficile from the computational analyses used in Figures 1-3. The concern is whether these samples are driving the perceived differences between Cx+/EIA+ patients and Cx+/EIA- patients (does C. difficile abundance or metabolite abundance still differentiate Cx+/EIA+ patients from Cx+/EIA- patients?).

Reviewer #1:

The mechanisms that protect some individuals from C. difficile-associated colitis remain poorly understood; however, recent data has implicated both diet and the microbiome. Here, the authors use paired metagenomic and metabolomic analysis to identify differences in asymptomatic and symptomatic patients, suggesting that competition between clostridial species for carbohydrate metabolism may play a role. The data is clearly presented and provides clear hypotheses for future studies aimed at understanding the complex interactions between enteric pathogens, the gut microbiome, and host pathophysiology.

Strengths of this study include its unique cohort, rigorous analysis and presentation, inclusion of some initial in vitro validation work, and potential for inspiring future hypothesis-driven experiments.

Weaknesses include the lack of consideration or ability to control for alternative hypotheses, including variations between C. difficile strains, dietary intake, differences in host physiology, and bile acid production/metabolism. The effect sizes are also modest with no high-level differences in the microbiome or metabolome between groups. Finally, there is no evidence of generalizability to other patient cohorts. Given these caveats, it is important to be clear throughout that this is a hypothesis generating exercise and that the degree to which commensal carbohydrate metabolism is protective against C. difficile infection requires further clinical and mechanistic data.

Comments for the authors:

1. Need to discuss the ability to exclude alternative hypotheses, including variations between C. difficile strains, dietary intake, differences in host physiology, and bile acid production/metabolism. The former seems like a critical point – are these individuals colonized by similar strains of C. difficile? Are they all toxin positive? I was unclear how asymptomatic carriage is defined, this is critical to the current paper and should be included in the main text and methods, not as a citation.

2. Given the compositional nature of the sequencing data it is possible that differences in C. difficile are responsible for some of the observed differences in community structure. I'd recommend masking C. difficile reads and re-running the key analyses to check if they hold up.

3. The in vitro validation is helpful, but I'm unclear as to whether it is new information. If any prior studies have been done they should be cited here.

Reviewer #2:

The manuscript by Fishbein et al. examines an exciting and timely question about the microbial and metabolomic factors in the gastrointestinal tract that determine if C. difficile remains dormant as a colonizer or triggers infection. They do this through the re-analysis of their previously published cohort wherein they can separate the colonization vs infection state on the basis of qPCR and toxin detection (EIA) which provides a unique opportunity to address their question in an excellently phenotyped cohort.

Using appropriate and current approaches, the authors find relatively subtle differences in the microbiome and metabolome of colonized/infected participants including certain carbohydrates which are elevated in asymptomatic individuals. They demonstrate these carbohydrates are not substrates for C. difficile; however, this line of experimentation sought to find negative results and it remains to be determined if they have any relevance in vivo or in complex communities. The authors could consider an additional experiment to probe this observation in more depth such as ex vivo fecal incubations or strain-strain competition experiments to provide more direct evidence for how they may influence the suppression of C. difficile.

Comments for the authors:

Given that this manuscript is primarily computational, it would be beneficial if the code for the analysis was shared in a public repository.

PRJNA748262 does not appear to be publicly available.

Line 66: would asymptomatic colonization be on the disease spectrum?

Reviewer #3:

This manuscript reveals exciting details of the lifestyle of C. difficile in individuals who are asymptomatic carriers and contrasts these with individuals with active CDI. It will be an important contribution to the C. difficile research field and more broadly to people interested in targeted manipulation of microbial communities.

The study team leveraged a unique patient cohort, coupled with metagenomic and metabolomic analyses, and bacterial culture techniques to suggest that the gut microbiome (namely, commensal clostridia) inhibit C. difficile proliferation. Much of the paper relies on the idea that C. difficile burdens are lower in asymptomatically colonized individuals versus those with C. difficile infection (CDI). However, many individuals who are asymptomatically colonized with C. difficile have burdens that are comparable to those who have CDI (and there may be a bimodal distribution of asymptomatically colonized individuals – those that have C. difficile detectable by metagenomic sequencing and those that do not). I worry that their conclusions are skewed by an apparent binary distribution of C. difficile burdens in both patient groups.

The patients are binned based on initial C. difficile diagnostic tests (asymptomatic individuals carry toxin-encoding C. difficile as detected by PCR but have no detectable toxin via immunoassay). I am unsure how sensitive the standard diagnostic immunoassay for C. difficile is but do know C. difficile toxin production is controlled by a complex regulatory network and abundance of these toxins can change with respect to parameters such as nutrient availability, temperature, pH, and cell density. I wonder if the isolates from the study are all capable of producing functional toxin. These strains could have mutations (in regulatory elements, for example) that may impact toxin production.

The authors perform a culture-based experiment to support their findings that certain metabolites present in the gastrointestinal tracts of asymptomatic individuals do not support the growth of C. difficile. They use isolates from the study participants but it is unclear if these isolates were taken from asymptomatic individuals or those with CDI but do not leverage strains commonly used in the research community (C. difficile 630 and C. difficile R20291).

Lines 67-69. What is the limit of detection of EIA? It's striking to me that, while C. difficile burdens are a predictor of Cx+/EIA+ vs. Cx+/EIA- patients, there are ~23 Cx+/EIA- patients whose relative abundance of C. difficile essentially superimposes with those of the Cx+/EIA+ group. There are fibroblast rounding assays that quantify C. difficile toxins. The limit of detection of these assays may be lower than kits used in diagnostic labs. Can the authors perform one of these assays on the samples in this study to better calibrate readers expectations of whether toxigenic C. difficile is or is not expressing toxin? As the paper stands, I assume that production of toxin in C. difficile is all-or-nothing, but prior work on regulation of toxin production in C. difficile has demonstrated that many regulatory cues influence toxin production (Martin-Verstraete et al. 2016) so I expect this to be non-binary. In addition, and considering the regulatory networks that control toxin production, are the C. difficile isolates from asymptomatic patients capable of producing toxin in vitro? Just because the gene is there doesn't mean that it's functional.

Line 140-142. "Given that C. difficile levels were an overt predictor of CDI…" Are C. difficile levels still a predictor of the Cx+/EIA+ state if the samples where C. difficile was not detectable by metagenomic sequencing were removed (see Figure S1C [bottom right hand corner of the graph], n=2 Cx+/EIA+ samples and n=? Cx+/EIA- samples)? The burdens of C. difficile in these individuals seem to be at least an order of magnitude lower than patients with low-but-detectable burdens and appear to be bimodally distributed. If there is no change to the conclusions of the study if these samples are removed, are there features (metabolites, taxa) that differentiate individuals who do or do not have metagenomically detectable C. difficile?

Line 144. There is no Figure S1D in the manuscript.

Lines 228-230. I really like the idea that rhamnose may be the by-product of microbiome metabolism or other dietary polysaccharides which could exclude C. difficile from the gut. What is known about rhamnose metabolism by gut microbes? Do any of the taxa that associate with Cx+/EIA+ conditions metabolize rhamnose? Do any of the taxa that associiate with Cx+/EIA- conditions metabolize rhamnopolysaccharides? This could be done by mining the metagenomes for CAZymes or by performing growth assays with isolates of relevant bacteria.

Lines 248-251: "The observed increased abundance of monosaccharides…" If this is true, shouldn't there be fewer sugars in both high diversity conditions and low diversity conditions? That is, in a high diversity microbiome, some microbes would metabolize complex polysaccahrides and others would cross feed on the waste products, whereas in a low diversity microbiome, there may be fewer degraders of polysaccharides, but maybe also fewer cross-feeders? Further expansion on this complexity or references to support the assertion in the sentence on lines 248-251 would be useful.

Lines 253-256: Given the previous reports cited in the manuscript and the range of metabolic capabilities illustrated by the clinical isolates used in this study, it would be worthwhile to assay the sugars from Figure 4 against strains of C. difficile commonly used in the C. difficile research community (at least, C. difficile 630 and difficile R0291).

Lines 262-264: This is really interesting. How many patients were excluded? Assaying toxin production in these patients (see comment on Lines 67-69, above) before and after diagnosis, or sequencing C. difficile from these patients at each of these time points, would be helpful in thinking about the transitions between asymptomatic carriage and symptomatic CDI. This is, of course, beyond the scope of the current study and only mentioned because it would be of scientific and clinical interest.

Line 320. How many Cx+/EIA- samples were included in the study?

Line 397. Please clarify in this section of the same conditions were used for VPI10643.

Lines 438-441. What percent of the variation in the data are expressed in this beta diversity metric? Is the conclusion different if a phylogenetically-aware metric (e.g. Weighted/Unweighted UniFrac) is used?

Figure S1. Please include p values for taxa noted in Figure S1C. How many patients' stool samples have undetectable C. difficile via metagenomic analysis?

Figure 4. OD readings are typically plotted on a log scale for growth curve data.

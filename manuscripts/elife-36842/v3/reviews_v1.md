# Peer review - Round 1

Editors:
- Zoran Nikoloski, Max Planck Institute of Molecular Plant Physiology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.36842.sa1](https://doi.org/10.7554/eLife.36842.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Essential Metabolism for a Minimal Cell" for consideration by eLife. Your article has been reviewed by Naama Barkai as the Senior Editor, a Reviewing Editor, and two reviewers. The following individual involved in review of your submission has agreed to reveal his identity: Ron Milo (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript by Breuer et al., addresses the important question of a minimal cell and provides a valuable resource in the field of synthetic biology. The extensive manual curation, the reconstruction of the metabolic network, and its characterization in silico and with usage of proteomics data provide a valuable foundation for studying the features of a minimal cell. The experiments and hypotheses suggested in the discussion are particularly appreciated. While the presented work provides a knowledge base resource to the community, the predictions formulated by the metabolic model should be described in a more nuanced way.

Essential revisions:

One of the main concerns deals with the lack of organism-specific incidental to the model predictions, namely: biomass composition, substrate uptake rates and secretion rates. While it is challenging to obtain such level of detail for a minimal organism, and the employed data pertain to the parental strain, it is important to explain how the model represents Syn3.0A and not Syn1.0. Although a comparison of the proposed and existing models has been attempted, the authors should provide a direct comparison of the metabolic capabilities between the original Syn1.0 strain and the reduced Syn3.0A to better delineate the latter from the former. The authors should clearly describe the approach (automated (how) or manual) used in comparing JCVI-syn3.0A model and iJW145.

A related concern is the approach used to infer internal composition from the growth media, since the media composition is not representative of the cytosol concentration. The authors should clarify the logic and approach used; if already published, the followed procedure should be appropriately referenced.

A third concern is the support of the claim that the model correctly predicts gene essentiality and could help further reduce the model namely through double knock-out simulations. Since Table S6 describes model accuracy, it should be moved to the main text. Given the availability of the data on categorization of the genes in 3 categories (essential, non-essential and quasi-essential), the authors should calculate the Matthews Correlation Coefficient: (1) assuming the quasi-essential genes to be essential and (2) assuming quasi-essential genes to be non-essential. The obtained metric should be compared to other Mollicute metabolic models.

The authors should verify the way in which the sensitivity analysis is conducted. A reasonable way to do the sensitivity analysis is to investigate what percentage of growth rate change is found for a given percentage of change in a parameter. Such an analysis may imply very strong variation in contrast to what is stated by the authors. In particular, the effect of the non-growth associated maintenance (NGAM) should be particularly re-investigated since the assumption that the NGAM would be strictly limited to the ATP efflux seems likely to be an under-estimation as many cellular processes may not be described.

The authors should use correct terminology when describing predictions from flux balance analysis throughout the manuscript, as it predicts yield; the conversion to growth rate is dictated by what the authors assume for uptake rate which if not measured but is a gross proxy, as indicated above.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Essential Metabolism for a Minimal Cell" for further consideration at eLife. Your revised article has been favorably evaluated by Naama Barkai (Senior Editor), a Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Reviewer #2:

We wish to thank the authors for taking time to address our previous comments. The addition of the whole metabolic map for JCVI Syn3.0 is integrative and should help readers understand the metabolism of the minimal cell. We appreciate that the model predictions were nuanced according to the available data (i.e. steady-state fluxes, in silico gene knockout mapping, etc.). While these comments were properly addressed, a second view of the (lengthy) paper yielded new comments:

Abstract:

The Abstract is overly concise for a paper that spans 76 pages including references. In general, the conclusions exposed in the abstract should be extended and "98% of enzymatic reactions supported by annotation." This seems like a wrong and inflated number that does not reflect the uncertainty in the network. Excluding exchange reactions, biomass, growth-associated maintenance and gas diffusion (O2 and CO2) 36 reactions remain orphan, including many transports. This correction brings the percentage down to 85.6% when applying a denominator of 250 (again excluding the mentioned reactions above).

"The model agrees well with genome-scale in vivo transposon mutagenesis experiments" Perhaps provide a quantitative statement rather than a qualitative one.

"The genes in the reconstruction have a high in vivo essentiality or quasi-essentiality of 92% , compared to 79% in silico essentiality." While the results presented in supplementary table 2 are consistent with these two numbers, we find 76% in silico essentiality when testing the model provided for single gene deletions. Also, the in vivo essentiality of 92% is obtained when assuming quasi-essential genes as essential and should be specified or the number with only essential genes (68%) should be included or at least mentioned.

"The reconstruction is the starting point for studying the evolution of metabolic subsystems and analyzing the effects of introducing alternative pathways." If claiming this in the abstract perhaps include subsystems to the reactions in the model.

"Finally, the identification of 30 essential genes with unknown function will motivate the search for new biological mechanisms beyond metabolism." After reading through the entire paper multiple times I still cannot see where this number is fetched from, so I cannot imagine how a reader could get to it.

Rather than pointing to a very accurate model of Syn3.0, the abstract should demonstrate that despite being the smallest organism known to date, Syn3.0 has many unknown elements. While the amount of information provided in the paper is highly valuable for the community, presenting the reconstruction as a way to clearly identify the grey areas of the genome is key for the development and substantial efforts have been made in that sense through 1- a detailed manual curation process, 2- proteomic validation of enzyme expression, 3- in vivo gene essentiality. This sentence of the abstract should be of prime importance: "This comparison together with proteomics data yields new hypotheses on gene functions as well as suggestions for several further gene removals".

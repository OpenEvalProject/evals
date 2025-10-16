# Peer review - Round 1

Editors:
- Peter Turnbaugh, University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58609.sa1](https://doi.org/10.7554/eLife.58609.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Hydrogen metabolism is important for infectious disease agents, but its role in chronic diseases like inflammatory bowel disease remain unclear. In this report, Hughes et al. analyze human microbiome data and use mouse models to demonstrate that hydrogenases are important for fitness in the inflamed gut, suggesting that hydrogen metabolism may contribute to bacterial overgrowth during colitis.

Decision letter after peer review:

Thank you for submitting your article "Reshaping of bacterial molecular hydrogen metabolism contributes to inflammation-associated gut microbiota dysbiosis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Peter Turnbaugh as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Wendy Garrett as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Hughes et al. investigate the role of hydrogen utilization by E. coli during colitis. They analyze previously published metagenomic datasets in humans and in mice to identify bacterial hydrogenases as factors that are increased during colitis. With a series of elegant in vivo experiments, by using a DSS colitis model and an IL10 colitis model, they demonstrate that hydrogenases are important for fitness in the inflamed gut for both a mouse and a human E. coli isolate. Overall, this is an important and well-conducted study, which nicely demonstrates the importance of hydrogen metabolism for bacterial overgrowth during colitis. The experiments are well designed and conducted, and carefully interpreted. The study fits well with the literature demonstrating a role for hydrogenases during infection with pathogens, but for the first time it shows their importance also for metabolism of non-pathogenic strains in inflammatory conditions.

Essential revisions:

1. The bioinformatics analysis is well motivated but could use a lot more work and details. The methods are unclear as to what cutoffs are used. There's no discussion of any controls that were run or prior data indicating the reliability of the hydrogenase annotations. The re-analysis of the human and mouse data did not adjust for multiple hypotheses. More importantly, gene abundance is analyzed without accounting for the increased abundance of Enterobacteriaceae in colitis, which could easily explain the observed gene-level enrichments. As is, I'm unconvinced that there is an association between IBD and hydrogenase abundance or the specific enrichment of "uptake hydrogenases".

2. Another major issue in my opinion is the conceptual framing around "dysbiosis", which is a problematic term due to its inconsistent use in the scientific literature but nonetheless implies some sort of overall shift in gut microbial community structure. That isn't really tested here, all of the experiments show competitive growth between artificial mutants and wild-type E. coli. There's also only a single experiment (Figure 4) that include healthy controls, making it impossible to determine if the expansion of E. coli is impacted by the loss of hya and/or hyb. Figure 4c,d shows that the double KO is still able to expand in DSS treated mice, conflicting with the hypothesis that hydrogen metabolism is required for dysbiosis. On a related note, the authors should discuss the alternative hypothesis that dysbiosis occurs prior to colitis. The assumption herein is that inflammation drives a shift in the microenvironment's redox potential which then shifts the gut microbiota. More citations are needed to explain the rationale and current evidence in support of these two alternative hypotheses in humans and mouse models. One simple experiment that could be done to address the author's dysbiosis hypothesis would be to colonize mice with a single strain at a time. Can the double KO still expand in the absence of wild-type? Does it reach a lower abundance than wild-type in mono-colonization?

3. While the genetics shows that this operon matters in vivo, there's no real data supporting whether or not hydrogenase activity is responsible, either in vitro or in vivo. Ideally additional assays and/or experiments could be added to provide support for the metabolic consequences of these deletions. At a minimum, this caveat needs to be added to the discussion and the authors should be careful not to imply that the activity matters (just that the operons do). Key controls are also missing for the bacterial genetics, including comparisons of the KO and wild-type strains during in vitro growth and complementation.

4. There is little insight into how mechanistically these hydrogenases may provide a growth advantage in the intestine, and specifically what it is about inflammation that makes Hyd-1 and Hyd-2 important? For example, how does DSS-induced weight loss change in Enterobacteriaceae-free (Jax B6) mice vs. those colonized with MP1 or EcN strains of E. coli? One might infer that EcN induces less inflammation than MP1, based upon Figure 2B vs. D, but there is no control group without E. coli to compare to. This leads me to the next example, which is Figure 5 piroxican Il10-/- experiments. Although the body weight of Il10-/- BALB/c mice on piroxicam is only minimally reduced (indicating less inflammation) compared to the Il10-/- C57BL/6 model, the EcN and MP1 bloom is still statistically significant. It is an oversimplification to conclude that Hyd-1 and Hyd-2 are important during "inflammation," as weight loss is the only measure of inflammation and differs between mouse strains and models. I recommend additional controls for each of these models, including DSS or piroxicam with no E. coli colonization, and knockout strains evaluated in the presence and absence of inflammation (i.e. no DSS to demonstrate Hyd-1 and Hyd-2 are not important under homeostatic conditions). Furthermore, there should be greater analysis into what aspect of inflammation makes Hyd-1 and Hyd-2 important for bacterial bloom – is there a direct correlation between extent of weight loss? Is there an immune cell type, cytokine signature, or histologic feature that makes Hyd-1 and Hyd-2 important? The spread of data in Figure 5 shows it would be possible to tease this apart.

5. Male and female mice were used in these experiments. DSS has a known sex difference. The authors must indicate the sex of the mice and test to see if sex could be responsible for the observed changes.

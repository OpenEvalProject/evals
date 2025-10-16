# Peer review - Round 1

Editors:
- Max Nieuwdorp, AMC Netherlands

Reviewers:
- Andrei Prodan, Amsterdam University Medical Center Netherlands
- Paul O'Toole, Ireland

## Review text

DOI: [10.7554/eLife.42693.036](https://doi.org/10.7554/eLife.42693.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Extensive Transmission of Microbes along the Gastrointestinal Tract" for consideration by eLife. Your article has been reviewed by Wendy Garrett as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Andrei Prodan (Reviewer #1); Paul O'Toole (Reviewer #3).

The reviewers have discussed the reviews with one another and although the paper is currently now suitable for publication, the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper by Schmidt et al., is an overall well written manuscript that shows that bacterial strain exchange between the oral and gut environments is more extensive than previously thought. Additionally, the manuscript puts forth that this is a normal occurrence, rather than solely a mark of dysbiosis / disease and that opportunistic pathogens had higher evidence of transmission along the gastrointestinal tract with an extensive exchange of strains between the two using SNV profiles of each bacterial strain with oral cavity bacterial strain dominance.

Essential revisions:

There are a few methodological questions that needs to be addressed. This includes cross checking with the ConStrains method to identify microbial strains (Luo et al., 2015. Also, the amount of sequence coverage per sample (in Gbp) should be specified so that readers have a platform-independent reference point for the coverage that is necessary and sufficient for SNV analysis. Moreover, as reviewer 3 points out the authors should further expand on their estimations of quantities and viability of bacterial cells in the lumen that can be attributed to salivary bacteria. In this regard, the paper could be strengthened if there would be some data on viability of bacterial strains in the intestinal tract as the authors might have underestimated the contribution of passively translocated DNA (belonging to living or dead bacteria) to the faecal microbiota. In this regard, a few years ago, Korem et al., (2015) published about this using shotgun metagenomic sequencing to calculate the ratio of sequencing coverage between the peak and trough providing a quantitative measure of a species' growth rate. It would be of importance to see if this bioinformatic approach would help solve this question. Finally, a dedicated section on statistical analysis in the method description of the paper would be helpful and the numbers of included individuals should be cross checked within the supplemental data and tables (e.g. Figure 1).

Please see the full reviews below for further points:

Reviewer #1:

This is a solid paper which shows that bacterial strain exchange between the oral and gut environments is more extensive than previously thought and a normal occurrence, rather than solely a mark of dysbiosis / disease. Nonetheless, they also show that opportunistic pathogens had higher evidence of transmission. While the authors find no correlation between the β-diversity measures (as determined by metagenomic profiling) of the gut and the oral environment, they show that there is an extensive exchange of strains between the two. This is done by determining the strain profiles (SNV profiles of each strain) and showing that, based on probabilistic models, the overlap in some of these profiles is significantly higher than would be expected by random chance ("transmission scores"). The fact that species transmission scores correlate with oral relative abundance, but not to gut abundance, indicate that (as would be expected) the direction of transmission is from the oral cavity to the gut as does the fact that 'oral SNVs observed at an initial time point were significantly enriched among fecal SNVs that were newly gained over time, but generally not vice versa '. The paper is made stronger by the use of longitudinal data.

The paper is concise and well-written, providing a detailed, clear and understandable description of the methods (e.g. how the transmission scores are calculated and what the rationale is). The visualizations (including the Supplementary figures) are very expressive and informative. Supporting information files have been submitted, and code and data have been made available on a GitHub repository.

I have very few critical remarks to make, I think the paper is rigorous and well-polished:

1) PRJEB28422 accession number does not exist on ENA (checked on Nov 27th). Did the authors mean PRJEB22368?

2) "Transmission scores were negatively correlated with genome size (ρ Spearman=-0.6), indicating that transmitted species generally had smaller genomes than non-transmitted ones" Any idea why this is the case?

3) "the fecal relative abundance of Fusobacterium sp. positively correlated with higher levels of transmission)" Why would this be the case?

Reviewer #2:

In this work, Schmidt et al., provide theoretical evidence for the transmission and colonization of oral microbial genomes in the distal gut. The results are interesting and important because they show that transmission of oral microbes to the gut occurs extensively in healthy individuals also in adulthood. Therefore, if these results are confirmed, oral-gut transmission might be an important factor to consider for the prevention and management of human diseases through the GIT microbiota.

We have a few major concerns that the authors should address to support their findings:

1) How were the cut-offs for vertical and horizontal genome coverage chosen? A 5% breadth of coverage seems low for the identification of microbial strains. Would the choice of these cut-offs affect the results? Indeed, Supplementary figure 4 shows that both vertical and horizontal genome coverage can affect the transmission score at least of some specific taxa. Please highlight the distribution of transmitters in this supplementary figure.

2) The authors base their work on the assumption that oral and gut SNVs profiles of transmitted genomes are more similar in an individual than between individuals. However, does this similarity of SNVs profiles necessarily imply transmission? Or, alternatively, could other individual-specific genetic and/or environmental factors shape a similar oral and gut microbiota in an individual instead of transmission?

3) As the authors use a low breadth of coverage and assume transmission based on similarity of SNVs profiles, we would like to ask that the authors confirm their results when using the ConStrains method to identify microbial strains (Luo et al., 2015). This method is also based on SNPs in oral and gut samples.

Reviewer #3:

This study entitled "Extensive Transmission of Microbes along the Gastrointestinal Tract" is an original work focusing on the transmission of bacterial strains between the oral and gut environment. The study is a robust analysis at strain-level of the oral and gut microbiota composition intra- and inter-individuals. The data are well exploited, especially regarding potential confounding factors between the different cohorts. The authors set out to identify population flow of bacteria from the oral cavity to the lumen. They defined metagenomes to an SNV-level resolution. The central thesis of this paper is that intra-individual overlap of SNVs between the oral cavity and the lumen is greater than that which would be expected from inter individual background thereby demonstrating oral taxa translocation. Within their model this event of translocation was a persistent one. The taxa identified as transmitted were phylogenetically diverse, yet some clade clustering was noted. The only noted characteristics of these taxa were reduced relative genome size and their anaerobic/ facultative aerobic nature.

This is a novel study with potentially significant ramifications for human intestinal microbial ecology.

My main critiques are these four points:

1) One of the pillar arguments in this paper is that the numbers of bacteria cells in the colon which show evidence of transmission, cannot be attributed to the passive translocation due to peristalsis. They argue that the amount of bacterial cells swallowed by a human per day (1.5*1012) would be depleted during passage through the upper digestive tract (stomach and duodenum) and thus would not contribute significantly to the gut microbiota. However, methodologically, the authors are investigating DNA not viable living cells. One might argue the authors have underestimated the contribution of passively translocated DNA (belonging to living or dead bacteria) to the faecal microbiota. The stomach and the mouth contain a high proportion of dead cells (perhaps only 1% of stomach bacteria cells are alive) whose DNA could translocate to the lumen. Given the estimates of an average person has 1 bowel moments a day (the cohort is older with disease so could be less), the average mass of stool to be 100 grams and the bacterial density in stool is estimated to be 0.9·1011 bacteria/g; an individual would pass 9x1012 bacterial cells a day. Presuming that an individual passes all the saliva they swallow a day in their bowel movement and there is no loss of bacterial DNA; One would detect ~1.5*1012 per stool. This would be above the 10% limit that the authors set. I think the authors should further expand on their estimations of quantities of bacterial cells in the lumen that can be attributed to salivary bacteria. The literature to which they reference in not primary work in essence and review. More solid numbers are needed when discussing the oral bacterial density and volume. Indeed, the focus of the Sender et al., 2016 paper is the colonic microbiota. I think their strong claims need stronger support. Likewise, the results presented in the study are not enough to support the following statement in particular "Approximately one in three salivary microbial cells colonise in the gut, accounting for at least 2% of the classifiable microbial abundance in feces".

2) The number of individuals reported in the text does not match the cohort and dataset overview presented in Figure 1. In the abstract and the main text, the authors reported the analysis of 470 healthy and diseased individuals but based on Figure 1 all together the cohorts comprised 571 individuals including 365 intra-individual couples. Further, the authors reported in the main text they they focused on a subset of 57 individuals for whom longitudinal data was available but based on Figure 1 only 46 individuals (including diseased individuals) presented time series. Then, for the case-control studies, the authors reported in the main text a total of 172 individuals but based on Figure 1 the cohorts CN-RA, FR-CRC and LU-T1D comprised 395 individuals including 219 intra-individual couples (healthy and diseased individuals). As a general comment, the authors should also clarify precisely in the main text whether the studied individuals are intra-individual couples (with both saliva and stool samples) or individuals with one sample type.

3) The authors profiled 310 prevalent species, which accounted for 99% of classifiable microbial abundance in both saliva and stool. However, there is no mention of the unclassifiable fraction of the reads, the proportion of classified over non-classified reads or the percentage of mapped reads.

4) The authors should acknowledge the difference between colonization of the lumen (faecal matter) versus colonization of the mucosa. Recent work by Zmora et al., 2018 on probiotics have highlighted the disparity between the colonization of the faecal matter versus the mucosa. I recognize they prepared the current submission before the Zmora paper came out. However, there are many other papers that make this point, at least with respect to faecal versus mucosa.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for sending your article entitled "Extensive Transmission of Microbes along the Gastrointestinal Tract" for peer review at eLife. Your article is being evaluated by three peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Wendy Garrett as the Senior Editor.

Reviewer #2:

We thank the authors for their work while revising their manuscript. The manuscript reads well, and we have only one additional comment concerning the correlations between average transmission scores and other parameters provided in the supplementary table.

We could reproduce the results (Results and Discussion section) for the correlations between transmission scores and prevalence_saliva (rho=0.6) as well as prevalence_gut (rho=0.05). However, there was a stronger correlation between average transmission score and prevalence_gut when accessing only the transmitters.

Additionally, strong correlations were observed for average transmission score and P/horizontal coverage for transmitters.

Can the authors comment?

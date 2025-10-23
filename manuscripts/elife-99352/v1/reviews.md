# Peer review - Round 1

Editors:
- Benjamin K Blackman, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.99352.3.sa0](https://doi.org/10.7554/eLife.99352.3.sa0)

Working with a diverse panel of rice accessions grown in field conditions, this valuable study measures changes in transcript abundance, tests for patterns of selection on gene expression, and maps the genetic basic of variation in gene expression in normal and elevated salinity treatments. The manuscript provides solid evidence that mean gene expression levels are further from the optimum abundance for more genes under the elevated salinity treatment compared to normal treatment, and that a relatively small number of genes are hotspots that harbor genetic variants which affect broader genome-wide patterns of natural variation in gene expression under high salinity conditions. However, the design, clarity, and interpretation of several statistical analyses can be improved, some opportunities for integration among datasets and analyses could yet be realized, and genetic manipulation is required to confirm functional involvement of any specific genes in regulatory networks or organismal traits that confer adaptation to higher salinity conditions. The manuscript will be of interest to evolutionary biologists studying the genetics of complex traits and a resource for plant biologists studying mechanisms of abiotic stress tolerance.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99352.3.sa1](https://doi.org/10.7554/eLife.99352.3.sa1)

The authors investigate the gene expression variation in a rice diversity panel under normal and saline growth conditions to gain insight into the underlying molecular adaptive response to salinity. They present a convincing case to demonstrate that environment stress can induce selective pressure on gene expression, which is in agreement with their earlier study (Groen et al, 2020). The data seems to be a good fit for their study and overall the analytic approach is robust.

(1) The work started by investigating the effect of genotype and their interaction at each transcript level using 3'-end-biased mRNA sequencing, and detect a wide-spread GXE effect. Later, using the total filled grain number as a proxy of fitness, they estimated the strength of selection on each transcript and reported stronger selective pressure in saline environment. However, this current framework rely on precise estimation of fitness and, therefore can be sensitive to the choice of fitness proxy.

(2) Furthermore, the authors decomposed the genetic architecture of expression variation into cis- and trans-eQTL in each environment separately and reported more unique environment specific trans-eQTLs than cis-. The relative contribution of cis- and trans-eQTL depends on both the abundance and effect size. I wonder why the latter was not reported while comparing these two different genetic architectures. If the authors were to compare the variation explained by these two categories of eQTL instead of their frequency, would the inference that trans-eQTLs are primarily associated with expression variation still hold?

(3) Next, the authors investigated the relationship between cis- and trans-eQTLs at transcript level and revealed an excess of reinforcement over compensation pattern. Here, I struggle to understand the motivation for testing the relationship by comparing the effect of cis-QTL with the mean effect of all trans-eQTLs of a given transcript. My concern is that taking the mean can diminish the effect of small trans-eQTLs potentially biasing the relationship towards the large-effect eQTLs.

Comments on latest version:

After the revision, the article has improved substantially. The authors have addressed most of my concerns and suggestions, except for testing the eQTL reinforcement/compensation relationship in the context of genetic architecture. I understand the motivation for testing this relationship at the gene level to determine whether it arises from directional or stabilizing selection, rather than examining it in a cis-trans pairwise fashion. However, I find the definition of this relationship unclear. The authors state in line 824 that "Genes were defined as compensating and reinforcing if they had at least 60% of individuals with opposite and same cis-trans allelic configuration, respectively." In contrast, if I understood correctly, the response to reviewers describes the relationship as reinforcing if the cis-eQTL effect is in the same direction as the mean effect of all the detected trans-eQTLs. I would request that the authors clarify their method of defining this relationship. Also, one should be aware of the fact that this relationship can evolve neutrally. Since there was no formal test performed to say it is otherwise, the authors might need to interpret the relationship carefully.

While the authors explain the possible factors that could lead to the trend of observing widespread genotype-dependent plastic responsse without significant genotype-dependent plasticity for fitness (L142), it is also important to consider the time axis. While filled grain serves as a proxy for fitness over time, gene expression profiles provide only a snapshot at a given time point. Therefore, temporal GxE dynamics may also play a role here.

Also, I am a little surprised by not mentioning anything about the code availability in this manuscript. I would request the authors to incorporate that in the revised version.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99352.3.sa2](https://doi.org/10.7554/eLife.99352.3.sa2)

In this work, the authors conducted a large-scale field trial of 130 indica accessions in normal vs. moderate salt stress conditions. The experiment consists of 3 replicates for each accession in each treatment, making it 780 plants in total. Leaf transcriptome, plant traits, and final yield were collected. Starting from a quantitative genetics framework, the authors first dissected the heritability and selection forces acting on gene expression. After summarizing the selection force acting on gene expression (or plant traits) in each environment, the authors described the difference in gene expression correlation between environments. The final part consists of eQTL investigation and categorizing cis- and trans-effects acting on gene expression.

Building on the group's previous study and using a similar methodology (Groen et al. 2020, 2021), the unique aspect of this study is in incorporating large-scale empirical field works and combining gene expression data with plant traits. Unlike many systems biology studies, this study strongly emphasizes the quantitative genetics perspective and investigates the empirical fitness effects of gene expression data. The large amounts of RNAseq data (one sample for each plant individual) also allow heritability calculation. This study also utilizes the population genetics perspective to test for traces of selection around eQTL. As there are too many genes to fit in multiple regression (for selection analysis) and to construct the G-matrix (for breeder's equation), grouping genes into PCs is a very good idea.

In the previous review, three major points were mentioned. The manuscript was modified, and here I briefly summarize them as a reference for future works:

(1) The separate sections (selection analysis, transcript correlation structure change, and eQTL) could use better integration.

(2) It would be worth considering joint analyses integrating the two environments together.

(3) Whether gene expression PCs or unique expression modules should be used in selection analyses.

Regarding whether to use PCs or WGCNA eigengenes to summarize gene expression for selection analyses, the authors reported that only a few WGCNA eigengenes were under selection, citing this observation as the rationale for choosing PC over eigengenes. However, as the relative false positive-negative rates of these choices likely require another dedicated study to explore, at this stage, it might be premature to state which method is better based on which gives more positive results. On one hand, one could easily imagine that plants screwed up by salinity have erratic genomewide expression and become extreme data points on the PCs, making the PCs a good proxy to correlate with fitness. On the other, it remains to be discussed whether this genomewide screwed-up-ness is what we want to measure in this study or whether we should focus on more dedicated gene modules instead. I suggest the authors acknowledge both possibilities. In this revision, I do not see relevant WGCNA results (as mentioned in the previous response letter) reported.

Figure 4: The observation that chlorophyll a content is under negative selection under BOTH conditions is a bit counterintuitive. The manuscript only mentioned "consistent with the general trend for reduced photosynthesis under salinity stress" (line 329) but did not mention why this increased fitness, even in normal conditions.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99352.3.sa3](https://doi.org/10.7554/eLife.99352.3.sa3)

The manuscript examines how patterns of selection on gene expression differ between a normal field environment and a field environment with elevated salinity based upon transcript abundances obtained from leaves of a diverse panel of rice germplasm. In addition, the manuscript also maps expression QTL (eQTL) that explains variation in each environment. One highlight from the mapping is that a small group of trans-mapping regulators explains some gene expression variation for large sets of transcripts in each environment.

The overall scope of the datasets is impressive, combining large field studies that capture information about fecundity, gene expression, and trait variation at multiple sites. The finding related to patterns indicating increased LD among eQTLs that have cis-trans compensatory or reinforcing effects in interesting in the context of other recent work finding patterns of epistatic selection. The authors have made some changes that address previous comments. However, some analyses in the manuscript remain less compelling or do not make the most from the value of collected data. Although the authors have made several improvements to the precision with which field-specific terminology is applied and to the language chosen when interpreting analytical findings, additional changes to improve these aspects of the manuscript remain necessary.

Selection of gene expression: One strength of the dataset is that gene expression and fecundity were measured for the same genotypes in multiple environments. However, the selection analyses are largely conducted within environments. Addition of phenotypic selection analyses that jointly analyze gene expression across environments and or selection on reaction norms would be worthwhile.

Gene expression trade-offs: The terminology and possibly methods involved in the section on gene expression trade-offs need amendment. I specifically recommend discontinuing reference to the analysis presented as an analysis of antagonistic pleiotropy (rather than more general as trade-offs) because pleiotropy is defined as a property of a genotype, not a phenotype. Gene expression levels are a molecular phenotype, influenced by both genotype and the environment. By conducting analyses of selection within environments as reported, the analysis does not account for the fact that the distribution of phenotypic values, the fitness surface, or both may differ across environments. Thus, this presents a very different situation than asking whether the genotypic effect of a QTL on fitness differs across environments, which is the context in which the contrasting terms antagonistic pleiotropy and conditional neutrality have been traditionally applied. The results reported do not persuasively support the assertion made in the response to reviewers that the terminology is reasonable due to strong coupling between genotype and phenotype. A more interesting analysis would be to examine whether the covariance of phenotype with fitness has truly changed between environments or whether the phenotypic distribution has just shifted to a different area of a static fitness surface.

Biological processes under selection / Decoherence: In the initial review, it was noted that PCA is likely not the most ideal way to cluster genes to generate consolidated metrics for a selection gradient analysis. Because individual genes will contribute to multiple PCs, the current fractional majority-rule method applied to determine whether a PC is under direct or indirect selection for increased or decreased expression comes across as arbitrary and with the potential for double-counting genes. A gene co-expression network analysis could be more appropriate, as genes only belong to one module and one can examine how selection is acting on the eigengene of a co-expression module. Building gene co-expression modules would also provide a complementary and more concrete framework for evaluating whether salinity stress induces "decoherence" and which functional groups of genes are most impacted. Although results of co-expression network analyses are now briefly discussed in the response to reviewers, the findings and their relationship to the PCA/"decoherence" analyses are not reported in the manuscript.

Selection of traits: Having paired organismal and molecular trait data is a strength of the manuscript, but the organismal trait data are underutilized. The manuscript as written only makes weak indirect inferences based on GO categories or assumed gene functions to connect selection at the organismal and molecular levels. After prompted by the initial reviews to test for correspondence between SNPs that explain organismal and gene expression trait variation or co-variance of co-expression module variation and trait variation, the response to reviewers indicates finding negative results. These findings should be included in the manuscript text and discussed.

Genetic architecture of gene expression variation: More descriptive statistics of the eQTL analysis have been included, although additional information about the variation in these measures within environments would be useful. The motivation for featuring patterns of cis-trans compensation specifically for the results obtained under high salinity conditions remains unclear to me. If the lines sampled have predominantly evolved under low salinity conditions, and the hypothesis being evaluated relates to historical experience of stabilizing selection, then evaluating the eQTL patterns under normal conditions provides the more relevant test of the hypothesis.

Lines 280-282: The revised sentence continues to read as an overstatement and merits additional revision with citations.

Lines 379-381: Following revision, it still remains unclear how the interpretation follows from the above analysis; the inference as written goes significantly beyond what may be specifically inferable from the result.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99352.3.sa4](https://doi.org/10.7554/eLife.99352.3.sa4)

Summary:

The researchers examined selection across multiple levels, including gene expression, biological processes, and regulatory mechanisms, with a particular focus on comparing selection between different environmental conditions. They further explored potential evolutionary mechanisms. This is made possible with a comprehensive dataset comprising gene expression data from 130 accessions with three replicates collected in two environments in the field, genomic data from 125 genotypes, and associated physiological traits. The findings have significant implications for understanding the evolution of stress adaptation, and the identified possible genes and pathways for further investigation.

The researchers began by focusing on the selection of gene expression across two environments, comparing the number of genes under selection and the effect sizes, as well as examining how selection in each environment acts on the same individual genes. They then expanded their analysis to consider selection in biological processes, investigating the relationships between selection acting on individual genes within processes and selection acting among different processes.

Additionally, they explored selection at the organismal level by examining traits.

The study further transitioned from analyzing individual gene expression to investigating gene-gene interactions. They briefly examined correlation variation among gene pairs between the two conditions, identifying pairs with rewired interactions that suggest potential selection on gene regulation or the effect of rewiring on tolerance. The researchers then delved into the genetic architecture underlying these patterns by mapping eQTLs. Their comparison of cis- and trans-eQTLs revealed that trans-eQTLs were more variable across conditions. Notably, they identified hotspots representing master regulators that possibly underlie the greater variability of trans-eQTLs across environments. They further discovered that trans-eQTLs are generally under purifying selection (particularly in salt conditions), while cis-eQTLs are under balancing selection, exhibiting higher nucleotide diversity. As for how cis- and trans-eQTL effects combine at the level of individual genes, more are found to be reinforced and the hypothesis of genetic fixation on cis- and trans-eQTL effects combination is further tested.

Strengths:

A key strength of this study is its comprehensive approach, extending beyond the analysis of gene expression to include gene-gene interactions, genetic architectures, and selections of genetic regulation factors. The exploration of gene expression selection through its connection with fitness, as introduced in the researchers' previous work, provides valuable insights into the role of gene expression in adaptation. The study investigates selection across multiple levels of biological responses, including individual gene expression, genes associated with biological processes, gene-gene interactions, and the underlying genetic architecture. The experimental design enables a direct comparison of selection between control and salinity conditions, which sheds light on the effects of stress on selection and the dynamics of adaptation to stress. Additionally, the manuscript is well-written, with a clear connection to current literature. The discussion effectively integrates findings with broader implications, making it a satisfying read.

Weaknesses:

The lack of formal testing for environment-specific selections (e.g., selection of gene expression specifically in salinity stress, PCs, or traits) is a major limitation, as previous reviewers have flagged. Explicit tests of eQTLs variation between conditions are introduced, so similar formal tests should also be introduced in selection sections. For example, a formal test of selections of gene expression might be helpful to solve variance/mean- standardization concerns between two environments.

Additionally, some aspects of the analysis appear somewhat arbitrary and could benefit from further sensitivity testing. Line 203: The concern about bias in detecting more CN than AP, as mentioned by the authors and previously flagged by reviewers, does not seem fully resolved with the current methods given the arbitrary cut-off. Incorporating additional tests suggesting the conclusion is insensitive to the cutoff would be very helpful. Similar is the classification of genes into compensatory and reinforcing categories based on 60% of individuals as a cutoff.

While this study focuses on gene regulation, its connection with the selection of gene expression and biological pathways is not well integrated. In particular, the discovery of eQTLs is not explicitly linked to gene expression selection or biological pathways, leaving this relationship underexplored. Suggestive comments: Currently the summarization of selection is based on eQTLs. It would be interesting to also summarize the selection patterns identified from previous sections based on genes being cis/trans-regulated. Moreover, it might be interesting to see if there is more loss or gain of eQTLs under salt stress and their functions. The current results mentioned variations of eQTLs but not clear if they are loss or gain. E.g., one way is to identify genes related to cis and trans-eQTLs and see their correlation changes with genes being regulated using CILP (also as a way to informatively narrow down gene pairs for CILP).

Similarly, the section on selection at the organismal trait level appears disconnected from the rest of the analysis (e.g., if it is not tested to be related to other features, mentioning why it might not be related would be helpful). Admittedly, the discussion of how biological processes discovered at different levels integrate together is helpful.

Other comments: given there is no comparison between loss of coherence (correlations) and gain of coherence under salinity stress to show the dominant role of decoherence, maybe need to also discuss the genes and processes related to the gain of coherence? This is because the understanding of activation (gain of coherence) of some regulations/processes under stress conditions could also be interesting. It is not clear if decoherence (e.g., lines 293-296) refers to significant correlation changes or just loss of the correlation in salinity stress.

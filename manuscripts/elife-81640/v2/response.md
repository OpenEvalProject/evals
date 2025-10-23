# Author response - Round 1

Authors:
- Lijiang Long ([ORCID: 0000-0002-9897-5900](https://orcid.org/0000-0002-9897-5900))
- Wen Xu ([ORCID: 0000-0003-2085-7223](https://orcid.org/0000-0003-2085-7223))
- Francisco Valencia
- Annalise B Paaby ([ORCID: 0000-0003-1422-047X](https://orcid.org/0000-0003-1422-047X))
- Patrick T McGrath ([ORCID: 0000-0002-1598-3746](https://orcid.org/0000-0002-1598-3746))

## Response text

DOI: [10.7554/eLife.81640.sa2](https://doi.org/10.7554/eLife.81640.sa2)

Essential revisions:

1) All reviewers noted the lack of controls for the peel-1 edited strain. I believe that backcrossing and whole-genome sequencing will not adequately address the concerns about the modest peel-1 effect and the single CRISPR-edited allele. The authors should either generate another peel-1 edited strain and test this new strain in the same experiments or add back peel-1 to the deleted strain to show that the modest peel-1 effect goes away.

2) Please update the statistical tests to address issues of multiple testing and non-normality.

3) The N2 data in Figures 2 and 3 are repeated. Please note that point.

4) Many of the other reviewer comments can be addressed by toning down some claims and providing more caveats and/or explanations. Reviewers made good suggestions for how to respond to these comments.

We appreciate the reviewers time and attention in reviewing our manuscript. We agree with their critiques and have addressed their major criticisms. Some of the main changes to the paper (marked in tracked changes):

1. There was significant worry that the conclusions relied on a single CRISPR-edited strain. Due to the small effect sizes, background effects or protein truncations could be responsible for the observed difference in fitness in the peel-1 knockout strain. To address this, we created 6 new CRISPR-edited strains. Two of these strains reversed the knock out allele back to wild-type, which would leave the background mutations intact. These two new strains showed decreased fitness from the original peel-1 allele, indicating that this peel-1 allele was responsible for the fitness differences we observed vs. nonspecific background mutations. We also generated four additional loss of function alleles of peel-1 in the first 3 amino acids of the protein. These loss-of-function mutations also showed decreased fitness from N2, further supporting our hypothesis that the fitness differences were from peel-1 effects and not background mutations. These alleles also demonstrate that the fitness difference was not due to the expression of the translation of a partial PEEL-1 protein product. This data can be found in a new Figure 4.

2. We have updated the statistics to account for multiple testing and non-Guassian effects. For the fitness experiments, we modified the statistical test to determine if the fitness of one strain was significantly different from the second strain in a non-parametric way. This approach took advantage of the large number of comparisons we did for the competitions that had a small effect. The complete approach is detailed in the methods.

3. We have made a number of changes to address these specific comments of the reviewers:

a. We have updated nomenclature of genetic elements and strains as suggested by reviewers.

b. We have added references as suggested by reviewers.

c. We have deleted the line about discovery of these elements in obligate outcrossing nematodes (we agree that they many obligate male/female species have not been studied).

d. We have removed the effects of zeel-1 from the manuscript (we agree that our initial conclusions about the role of zeel-1 were incorrect).

e. We added a line to make it clear that our results suggest that additional natural polymorphisms linked to peel-1 also affect laboratory fitness (as the NIL has a much stronger effect that the engineered peel-1 strains).

f. We have removed the Sivasundar reference and added a review that further supports the low outcrossing rate. We have made explicit the carrying costs as suggested by reviewer 3.

g. We have removed PTM573 from the paper.

h. We have indicated where the data was shared between different figures.

4. We unfortunately do not have the detailed egg-laying rates for each strain to further analyze. While the experiments suggested by Reviewer 3 would be interesting, we believe they are outside of the scope of the paper (short report). Re Reviewer 4’s comments on starvation, differences in their response also could play a role in the laboratory fitness. Teasing out the exact contribution of egg-laying, growth, dauer formation, starvation, etc would be laborious.[Editors’ note: what follows is the authors’ response to the second round of review.]

Reviewer #2 (Recommendations for the authors):

1. While the authors have addressed the major criticisms that focused on the genetics and reproducibility of the peel-1 mutant effect, there are some aspects of their fitness assays that remain unclear at the moment and would be important to clarify. The results shown in panel Figure 4D are central to the interpretation of the main claim of this paper, yet several questions come into mind upon close inspection, for instance:

1.1 Why is the data coming from independently generated alleles of the same genotype combined? Looking at the source data, it would appear that the authors replicated each pair-wise competition assay 6 times. However the data originating from independent alleles were combined in the final plots. As a result, the wt control and the original peel-1 mutant allele (kah126) have 6 replicates each, whereas other conditions, like the peel-1 "revertant" mutants and "new" peel-1 mutants have 12 and 18 replicates, respectively. I find it a bit troublesome that the fitness estimations are being done by aggregating independently derived lines (which goes against the original purpose of having independent alleles).

– The data for the different lines can be separated and reported.

We revised our presentation of these results to include comparisons within and among the independently derived alleles. Our results now show that all independently derived but identical alleles are equivalent to each other in the competition assays, and further, that all three allele classes of the peel-1 mutants are equivalent to each other. Figure 4D has been updated to display the replicate lines separately, and the text has been updated to describe our analysis in finer detail.

1.2. Although it was brought up by a reviewer in the first round, it appears that there is no information available on the timing of the competitive fitness experiments. Were the experiments performed in parallel? And if not, when exactly? (this is important information for readers that should be available in the methods section/supplement).

– Please answer this question by adding text to the Methods.

Added ‘Pairwise competition assays in figure 2 and figure 3 were done in parallel with the same start date. The competition assays in figure 4 were performed parallel with a different start date.’ to the method section.

2. I think it would be very important to check that the phenotype of the new peel-1 lines (new mutant alleles and revertant) is also consistent when measuring the total number of offspring laid by hermaphrodites (see Figure 3C)

– Without these data, the authors can mention that this trait was not measured for all of the peel-1 lines.

We added this line (195).

3. The authors may want to reconsider or justify the use of the term "biological role", for example as used in line 196

"These experiments strongly support a biological role for peel-1. "

I find the use of the term "biological role" very confusing in this context because it implies that the role of peel-1 as a toxin (or that of selfish elements in general) is "non- biological". Maybe the authors refer to a "physiological role" (not perfect either but more accurate)?

– Please edit to a different term. All genes have biological and physiological roles. Maybe "fitness-relevant role"?

Changed in this line and in the conclusion.

Overall, this is a very exciting and interesting result and the manuscript has been greatly improved. Yet, many questions still remain open (which is OK if this is intended to be only a short report). How would a protein that is only expressed in sperm delay the development of hermaphrodites? Does this effect depend on zeel-1? Are the two opposing roles of peel-1 independent? (in other words, can one isolate mutants that abrogate toxicity but not the effect on fitness and vice versa). Does the benefit of carrying peel-1 evolved before or after the toxicity? Is there balancing selection and what is the selective force?

– Depending on space in the Discussion, some or all of these points can be addressed.

We added an additional paragraph at the end of the Results to address these points.

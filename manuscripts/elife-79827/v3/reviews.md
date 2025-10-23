# Peer review - Round 1

Editors:
- Emilia Huerta-Sanchez, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79827.sa0](https://doi.org/10.7554/eLife.79827.sa0)

This study leverages genetic and linguistic data from the islands of Cabo Verde, and provides a valuable example of how genetic ancestry patterns vary across admixed populations due in part to their unique local history and social practices of that time. The empirical and computational analyses supporting the claims of the authors are solid, and the tools developed will be useful for the study of genetically admixed individuals. The work will be of interest to human evolutionary biologists and anthropologists.


---

# Peer review - Round 1

Editors:
- Emilia Huerta-Sanchez, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79827.sa1](https://doi.org/10.7554/eLife.79827.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The admixture histories of Cabo Verde" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Emilia Huerta-Sanchez as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Molly Przeworski as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Xinjun Zhang (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Both reviewers enjoyed reading the paper and found the results of this study to be important as it provides insights into how admixture shapes patterns of genetic variation. Both reviewers would like to see a revised version of the manuscript. There were some clarifications and a few additional analyses that the reviewers feel could strengthen the paper. These include:

1) The authors infer demographic history using a previously developed method (meTHIS), and it would be great to see the model robustness when fixed parameters are misspecified: the ancestral population sizes, recent gene flow between Europeans and Africans (eg. back-to-Africa migrations), and the possibility of population size fluctuation in Cabo Verde in recent history (or at least, more evidence to justify a continuous population growth).

2) The authors suggest that longer ROH in one ancestry implies more admixture; is a higher proportion of admixture the only way to generate these ROH patterns (instead of a severe bottleneck in the ancestral population)?

3) Revealing that different island populations in Cabo Verde have different admixture histories provides support for variation in the way in which these islands were founded. The authors propose a set of interesting hypotheses for how the different islands were founded; could the authors use simulations to see if there is some support for these hypotheses?

4) The authors could motivate why they chose the methods applied to the data.

5) Please review and respond to the individual reviewer comments as well.

Reviewer #1 (Recommendations for the authors):

Line 333: "thus illustrating the strong signal of genetic isolation-by-distance (51) within Cabo Verde at very reduced geographical scales." Is this consistent/similar with what is observed for other island populations?

Line 335: It will be helpful for readers to include the definition of "utterance" in the main text.

Figure F6: What is h?

Methods:

Line 856: "We collapsed the local ancestry assignments for each SNP in each Cabo Verdean individuals hence obtained into" I didn't get what "collapsed" means in this context. Also, I thought that RFmix has a phasing step, so the phase that is given as input may be different from the phase it infers. So how do the authors deal with regions that are heterozygous in ancestry (e.g. one chromosome is African and the other is European) with their calls of runs of homozygosity for their ancestry-specific ROH sizes?

Line: 916: "we first design MetHis v1.0 (37) forward-in-time simulations of four competing" Could the authors say more about their forward-in-time simulations? Are these simulations created by the authors? It seems the authors are using real data. How did the authors make 20000 haploid genomes from the Mandinka and IBS who have really small sample sizes? Could they say more here to explain how these forwards in time simulations are different than what we typically use (e.g. SLIM)? The real data is not sequencing data, so how did the authors recreate that in the simulations? I assume that might affect their ROH calling and ancestry calling?

Reviewer #2 (Recommendations for the authors):

There are a number of areas where the paper can improve and strengthen.

Specific revision suggestions:

1) Title: the current title "the admixture histories of Cabo Verde" is underwhelming and does not capture the main findings of the paper. The authors can consider a different title that reflects the admixture history reconstructed by revealing the co-shifting of genetic and sociocultural diversity, which is storytelling about TAST.

2) The genetic relationship analyses

a. the authors used MDS to draw relationships between Cabo Verdeans and other European and African continental populations. I am not an MDS expert (nor do I expect the general audience to be), and it is not clear to me why ADS-MDS is used here instead of a traditional PCA in pair with classic admixture statistical tests such as F statistics. Do we learn anything new from ADS-MDS that PCA and F stats can't tell us? Would like to see more explanation and justification in the text. It would also be helpful to include F statistic tests and how they compare to the MDS results, at least in the Supplementary Figures.

b. Could the authors comment on the proportion of missing data in the genotypes, and whether the removal of them is expected to change MDS results in any way?

c. Furthermore, I find Figure F2 very hard to read as I need to constantly scroll back to Figure F1 for color legends – the authors should consider either (1) adding legends to Figure F2, or (2) merging Figure F1 and F2 as the same figure, highlighting the current Figure F2 panel A-C in the context of geographical locations in Figure F1, and move the other panels to Supplementary Figures.

3) Admixture analysis:

a. In Verdu et al. 2017 Current Biology, the authors performed similar MDS and ADMIXTURE analyses and made similar conclusions on Cabo Verdeans being related to Senegambians and Southern Europeans. What new information are we learning from here? Are we only confirming the previous observations on all CV islands? In any case, if there are novel discoveries from here that I am missing from reading the text, the authors should at least consider clarifying and re-emphasizing the messages.

b. For the ADMIXTURE analysis, could the authors explain the justification for choosing the maximum value of K=10? What would the plot look like when K is larger?

c. The authors mentioned that Asian populations are being compared with Cabo Verdeans in the admixture analyses, but I don't see them being displayed on the plot (Figure F3) – in general, is there any evidence there's ancestry contribution in CV from populations outside of Europe and Africa? How would the admixture plot look like when other worldwide populations are included?

4) ROH and local ancestry inference

a. What are the proportions of long ROHs among all ROHs in these island populations?

b. The authors interpreted the finding of more long-ROHs exclusively in one ancestry as essentially an increase in admixture proportion from the respective source population, either through recurring admixtures or relatively recent admixture events. However, I wonder if two source populations contributed equally to the admixture, but one source experienced more bottleneck themselves and therefore carry more long-ROH in the first place, would that lead to the enrichment of long ROHs in that ancestry? Could the authors run some simulations to test whether alternative model(s) (eg. different ancestral population sizes, admixture proportions and times, etc.) could lead to a similar distribution of long ROH and their overlapping with respective ancestry?

c. Additionally, I wonder if the long ROHs in these island populations are enriched in low recombination regions or functionally important regions. And if so, would the authors expect any of such factors could affect the distribution of ROHs and the interpretations thereafter? Furthermore, how would the authors expect the difference in fine-scale recombination rate (and mutation rates) between Africans and Europeans possibly affect the ROH and ancestry distributions?

d. For Figure F4D – it's a bit hard to read the differences here as these violin plots appear uniformly distributed across populations despite slight differences. For example, is the overrepresentation of ancestries in certain populations significant, such as European contribution in Fogo and Brava and African contribution in Sal and Sao Vicente? Could the authors provide some p-values here?

e. Line 358-359: why is it surprising to find that individuals from distant islands differ in African admixture level if we already see that their ADMIXTURE-revealed ancestry components differ between islands?

5) Estimation of admixture history

a. From what I see, the RF model considers many admixture-related parameters but doesn't consider the evolutionary history in the source populations before 20 generations ago. Can the authors comment on how robust the RF model is to demographic model misspecifications, especially related to the ancestral population size in the source populations? Most importantly, are the ABC posteriors sensitive to the demographic parameters that are fixed in the simulations?

b. For the recipient population, the population sizes are projected to be increasing over the 20 generations in all 4 admixture scenarios – is that realistic according to the historical record? Was there any reduction in Ne in Cabo Verde islands during the TAST? How is the inference robust to alternative models where the admixed population's size fluctuates over time?

c. Also, would the historical gene flows between Southern Europeans and Northern Africans and within Africa (eg. Moorjani et al. 2011 Plos Genetics; Busby et al. 2016 eLife; Botigue et al. 2013 PNAS) confound the inference of admixture history?

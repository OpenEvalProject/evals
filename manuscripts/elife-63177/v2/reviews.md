# Peer review - Round 1

Editors:
- Molly Przeworski, Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63177.sa1](https://doi.org/10.7554/eLife.63177.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper presents a new method for identifying regions of the genome on which natural selection has acted following recent population admixture. The authors apply it and other approaches to document that the Duffy null allele, which confers resistance to the malaria pathogen Plasmodium vivax, has been under strong positive selection in populations of the Cabo Verde of mixed African and European ancestries. The method should be broadly applicable and the specific example is a notable contribution to the understanding of how admixture can enable rapid adaptations

Decision letter after peer review:

Thank you for submitting your article "Rapid adaptation to malaria facilitated by admixture in the human population of Cabo Verde" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Bavesh Kana as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Fernando Racimo/Graham Gower (Reviewer #2); George Busby (Reviewer #3).

The three reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. They all agreed that a finding of selection on Santiago but not the other two islands provides a nice example of parallel selection on malarial resistance in the recent human past, complementing findings for other African locations. Moreover, they appreciated the development of a new statistical approach to detect selection since population mixture. However, there were a number of concerns raised about the test and its application, as well as some other analyses, and a general feeling that more extensive analyses and explorations of the test performance were needed to build a strong case.

Summary:

This paper reports on selection for the Duffy null allele since humans of African and European ancestry colonized the Cape Verde Islands (~20 generations ago). The Duffy null allele is quasi-fixed in sub-Saharan Africa and confers resistance to P. vivax, which was apparently a stronger selection force on one of three islands (Santiago). The authors also document an effect of selection at one locus on genome-wide ancestry (as previously reported by Pierron et al., 2018, cited).

Essential revisions:

1) The new statistical test and its application

i) Most results in the manuscript rely on the phase imputation and local ancestry assignment described here. However, no discussion is given to how errors in the phase-imputation or local-ancestry assignment might influence results (such as calculation of the DAT and iDAT statistics). If any Cabo Verde individuals carry recent ancestry from non-African and non-European sources, what effect might that have on local-ancestry assignment? Was any attempt made to identify such individuals, or verify that none exist in the dataset?

ii) "[W]e calculated iDAT only for distances where DAT>=0.25" One wonders if this choice was made for a specific reason---such as to ensure fairer comparisons across differently-sized chromosomes? For instance, if the DARC locus were instead found on chr22, the ancestry-tract-length distributions might be severely truncated. Some more analyses related to the choice of input parameters to the iDAT scores would help make this statistic more widely applicable and robust to other scenarios, beyond the one studied in this paper. A discussion of when this statistic might be more or less appropriate (could it work with older selection scenarios) would also be a nice addition.

iii) Does the DARC locus show any other selection signals that are not dependent on local ancestry assignments? If not, that would be a good way to further support the use of the iDAT score (in this paper and future studies), in that it could be particularly sensitive to recent selection signals that might not be picked up by other methods. Are there extended haplotype homozygosity signals in the region as well?

iv) Do the authors account for subsequent recent migration from Africa/Europe? Could subsequent pulses of African ancestry explain the observed selection signals? If there has been significant recent migration from Africa into Santiago from Africa, then this will have brought African DARC haplotypes into the population, and driven up the overall West African ancestry proportions. Is this accounted for by the DAT standardisation.

v) There is more African ancestry in general on Santiago c.f. Fogo and the NW Cluster. Indeed, the ancestry proportions on Fogo/NW Cluster are approaching 50/50 African/European. Assuming (as the authors do) that this reflects similar ancestry proportions to the initial source groups, is there power to detect local ancestry change when the ancestries are in roughly similar proportions? Is it possible to delineate what ancestry proportions are best suited to this method? e.g. these power calculations on iHS in Figure 2 from Voight et al., (2006)

vi) How do differences in fine-scale recombination rates between African and European populations affect the test? Perhaps they could define the haplotype length for iDAT in population-specific genetic distance (e.g., using the map from Hinch et al., 2011)?

vii) Are the p-values for iDAT well-calibrated across Fst values? In that regard, and more generally, it would be helpful to see the performance of iDAT for some simulations with real present-day African genomes and European genomes at the estimated starting admixture fractions, in which individuals are mixed and recombination operates in a neutral scenario for 20 generations.

viii) Given the hypothesis that selection should have affected Santiago but not the two other islands, the authors should show that a significant iDAT test is *not* seen for the other two islands.

2) Other targets of selection

i) There are a few other peaks in the selection scan that are not discussed in the text. It would be interesting to see what genes these peaks overlap with and if they have anything to do with the response to malaria; in particular, to explore if the genome-wide ancestry shift is solely due to the DARC locus, or whether other malaria-response alleles could be driving the shift as well.

ii) Are the authors able to estimate whether there has been more selection on African ancestry tracts compared to European tracts? For example, if you sum the iDAT values across the genome, are the results +ve, -ve or 0? If it's -ve, might this be additional evidence that African ancestry has been favoured, over and above being around the DARC locus?

3) Effect of ancestry on other chromosomes

This point is very interesting but hard to understand from what is shown. To see it more clearly, it would be helpful to show the ancestry proportions at Duffy and around it for chromosome 1 versus for the rest of the genome. Moreover, the results of simulations (Figure 4B) are confusing, as it seems counter-intuitive for the effect to be weaker for chr 1 alone than for the whole genome; what might be more readily interpreted is the increase in admixture proportion for chr 1 alone vs for the other 21 autosomes. It would also be important to simulate a single admixture event rather than continuous migration, to evaluate if it would make a difference to the findings.

4) Application of SWIF(r)

It was unclear from the description if the simulations of sweeps on which they trained were of selection in the right demographic setting (i.e., since admixture at appreciable frequency) or using standard sweep from a new mutation in a constant size, random-mating population. If the latter, then the training set for sweeps is not the right one, and the precision recall not informative about the actual problem (which is to distinguish neutral admixture from admixture followed by selection on an allele of one ancestry). On a more minor note, why train on only 100 sweep simulations?

5) The following paper should be cited and discussed: https://www.biorxiv.org/content/10.1101/205252v2

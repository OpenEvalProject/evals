# The evolution of non-reproductive workers in insect colonies with haplodiploid genetics

## Authors

- Jason W Olejarz<sup>1</sup>
- Benjamin Allen<sup>1</sup>
- Carl Veller<sup>1</sup>
- Martin A Nowak<sup>1</sup> †

### Affiliations

1. Program for Evolutionary Dynamics Harvard University Cambridge United States
2. Center for Mathematical Sciences and Applications, Harvard University Cambridge United States
3. Department of Mathematics Emmanuel College Boston United States
4. Department of Organismic and Evolutionary Biology Harvard University Cambridge United States
5. Department of Mathematics Harvard University Cambridge United States

† Corresponding author

## Abstract

10.7554/eLife.08918.001 Eusociality is a distinct form of biological organization. A key characteristic of advanced eusociality is the presence of non-reproductive workers. Why evolution should produce organisms that sacrifice their own reproductive potential in order to aid others is an important question in evolutionary biology. Here, we provide a detailed analysis of the selective forces that determine the emergence and stability of non-reproductive workers. We study the effects, in situations where the queen of the colony has mated once or several times, of recessive and dominant sterility alleles acting in her offspring. Contrary to widespread belief based on heuristic arguments of genetic relatedness, non-reproductive workers can easily evolve in polyandrous species. The crucial quantity is the functional relationship between a colony’s reproductive rate and the fraction of non-reproductive workers present in that colony. We derive precise conditions for natural selection to favor the evolution of non-reproductive workers. DOI: http://dx.doi.org/10.7554/eLife.08918.001

## Introduction

Eusociality is a form of social organization where some individuals reduce their own lifetime reproductive potential to raise the offspring of others (Wilson, 1971; Crespi and Yanega, 1995; Gadagkar, 2001; Hunt, 2007; Nowak et al., 2010). Primary examples are ants, bees, social wasps, termites, and naked mole rats. There have been ~10–20 origins of eusociality, about half of them in haplodiploid species and the other half in diploid ones (Andersson, 1984). A crucial step in the origin of eusociality is cancellation of dispersal behavior (Abouheif and Wray, 2002; Nowak et al., 2010, 2011; Hunt, 2012; Tarnita et al., 2013). Individuals who stay at the nest begin to work at tasks such as care of the young, defense of the nest, and foraging behavior. Eusociality can evolve if the strong reproductive advantages of the queen, including reduced mortality and increased rate of oviposition, arise already for small colony sizes (Nowak et al., 2010).

Haplodiploidy is the sex-determination system of ants, bees, and wasps. With haplodiploidy, females arise from fertilized eggs and are diploid. They have two homologous sets of chromosomes, one padumnal (paternally inherited) and one madumnal (maternally inherited). Males arise from unfertilized eggs and are haploid. They have one set of chromosomes, which is madumnal. With haplodiploid genetics, mated females can become queens and lay female and male eggs. In many cases, unmated females become workers, which can lay male eggs but not female eggs. Therefore, in a haplodiploid colony, male eggs could come from the queen or from the workers. This creates intracolony competition between the fertilized queen and the unfertilized workers over the production of males. In this paper, we investigate genetic mutations that affect the phenotype of the workers and make them non-reproductive (or sterile). We calculate conditions both for the evolutionary invasion and evolutionary stability of such mutations.

The typical theoretical approach for investigating the evolution of non-reproductive workers makes use of coefficients of relatedness. Relatedness of one individual to another is the probability that a random allele in the former is also in the latter due to recent common ancestry. In particular, there are three coefficients of relatedness that are of primary interest (Hamilton, 1964; Trivers and Hare, 1976). First, consider the relatedness of a female to one of her sons, Rson. In parthenogenetically producing a son, a diploid female transmits a haploid genome to him. Under Mendelian segregation, each allele in her genome has probability 1/2 of inclusion in this transmitted haploid complement, and so Rson = 1/2. Next, consider the relatedness of a female to one of her brothers, Rbrother. The female and her brother share a mother, and so the probability that an allele inherited maternally by the female is the same allele as inherited maternally by her brother is 1/2. On the other hand, the male has no father, and so there is no chance that an allele in the female is equivalent to one in her brother through paternal inheritance. A random allele in the diploid female has equal chance of being padumnal or madumnal, and so Rbrother = (1/2)(0) + (1/2)(1/2) = 1/4. Finally, consider the relatedness of a female to one of her sisters, Rsister. This coefficient of relatedness depends on the number, n, of different males that the queen mates with before laying eggs. For a padumnal allele in a female to be identical, by paternal descent, to that in a sister requires them only to share the same father (probability 1/n), since that father is haploid and therefore always transmits the same allele. Sisters share a mother, and so the probability that an allele inherited maternally by one female is the same allele as inherited maternally by her sister is 1/2. Therefore, Rsister = (1/2)(1/n) + (1/2)(1/2) = (2 + n)/(4n).

The traditional investigation of evolution of non-reproductive workers uses the following relatedness-based heuristic. The relatedness of a female to her male offspring is Rson = 1/2. If the queen mates with only a single male (n = 1), then the relatedness of a female worker to one of her random sisters is Rsister = 3/4 > Rson. The naive conclusion is that worker altruism should readily evolve, because a worker can more efficiently spread her genes by raising her sisters. This conjecture is known as the ‘haplodiploidy hypothesis’ (Hamilton, 1964, 1972). If the queen mates with more than two males (n>2), then Rsister < Rson. Now the preference of an unfertilized worker is reversed, because she has a higher relatedness to her own male offspring than to one of her random sisters. These old arguments suggest that queen monogamy and haplodiploid genetics synergistically act as a driving force for the evolution of worker altruism (Hamilton, 1964, 1972).

But worker-laid eggs do not compete only with queen-laid female eggs. The high relatedness of a female to her sisters in Hymenopteran colonies is cancelled by the low relatedness of the same female to her brothers (Trivers and Hare, 1976). In a colony with a singly mated queen, the relatedness of a worker to a sister is Rsister = 3/4. But the relatedness of a worker to a brother is only Rbrother = 1/4, regardless of the number of times the queen mates. So, when a worker female helps her queen reproduce, she aids in the production both of sisters (to whom she is highly related) and brothers (to whom she is not). In the relatedness-based argument, these effects exactly cancel each other out, and so the unusually high relatedness of sisters in eusocial colonies cannot be the simple solution to the puzzle of worker altruism that it was once thought to be (Trivers and Hare, 1976). This is true even when the population sex ratio is female-biased, because when more reproductive females are produced than males, the average reproductive success of a female is lower than that of the average male exactly in proportion to their relative abundances (Craig, 1979).

More recently, it was proposed that each eusocial lineage must have passed through a ‘monogamy window’—a period of evolutionary history in which queens were singly mated (Boomsma, 2009). This argument assumes that worker-laid eggs compete equally with queen-laid female and male eggs. If the queen is singly mated (n = 1), and if the colony’s sex ratio is 1/2, then a worker has an average relatedness to siblings (sisters and brothers) of (Rsister + Rbrother)/2 = ((3/4) + (1/4))/2 = 1/2. Relatedness of a worker to her son is also Rson = 1/2. In this case, assuming that worker-laid eggs substitute equally for queen-laid female and male eggs, the argument suggests that any infinitesimal benefit of non-reproductive workers to colony productivity should lead to evolution of worker altruism. If queens mate more than once (n≥2), then the average relatedness of a worker to a random sibling falls below 1/2, and evolution of worker altruism is supposed to be strongly disfavored (Boomsma, 2009).

There also exist hypothetical scenarios in which the relatedness values of a female to a random sister and a random brother would not cancel (Trivers and Hare, 1976): for example, the sex ratio could vary from colony to colony, while the average sex ratio in the population remains at 1/2. Evolution of helping might then be expected in the female-biased colonies (Trivers and Hare, 1976). Some recent papers (Gardner et al., 2012; Alpedrinha et al., 2013) examine this case of split sex ratios and also question the importance of haplodiploidy for the evolution of helping. Based on their analysis, the authors conclude that haplodiploidy can have either a positive or negative influence on the evolution of helping depending on colony variables, and they determine the effect of haplodiploidy on the evolution of helping to generally be small. But they claim, in agreement with Boomsma (2009), that monandry is a key requirement for the evolution of a worker caste. They argue that, in the case of lifetime monogamy, “any small efficiency benefit from rearing siblings (b/c > 1) would lead to helping being favored by natural selection.” (Gardner et al., 2012)

In this paper, we investigate the situation where worker-laid male eggs compete directly with queen-laid male eggs. In other words, there are two types of reproduction events to consider: A worker can lay a male egg, or, instead, the queen can lay a male egg while the worker helps to raise the queen’s male egg. In either case, a male is produced. Thus, the sex ratio of the colony is unaffected by which of these two strategies is realized. The reproductive competition between the queen and the workers is only over the male offspring. (We do not assume that the sex ratio is equal to 1/2; we only assume that it is independent of the fraction of worker-produced males.) This possibility represents the simplest scenario for studying the evolution of non-reproductive workers and is biologically plausible (Winston, 1987; Sundstrom, 1994; Sundstrom et al., 1996; Queller and Strassmann, 1998; Hammond et al., 2002). Once this case is understood, subsequent analysis can consider the situation where both the fraction of worker-produced male offspring and the colony’s sex ratio vary at the same time.

The relatedness of a worker to her male offspring, Rson = 1/2, is always larger than the relatedness of a worker to a brother, Rbrother = 1/4. Thus, if worker-laid male eggs compete primarily with queen-laid male eggs, then relatedness-based arguments might predict that worker altruism should not evolve with any number of matings of the queen unless non-reproductive workers provide some benefit to the colony.

We study a model of competition between worker-laid and queen-laid male eggs that incorporates both haplodiploid genetics and a variable number of matings of the queen. Specifically, we analyze the selection pressure acting on the emergence and stability of non-reproductive workers in situations where the queen has mated once or several times. Our model assumes that the evolution of sterile workers has a negligible effect on the sex ratio of a population, which allows us to isolate and identify the specific selective forces. We derive exact conditions for the invasion and stability of non-reproductive workers.

## Model

We study the evolution of a non-reproductive worker caste in the context of haplodiploid genetics, where females are diploid and males are haploid. Virgin queens can mate with one or several males. The parameter n denotes the number of matings of the queen. Unfertilized workers help raise the offspring of the queen, but they can also lay male eggs.

We analyze the conditions under which a wild-type allele, A, can be invaded by a mutant allele, a, which causes workers to be non-reproductive. Since we consider a loss of function event (the loss of the tendency to produce eggs), it is more likely that the mutation is recessive rather than dominant. Therefore in the main text we present the conditions for a recessive mutant allele. In the Methods, we give derivations and results for both recessive and dominant alleles.

If the mutant allele is recessive, then

![Figure 1.](https://cdn.elifesciences.org/articles/08918/elife-08918-fig1-v2.jpg)

**Figure 1.:** The wild-type allele is A. The mutant allele inducing worker sterility is a. (A) There are three types of virgin queens: AA , Aa, and aa. Each queen mates n times. Of those matings, n − m are with wild-type males (type A) and m are with mutant males (type a). Hence, there are 3(n + 1) types of fertilized queens (colonies). (B) Relative proportions of offspring for each colony type if the mutant allele, a, for worker sterility is recessive. For example, if the queen’s genotype is Aa, then half of her sons are A and the other half are a. We denote this by A + a. If the queen’s genotype is aa and she has mated with both types of males, 0< m < n, then she has both Aa and aa workers (in proportion n − m and m, respectively); her Aa workers produce male eggs, which have an equal proportion of A and a genotypes. (C) Relative proportions of offspring for each colony type if the mutant allele, a, for worker sterility is dominant.DOI: http://dx.doi.org/10.7554/eLife.08918.003

The genotype of the colony is determined by the genotype of the queen and the sperm she has stored. There are 3(n + 1) types of colonies that need to be considered to formulate the full dynamics. The different colony types, and corresponding offspring with a recessive sterility allele, a, are shown in Figure 1B.

For each colony, there are three types of offspring: queen-laid females, queen-laid males, and worker-laid males. Figure 1B can be understood by considering how the queen and the workers produce their offspring.

Consider the offspring of type AAm colonies. The queen makes a female by randomly selecting one of the two alleles from her own genotype and pairing it with an allele selected randomly from the sperm of one of her mates. In type AAm colonies, the type AA queen mates with (n − m) type A males and m type a males. From her own genotype, the queen always selects an A allele. From her mates’ sperm, the queen selects an A allele with probability (n − m)/n or an a allele with probability m/n. Notice that in Figure 1B,C, for simplicity of presentation, we omit the overall normalization of each entry. So, for example, for type AAm colonies, we simply write that the queen produces n − m type AA females for every m type Aa females (first row, second column of Figure 1B). The correct normalizations are included in the calculations of the Materials and methods section.

The queen makes a male by randomly selecting one of the two alleles from her own genotype. Because the queen in a type AAm colony only carries the A allele, she can only produce type A drones (first row, third column of Figure 1B).

For a type AAm colony, in the 'Workers’ Sons' column, we must consider the rates of production of type AA and type Aa females by the queen, and we must consider the offspring of the type AA and type Aa females that the queen produces. The fraction of queen-produced females of type AA is, as described above, (n − m)/n, and each type AA female produces only type A males. The fraction of queen-produced females of type Aa is, as described above, m/n, and each type Aa female produces type A and type a males with equal probability. The total fraction of worker-laid males that are of type A is (n − m)/n + (1/2)(m/n) = (2n − m)/2n. The total fraction of worker-laid males that are of type a is (1/2)(m/n) = m/2n. Therefore, the workers of type AAm colonies produce 2n − m type A males for every m type a males (first row, fourth column of Figure 1B).

The logic behind the offspring of type Aam and type aam colonies is the same. The only other point is that type aa workers are non-reproductive. To see how worker sterility enters into Figure 1B, consider the worker-produced males of type aam colonies. The queen of type aam colonies produces n − m type Aa females for every m type aa females (third row, second column of Figure 1B). Type Aa workers produce equal numbers of type A and type a males. Type aa workers are non-reproductive; they do not contribute to the colony’s production of worker-produced males. So, in type aam colonies, all worker-produced males come from type Aa workers, and type A and type a males are therefore produced by workers in equal amounts (third row, fourth column of Figure 1B).

The entries in Figure 1C originate from the same reasoning. The only difference is that, if the sterility allele, a, is dominant, then type Aa and type aa workers do not contribute to a colony’s production of worker-produced males. The entries in Figure 1C are described in detail in the Materials and methods.

In our analysis, we neglect stochastic effects. This is reasonable if we assume that the number of individuals produced by a colony is very large. In this case, the fractions of colony offspring of different genotypes in a generation do not differ significantly from the entries in Figure 1B,C.

A crucial quantity is the functional relationship between the fraction of males produced by the queen, p, and the fraction of non-reproductive workers, z, that are present in a colony. The parameter z can vary between 0 and 1. If z = 0, then there are no non-reproductive workers in the colony. If z = 1, then all workers in the colony are non-reproductive. We denote by pz the fraction of males that come from the queen if the fraction of non-reproductive workers is z. The quantity p0 denotes the fraction of males that come from the queen if there are no non-reproductive workers in the colony. We expect p0 to be less than 1. The quantity p1 denotes the fraction of males that come from the queen if all workers are non-reproductive. Clearly, p1 = 1.

It is natural to assume that

![Figure 2.](https://cdn.elifesciences.org/articles/08918/elife-08918-fig2-v2.jpg)

**Figure 2.:** (A) The function p denotes the fraction of male offspring that come from the queen if a fraction, zz, of the workers are non-reproductive. Therefore, 1 − p is the fraction of male offspring that come from the workers. Clearly, zp should be an increasing function. More workers that are sterile means a larger fraction of males that come from the queen. If all workers are non-reproductive, then all males come from the queen, zp1 = 1. (B) The function r denotes the reproductive rate (or efficiency) of the colony if a fraction, zz, of the workers are non-reproductive. Without loss of generality, we normalize such that r0 = 1. If worker sterility has an advantage, then it should increase colony efficiency for some values of z, but the function r need not be monotonically increasing. It is possible that maximum colony efficiency is obtained for an intermediate value of zz. Several possibilities for the colony efficiency function, r, are shown.zDOI: http://dx.doi.org/10.7554/eLife.08918.004

The mutant allele can be favored by natural selection if non-reproductive workers provide a benefit to the colony, which is of course a natural assumption for the evolution of worker altruism. Division of labor has the potential to improve efficiency (Cole, 1986; Naeger et al., 2013). Another key component in our analysis is the functional relationship between the rate, r, at which the colony produces reproductive units (virgin queens and males) and the fraction of sterile workers, z. We use the notation rz to describe the reproductive rate of a colony where a fraction, z, of workers are non-reproductive. The quantity r0 denotes the reproductive rate of the colony if none of the workers are non-reproductive. Non-reproductive workers have a chance to be favored by natural selection if rz > r0 for some z. But the function rz need not be monotonically increasing. It is possible that there is an optimum fraction of non-reproductive workers, which maximizes the overall reproductive rate of the colony. We will study various functional forms of rz. Several sample forms of the function rz are shown in Figure 2B.

## Results

If the mutant allele is recessive, then AA and Aa workers lay male eggs, while aa workers are non-reproductive. For single mating, n = 1, we find that the a allele can invade an all-A resident population provided

(1)r1/2r0>6+2p05+3p0

What is the intuition behind this condition? There are five colony types, AA0, AA1, Aa0, Aa1, and aa0, which are relevant for determining if the mutant allele can invade. Four of those colony types do not produce sterile workers (z = 0), so the parameters p0 and r0 enter into Equation 1. In colonies of type Aa1, half of the workers are sterile (z = 1/2); thus the parameter r1/2 enters into Equation 1. Moreover, both the queen and the workers in Aa1 colonies each produce 50% type A males and 50% type a males; therefore the parameter p1/2 is irrelevant for the invasion and absent from Equation 1.

If all males are initially produced by the workers (p0 = 0), then the ratio of the efficiency of type Aa1 colonies to type AA0 colonies, r1/2/r0, must be greater than 6/5 for non-reproductive workers to appear. Notice that the critical value of r1/2/r0 is a decreasing function of p0. Intuitively, this means that if worker sterility has a smaller phenotypic effect on a colony (such that p0 is closer to p1 = 1), then the efficiency gain from sterile workers does not need to be as high to facilitate the invasion of sterility. If p0 is small, then we get efficiency thresholds for r1/2/r0 of ~1.1-1.2. If p0 is large, then we get efficiency thresholds that are close to 1. As long as p0 is not infinitesimally close to 1, the ratio r1/2/r0 must always be greater than 1 by a finite amount. Sterility cannot invade if sterile workers do not appreciably improve colony efficiency.

We note that other studies report the evolution of a worker caste with infinitesimal efficiency benefits in singly mated colonies (Boomsma, 2007, 2009; Gardner et al., 2012). But these papers consider competition between worker offspring and queen-laid female eggs, which induces sex-ratio effects that complicate the analysis.

Another recent study argues that eusociality can evolve even if sterile workers are relatively inefficient at raising siblings (Avila and Fromhage, 2015). But this work focuses centrally on the evolution of nest formation, where nest-site limitation and dispersal mortality impose ecological constraints on independent breeding. In our study, we analyze the scenario where nests have already formed, and non-reproductive workers emerge as a subsequent step in the path to advanced eusociality.

For double mating, n = 2, we find that the a allele can invade an all-A resident population provided

(2)r1/4r0>6+3p05+3p0+p1/4

Now there are six colony types, AA0, AA1, AA2, Aa0, Aa1, and aa0, which are relevant for determining if the mutant allele can invade. Colony types AA0, AA1, AA2, Aa0, and aa0 do not produce sterile workers (z = 0), so the parameters p0 and r0 appear in Equation 2. Colonies of type Aa1 produce a fraction 1/4 of sterile workers (z = 1/4). The Aa1 queen uses the sperm from the type A male that she has mated with to produce AA and Aa workers in equal proportion. Or the Aa1 queen uses the sperm from the type a male to produce Aa and aa workers with equal proportion. Thus, 1/4 of the workers are of type aa and are non-reproductive. Correspondingly, the parameters p1/4 and r1/4 appear in Equation 2.

The maximum critical value of r1/4/r0 for evolution of non-reproductive workers is 6/5, and the minimum critical value is 1. The threshold of r1/4/r0 is large (~1.1-1.2) if p0 is small. The threshold of r1/4/r0 is close to 1 if p0 is large. Provided that p0 is not infinitesimally close to 1, the ratio r1/4/r0 must always be greater than 1 by a finite amount for sterile workers to be able to invade.

It is not clear, a priori, that Equation 2 would be easier or harder to satisfy than Equation 1. Empirical knowledge of the parameters p0, p1/4, r0, r1/4, and r1/2 is needed to determine whether sterility invades more easily for single mating than for double mating.

An illustration of the parameter space and whether single or double mating is more conducive to development of sterility is shown in

![Figure 3.](https://cdn.elifesciences.org/articles/08918/elife-08918-fig3-v2.jpg)

**Figure 3.:** (A) For single mating, n = 1, the invasion of a recessive worker sterility allele depends on the parameters p0 and r1/2; for double mating, n = 2, it depends on the parameters p0, p1/4, and r1/4. (B) The evolutionary stability of a recessive worker sterility allele depends on the parameters p0, r1/2, and r1 for single mating, and on the parameters p1/2, r1/2, and r1 for double mating. We set r0 = 1 as baseline.DOI: http://dx.doi.org/10.7554/eLife.08918.005

The region of parameter space for which sterility invades for double mating but not for single mating is arbitrarily large. The region of parameter space for which sterility invades both for double mating and for single mating is also arbitrarily large. These features apply generally for different values of p0 and p1/4.

For many possible combinations of those parameters, worker sterility invades for double mating but not for single mating. For example, if p0 = 0.8 and p1/4 = 0.9, then for single mating the invasion condition is r1/2 > 1.027 while for double mating the invasion condition is r1/4 > 1.012. (Here, without loss of generality, we set r0 = 1.) The latter condition could be easier to satisfy—even if rz increases linearly with z.

We note that colony reproductive efficiency, rz, would not necessarily be expected to increase monotonically with the fraction of sterile workers, z. The law of diminishing returns may apply to the addition of non-reproductive workers to a colony. Non-reproductive workers contribute positively to the colony’s total reproductive output by performing colony maintenance and helping to raise other individuals’ offspring. But by not laying any eggs, non-reproductive workers are also negatively affecting the colony’s total reproductive output. Consequently, colony reproductive efficiency may be maximized if some workers reproduce while other workers focus their efforts on colony maintenance. In our model, this would correspond to rz reaching a maximum for some 0 < z < 1.

Assuming that

![Figure 4.](https://cdn.elifesciences.org/articles/08918/elife-08918-fig4-v2.jpg)

**Figure 4.:** Equations 1 and 2.The sterility allele is recessive. For numerically probing invasion, we use the initial condition  and XA⁢A,0=1-10-2. We set XA⁢A,1=10-2r0 = 1. A: Single mating, n = 1. Parameters p0 = 0.1 and r1 = 1.29. B: Double mating, n = 2. Parameters p0 = 0.2, p1/4 = 0.4, p1/2 = 0.6, r1/2 = 1.24 and r1 = 1.6.DOI: http://dx.doi.org/10.7554/eLife.08918.006

We have also calculated the condition for the evolutionary stability of non-reproductive workers. For single mating, n = 1, we find that the a allele is stable against invasion of A in an all-a resident population provided

(3)r1r0-1-p022⁢r1r1/2-1⁢>1

Three colony types, aa1, aa0, and Aa1, are relevant for determining if the a allele for sterility is evolutionarily stable to invasion by the A allele. Type aa1 colonies produce only sterile workers (z = 1), hence the appearance of r1 in Equation 3. Type aa0 colonies produce no sterile workers (z = 0), hence the appearance of p0 and r0 in Equation 3. Type Aa1 colonies produce 50% sterile workers (z = 1/2), hence the appearance of r1/2 in Equation 3. The parameter p1/2 is irrelevant because the queen and the reproductive workers in type Aa1 colonies each produce 50% type A males and 50% type a males.

For double mating, n = 2, we find that the a allele is evolutionarily stable provided

(4)r1r1/2-(1-p1/2)⁢2⁢r1r1/2-1>1

Three colony types, aa2, aa1, and Aa2, are relevant for determining if the a allele for sterility is evolutionarily stable. Type aa2 colonies produce only sterile workers (z = 1), hence the appearance of r1 in Equation 4. Type aa1 and type Aa2 colonies each produce 50% sterile workers (z = 1/2), hence the appearance of p1/2 and r1/2 in Equation 4. The conditions for invasion and stability with more than two matings are given in the Materials and methods.

Empirical knowledge of the parameters p0, p1/2, r0, r1/2, and r1 is needed to determine if worker sterility is more stable for single mating than for double mating. For many possible combinations of those parameters, worker sterility is evolutionarily stable for double mating but not for single mating. For example, if p0 = 0.6, p1/2 = 0.9, r0 = 1, and r1/2 = 1.05, then for single mating the stability condition is r1 > 1.105 while for double mating the stability condition is only r1 > 1.087. The latter condition is less stringent. The parameter space for evolutionary stability for specific values of pz is shown in Figure 3B.

![Figure 5.](https://cdn.elifesciences.org/articles/08918/elife-08918-fig5-v2.jpg)

**Figure 5.:** n = 1).We consider a recessive sterility allele, a. There are four possible scenarios: The mutant allele cannot invade but is evolutionarily stable (bistability); the mutant allele can invade and is evolutionarily stable; the mutant allele can invade but is unstable (coexistence); the mutant allele cannot invade and is unstable. Only three parameters matter: p0, r1/2, and r1; p0 denotes the fraction of male offspring that come from the queen if there are no sterile workers in the colony (z = 0); r1/2 and r1 denote respectively the reproductive rate (efficiency) of the colony if z = 1/2 and z = 1 of all workers are sterile. The baseline value is r0 = 1. (A) Phase diagram for p0 = 0.5. (B) Phase diagram for p0 = 0.9. As p0 gets closer to 1, the intersection of the critical curves approaches the point (r1/2,r1) = (1,1).DOI: http://dx.doi.org/10.7554/eLife.08918.007

![Figure 6.](https://cdn.elifesciences.org/articles/08918/elife-08918-fig6-v2.jpg)

**Figure 6.:** Figure 5A.The sterility allele is recessive, and we consider single mating (n = 1). For each of the four panels, we use the initial conditions: A:  and XA⁢A,0=1-10-3; B: XA⁢A,1=10-3 and Xa⁢a,1=1-10-3; C: Xa⁢a,0=10-3 and XA⁢A,0=0.27 (lower curve), and Xa⁢a,0=0.73 and XA⁢A,0=0.26 (upper curve); D: Xa⁢a,0=0.74 and XA⁢A,0=1-10-2 (lower curve), and XA⁢A,1=10-2 and Xa⁢a,1=1-10-2 (upper curve). We set Xa⁢a,0=10-2r0 = 1. A: Parameters p0 = 0.5, r1/2 = 1.0869, and r1 = 1.1521. B: Parameters p0 = 0.5, r1/2 = 1.0669, and r1 = 1.1321. C: Parameters p0 = 0.5, r1/2 = 1.0669, and r1 = 1.1521. D: Parameters p0 = 0.5, r1/2 = 1.0869, and r1 = 1.1321.DOI: http://dx.doi.org/10.7554/eLife.08918.008

![Figure 7.](https://cdn.elifesciences.org/articles/08918/elife-08918-fig7-v2.jpg)

**Figure 7.:** n = 1) and double mating (n = 2) on the evolution of worker sterility.Whether or not single or double mating favors the evolution of worker sterility depends on the functions p and zr. The function zp specifies the fraction of male offspring that come from the queen if a fraction, zz, of all workers in the colony is non-reproductive. The function r specifies the reproductive rate (or efficiency) of the colony if a fraction, zz, of all workers in the colony is non-reproductive. We consider a recessive mutant allele, a, for worker sterility. (A, B) For these parameter choices, the mutant allele causing worker sterility can invade for double mating but not for single mating. (C, D) For these parameter choices, the mutant allele causing worker sterility is evolutionarily stable for double mating but not for single mating.DOI: http://dx.doi.org/10.7554/eLife.08918.009

For a dominant sterility allele, there is typically a large region of parameter space for which sterility evolves for double mating but not for single mating. There is also an arbitrarily large region of parameter space for which sterility evolves for double mating and for single mating. For a recessive allele, it is possible that more than two matings are necessary for the emergence of worker sterility. These additional examples are presented in the Materials and methods.

## Discussion

Single mating of queens has often been claimed to be a key factor in the evolution of eusociality. This paradigm derives from heuristic relatedness-based arguments. For example, Boomsma’s ‘monogamy window hypothesis’ (Boomsma, 2007, 2009) holds that persistent monandry is crucial in the evolution of a worker caste. His argument is that, under monandry, because a worker is equally related to her own offspring as to her mother’s offspring (1/2), her reduced reproduction will be selected for if it increases production of the latter more than it decreases production of the former. By this argument, under monandry but not multiple mating, very small colony-level efficiency gains from workers should lead to their evolution.

On the empirical side, Hughes et al. (2008) study a phylogeny of the Hymenoptera, and, employing an ancestral state reconstruction analysis, infer that each of the eight independent transitions to eusociality in the Hymenoptera occurred in a monandrous ancestral species. They take this correlation to be evidence for the causal claim that monandry is key to the evolution of eusociality. But, if most ancestral species in the clade were monandrous [as appears to be the case: Hughes et al. (2008), Fig S1; Nonacs (2011)], then the fact that the ancestors of eusocial species in the clade were monandrous would not be surprising (Nonacs, 2011). As an extreme example, if Hughes et al. were to repeat their study for the trait of haplodiploidy, they would also find that each of the eight independent transitions to eusociality occurred in a haplodiploid ancestral species (since all Hymenoptera are haplodiploid). It would be absurd to consider this to be evidence for the theoretical claim that haplodiploidy is key to the evolution of eusociality.

An important aspect of the evolution of advanced eusociality is the cancellation of all worker reproduction—in particular, the production of males. Here, we have performed a rigorous mathematical analysis of the conditions under which worker non-reproduction evolves. Our analysis has revealed that monandry does not play a crucial role in the evolution of non-reproductive worker castes. Indeed, in some cases, non-reproduction evolves when queens are multiply mated, but not when they are singly mated. Our results therefore show that the dominant paradigm, that monandry is crucial for the evolution of eusociality because it maximizes relatedness among siblings, needs to be revised. It may still turn out that monandry is important in the evolution of non-reproductive castes, but this would have to be for other reasons (Nowak et al., 2010; Nonacs, 2011; Hunt, 2012; Wilson and Nowak, 2014).

These insights have been achieved because of a more general treatment of the colony-level effects of non-reproductive workers than is allowed for by simple relatedness-based arguments. In our model, we have explicitly accounted for two key parameters that are often neglected in other studies: rz, the reproductive rate of the colony, and pz, the proportion of male offspring that come from the queen, if a fraction z of the colony’s workers are non-reproductive. The conditions under which selection favors non-reproductive workers have been shown to depend crucially, and in interesting ways, on these two parameters. Empirical measurement of these parameters is therefore required to understand the selective forces underlying the evolution of non-reproductive castes in social insects. This suggests a line of future research.

It is important to distinguish between worker non-reproduction (workers produce no offspring, but may still retain the ability to do so), and the more specific phenomenon of worker sterility (workers do not have the ability to reproduce). An embedded distinction is that, in very many eusocial insect species, worker females have lost the ability to lay fertilized (female) eggs—e.g., through loss or degradation of the spermatheca—but retain the ability to lay unfertilized (male) eggs—i.e., they have functional ovaries (Bourke, 1988; Hölldobler and Wilson, 1990). In comparison, complete sterility (sexual and asexual) is rare in the eusocial insects; for example, only 9 of the roughly 300 genera of ants are known to have evolved complete worker sterility (Bourke, 1995).

In our model, we have assumed that workers can lay only unfertilized male eggs. Our model therefore best applies to those transitions from species whose workers lay only male eggs to species where the workers are non-reproductive. This is probably the most common and important route to a non-reproductive worker caste in the social insects (Bourke, 1988).

It is important to realize that our model applies significantly more generally than to just the (comparatively few) transitions to complete worker sterility. We have focused here on the case where a single (recessive or dominant) allele turns off worker production of males. However, mathematically, this assumption can easily be relaxed by supposing that the allele in question merely alters the frequency of worker male production by some amount. Thus, our approach is flexible enough to handle a variety of molecular mechanisms for worker reproductive restraint, which are still being elucidated for particular species (Abouheif and Wray, 2002; Dearden, 2006; Khila and Abouheif, 2008; Moczek et al., 2011; Cameron et al., 2013; Sadd et al., 2015; Kapheim et al., 2015).

One potentially important factor in the evolution of worker non-reproduction is worker policing. Here, if a worker lays a (male) egg, there is some chance that another worker will destroy the egg. This reduces the incentive for workers to lay male eggs in the first place, therefore selecting for decreased worker reproduction (Bourke, 1999; Wenseleers et al., 2004; Ratnieks et al., 2006). A slightly modified version of our model can cover the case of worker policing (with appropriate interpretations of the parameters rz and pz). A detailed investigation of this situation is desirable, and is in progress. Moreover, our analysis demonstrates that worker policing, though perhaps conducive to the evolution of worker non-reproduction, is not necessary for it.

Our analysis makes no use of inclusive fitness theory, which is an unnecessary construct (Nowak et al., 2010; Allen et al., 2013). Indeed, our analysis shows that the evolution of non-reproductive workers depends on precise functional relationships between worker reproduction, queen reproduction, and colony efficiency, which inclusive fitness heuristics cannot account for. We note that inclusive fitness theory, which has dominated this area for decades, has not produced a mathematical analysis of even the most basic factors leading to the evolution of non-reproductive workers. A clear understanding of how natural selection acts on the evolution of any social behavior is possible once the field has recognized the limitations of inclusive fitness and has moved beyond them.

## Materials and methods

In this Materials and methods section, we present a mathematical model for the population dynamics of Hymenopteran colonies, and we calculate exact conditions that must be satisfied for non-reproductive workers to evolve. Our model uses haplodiploid genetics. Each female carries homologous pairs of maternal and paternal chromosomes, while each male possesses a single set of chromosomes. We assume that a specific mutation (allele) leads to non-reproductive workers. The A allele represents normal behavior, while the mutant a allele leads to unmated females (workers) abstaining from laying their own male eggs. If the a allele is dominant, then workers that possess at least one a allele are sterile. If the a allele is recessive, then workers that are homozygous for a are sterile. Under what conditions does the a allele for non-reproductive workers invade a population? Under what conditions is the a allele evolutionarily stable against invasion by A? A mathematical analysis of this problem lends insight into the selective forces that act on the evolution of worker sterility. While a loss of function mutation is probably recessive, it is instructive to consider both the dominant and recessive cases in detail.

## Description of the model

Consider a large population of insects. There are many colonies in the population, and each colony produces many offspring over its lifetime. The particular species under investigation has a haplodiploid genetic system. Females carry homologous pairs of maternal and paternal chromosomes, while males carry a single set of chromosomes. Queens can produce diploid female workers and gynes (future queens) from her own genotype combined with the genotype of each of the male drones that she has mated with. Queens can also produce drones using her own genotype. Female workers can produce drones as well. Thus there can be competition over whether the queen or the workers produce most of the males in a colony.

To investigate the selective forces behind non-reproductive workers—i.e., workers that do not parthenogenetically produce haploid drones—we propose two alleles, A and a. The phenotype corresponding to the A allele is such that workers produce drones. The phenotype corresponding to the a allele is such that workers do not produce drones.

An important parameter is the number, n, of males with which the colony’s queen has mated. A schematic of the mating events is shown in Figure 1A. There are several possibilities: A type AA gyne mates with n − m type A males and m type a males. A type Aa gyne mates with n − m type A males and m type a males. A type aa gyne mates with n − m type A males and m type a males.

The mating events are random. A virgin queen mates with n randomly chosen males in the population. Notice that, for mating, the gynes and drones are considered well-mixed: A gyne from one colony can mate with n drones, each chosen randomly from among the colonies in the population. For n = 1, we obtain single mating (monandry). For n = 2, we obtain double mating.

The following system of ordinary differential equations describes the selection dynamics in continuous time:

(5)X˙AA,m=d⁢XAA,md⁢t=nm⁢xA⁢A⁢yAn-m⁢yam-⁢ϕXA⁢A,mX˙Aa,m=d⁢XAa,md⁢t=nm⁢xA⁢a⁢yAn-m⁢yam-ϕ⁢XA⁢a,mX˙a⁢a,m=d⁢Xaa,md⁢t=nm⁢xa⁢a⁢yAn-m⁢yam-ϕ⁢Xa⁢a,m

The overdot denotes the time derivative, d/dt. We use the overdot notation for any time derivative.

We understand Equation 5 as follows. We represent the genotype of a colony by the genotype of its queen and the sperm she has stored from her matings. Each queen carries homologous pairs of maternal and paternal chromosomes, so each queen has one of three possible combinations of the A and a alleles in her own genotype: AA, Aa, or aa. A particular queen has mated with n − m type A males and m type a males. The number of colonies that are headed by type AA queens who have mated with n − m type A males and m type a males is denoted by XAA,m. The number of colonies that are headed by type Aa queens who have mated with n − m type A males and m type a males is denoted by XAa,m. The number of colonies that are headed by type aa queens who have mated with n − m type A males and m type a males is denoted by Xaa,m. The variables xAA, xAa, and xaa denote the numbers of gynes of the three possible genotypes in the population. The variables yA and ya denote the numbers of drones of the two possible genotypes in the population. A gyne randomly mates with n drones to become a queen. The binomial coefficient accounts for all possible sequences in which a female can mate with m males carrying an a allele out of n total matings.

We require that the total number of colonies sums to a constant value, c, at all times:

(6)∑m=0n(XAA,m+XAa,m+Xaa,m)=c

Colonies compete for resources which are limited. Notice that ϕ in Equation 5 represents a density-dependent death rate. We use ϕ to model the effect of environmental constraints in limiting the total number of colonies. To enforce the density constraint, Equation 6, on the colony variables, we set

(7)ϕ=c-1⁢(xAA+xAa+xaa)⁢(yA+ya)n

Our choice to analyze the evolutionary dynamics of sterile workers in continuous time is a matter of preference. Working in continuous time usually simplifies the analysis. For example, when we derive conditions for the invasion of a recessive allele or the stability of a dominant allele, the perturbative expansion of the colony variables must be performed to second order, and the calculations become quite messy.

There are a couple of key biological parameters in our model. The emergence of sterile workers can affect the fraction of male eggs in a colony that originate from the queen. If a fraction z of workers in a colony are non-reproductive, then the fraction of male offspring that originate from the queen is denoted by pz. The queen and the unfertilized females may compete for production of male eggs. The function pz for 0 ≤ z < 1 likely varies for different species. It is reasonable to expect that pz is an increasing function of z; an increase in the proportion of workers that are non-reproductive results in a larger proportion of queen-produced males. If all workers are non-reproductive, then z = 1 and p1 = 1.

The other key function in our model is the efficiency, rz, of a colony in which a fraction z of workers are non-reproductive. An appropriate biological intuition is that the parameter rz is the total number of offspring produced by a colony when a fraction, z, of workers in the colony are non-reproductive. As we shall see, the ratios of colony efficiency values, rz, for colonies with different genotypes—i.e., the relative reproductive efficiencies of colonies with different genotypes—are important quantities for understanding the evolutionary dynamics of a mutation that causes workers to be non-reproductive. As baseline, we set r0 = 1.

Non-reproductive workers forego their own reproductive potential in order to help raise their nestmates’ offspring. If this division of labor has some advantage for the colony, then we expect rz > 1 for some values of z. It is not necessary, however, that rz is a monotonically increasing function.

Since we are focused on the evolutionary dynamics of the colony variables, XAA,m, XAa,m, and Xaa,m for 0 ≤ m ≤ n, we rewrite the first term on the right-hand side of Equation 5 in terms of the colony variables. We express each of the gyne and drone numbers, xAA, xAa, xaa, yA, and ya, as a linear combination of the colony variables, XAA,m, XAa,m, and Xaa,m. The coefficients in these linear relationships depend on whether the allele, a, that acts in a worker to induce that worker’s sterility is dominant or recessive.

## Reproductives with a dominant sterility allele

For a dominant allele, a, causing worker sterility, we have the reproduction events shown in Figure 1C. These can be understood as follows.

Consider the offspring of type AA,m colonies. The queen produces n − m type AA females for every m type Aa females. Because the queen only carries the A allele, she can only produce type A drones. Only workers that carry two copies of the A allele are capable of making drones, and they can therefore only pass on copies of the A allele, so workers are also only capable of making type A drones.

Consider the offspring of type Aa,m colonies. The queen produces n − m type AA females, n type Aa females, and m type aa females out of every 2n females that she produces. Because the queen carries the A and a alleles, she produces type A and type a drones in equal proportion. Only workers that carry two copies of the A allele are capable of making drones, and they therefore only pass on copies of the A allele, so workers are only capable of making type A drones.

Consider the offspring of type aa,m colonies. The queen produces n − m type Aa females for every m type aa females. Because the queen only carries the a allele, she can only produce type a drones. Only workers that carry two copies of the A allele are capable of making drones, but type AA workers are not produced by the queen, so workers do not produce males.

For studying the invasion of the mutant allele, only a subset of those colony types are relevant. Also, for simplicity, we neglect stochastic effects. The number of individuals produced by a colony is assumed to be very large, so that the fractions of colony offspring of the various possible genotypes are always exactly the same for that type of colony.

Our attention is on the evolution of the 3(n + 1) colony variables. Therefore, it is helpful to write all quantities in terms of the colony variables. We can write each type of reproductive of a colony (xAA, xAa, xaa, yA, and ya) as a simple weighted sum of colony variables. Using Figure 1C, the numbers of unfertilized females (xAA, xAa, and xaa) and males (yA and ya) in the population which are capable of mating can be written as:

(8)xAA=∑m = 0n[n-mngrmnXAA,m+n-m2ngrm+n2nXAa,m]xAa=∑m = 0n[mngrmnXAA,m+12grm+n2nXAa,m+n-mngr1Xaa,m]xaa=∑m = 0nm2ngrm+n2nXAa,m+mngr1Xaa,myA=∑m = 0n[krmnXAA,m+2-pm+n2n2krm+n2nXAa,m]ya=∑m =0n[12pm+n2nkrm+n2nXAa,m+kr1Xaa,m]

Here, 0 < g ≤ 1 is the fraction of all females produced by a colony that are gynes. Moreover, 0 < k ≤ 1 is the fraction of all males produced by a colony that are able to mate. For example, if only a small percentage of female and male offspring of a colony eventually disperse and mate, then we have g≪1 and k≪1. The parameters g and k are written explicitly here for conceptual clarity. As we shall see, they turn out to be irrelevant in the conditions for invasion and stability of non-reproductive workers.

## Reproductives with a recessive sterility allele

For a recessive allele, a, causing worker sterility, we have the reproduction events shown in Figure 1B. These can be understood as follows.

Consider the offspring of type AA,m colonies. The queen produces n − m type AA females for every m type Aa females. Because the queen only carries the A allele, she can only produce type A drones. A fraction (n − m)/n of all workers produce only type A males, and a fraction m/n of all workers produce type A and type a males in equal proportion. Altogether, workers produce a fraction (2n − m)/(2n) type A males and a fraction m/(2n) type a males.

Consider the offspring of type Aa,m colonies. The queen produces n − m type AA females, n type Aa females, and m type aa females out of every 2n females that she produces. Because the queen carries the A and a alleles, she produces type A and type a drones in equal proportion. A fraction (n − m)/(2n) of all workers produce only type A males, and a fraction 1/2 of all workers produce type A and type a males in equal proportion. Workers that carry two copies of the a allele are non-reproductive. Altogether, workers produce a fraction (3n − 2m)/(4n − 2m) type A males and a fraction n/(4n − 2m) type a males.

Consider the offspring of type aa,m colonies. The queen produces n − m type Aa females for every m type aa females. Because the queen only carries the a allele, she can only produce type a drones. A fraction (n − m)/n of all workers produce type A and type a males in equal proportion. Workers that carry two copies of the a allele are non-reproductive. Altogether, workers produce type A and type a males in equal proportion.

For studying the invasion of the mutant allele, only a subset of those colony types are relevant. Also, for simplicity, we neglect stochastic effects. The number of individuals produced by a colony is assumed to be very large, so that the fractions of colony offspring of the various possible genotypes are always exactly the same for that type of colony.

Our attention is on the evolution of the 3(n + 1) colony variables. Therefore, it is helpful to write all quantities in terms of the colony variables. We can write each type of reproductive of a colony (xAA, xAa, xaa, yA, and ya) as a simple weighted sum of colony variables. Using Figure 1B, the numbers of unfertilized females (xAA, xAa, and xaa) and males (yA and ya) in the population which are capable of mating can be written as:

(9)xA⁢A=∑m=0nn-mn⁢g⁢r0⁢XA⁢A,m+n-m2⁢n⁢g⁢rm2⁢n⁢XA⁢a,mxA⁢a=∑m=0nmn⁢g⁢r0⁢XA⁢A,m+12⁢g⁢rm2⁢n⁢XA⁢a,m+ n-mn⁢g⁢rmn⁢Xa⁢a,mxa⁢a=∑m=0nm2⁢n⁢g⁢rm2⁢n⁢XA⁢a,m+mn⁢g⁢rmn⁢Xa⁢a,myA=∑m=0n2⁢n-m+m⁢p02⁢nkr0XA⁢A,m+n⁢3-pm2⁢n-m⁢2-pm2⁢n2⁢(2⁢n-m)krm2⁢nXA⁢a,m+121-pmnkrmnXa⁢a,mya=∑m=0nm2⁢n(1-p0)kr0XA⁢A,m+n1+pm2⁢n-m⁢pm2⁢n2⁢(2⁢n-m)krm2⁢nXA⁢a,m+121+pmnkrmnXa⁢a,m

Here, 0 < g ≤ 1 is the fraction of all females produced by a colony that are gynes. Moreover, 0 < k ≤ 1 is the fraction of all males produced by a colony that are able to mate. For example, if only a small percentage of female and male offspring of a colony eventually disperse and mate, then we have g≪1 and k≪1. The parameters g and k are written explicitly here for conceptual clarity. As we shall see, they turn out to be irrelevant in the conditions for invasion and stability of non-reproductive workers.

## Rescaling of the model variables

We have described the biological intuition for our model of population genetics. To calculate conditions for understanding the evolutionary dynamics of a mutation that effects worker sterility, it is mathematically convenient to make the following substitutions:

(10)XA⁢A,m→c⁢XA⁢A,mXA⁢a,m→c⁢XA⁢a,mXa⁢a,m→c⁢Xa⁢a,mxA⁢A→g⁢c⁢xA⁢AxA⁢a→g⁢c⁢xA⁢axa⁢a→g⁢c⁢xa⁢ayA→k⁢c⁢yAya→k⁢c⁢yaϕ→g⁢kn⁢cn⁢ϕt→g-1⁢k-n⁢c-n⁢t

Let’s see what happens when we rescale the model variables and parameters according to Equation 10. We substitute Equation 10 into Equation 5 to obtain

(11)X˙A⁢A,m=d⁢XA⁢A,md⁢t= nmxA⁢A⁢yAn-m⁢yam-ϕ⁢XA⁢A,mX˙A⁢a,m=d⁢XA⁢a,md⁢t=⁢nmxA⁢a⁢yAn-m⁢yam-ϕ⁢XA⁢a,mX˙a⁢a,m=d⁢Xa⁢a,md⁢t= nm⁢xa⁢a⁢yAn-m⁢yam-ϕ⁢Xa⁢a,m

We substitute Equation 10 into Equation 6 to obtain

(12)∑m=0n(XA⁢A,m+XA⁢a,m+Xa⁢a,m)=1

We substitute Equation 10 into Equation 7 to obtain

(13)ϕ=(xA⁢A+xA⁢a+xa⁢a)⁢(yA+ya)n

## Reproductives (rescaled) with a dominant sterility allele

We substitute Equation 10 into Equation 8 to obtain

(14)xA⁢A=∑m=0nn-mn⁢rmn⁢XA⁢A,m+n-m2⁢n⁢rm+n2⁢n⁢XA⁢a,mxA⁢a=∑m=0nmn⁢rmn⁢XA⁢A,m+12⁢rm+n2⁢n⁢XA⁢a,m+n-mn⁢r1⁢Xa⁢a,mxa⁢a=∑m=0nm2⁢n⁢rm+n2⁢n⁢XA⁢a,m+mn⁢r1⁢Xa⁢a,myA=∑m=0nrmn⁢XA⁢A,m+2-pm+n2⁢n2⁢rm+n2⁢n⁢XA⁢a,mya=∑m=0n12 ⁢pm+n2⁢n ⁢rm+n2⁢n⁢XA⁢a,m+r1⁢Xa⁢a,m

## Reproductives (rescaled) with a recessive sterility allele

We substitute Equation 10 into Equation 9 to obtain

(15)xA⁢A=∑m=0nn-mn⁢r0⁢XA⁢A,m+n-m2⁢n⁢rm2⁢n⁢XA⁢a,mxA⁢a=∑m=0nmn⁢r0⁢XA⁢A,m+12⁢rm2⁢n⁢XA⁢a,m+n-mn⁢rmn⁢Xa⁢a,mxa⁢a=∑m=0nm2⁢n⁢rm2⁢n⁢XA⁢a,m+mn⁢rmn⁢Xa⁢a,myA=∑m=0n2⁢n-m+m⁢p02⁢nr0XA⁢A,m+n3-pm2⁢n-m2-pm2⁢n⁢2⁢(2⁢n-m)rm2⁢nXA⁢a,m+121-pmnrmnXa⁢a,mya=∑m=0nm2⁢n(1-p0)r0XA⁢A,m+n1+pm2⁢n⁢-m⁢pm2⁢n2⁢(2⁢n-m)rm2⁢nXA⁢a,m+121+pmnrmnXa⁢a,m

## Conditions for evolutionary invasion and evolutionary stability of worker sterility: perturbative analysis

Notice that when we rescale the model variables and parameters according to Equation 10, the evolutionary dynamics are mathematically unchanged: Equation 5 has the same form as Equation 11, Equation 6 has the same form as Equation 12, Equation 7 has the same form as Equation 13, Equation 8 has the same form as Equation 14, and Equation 9 has the same form as Equation 15. But it is apparent why the rescalings (Equation 10) are helpful in doing calculations: When the right-hand side of (Equation 11) is written out in terms of the colony frequency variables XAA,m, XAa,m, and Xaa,m, the parameters g, k, and c, which are not essential for understanding the evolutionary invasion or evolutionary stability of non-reproductive workers, no longer appear in the calculations. This simplifies writing and improves clarity in the calculations that follow.

To begin, note that only two pure equilibria are possible:

From Equation 11, if any mixed equilibria exist, then they will feature 3(n + 1) nonzero frequencies.

## Invasion of a dominant worker sterility allele

What happens if we start with an infinitesimal quantity of the mutant allele, a, by perturbing the XAA,0 = 1 pure equilibrium: XA⁢A,0→1-ϵ⁢δA⁢A,0(1), with ϵ≪1? Does a dominant worker sterility allele spread in the population, or is it eliminated?

Although the state space is (3n + 2)-dimensional (3n + 3 types of colonies subject to the density constraint), the analysis simplifies. Provided that the perturbation is small (i.e. that ϵ≪1), only three colony types, AA,0, AA,1, and Aa,0, determine whether or not the dominant worker sterility allele invades. Any other colony type is headed by a queen that possesses at least two mutant a alleles (from her own genotype combined with the sperm she has collected), but such queens are so rare as to be negligible. The relevant equations among (Equation 11) for studying invasion of a dominant sterility allele are

(16)X˙A⁢A,0=xA⁢A⁢yAn-ϕ⁢XA⁢A,0X˙A⁢A,1=n⁢xA⁢A⁢yAn-1⁢ya-ϕ⁢XA⁢A,1X˙A⁢a,0=xA⁢a⁢yAn-ϕ⁢XA⁢a,0

Formally keeping track of powers of ϵ, and disregarding higher-order terms, we have:

(17)XA⁢A,0=1-ϵ⁢δA⁢A,0(1)-O⁢(ϵ2)XA⁢A,1=+ϵ⁢δA⁢A,1(1)+O(ϵ2)  XA⁢a,0=+ϵ⁢δA⁢a,0(1)+O(ϵ2)

To simplify the density constraint (Equation 12) for our calculation, we substitute (Equation 17) into (Equation 12) and collect powers of ϵ. We get

(18)δA⁢A,0(1)=δA⁢A,1(1)+δA⁢a,0(1)

Next, we substitute (Equation 17) into (Equation 14), using the density constraint (Equation 18) and keeping terms only up to order ϵ:

(19)xA⁢A=r0+ϵn-1r1n-nr0nδAA,1(1)+-2r0+r122δAa,0(1) +O(ϵ2)xA⁢a=ϵr1nnδAA,1(1)+r122δAa,0(1) +O(ε2)yA=r0+ε-r0-r1nδAA,1(1)+2-p12r12-2r02δAa,0(1) +O(ε2)ya=εp12r122δAa,0(1)+O(ε2)

By plugging (Equation 19) and (Equation 17) into (Equation 16), using the density constraint (Equation 18), and collecting powers of ϵ, we find

δ˙A⁢A,1(1)=-r0n+1⁢δA⁢A,1(1)+n⁢p12⁢r12⁢r0n2⁢δA⁢a,0(1)δ˙A⁢a,0(1)=r1nr0nnδA⁢A,1(1)+-2r0n+1+⁢r12⁢r0n2⁢δA⁢a,0(1)

The equations for δ˙A⁢A,1(1) and δ˙A⁢a,0(1) can be written in matrix form as

δ˙A⁢A,1(1)δ˙A⁢a,0(1)=-r0n+1n⁢p12⁢r12⁢r0n2r1n⁢r0nn-2⁢r0n+1+r12⁢r0n2δA⁢A,1(1)δA⁢a,0(1)⁢

Setting the dominant eigenvalue to be greater than zero and simplifying, we find that the dominant allele for worker sterility increases in frequency if

(20)r12r0⁢1+p12⁢r1nr0>2

Depending on the values of the parameters

![Figure 8.](https://cdn.elifesciences.org/articles/08918/elife-08918-fig8-v2.jpg)

**Figure 8.:** The evolutionary invasion of a dominant worker sterility allele depends on values of the parameters p1/2, r1/2, and r1 for single mating, n = 1, and on values of the parameters p1/2 and r1/2 for double mating, n = 2. The figure shows four parameter regions indicating whether or not worker sterility can evolve for single or double mating. We set r0 = 1 as baseline.DOI: http://dx.doi.org/10.7554/eLife.08918.010

## Invasion of a recessive worker sterility allele

What happens if we start with an infinitesimal quantity of the mutant allele, a, by perturbing the XAA,0 = 1 pure equilibrium: XA⁢A,0→1-ϵ⁢δA⁢A,0(1), with ϵ≪1? Does a recessive worker sterility allele spread in the population, or is it eliminated?

Although the state space is (3n + 2)-dimensional (3n + 3 types of colonies subject to the density constraint), the analysis again simplifies. Provided that the perturbation is small (i.e. that ϵ≪1), only six colony types, AA,0, AA,1, Aa,0, AA,2, Aa,1, and aa,0, determine whether or not the recessive worker sterility allele invades. Any other colony type is headed by a queen that possesses at least three mutant a alleles (from her own genotype combined with the sperm she has collected), but such queens are so rare as to be negligible. The relevant equations among (Equation 11) for studying invasion of a recessive sterility allele are

(21)X˙⁢AA,0=xA⁢A⁢yAn-ϕ⁢XA⁢A,0X˙A⁢A,1=n⁢xA⁢A⁢yAn-1⁢ya-ϕ⁢XA⁢A,1X˙A⁢a,0=xA⁢a⁢yAn-ϕ⁢XA⁢a,0X˙A⁢A,2=n⁢(n-1)2⁢xA⁢A⁢yAn-2⁢ya2-ϕ⁢XA⁢A,2X˙A⁢a,1=n⁢xA⁢a⁢yAn-1⁢ya-ϕ⁢XA⁢a,1X˙a⁢a,0=xa⁢a⁢yAn-ϕ⁢Xa⁢a,0

Recall that for analysis of the dominant allele, we only needed to consider terms of order ϵ to derive conditions for invasion of the allele. For analysis of the recessive allele, terms of order ϵ do not provide sufficient information for determining if the allele invades, which adds a level of tedium to the calculation. Formally keeping track of powers of ϵ and ϵ2, and disregarding higher-order terms, we have:

(22)XA⁢A,0=1-ϵ⁢δA⁢A,0(1)-ϵ2⁢δA⁢A,0(2)-⁢O(ϵ3)XA⁢A,1=+ϵ⁢δA⁢A,1(1)+ϵ2⁢δA⁢A,1(2)+O⁢(ϵ3)XA⁢a,0=+ϵ⁢δA⁢a,0(1)+ϵ2⁢δA⁢a,0(2)+O(ϵ3)XA⁢A,2=+ϵ2⁢δA⁢A,2(2)+O(ϵ3)XA⁢a,1=+ϵ2⁢δA⁢a,1(2)+O(ϵ3)Xa⁢a,0=+ϵ2⁢δa⁢a,0(2)+O(ϵ3)

The simplified density constraint, Equation 18, holds regardless of whether the sterility allele under consideration is dominant or recessive. To further simplify the density constraint (Equation 12) for the case of a recessive sterility allele, we substitute (Equation 22) into (Equation 12) and collect powers of ϵ2. We get

(23)δA⁢A,0(2)=δA⁢A,1(2)+δA⁢a,0(2)+δA⁢A,2(2)+δA⁢a,1(2)+δa⁢a,0(2)

Next, we substitute (Equation 22) into (Equation 15), using the density constraints (Equation 18) and (Equation 23) and keeping terms up to order ϵ2:

(24)xA⁢A⁢r0-1=  1+ϵ-1nδA⁢A,1(1)-12δA⁢a,0(1)+ϵ2-1nδA⁢A,1(2)-12δA⁢a,0(2)-2nδA⁢A,2(2)+-2⁢n+(n-1)⁢r12⁢n⁢r0-12⁢nδA⁢a,1(2)-δa⁢a,0(2)+O(ϵ3)xA⁢a⁢r0-1=ϵ1nδA⁢A,1(1)+12δA⁢a,0(1)+ϵ21nδA⁢A,1(2)+12δA⁢a,0(2)+2nδA⁢A,2(2)+⁢r12⁢n⁢r0-12⁢δA⁢a,1(2)+δa⁢a,0(2)+O(ϵ3)xa⁢a⁢r0-1=ϵ2⁢r12⁢n⁢r0-12n⁢δA⁢a,1(2)+O(ϵ3)yA⁢r0-1= 1+ϵ-1-p02⁢nδA⁢A,1(1)-1+p04δA⁢a,0(1)+ϵ2[-1-p02⁢nδA⁢A,1(2)-1+p04δA⁢a,0(2)-1-p0n⁢δA⁢A,2(2)                 +2-4⁢n-2-n3-p12⁢n⁢-p12⁢nr12⁢n⁢r0-12⁢(2⁢n-1)⁢δA⁢a,1(2)-1+p02δa⁢a,0(2)]+O(ϵ3)ya⁢r0-1= ϵ1-p02⁢nδA⁢A,1(1)+1+p04δA⁢a,0(1)+ϵ2[1-p02⁢nδA⁢A,1(2)+1+p04δA⁢a,0(2)+1-p0n⁢δA⁢A,2(2)                 +n+(n - 1)p12⁢nr12⁢n⁢r0-12⁢(2⁢n-1)⁢δA⁢a,1(2)+1+p02δa⁢a,0(2)]+O(ϵ3)

By plugging (Equation 24) and (Equation 22) into (Equation 21), using the density constraint (Equation 18), and collecting powers of ϵ, we find

δ˙A⁢A,1(1)=-1+p02r0n+1δA⁢A,1(1)+n1+p04r0n+1δAa,0(1)

δ˙A⁢a,0(1)=1nr0n+1δA⁢A,1(1)-12r0n+1δAa,0(1)

The equations for δ˙A⁢A,1(1) and δ˙A⁢a,0(1) can be written in matrix form as

δ˙A⁢A,1(1)δ˙A⁢a,0(1)=r0n+1⁢-(1+p0)2n⁢(1+p0)41n-12δA⁢A,1(1)δA⁢a,0(1)⁢

The two eigenvectors (v0 and v-) and their corresponding eigenvalues (λ0 and λ-) are

v0=n2      λ0  = 0

v-= n⁢(1+p0)-2      λ-=-(2+p0)2⁢r0n+1

Notice that the dominant eigenvalue is equal to zero, so a computation to leading order in ϵ cannot provide information on the invasion of the recessive sterility allele.

We can also see this more formally. An arbitrary initial perturbation to a resident A population can be written as a linear superposition of the eigenvectors v0 and v-:

(25)δA⁢A,1(1)δA⁢a,0(1)=C0⁢n2+C-⁢n⁢(1+p0)-2⁢ exp -(2+p0)2⁢r0n+1⁢t

Here C0 and C− are constants. We can substitute (Equation 24) and (Equation 22) into (Equation 21), using the density constraints (Equation 18) and (Equation 23), keeping terms of order ϵ and ϵ2, and dividing each term by one factor of ϵ. We obtain

(26)-⁢δ˙A⁢A,0(1)-ϵ⁢δ˙A⁢A,0(2)⁢r0-(n+1)=2-n-n⁢p04⁢n-2δA⁢A,1(1)+nδA⁢a,0(1)+ϵ[2-n-n⁢p04⁢n-2δA⁢A,1(2)+nδA⁢a,0(2)+-2+n⁢p0n⁢δA⁢A,2(2)+r12⁢n⁢r0-1-n2+r12⁢n⁢r0-1-n4-2+n+(n-1)⁢p12⁢n⁢r12⁢n⁢r0-12⁢n⁢(2⁢n-1)⁢δA⁢a,1(2)-n⁢(1+p0)2⁢δa⁢a,0(2)+(1-p0)⁢[3+n⁢(1-p0)+p0]8⁢n⁢[δA⁢A,1(1)]2+n⁢(1+p0)⁢[3+n+(n-1)⁢p0]32⁢[δA⁢a,0(1)]2+3+n-(n-1)⁢p028δA⁢A,1(1)δA⁢a,0(1)]

We can again use the density constraints (Equation 18) and (Equation 23) to rewrite the left-hand side of (Equation 26). We can also substitute the general solution for the quantities δA⁢A,1(1) and δA⁢a,0(1), Equation 25, into the right-hand side of (Equation 26):

(27)-δ˙A⁢A,1(1)-δ˙A⁢a,0(1) r0-(n+1)+ϵ[-δ˙A⁢A,1(2)-δ˙A⁢a,0(2)-δ˙A⁢A,2(2)-δ˙A⁢a,1(2)-δ˙a⁢a,0(2)]r0-(n+1)=2-n-npo4n[-2(nC0+n1+poC-exp-(2+p0)2r0n+1t)+n(2C0-2C-exp(-(2+p0)2r0n+1t))]+ϵ[2-n-n⁢p04⁢n(-2δA⁢A,1(2)+nδA⁢a,0(2))+-2+n⁢p0n⁢δA⁢A,2(2)+r12⁢n⁢r0-1-n⁢[2+r12⁢n⁢r0-1-n⁢(4-(2+n+(n-1)⁢p12⁢n)⁢r12⁢n⁢r0-1)]2⁢n⁢(2⁢n-1)⁢δA⁢a,1(2)-n⁢(1+p0)2⁢δa⁢a,0(2)+(1-p0)⁢[3+n⁢(1-p0)+p0]8⁢n⁢[δA⁢A,1(1)]2+n⁢(1+p0)⁢[3+n+(n-1)⁢p0]32⁢[δA⁢a,0(1)]2+3+n-(n-1)⁢p028δA⁢A,1(1)δA⁢a,0(1)]

Note that each term in (Equation 27) involving the quantities δA⁢A,1(2), δA⁢a,0(2), δA⁢A,2(2), δA⁢a,1(2), and δa⁢a,0(2) is multiplied by ϵ. In the limit ϵ→0, the quantities δA⁢A,1(2), δA⁢a,0(2), δA⁢A,2(2), δA⁢a,1(2), and δa⁢a,0(2) do not affect the dynamics of the quantities δA⁢A,1(1) and δA⁢a,0(1). However, the quantities δA⁢A,1(1) and δA⁢a,0(1) alone tell us nothing about whether or not the recessive sterility allele invades a resident A population. Therefore, we must consider the terms of order ϵ2 in our dynamical equations (Equation 21) to determine if a rare a allele can invade a resident A population. In our calculations that follow, we use the eigenvector v0 corresponding to the zero eigenvalue, i.e.

(28)δA⁢A,1(1)δA⁢a,0(1)=δA⁢A,0(1)n+2⁢n2

Substituting (Equation 24), (Equation 22), and (Equation 28) into (Equation 21), using the density constraints (Equation 18) and (Equation 23), and keeping terms of order ϵ2, we have

(29)-δ˙A⁢A,0(2)⁢r0-(n+1)=2-n-np04n-2δA⁢A,1(2)-nδAa,0(2)+-2+n⁢p0n⁢δA⁢A,2(2)+r12⁢n⁢r0-1-n⁢[2+r12⁢n⁢r0-1-n⁢(4-(2+n+(n-1)⁢p12⁢n)⁢r12⁢n⁢r0-1)]2⁢n⁢(2⁢n-1)⁢δA⁢a,1(2)-n⁢(1+p0)2⁢δa⁢a,0(2)+n⁢(n+3)2⁢(n+2)2⁢[δA⁢A,0(1)]2

We also have

δ˙A⁢A,1(2)r0-(n+1)=1+p04-2δA⁢A,1(2)+nδAa,0(2)             +(1-p0)⁢δA⁢A,2                                             (2)+n[n+(n-1)⁢p12⁢n]2⁢(2⁢n-1)⁢ r12⁢n⁢r0-1⁢δA⁢a,1(2)+n⁢(1+p0)2⁢δa⁢a,0(2)                              -n⁢(n+1)(n+2)2⁢[δA⁢A,0(1)]2                            δ˙A⁢a,0(2)r0-(n+1)=-12n-2δA⁢A,1(2)+nδAa,0(2)                 +2n⁢δA⁢A,2(2)                                           +12⁢r12⁢n⁢r0-1⁢δA⁢a,1(2)                              +δa⁢a,0                                                                  (2)-2⁢n(n+2)2⁢[δA⁢A,0(1)]2                           δ˙A⁢A,2(2)⁢r0-(n+1)=-δA⁢A,2(2)+n⁢(n-1)2⁢(n+2)2⁢[⁢δAA,0(1)]2           δ˙A⁢a,1(2)⁢r0-(n+1) =-δA⁢a,1(2)+2⁢n(n+2)2⁢[δA⁢A,0(1)]2               δ˙aa,0(2)⁢⁢r0-(n+1)=-δa⁢a,0(2)+12⁢n⁢r12⁢n⁢r0-1⁢δA⁢a,1(2)

We can directly integrate the equation for δ˙A⁢A,2(2). We get

(30)δA⁢A,2(2)=n⁢(n-1)2⁢(n+2)2⁢[δA⁢A,0(1)]2⁢[1-exp -r0n+1t⁢]

We can also directly integrate the equation for δ˙A⁢a,1(2). We get

(31)δA⁢a,1(2)=2⁢n(n+2)2⁢[δA⁢A,0(1)]2⁢[1-exp -r0n+1⁢t]

We can use the solution for δA⁢a,1(2) to solve for δa⁢a,0(2). We get

(32)δa⁢a,0(2)=r12⁢nr0⁢(n+2)2⁢[δA⁢A,0(1)]2⁢[1-(1+r0n+1⁢t) ⁢exp (-r0n+1⁢t)]

Manipulating the equations for δ˙A⁢A,1(2) and δ˙A⁢a,0(2), we find that

r0-(n+1)dd⁢t⁢⁢(-2⁢δA⁢A,1(2)+n⁢δA⁢a,0(2))=-(2+p0)2(-2⁢δA⁢A,1(2)+n⁢δA⁢a,0(2))+2⁢p0⁢δA⁢A,2(2)-n⁢[1+2⁢(n-1)⁢p12⁢n]2⁢(2⁢n-1)⁢r12⁢n⁢r0-1⁢δA⁢a,1(2)-n⁢p0⁢δa⁢a,0(2)+2⁢n(n+2)2⁢[δA⁢A,0(1)]2

We can integrate this equation to solve for the quantity -2⁢δA⁢A,1(2)+n⁢δA⁢a,0(2). We obtain

(33)-2⁢δA⁢A,1(2)+n⁢δA⁢a,0(2)=[2⁢n⁢[p0-n⁢(1+2⁢p0+2⁢(n-1)⁢p12⁢n)]⁢r12⁢n⁢r0-1(n+2)2⁢(2+p0)⁢(2⁢n-1)+2⁢n⁢[2+(n-1)⁢p0](n+2)2⁢(2+p0)][δA⁢A,0(1)]2+[2⁢n⁢[2-3⁢n+2⁢(n-1)⁢n⁢p12⁢n]⁢r12⁢n⁢r0-1(n+2)2⁢p0⁢(2⁢n-1)-2⁢n⁢[n-1-r12⁢n⁢r0-1⁢(1+r0n+1⁢t)](n+2)2][δA⁢A,0(1)]2exp(-r0n+1t)+[4⁢n⁢[n⁢(3-2⁢(n-1)⁢p12⁢n)-2]⁢r12⁢n⁢r0-1(n+2)2⁢p0⁢(2+p0)⁢(2⁢n-1)+4⁢n⁢(n-2)(n+2)2⁢(2+p0)][δA⁢A,0(1)]2 exp -(2+p0)2r0n+1t

To determine if the resident A population is unstable to invasion by the a allele, we must consider the regime 1≪t≪ϵ-1. Notice that on a short time scale, each of the time-dependent terms in Equations 30–33 will approach zero. We must consider the sign of δ˙A⁢A,0(2) in the limit of large times t≫1 but before the terms in (Equation 22) become comparable in magnitude. Our condition for invasion of the sterility allele is therefore

(34)limϵ⁢t→0t→∞δ˙AA,0(2)>0

Substituting (Equations 29–33) into (Equation 34), we find that the recessive allele for worker sterility increases in frequency if

r12⁢nr0>2⁢(2⁢n-1)⁢(2+n+n⁢p0)2⁢n2⁢(2+p0+p12⁢n)+n⁢(3+3⁢p0-2⁢p12⁢n)-2⁢(1+p0)

In the Results, we focused on single and double mating. Figure 3A shows that fairly large efficiency increases from non-reproductive workers (around 10–20%) are needed for sterility to invade.

Figure 3A also shows how the number of matings affects the invasion of non-reproductive workers for different values of the parameters r1/4 and r1/2. Sample forms of the functions pz and rz are shown in Figure 7A,B. For Figure 7A, we have p0 = 0.8, p1/4 = 0.85, r0 = 1, r1/4 = 1.02, and r1/2 = 1.026; i.e., pz increases linearly in z, while rz increases sublinearly in z. For these values of pz and rz, sterility invades for double mating (n = 2) but not for single mating (n = 1). For Figure 7B, we have p0 = 0.8, p1/4 = 0.9, r0 = 1, r1/4 = 1.013, and r1/2 = 1.026; i.e., pz increases sublinearly in z, while rz increases linearly in z. For these values of pz and rz, sterility invades for double mating (n = 2) but not for single mating (n = 1).

In

![Figure 9.](https://cdn.elifesciences.org/articles/08918/elife-08918-fig9-v2.jpg)

**Figure 9.:** For double mating, n = 2, the invasion of a recessive worker sterility allele depends on the parameters p0, p1/4, and r1/4; for triple mating, n = 3, it depends on the parameters p0, p1/6, and r1/6. We set r0 = 1 as baseline.DOI: http://dx.doi.org/10.7554/eLife.08918.011

![Figure 10.](https://cdn.elifesciences.org/articles/08918/elife-08918-fig10-v2.jpg)

**Figure 10.:** n = 1), double mating (n = 2), and triple mating (n = 3) on the evolution of worker sterility.Whether or not triple mating favors the evolution of worker sterility depends on the functions p and zr. We consider a recessive mutant allele, za, for worker sterility. (A, B) For these parameter choices, the mutant allele causing worker sterility can invade for triple mating but not for double or single mating.DOI: http://dx.doi.org/10.7554/eLife.08918.012

## Stability of a dominant worker sterility allele

We assume that a dominant worker sterility allele has spread to fixation. We consider the evolutionary stability of a population consisting entirely of sterile workers to invasion by reproductive workers. What happens if we start with an infinitesimal quantity of the mutant allele, A, by perturbing the Xaa,n = 1 pure equilibrium: Xa⁢a,n→1-ϵ⁢δa⁢a,n(1), with ϵ≪1? Does the dominant worker sterility allele return to fixation, or is it invaded by the worker reproduction allele?

Although the state space is (3n + 2)-dimensional (3n + 3 types of colonies subject to the density constraint), the analysis simplifies. Provided that the perturbation is small (i.e. that ϵ≪1), only six colony types, aa,n, aa,n − 1, Aa,n, aa,n − 2, Aa,n − 1, and AA,n, determine whether or not the dominant worker sterility allele is stable. Any other colony type is headed by a queen that possesses at least three mutant A alleles (from her own genotype combined with the sperm she has collected), but such queens are so rare as to be negligible. The relevant equations among (Equation 11) for studying stability of a dominant sterility allele are

(35)X˙a⁢a,n=xa⁢a⁢yan-ϕ⁢Xa⁢a,nX˙a⁢a,n-1=n⁢xa⁢a⁢yan-1⁢yA-ϕ⁢Xa⁢a,n-1X˙A⁢a,n=xA⁢a⁢yan-ϕ⁢XA⁢a,nX˙a⁢a,n-2=n⁢(n-1)2⁢xa⁢a⁢yan-2⁢yA2-ϕ⁢Xa⁢a,n-2X˙A⁢a,n-1=n⁢xA⁢a⁢yan-1⁢yA-ϕ⁢XA⁢a,n-1X˙A⁢A,n=xA⁢A⁢yan-ϕ⁢XA⁢A,n

For analysis of the dominant sterility allele, terms of order ϵ do not provide sufficient information for determining whether the allele is stable, which adds a level of tedium to the calculation. Formally keeping track of powers of ϵ and ϵ2, and disregarding higher-order terms, we have:

(36)Xa⁢a,n=1-ϵ⁢δa⁢a,n(1)-ϵ2⁢δa⁢a,n(2)-O⁢(ϵ3)Xa⁢a,n-1=+ϵ⁢δa⁢a,n-1(1)+ϵ2⁢δa⁢a,n-1(2)+O(ϵ3)XA⁢a,n=+ϵ⁢δA⁢a,n(1)+ϵ2⁢δA⁢a,n(2)+O(ϵ3)Xa⁢a,n-2=+ϵ2⁢δa⁢a,n-2(2)+O(ϵ3)XA⁢a,n-1=+ϵ2⁢δA⁢a,n-1(2)+O(ϵ3)XA⁢A,n=+ϵ2⁢δA⁢A,n(2)+O⁢(ϵ3)

To determine the density constraints, we substitute (Equation 36) into (Equation 12) and collect powers of ϵ and ϵ2. At order ϵ, we get

(37)δa⁢a,n(1)=δa⁢a,n-1(1)+δA⁢a,n(1)

At order ϵ2, we get

(38)δa⁢a,n(2)=δa⁢a,n-1(2)+δA⁢a,n(2)+δa⁢a,n-2(2)+δA⁢a,n-1(2)+δA⁢A,n(2)

Next, we substitute (Equation 36) into (Equation 14), using the density constraints (Equation 37) and (Equation 38) and keeping terms up to order ϵ2:

(39)xa⁢a⁢r1-1=1+ϵ[-1nδa⁢a,n-1(1)-12δA⁢a,n(1)]+ϵ2[-1nδa⁢a,n-1(2)-12δA⁢a,n(2)-2nδa⁢a,n-2(2)+-2⁢n+(n-1)⁢r2⁢n-12⁢n⁢r1-12⁢nδA⁢a,n-1(2)-δA⁢A,n(2)]+O(ϵ3)xA⁢a⁢r1-1=ϵ[1nδa⁢a,n-1(1)+12δA⁢a,n(1)]+ϵ2[1nδa⁢a,n-1(2)+12δA⁢a,n(2)+2nδa⁢a,n-2(2)+r2⁢n-12⁢n⁢r1-12δA⁢a,n-1(2)+ δA⁢A,n(2)] + O(ϵ3) xA⁢A⁢r1-1=ϵ2[r2n-12nr1-12nδA⁢a,n-1(2)]+O(ϵ3)ya⁢r1-1=1+ϵ[-12δA⁢a,n(1)]+ϵ2[-12δA⁢a,n(2)+-2+p2⁢n-12⁢n⁢r2⁢n-12⁢n⁢r1-12δA⁢a,n-1(2)-δA⁢A,n(2)]+O(ϵ3)yA⁢r1-1=ϵ[12δA⁢a,n(1)]+ϵ2[12δA⁢a,n(2)+2-p2⁢n-12⁢n2r2⁢n-12⁢nr1-1δA⁢a,n-1(2)+ δA⁢A,n(2)]+O(ϵ3)

By plugging (Equation 39) and (Equation 36) into (Equation 35), using the density constraint (Equation 37), and collecting powers of ϵ, we find

δ˙a⁢a,n-1(1)=-r1n+1⁢δa⁢a,n-1(1)+n2⁢r1n+1⁢δA⁢a,n(1)

δ˙Aa,n(1)=1nr1n+1⁢δa⁢a,n-1(1)-12⁢r1n+1⁢δA⁢a,n(1)

The equations for δ˙a⁢a,n-1(1) and δ˙A⁢a,n(1) can be written in matrix form as

δ˙a⁢a,n-1(1)δ˙A⁢a,n(1)=r1n+1-1n21n-12⁢δa⁢a,n-1(1)δA⁢a,n(1)⁢

The two eigenvectors (v0 and v-) and their corresponding eigenvalues (λ0 and λ-) are

v0= n2     λ0=0

v-= n-1     λ-=-32⁢r1n+1

Notice that the dominant eigenvalue is equal to zero, so a computation to leading order in ϵ cannot provide information on the stability of the dominant sterility allele.

We can also see this more formally. An arbitrary initial perturbation to a resident A population can be written as a linear superposition of the eigenvectors v0 and v-:

(40)δa⁢a,n-1(1)δA⁢a,n(1)=C0⁢n2+C-n-1⁢⁢ exp -32⁢r1n+1⁢t

Here C0 and C- are constants. We can substitute (Equation 39) and (Equation 36) into (Equation 35), using the density constraints (Equation 37) and (Equation 38), keeping terms of order ϵ and ϵ2, and dividing each term by one factor of ϵ. We obtain

(41)[-⁢δ˙a⁢a,n(1)-ϵ⁢δ˙a⁢a,n(2)]⁢r1-(n+1)=1-n2n(-2δa⁢a,n-1(1)+nδA⁢a,n(1))+ϵ[1-n2⁢n(-2δa⁢a,n-1(2)+nδA⁢a,n(2))+n-2n⁢δa⁢a,n-2(2)+2⁢n-(1+n⁢(1+n⁢(2-p2⁢n-12⁢n)))⁢r2⁢n-12⁢n⁢r1-12⁢n⁢δA⁢a,n-1(2)-n⁢δA⁢A,n(2)+n⁢(n+1)8⁢[δA⁢a,n(1)]2+12δa⁢a,n-1(1)δA⁢a,n(1)]

We can again use the density constraints (Equation 37) and (Equation 38) to rewrite the left-hand side of (Equation 41). We can also substitute the general solution for the quantities δa⁢a,n-1(1) and δA⁢a,n(1), Equation 40, into the right-hand side of (Equation 41):

(42)[-δ˙a⁢a,n-1(1)-δ˙Aa,n(1)]⁢r1-(n+1)+ϵ[-δ˙a⁢a,n-1(2)-δ˙A⁢a,n(2)-δ˙a⁢a,n-2(2)-δ˙A⁢a,n-1(2)-δ˙A⁢A,n(2)]r1-(n+1)=1-n2n[-2(nC0+nC-exp (-32r1n+1t))+n(2C0-C-exp (-32r1n+1t))]+ϵ[1-n2⁢n(-2δa⁢a,n-1(2)+nδA⁢a,n(2))+n-2n⁢δa⁢a,n-2(2)+2⁢n-(1+n⁢(1+n⁢(2-p2⁢n-12⁢n)))⁢r2⁢n-12⁢n⁢r1-12⁢n⁢δA⁢a,n-1(2)-n⁢δA⁢A,n(2)+n⁢(n+1)8⁢[δA⁢a,n(1)]2+12δa⁢a,n-1(1)δA⁢a,n(1)]

Note that each term in (Equation 42) involving the quantities δa⁢a,n-1(2), δA⁢a,n(2), δa⁢a,n-2(2), δA⁢a,n-1(2), and δA⁢A,n(2) is multiplied by ϵ. In the limit ϵ→0, the quantities δa⁢a,n-1(2), δA⁢a,n(2), δa⁢a,n-2(2), δA⁢a,n-1(2), and δA⁢A,n(2) do not affect the dynamics of the quantities δa⁢a,n-1(1) and δA⁢a,n(1). However, the quantities δa⁢a,n-1(1) and δA⁢a,n(1) alone tell us nothing about whether or not the dominant sterility allele is stable against invasion by the mutant A allele. Therefore, we must consider the terms of order ϵ2 in our dynamical equations (Equation 35) to determine if the a allele is stable against invasion by the mutant A allele. In our calculations that follow, we use the eigenvector v0 corresponding to the zero eigenvalue, i.e.

(43)δa⁢a,n-1(1)δA⁢a,n(1)=δa⁢a,n(1)n+2n2

Substituting (Equation 39), (Equation 36), and (Equation 43) into (Equation 35), using the density constraints (Equation 37) and (Equation 38), and keeping terms of order ϵ2, we have

(44)-δ˙a⁢a,n(2)⁢r1-(n+1)=1-n2n(-2δa⁢a,n-1(2)+nδA⁢a,n(2))+n-2n⁢δa⁢a,n-2(2)+2⁢n-(1+n⁢(1+n⁢(2-p2⁢n-12⁢n)))⁢r2⁢n-12⁢n⁢r1-12⁢n⁢δA⁢a,n-1(2)-n⁢δA⁢A,n(2)+n⁢(n+3)2⁢(n+2)2⁢[δa⁢a,n(1)]2

We also have

δ˙a⁢a,n-1(2)⁢r1-(n+1)=12(-2⁢δa⁢a,n-1(2)+n⁢δA⁢a,n(2))+n⁢(2-p2⁢n-12⁢n)2⁢r2⁢n-12⁢n⁢r1-1⁢δA⁢a,n-1(2)+n⁢δA⁢A,n(2)-n⁢(n+1)(n+2)2⁢[δa⁢a,n(1)]2δ˙A⁢a,n(2)⁢r1-(n+1)=-12n(-2⁢δa⁢a,n-1(2)+n⁢δA⁢a,n(2))+2n⁢δa⁢a,n-2(2)+12⁢r2⁢n-12⁢n⁢r1-1⁢δA⁢a,n-1(2)+δA⁢A,n(2)-2⁢n(n+2)2⁢[δa⁢a,n(1)]2δ˙a⁢a,n-2(2)⁢r1-(n+1)=-δa⁢a,n-2(2)+n⁢(n-1)2⁢(n+2)2⁢[δa⁢a,n(1)]2δ˙A⁢a,n-1(2)⁢r1-(n+1)=-δA⁢a,n-1(2)+2⁢n(n+2)2⁢[δa⁢a,n(1)]2δ˙AA,n(2)r1-(n+1)=-δAA,n(2)+12⁢n⁢r2⁢n-12⁢n⁢r1-1⁢δA⁢a,n-1(2)

We can directly integrate the equation for δ˙a⁢a,n-2(2). We get

(45)δa⁢a,n-2(2)=n⁢(n-1)2⁢(n+2)2⁢[δa⁢a,n(1)]2⁢[1-exp (-r1n+1⁢t)]

We can also directly integrate the equation for δ˙A⁢a,n-1(2). We get

(46)δA⁢a,n-1(2)=2⁢n(n+2)2⁢[δa⁢a,n(1)]2⁢[1-exp (-r1n+1⁢t)]

We can use the solution for δA⁢a,n-1(2) to solve for δA⁢A,n(2). We get

(47)δA⁢A,n(2)=r2⁢n-12⁢nr1⁢(n+2)2⁢[δa⁢a,n(1)]2⁢[1-(1+r1n+1⁢t) ⁢exp (-r1n+1⁢t)]

Manipulating the equations for δ˙a⁢a,n-1(2) and δ˙A⁢a,n(2), we find that

r1-(n+1)dd⁢t⁢⁢(-2⁢δa⁢a,n-1(2)+n⁢δA⁢a,n(2))=-32(-2⁢δa⁢a,n-1(2)+n⁢δA⁢a,n(2))+2⁢δa⁢a,n-2(2)-n⁢(3-2⁢p2⁢n-12⁢n)2⁢r2⁢n-12⁢n⁢r1-1⁢δA⁢a,n-1(2)-n⁢δA⁢A,n(2)+2⁢n(n+2)2⁢[δa⁢a,n(1)]2

We can integrate this equation to solve for the quantity -2⁢δa⁢a,n-1(2)+n⁢δA⁢a,n(2). We obtain

(48)-2⁢δa⁢a,n-1(2)+n⁢δA⁢a,n(2)=[2⁢n⁢(n+1)3⁢(n+2)2-2⁢n⁢(1+n⁢(3-2⁢p2⁢n-12⁢n))⁢r2⁢n-12⁢n3⁢(n+2)2⁢r1][δa⁢a,n(1)]2-[2⁢n⁢(n-1)(n+2)2+2⁢n⁢(1-n⁢(3-2⁢p2⁢n-12⁢n)-r1n+1⁢t)⁢r2⁢n-12⁢n(n+2)2⁢r1][δa⁢a,n(1)]2  exp (-r1n+1t)+[4⁢n⁢(n-2)3⁢(n+2)2+4⁢n⁢(2-n⁢(3-2⁢p2⁢n-12⁢n))⁢r2⁢n-12⁢n3⁢(n+2)2⁢r1][δa⁢a,n(1)]2 exp (-32r1n+1t)

To determine if the resident a population is unstable to invasion by the A allele, we must consider the regime 1≪t≪ϵ-1. Notice that on a short time scale, each of the time-dependent terms in Equations 45–48 will approach zero. We must consider the sign of δ˙a⁢a,n(2) in the limit of large times t≫1 but before the terms in (Equation 36) become comparable in magnitude. Our condition for stability of the sterility allele is therefore

(49)limϵ⁢t→0t→∞δ˙a⁢a,n(2)<0

Substituting (Equations 44–48) into (Equation 49), we find that the dominant allele for worker sterility is evolutionarily stable if

r1r2⁢n-12⁢n>2+3⁢n-n⁢p2⁢n-12⁢n2⁢(n+1)

## Stability of a recessive worker sterility allele

We assume that a recessive worker sterility allele has spread to fixation. We consider the evolutionary stability of a population consisting entirely of sterile workers to invasion by reproductive workers. What happens if we start with an infinitesimal quantity of the mutant allele, A, by perturbing the Xaa,n = 1 pure equilibrium: Xa⁢a,n→1-ϵ⁢δa⁢a,n(1), with ϵ≪1? Does the recessive worker sterility allele return to fixation, or is it invaded by the worker reproduction allele?

Although the state space is (3n + 2)-dimensional (3n + 3 types of colonies subject to the density constraint), the analysis again simplifies. Provided that the perturbation is small (i.e. that ϵ≪1), only three colony types, aa,n, aa,n−1, and Aa,n, determine whether or not the recessive worker sterility allele is evolutionarily stable. Any other colony type is headed by a queen that possesses at least two mutant A alleles (from her own genotype combined with the sperm she has collected), but such queens are so rare as to be negligible. The relevant equations among (Equation 11) for studying stability of a recessive sterility allele are

(50)X˙a⁢a,n=xa⁢a⁢yan-ϕ⁢Xa⁢a,nX˙a⁢a,n-1=n⁢xa⁢a⁢yan-1⁢yA-ϕ⁢Xa⁢a,n-1X˙A⁢a,n=xA⁢a⁢yan-ϕ⁢XA⁢a,n

Formally keeping track of powers of ϵ, and disregarding higher-order terms, we have:

(51)Xa⁢a,n=1-ϵ⁢δa⁢a,n(1)-O(ϵ2)Xa⁢a,n-1=+ϵ⁢δa⁢a,n-1(1)+O⁢(ϵ2)XA⁢a,n=+ϵ⁢δAa,n(1)+O⁢(ϵ2)

Next, we substitute (Equation 51) into (Equation 15), using the density constraint (Equation 37) and keeping terms only up to order ϵ:

(52)xa⁢a=r1+ε(n-1)rn-1n -nr1nδa⁢a,n-1(1)+-2r1+r122δAa,n(1)+O(ε2)xA⁢a=εrn-1n nδa⁢a,n-1(1)+r122δAa,n(1)+O(ε2)ya=r1+ε-2r1+ (1+pn-1n)rn-1n2δa⁢a,n-1(1)+-2r1+r122δAa,n(1)+O(ε2)yA = ϵ  (1-pn-1n)rn-1n2δa⁢a,n-1(1)+r122δAa,n(1)+O(ε2)

By plugging (Equation 52) and (Equation 51) into (Equation 50), using the density constraint (Equation 37), and collecting powers of ϵ, we find

δ˙aa,n-1(1)=-2r1n+1+n(1-pn-1n)rn-1nr1n2δa⁢a,n-1(1)+nr12r1n2δA⁢a,n(1)

δ˙Aa,n(1)=rn-1n⁢r1nnδa⁢a,n-1(1)+-2⁢r1n+1+r12⁢r1n2δAa,n(1)

The equations for δ˙a⁢a,n-1(1) and δ˙A⁢a,n(1) can be written in matrix form as

δ˙a⁢a,n-1(1)δ˙A⁢a,n(1)=-2⁢r1n+1+n⁢(1-pn-1n)⁢rn-1n⁢r1n2n⁢r12⁢r1n2rn-1n⁢r1nn-2⁢r1n+1+r12⁢r1n2δa⁢a,n-1(1)δA⁢a,n(1)⁢

Setting the dominant eigenvalue to be greater than zero and simplifying, we find that the recessive allele for worker sterility is evolutionarily stable if

(53)r1rn-1n-n⁢(1-pn-1n)22r1r12⁢-1⁢>1

Figure 3B shows how the number of matings affects the evolutionary stability of non-reproductive workers for different values of the parameters r1/2 and r1. Sample forms of the functions pz and rz are shown in Figure 7C,D. For Figure 7C, we have p0 = 0.8, p1/2 = 0.92, r0 = 1, r1/2 = 1.016, and r1 = 1.045; i.e., pz increases sublinearly in z, while rz increases superlinearly in z. For these values of pz and rz, sterility is stable for double mating (n = 2) but not for single mating (n = 1). For Figure 7D, we have p0 = 0.8, p1/2 = 0.94, r0 = 1, r1/2 = 1.0225, and r1 = 1.045; i.e., pz increases sublinearly in z, while rz increases linearly in z. For these values of pz and rz, sterility is stable for double mating (n = 2) but not for single mating (n = 1).

## Numerical experiments

For additional insight, we perform random sampling of the parameter space to obtain some intuition whether evolution of non-reproductive workers is more or less likely for single or double mating. We will also evaluate the likelihood of selection favoring invasion or evolutionary stability of alleles (mutations) that induce non-reproductive workers. Thus, we do random sampling of the parameter regions shown in Figures 3A, 5A, and 8. In each case, the outcome depends on two efficiency values, which we call rz1 and rz2 with z1 < z2. For Figure 3A, those values are r1/4 and r1/2. For Figure 5A and for Figure 8, those values are r1/2 and r1.

The outcome of this numerical experiment depends on how we choose to randomize the colony efficiency values, rz1 and rz2. There are many ways to do this. Here, we consider two possibilities:

P⁢(rz⁢1,rz⁢2)=12⁢π⁢σ2⁢exp -[(rz⁢1-μ)2+(rz⁢2-μ)2]2⁢σ2

There is no correlation between rz1 and rz2. The average is μ = 1. We choose σ = 0.1 for Figure 3A. We choose σ = 0.2 for Figures 5A and 8.

P⁢(rz⁢1,rz⁢2)=12⁢π⁢σ2⁢1-ρ2⁢exp -[(rz⁢1-μ)2+(rz⁢2-μ)2-2⁢ρ⁢(rz⁢1-μ)⁢(rz⁢2-μ)]2⁢σ2⁢(1-ρ2)

We set ρ = 0.8. Now, there is positive correlation between rz1 and rz2. We choose μ and σ as for Procedure 1.

Table 1 shows the outcome of this numerical experiment for the parameter values used in Figures 3A and 8. Table 2 shows the outcome of this numerical experiment for the parameter values used in Figure 5A. For example, consider the first row of Table 1. We set p0 = 0.2 and p1/4 = 0.4 with a recessive sterility allele, as this corresponds with Figure 3A. Procedure 1 is used for selecting values of r1/4 and r1/2. For a randomly chosen pair of efficiency values r1/4 and r1/2, the probabilities that the sterility allele does not invade, invades only for n = 1, invades only for n = 2, and invades for n = 1 and n = 2 are 0.7769, 0.0644, 0.1465, and 0.0122, respectively. For the second row of Table 1, Procedure 2 is used for selecting values of r1/4 and r1/2. For a randomly chosen pair of efficiency values r1/4 and r1/2, the probabilities that the sterility allele does not invade, invades only for n = 1, invades only for n = 2, and invades for n = 1 and n = 2 are 0.8237, 0.0177, 0.0997, and 0.0589, respectively. The third and fourth rows of Table 1 and the rows of Table 2 are understood in the same way.10.7554/eLife.08918.013Table 1.Numerical experiments. We randomly select the two relevant colony efficiency values from a bivariate normal distribution. For Procedure 1, the two efficiency values are uncorrelated. For Procedure 2, they are correlated (with correlation 0.8). The results of the numerical experiment for Figures 3A and 8 are shown. For Figure 3A, which describes a recessive allele inducing non-reproductive workers, we randomly generate values for r1/4 and r1/2. For Figure 8, which describes a dominant allele inducing non-reproductive workers, we randomly generate values for r1/2 and r1. The table shows the likelihood of the four possible outcomes: non-reproductive workers (i) do not invade, (ii) invade for single mating but not for double mating, (iii) invade for double mating but not for single mating, and (iv) invade for both single and double mating. For this particular randomization experiment, double mating is more favorable than single mating for the invasion of non-reproductive workers. All p values are exactly as in the corresponding Figures.DOI: http://dx.doi.org/10.7554/eLife.08918.013Does notInvades for n = 1Invades for n = 2Invades for bothinvadebut not n = 2but not n = 1n = 1 and n = 2Figure 3A, Proc. 1, recessive0.77690.06440.14650.0122Figure 3A, Proc. 2, recessive0.82370.01770.09970.0589Figure 8, Proc. 1, dominant0.79440.01290.08300.1097Figure 8, Proc. 2, dominant0.79270.01460.02600.166710.7554/eLife.08918.014Table 2.Numerical experiments. With the equivalent Procedures, we explore the likelihood of the four scenarios regarding invasion and/or stability for single mating. Results of the numerical experiment for Figure 5A, describing a recessive allele, are shown. We randomly generate values for r1/2 and r1. The value p0 = 0.5 is exactly as in Figure 5A.DOI: http://dx.doi.org/10.7554/eLife.08918.014Does not invadeDoes not invadeInvadesInvadesand is unstablebut is stablebut is unstableand is stableFigure 5A, Proc. 1, recessive0.34840.30140.30070.0495Figure 5A, Proc. 2, recessive0.52950.12030.23790.1123

For both Procedures, we find that the invasion of non-reproductive workers is more likely favored for double mating, n = 2, than for single mating, n = 1.

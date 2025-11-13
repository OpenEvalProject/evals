# Spatial structure favors microbial coexistence except when slower mediator diffusion weakens interactions

## Authors

- Alexander Lobanov<sup>1</sup>
- Samantha Dyckman<sup>1</sup>
- Helen Kurkjian<sup>1</sup> ([ORCID: 0000-0002-3610-5344](https://orcid.org/0000-0002-3610-5344))
- Babak Momeni<sup>1</sup> ([ORCID: 0000-0003-1271-5196](https://orcid.org/0000-0003-1271-5196)) †

### Affiliations

1. Biology Department, Boston College Boston United States ([ROR:02n2fzt79](https://ror.org/02n2fzt79))
2. Department of Aquatic Ecology, Swiss Federal Institute of Aquatic Science and Technology Dübendorf Switzerland ([ROR:00pc48d59](https://ror.org/00pc48d59))

† Corresponding author

## Abstract

Microbes often exist in spatially structured environments and many of their interactions are mediated through diffusible metabolites. How does such a context affect microbial coexistence? To address this question, we use a model in which the spatial distributions of species and diffusible interaction mediators are explicitly included. We simulate the enrichment process, examining how microbial species spatially reorganize and how eventually a subset of them coexist. In our model, we find that slower motility of cells promotes coexistence by allowing species to co-localize with their facilitators and avoid their inhibitors. We additionally find that a spatially structured environment is more influential when species mostly facilitate each other, rather than when they are mostly competing. More coexistence is observed when species produce many mediators and consume some (not many or few) mediators, and when overall consumption and production rates are balanced. Interestingly, coexistence appears to be disfavored when mediators are diffusing slowly because that leads to weaker interaction strengths. Overall, our results offer new insights into how production, consumption, motility, and diffusion intersect to determine microbial coexistence in a spatially structured environment.

## Introduction

Microbes are rarely found in isolation in nature. Instead, they are found coexisting with one another in complex networks of interactions (Ma et al., 2020). Given the differences among taxa and the competitive forces that act between them, a fundamental question in microbial community ecology is how this coexistence is maintained (Chesson, 2000b; Solé and Bascompte, 2006; Widder et al., 2016). And because many important industrial, environmental, and health-related processes rely on microbial communities to function (e.g. anaerobic granules, microbial mats, and gut microbiota, respectively), understanding the conditions that favor microbial coexistence is critical to sustaining these systems.

Spatial structure and organization may shape coexistence via numerous mechanisms (Tilman, 1994; Durrett and Levin, 1994; Tilman and Kareiva, 1998; Durrett and Levin, 1998; Kerr et al., 2002; Brockhurst et al., 2006; Amarasekare, 2003), often by modulating the interactions among individuals. For example, in a spatially structured environment where progeny is more likely to be in the vicinity of parents, intensified intrapopulation competition can give less competitive species a chance to survive (Chesson, 2000a). In other conditions, spatial isolation can allow organisms with conflicting abiotic needs to flourish in appropriate environments (Kim et al., 2011; Satoh et al., 2007). The interplay between dispersal and competition can also allow coexistence between species that are more competitive growers and species that are better at dispersing and colonizing (Tilman, 1990).

Spatial heterogeneity has been invoked as a mechanism for microbial coexistence since the pioneering work by Gause, 1934. And although general concepts of coexistence are expected to apply equally to microbes, microbial communities may be affected by spatial structure in unique ways because of the scale and multiplicity of microbial interactions. An important and ubiquitous example of this are microbial interactions that are mediated via diffusible metabolites—including resources and metabolic byproducts. Spatial structure can stabilize these interactions and support coexistence, for example, by allowing cheaters to be excluded from beneficial interactions (Momeni et al., 2013b; Pande et al., 2016), or by permitting facilitative chemical interactions while preventing the inhibitory effects of an interacting organism’s physical presence (Kim et al., 2008). And while it is clear that the outcomes of interactions via diffusible mediators in structured environments may depend on mediator diffusion rates (Kümmerli et al., 2014; Allison, 2005) and the larger network of antagonistic and cooperative interactions (Nadell et al., 2016), how such factors translate into community-level consequences is not well understood.

Prior reports that address coexistence of metabolically interacting microbes in a spatially structured environment are scarce. In an implicit model, Murrell and Law, 2003 have shown in a modified Lotka–Volterra model that when interspecific competition operates over shorter distances than intraspecific competition a spatially structured environment can lead to species coexistence by allowing for aggregation. And in recent work with explicit modeling of space, Weiner et al., 2019 examined coexistence in territorial populations interacting through diffusible mediators and found that metabolic tradeoffs allow for the coexistence of more species than the number of nutrients.

Our model is distinct from previous work in that we allow overlap and dispersal of populations through the shared space. Our motivation is to capture situations in which microbes can disperse inside a matrix that defines the spatial structure. An example of this is the mucosal layer of the digestive or respiratory tract, in which stratification is possible, yet the distribution of different species populations can overlap. Another example is in yogurt or cheese, where spatial structure exists, but populations are not territorial. We modify a previously developed mediator-explicit model (Niehaus et al., 2019) to account for spatial structure and the dispersion of species in the same space. Here, we limit our study to one-dimensional (1D) spatial structure as a starting point. We examine in our model conditions under which coexistence is favored. We should emphasize that even though we choose our parameters within the range of typical values observed among microbial communities, the purpose of this work is not to recapture a specific community. Instead, by examining a range of values for parameters such as metabolite diffusion and species dispersal, we hope to gain a better understanding of how rates of these processes can affect species coexistence.

## Results

### A spatial mediator-explicit model of microbial communities

In our mediator-explicit model, species interact through metabolites that they produce and/or consume (Figure 1A, B; Niehaus et al., 2019). Each species can produce a subset of metabolites and consume a subset of metabolites. Each of the metabolites in the shared environment can in turn influence any of the species by increasing or decreasing their growth rate (i.e. facilitation or inhibition, respectively) compared to how each species grows in the absence of interactions (Niehaus et al., 2019). We also assume that different interaction mediators additively influence the overall growth rate of each species (see Model description in Methods).

![Figure 1.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig1-v2.jpg)

**Figure 1.:** (A) Species are engaged in metabolite-mediated interactions with other species. Each species produces a subset of mediators and consumes a subset. Each mediator can positively or negatively modulate the growth rate of the species it influences. In our model, consumption is present whenever there is an influence from a mediator on a species, regardless of whether the influence is facilitative or inhibitory. Production and consumption of mediators are indicated by open arrows. (B) In a one-dimensional (1D) spatial context, species and mediators are defined as functions of space that change over time because of population growth and dispersal as well as mediator production, consumption, and diffusion. A cartoon representation of the distributions of four species and three mediators are shown here over the spatial context (z). (C) Simulations were run at different ratios of facilitative to inhibitory interactions (fac:inh) for spatial (open blue squares) and well-mixed (filled blue circles) communities. Each ratio was run 500 times with the richness (number of species stably surviving at the end of a simulation) averaged over all the simulations. Each simulation started with 10 species and 5 mediators and ran for 100 generations. The error bars are 95% confidence intervals generated by bootstrapping 100 samples. Here, the species dispersal coefficient is $5\times10^{-9}$ cm2/hr. Boxes mark fac:inh ratios used in later simulations.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Here, we examine a simple case with five species and three mediators. Markers and error bars show mean and standard deviation of the percentage change in the community composition over 10 generations of growth (one round of growth between dilutions). There was minimal change (less than 1% difference) after 100 generations of growth in both well-mixed and spatial contexts. This observation was consistent regardless of the initial ratio of facilitation to inhibition interactions, at fac:inh = 10:90 (top), 50:50 (middle), and 90:10 (bottom). In all cases, DCell = 5 × 10−9 cm2/hr and DMed = 1.8 × 10−2 cm2/hr.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Similar to Figure 1C, simulations were run at different fac:inh ratios for both spatial communities (blue squares) and well-mixed communities (red circles). Each ratio was run 500 times with the richness (number of species stably surviving at the end of a simulation) averaged over all the simulations. Each simulation started with 10 species and 5 mediators and ran for 100 generations. The error bars are 95% confidence intervals generated by bootstrapping 100 samples. Here, the species dispersal coefficient is $5\times10^{-9}$ cm2/hr.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) Species are initially stacked over the spatial extent of the community. We examine a simple case with five species and three mediators (interaction network shown in the inset). Different progressions are observed at high (B, DCell = 5 × 10−6 cm2/hr) versus low (C, DCell = 5 × 10−9 cm2/hr) dispersal rates, leading to different coexistence outcome. In both cases, DMed = 1.8 × 10−2 cm2/hr.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** For simplicity, we consider an initial pool of five species with three mediators. We kept the same interaction network (A) in both spatial and well-mixed conditions and simulated the species dynamics. In the interaction network, hollow arrows indicate the flow of mediators (either production or consumption). The thickness of the lower end of each arrow shows the production rate and the thickness of the upper end of the arrow shows the strength of the mediator influence on the corresponding species. The basal growth rate of each species is shown as different shades of gray, with darker shades indicating larger basal growth rates. For spatial communities, the population density represents the sum of all densities across different spatial extents. We ran the simulation in both cases through 10 rounds of growth and dilution. Different population dynamics and ultimately different coexistence outcomes are observed in these cases after simulating 100 generations. Note that even though Species 4 and 5 in the spatial community and Species 1, 4, and 5 in the well-mixed community are still present in the final communities, because they exhibit a trend of decline in relative frequency, we consider them not to coexist (in accordance with our coexistence criterion, see Methods). (B, C) In this example, proximity of Species 1 to a beneficial Species 2 in the spatial community allows a strong boost in the growth of Species 1, leading to its coexistence with Species 2 and 3. In contrast, Species 1 in the well-mixed community receives a smaller portion of C1, not enough to allow Species 1 to keep up with the other species. In C, only coexisting species and mediators related to them are shown.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** For simplicity, we consider an initial pool of five species with three mediators, but rather than fac:inh = 90:10 in Figure 1—figure supplement 4, here we initially assign fac:inh = 10:90. We kept the same interaction network (A) in both spatial and well-mixed conditions and simulated the species dynamics. In the interaction network, hollow arrows indicate the flow of mediators (either production or consumption). The thickness of the lower end of each arrow shows the production rate and the thickness of the upper end of the arrow shows the strength of the mediator influence on the corresponding species. The basal growth rate of each species is shown as different shades of gray, with darker shades indicating larger basal growth rates. For spatial communities, the population density represents the sum of all densities across different spatial extents. We ran the simulation in both cases through 10 rounds of growth and dilution. Different population dynamics are observed in these cases. Note that even though Species 4 in the spatial community is still present in the final communities, because they exhibit a trend of decline in relative frequency, we consider them not to coexist (in accordance with our coexistence criterion, see Methods). (B, C) In this example, proximity of Species 1 to an inhibitory Species 2 in the spatial community leads to rapid exclusion of Species 1. Early extinction of Species 1 removes its inhibition of Species 4 and allows Species 4 to sustain longer in the spatial context compared to the well-mixed community. In C, only coexisting species and mediators related to them are shown.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** For simplicity, here we consider only two species engaged in commensalism (Species 1 providing a benefit to Species 2) through a single mediator (see insets). We examined a no-interaction control (A), versus when the species were initially close (B) or far (C) from each other within the spatial extent of the communities. All parameters are similar to Table 1, except the mediator diffusion coefficient which is chosen at DMed = 1.8 × 10−3 cm2/hr to exaggerate the impact of mediator diffusion in space. The panel on the left shows the initial distribution of the two populations in space and the panel on the right shows the population dynamics. Notably, the ratio of Species 1 to Species 2 drops by 10-fold, when Species 2 is farther away from Species 1 (C versus B). The basal growth rate of Species 1 and 2 are 0.1 and 0.08/hr, respectively. We ran the simulation for five rounds of growth and dilution.

![Figure 1—figure supplement 7.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig1-figsupp7-v2.jpg)

**Figure 1—figure supplement 7.:** All parameters other than the community’s spatial extent are kept fixed. Here, (A) DCell = 5 × 10−8 cm2/hr and (B) DCell = 5 × 10−9 cm2/hr. Legend shows the values of fac:inh assigned in the initial pool. In these simulations, the spatial resolution dz is kept at 0.05 mm in all cases and the initial extent of each species is 1/10th of the total spatial extent at the beginning of each simulation.

![Figure 1—figure supplement 8.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig1-figsupp8-v2.jpg)

**Figure 1—figure supplement 8.:** All parameters other than the local carrying capacity kY are kept fixed. Imposing a local carrying capacity on the total cell number (see the equations described in Methods) lowers the competitive advantage of the most successful species and allows more coexistence. This is similar to the idea of strengthened intrapopulation competition in a spatially structured environment that has been discussed in depth in the past as one of the reasons that spatial environments can support more coexistence. To focus on the effect of interspecies interaction, we assume kY = 109 cells/ml in our other simulations throughout this manuscript to minimize the impact of kY (i.e. a forced intrapopulation competition) on our results.

![Figure 1—figure supplement 9.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig1-figsupp9-v2.jpg)

**Figure 1—figure supplement 9.:** For simplicity, here we use the same examples as Figure 1—figure supplement 4 with five species and three mediators in the initial pool. We keep the same interaction network (A), but rearrange the initial order of species in the spatial community (original: 1, 2, 3, 4, 5; reorder: 1, 3, 4, 5, 2). We ran the simulation in both cases through 10 rounds of growth and dilution. Different population dynamics and ultimately different coexistence outcomes are observed in these cases after simulating 100 generations. Note that even though Species 4 and 5 in the original community and Species 1 and 3 in the reorder community are still present in the final communities, because they exhibit a trend of decline in relative frequency, we consider them not to coexist (in accordance with our coexistence criterion, see Methods). (B, C) In this particular example, after changing the order, Species 1 and 3 receive less of the benefits from Species 2, leading to the emergence of Species 2, 4, and 5 as an alternative stable coexistence. In C, only coexisting species and mediators related to them are shown.

We assume a 1D spatial structure which preserves the spatial context but allows the diffusion of metabolites and dispersal of species. Multiple metabolites and species can be present in a single location. Both metabolite diffusion and species dispersal are modeled as random walk processes, characterized with a diffusion coefficient and a dispersal coefficient, respectively. In a typical simulation, we start from an initial distribution in which populations occupy adjacent, non-overlapping spatial locations at low initial density. This choice is made to impose a reproducible initial condition that emphasizes the role of space. Each simulation starts with a network of interactions in which interaction strengths, production and consumption links, and production and consumption rates are assigned randomly. The initial pool typically contains 10 species and 5 interaction mediators. We simulate community enrichment through rounds of growth and dilution (Niehaus et al., 2019; Goldford et al., 2018) for 100 generations, and assess the richness of each resulting community (i.e., the number of species stably persisting in the community). We have chosen 100 generations of growth, because we have observed that often this is enough to reliably decide which species stably persist in the community (Figure 1—figure supplement 1). At each dilution step, we assume that the overall spatial distribution of the community is preserved and all populations at all locations are diluted with the same factor. We recognize that this assumption is not universally true; however, we adopt it as an approximation, in the absence of additional information about a particular community. Such a dilution preserves some of the spatial structure of the community in the next round of growth and could represent a biofilm getting partially washed away by rain or in a microfluidic device, gut microbiota after a defecation event, or a broken-off portion of a granule initiating a new granule. We use a well-mixed version (Niehaus et al., 2019)—devoid of any spatial context—with the same set of parameters for species properties and interactions (i.e. consumption and production rates, basal growth rates, mediator influences, etc.) for all comparisons. Figure 1—figure supplement 2 shows an example of the population distributions and dynamics during the course of enrichment. In a simple example, we show that interactions and subsequently the population dynamics are affected by growing in a well-mixed versus spatial environment (Figure 1—figure supplement 3). We explored the impact of the overall spatial extent of the community and found that within an order of magnitude of change, the outcomes remained the same (Figure 1—figure supplement 4).

The shift from interspecies competition to intraspecies competition can favor coexistence in a spatially structured environment. To assess this impact, we imposed a cap on total cell number at each location in space. As this cap became more restrictive, it suppressed the most competitive species and led to higher coexistence (Figure 1—figure supplement 5). Since our focus in this manuscript is the impact of interspecies interactions, in the rest of this manuscript we pick the total cell number cap at a level (kY = 109 cells/ml) that minimizes the impact of imposed intrapopulation competition.

### A spatial environment favors coexistence more when facilitation among species is prevalent

We first examined how the prevalence of facilitative versus inhibitory interactions impacted coexistence in spatial communities. In our simulations, we dictated the ratio of facilitative and inhibitory interactions in the initial pool of species. Our results show that, similar to a well-mixed environment, more facilitative interactions lead to higher richness in communities that emerge from enrichment (Figure 1C, along the x-axis). Additionally, we observe that spatial communities show more coexistence than well-mixed communities when facilitation among species is prevalent (Figure 1C, spatial versus well-mixed). The same pattern, although less pronounced, was present when instead of richness we used the Shannon index to assess the diversity of resulting communities (Figure 1—figure supplement 2). Our explanation is that species locally grow better when adjacent to a facilitative partner and grow worse when in the vicinity of an inhibitory partner. The resulting spatial self-organization in effect amplifies facilitative interactions and dampens inhibitory interactions, leading to more coexistence. This is supported by our data which shows that the position of specific species with respect to other species that facilitate or inhibit it can impact the population dynamics (Figure 1—figure supplement 8). Because of the marked impact of the fac:inh ratio (i.e. the ratio of the number of facilitative interactions to the number of inhibitory interactions), moving forward, we will examine three conditions, with equal fractions of facilitative and inhibitory influences (fac:inh = 50:50), mostly inhibitory (fac:inh = 10:90), or mostly facilitative (fac:inh = 90:10) to scope the impact on coexistence.

At low species dispersal, self-organization is one of the mechanisms that can lead to a difference between spatial and well-mixed communities (Figure 1—figure supplement 3). In a simplified interpretation, self-organization can be in the form of co-localization driven by facilitation or segregation driven by inhibition. In our simulations, we observed that co-localization had a stronger effect on coexistence. The positive influence was reinforced by more growth in the vicinity of the partner, leading to a stronger representation of facilitation in spatial communities. In contrast, segregation only had a modest effect on weakening the impact of inhibition. As a result, there is more similarity between well-mixed and spatial communities in the absence of strong facilitative interactions (Figure 1C).

### Coexistence is favored when many metabolites are produced and influence an intermediate number of species

Because metabolites are at the center of interspecies interactions in our model, we examined their impact on spatial coexistence of the average number of metabolites produced by each species and the average number of species influenced by each mediator. We found that coexistence is favored when the number of metabolites produced is larger (Figure 2, along the y-axis). This effect was stronger when the metabolite influences were mostly facilitative (fac:inh = 90:10, versus 50:50 or 10:90). In contrast, coexistence achieved its maximum values at intermediate ranges of mediator influence (Figure 2, x-axis), that is lower coexistence was observed when each mediator influenced too many or too few species on average. We note that these trends were largely the same between spatial and well-mixed communities.

![Figure 2.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig2-v2.jpg)

**Figure 2.:** Different ranges of production and mediator influence values were analyzed for both well-mixed and spatial communities at three different fractions of fac:inh influences in the initial pool of species (10:90, 50:50, and 90:10). Mean richness (i.e. average number of species stably present at the end of a simulation) was calculated for 500 simulated instances and marked on the color bar. Each simulation started with 10 species and 5 mediators and ran for 100 generations. The x-axis represents the average number of species influenced by a mediator and the y-axis represents the average number of mediators produced by each species. Other simulation parameters are listed in Table 1.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Different ranges of production and mediator influence values were analyzed for both well-mixed and spatial communities at three different fractions of fac:inh influences in the initial pool of species (10:90, 50:50, and 90:10). The ratio of spatial to well-mixed mean richness values is calculated for 500 simulated instances and marked on the color bar. Each simulation started with 10 species and 5 mediators and ran for 100 generations. The x-axis represents the average number of species influenced by a mediator and the y-axis represents the average number of mediators produced by each species.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Different ranges of production and mediator influence values were analyzed for both well-mixed and spatial communities at three different fractions of fac:inh influences in the initial pool of species (10:90, 50:50, and 90:10). Mean richness (i.e. average number of species stably present at the end of a simulation) was calculated for 500 simulated instances and marked on the color bar. Each simulation started with 10 species and 5 mediators and ran for 100 generations. The x-axis represents the average number of species influenced by a mediator and the y-axis represents the average number of mediators produced by each species. Here, the maximum interaction strength magnitude  $r_{int,0}$ = 0.05.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Different ranges of production and mediator influence values were analyzed for both well-mixed and spatial communities at three different fractions of fac:inh influences in the initial pool of species (10:90, 50:50, and 90:10). Mean richness (i.e. average number of species stably present at the end of a simulation) was calculated for 500 simulated instances and marked on the color bar. Each simulation started with 10 species and 5 mediators and ran for 100 generations. The x-axis represents the average number of species influenced by a mediator and the y-axis represents the average number of mediators produced by each species. Here, the maximum interaction strength magnitude  $r_{int,0}$ = 0.5.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** We separated the outcomes based on whether one (No coexistence) or more species (With coexistence) emerged from enrichment and examined the occurrence of self-facilitation. Occurrence is defined here as the average number of self-facilitation links (i.e. production of a mediator that benefits its producer) divided by the number of species present in the community. Each simulation started with 10 species and 5 mediators and ran for 100 generations. Here qc = 0.5 and qp = 0.5. Diamond markers (◊) show the occurrence in the initial pool of species before enrichment. The error bars are 95% confidence intervals generated by bootstrapping 100 samples using 500 total instances simulated. Mann–Whitney U test was used for comparison of occurrences between ‘No coexistence’ and ‘With coexistence’ cases to calculate the p values. More self-facilitation occurrence was associated with absence of coexistence when fac:inh was 50:50 or 90:10, but the reverse trend held when interactions within the initial pool were mostly inhibitory (fac:inh = 10:90).

Our explanation is that a larger range of production offers more opportunities for interaction, which through the enrichment process lead to the selection of facilitative subsets that coexist (Niehaus et al., 2019). A low mediator influence range works in the opposite direction, reduces opportunities for interactions and results in lower coexistence. Very high mediator influence range potentially leads to more self-facilitation (i.e. producing a metabolite that is beneficial to the producer species), which our data suggest can lead to take-over by a single species and a lower coexistence as a result (Figure 2—figure supplement 1).

### Coexistence is higher when there is balance between production and consumption of mediators

We next asked how the rates of production and consumption of mediators would influence coexistence. To address this question, we surveyed a range of average rates of production and consumption. We observed that the highest levels of coexistence occurred when there was a balance between consumption and production rates among species, with slightly higher production than consumption (Figure 3).

![Figure 3.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig3-v2.jpg)

**Figure 3.:** Different average production and consumption rates were analyzed for both well-mixed and spatial communities at three different fractions of fac:inh influences in the initial pool of species (10:90, 50:50, and 90:10). Mean richness (i.e. average number of species stably present at the end of a simulation) is calculated for 500 simulated instances. Each simulation started with 10 species and 5 mediators and ran for 100 generations. Color bar represents the average richness. The x-axis represents the average production rate of mediators and the y-axis represents the average consumption rate of mediators. Other simulation parameters are listed in Table 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Different average production and consumption rates were analyzed for both well-mixed and spatial communities at three different fractions of fac:inh influences in the initial pool of species (10:90, 50:50, and 90:10). The ratio of spatial to well-mixed mean richness values is calculated for 500 simulated instances and marked on the color bar. Each simulation started with 10 species and 5 mediators and ran for 100 generations. The x-axis represents the average production rate of mediators and the y-axis represents the average consumption rate of mediators.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Different average production and consumption rates were analyzed for both well-mixed and spatial communities at three different fractions of fac:inh influences in the initial pool of species (10:90, 50:50, and 90:10). Mean richness (i.e. average number of species stably present at the end of a simulation) is calculated for 500 simulated instances. Each simulation started with 10 species and 5 mediators and ran for 100 generations. Color bar represents the average richness. The x-axis represents the average production rate of mediators and the y-axis represents the average consumption rate of mediators. Here, the maximum interaction strength magnitude  $r_{int,0}$ = 0.05.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Different average production and consumption rates were analyzed for both well-mixed and spatial communities at three different fractions of fac:inh influences in the initial pool of species (10:90, 50:50, and 90:10). Mean richness (i.e. average number of species stably present at the end of a simulation) is calculated for 500 simulated instances. Each simulation started with 10 species and 5 mediators and ran for 100 generations. Color bar represents the average richness. The x-axis represents the average production rate of mediators and the y-axis represents the average consumption rate of mediators. Here, the maximum interaction strength magnitude  $r_{int,0}$ = 0.5.

Our justification for the observed pattern is that in one extreme where production is too high (lower right corner of each plot), mediators will build up in the environment. This will put the community in a regime in which consumption is not enough to create a feedback, that is ‘reusable mediators’ as discussed in Niehaus et al., 2019, which leads to lower coexistence. In the other extreme, when consumption is too high (upper left corner of each plot), metabolites that mediate the interactions will be depleted from the environment, leading to an effectively weaker interaction and thus lower coexistence. However, when production is slightly higher than consumption, metabolite quantities are sufficient to create strong interactions and facilitation feedbacks, leading to higher coexistence. While coexistence is slightly higher in the spatial communities compared to well-mixed ones, the production–consumption trends apply equally to spatial and well-mixed communities, as expected.

### Limited species dispersal in a spatial environment allows more coexistence, especially when facilitation is common

Because species dispersal is a major factor in preserving community spatial structure, we examined how the dispersal coefficient affected coexistence outcomes. For this, we kept the diffusion coefficient of the mediators fixed and surveyed mean richness among many instances of communities randomly assembled (n = 500). When the diffusion coefficient for species approaches zero and cells remain in their original spatial location, we observe higher levels of coexistence (Figure 4). We also observed that the impact of lower dispersal is stronger in communities in which most interactions are facilitative rather than inhibitory. Our explanation is that lower dispersal rates mean that species grow best in spatial locations that are more supportive for their growth, which is in the vicinity of their beneficial partners and away from competitors or inhibitors. As discussed in Figure 1, such self-organization effectively amplifies facilitative interactions and de-emphasizes inhibitory interactions, leading to a higher coexistence. This is also consistent with the observation that the effect of dispersal rate is strongest when the proportion of facilitative interactions is highest. As the dispersal coefficient increases, the self-organization gets washed away by dispersal of cells to less than ideal locations for their growth and its benefit for coexistence diminishes.

![Figure 4.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig4-v2.jpg)

**Figure 4.:** Communities in spatially structured environments were simulated with different dispersal coefficients at three different fractions of fac:inh influences (10:90, 50:50, and 90:10). Mean richness (i.e. average number of species stably present at the end of a simulation) was calculated for 500 simulated instances. Each simulation started with 10 species and 5 mediators and ran for 100 generations. Other simulation parameters are listed in Table 1. The error bars are 95% confidence intervals generated by bootstrapping 100 samples.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Communities in spatially structured environments were simulated with different dispersal coefficients at three different fractions of fac:inh influences (10:90, 50:50, and 90:10). Mean richness (here based on the average number of species present at the end of a simulation) was calculated for 500 simulated instances. Each simulation started with 10 species and 5 mediators and ran for 100 generations (top) or 200 generations (bottom). Other simulation parameters are listed in Table 1. The error bars are 95% confidence intervals generated by bootstrapping 100 samples. As expected, assessing species presence after 200 generations shows lower richness compared to 100 generations, since some species go extinct during the additional 100 generations. Nevertheless, both cases show a decreasing richness in spatial communities with larger dispersal coefficients (still richness stays higher than the well-mixed levels).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** For these cases, we use fac:inh = 90:10, because it showed the strongest change at intermediate dispersal values. Mean richness (i.e. average number of species stably present at the end of a simulation) was calculated for 500 simulated instances. In each instance, we simulated the enrichment and coexistence in the baseline case (100% ρij) as well as the same community when for self-facilitation links, the influence of the corresponding mediator on its producer was reduced by a factor of 5 (20% ρij). This is shown visually in the top schematic. This allows us to assess the impact of self-facilitation links in different conditions. We acknowledge that this assessment is not perfect, because weakening self-facilitation links in this way also reduces the beneficial influence of other species on Si that may happen via Cj. Nevertheless, we observe that at intermediate dispersal levels (Intermed. Dispersal, spatial; DCell = 5 × 10−6 cm2/hr), weakening self-facilitation links leads to more coexistence. In contrast, this effect is absent when dispersal levels are low (Low dispersal, spatial; DCell = 5 × 10−9 cm2/hr) or in well-mixed communities (Well-mixed). Each simulation started with 10 species and 5 mediators and ran for 100 generations. Other simulation parameters are listed in Table 1. The error bars are 95% confidence intervals generated by bootstrapping 100 samples.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** For each of the cases of (A) fac:inh = 10:90, (B) fac:inh = 50:50, and (C) fac:inh = 90:10, we simulated 100 instances and in each instance, we examined coexistence outcome (final richness) in 100 permutations of the order of species (as an example, 10, 3, 6, 1, 5, 7, 4, 2, 9, 8 would be a permutation of the order of the 10 species). Asterisks (*) show the calculated richness for the corresponding well-mixed community, and the circle (o) and the error bar show the mean and standard deviation of the richness values obtained for the 100 permutations tested. Overall, we observe that it is common to reach a different richness value when the order of species is changed.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** Similar to Figure 4—figure supplement 3, we simulated 100 instances each of fac:inh = 10:90, 50:50, and 90:10, and in each instance, we examined coexistence outcome (final richness) in 100 permutations of the order of species. Red circles (○) show the calculated richness for the corresponding well-mixed community, and the blue filled circles (●). The standard deviation of the richness values obtained for the 100 permutations are shown in (A). The 95% confidence interval for the slope of the standard deviation of richness with respect to fp was 1.01 ± 0.13. The trend was maintained for the coefficient of variations of the 100 permutations as well (B). The 95% confidence interval for the slope of the standard deviation of richness with respect to fp was 0.48 ± 0.10. The Matlab function fitlm was used to estimate the slope and its standard error. Confidence intervals are calculated as $i_{t}0.975,N-2∙SE$, where $i_{t}$ is the inverse t coefficient, $N$ is the number of data points, and SE is the standard error of the slope.

At intermediate levels of dispersal, the trend reversed and well-mixed communities showed more coexistence compared to spatial communities. This is interesting because at the limit of extremely rapid diffusion (shown with a ‘∞’ sign in Figure 4) when we kept the species distribution uniform across the spatial extent, coexistence outcomes matched the well-mixed case, as expected. We found two factors that contributed to this trend. The first contribution came from longer-term changes in dynamics at intermediate levels of dispersal. Even after 100 generations, which is the typical extent of our studies, at intermediate levels of dispersal (e.g. DCell = 5 × 10−6 cm2/hr), the spatial distribution of populations is still changing considerably. As a result, our strict criteria for stable coexistence removes some of the populations that are still temporally not stable enough, leading to a lower overall assessment of coexistence in these cases. To show this, we examined the range of dispersal coefficients again, but kept all the species that were present after 100 generations, rather than those with stable population fractions at that point (see Model implementation in Methods). The results show that higher dispersal coefficients using this measure lowers the richness of resulting communities (based on presence, rather than stable presence), but not below the levels expected from well-mixed communities (Figure 4—figure supplement 1). As a second factor, we hypothesized that self-facilitation interactions contribute to the decrease in coexistence at intermediate dispersal levels. Our rationale was that self-facilitation interactions are amplified in communities in which the spatial context is preserved, because the distribution of producers matches the distribution of self, but not other recipients in such a case. This can lead to community overtake by a self-facilitating species. This effect will be weaker in communities at intermediate dispersal rates: at low dispersal rates self-facilitating species will be more confined in space and some of the metabolite will leak out to other species; in the other extreme, in the very high dispersal rates all distributions will become uniform and the distinction between self and others diminishes. To test this, we tested weaker self-facilitation links in our simulations and observed that this change led to higher coexistence in communities with intermediate dispersal coefficients but not in well-mixed communities or communities with low dispersal coefficients (Figure 4—figure supplement 2). It is a matter of debate how prevalent self-facilitation interactions are within microbial communities. Self-facilitation interactions do exist, for example when a species breaks down a recalcitrant substrate such as cellulose into smaller molecules that can be beneficial. However, if they are not as prevalent as what our model assumes, some of our predictions might be affected.

### Coexistence is disrupted when the diffusion of mediators is too slow

The rate of diffusion of metabolites also has the potential to affect coexistence. We investigated coexistence over a range of mediator diffusion coefficients. We still typically observe a higher mean richness for spatial communities compared with the well-mixed communities (Figure 5). However, unlike the conventional wisdom, as the diffusion of mediators becomes slower, coexistence in spatial communities decreases. At low diffusion coefficients, coexistence drops even below that of corresponding well-mixed communities. We associate this trend to weaker effective interactions among species at lower diffusion coefficients. Mediators that are involved in facilitation play a major part in allowing coexistence of species (Niehaus et al., 2019); if these mediators get consumed by nearby species and do not travel long enough to reach other members of the community, the interaction-driven mechanism of coexistence is disrupted.

![Figure 5.](https://cdn.elifesciences.org/articles/82504/elife-82504-fig5-v2.jpg)

**Figure 5.:** A range of metabolite diffusion coefficients were simulated in spatial communities (squares) at three different fractions of fac:inh influences (10:90, 50:50, and 90:10). We simulated corresponding well-mixed communities (circles) for comparison. Each condition was run 500 times with the richness (number of species stably surviving at the end of a simulation) averaged over all the simulations. Each simulation started with 10 species and 5 mediators and ran for 100 generations. Other simulation parameters are listed in Table 1. The error bars are 95% confidence intervals generated by bootstrapping 100 samples.

## Discussion

Our results dispel the common presumption that a spatially structured environment will universally lead to more coexistence. We find that, compared to a well-mixed environment, a spatial environment can favor or disfavor coexistence depending on the balance between species dispersal and the diffusion of interaction mediators. Interestingly, a lower species dispersal rate favors coexistence, but this effect can be diminished or even reversed if accompanied by low mediator diffusion rates. Coexistence is favored when species have a broad range of consumption and an intermediate range of production of interaction mediators. Additionally, we predict more coexistence when there is a balance between overall production and consumption rates for mediators.

The spatial structure of microbial communities has been extensively studied for example in simulating the development of biofilms (Wang and Zhang, 2010; Kreft et al., 2001; Xavier and Foster, 2007; von der Schulenburg et al., 2009), for specific interactions among species (Momeni et al., 2013b; Momeni et al., 2013a; Kang et al., 2014), or for modeling game-theory dynamics (Nakamaru et al., 1997; Brauchli et al., 1999; Saxer et al., 2009; Hauert and Doebeli, 2004). However, as there is often a tradeoff between the incorporation of detailed mechanisms and generality of conclusions (Levins, 1966; Momeni et al., 2011), we chose in this work to explore a simple, general model of chemically mediated microbial interactions. We assumed, for example, that mediators affected species by additively influencing their growth rates. Although it is possible (and even probable) that mediator effects could be multiplicative, nonlinear, or otherwise context dependent and that they may impact other model parameters, we chose here to present what we felt to be the simplest case. Exploration of alternative implementations of mediator effects would make a fascinating follow-up to this work.

We have made assumptions in our model to simplify the configuration and make the analyses and interpretations easier. We asked if making these assumptions more realistic would affect our conclusions. For example, we have assumed no carrying capacity limit for the growth of our populations. We explored the effect of imposing a total population limit, enforced at each spatial location, and found that it did alter our conclusions (Figure 1—figure supplement 5). However, because the relationship between carrying capacity and coexistence has been explored extensively elsewhere, we chose parameters to minimize this impact, allowing us to focus on other interspecies interactions (beyond competition) and relative rates of diffusion and dispersal. We also tested the impact of the spatial extent of the community (Z), and observed that our results were largely unaffected if the community’s spatial extent was changed by an order of magnitude (Figure 1—figure supplement 4). The effect of larger changes in the spatial extent can be examined by scaling the diffusion and dispersal coefficients accordingly.

Beyond the details of our assumptions, there are also alternative representations of interactions among species, including a simplified Lotka–Volterra model and its variations (Wangersky, 1978), a consumer-resource model (Goldford et al., 2018; Marsland et al., 2019), or a reduced metabolic model (Liao et al., 2020). There are trade-offs in tractability and complexity in choosing which model to use. Our reasoning for adopting the mediator-explicit model was to (1) explicitly include metabolites that mediate the interactions in the model (Momeni et al., 2017); (2) incorporate both metabolites that support the growth of other species as well as those that are inhibitory, such as waste products and toxins (Momeni et al., 2017); and (3) keep the model simple to allow a clear interpretation of mechanisms and processes when analyzing the results. We think it will be worthwhile to compare the predictions of other models to clarify what assumptions are necessary to generate the trends we have obtained and how general the conclusions are.

If spatial organization of cells matters, we also expect that the initial spatial position of species in the community impacts coexistence. To test this, we started from 100 simulations instances and in each case, we tried 100 rearrangements, each obtained by shuffling the spatial position of species, while keeping the species properties and interactions intact. Interestingly, in many cases coexistence was affected (Figure 4—figure supplement 3), indicating that the adjacency to partners is an important determinant of spatial coexistence (as also suggested by Figure 1—figure supplement 3 and Figure 1—figure supplement 7). When we examined the effect of the fac:inh ratio on these outcomes, we observed that larger changes in richness when facilitation interactions were more prevalent in the community (Figure 4—figure supplement 4), which aligns with many of our other results showing that facilitation amplifies the positive effect of spatial structure on coexistence. Although these results are tantalizing, a detailed examination of the spatial organization of populations and metabolites within the community requires a dedicated investigation and is beyond the scope of this work.

Finally, our model assumes that dispersal and diffusion rates are uniform across species and metabolites, respectively. However, dispersal ability can vary widely across microbial taxa, depending on cell size, motility type, chemotaxis, quorum sensing, and other factors. And how the dispersal rates of individuals scale up to affect population- and community-level dynamics is not well understood. Likewise, the diffusion rates of metabolites have the potential to vary greatly with molecule size and shape. Although outside the scope of this work, we are exploring heterogeneity in these rates of movement as an interesting follow-up.

Overall, we believe this work revisits how spatial structure—and spatial self-organization—affects community assembly and coexistence. In our model, which emphasizes the contributions of interspecies interactions, we find that the impact of spatial structure on coexistence largely arises from two processes: (1) spatial self-organization, which can improve coexistence by favoring facilitation over inhibition, and (2) localization of interactions, which can promote coexistence in association with self-organization or hamper coexistence by slowing down and weakening species interactions.

## Methods

### Model description

Our model is an extension of a model introduced earlier (Niehaus et al., 2019) in which a set of species interact with each other through diffusible mediators. Each mediator is produced by a subset of species, consumed by a subset of species, and has a positive or negative influence on the growth rate of some species (Figure 1).

$$
\frac{dS_{i}(z,t)}{dt}=D_{Cell}\frac{d^{2}S_{i}(z,t)}{dz^{2}}+(1−\frac{\sumj=1MS_{j}(z,t)}{k_{Y}})[r_{i0}+\sumj=1Mρ_{ij}(\frac{C_{j}(z,t)}{k_{sat}}\delta_{ij}^{−}+\frac{C_{j}(z,t)}{C_{j}(z,t)+k_{sat}}\delta_{ij}^{+})]S_{i}(z,t)
$$



$$
\frac{dC_{j}z,t}{dt}=D_{Med}\frac{d^{2}C_{j}z,t}{dz^{2}}+\sum_{j=1}^{M}\beta_{ji}S_{i}z,t-\alpha_{ji}S_{i}z,t
$$

Here, $S_{i}$ is the spatiotemporal density of species i (i = 1, …, Nc). $C_{j}$ is the spatiotemporal concentration of mediator j (j = 1, …, Nm). DCell is the dispersal coefficient for cells. DMed is the diffusion coefficient for mediators. $k_{Y}$ is the local carrying capacity (for the total density of cells) at each location. $ρ_{ij}$ is the interaction coefficient expressed as the impact of mediator j on species i. Additionally,

$$
\delta_{ij}^{−}={1,ρ_{ij}<00,ρ_{ij}>0 and \delta_{ij}^{+}={0,ρ_{ij}<01,ρ_{ij}>0
$$

$k_{sat}$ is the interaction strength saturation level. $\beta_{ji}$ and $\alpha_{ji}$ are average production rate and consumption rates, respectively, between species i and mediator j. Similar to Niehaus et al., 2019, each species has a basal growth rate (in the absence of interactions with other species), and influential mediators additively modulate this growth rate. At z = 0 and z = Z, no-flow boundary conditions are enforced for both species and mediators by setting the local spatial derivatives of these parameters to zero at the boundaries.

Typical parameters used in our simulations (unless otherwise stated) are listed in Table 1. These parameters are chosen in the expected realistic range of values; for example, the typical diffusion coefficient of small molecules in water is in the range of 100–1000 µm2/s, and we have used 500 µm2/s as a generic value. When comparing spatial communities with their well-mixed counterparts, exactly the same parameters for basal growth rates, production and consumption rates, mediator influences, and networks of production and consumption are used. This choice is made to reduce the stochasticity caused by other parameters and to focus only on the impact of spatial structure.

**Table 1.**
 Parameters used in our simulations are listed.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Value (unit)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Number of instances examined (Ns)</td>
      <td>500</td>
    </tr>
    <tr>
      <td>Number of cell types in the initial pool (Nc)</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Number of interaction mediators (Nm)</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Total initial cell density (TID)</td>
      <td>104 (cells/ml)</td>
    </tr>
    <tr>
      <td>Interaction strength saturation level (ksat)</td>
      <td>104 (cells/ml)</td>
    </tr>
    <tr>
      <td>Population extinction threshold (ExtTh)</td>
      <td>0.1 (cells/ml)</td>
    </tr>
    <tr>
      <td>Population dilution threshold (DilTh)</td>
      <td>107 (cells/ml)</td>
    </tr>
    <tr>
      <td>Consumption rate (αij)</td>
      <td>0.075–2.25 (fmol per cell per hour; avg. 0.15)Stochastic with a uniform distribution</td>
    </tr>
    <tr>
      <td>Production rate (βij)</td>
      <td>0.1–0.2 (fmol per cell per hour; avg. 0.1)Stochastic with a uniform distribution</td>
    </tr>
    <tr>
      <td>Probability of production link per population (qp)</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>Probability of influence link per mediator (qc)</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>Maximum interaction strength magnitude (rint,0)</td>
      <td>0.2 (1/hr)</td>
    </tr>
    <tr>
      <td>Basal growth rate of species (r0)</td>
      <td>0.1–0.2 (1/hr); stochastic with a uniform distribution</td>
    </tr>
    <tr>
      <td>Number of generations for enrichment (nGen)</td>
      <td>100</td>
    </tr>
    <tr>
      <td>Dispersal coefficient for cells (DCell)</td>
      <td>5 × 10−9 (cm2/hr)</td>
    </tr>
    <tr>
      <td>Diffusion coefficient for mediators (DMed)</td>
      <td>1.8 × 10−2 (cm2/hr)</td>
    </tr>
    <tr>
      <td>Local carrying capacity per dz (kY)</td>
      <td>109 cells/ml</td>
    </tr>
    <tr>
      <td>Total community spatial extent (Z)</td>
      <td>0.5 cm</td>
    </tr>
    <tr>
      <td>Spatial resolution for species distributions (dz)</td>
      <td>0.005 cm</td>
    </tr>
    <tr>
      <td>Cell growth update and uptake timescale (dtau)</td>
      <td>0.01 hr</td>
    </tr>
    <tr>
      <td>Mediator diffusion time-step (dt)</td>
      <td>0.1dz2/DMed</td>
    </tr>
    <tr>
      <td>Cell dispersal simulation time-step (dc)</td>
      <td>0.1dz2/DCell</td>
    </tr>
  </tbody>
</table>

To sample different possibilities, the interaction terms as well as production and consumption rates are randomly assigned in each instance of the simulation. Similar to our previous work (Niehaus et al., 2019), the production/consumption matrices are random, that is each element of the matrix has a binomial distribution with a fixed probability of being present ($q_{p}$ and $q_{c}$ for production and consumption/influence links, respectively). The production and consumption rates have a uniform distribution between 0.5 and 1.5 times a set value each ($\beta_{ij}$ and $\alpha_{ij}$ for production and consumption rates, respectively). The interaction matrix which represents the influence of mediators on species has the same structure as the consumption matrix. The magnitude of the influence in this matrix has a uniform distribution between 0 and a maximum value, $r_{int,0}$ . The sign of the influence is chosen from a binomial distribution based on the ratio of fac:inh.

### Model implementation

We solve the equations in ‘Model description’ numerically in Matlab using a finite difference discrete version of the equations. Mediator diffusion and cell dispersal take place often at very different time scales. To simulate these processes, we use different numerical time-steps to update the mediator and cell distributions. To allow flexibility in modeling different diffusion and dispersal coefficients, we used asynchronous updates with two independent time-steps: one for updating the diffusion of metabolites and another one for growth and dispersal of cells. The source codes are shared for transparency and reproducibility (see Code availability).

To assess coexistence, we use a criterion similar to Niehaus et al., 2019. In short, any species whose density drops below a pre-specified extinction threshold (ExtTh) is considered extinct. Among species that persist throughout the simulation, only those are considered to coexist whose relative frequency does not decrease by more than 10% of its value in the last 20 generations of the simulation. We consider these species to be ‘stably present’ in the community. Species whose relative frequency declines faster than this threshold are assumed to go extinct later and are not considered to be part of coexisting communities. The only exception to this criterion is the data in Figure 4—figure supplement 1, in which all present species (rather than stably present species) are included in the assessment of final richness.

### Statistics

Mean richness values are calculated by averaging the richness values calculated over all simulated instances for a given condition. Confidence intervals for mean richness values are calculated by bootstrapping over all simulated instances for a given condition. The standard routine in Matlab, bootci, is used in all cases for bootstrapping.

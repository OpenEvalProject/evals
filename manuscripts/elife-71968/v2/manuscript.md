# The evolution of division of labour in structured and unstructured groups

## Authors

- Guy Alexander Cooper<sup>1</sup> ([ORCID: 0000-0002-1748-8183](https://orcid.org/0000-0002-1748-8183)) †
- Hadleigh Frost<sup>3</sup>
- Ming Liu<sup>2</sup> ([ORCID: 0000-0002-5170-8688](https://orcid.org/0000-0002-5170-8688))
- Stuart Andrew West<sup>2</sup> ([ORCID: 0000-0003-2152-3153](https://orcid.org/0000-0003-2152-3153))

### Affiliations

1. St John's College Oxford United Kingdom
2. Department of Zoology, University of Oxford Oxford United Kingdom
3. Mathematical Institute, University of Oxford Oxford United Kingdom

† Corresponding author

## Abstract

Recent theory has overturned the assumption that accelerating returns from individual specialisation are required to favour the evolution of division of labour. Yanni et al., 2020, showed that topologically constrained groups, where cells cooperate with only direct neighbours such as for filaments or branching growths, can evolve a reproductive division of labour even with diminishing returns from individual specialisation. We develop a conceptual framework and specific models to investigate the factors that can favour the initial evolution of reproductive division of labour. We find that selection for division of labour in topologically constrained groups: (1) is not a single mechanism to favour division of labour—depending upon details of the group structure, division of labour can be favoured for different reasons; (2) always involves an efficiency benefit at the level of group fitness; and (3) requires a mechanism of coordination to determine which individuals perform which tasks. Given that such coordination must evolve prior to or concurrently with division of labour, this could limit the extent to which topological constraints favoured the initial evolution of division of labour. We conclude by suggesting experimental designs that could determine why division of labour is favoured in the natural world.

## Introduction

Division of labour, where cooperating individuals specialise to carry out distinct tasks, plays a key role at all levels of biology (Bourke, 2011; Queller, 1997; Maynard Smith and Szathmáry, 1995; West et al., 2015). Cells are built by genes carrying out different functions (Bourke, 2011; Levin and West, 2017). In clonal groups of bacteria, cells specialise to produce and secrete different factors that facilitate growth (Dragoš et al., 2018a; Veening et al., 2008; West and Cooper, 2016). Pathogens rely on division of labour for protection from the host immune response and competitors (Ackermann et al., 2008; Diard et al., 2013). Multicellular organisms are composed of reproductive germ cells and sterile somatic cells that are not passed to the next generation (Bourke, 2011; Maynard Smith and Szathmáry, 1995). The ecological dominance of the social insects arises from division of labour between queens and the different types of workers (castes) (Hölldobler and Wilson, 1990; Oster and Wilson, 1978).

It has long been established that the evolution of division of labour requires an efficiency benefit from individual specialisation (Figure 1A and B for reproductive division of labour) (Bourke, 2011; Cooper and West, 2018; Ispolatov et al., 2012; Michod, 2006; Oster and Wilson, 1978; Schiessl et al., 2019; Biggart, 1776; Maynard Smith and Szathmáry, 1995; Solari et al., 2013). In particular, that there is an accelerating (convex) return when individuals commit more effort to a particular task, such that twice the investment more than doubles the return (Bourke, 2011; Cooper and West, 2018; Ispolatov et al., 2012; Michod, 2006; Solari et al., 2013). An accelerating return from individual investment can exist for several reasons. A task could become more effective as more effort is put into it, or it could be carried out with diminishing costs. This could occur if there are large upfront costs from performing a task. For instance, any reproduction by a cell in Volvocine groups first requires individual growth to the size of a daughter colony (Michod, 2006). Alternatively, there could be a disruptive cost to carrying out multiple tasks at the same time if the tasks do not mix well. For instance, in cyanobacteria the enzymes that fix environmental nitrogen are degraded by oxygen, a bi-product of photosynthesis (Flores and Herrero, 2010).

![Figure 1.](https://cdn.elifesciences.org/articles/71968/elife-71968-fig1-v2.jpg)

**Figure 1.:** (A) Theory has shown that either a linear or diminishing return from more cooperation (or reproduction) favours uniform cooperation, with all individuals investing the same amount of effort into cooperation and reproduction (i.e. no division of labour) (Cooper and West, 2018; Michod, 2006; Schiessl et al., 2019). (B) In contrast, an accelerating return from more cooperation (or reproduction) favours reproductive division of labour, with some individuals specialising in high levels of cooperation (helpers) and others in low levels of cooperation (reproductives) (Cooper and West, 2018; Michod, 2006; Schiessl et al., 2019).

In contrast, Yanni et al. found that division of labour between helpers and reproductives can sometimes be favoured even when there are diminishing (concave) returns from individual specialisation (Yanni et al., 2020). Specifically, reproductive division of labour could arise in topologically constrained groups—where each cell in a spatially structured group shares cooperative benefits with only their direct neighbours (Staps and Tarnita, 2020; Yanni et al., 2020). Their analyses suggested that this is particularly likely to occur in sparsely structured groups, where cells have a small number of neighbours (Yanni et al., 2020). This is a novel result. Diminishing returns means that specialised individuals are inefficient, and earlier work suggested that division of labour could not be favoured in this situation (Figure 1A, Cooper and West, 2018; Michod, 2006; Schiessl et al., 2019). Consequently, this result has the potential to overturn our understanding of the factors that favour the evolution of division of labour.

However, there are several issues that still need to be resolved with how topological constraints can favour division of labour. Why exactly do the predictions of this new theory differ from previous theory? Are special group structures the only way to alter the predictions of the previous theory, or is this an example of a more general phenomenon (Rueffler et al., 2012)? Do these findings rely upon implicit assumptions, which may not be reasonable during the initial evolution of division of labour? Answering these questions is not only of theoretical importance: it is also key for planning future empirical studies. Quantifying the shape of the returns from individual specialisation has been assumed to be a fundamental step in determining why division of labour was favoured in some species, but not others (Diard et al., 2013; Dragoš et al., 2018a; Flores and Herrero, 2010; Koufopanou, 1994; Mridha and Kummerli, 2021; Strassmann et al., 2000; Veening et al., 2008).

We first use the methodology developed by Rueffler et al., 2012, to derive the general conditions that favour the initial evolution of reproductive division of labour between helpers and reproductives. We then use this framework to examine when and why topological constraints can favour division of labour. More specifically, we determine the ultimate cause of division of labour in specific topologically constrained groups, such as filaments and branching growths, as well as in a general analysis of arbitrary group structures. We then ask whether division of labour without an accelerating return from individual specialisation could arise in groups without topological constraints. To test our hypothesis that between-individual coordination is required for division of labour in these cases, we re-examine our models while assuming that cells adopt helper and reproductive roles randomly (no coordination). We finish by suggesting experimental designs for determining why division of labour has evolved in specific species.

## Results and discussion

### General invasion analysis

We follow previous studies by assuming that individual fitness is the product of individual viability, which is the chance of surviving to maturity, and individual fecundity, which is proportional to the number of offspring if the individual reaches maturity (Cooper and West, 2018; Michod, 2006; Yanni et al., 2020). We examine the specific case of reproductive division of labour between helpers and reproductives, where helpers are more cooperative, contributing to a higher viability for group members, and reproductives are less cooperative, contributing to higher individual fecundity.

We consider an initial population of clonal groups each containing $n$ individuals, in which all individuals cooperate at the evolutionarily stable (ES) level ($z^{∗}$), which is the level that cannot be outcompeted by a mutant strain that uses a different level of uniform cooperation across the group (Maynard Smith, 1982). We then ask when this population of uniform cooperators can be invaded by a mutant strain that employs a reproductive division of labour.

Without loss of generality, we assume that the mutant strain is composed of $n_{h}$ helpers that invest $z_{h}\geq0$ into cooperation and $n_{r}$ reproductives that invest $z_{r}\geq0$ into cooperation (where $n_{h}+n_{r}=n>2$ and $z_{h} >z_{r}$). We set individual fitness as the product of individual fecundity, $F>0$, and individual viability, where helpers and reproductives may in principle have different viability functions, $V_{h}>0$ and $V_{r}>0$ (but see Appendix C.2) (Michod, 2006; Yanni et al., 2020). The fitness of the clonal group is given by the sum of individual fitness:

$$
W(z_{h},z_{r})=n_{h}F(z_{h})V_{h}(z_{h},z_{r})+n_{r}F(z_{r})V_{r}(z_{h},z_{r}),
$$

where the first term on the right-hand side is the total fitness of the prospective helpers and the second term on the right-hand side is the total fitness of the prospective reproductives.

Fecundity is determined by an individual’s investment in cooperation ($F=F(z),$ where $z$ is the focal individual’s level of cooperation) and viability is determined by the level of cooperation at the level of the group ($V_{h}=V_{h}(z_{h},z_{r})$ and $V_{r}=V_{r}(z_{h},z_{r})$). We assume that there is a tradeoff between fecundity and viability such that higher individual cooperation leads to lower individual fecundity ($F^{′}(z)<0$), but that more cooperation leads to a higher viability for all individuals (i.e. $V_{h}^{z_{h}},V_{h}^{z_{r}}, V_{r}^{z_{h}}, V_{r}^{z_{r}}>0$, where superscripts denote partial derivatives). We assume that viability selection occurs just prior to reproduction. This is consistent with previous models and ensures that there there is no feedback between a cell’s viability and its ability to produce cooperative benefits for the group (Cooper and West, 2018; Michod, 2006; Yanni et al., 2020).

We determine the invadability conditions that favour reproductive division of labour by applying the general approach of Rueffler et al., 2012. The key step is to approximate the relative fitness of a reproductive division of labour mutant by taking a second-order Taylor expansion of fitness, centred on the resident strategy of uniform cooperation, $z^{∗}$:

$$
W(z^{∗}+Δz_{h}, z^{∗}+Δz_{r})−W(z^{∗}, z^{∗})≈
$$



$$
W^{z_{h}}Δz_{h}+W^{z_{r}}Δz_{r}+\frac{1}{2}W^{z_{h}z_{h}}Δz_{h}^{2}+\frac{1}{2}W^{z_{r}z_{r}}Δz_{r}^{2}+W^{z_{h}z_{r}}Δz_{h}Δz_{h},2(a)2(b)2(c)2(d)2(e)
$$

where $Δz_{h}>Δz_{r}$ captures the change in the level of cooperation for mutant helpers and reproductives, respectively, which we assume are small in magnitude. The superscripts represent first- and second-order partial derivatives, where all partial derivatives are evaluated at the resident strategy of uniform cooperation ($z_{h}=z_{r}=z^{∗}$). If a mutant strain exists such that Equation 2 is positive ($W(z^{∗}+Δz_{h}, z^{∗}+Δz_{r})>W(z^{∗}, z^{∗})$), then division of labour between helpers and reproductives is favoured to evolve. Conversely, if for all possible mutant strains, Equation 2 is negative ($W(z^{∗}, z^{∗})>W(z^{∗}+Δz_{h}, z^{∗}+Δz_{r})$), then uniform cooperation is evolutionarily stable.

### The three pathways to division of labour

We found that reproductive division of labour could be favoured for three distinct reasons, corresponding to different subsets of terms on the right-hand side of Equation 2. Our results for reproductive division of labour, where fitness is partitioned as the product of fecundity and viability, align with those found by Rueffler et al., 2012, for division of labour more generally. We now go through these three distinct scenarios.

#### Scenario 1: Accelerating returns from individual specialisation

The first and most studied scenario that can favour division of labour is when there are accelerating returns from individual specialisation. This occurs if there is an accelerating fitness return from either helper specialisation in cooperation or reproductive specialisation in fecundity (Figure 1; Cooper and West, 2018; Michod, 2006; Oster and Wilson, 1978).

Mathematically, this scenario is a consequence of the third and fourth terms of the Taylor expansion ($2c$ and $2d$), which capture the second-order fitness effect of a small, unilateral change in cooperation by either prospective helpers or reproductives, respectively. Division of labour is favoured to evolve whenever at least one of $2c$ and $2d$ is greater than zero ($W^{z_{h}z_{h}}>0$ or $W^{z_{r}z_{r}} >0$), and where we have assumed that the first two terms are both zero ($W^{z_{h}}=0$ and $W^{z_{r}}=0$; see between-individual differences below; Figure 2A). In either scenario, an efficiency benefit to group fitness arises from individual specialisation because the more effort that each individual puts into a task, the better they can perform that task. Rueffler et al. termed these kinds of scenario as ‘accelerating performance functions’ (Rueffler et al., 2012).

![Figure 2.](https://cdn.elifesciences.org/articles/71968/elife-71968-fig2-v2.jpg)

**Figure 2.:** Division of labour is favoured if some individuals are predisposed to being reproductives or helpers. (A) In the absence of another mechanism, if there are no differences between individuals (black and grey lines), then division of labour is not favoured. (B) If some individuals can produce larger viability benefits than others (black line), or if some individuals can access greater fecundity benefits than others (grey line), then this predisposition favours division of labour.

#### Scenario 2: Between-individual differences

The second scenario that can favour reproductive division of labour is when there are pre-existing differences between individuals in the group, such that some individuals are predisposed to one task or the other. For example, if some individuals can secure larger viability benefits for the group at the same fecundity cost as others (Figure 2B).

This scenario is captured by the first two terms of the Taylor expansion $(2a and 2b)$ , which are the first-order fitness effects from a small, unilateral change in the level of cooperation by prospective helpers or reproductives. If the direct fitness effects are non-zero (positive or negative) at the resident strategy of uniform cooperation ($W^{z_{h}}\neq0$ or $W^{z_{r}}\neq0$), then division of labour can invade independently of any higher-order effects (the remaining terms in Equation 2).

We term this scenario ‘between-individual differences’ because it requires that there is pre-existing phenotypic or environmental variation between individuals in the group. For the within-species case, ancestral groups are usually composed of clonal or highly related individuals, who will be phenotypically similar or identical. Consequently, this mechanism could be less important for the division of labour except when there are consistent differences in the microenvironment experienced by different individuals (Tverskoi et al., 2018; Tverskoi and Gavrilets, 2021). In contrast, this scenario is likely to be widespread in the evolution of non-reproductive division of labour between species, such as for mutualisms or symbioses (Kiers et al., 2011; Rueffler et al., 2012; Wyatt et al., 2014). Individuals of different species often differ in their abilities to perform certain tasks (Kiers et al., 2011). Rueffler et al. termed this scenario ‘positional’, but we avoid that term to prevent confusion with topological position (Rueffler et al., 2012).

Between-individual differences provide a first-order fitness benefit to dividing labour, and so it does not matter whether the subsequent benefits of increased cooperation or fecundity are accelerating or diminishing (Figure 1), so long as these benefits are different for different individuals (Figure 2). When some individuals are predisposed to being either helpers or reproductives, then individual specialisation provides an efficiency benefit to group fitness by capitalising on these inherent differences.

#### Scenario 3: Reciprocal specialisation

The final scenario that can favour division of labour is when reciprocal specialisation by both helpers and reproductives provides a fitness benefit to the group (Figure 3). This scenario requires two key conditions. First, simultaneous specialisation, where some individuals invest more in cooperation (more viability benefits for the group), and others invest less in cooperation (greater individual fecundity; but see below). Second, this reciprocal specialisation must provide a group-level fitness benefit, because the increased benefits of cooperation are preferentially directed towards reproductives.

![Figure 3.](https://cdn.elifesciences.org/articles/71968/elife-71968-fig3-v2.jpg)

**Figure 3.:** We assume that there are diminishing returns from specialisation in either viability or fecundity (Figure 1A). (A) In this case, a unilateral increase in cooperation by helpers or a unilateral decrease in cooperation by reproductives leads to a diminishing fitness benefits to the group, which favours uniform cooperation (no division of labour). (B) In contrast, a reciprocal increase in cooperation by helpers (more viability benefits provided by helpers) and a decrease in cooperation by reproductives (larger reproductive fecundity) can produce an accelerating return to the fitness of the group if the benefits of increased cooperation are preferentially directed to reproductives. Thus, reciprocal specialisation can still favour division of labour, even though the returns from individual specialisation are diminishing. In the middle plots of (A) and (B), only the shape of the benefits from increased specialisation is plotted.

Mathematically, this scenario involves the last term of the Taylor expansion ($2e; W^{z_{h}z_{r}}Δz_{h}Δz_{r}$). This term is generated by a between-individual, second-order fitness effect, capturing how increased investment in viability by some individuals affects the returns from increased investment in fecundity by others, and vice versa. Rueffler et al. referred to this as a ‘synergistic benefit’ to division of labour (Queller, 1985; Queller, 2011; Rueffler et al., 2012).

Critically, this scenario still involves an efficiency benefit to specialisation, but at the level of group fitness rather than in each fitness component separately (Appendix C.1). By this we mean that there is an accelerating fitness benefit to the group when helpers and reproductives reciprocally specialise, leading to a higher group fitness than in groups with uniform cooperation (generalists). This occurs if the increased help given to reproductives is sufficiently amplified by the increased fecundity of reproductives (Yanni et al., 2020). This synergistic efficiency benefit can favour division of labour even if there are diminishing returns from individual specialisation.

Division of labour by reciprocal specialisation can also evolve without a joint mutation in the level of cooperation of both helpers and reproductives (no simultaneous specialisation). In this case, the chance invasion (to fixation) of a slightly deleterious mutant that specialises in only one phenotype can destabilise uniform cooperation, creating a selection pressure for the other phenotype to also specialise that is greater than the selection pressure to purge the initial mutant. In this two-step scenario, it is nevertheless the synergistic benefit from reciprocal specialisation that makes division of labour more efficient.

### Group structure in the general framework

Our above analysis has shown that reproductive division of labour can be favoured for three reasons: (1) accelerating returns make individual specialisation more efficient; (2) between-individual differences make individual specialisation more efficient; and (3) there is a synergistic efficiency benefit from reciprocal specialisation. These results agree with previous analyses by Rueffler et al., 2012.

We now use this framework to examine how and why topological constraints can favour division of labour in the absence of an accelerating return from individual specialisation (i.e. when scenario 1 does not hold). We ask three questions. First, can topological constraints favour division of labour by between-individual differences (scenario 2), and/or by reciprocal specialisation (scenario 3)? Second, are topological constraints the only way to evolve a division of labour without an accelerating return from individual specialisation? Third, does the evolution of division of labour by between-individual differences (scenario 2) and reciprocal specialisation (scenario 3) require coordination between individuals to determine which cells become helpers or reproductives?

#### Question 1: How do topological constraints favour division of labour?

We consider two spatial models, based on the group structures proposed by Yanni et al., to examine whether topologically constrained groups favour division of labour by: (a) between-individual differences and/or (b) reciprocal specialisation (Yanni et al., 2020).

##### Can topological constrains lead to division of labour by between-individual differences?

Consider a group in which cells alternately have either two or three neighbours, in a branching structure (Figure 4). Such a group structure might have occurred for some early forms of multicellular life (Yanni et al., 2020). We term cells with three neighbours ‘node’ cells and cells with two neighbours ‘edge’ cells. We assume that cells investing an amount $z\geq0$ into cooperation produce an amount $H(z)$ of a public good. We assume non-accelerating returns from individual specialisation (i.e. $H^{′′}(z)\leq0$ or $F′′ (z)\leq0$). The cell keeps a fraction $1−\lambda$ of the public good that it produces, and the remaining fraction $\lambda$ is shared equally between its direct neighbours (the ‘shareability’ of cooperation: $0<\lambda\leq1$). We assume that the viability of a cell is equal to the sum of the public good that it absorbs.

![Figure 4.](https://cdn.elifesciences.org/articles/71968/elife-71968-fig4-v2.jpg)

**Figure 4.:** We show here different scenarios in which division of labour can evolve (non-white shades) and the size of its fitness benefit if so (darker shades). We consider three specific spatial models, including: a branching structure (A and D); a filament structure (B and E); and a well-mixed group (C and F). We consider when cells know their location in the group when specialising (with coordination; A–C) and when they do not (without coordination; D–F), in which case cells specialise randomly. (A) In a branching group structure with coordination, division of labour with diminishing returns from specialisation ($\alpha<1$) can be favoured by between-individual differences whenever the benefits of cooperation are shared ($\lambda>0$). (B) In a filament structure with coordination, division of labour with diminishing returns from specialisation ($\alpha<1$) can be favoured by reciprocal specialisation when cells share a sufficient majority of the public good they produce with neighbours (e.g. when linear returns: $\lambda>\frac{1}{2}$). (C) In a well-mixed group with coordination, division of labour with diminishing returns from specialisation ($\alpha<1$) can be favoured by reciprocal specialisation if cells share an even larger proportion of the public good they produce with neighbours (e.g. when linear returns: $\lambda>\frac{n−1}{n}$). (D–F) When cells specialise randomly (no coordination) across all three spatial models, then division of labour can only evolve if there is an accelerating return from specialisation ($\alpha>1$). Throughout, we have assumed a linear return from fecundity specialisation, $Fx=1-x$, and allow for a non-linear return from investment in cooperation, $Hx=x^{\alpha}$ , where $\alpha$ controls the shape of the return.

For this model, we find that for all social traits ($\lambda>0$), reproductive division of labour by between-individual differences can evolve (Figure 4A; Appendix A.1). This occurs because different cells have different viability-fecundity tradeoffs depending on their position in the group. Edge cells receive relatively less public good from their (fewer) neighbours, and so pay a smaller opportunity cost from decreased fecundity (increased cooperation). In contrast, node cells receive relatively more public good from their (more numerous) neighbours, and so pay a larger opportunity cost from decreased fecundity (increased cooperation). Consequently, this between-cell difference favours node cells to specialise in fecundity (reproductives) and edge cells to specialise in increased cooperation (helpers). Importantly, because this pathway to division of labour is driven entirely by a first-order effect (2a and 2b), it does not require a second-order efficiency benefit from specialisation (2c, 2d, or 2e).

More generally, a formal analysis of arbitrary group structures reveals that division of labour by between-individual differences can always evolve whenever the number of neighbours varies for different cells in the group (Appendix A.2).

##### Can topological constraints lead to division of labour by reciprocal specialisation?

Consider a one-dimensional chain of cells, as examined by Yanni et al. Chains are found in species like cyanobacteria that form filaments of cells, and such structures might have been important at the onset of the evolution of multicellularity (Figure 4, Yanni et al., 2020). We assume arbitrarily that ‘odd’ cells along the filament are putative helpers and ‘even’ cells are putative reproductives. We otherwise make the same assumptions as for the branching structure model: there is a non-accelerating return from individual specialisation (i.e. $H^{′′}(z)\leq0$ or $F′′ (z)\leq0)$, and the cell keeps a fraction $1−\lambda$ of the public good that it produces, with the remaining fraction $\lambda$ being shared equally by its direct neighbours.

If the amount of public good shared with neighbours is sufficiently large (high $\lambda$), then we find that division of labour via reciprocal specialisation can evolve (Figure 4B; Appendix A. 3). For instance, in the case of linear fecundity and public good returns ($H^{′′}(z)=F^{′′}(z)=0$), division of labour by reciprocal specialisation can evolve if helpers share more of the public good that they produce with their neighbours than they keep for themselves ($\lambda>\frac{1}{2}$). If there are diminishing returns from specialisation ($H^{′′}(z)<0$ or $F^{′′}(z)<0$), then division of labour can still be favoured but then the amount of the public good preferentially shared with neighbours must be even greater still (higher $\lambda;$ Figure 4E).

For an arbitrary group structure, our analysis in the previous section implies that division of labour can evolve by between-individual differences, unless every cell in the group has the same number of neighbours. Consider a group in which every cell has exactly d neighbours. In this case, we show (Appendix A.5) that division of labour can still be favoured due to reciprocal specialisation if:

$$
\lambda\mu> d
$$

λ is the shareability of cooperation as defined previously and μ captures how easily the group can be ‘bi-partitioned’. That is, μ is a measure of the extent that the group can be divided into two classes of cells such that cells are neighbours with many cells of the opposing class and few neighbours of their own class. Thus, reciprocal specialisation can favour division of labour if: (1) groups are more sparse (low d); (2) groups are structured such that helpers can be neighbours with reproductives more than with other helpers, and vice versa (high μ); and/or (3) when the benefits of cooperation are preferentially shared with neighbours (high $\lambda$). In combination, these three factors amplify the synergistic benefits of reciprocal helper and reproductive specialisation, which can produce an accelerating fitness return for the group, even when there are non-accelerating returns from individual specialisation (Appendix C.1).

If one or two of these factors are particularly favourable for reciprocal specialisation, then the condition(s) on the remaining factor(s) can be relaxed. For instance, cells in a filament have only two neighbours ($d=2$), and the potential alternation of helpers and reproductives in the filament means that helpers can share their cooperative public goods with reproductives exclusively (maximal $\mu).$ Consequently, reciprocal specialisation is possible even when the shareability of cooperation is reasonably low (e.g. $\lambda>\frac{1}{2}$ for linear benefits).

To conclude, topological constraints are not a single explanation for division of labour, in that they can favour division of labour for two different biological reasons. Different group structures can lead to either between-individual differences favouring division of labour (scenario 2) or reciprocal specialisation favouring division of labour (scenario 3). In all cases, there is an efficiency benefit from specialisation at the level of group fitness even if the returns from individual specialisation are non-accelerating.

### Question 2: Are topological constraints required for division of labour without accelerating returns from individual specialisation?

We considered a well-mixed social group of $n$ cells, where all cells share the benefits of cooperation with one another, and so there are no topological constraints (Figure 4). We then examined whether division of labour could be favoured by: (a) between-individual differences; and/or (b) reciprocal specialisation. In both cases, we assume that when a cell invests $z$ into cooperation, it produces an amount $H(z)$ of a public good. A cell keeps a fraction $1−\lambda$ of the public good that it produces and the remaining fraction $\lambda$ is shared by the rest of the social group members equally. We again consider the case where there is a non-accelerating return from individual specialisation ($H(z)^{′′}\leq0$; $F′′ (z)\leq0)$.

#### Can between-individual differences favour division of labour without a topological constraint?

In the well-mixed group of identical cells, we find that division of labour cannot arise by between-individual differences (Appendix A.4). This is because all cells have the same number of neighbours, which we have shown more generally can never produce between-individual differences. This prediction could be violated if one of our assumptions do not hold: for instance, if there are consistent differences in the microenvironment that predispose some cells to one task or the other (Tverskoi et al., 2018; Tverskoi and Gavrilets, 2021; Yanni et al., 2020).

#### Can reciprocal specialisation favour division of labour without a topological constraint?

In the well-mixed group of identical cells, if the amount of public good shared with neighbours is sufficiently large (high $\lambda$), then we find that division of labour via reciprocal specialisation can evolve (Figure 4F; Appendix A.4). If there are linear returns from increased specialisation ($H^{′′}(z)=F^{′′}(z)=0$), then division of labour can evolve when the public good produced by an individual benefits an average group member more than the producer ($\lambda>\frac{n−1}{n}$; Figure 4C). These results are like those found for a filament of cells (Figure 4B). In both cases, more generous sharing (higher $\lambda$) means that the synergistic benefits of reciprocal specialisation can be great enough to compensate for the non-accelerating returns from individual specialisation. In well-mixed groups, very generous sharing ($\lambda≈1$) also compensates for the fact that helpers are neighbours with all other helpers (no sparsity and minimally ‘bi-partionable’).

To conclude, the well-mixed model shows that a topological constraint is not required for the evolution of division of labour with non-accelerating returns from individual specialisation. This result is in direct contradiction to that of Yanni et al., 2020. This difference arises because helpers in their model always benefit at least as much as any of its neighbours from its own public good production ($\lambda\leq\frac{n-1}{n}$) (Yanni et al., 2020). Our model allows for biological scenarios where the public good benefits an average neighbour more than the producer ($\lambda>\frac{n−1}{n}$). For instance, reproductive cells in cyanobacteria may absorb more of the fixed nitrogen produced by helpers than helpers do to meet the large energetic requirements of cell duplication and division (Flores and Herrero, 2010; Herrero et al., 2016; Meeks and Elhai, 2002). At the extreme, the public good can be an ‘others-only’ trait that benefits neighbours but not the producer at all ($\lambda=1$) (Pepper, 2000). An example of this are the dispersal benefits provided by stalk cells in Dyctiostelium discodeum fruiting bodies or the self-sacrificing behaviour of helper cells in Salmonella enterica infections (Ackermann et al., 2008; Strmecki et al., 2005). Consequently, our model allows for a wider spectrum of biologically realistic scenarios. Critically, division of labour can be favoured in a group of well-mixed cells because it provides an efficiency benefit at the group level, via reciprocal specialisation (scenario 3), in an analogous way to our model with a one-dimensional chain of cells (question 1b).

### Question 3: Is coordination required to favour division of labour without accelerating returns from individual specialisation?

We hypothesised that the benefits of between-individual differences (scenario 2) or reciprocal specialisation (scenario 3) rely on the implicit assumption that cells are coordinating which individuals specialise to become reproductive and helpers. This matters because mechanisms for coordinating division of labour, such as between cell signalling, might not be expected to exist before division of labour has evolved (Cooper et al., 2022; Liu et al., 2021). Consequently, if coordination was required, then this could limit the extent to which topological constrains favour the initial evolution of division of labour.

We investigated this hypothesis by repeating our above analyses, while assuming that cells do not have access to information that allows them to coordinate their phenotypes. Specifically, cells do not know if they are ‘odd’ or ‘even’, or if they are ‘edge’ or ‘node’. We assumed instead that a reproductive division of labour mutant induces each cell in the group to adopt the role of a helper or reproductive with a uniform probability (random specialisation). Random specialisation has been observed in a number of microbes (Ackermann et al., 2008; Diard et al., 2013; Veening et al., 2008). For filaments, branching group structures, and well-mixed groups, we found that division of labour can no longer evolve with non-accelerating returns from individual specialisation (Figure 4D–E; Appendices B.1 and B.2). In Appendix B.3, we have shown that this result holds for any group structure.

Consequently, for division of labour to evolve with non-accelerating returns from individual specialisation, there must exist some mechanism to coordinate which cells specialise to perform which tasks. It is possible that the mechanism need not produce a perfect allocation of labour across the group as analysed in our models (Liu et al., 2021). However, because division of labour cannot be favoured to evolve if role allocation is fully random, at least some degree of even imperfect between-cell coordination will be required.

A clear example of coordinated division of labour in topologically constrained groups is the use of between-cell signalling in some cyanobacteria filaments to determine which cells become sterile nitrogen fixing heterocysts and which cells become reproductive photosynthesisers (Flores and Herrero, 2010; Meeks and Elhai, 2002). However, a signal to coordinate distinct phenotypes must exist prior to or concurrently with the emergence of division of labour, and so a topological constraint is less likely to have favoured the initial evolution of division of labour in cyanobacteria. Alternatively, division of labour could have been favoured by an accelerating return from individual specialisation (scenario 1), with coordination only being favoured to evolve subsequently. Empirically, an accelerating return seems likely, as the key tasks performed by reproductives and helpers do not mix well (photosynthesis and nitrogen fixation) (Flores and Herrero, 2010; Meeks and Elhai, 2002).

These analyses do not suggest that topological constraints could never favour the initial evolution of division of labour. For instance, a pre-existing cue could allow division of labour to initially evolve with a metabolically cheaper form of coordination. More specifically, phenotype could be determined in response to the number of neighbours or the local concentration of some resource. Further, if there are pre-existing differences between individuals due to a pre-existing mechanism of coordination, then this mechanism can be co-opted to coordinate division of labour. However, the biological plausibility of any pre-existing mechanism would need to be explicitly justified and modelled on a case-by-case basis (Duarte et al., 2011). This would include modelling the metabolic cost, benefits and effectiveness of the mechanism (Cooper et al., 2022; Duarte et al., 2012; Liu et al., 2021). Empirically, while between-cell coordination has evolved in several labour-dividing microbial species, further studies—such as ancestral-state reconstructions—are needed to show whether coordination evolved prior to, concurrently with, or subsequent to division of labour in individual species.

In contrast, an accelerating return from individual specialisation depends on non-adaptive factors such as the physics, chemistry, or external constraints associated with the public good and its production. For instance, an accelerating return can arise if some intermediate products associated with cooperation and fecundity do not ‘mix-well’ on a chemical level. Consequently, no additional adaptive or pre-adaptation argument is needed to explain this pathway to division of labour.

### Distinguishing the ultimate causes of division of labour in the wild

How can we distinguish empirically which of the different scenarios favoured real-world examples of division of labour (Figure 5)? We suggest experimental designs for microbial systems, where mixtures of helper and reproductive cells are grown together, and which make use of methods to genetically manipulate and measure the relative levels of cooperation and reproduction of each phenotype (Ackermann et al., 2008; Diard et al., 2013; Dragoš et al., 2018a; Dragoš et al., 2018b; Mavridou et al., 2018; Mridha and Kummerli, 2021; van Gestel et al., 2015). These are rough suggestions for the kind of experiments required, as details and possibilities will vary system from system, depending upon factors such as the degree of specialisation, the mechanism by which labour is divided, and what manipulations are possible. In addition, these experiments would need to follow from key first steps, such as demonstrating division of labour and a tradeoff between reproduction and cooperation (Diard et al., 2013; Dragoš et al., 2018a; Dragoš et al., 2018b; Veening et al., 2008; Zhang et al., 2020; Figure 5).

![Figure 5.](https://cdn.elifesciences.org/articles/71968/elife-71968-fig5-v2.jpg)

**Figure 5.:** (A) To test whether division of labour is favoured by an accelerating return from individual specialisation, we must separately determine whether an increase in helper cooperation or a decrease in reproductive cooperation leads to an accelerating increase in group fitness. (B) To test whether division of labour is favoured by between-individual differences, we must determine whether an increase in cooperation by helpers produces a different group fitness benefit than an increase in cooperation by reproductives. (C) To test whether division of labour is favoured by reciprocal specialisation, we must determine whether there exists at least one relative degree of helper-to-reproductive specialisation for which group fitness is greater than the fitness of uniform cooperation.

Testing for accelerating returns from individual specialisation (scenario 1): In at least three treatments, vary the level of cooperation performed by the helpers (Figure 5A top-left), to test whether the benefits of increased cooperation are accelerating (Figure 5A right). Across at least three other treatments, vary the level of reproduction by the reproductives (Figure 5A bottom-left), to test whether the benefits of increased fecundity are accelerating (Figure 5A right). At least three treatments are required to be able to test for non-linear (accelerating) benefits.

Testing for between-individual differences (scenario 2): In some treatments, vary the level of cooperation of helpers (Figure 5B top-left). In other treatments vary the level of cooperation of reproductives (Figure 5B bottom-left). If division of labour evolves in this system by between-individual differences, then we should observe that group fitness varies differently depending on whether it is helpers or reproductives that are cooperating at a higher rate (Figure 5B right).

Testing for reciprocal specialisation (scenario 3): Use a classic $N\timesN$ factorial experiment where the level of cooperation performed by helpers and the level of reproduction performed by reproductives are both varied (Figure 5C left). Division of labour is favoured by reciprocal specialisation if there is a significant interaction term between these two factors, with at least one treatment that produces a group fitness larger than that for uniformly cooperating cells (Figure 5C right).

### Conclusion

Division of labour can be favoured to evolve without accelerating returns from individual specialisation. Nevertheless, for this to occur requires: (a) between-individual differences in task-efficiency or synergistic benefits from reciprocal specialisation and (b) a mechanism to coordinate which individuals perform which tasks. In contrast, accelerating returns can favour division of labour without a mechanism to coordinate task allocation, possibly making it more likely to favour the initial evolution of division of labour. Ultimately, determining the relative importance of these different pathways to division of labour is an empirical question, requiring experimental studies of the type we have outlined above.

## Materials and methods

### Resident strategy of uniform cooperation

We start by solving for the ESS strategy where both types of individuals invest the same amount in cooperation ($z_{h}=z_{r}=z$; uniform cooperation). This is the level of uniform investment in cooperation, $z^{*}$ , for which there is no selection for a uniform change in the amount of cooperation by all individuals in the group:

$$
\frac{∂W(z,z)}{∂z}|_{z=z^{∗}}=0
$$

More explicitly, we can write this as:

$$
n_{h}FV_{h}(\frac{F^{′}}{F}+\frac{n_{h}V_{h}^{z_{h}}+n_{r}V_{r}^{z_{h}}}{n_{h}V_{h}})|_{z_{h}=z_{r}=z^{∗}}+n_{r}FV_{r}(\frac{F^{′}}{F}+\frac{n_{h}V_{h}^{z_{r}}+n_{r}V_{r}^{z_{r}}}{n_{r}V_{r}})|_{z_{h}=z_{r}=z^{∗}}=0
$$

where we have suppressed the functional dependencies for ease of presentation. The first term gives the group fitness change due to a marginal increase in ‘helper’ cooperation, and the second term gives the group fitness change due to a marginal increase in ‘reproductive’ cooperation. So, at the uniform strategy, $z^{*}$ , any increase in the fitness caused by the increased cooperation of one subgroup of the population is balanced by a commensurate decrease in fitness caused by the same increase in cooperation for the other subgroup $\frac{∂W(z_{h},z_{r})}{∂ z_{h}}|_{z_{h}=z_{r}=z^{∗}}=−\frac{∂W(z_{h},z_{r})}{∂ z_{r}}|_{z_{h}=z_{r}=z^{∗}}$.

The constrained optimum, $z_{h},z_{r} = z^{*},z^{*},$ computed using Equation 4 does not necessarily correspond to a critical point of $W$, that is, the first derivates $\frac{\partialWz_{h},z_{r}}{\partial z_{h}}$ and $\frac{\partialWz_{h},z_{r}}{\partial z_{r}}$ might not vanish at this point. However, if the functions $V_{h}$ and $V_{r}$ are symmetrical, in the sense that

$$
n_{h}V_{h}(z_{h},z_{r}) = n_{r}V_{r}(z_{r},z_{h}),
$$

then the fitness function satisfies $W(z_{h},z_{r}) = W(z_{r},z_{h})$, and it can be seen that this implies that the point $(z_{h},z_{r}) = (z^{*},z^{*})$ is actually a critical point of $W(z_{h},z_{r})$.

#### Division of labour by between-individual differences

Division of labour by between-individual differences occurs if either of the first two terms of the Taylor expansion (Equation 2) is non-zero ($W^{z_{h}}\neq 0$ or $W^{z_{r}}\neq 0$). In this case, directional selection will increase or decrease the level of cooperation of one of the individual types. We give here the associated partial differentials of fitness (Equation 1):

$$
\frac{\partialWz_{h},z_{r}}{\partial z_{h}}|_{z_{h}=z_{r}=z^{*}}=n_{h}F^{`}V_{h}+n_{h}FV_{h}^{z_{h}}+n_{r}FV_{r}^{z_{h}}
$$



$$
\frac{\partialWz_{h},z_{r}}{\partial z_{r}}|_{z_{h}=z_{r}=z^{*}}=n_{r}F^{`}V_{r}+n_{h}FV_{h}^{z_{r}}+n_{r}FV_{r}^{z_{r}}
$$

These expressions capture the fitness consequences of a marginal increase in cooperation by helpers and reproductives, respectively. The first term of each captures the fecundity cost to own type of producing more public good, whereas the second term and third term are the viability benefits that accrue to both types from this increased cooperation. If directional selection in both traits is zero ($\frac{\partialWz_{h},z_{r}}{\partial z_{h}}|_{z_{h}=z_{r}=z^{*}}=0$ and $\frac{\partialWz_{h},z_{r}}{\partial z_{r}}|_{z_{h}=z_{r}=z^{*}}=0$), then $z_{h}=z_{r}=z^{*}$ is a critical point, and Equations 6 and 7 imply that

$$
\frac{F^{′}}{F}|_{z_{h}=z_{r}=z^{∗}}=−\frac{n_{h}V_{h}^{z_{h}}+n_{r}V_{r}^{z_{h}}}{n_{h}V_{h}}|_{z_{h}=z_{r}=z^{∗}}
$$



$$
\frac{F^{′}}{F}|_{z_{h}=z_{r}=z^{∗}}=−\frac{n_{h}V_{h}^{z_{r}}+n_{r}V_{r}^{z_{r}}}{n_{h}V_{h}}|_{z_{h}=z_{r}=z^{∗}}
$$

These equations mean that, if $z_{h}=z_{r}=z^{*}$ is a critical point, then any marginal viability benefit to the group of increased cooperation by one subgroup is cancelled by the fecundity cost to that same subgroup. Moreover, Equations 8 and 9 together imply that

$$
\frac{n_{h}V_{h}^{z_{h}}+n_{r}V_{r}^{z_{h}}}{n_{h}V_{h}}|_{z_{h}=z_{r}=z^{∗}}=\frac{n_{h}V_{h}^{z_{r}}+n_{r}V_{r}^{z_{r}}}{n_{h}V_{h}}|_{z_{h}=z_{r}=z^{∗}}
$$

If this equation does not hold, then $z_{h}=z_{r}=z^{*}$ is not a critical point, that is, there is a difference in the viability-fecundity tradeoffs between subgroups such that some individuals (without loss of generality, helpers) can secure larger benefits for the group at the same fecundity cost as others (reproductives). This gives our first condition for division of labour being able to evolve:

The between-individual differences condition for division of labour

$$
\frac{n_{h}V_{h}^{z_{h}}+n_{r}V_{r}^{z_{h}}}{n_{h}V_{h}}|_{z_{h}=z_{r}=z^{∗}}>\frac{n_{h}V_{h}^{z_{r}}+n_{r}V_{r}^{z_{r}}}{n_{h}V_{h}}|_{z_{h}=z_{r}=z^{∗}}.
$$

If individuals are indistinguishable when both types invest equally in cooperation ($z_{h}=z_{r}=z$), then the viability functions satisfy $V_{h}(z,z)=V_{r}(z,z)$. In this case, Condition 11 can be restated as:

$$
V_{h}^{z_{h}}+\frac{n_{r}}{n_{h}}V_{r}^{z_{h}}>V_{r}^{z_{r}}+\frac{n_{h}}{n_{r}}V_{h}^{z_{r}}
$$

This says that the contribution to total viability from the increased specialisation of helper individuals is strictly larger than the contribution to total viability from the increased specialisation of reproductives. As a result, helpers are predisposed to become more helper-like as they can gain larger viability gains for the group than the other type of individual.

### Division of labour by an accelerating return from individual specialisation

Division of labour by an accelerating return from individual specialisation can occur if either of the third or fourth terms in the Taylor expansion (Equation 2) are positive in value ($W^{z_{h}z_{h}}>0$ or $W^{z_{r}z_{r}}>0$). Taking the second derivative of fitness (Equation 24) with respect to each trait and evaluating at the critical point of uniform cooperation $z^{*}$ gives:

$$
\frac{∂^{2}W}{∂z_{h}^{2}}|_{z_{h}=z_{r}=z^{∗}}=2n_{h}F^{′}V_{h}^{z_{h}}+n_{h}F^{′′}V_{h}+n_{h}FV_{h}^{z_{h}z_{h}}+n_{r}FV_{r}^{z_{h}z_{h}}
$$



$$
\frac{∂^{2}W}{∂z_{r}^{2}}|_{z_{h}=z_{r}=z^{∗}}=2n_{r}F^{′}V_{r}^{z_{r}}+n_{r}F^{′′}V_{r}+n_{h}FV_{h}^{z_{r}z_{r}}+n_{r}FV_{r}^{z_{r}z_{r}}
$$

The terms of Equations 13 and 14 capture the second-order effects of increased investment in cooperation. The first term of each captures the decline in the fitness benefit of increased cooperation due to the cross-interaction between fecundity and viability. For instance, as a helper invests more in cooperation (higher $x$), it increases its own viability (higher $V_{h}$), but its fecundity declines as well (lower $F$) and so the relative benefit of this increased viability is lessened (the cross term $F^{`}V_{h}^{z_{h}}$ is negative). This represents a kind of decelerating return from cooperation. The second term of each captures the second-order effect of decreased investment in fecundity. If this term is positive, then this means that there is a diminishing fecundity cost to increased investment in cooperation, which can favour division of labour. The third and fourth terms capture the second-order effect of increased investment in viability, that is, does each successive investment in the public good lead to a larger or smaller increase in viability than the previous investment of the same size? The return on investment (ROI) in viability is accelerating if $V_{h}^{z_{h}z_{h}}>0$, $V_{r}^{z_{h}z_{h}}>0$, $V_{h}^{z_{r}z_{r}}>0$, and $V_{r}^{z_{r}z_{r}}>0$. The ROI is diminishing if these second derivates are negative: $V_{h}^{z_{h}z_{h}}<0$, $V_{r}^{z_{h}z_{h}}<0$, $V_{h}^{z_{r}z_{r}}<0$, and $V_{r}^{z_{r}z_{r}}<0$.

Thus if either Equation 13 or Equation 14 is positive, then division of labour is favoured to evolve. This gives the second condition for division of labour.

The accelerating returns from individual specialisation condition for division of labour

$$
\frac{n_{h}V_{h}^{z_{h}z_{h}}+n_{r}V_{r}^{z_{h}z_{h}}}{n_{h}V_{h}}|_{z_{h}=z_{r}=z^{∗}}+\frac{F^{^{″}}}{F}|_{z_{h}=z_{r}=z^{∗}}+2\frac{F^{′}}{F}\frac{V_{h}^{z_{h}}}{V_{h}}|_{z_{h}=z_{r}=z^{∗}}>0,
$$



$$
\frac{n_{h}V_{h}^{z_{r}z_{r}}+n_{r}V_{r}^{z_{r}z_{r}}}{n_{r}V_{r}}|_{z_{h}=z_{r}=z^{∗}}+\frac{F^{^{″}}}{F}|_{z_{h}=z_{r}=z^{∗}}+2\frac{F^{′}}{F}\frac{V_{h}^{z_{r}}}{V_{r}}|_{z_{h}=z_{r}=z^{∗}}>0.
$$

Fixing our attention on just Equation 15 (or equivalently on 16), this condition states that the sum of the second-order viability effect from increased cooperation (first term on left-hand side) and the second-order fecundity effect of increased cooperation (second term on left-hand side) must be larger than the marginal fecundity cost of increased investment in viability (third term on left-hand side). Note that the third term on left-hand side is always negative because increased investment in viability decreases the value of increased investment in fecundity. Therefore, division of labour by a single-trait mutation can only happen if there is an accelerating ROI in at least one of fecundity, $F(z)$; helper viability, $V_{h}(z_{h},z_{r})$; or reproductive viability, $V_{r}(z_{h},z_{r})$.

### Division of labour by reciprocal specialisation

The last remaining scenario for division of labour is that the resident strategy of uniform cooperation is unstable to mutations in both traits, which can occur depending on the value of the last term of the Taylor expansion (Equation 2; $W^{z_{h}z_{r}}Δz_{h}Δz_{r}$). This kind of instability can arise if there is a joint mutation that affects the level of cooperation of both helpers and reproductives at the same time ($Δz_{h}\neq 0$ and $Δz_{r}\neq0$). However, it could also occur if a slightly deleterious mutation in one trait invades by drift and destabilises the other trait so much that the population evolves away from the critical point. In either case, it will be found that same condition must be satisfied in order for division of labour to evolve. In the rest of this section, we give the general analysis of whether $(z_{h},z_{r}) = (z^{*},z^{*})$ is unstable to two-trait mutations, and then consider a simplifying special case to clarify the biological interpretation of this analysis.

Suppose that the resident strategy of uniform cooperation ($(z_{h},z_{r}) = (z^{*},z^{*})$) is stable against single-trait mutations (i.e. Conditions 15 and 16 not satisfied). Then the resident strategy is unstable to two-trait mutations if and only if the determinant of the Hessian is negative:

$$
\frac{∂^{2}W}{∂z_{h}^{2}}\frac{∂^{2}W}{∂z_{r}^{2}}<(\frac{∂^{2}W}{∂z_{h}z_{r}})^{2}.
$$

This condition is satisfied if the strength of directional selection pushing the population back to the critical point along either of the trait-value directions is less than the strength of directional selection on a trait when moved off of the critical point along the other trait direction. To evaluate the Hessian condition, we first compute the second-order cross derivatives:

$$
\frac{∂^{2}W}{∂z_{h}z_{r}}​|_{z_{h}=z_{r}=z^{∗}}=\frac{∂^{2}W}{∂z_{r}z_{h}}​|_{z_{h}=z_{r}=z^{∗}}=F′(n_{h}V_{h}^{z_{r}}+n_{r}V_{r}^{z_{h}})+F(n_{h}V_{h}^{z_{r}z_{h}}+n_{r}V_{r}^{z_{r}z_{h}})
$$

Here, we have used that $V_{i}^{z_{h}z_{r}}= V_{i}^{z_{r}z_{h}}$ . Substituting this, and Equations 13 and 14, into the Hessian condition gives:

The reciprocal specialisation condition for division of labour

$$
n_{h}V_{h}n_{r}V_{r}(\frac{n_{h}V_{h}^{z_{h}z_{h}}+n_{r}V_{r}^{z_{h}z_{h}}}{n_{h}V_{h}}+\frac{F§quot;}{F}+2\frac{F^{′}}{F}\frac{V_{h}^{z_{h}}}{V_{h}})(\frac{n_{h}V_{h}^{z_{r}z_{r}}+n_{r}V_{r}^{z_{r}z_{r}}}{n_{r}V_{r}}+\frac{F§quot;}{F}+2\frac{F^{′}}{F}\frac{V_{h}^{z_{h}}}{V_{r}})|z_{h}=z_{r}=z^{∗}<((n_{h}V_{h}^{z_{r}z_{h}}+n_{r}V_{r}^{z_{r}z_{h}})+\frac{F^{′}}{F}(n_{h}V_{h}^{z_{r}}+n_{r}V_{r}^{z_{h}}))^{2}|z_{h}=z_{r}=z^{∗}
$$

Assume that neither Condition 15 nor 16 is satisfied, that is, the individual ROI is non-accelerating. Then the left-hand side of the inequality is strictly positive, which means that Condition 19 is nontrivial. We will see in examples that Condition 19 can be satisfied, which means that division of labour can evolve by reciprocal specialisation even when the individual ROI is diminishing.

To clarify further the biological meaning of Condition 19, consider a simple family of models in which viability and fecundity are linear functions. In this case, all second derivates are zero, and so we get the simplified condition:

Simplified reciprocal specialisation condition for division of labour

$$
4n_{h}V_{h}^{z_{h}}n_{r}V_{r}^{z_{r}}​|_{z_{h}=z_{r}=z^{∗}}<(n_{h}V_{h}^{z_{r}}+n_{r}V_{r}^{z_{h}})^{2}​|_{z_{h}=z_{r}=z^{∗}}
$$

In the case that the viability functions are (Equation 5) this condition further simplifies to:

$$
V_{h}^{z_{h}}​|_{z_{h}=z_{r}=z^{∗}}< V_{h}^{z_{r}}​|_{z_{h}=z_{r}=z^{∗}}.
$$

This inequality is satisfied if the viability of reproductives increases faster with increased cooperation from helpers, than it does from increased cooperation from reproductives. This makes clear that reciprocal specialisation can evolve if reproductives stand to gain more from help from helpers than they would gain by helping themselves.

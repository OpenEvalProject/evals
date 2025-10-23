# Peer review - Round 1

Editors:
- Dan Haydon, University of Glasgow United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.48401.sa1](https://doi.org/10.7554/eLife.48401.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper is an excellent example of how in vitro models of cell-virus interactions can be used to shape and formulate more general and larger-scale hypotheses about epidemiological dynamics. In this case, the choice of bat cell lines expressing induced and constitutive immune phenotypes enables estimates of different viral propagation rates. The results suggest that if bat cells do have greater constitutive immunity, this could lead to situations in which viruses that do propagate in bats will do so with much greater vigour (and possibly virulence and transmissability) should they 'spill-over' into non-bat hosts. The paper should be of wide general interest to those with interests in emerging disease dynamics and to quantitative biologists interested in the mathematical modelling of in vitro systems.

Decision letter after peer review:

Thank you for submitting your article "Within-host dynamics of virulent viruses in bat reservoirs for emerging zoonotic disease" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Dan Haydon as the Reviewing Editor and Reviewer #3, and the evaluation has been overseen by Neil Ferguson as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

There is a view that bats (both as individuals and populations) are able to maintain a large number of virus species (often with little or no pathology) that are highly pathogenic outside of this order, and this paper seeks mechanistic reasons for why this might be. Specifically the authors set out to explore whether this might be due to uniquely constitutive immune capabilities of bat cells. To explore this hypothesis, the authors study the dynamics of 3 strains of vesicular stomatitis virus that express different sorts of glycoprotein, in 3 different cell cultures: Vero (non-bat cells with limited antiviral capabilities); Egyptian Fruit Bat cells which demonstrate an idiosyncratic induced interferon response, and Black Fruit Bat cells which constitutively express interferon. Well-mixed and imperfectly-mixed frequency dependent models of the infection dynamics are fitted to the means of these replicated time-series, and the models constructed to reflect the possibly differential anti-viral capabilities of the cell lines. The parameter estimates from the model fitting process lead to the key conclusion that 'induced immune responses favor slower cell-to-cell transmission rates (a proxy for viral replication rates) […] while constitutive immunity amplifies cellular transmission rates, in conjunction with less rapid antiviral responses.' The authors further conclude that '[i]f hosts with constitutive immune defenses favor evolution of rapidly transmitting viruses, such pathogens are likely to cause extreme virulence in spillover hosts lacking similarly constitutive defenses'.

One reviewer indicates that if the paper has set out to answer the question as to whether the immune phenotype of bats alters the capacity for viruses to persist within them, the answers are not sufficiently clear to merit publication in eLife. This is an understandable point of view: it seems that none of the best-fitting well-mixed models are constitutive, and only one of the spatially explicit models is constitutive where we might expect it to be (and one where we wouldn't expect it to fit best). However, I have decided to go with the majority view and provide an opportunity for revision, but the authors should consider carefully whether the essential points below can be met (or convincingly rebutted).

Essential revisions:

1) Overall, the reviewers felt that this paper was quite a bit more complicated in the presentation of its results than it needs to be, and I encourage the authors to find ways of simplifying the Results section and linearizing the framing of the key messages. I wondered what the benefits of presenting both the well-mixed and spatial models were? Which is the most appropriate? Do they say importantly different things? Could the manuscript be simplified by focusing on just one?

2) Another key question the authors should consider is whether the data in Figure 4 really support (or even need) the cell turnover embedded within the formulation of the model? Could the main point of the paper be more clearly made by fitting simpler models more consistent with the short time frame of the experimental data, and concentrating on the initial infection spread and sometime declines, rather than a scenario requiring cell turnover? If the cell cultures were capable of maintaining infection over the longer term, why weren't the experiments run over longer time frames to demonstrate this?

Introduction:

3) The authors cannot claim to be studying the within-host dynamics of bat viruses. Rather, they experimentally examine and model the dynamics of recombinant viruses in vitro. The authors should explicitly recognize throughout their manuscript that their study is at this more limited scale and, as a result, that its impact is also limited.

Results/Materials and methods:

4) The three cell lines are presented as examples of no immunity, induced immunity and constitutive immunity. The questions set out at the end of the Introduction are not answered directly (for example at the beginning of the Discussion) with attention instead diverted to measures of rate of spread. Ensure a more identifiable match between the questions posed at the end of the Introduction, and the start of the Discussion.

5) Add more explanation of what these virus lines are and why they are chosen. The reader is not told that rVSV-MARV and rVSV-EBOV are recombinant viruses expressing Ebola and Marburg Virus (Results first paragraph). Moreover, it is not stated why the authors employ two viruses (they do not seem to be interested in contrasting them but they cannot be said to be true replicates) or these two in particular.

6) How many replicates were there for each cell-line/clone combination? The only detail mentioned in this regard is that there were 2-3 technical replicates per plate. Such details should be stated prominently in the Results, since large numbers of points are plotted, but the reader has no way to discern which of them are independent.

7) There is a strong case for requiring the model is fitted to the individual replicates and not the mean of the replicates. If this case is rejected, then careful justification must be provided.

8) The cell cultures are grown to 90% confluency, and are modeled as systems in which there is cell birth and natural death (birth rate about 4x the natural death rate). Readers are likely to be left with a number of questions that the authors should address more explicitly: Where does the birth rate parameter come from? Is this a realistic estimate reflective of the dynamics of the cell culture, or is it a deduction based on the requirement to sustain the infection dynamics (either endemic or oscillatory?). The Materials and methods suggest that it is what would be required to maintain sustainable live cell populations, but is this what actually happens in the culture during the infection? What sort of turnover does this result in, in the absence of infection? What is the justification for frequency over density dependent dynamics? At the heart of these questions is whether it is appropriate to think of these cell cultures as a sort of viral chemostat which could maintain steady state or oscillatory dynamics indefinitely, or whether the system would be better modeled as an infection process in a fixed non-reproducing host population. The latter view would substantially simplify the paper if such a perspective was justifiable.

9) The potential influence of the assumed value for the rate at which antiviral cells regress to susceptibility is unclear. At present, it is not clear where the parameter value used comes from and what impact it could have on the results. This is particularly pertinent since sustained epidemics are ascribed to the antiviral cells returning to susceptibility – can one confidently separate this from birth of new susceptibles?

10) Why is ε not estimated? It seems to be fixed at 0 or 1. In subsection “Fitting of theoretical model to cell culture data demonstrates higher within-host transmission rates under constitutive immune assumptions” this seems to be recognized but Supplementary file 4 doesn't provide any intermediate values. It wasn't clear to why ε is bounded at 1. It is a rate?

11) It is surely odd that as b (and u) is lowered towards zero, R0 also tends to zero. Surely one would expect a virus to be able to spread in a non-renewing monolayer?

Discussion:

12) The use of the word 'favor' in the first paragraph of the Discussion is a little misleading and should be re-worded. These findings are not based on any evolutionary process.

13) The Discussion should make clear that the question of whether bats in general have constitutively active intracellular immunity is far from resolved. As touched on in the Introduction, this partly depends on definition – does constitutive expression of e.g. interferon-α actually provide constitutive protection? What about other immune genes which seem to be defective (e.g. Xie et al., 2018)? More generally, the immune systems of only a very small fraction of bat diversity (and of non-lab animals in general) has been studied, so it remains unclear how well we can generalise to all bats, or whether bats are truly unusual relative to other wild animals. Where possible the authors should list examples of studies showing constitutive immunity specifically in the species (or close relatives of these) thought to be reservoirs for the highly virulent viruses discussed.

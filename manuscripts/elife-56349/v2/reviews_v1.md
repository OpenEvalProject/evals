# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56349.sa1](https://doi.org/10.7554/eLife.56349.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work is a computational work on the evolution of multicellularity. Inspired by the life cycle of Dictyostelium, the authors develop a mathematical model that incorporates cellular aggregation and chemotaxis in a cyclic environment and show how the greater fidelity of multicellular chemotaxis leads to selection for that state. The model is an enlightening case study of this very important evolutionary issue.

Decision letter after peer review:

Thank you for submitting your article "Evolution of multicellularity by collective integration of spatial information" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In this paper, the authors consider the problem of evolutionary transitions to multicellularity, and in particular the case in which aggregation drives the process. Inspired by the life cycle of Dictyostelium, they consider a model in which cells (moving on a grid) search for resources and can adhere to each other based on the match between ligand and receptors on their surfaces. All of this takes place in the context of a chemotactic march towards a local chemoattractant within one temporal "season", after which fitness-dependent reproduction occurs, the population is culled back to its starting size, and the environmental conditions are changed.

The reviewers all are of the opinion that this work provides an interesting perspective on a possible mechanistic basis of 'collective-level' function, that stems from physical interactions among cells in the absence of explicitly modelled costs and benefits of single cell's choices. At the same time, the reviewers were clear that there are many aspects of the model and the modelling approach that are not clear, unnecessarily complicated or not well justified. In light of these, major revisions to the paper will be necessary, as explained below.

Essential revisions:

1) Considering the paper as a whole, there are far too many things happening at once to draw any meaningful conclusions. There is the complexity of adhesion, the nature of the chemotaxis, the temporal switching between seasons, and the reproduction process. Each of these is explored to a limited extent, and it is unclear which are absolutely crucial to the conclusions reached and how sensitive the conclusions are to the assumptions made.

2) Regarding the definition of the model itself, the reviewers find it inappropriate to relegate so much of that explanation to the Materials and methods section. The very large number of parameters (18) in Table 1 needs to be made clear (and that table should be referenced – it does not appear to be at present). Please explain more of the model in the body of the paper.

3) The reviewers are supportive of abstract models, but inasmuch as the authors have set up a physical/biological scenario with familiar processes (chemotaxis, adhesion) it would have been very helpful to have justified the kinds of dimensionless parameters that characterize the model in terms of real physical and biological features.

4) The essence of a Monte Carlo simulation is the definition of an energy function and a temperature, which together yield a Boltzmann factor that is used to decide if an attempted step is taken. The authors do not make clear in the main body of the text that they are performing a Monte Carlo calculation (that is only specified in the Materials and methods section). They refer to MCS (Monte Carlo Steps) in the body of the paper without defining that term. But the larger question is why this kind of nonequilibrium biological system should have such an energy, and what would be the biological significance of the temperature? In addition, of course, the "steps" taken are those of Monte Carlo algorithm and have no direct interpretation in terms of real time.

5) The presentation of the model and the main results lack clarity in some key aspects:

a) the relation between cell–cell and cell-medium adhesion and surface tension (subsection “Strongly adhering cells perform efficient collective chemotaxis We first assessed how well groups of cells with different adhesion strengths”) is not explained, so it is not really clear what negative surface tension means.

b) as surface tension pools two different kinds of adhesion, does it mean that in a certain sense adhesion to the surface can be traded off against adhesion between cells? This is important to know in connection to experiments.

c) since the measure of sequence complementarity is symmetric, why does one need to suppose the existence of both a ligand and a receptor? Would it change anything if cells were characterized by only one sequence? If yes, it would be interesting to know if at the end of the numerical experiment ligand and receptor evolve to be the same or if 'molecular' diversity is maintained.

d) the process of cell division/regrowth and the fact that cells do not change position from one season to the next should be more clearly explained in the main text.

e) what is the initial spatial distribution of cells at the beginning of every season, and if this matters (many models assume aggregation-dispersal cycles, that does not seem to be the case here), should be specified or repeated in the evolutionary section.

f) Figure 5 should depict a case of bistability: now it is not clear that different evolutionary outcomes are associated with differences in the initial surface tension, rather than in the initial cell configuration. It would by the way be interesting to see if the second also gives rise to bistability.

6) Cell migration (subsection “Cell migration”) is defined in terms of the actual direction of the cell over the past steps. This seems to build in persistence, and would appear to have a profound effect on the dynamics. Is this the case?

7) In general, it would be useful if statements like "In our case, aggregation leads to a highly efficient search strategy, guided by long-range, albeit noisy, gradients." (Discussion section) could be made more quantitative. For instance, one would like to get a sense of whether the conclusions are robust to changes in (at least a few important) parameters. One would expect so from results in active matter physics, but it would be useful of the authors could argument it and indicate when they expect different conclusions to hold. Moreover, what is the role of the particular gradient chosen here in 'focalizing' the formation of multicellular groups (would an essentially 1-D gradient, where isolines are parallel, do the job?) and of its intensity/spatial variation (in the movie, one sees that the centre of the gradient changes among four positions, does it matter?).

8) The authors claim that, in contrast to previous work, the increased fitness of the aggregates (better ability to perform chemotaxis) is an emergent property. The reviewers struggled to find a physical/mathematical explanation as to why such a relationship exists in the model but it appears that subsection “Chemotaxis” contains the mechanism. The text speaks of the "centre of mass of the perceived gradient". Unless we are mistaken, such a quantity averages over the individual constituent's contributions in such a way that larger cells will have more accurate measurements of the gradient. This is just the law of large numbers. If this is the case, then this feature is not an emergent property at all, but is part of the definition of the model. Please clarify. If the above critique is correct, then why bother with the complex model? The authors could just use the fact that larger aggregates are better at chemotaxis for the reason given and proceed from there.

The above suggests that the authors have basically put the answer in from the beginning. The model has the explicit feature that those that perform chemotaxis better reproduce more. So of course, that will be reinforced. But multicellularity has costs and benefits, and the model does not appear to contain any costs associated with multicellularity. In real biological examples there are many – the increased metabolic cost of the structures that hold cells together, greater need for regulatory genetic networks, etc.

9) The referencing of the text to Figure 3 is all mixed up, leaving both text and figure hard to follow. -The authors should revise this section and make sure that they clearly state if higher chemotactic performance arises due to longer persistence of cell clusters only or due to longer persistence and higher chemotactic accuracy of whole cell cluster. Varennes et al., (2017) and manuscripts citing this work give measures for chemotactic accuracy within cell populations. – Figure 3D should show error bars. Annotation of Figure 3F should be detailed, what is bar{X}? Is this the local gradient including noise or averaged on which scale.

10) The assessment time scale emerges as a decisive factor – it appears as a theoretical construct right now. What could it correspond to in the real world? Please discuss.

11) As for the particular details of the model, it is left unsaid in the main text but stated in the Materials and methods section that there is a preferred cell size A_T and a harmonic energy around that size. As the target size is (Table 1) some 50 pixels, we are confused, as it seems that each "cell" occupies one lattice size. This energy would then clearly bias the system to aggregate already. Please clarify. The use of the term "pixel" for a lattice site is confusing.

12) The literature overview appears limited – please revise and consider recent work for example but not limited to Varennes et al., (2017); Jacobeen et al., (2018). The authors should also discuss Guttal and Couzin, 2010. And they should acknowledge relevant literature exploring, for example, similar issues in the Volvocales; Solari er al., (2006); Solari, Kessler and Goldstein, (2013).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Evolution of multicellularity by collective integration of spatial information" for consideration by eLife. We regret that delay in reaching a decision on your revised manuscript, due in part to challenges presented by the pandemic. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

In this paper, the authors consider the problem of evolutionary transitions to multicellularity, and in particular the case in which aggregation drives the process. Inspired by the life cycle of Dictyostelium, they consider a model in which cells (moving on a grid) search for resources and can adhere to each other based on the match between ligand and receptors on their surfaces. All of this takes place in the context of a chemotactic march towards a local chemoattractant within one temporal "season", after which fitness-dependent reproduction occurs, the population is culled back to its starting size, and the environmental conditions are changed.

Essential revisions:

The authors have significantly reshaped the manuscript and added new interesting simulations in response to the reviewers' comments. We think the sensitivity analysis to different parameters, as well as the tests with alternative models, is important in showing the generality of the results.

If the authors made considerable efforts in explaining the model hypotheses, we found ourselves still puzzled about a few points in the main text, and reading the methods only provided part of the answers. We think some corrections are needed, in particular to help the reader understand how and when clustering of ameboid cells enhances chemotaxis.

1) The multiple scales at which different properties are defined makes it still difficult to figure the model out. Definition of the cell-to-cell contact energy J_{c,c} (subsection “2.1 Model setup”) and of averages in Figure 3 would help. The transition between the site and cell scale seems to be problematic if more than one cell have the same identifying string, which would happen if mutations do not happen (subsection “4.2 Evolutionary dynamics”), or if connectedness within cells is not ensured (subsection “4.1 Cell dynamics”).

2) We do not see how negative surface tension may imply 'repulsion' (subsection “Evolutionary model”, subsection “The evolution of uni- or multicellular strategies depends on environment stability”, Discussion section) between cells, rather than just an average higher probability for sites at the cell surface of sticking to the medium than to other cells. 'dispersion', also, may be due to amplification of fluctuations by persistence on the time scale of cell velocity update. Description of the behaviour of cells in isolation, especially how cell displacement depends on the magnitude of negative gamma would be very useful.

3) We do not understand the explanation for the evolution of small cell-to-cell adhesion for high frequency of environmental change. The authors claim that clusters always migrate faster up the gradient than single cells (Discussion section), but then in subsection “The evolution of uni- or multicellular strategies depends on environment stability” they seem to indicate the opposite. In the present formulation it is not clear if the advantage of single cells is given by the growing importance of the transient to clustering after reproduction and culling (that we imagine introduces, willing or not, a sort of local dispersal by creating 'holes' in coherent clusters), or by the fact that moving fast in one direction might not be the best strategy when such direction changes very fast (alike environmental response vs bet-hedging).

4) We wonder if the fact that the string defining adhesion to the medium is a substring of that defining adhesion to other cells may have evolutionary effects, as the two kinds of adhesion will be in general correlated. We understand that this is a convenient choice, but are not sure that the existence of such correlations may be justified for cells. Secondly, by looking at Appendix Figure A2.1, we are puzzled by the statement that cell–cell variation in adhesion strength after evolution is small (subsection “The evolution of uni- or multicellular strategies depends on environment stability” and Appendix subsection “2.1 Adhesion strength distribution for τs = 100 x 103 MCS”), since no quantitative comparison is made with other situations (for instance, when the unicellular strategy evolves?).

# Resource plasticity-driven carbon-nitrogen budgeting enables specialization and division of labor in a clonal community

## Authors

- Sriram Varahan<sup>1</sup> ([ORCID: 0000-0002-3609-4032](https://orcid.org/0000-0002-3609-4032))
- Vaibhhav Sinha<sup>2</sup> ([ORCID: 0000-0002-5169-5485](https://orcid.org/0000-0002-5169-5485))
- Adhish Walvekar<sup>1</sup> ([ORCID: 0000-0001-7344-7653](https://orcid.org/0000-0001-7344-7653))
- Sandeep Krishna<sup>2</sup> ([ORCID: 0000-0002-0581-173X](https://orcid.org/0000-0002-0581-173X)) †
- Sunil Laxman<sup>1</sup> ([ORCID: 0000-0002-0861-5080](https://orcid.org/0000-0002-0861-5080)) †

### Affiliations

1. InStem - Institute for Stem Cell Science and Regenerative Medicine Bangalore India
2. Simons Centre for the Study of Living Machines, National Center for Biological Sciences, Tata Institute for Fundamental Research Bangalore India
3. Manipal Academy of Higher Education Manipal India

† Corresponding author

## Abstract

Previously, we found that in glucose-limited Saccharomyces cerevisiae colonies, metabolic constraints drive cells into groups exhibiting gluconeogenic or glycolytic states. In that study, threshold amounts of trehalose - a limiting, produced carbon-resource, controls the emergence and self-organization of cells exhibiting the glycolytic state, serving as a carbon source that fuels glycolysis (Varahan et al., 2019). We now discover that the plasticity of use of a non-limiting resource, aspartate, controls both resource production and the emergence of heterogeneous cell states, based on differential metabolic budgeting. In gluconeogenic cells, aspartate is a carbon source for trehalose production, while in glycolytic cells using trehalose for carbon, aspartate is predominantly a nitrogen source for nucleotide synthesis. This metabolic plasticity of aspartate enables carbon-nitrogen budgeting, thereby driving the biochemical self-organization of distinct cell states. Through this organization, cells in each state exhibit true division of labor, providing growth/survival advantages for the whole community.

## Introduction

During the development of microbial communities, groups of cells come together and exhibit heterogeneity within spatial organization (Ackermann, 2015). As the community develops, cells can present specialization of function, which allows the community as a whole to perform various tasks including the acquisition of food, defense against competing microorganisms, or more efficient growth (Newman, 2016; Niklas, 2014; West and Cooper, 2016). This division of labor allows breakdown of complex biological processes into simpler steps, eliminating the need for individual cells to perform several tasks simultaneously, thereby enhancing the overall efficiency with which cells in the community function (Giri et al., 2019; Johnson et al., 2012; Rueffler et al., 2012; van Gestel et al., 2015). Due to these advantages, division of labor is widely prevalent across diverse microbial communities and can be found at different levels of biological organization (Gordon, 2016; Kirk, 2003; Tarnita et al., 2013). However, the underlying rules that enable division of labor within cell populations remain to be deciphered.

In particular, microbial community development is commonly triggered by nutrient limitation (Ackermann, 2015; Hoehler and Jørgensen, 2013; Johnson et al., 2012). Clearly, an optimal allocation of resources is critical for maximizing overall fitness within a microbial community, especially when the availability of nutrients is limiting (Litchman et al., 2015; Wessely et al., 2011). One strategy by which the community can manage the requirement of different resources is by sharing metabolic products, and this is employed by many microbial communities (D'Souza et al., 2018; Liu et al., 2015). Since resources can often be insufficient, the sharing of such resources might incur a cost to the cell. Hence, different cells of the community exhibit metabolic interdependencies, presumably to balance out trade-offs arising from resource sharing. While this concept has been demonstrated for example, in synthetically engineered systems, where required metabolic dependencies are created between non-isogenic cells (Campbell et al., 2016; Campbell et al., 2015), this has been exceptionally challenging to demonstrate within a clonal community of cells. We recently discovered that metabolic constraints are sufficient to enable the emergence and maintenance of cells in specialized biochemical states within a clonal S. cerevisiae community (Varahan et al., 2019). Remarkably, this occurs through a simple, self-organized biochemical system. In yeast growing in low glucose, cells are predominantly gluconeogenic. As the colony matures, groups of cells exhibiting glycolytic metabolism emerge with spatial organization. Strikingly, this occurs through the production (via gluconeogenesis) and accumulation of a limiting metabolic resource, trehalose. As this resource builds up, some cells spontaneously switch to utilizing trehalose for carbon, which then drives a glycolytic state. This also depletes the resource, and therefore a self-organized system of trehalose producers and utilizers establish themselves, enabling structured phenotypic heterogeneity (Varahan et al., 2019).

This observation raises a deeper question, of how such groups of heterogeneous cells can sustain themselves in this self-organized biochemical system. In particular, is it sufficient to only have the build-up of this limiting, controlling resource? How are carbon and nitrogen requirements balanced within the cells in the heterogeneous states? In this study, we uncover how a non-limiting resource with plasticity in function can control the organization of this entire system. We find that the amino acid aspartate, through distinct use of its carbon or nitrogen backbone, enables the emergence and organization of heterogeneous cells. In gluconeogenic cells, aspartate is utilized in order to produce the limiting carbon resource, trehalose, which in turn is utilized by other cells that switch to and stabilize in a glycolytic state. Combining biochemical, computational modeling and analytical approaches, we find that aspartate is differentially utilized by the oppositely specialized cells of the community as a carbon or a nitrogen source to sustain different metabolism. This carbon/nitrogen budgeting of aspartate is crucial for the emergence of distinct cell states in this isogenic community. Through this, cell groups show complete division of labor, and each specialized state provides distinct proliferation and survival advantages to the colony. Collectively, we show how the carbon/nitrogen economy of a cell community enables a self-organizing system based on non-limiting and limiting resources, and this allows organized phenotypic heterogeneity in cells.

## Results

### Amino acid driven gluconeogenesis is critical for emergence of metabolic heterogeneity

In a previous study (Varahan et al., 2019), we discovered that trehalose controls the emergence of spatially organized, metabolically heterogeneous groups of cells within a S. cerevisiae colony growing in low glucose. Within this colony were cells with high gluconeogenic activity, and other cells showing high glycolytic/pentose phosphate pathway (PPP) activity (Figure 1A). The high glycolytic/PPP activity cells could be distinguished as ‘light’ cells, and the highly gluconeogenic cells as ‘dark’, based purely on optical density as observed by brightfield microscopy, as shown in Figure 1A (Varahan et al., 2019). In this system, cells start in a gluconeogenic state, and these cells (dark) produce trehalose. When a threshold concentration of external trehalose is reached, a subpopulation of cells switch to trehalose consumption that drives a glycolytic state, and these cells continue to proliferate as light cells (Figure 1A). Trehalose is a limiting resource since it is not freely available in the glucose limited external environment, and must be synthesized via gluconeogenesis (François et al., 1991). We therefore first asked how the loss of gluconeogenesis affects the emergence of metabolically specialized light cells. For this, we genetically generated mutants that lack two key gluconeogenic enzymes (PCK1 and FBP1). These gluconeogenic mutants (Δpck1 and Δfbp1) expectedly formed smooth colonies completely lacking structured morphology (which correlates with the absence of metabolic heterogeneity; Figure 1B and Figure 1—figure supplement 1A). Further, these mutants had essentially undetectable cells with high PPP activity (light cells), based on the fluorescence-signal of a PPP reporter, as compared to a wild-type colony, although the total number of viable cells in all the colonies were comparable (Figure 1C and Figure 1—figure supplement 1B). This confirms that gluconeogenesis is critical for the emergence and maintenance of metabolic heterogeneity in the colony.

![Figure 1.](https://cdn.elifesciences.org/articles/57609/elife-57609-fig1-v2.jpg)

**Figure 1.:** (A) External trehalose controls the emergence of light cells. Trehalose synthesized by the dark cells fuels glycolysis and pentose phosphate pathway in light cells. (B) Gluconeogenesis is required for development of structural morphology in the colonies. The panel shows the morphology of mature wild-type and gluconeogenic mutant (∆pck1 and ∆fbp1) yeast colonies in rich medium, with supplemented glucose as the sole variable. Scale bar: 2 mm. Also see Figure 1—figure supplement 1A for more information. (C) Spatial distribution of mCherry fluorescence across a colony, indicating the activity of a reporter for pentose phosphate pathway (TKL1) activity in wild-type and gluconeogenesis defective mutants (∆pck1 and ∆fbp1). (D) Amino acids and in particular aspartate is required for the development of structural morphologies in the colonies in a gluconeogenesis dependent manner. The panel shows the morphology of mature wild-type and gluconeogenesis-defective (∆pck1) yeast colonies in minimal medium (low glucose), with and without amino acid supplementation, or with only aspartate supplementation. (E) Spatial distribution of mCherry fluorescence across a colony, indicating the activity of a reporter for pentose phosphate pathway (TKL1) activity in wild-type colonies grown either in minimal media or minimal media supplemented with all amino acids or just aspartate.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/57609/elife-57609-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Gluconeogenesis is required for development of structural morphology in the colonies. The panel shows the morphology of mature wild-type and gluconeogenesis defective (∆pck1 and ∆fbp1) yeast colonies in rich medium, with supplemented glucose as the sole variable. Scale bar: 2 mm. (B) Viability of cells in wild-type, Δpck1 and Δfbp1 colonies grown in rich medium (low glucose) for 7 days were measured by collecting cells from the colonies and plating them in rich medium (n = 5). Statistical significance was calculated using unpaired t test and error bars represent standard deviation. Similarly, viability of cells in wild-type colonies grown either in minimal media or minimal media supplemented with all amino acids, or just aspartate, were measured by collecting cells from the colonies and plating them in rich medium (n = 5). Statistical significance was calculated using unpaired t test and error bars represent standard deviation. (C) The panel shows the morphology of mature wild-type and gluconeogenesis defective (∆pck1) yeast colonies grown for 7 days in minimal medium (low glucose), with and without supplementation of the indicated amino acids. Scale bar: 2 mm.

Trehalose, the produced resource controlling the switch to the light state (Varahan et al., 2019), is a disaccharide made up of two molecules of glucose and is produced via gluconeogenesis. This two-state community of cells requires a continuous supply of trehalose to sustain itself. Therefore, in order to address how dark cells maintained threshold concentrations of trehalose, we asked how this resource itself is produced. Notably, the media conditions under which these colonies develop essentially have non-limiting amounts of amino acid resources (2% yeast extract and 2% peptone). We therefore hypothesized that amino acids (available in non-limiting levels) could act as carbon sources (via possible anaplerotic processes) to fuel trehalose production in dark cells. We tested this by growing wild-type cells in media devoid of free amino acids, but with sufficient ammonium sulfate (Minimal medium). Wild-type colonies failed to develop structured colonies (which correlates with the lack of metabolic heterogeneity) in the absence of free amino acids, and this could be rescued by adding back amino acids to this media (Figure 1D). Expectedly, this amino acid dependent rescue of colony morphology depended on gluconeogenesis, since a Δpck1 strain failed to develop morphology even after the addition of amino acids to the medium (Figure 1D). This shows that non-limiting amino acids promote the development of structured colonies exhibiting metabolic heterogeneity, in a gluconeogenesis dependent manner. Interestingly this amino acid dependent effect is specific. In add-back experiments in minimal medium, amongst all amino acids tested, aspartate supplementation strongly promoted the development of structured colonies exhibiting metabolic heterogeneity (Figure 1D). This ‘rescue’ by aspartate was stronger than that seen with the addition of any other amino acids individually or in combination (Figure 1D and Figure 1—figure supplement 1C). This was further validated via experiments wherein wild-type colonies that developed in minimal medium, supplemented either with all amino acids, or only aspartate alone, exhibited spatially restricted metabolic heterogeneity comparable to the wild-type colonies grown in rich media. The light cell population was estimated using the fluorescent PPP reporter, which serves as an excellent proxy for light cells (Varahan et al., 2019; Figure 1E and Figure 1—figure supplement 1B). Collectively, these results reveal that aspartate is sufficient for the development of metabolically specialized colonies in a gluconeogenesis-dependent manner. The addition of other amino acids (particularly glutamine/glutamate) only show a delayed, weaker emergence of light cells. This would be consistent with their eventual, steady conversion to aspartate, which will not result in a build-up of excess amounts of this amino acid.

### Aspartate promotes light cell emergence by directly fueling trehalose synthesis

In contrast to their canonical roles as nitrogen sources, amino acids can also act as carbon donors for several metabolic processes (Boyle, 2005). While many amino acids can enter the tricarboxylic acid (TCA) cycle via anaplerosis, and TCA intermediates in turn can enter gluconeogenesis, aspartate is unique. It is the only amino acid that can directly enter gluconeogenesis, without entering into the TCA cycle. This is via the conversion of aspartate into oxaloacetate directly in the cytosol through the activity of aspartate transaminase. In this cytosolic process, aspartate and 2-oxoglutarate combine to give one molecule each of oxaloacetate and glutamate. All the other amino acids have to be first transported to the mitochondria and enter the TCA cycle, and these TCA intermediates must then be transported back to the cytosol to enter gluconeogenesis (Brunengraber and Roe, 2006). Since the addition of aspartate alone to minimal media was sufficient for light cells to emerge, we tested if aspartate is a direct carbon source required for trehalose production within the colony, since trehalose is a pre-requisite for light cell emergence. Wild-type colonies were grown in minimal media supplemented with all amino acids, or aspartate alone, or all amino acids without aspartate (aspartate dropout) and total trehalose levels in the 7 day old colonies were measured. As controls, trehalose levels in the Δpck1 colonies (gluconeogenesis defective) and Δtps1 colonies (trehalose synthesis defective) were measured. Compared to colonies grown in minimal medium, colonies grown in minimal medium supplemented with all amino acids, or aspartate alone, had significantly higher amounts of trehalose (Figure 2A). Notably, the level of trehalose in wild-type colonies grown in aspartate dropout minimal medium was significantly lower compared to colonies grown in minimal media supplemented with all amino acids or just aspartate, demonstrating that aspartate can be the primary carbon contributor towards trehalose synthesis (Figure 2A). As expected, Δpck1 colonies (gluconeogenesis defective) and Δtps1 (trehalose synthesis defective) had background levels of trehalose (Figure 2A). Furthermore, colonies grown on aspartate dropout medium had fewer light cells (quantified using the PPP reporter activity) compared to colonies grown in minimal media supplemented with all amino acids or just aspartate (Figure 2B and Figure 2—figure supplement 1). This shows that aspartate enables trehalose production, which in turn controls the emergence of metabolic heterogeneity in these clonal colonies (Figure 2A and B). To demonstrate that aspartate directly provides the carbon backbone of trehalose, we grew colonies in minimal medium (low glucose) supplemented with 13C-labeled aspartate, and measured intracellular levels of 13C–labeled gluconeogenic intermediates or end-products directly by targeted mass spectrometric methods described earlier (Vengayil et al., 2019; Figure 2C). Cells in wild-type colonies accumulated 13C-labeled 3-phosphoglycerate (3 PG) and 13C-labeled trehalose, while these labeled metabolites were undetectable in a gluconeogenic mutant (Δpck1) (Figure 2D). Collectively, these data show that aspartate provides the carbon skeleton for trehalose production via gluconeogenesis, and this turn is essential for the emergence of spatially restricted metabolic heterogeneity.

![Figure 2.](https://cdn.elifesciences.org/articles/57609/elife-57609-fig2-v2.jpg)

**Figure 2.:** (A) Comparative steady-state amounts of trehalose measured in wild-type, ∆pck1 (gluconeogenesis defective) and ∆tps1 (trehalose synthesis defective) colonies grown in minimal medium, or minimal medium supplemented with either all amino acids, or aspartate alone, or all amino acids without aspartate (aspartate dropout) (n = 3). Colony insets represent wild-type colony morphology in different media conditions. Statistical significance was calculated using unpaired t test (*** indicates p<0.001) and error bars represent standard deviation. (B) Aspartate significantly contributes to colony development and emergence of light cells. Spatial distribution of mCherry fluorescence across a colony, indicating the activity of a reporter for pentose phosphate pathway (TKL1) activity in wild-type yeast colonies grown in minimal medium (low glucose), supplemented with either all amino acids, or aspartate alone, or all amino acids without aspartate (aspartate dropout). Also see Figure 2—figure supplement 1A for more information. (C and D) Metabolic-flux based analysis comparing relative 13C incorporation from 13C-labeled aspartate into newly synthesized gluconeogenic intermediates (3-phosphoglycerate and glucose-6-phosphate) and trehalose, in wild-type and ∆pck1 colonies.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/57609/elife-57609-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) The light cell population was calculated by spotting wild-type cells harboring the PPP reporter plasmid either in minimal media or minimal media supplemented with either all amino acids or aspartate or all amino acids without aspartate (aspartate dropout). After 7 days of growth, cells from the entire colony (for each media condition) were collected and the percentage of fluorescent cells from colonies grown in each media condition were quantified (2000 cells per colony and three colonies per media condition). Statistical significance was calculated using unpaired t test (** indicates p<0.01, *** indicates p<0.001) and error bars represent standard deviation.

### An agent-based model suggests how differential aspartate utilization drives the emergence of self-organized, metabolically heterogeneous states

We had previously noted that the light cells had higher rates of nucleotide synthesis (Varahan et al., 2019). Synthesis of the nucleotide backbone requires an assimilation of carbon (typically from glucose derived metabolites, notably pentose sugars from the PPP), as well as nitrogen that comes from amino acids (primarily glutamine and aspartate) (Boyle, 2005). Indeed, this donation of nitrogen by aspartate towards nucleotide synthesis is considered a primary role of this amino acid. Interestingly, within the dark cells of the colony, aspartate is also being used as a carbon source for the synthesis of trehalose (Figure 2D). This raises the central idea of molecular budgeting: how is the utilization of aspartate as a carbon/nitrogen source managed in different types of cells? To theoretically address this question, we refined our originally coarse-grained mathematical model from Varahan et al., 2019. In the original model that simulates the development of the colony with dark and light cells, the resource driving the emergence of light cells was featureless and could only be used to drive hypothetically opposite metabolism (Varahan et al., 2019). In our new model, we now build-in molecule specificity. Based on experimental data, we incorporate aspartate utilization for the emergence of metabolic subpopulations, and self-organization within the colony. The processes now included in the model are explained below (See Materials and methods for a detailed description):

Both dark and light cells utilize externally available resources to synthesize and accumulate the metabolites needed for growth. We can now assign two specific categories for these accumulating metabolites: carbon (C) and nitrogen (N). The dark cells utilize a single resource, aspartate, to serve both C and N requirements. Aspartate itself is a molecule that is in excess in the environment (non-limiting). We propose that the dark cells budget the aspartate flux for both these requirements, and some of the accumulated C (as trehalose) becomes available in the extracellular environment. From our earlier findings (Varahan et al., 2019), we know that the extracellular trehalose controls when some dark cells switch to being light cells. The light cells utilize the available trehalose for their C needs (driving glycolysis and the PPP). However, aspartate remains readily available for their N requirements, which includes nucleotide synthesis (this is illustrated in the model schematic and sample colony in Figure 3A). We now implement this revised model as an agent-based simulation, and monitor colony growth with these new assumptions of aspartate utilization. The specific modifications from the original model and the new parameters are introduced below:

![Figure 3.](https://cdn.elifesciences.org/articles/57609/elife-57609-fig3-v2.jpg)

**Figure 3.:** (A) A model schematic based on an experimental understanding of aspartate utilization by the two cell types in the system. Dark and light cells are colored accordingly. Dark cells take in aspartate, budget it for nitrogen (N) and carbon (C) needs. Some of the accumulating C is released into the extracellular environment as trehalose, triggering the switching into light cells and also acting as the primary C source for light cells as it diffuses in the 2D space. On the right, we have a representative simulated colony generated from a default parameter set. Parameters are indicated in the parentheses. (B) Varying the fraction of aspartate flux allocated towards nitrogen (N) in order to observe the simulated colony over the same length of time. When the majority of the flux is used for carbon (C) needs, the simulated colonies resemble experimental colonies. If less aspartate is allocated for C rather than N, the developed colonies no longer resemble the experimental colonies. (C) Varying the relative rate of aspartate uptake compared to trehalose uptake by the light cells in order to observe simulated colonies over the same length of time. If the rate is the same, as shown in the first simulated colony where AspU = 1.0, the colony is underdeveloped. A middle value of AspU = 4.0 generates colonies similar to experimental colonies, while for a large value of AspU on the right, the dark cell blocks and light cell blocks have similar division times and the final colony is larger.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/57609/elife-57609-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Dark cells secrete a fraction, Pf, of their internal carbon levels as trehalose. However, we place an upper limit on the absolute amount of secreted trehalose at 0.12 units/Time. This limit is meant to mimic realistic export conditions. An assumption made is that due to physiological constraints on the cell, the amount of trehalose exported/present outside should not be arbitrarily large. This figure shows that most of the time, the cells are operating well below this upper limit. This demonstrates that the rate of trehalose production in the system is governed by other processes of the model pertaining to uptake, budgeting and growth by division.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/57609/elife-57609-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** The bins along the x-axis measure the time steps elapsed between a cell block’s birth and when it divides. The cell blocks have the same probability of division once they build up sufficient N and C reserves. These histograms illustrate that the division times in our simulation are different due to resource requirements being fulfilled at different times.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/57609/elife-57609-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Each panel is a generated colony using the values of ‘f’ and ‘AspU’ corresponding to its location. Note: the axes values are not on a linear or logarithmic scale but are chosen for representative purposes to show parametric trends. Increasing AspU increases the rate of aspartate influx into the system. Overall, this generates larger colonies. Since dark cell blocks are not limited by the trehalose production, they divide at about the same rate as light cell blocks. This is contrary to experimental observations where dark cells grow slower than light cells. With the parameter f, extremely low values allocate too little of the metabolic budget to nitrogen reserves. This results in slow growing colonies which have a higher fraction of light cell blocks. On the other hand, higher values allocate too much of the budget to nitrogen reserves. This slows down the rate of trehalose production, thereby slowing down the emergence of light cells and their proliferation and gives us smaller overall colonies. Thus, increasing both AspU and f together leads to realistic looking colonies as observed along the top diagonal elements in this figure. The blue shaded central panel in the figure is a colony generated using default values of f and AspU.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/57609/elife-57609-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** (A) A colony where light cell blocks are not allowed to switch to dark cell blocks during the simulation. This is similar to the original model implemented in Varahan et al., 2019. (B) A colony implemented using our current model, where light cell blocks can switch to dark cell blocks with a low probability (PLD = 10−4/Time), if the level of trehalose at their location is below a certain threshold (TLD = 10−4 units). The two panels illustrate how the colonies are not significantly different, but the current model does not constrain the light cells to remain fixed in their metabolic state.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/57609/elife-57609-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** A step-by-step description is provided in the Materials and methods section of the main text.

By varying the two main parameters in this study, the model makes the following predictions:

![Video 1.](https://cdn.elifesciences.org/articles/57609/elife-57609-video1.mp4.jpg)

**Video 1.:** A simulation movie of the WT colony over 750 time-steps (~6 days in real time). The colony starts with 95–99% dark cells, which go through switching and growth phases as observed. This colony is generated using default parameter values in the model.

![Video 2.](https://cdn.elifesciences.org/articles/57609/elife-57609-video2.mp4.jpg)

**Video 2.:** A simulation movie where the budgeting fraction ‘f’ is 50%, i.e., 50% of the aspartate flux is allocated towards nitrogen reserves. The dark cell blocks cannot allocate sufficient carbon for themselves, leading to almost no divisions by the dark cell blocks while the light cells at the edge keep proliferating. For comparison, the default value of ‘f’ is 12.5%.

![Video 3.](https://cdn.elifesciences.org/articles/57609/elife-57609-video3.mp4.jpg)

**Video 3.:** A simulation movie where the relative rate of aspartate uptake is equal to the trehalose uptake rate. (i.e. AspU = 1.0). In this case, the aspartate uptake by dark cells is much slower, which also leads to slower trehalose production, resulting in smaller colonies consisting of predominantly dark cell blocks.

![Video 4.](https://cdn.elifesciences.org/articles/57609/elife-57609-video4.mp4.jpg)

**Video 4.:** A simulation movie where the relative rate of aspartate uptake is high. (i.e. AspU = 8.0). In this case, the dark cells allocate adequate aspartate for both nitrogen and carbon requirements rapidly enough. This leads to both dark and light cells having nearly the same division rate.

### Aspartate allows differential carbon/nitrogen budgeting in light and dark cells of the colony in vivo

Our agent-based model suggested that the emergence of light cells and the spatial patterns similar to those observed experimentally arise when aspartate is used predominantly as a carbon source in dark cells. We therefore hypothesized that distinct cells in the colony might differentially utilize aspartate predominantly as either a carbon or a nitrogen source. We previously showed that light cells exhibit high PPP activity and nucleotide biosynthesis, using carbon precursors derived from the trehalose, provided by the dark cells (Varahan et al., 2019). As mentioned earlier, aspartate serves as a nitrogen donor in the synthesis of purine and pyrimidine nucleotides, but can also serve as a gluconeogenic substrate, providing the carbon backbone for the synthesis of trehalose (Figure 4A; Jones, 1980). Based both on theory and our model simulations, can we now experimentally test if aspartate predominantly serves as a carbon source in dark cells to fuel trehalose production, while primarily providing nitrogen for nucleotide biosynthesis in light cells? Note that this will not be absolute: all cells will make some nucleotides, and so aspartate will provide nitrogen in both dark and light cells. An expectation would be a relative difference in flux, which is the essence of this idea of differential carbon/nitrogen budgeting.

![Figure 4.](https://cdn.elifesciences.org/articles/57609/elife-57609-fig4-v2.jpg)

**Figure 4.:** (A) Metabolic fates of aspartate: The carbon of aspartate (green) can be used for synthesis of molecules like trehalose via gluconeogenesis (green boxed). The nitrogen of aspartate (red) is incorporated into nucleotide precursors including inositol monophosphate (IMP) AND cytidine monophosphate (CMP) (red boxed). (B and C) Metabolic-flux based analysis comparing relative 13C incorporation from 13C labelled aspartate into newly synthesized gluconeogenic intermediate (3-phosphoglycerate) (n = 3) and trehalose, and 15N incorporation from 15N labelled aspartate into newly synthesized nucleotides, in light and dark cells (n = 2). Statistical significance was calculated using unpaired t test (** indicates p<0.01) and error bars represent standard deviation. For panel C, two independently carried out biological replicates are shown.

We decided to investigate this directly, by using a stable-isotope based quantitative metabolic-flux approach. We grew wild-type colonies in minimal media containing 13C-labeled aspartate, and collected light and dark cells by rapid micro-dissection of the ~1 cm colonies, followed by immediate quenching of the cells and metabolite extraction (see Materials and methods), and measured the amounts of 13C–labeled gluconeogenic metabolites (3 PG and 13C–trehalose), respectively in dark and light cells by LC-MS/MS. Dark cells accumulated significantly higher levels of 13C-labeled 3 PG and 13C-labeled trehalose as compared to the light cells (Figure 4B). Using a similar experimental approach with 15N-labeled aspartate provided, we next measured the relative nitrogen-label incorporation into nucleotides in light and dark cells. Here, in stark contrast to the earlier results for carbon, the light cells accumulated substantially higher levels of 15N-labeled nucleotides compared to dark cells (Figure 4C). Collectively, we experimentally observe differential C/N budgeting in light and dark cells, based on aspartate utilization.

Thus, aspartate exhibits metabolite plasticity within the cells of a colony. The gluconeogenic dark cells utilize this amino acid primarily as a carbon source in gluconeogenesis (leading to trehalose production), while the light cells (with high PPP activity) predominantly utilize aspartate as a nitrogen donor for nucleotide biosynthesis. Collectively, these results reveal how plasticity in the use of a non-limiting resource, aspartate, enables the development of metabolically heterogeneous colonies.

### Dark and light cells exhibit division of labor, with distinct survival and collective growth advantages

What can this type of formation of specialized states, derived from biochemically self-organizing systems, mean for such a community of cells? Non-genetic heterogeneity can be beneficial for cell populations. Due to heterogeneity, some individual cells can survive environmental changes, which thereby allow genotypes to persist in ever-changing environments. Further, division of labor between individuals of a community can enhance collective community growth, development, and the efficiency of the functions that they perform (Giri et al., 2019; van Gestel et al., 2015). We therefore wondered if the distinct metabolic states within the yeast colony conferred a collective growth or survival advantage. Yeast cells routinely encounter environmental fluctuations like desiccation and freezing/thawing regularly (Gasch, 2007; Gasch and Werner-Washburne, 2002). Here, trehalose particularly enables the survival of yeast cells when faced with such environmental insults (D'Amore et al., 1991; Erkut et al., 2016; Wiemken, 1990). Since dark (gluconeogenic) cells accumulate high amounts of trehalose (Varahan et al., 2019), we suspected that these cells might better survive extreme conditions like desiccation and freezing/thawing. To test this, we isolated light and dark cells from ~7 day old colonies and subjected them to repeated freeze/thaw cycles or severe desiccation (7 and 14 days). We used yeast cells grown in glycolytic or gluconeogenic liquid medium as controls, and measured cell survival either by spotting the cells on a fresh plate (for a freeze/thaw tolerance) or counting the percentage of surviving cells (for desiccation tolerance). Dark cells showed markedly higher survival rates post freeze/thaw treatment (similar to the gluconeogenic control) compared to light cells (which phenocopied cells grown in high glucose) (Figure 5A). Similarly, dark cells survived complete desiccation better than light cells (Figure 5B). Finally, we looked at the role of dark cells in the long-term survivability of the wild-type colony as a whole. To dissect this, we used cells lacking the trehalase enzyme (Δnth1) as a control, since colonies from these cells produce but cannot utilize trehalose to fuel glycolysis, and lack light cells (Varahan et al., 2019). We also compared these to the long-term survivability of Δpck1 cells (gluconeogenesis-defective), since these colonies lack both light and dark cells. Although we did not see a difference in the number of viable cells in the 7 day old colonies, in mature (21 day) colonies the percentage of viable cells were significantly lower in the Δpck1 colonies compared to the wild-type and Δnth1 colonies (Figure 5C). Therefore, the presence of dark cells positively influences the long-term survivability of the colony as a whole, and these cells can survive environmental insults like desiccation, freeze/thaw cycles and nutrient limitation.

![Figure 5.](https://cdn.elifesciences.org/articles/57609/elife-57609-fig5-v2.jpg)

**Figure 5.:** (A) Equal numbers of light and dark cells were subjected to multiple freeze-thaw cycles, and survival estimated by spotting onto rich media plates and allowing growth for 18 hr. Cells grown in gluconeogenic medium (2% ethanol/glycerol) and glycolytic medium (2% glucose) were used as controls. (B) Desiccation tolerance of light and dark cells were measured after 7 days and 14 days (n = 3). Statistical significance was calculated using unpaired t test (** indicates p<0.01) and error bars represent standard deviation. (C) Long term viability of cells in wild-type (light and dark cells), Δnth1 (only dark cells) and Δpck1 (no light or dark cells) colonies were measured by growing colonies for either 7 or 21 days and collecting cells from the colonies and plating them in rich medium (n = 5). Statistical significance was calculated using unpaired t test (** indicates p<0.01) and error bars represent standard deviation. (D and E) Foraging responses of wild-type, Δnth1 and Δpck1 cells measured as a function of their ability to spread on a plate. Colony spreading was quantified by measuring the diameter of the colonies every day for 21 days (n = 3). Statistical significance was calculated using unpaired t test (** indicates p<0.01) and error bars represent standard deviation. Scale bar: 2 mm. (F) Directional foraging of light cells towards glucose was measured by growing wild-type cells, Δnth1 cells and Δpck1 cells on rich medium plates (low glucose) and placing a paper disc soaked in 50% glucose at a distance of 2 cm from the colonies (n = 3).

Complex colony development under nutrient limitation includes foraging responses, where the outward expansion of the colony allows the cells to reach fresh nutrient sources (Palková and Váchová, 2016; Váchová and Palková, 2018). We previously observed that light cells enable efficient colony expansion, and colonies with only dark cells (Δnth1 trehalase mutants) cannot expand as efficiently as a wild-type colony (Varahan et al., 2019). Since the gluconeogenesis defective mutant (Δpck1) lacked light cells, we also hypothesized that these colonies are compromised at colony expansion as well. To test this, wild-type, ∆nth1 and ∆pck1 were spotted as colonies and colony expansion was monitored over time (7 days and 21 days). At 21 days, the Δnth1 and Δpck1 colonies had significantly reduced expansion compared to wild-type colonies. This reiterates that the light cells are important for the effective long-term expansion of the colony (Figure 5D and E). This also suggests the possibility that colonies lacking light cells may not be able to expand towards suitable nutrients. To contextualize this with the localized availability of high-quality nutrients, we designed an experiment where an external source of glucose was added to the plate at some distance from the colony, and the expansion of colonies towards this glucose source was estimated (Figure 5F). Strikingly, the light cells from wild-type colonies showed rapid, directional proliferation towards the glucose source. Notably, both the Δnth1 cells (trehalose-breakdown deficient, no light cells), and the Δpck1 cells (no trehalose production) showed markedly reduced directional movement towards the glucose source (Figure 5F). This was quantified using an expansion factor (the ratio of the colony area of the half of the colony growing towards the glucose source/colony area of the other half of the colony) (Figure 5F). These data conclusively show that light cells are essential for the outward expansion and foraging response of the colony. Together, the presence of dark and light cells allows greater colony survival, resistance to stress, and the ability to expand towards preferred nutrient sources. This can collectively provide the colony with the ability to persist and thrive in varying environments, and is further discussed below.

## Discussion

We present data illustrating how plasticity in the use of a non-limiting resource, aspartate, is sufficient for the emergence and maintenance of spatially organized, distinct metabolic states of groups of cells. Aspartate is required for gluconeogenic cells to achieve threshold concentrations of a limiting resource, trehalose, which in turn drives specialization in these clonal microbial communities (Figure 6). In low glucose conditions, cells expectedly perform gluconeogenesis to replenish glucose reserves. During this process, cells utilize aspartate predominantly as a carbon source that drives gluconeogenesis, via its conversion to oxaloacetate. One eventual metabolic outcome of gluconeogenesis is trehalose synthesis, and cells accumulate synthesized trehalose. Trehalose also directly benefits gluconeogenic cells, allowing them to survive environmental stresses including desiccation and repeated freeze/thaw cycles. As trehalose builds-up and threshold concentrations of externally available trehalose are reached, some cells stochastically take up and consume trehalose, breaking it down to glucose. This uptake and consumption of trehalose switches the metabolic state of these cells to that of high PPP/Glycolysis. In this complimentary metabolic state, cells now utilize aspartate as a nitrogen source. The combination of available glucose (from trehalose) combined with the use of aspartate as a nitrogen source allows light cells to synthesize end point molecules like nucleotides, which enable rapid proliferation, and efficient expansion and foraging for nutrients (Figure 6).

![Figure 6.](https://cdn.elifesciences.org/articles/57609/elife-57609-fig6-v2.jpg)

**Figure 6.:** Cells in low glucose perform gluconeogenesis (Dark cells), as would be required in low glucose medium. During this process, dark cells predominantly budget aspartate for their carbon needs to synthesize trehalose. The accumulated trehalose reserves in the dark cells allow them to survive environmental challenges including desiccation and repeated freeze/thaw cycles. Trehalose also accumulates externally, and once threshold levels of external trehalose are reached, some cells stochastically switch to the light state and utilize this trehalose to fuel their high glycolysis and pentose phosphate pathway (PPP) activity. Cells that switch to the light cell state predominantly use aspartate as a ‘nitrogen’ source to synthesize nucleotides via PPP, while utilizing trehalose for their carbon needs. This makes light cells primed for proliferation, which in turn results in increased or directional colony expansion. This metabolic specialization and division of labor between the light and dark cells creates a cross-feeding system (built around trehalose), and allows the colony as a whole to survive unfavorable conditions and forage efficiently even in nutrient limiting conditions.

Key to understanding this self-organized system of cells existing in specialized states, with cells in one state dependent on the functioning of the other, is the idea of distinct carbon-nitrogen budgeting which depends on a metabolically plastic resource. This can function as both a carbon and nitrogen source. Previously we showed how trehalose availability can create a self-organized system, where some cells will switch a new (glycolytic) metabolic state, and these cells will themselves be sustained by the cells in the original (gluconeogenic) metabolic state that produce trehalose (Varahan et al., 2019). In this system, trehalose is a limiting metabolite. It is minimal in the cells that seed the colony, and builds up over time due to gluconeogenesis, which is the required metabolic state in low glucose conditions. Only when trehalose builds up, some cells switch to a glycolytic state. Such an idea of threshold amounts of sentinel metabolites that can control cell states is an emerging area of interest (Cai and Tu, 2011; Krishna and Laxman, 2018). In this study, we take a step back to discover that the underpinnings of this system, which lead to the formation of this limiting resource (trehalose) lies in a metabolic economy where carbon and nitrogen need to be ‘budgeted’ distinctly. This requires a metabolically plastic resource available in sufficient (‘non-limiting’) quantities. In order for cells to achieve threshold levels of the limiting resource, trehalose, cells utilize a non-limiting resource (aspartate) to fuel trehalose biosynthesis. Conventionally, aspartate is thought of as a ‘nitrogen’ source since it is required for nucleotide metabolism (Boyle, 2005). However, as we also observe in this study, aspartate serves as an effective carbon source to synthesize trehalose via gluconeogenesis in dark cells. In light cells, carbon is no longer limiting (since these cells can utilize the built-up trehalose). In these cells, aspartate can go back to predominantly satisfy its ‘conventional’ role as a nitrogen donor for nucleotide synthesis. This differential use of a single metabolite to meet distinct carbon and nitrogen demands of cells in opposite metabolic states is a remarkable example of metabolic budgeting within spatially organized cells. This plastic ability of aspartate, combined with non-limiting amounts at which it is available makes it the driver of phenotypic heterogeneity in this system. Cross-feeding systems, where groups of cells produce resources that another group of cells utilize are widely prevalent in microbial systems (D'Souza et al., 2018; Doebeli, 2002). Typically, this involves multi-species communities, or dependent auxotrophs. Here one group of cells cannot efficiently carry out a specific metabolic task, and obtain required precursors from other cells that produce it (and vice versa) (Johnson et al., 2012; Mee et al., 2014; Wintermute and Silver, 2010). Contrastingly, studies of organized, interdependent specialization of function in cell groups within spatially restricted, clonal microbial communities are relatively uncommon. Our study in a clonal yeast colony illustrates how simpler, self-organized biochemical networks, built on differential metabolic budgeting, and driven by mass-action based flux towards the production/utilization of specific resources, are sufficient to enable sustainable cross-feeding systems without a requirement for metabolic auxotrophies or metabolic deficiencies.

In these contexts, our coarse-grained and more refined agent-based models can be instructive in revealing the range of possible scenarios that can enable such metabolic networks in cross-feeding systems (Laxman and Krishna, 2020). Our original model only showed how a build-up of a resource, and its subsequent consumption, would create a specific type of patterning/organization of cells (with resource ‘users’ and ‘producers’) (Varahan et al., 2019). With this improved, agent-based model, we can now bring context and dissect out what the consequences of differential carbon/nitrogen budgeting, with the use of non-limiting resources, and the production and use of limiting resources, might entail. Note that such models only demonstrate that the mechanisms they include are sufficient to explain observed phenomena; they do not demonstrate the necessity of these mechanisms. However, showing sufficiency is useful as a consistency check on our biological understanding of the mechanisms at play, and in providing a framework within which to explore constraints on the mechanisms that we believe are biologically important. Our model suggested that, with the mechanisms included, the experimentally observed spatial patterns only arose when aspartate was predominantly used as a carbon source in gluconeogenic cells, which we then confirmed experimentally. Importantly, such models also show how such processes require spatial structure and organization to sustain themselves, and suggest entirely different requirements for well-mixed populations of cells. For example, well-mixed yeast cultures in glucose limitation undergo well studied metabolic cycles (Laxman and Tu, 2010; Kudlicki et al., 2005), coincident with a fraction of the population committing to growth and proliferation while other cells remain quiescent. In this context, distinct models, based on the formation of relaxation oscillators, explain how threshold amounts of metabolites control cell state switching and heterogeneity (Burnetti et al., 2016; Krishna and Laxman, 2018; Laxman and Krishna, 2020).

This population of clonal yeast cells existing as a cross-feeding population exhibits many features that are consistent with a colony level bet-hedging strategy. The dark cells (which are a majority of the population) are highly gluconeogenic, and exhibit general features of a starvation state. When glucose is limited, cells will shift to gluconeogenesis, and in these conditions, mass action dependent metabolic flux is extremely high towards trehalose synthesis, making the production of this resource an unavoidable, ‘default’ outcome. Since aspartate is available in non-limiting amounts for these developing colonies, dark cells have no shortage of carbon precursors required for the synthesis of trehalose. Trehalose is a versatile metabolite, that enables dark cells to survive and persist through extreme environments that yeast cells come across naturally (such as surviving water loss [desiccation], or freeze-thaw cycles etc. [D'Amore et al., 1991; Erkut et al., 2016; Wiemken, 1990]). In contrast, the light cells are glycolytic, with high pentose phosphate activity. This is a metabolic signature of a ‘growth state’ (van den Brink et al., 2008; Wiebe et al., 2008), and these cells achieve this state because they can take up and breakdown the available trehalose to fuel glycolysis. Importantly, cells in both states are required, for the colony as a whole to collectively, successfully expand and forage for nutrients (as shown here, and previously [Varahan et al., 2019]). Foraging for nutrients is an important strategy used by microbial communities to tackle nutrient limitation. The presence of cells in both metabolic states allows the following: each state is primed for a different nutrient condition. The dark cells will easily transition to quiescence and survive extreme stress. The light cells are poised to rapidly grow when the colony reaches a more favorable (glucose replete) nutrient environment by foraging. It therefore appears that the benefits of trehalose production and utilization by the dark and light cells (for different purposes, via the differential budgeting of carbon and nitrogen coming from aspartate) are considerable, in contrast to the minimal biochemical costs of production.

The principles emerging from this two-state system in a yeast colony are pertinent to the emergence of complexity from relatively simple processes. In an elegant theoretical framework, Cornish-Bowden and Cardenas formulated how in a living system, self-organizing processes can maintain themselves indefinitely, and how they can be modified across generations (Cornish-Bowden and Cárdenas, 2008). In their study, they extend the original idea of ‘metabolism-replacement systems’ (M-R systems), and the importance of metabolic closure (Rosen, 1972; Rosen, 1966; Rosen, 1965). A living M-R system, as conceptualized (Cornish-Bowden and Cárdenas, 2008), requires a few specific properties: (1) some molecules are available in unlimited quantities from the environment, (2) a partition must be present to separate the system from its environment, (3) these molecules can enter in and out of the partition, (4) the chemistry of these molecules enable them to participate in biochemical cycles, (5) these molecules/reactions will not participate in processes that interfere with these biochemical cycles, and (6) the thermodynamics of these reactions are sufficiently favorable. By these definitions, this yeast colony where the combination of aspartate in (practically) non-limiting amounts, as well as the build-up and use of a limiting resource (trehalose), along with the separation of compartments (and cells) for different biochemical processes where these molecules are used, largely works as a M-R system that enables the stable emergence and maintenance of phenotypically heterogeneous states. This system, with biochemical specialization and division of (metabolic) labor is also a demonstration of both the importance of specific enzymes (eg. trehalase), and metabolic control analysis, leading to the distribution of tasks via the differential budgeting of carbon and nitrogen. This is the essence of a cellular or multi-cellular economy where metabolic supply and demand must be balanced, and which depends on the combination of resources available (Hofmeyr, 2008; Hofmeyr and Cornish-Bowden, 2000).

The result of this self-organized system are groups of clonal cells, spatially organized into groups that exhibit division of labor (van Gestel et al., 2015; West and Cooper, 2016). Dividing tasks between lower units (such as groups of cells) can allow tremendous enhancements in efficiency of processes. By enforcing division of labor, microbial communities effectively achieve what multicellular organisms do within tissues, and aid in the development of the whole community. While division of labor has often been used loosely, more stringent definitions of division of labor require (1) functional complementarity, (2) synergistic advantages, (3) negative frequency-dependent selection, and (4) positive assortment (Giri et al., 2019). This yeast colony, with its self-organized system of cells in opposite metabolic states, appears to satisfy these criteria for division of labor. The result is a community of clonal cells where each metabolic/phenotypic state has individual advantages (greater survival or greater proliferation), enables the colony to adapt to fluctuating nutrient environments and survive environmental adversities, and also provides an increased growth advantage and capability to forage for new nutrients.

Summarizing, we demonstrate how efficient carbon/nitrogen resource budgeting and metabolic plasticity of a non-limiting resource are sufficient to control the emergence of spatially separated cells in specialized states. This division of labor, resulting in an interdependent cross-feeding system of cells provides collective advantages to the population to survive environmental challenges and expand towards new resources, in a manner reminiscent of multicellular organisms.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gene (Saccharomyces cerevisiae)</td>
      <td>pck1</td>
      <td>Saccharomyces genome database (SGD)</td>
      <td>SGD:S000001805</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Saccharomyces cerevisiae)</td>
      <td>fbp1</td>
      <td>Saccharomyces genome database (SGD)</td>
      <td>SGD:S000004369</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Saccharomyces cerevisiae)</td>
      <td>nth1</td>
      <td>Saccharomyces genome database (SGD)</td>
      <td>SGD:S000002408</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Saccharomyces cerevisiae)</td>
      <td>Prototrophic sigma1278b, MATa (WT)</td>
      <td>Isolate from Fink Lab.</td>
      <td>YBC16G1</td>
      <td>Wild-type strain.</td>
    </tr>
    <tr>
      <td>Strain, strain background (Saccharomyces cerevisiae)</td>
      <td>Δpck1</td>
      <td>This study</td>
      <td></td>
      <td>sigma1278b MAT a pck1::kanMX6</td>
    </tr>
    <tr>
      <td>Strain, strain background (Saccharomyces cerevisiae)</td>
      <td>Δfbp1</td>
      <td>This study</td>
      <td></td>
      <td>sigma1278b MAT a fbp1::kanMX6</td>
    </tr>
    <tr>
      <td>Strain, strain background (Saccharomyces cerevisiae)</td>
      <td>Δnth1</td>
      <td>Varahan et al., 2019</td>
      <td></td>
      <td>sigma1278b MAT a nth1::kanMX6</td>
    </tr>
    <tr>
      <td>Strain, strain background (Saccharomyces cerevisiae)</td>
      <td>WT (pTKL1-mCherry)</td>
      <td>Varahan et al., 2019</td>
      <td></td>
      <td>Wild-type strain with pentose phosphate pathway reporter plasmid (mCherry with TKL1 promoter)</td>
    </tr>
    <tr>
      <td>Strain, strain background (Saccharomyces cerevisiae)</td>
      <td>Δpck1 (pTKL1-mCherry)</td>
      <td>This study</td>
      <td></td>
      <td>Δpck1 strain with pentose phosphate pathway reporter plasmid (mCherry with TKL1 promoter)</td>
    </tr>
    <tr>
      <td>Strain, strain background (Saccharomyces cerevisiae)</td>
      <td>Δfbp1 (pTKL1-mCherry)</td>
      <td>This study</td>
      <td></td>
      <td>Δfbp1 strain with pentose phosphate pathway reporter plasmid (mCherry with TKL1 promoter)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pTKL1-mCherry</td>
      <td>Varahan et al., 2019</td>
      <td></td>
      <td>mCherry under the TKL1 promoter and CYC1 terminator. p417 centromeric plasmid backbone, G418R.</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Glucose (GO) Assay Kit</td>
      <td>Sigma Aldrich</td>
      <td>Cat. #: GAGO20-1KT</td>
      <td>Kit used for the biochemical measurement of trehalose from cells.</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>15N Aspartate</td>
      <td>Cambridge isotope laboratories</td>
      <td>Cat. #: NLM-718-PK</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>15N Ammonium sulphate</td>
      <td>Cambridge isotope laboratories</td>
      <td>Cat. #: NLM-713-PK</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>13C Aspartate</td>
      <td>Cambridge isotope laboratories</td>
      <td>Cat. #: CLM-1801-PK</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Yeast strains and growth media

The natural, prototrophic sigma 1278b strain of S. cerevisiae (referred to as wild-type or WT) was used in all experiments. Strains with gene deletions or chromosomally tagged proteins (at the C-terminus) were generated as described (Longtine et al., 1998). Strains used in this study are listed above. The growth medium used in this study is rich medium (1% yeast extract, 2% peptone and 2% glucose or 0.1% glucose).

### Colony spotting assay

All strains were grown overnight at 30 °C in either rich medium or defined minimal medium, as specified. 5 microliters of the overnight cultures were spotted on rich medium (low glucose) (1% yeast extract, 2% peptone, 0.1% glucose and 2% agar) or minimal medium (low glucose) (0.67% yeast nitrogen base with ammonium sulfate, without amino acids and 2% agar) supplemented with either all amino acids, all amino acids excluding aspartate or just aspartate at a concentration of 2 mM. Plates were incubated at 30 °C for 7 days unless mentioned otherwise.

### Colony imaging

For observing colony morphology, colonies were imaged using SZX-16 stereo microscope (Olympus) wherein the light source was above the colony. Bright-field imaging of 7 day old colonies were done using SZX-16 stereo microscope (Olympus) wherein the light source was below the colony. Epifluorescence microscopy imaging of 7 day old gluconeogenesis reporter colonies (pPCK1-mCherry), pentose phosphate pathway (PPP) reporter colonies (pTKL1-mCherry) and HXK1 reporter colonies (pHXK1-mCherry) were imaged using the red filter (excitation of 587 nm, emission of 610 nm) of SZX-16 stereo microscope (Olympus).

### Biochemical estimation of trehalose/glycogen levels

Trehalose and glycogen from yeast samples were quantified as described previously, with minor modifications (Gupta and Laxman, 2020). 10 OD600 of light cells and dark cells from 7 day old wild-type colonies (rich medium, 0.1% glucose) were collected. After re-suspension in water, 0.5 ml of cell suspension was transferred to four tubes (two tubes for glycogen assay and the other two tubes for trehalose assay). When sample collections were complete, cell samples (in 0.25 M sodium carbonate) were boiled at 95–98°C for 4 hr, and processed as described earlier (Gupta and Laxman, 2020) to estimate steady state trehalose amounts, based on glucose release. Assays were done using a 96-well plate format. Samples were added into each well with appropriate dilution within the dynamic range of the assay (20–80 µg/ml glucose). For the measurement of extracellular trehalose, a single wild-type colony (1 day to 7 day old colony) was re-suspended in 100 microliters of water and centrifuged at 20000 g for 5 min. The supernatant was collected and buffered to a pH of 5.4 (optimal for trehalase activity) using sodium acetate buffer (pH 5.0), and subsequently trehalose was estimated using the same protocol.

### Freeze-thaw survival assay

Light cells and dark cells were isolated from 7 day old wild-type colonies and washed twice with MilliQ water. Subsequently cells were resuspended in MilliQ water at an OD600 of 0.1. These were subjected to rapid freezing by plunging tubes into liquid nitrogen for five mins, followed by thawing at room temperature for five mins, for multiple cycles using protocols described earlier (Erkut et al., 2016). 5 µl from each of these samples were spotted onto rich medium plates (2% glucose). Cells were allowed to grow for 18 hr at 30 °C before imaging the plates and estimating survival using growth in a colony spot assay as the output.

### Desiccation tolerance assay

Desiccation tolerance assays were performed as described earlier (Erkut et al., 2016), with slight modifications. Briefly, light and dark cells were isolated from 7 day old wild-type colonies and brought to a final volume of 1 ml in PBS. Two hundred microliter aliquots were transferred to a 96- well tissue culture plate, centrifuged, and the excess water was removed. Cells were allowed to desiccate in a humid incubator at 27 °C for 7 days or 14 days. Samples were resuspended in diluted PBS to a final volume of 200 µl and plated for colony counting. The number of colony forming units per milliliter (cfu/ml) for each plate was measured, using an average from three independent controls. The relative viability of each experimental sample (done in biological triplicate) was determined by dividing the cfu/ml for that sample by the average cfu/ml of the control plates.

### Glucose foraging assay

Wild-type, ∆nth1 and ∆pck1 cells were grown overnight and 5 µl were spotted onto rich, low glucose medium. A small paper disc was soaked in 50% glucose solution overnight and placed at a distance of 2 cm from the colony spots. Colonies were allowed to develop at 30 °C for 7 days and were imaged. As a control, strains were spotted on a plate containing paper discs soaked in PBS.

### Metabolite extractions and measurements by LC-MS/MS

Light cells and dark cells isolated from wild-type colonies grown in different media were rapidly harvested and metabolites were extracted as described earlier (Walvekar et al., 2018). Metabolites were measured using LC-MS/MS method as described earlier (Walvekar et al., 2018). Standards were used for developing multiple reaction monitoring (MRM) methods on Sciex QTRAP 6500. Metabolites were separated using a Synergi 4µ Fusion-RP 80A column (100 × 4.6 mm, Phenomenex) on Agilent’s 1290 infinity series UHPLC system coupled to the mass spectrometer. For positive polarity mode, buffers used for separation were- buffer A: 99.9% H2O/0.1% formic acid and buffer B: 99.9% methanol/0.1% formic acid (Column temperature, 40°C; Flow rate, 0.4 ml/min; T = 0 min, 0% B; T = 3 min, 5% B; T = 10 min, 60% B; T = 11 min, 95% B; T = 14 min, 95% B; T = 15 min, 5% B; T = 16 min, 0% B; T = 21 min, stop). For negative polarity mode, buffers used for separation were- buffer A: 5 mM ammonium acetate in H2O and buffer B: 100% acetonitrile (Column temperature, 25°C; Flow rate: 0.4 ml/min; T = 0 min, 0% B; T = 3 min, 5% B; T = 10 min, 60% B; T = 11 min, 95% B; T = 14 min, 95% B; T = 15 min, 5% B; T = 16 min, 0% B; T = 21 min, stop). The area under each peak was calculated using AB SCIEX MultiQuant software 3.0.1.

### 15N- and 13C- based metabolite labelling experiments

For detecting 15N label incorporation in nucleotides, 15N Ammonium sulfate (Sigma-Aldrich) and 15N Aspartate (Cambridge Isotope Laboratories) with all nitrogen atoms labeled were used. For 13C-labeling experiment, 13C aspartate with all carbon atoms labeled (Cambridge Isotope Laboratories) was used. All the parent/product masses measured are enlisted in Table 1. For all the nucleotide measurements, release of the nitrogen base was monitored in positive polarity mode. For all sugar phosphates, the phosphate release was monitored in negative polarity mode. The HPLC and MS/MS protocol was similar to those explained above.

**Table 1.**
 Mass transitions used for LC-MS/MS experiments.


<table>
  <tbody>
    <tr>
      <td>Nucleotides</td>
      <td>Formula</td>
      <td>Parent/Product (positive polarity)</td>
      <td>Comment (for 15N experiment)</td>
    </tr>
    <tr>
      <td>AMP</td>
      <td>C10H14N5O7P</td>
      <td>348/136</td>
      <td>Product has all N</td>
    </tr>
    <tr>
      <td>15N_AMP_1</td>
      <td></td>
      <td>349/137</td>
      <td></td>
    </tr>
    <tr>
      <td>15N_AMP_2</td>
      <td></td>
      <td>350/138</td>
      <td></td>
    </tr>
    <tr>
      <td>15N_AMP_3</td>
      <td></td>
      <td>351/139</td>
      <td></td>
    </tr>
    <tr>
      <td>15N_AMP_4</td>
      <td></td>
      <td>352/140</td>
      <td></td>
    </tr>
    <tr>
      <td>15N_AMP_5</td>
      <td></td>
      <td>353/141</td>
      <td></td>
    </tr>
    <tr>
      <td>GMP</td>
      <td>C10H14N5O8P</td>
      <td>364/152</td>
      <td>Product has all N</td>
    </tr>
    <tr>
      <td>15N_GMP_1</td>
      <td></td>
      <td>365/153</td>
      <td></td>
    </tr>
    <tr>
      <td>15N_GMP_2</td>
      <td></td>
      <td>366/154</td>
      <td></td>
    </tr>
    <tr>
      <td>15N_GMP_3</td>
      <td></td>
      <td>367/155</td>
      <td></td>
    </tr>
    <tr>
      <td>15N_GMP_4</td>
      <td></td>
      <td>368/156</td>
      <td></td>
    </tr>
    <tr>
      <td>15N_GMP_5</td>
      <td></td>
      <td>369/157</td>
      <td></td>
    </tr>
    <tr>
      <td>CMP</td>
      <td>C9H14N3O8P</td>
      <td>324/112</td>
      <td>Product has all N</td>
    </tr>
    <tr>
      <td>15N_CMP_1</td>
      <td></td>
      <td>325/113</td>
      <td></td>
    </tr>
    <tr>
      <td>15N_CMP_2</td>
      <td></td>
      <td>326/114</td>
      <td></td>
    </tr>
    <tr>
      <td>15N_CMP_3</td>
      <td></td>
      <td>327/115</td>
      <td></td>
    </tr>
    <tr>
      <td>UMP</td>
      <td>C9H13N2O9P</td>
      <td>325/113</td>
      <td>Product has all N</td>
    </tr>
    <tr>
      <td>15N_UMP_1</td>
      <td></td>
      <td>326/114</td>
      <td></td>
    </tr>
    <tr>
      <td>15N_UMP_2</td>
      <td></td>
      <td>327/115</td>
      <td></td>
    </tr>
    <tr>
      <td>Trehalose and sugar phosphates</td>
      <td>Formula</td>
      <td>Parent/Product (negative polarity)</td>
      <td>Comment (for 13C experiment)</td>
    </tr>
    <tr>
      <td>Trehalose</td>
      <td>C12H22O11</td>
      <td>341.3/179.3</td>
      <td></td>
    </tr>
    <tr>
      <td>13C_Trehalose_12</td>
      <td></td>
      <td>353.3/185.3</td>
      <td>Product has 6 C all of which are labeled</td>
    </tr>
    <tr>
      <td>13C_3 PG_3</td>
      <td></td>
      <td>188/97</td>
      <td></td>
    </tr>
    <tr>
      <td>G6P</td>
      <td>C6H13O9P</td>
      <td>259/97</td>
      <td>Monitoring the phosphate release</td>
    </tr>
    <tr>
      <td>13C_G6P_6</td>
      <td></td>
      <td>265/97</td>
      <td></td>
    </tr>
    <tr>
      <td>6 PG</td>
      <td>C6H13O10P</td>
      <td>275/97</td>
      <td>Monitoring the phosphate release</td>
    </tr>
  </tbody>
</table>

### Model methods and parameters

#### Model construction

We extend the coarse-grained model from our previous study (Varahan et al., 2019) to include the idea that both dark and light cells need to accumulate enough N and C for cell division. Once again, the model consists of a population of dark and light ‘cell blocks’ on a 2D grid. Additionally, we track the spatiotemporal levels of extracellular trehalose on this grid as it is secreted, consumed and diffuses. We do not track the levels of aspartate as it is assumed to be a non-limiting resource.

#### Initial conditions of the model

We start with an approximately circular colony 20 grid lengths in radius at the center of our grid. 95–99% of the 1257 cell blocks are in the dark state. There is no extracellular trehalose on the grid at the start.

#### Model implementation

Running the model is almost identical to the implementation in Varahan et al., 2019, except for a few extra steps, refinements, and parameters to consider. For clarity, we will outline the entire algorithm here using default parameter values. The following steps are to be carried out in each time step after colony initialization.

The above algorithm and default parameter values simulate a wild type colony as seen in Figure 3A. For variations of the two main parameters, f and AspU, refer to Figure 3B & C and for a more detailed picture, refer to Figure 3—figure supplement 3. The set of parameters used in the model is shown in Table 2 and for a flowchart of the algorithm, refer to Figure 3—figure supplement 5.

**Table 2.**
 Model parameters.


<table>
  <tbody>
    <tr>
      <td>Main parameters</td>
      <td>Notation</td>
      <td>Default Value</td>
      <td>Range of Variation</td>
    </tr>
    <tr>
      <td>Fraction of aspartate flux allocated to N in dark cell blocks</td>
      <td>f</td>
      <td>0.125</td>
      <td>0.0–1.0 (0–100%)</td>
    </tr>
    <tr>
      <td>Relative rate of aspartate uptake compared to trehalose uptake rate</td>
      <td>AspU</td>
      <td>4.0</td>
      <td>1.0–8.0</td>
    </tr>
    <tr>
      <td>Additional parameters</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Yield (converting N to C)</td>
      <td>Y</td>
      <td>0.31 C/N</td>
      <td></td>
    </tr>
    <tr>
      <td>Fraction secreted as trehalose, per dark cell block</td>
      <td>Pf</td>
      <td>0.049/Time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Max secreted trehalose, per dark cell block</td>
      <td>--</td>
      <td>0.12 units/Time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Extra N for light cells</td>
      <td>ExN</td>
      <td>4.0</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Aspartate consumed by dark and light cell blocks</td>
      <td>AspU*Cmax</td>
      <td>0.2/Time</td>
      <td></td>
    </tr>
    <tr>
      <td>Parameters from previous model</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Growth rate (light and dark cell block)</td>
      <td>g</td>
      <td>0.04/Time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Max trehalose consumed by a light cell block</td>
      <td>Cmax</td>
      <td>0.05 units/Time</td>
      <td></td>
    </tr>
    <tr>
      <td>Switching threshold (dark to light)</td>
      <td>TDL</td>
      <td>1.5 units</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Switching probability (dark to light)</td>
      <td>PDL</td>
      <td>0.5/Time</td>
      <td></td>
    </tr>
    <tr>
      <td>Switching threshold (light to dark)</td>
      <td>TLD</td>
      <td>0.0001 units</td>
      <td></td>
    </tr>
    <tr>
      <td>Switching probability (light to dark)</td>
      <td>PLD</td>
      <td>0.0001/Time</td>
      <td></td>
    </tr>
    <tr>
      <td>Scaled diffusion constant of trehalose</td>
      <td>Deff</td>
      <td>0.24 L2/Time</td>
      <td></td>
    </tr>
  </tbody>
</table>

#### Model parameters

The new parameters introduced in the current model are chosen to reliably reproduce patterns similar to the experimental WT colony (both the final form, as well as at different stages of its growth). Our purpose here is simply to show that this model is sufficient to produce spatial patterns similar to what we observe experimentally, not to do a detailed fitting of parameter values to data. However we outline the biological reasoning behind some of the choices below:

### Code availability

We implemented the model using Python and Jupyter Notebooks. The code used in this study is available at: https://github.com/vaibhhav/metabplastic (Varahan, 2020; copy archived at https://github.com/elifesciences-publications/metabplastic).

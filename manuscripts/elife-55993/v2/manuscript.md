# Combining agent-based, trait-based and demographic approaches to model coral-community dynamics

## Authors

- Bruno Sylvain Carturan<sup>1</sup> ([ORCID: 0000-0001-6811-1063](https://orcid.org/0000-0001-6811-1063)) †
- Jason Pither<sup>1</sup> ([ORCID: 0000-0002-7490-6839](https://orcid.org/0000-0002-7490-6839)) †
- Jean-Philippe Maréchal<sup>4</sup> ([ORCID: 0000-0002-9413-5242](https://orcid.org/0000-0002-9413-5242))
- Corey JA Bradshaw<sup>5</sup> ([ORCID: 0000-0002-5328-7741](https://orcid.org/0000-0002-5328-7741))
- Lael Parrott<sup>1</sup> †

### Affiliations

1. Department of Biology, University of British Columbia Kelowna Canada
2. Institute for Biodiversity, Resilience, and Ecosystem Services, University of British Columbia Kelowna Canada
3. Department of Earth, Environmental and Geographic Sciences, University of British Columbia Kelowna Canada
4. Nova Blue Environment Schoelcher France
5. Global Ecology, College of Science and Engineering, Flinders University Adelaide Australia

† Corresponding author

## Abstract

The complexity of coral-reef ecosystems makes it challenging to predict their dynamics and resilience under future disturbance regimes. Models for coral-reef dynamics do not adequately account for the high functional diversity exhibited by corals. Models that are ecologically and mechanistically detailed are therefore required to simulate the ecological processes driving coral reef dynamics. Here, we describe a novel model that includes processes at different spatial scales, and the contribution of species’ functional diversity to benthic-community dynamics. We calibrated and validated the model to reproduce observed dynamics using empirical data from Caribbean reefs. The model exhibits realistic community dynamics, and individual population dynamics are ecologically plausible. A global sensitivity analysis revealed that the number of larvae produced locally, and interaction-induced reductions in growth rate are the parameters with the largest influence on community dynamics. The model provides a platform for virtual experiments to explore diversity-functioning relationships in coral reefs.

## Introduction

Corals are the foundation species of coral-reef ecosystems and provide essential ecological functions for ecosystem resilience, as well as services to millions of people worldwide (Moberg and Folke, 1999; Woodhead et al., 2019). The loss of coral cover and the change in species composition occurring in communities around the globe (Hughes et al., 2018; Torda et al., 2018) therefore alter the functioning of the entire ecosystem. For instance, the replacement of morphologically complex, but highly sensitive species, by simpler and more resilient species reduces the overall architectural complexity of reef habitats (Alvarez-Filip et al., 2009)—this flattening reduces the diversity and abundance of fish (Darling et al., 2017; Newman et al., 2015) and macroinvertebrates (Nelson et al., 2016) and the functions they provide (e.g. grazing, bioerosion) (Pratchett et al., 2018).

Disentangling the identity effect (effects of individual species on processes) from the diversity effect (shared effects of a collection of species on processes) is necessary to define which species, functional groups, or aspects of diversity are essential for maintaining ecological processes (Bellwood et al., 2019; Brandl et al., 2019). While the effect of such essential species on ecosystem functions and the consequences of their loss has been widely reported (e.g. Hughes, 1994; Alvarez-Filip et al., 2009; Hoey and Bellwood, 2009), the relationship between species richness or functional diversity and ecosystem functioning is still poorly understood. Diversity is hypothesized to enhance functioning because of niche complementarity and facilitation (Bulleri et al., 2016; Loreau, 2000), but tests of this hypothesis with corals are scarce (but see McWilliam et al., 2018a).

Even less understood is the effect of diversity on the temporal variability (i.e. stability) and resilience (i.e. resistance and recovery) of community-level aggregate properties such as biomass, percentage cover, and calcification rate (Griffin et al., 2009). Higher diversity is hypothesized to promote ecosystem stability and resilience via asynchronous, independent population dynamics and compensatory population dynamics resulting from functional redundancy and response diversity—the latter is the insurance hypothesis (reviewed in Griffin et al., 2009 and McCann, 2000). Tests of the insurance hypothesis are rare for coral reefs (but see Mellin et al., 2014 and Nash et al., 2016 for fish, and Zhang et al., 2014 and Clements and Hay, 2019 for coral diversity).

Predicting how the reassembly of coral species in reefs alters ecosystem functioning is therefore a research priority to inform conservation management (Bellwood et al., 2019; Graham et al., 2014). To do this requires identifying the main ecosystem processes and associated functional traits affecting coral dynamics, and quantifying the relationship between the two (Bellwood et al., 2019; Carturan et al., 2018). Both virtual and physical experiments are also required (Brandl et al., 2019; Mcleod et al., 2019), where different aspects of diversity such as species and functional richness, and external factors such as disturbance regimes, larval connectivity, and grazing, are varied independently from one another to determine how they influence these dynamics. Unfortunately, physical experiments with coral species are unwieldy because of their slow growth rates and challenging environment in which they exist. However, models use simulation to overcome these challenges. To simulate the effect of species and functional diversity on ecosystem functioning realistically, models should include: (i) links between functional traits and processes; (ii) biotic interactions such as spatial competition, and (iii) population dynamics representing demographic structure. Although some coral models have been developed (reviewed in Kubicek and Borell, 2011; Weijerman et al., 2015), most implement only one or two of these aspects at most, and often with limited ecological detail. Importantly, no models have yet been developed to represent the breadth of species richness and functional diversity found in coral reefs in different regions of the world.

Trait-based approaches (eventually combined with demographic approaches) have been used in conceptual, statistical, equation-based, and agent-based models to address diverse theoretical and practical questions (Zakharova et al., 2019). Agent-based approaches are particularly suited to simulate coral-community dynamics as a function of diversity, functional traits and demography because (i) spatial processes can easily be implemented explicitly, (ii) it is possible to describe the functional (by implementing effect, resistance, and recovery traits) and demographic (by implementing age or size-related fecundity and survival effects on ecosystem functions) characteristics of each individual in the community, and (iii) they are flexible and adaptable frameworks that can implement different types of submodels (e.g. statistical, equation-based, or algorithmic), which can be evaluated separately (DeAngelis and Grimm, 2014; Grimm et al., 2005; Grimm and Railsback, 2005). Agent-based models have been criticized for being complex, and difficult to parameterize, analyze and communicate. However, empirical, trait-based approaches and traits databases have become more prevalent, facilitating model parameterization. Additionally, standardized protocols—such as the Overview, Design concepts and Details (ODD) protocol and hierarchically structured validation—are now well-defined to help communicate and validate agent-based models (Grimm et al., 2020; Grimm et al., 2006; Kubicek et al., 2015).

We present a new, spatially explicit, agent-based model representing benthic communities in tropical reefs composed of coral species and six functional groups of algae. Individual colonies grow, reproduce, compete for space, and respond to disturbances as a function of their size and trait-process relationships, which we defined using 11 functional traits (Table 1) informed by published empirical data (Figure 1, Figure 2). The number of coral species present in the community can be varied without impacting model complexity and processing time. Functional diversity can be varied by sampling species from a set of 798 functionally realistic species, which we obtained by imputing missing trait data based on values measured for real species (Madin et al., 2016a). Importantly, we used empirical data and previously established models to implement most of the processes represented in the model (Table 2). Our aim is to provide the full description of our model’s design, concepts, and capabilities. In the main text, we present a streamlined description, and use the Appendices for details regarding: (1) traits and imputation of missing data (Appendix 1), (2) the Overview, Design concepts and Details protocol (Appendices 2 and 4), (3) calibration with empirical data (Appendix 3), (4) hierarchically structured validation (Appendix 5), and (5) global sensitivity analysis (Appendix 6). For complete transparency and reproducibility, the model, the R scripts and instructions are available on the Open Science Framework (OSF) (Carturan et al., 2020).

![Figure 1.](https://cdn.elifesciences.org/articles/55993/elife-55993-fig1-v2.jpg)

**Figure 1.:** Six different variables as model inputs determine (i) initial community composition, (ii) number of larvae coming from the regional pool (total number divided among different species, with annual supply for spawning species, and biannual supply for brooding species), (iii) thermal stress in degree-heating weeks, (iv) hydrodynamic regime intensity expressed as dislodgment mechanical threshold (unitless), (v) sedimentation, and (vi) the percentage of reef grazed. All variables are inputs at every time period except for the initial community composition that is determined during initialization. The model represents a 25 m2 coral reef community and is composed of 1 cm2 cell agents. Once every time step, living agents (algae and corals) grow by converting their neighbouring agents within a certain radius (white arrows in middle panel). Different processes affect the community at different spatial scales. For instance, the grazing process lasts until the imposed percentage cover grazed over the entire reef is reached. In contrast, coral colonies are individually considered for dislodgment during hydrodynamic disturbance and a single agent is potentially converted into a new coral recruit when larvae settle successfully. Radar charts represent the functional characteristics of coral species (defined by a specific colour): each vertex corresponds to a functional trait and the coloured polygon indicates the trait values of the species (higher values are farther away from the centre of the web). At the end of each time step, the model provides the percentage cover, the number of coral recruits, and the size of each colony for every taxon, and optionally, the reef rugosity created by coral colonies (bottom panel). The benthic community at the largest scale is a screenshot of the model output.

![Figure 2.](https://cdn.elifesciences.org/articles/55993/elife-55993-fig2-v2.jpg)

**Figure 2.:** Large white arrows define the ordering of processes and black arrows show the direction of data transfer; dashed black arrows are optional processes (not activated for the analyses we present here). The order of occurrence of coral reproduction, bleaching, and colony dislodgement and fragmentation is imposed to simulate recruitment failure due to the occurrence of a disturbance prior to reproduction. The intensity of waves and cyclones is expressed as a dimensionless dislodgment mechanical threshold; thermal stress is expressed in degree-heating weeks.

**Table 1.**
 The 11 functional traits we used to implement ecological processes in the model.


<table>
  <thead>
    <tr>
      <th>Traits</th>
      <th>Related processes and details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Age at maturity (yr)</td>
      <td>The minimum age required for a coral colony to reproduce (Appendix 2: §7.2.1.1.a)</td>
    </tr>
    <tr>
      <td>Aggressiveness (0 to 100)</td>
      <td>Spatial direct competition for space between coral species; the trait is only used for species not considered in the Precoda et al., 2017 study on probability of species-pair interactions (Appendix 1: §1.2)</td>
    </tr>
    <tr>
      <td>Colony max diameter (cm)</td>
      <td>Initial colony size distributions (Appendix 2: §5.2.2); colony fecundity (for the species with small colonies; Appendix 2: §7.2.1.1.b); bleaching (Appendix 2: §7.4.2.1; Appendix 4); colony vegetative growth (to define maximum planar area; Appendix 2: §7.5.1)</td>
    </tr>
    <tr>
      <td>Corallite area (cm2)</td>
      <td>Colony fecundity (Appendix 2: §7.2.1.1.b); bleaching (Appendix 2: §7.4.2.1; Appendix 4)</td>
    </tr>
    <tr>
      <td>Egg diameter (mm)</td>
      <td>Time to motility of coral larvae (§7.2.1.1.d)</td>
    </tr>
    <tr>
      <td>Polyp fecundity</td>
      <td>Colony fecundity (Appendix 2: §7.2.1.1.b)</td>
    </tr>
    <tr>
      <td>Growth form</td>
      <td>Formation of reef rugosity (Appendix 2: §7.1.2.2); colony fecundity (Appendix 2: §7.2.1.1.b); dislodgement (Appendix 2: §7.3.1.2); spatial competition (overtopping; Appendix 2: §7.5)</td>
    </tr>
    <tr>
      <td>Growth rate (mm.yr−1)</td>
      <td>Bleaching (Appendix 2: §7.4.2.1; Appendix 4); vegetative growth (Appendix 2: §7.5.1)</td>
    </tr>
    <tr>
      <td>Mode of larval development</td>
      <td>Coral reproduction (Appendix 2: §7.2.1.1.a)</td>
    </tr>
    <tr>
      <td>Microscopic reduced scattering coefficient (µS,m, mm−1)</td>
      <td>Bleaching (Appendix 2: §7.4.2.1; Appendix 4)</td>
    </tr>
    <tr>
      <td>Sexual system</td>
      <td>Colony fecundity (Appendix 2: §7.2.1.1.b)</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Empirical data and models we used to implement ecological processes in the model.


<table>
  <thead>
    <tr>
      <th>Processes/variables</th>
      <th>Comments</th>
      <th>References</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Colony size (initialization)</td>
      <td>We used colony size distributions measured for eleven species and maximum colony diameter to define colony size distributions for each species (Appendix 2: §5.2.2)</td>
      <td>E. H. Meesters and R. P. M. Bak, personal communication, May 2017</td>
    </tr>
    <tr>
      <td>Herbivorous fish density supported by the reef rugosity</td>
      <td>We used an empirical model to determine the density of herbivore fish present in the reef as a function of reef rugosity (Appendix 2: §7.1.2.2)</td>
      <td>Bozec et al., 2013</td>
    </tr>
    <tr>
      <td>Grazing intensity due to herbivorous fish density</td>
      <td>We defined a model using empirical data to determine the surface of the reef grazed as a function of herbivorous fish density (Appendix 2: §7.1.2.2)</td>
      <td>Williams and Polunin, 2001</td>
    </tr>
    <tr>
      <td>Polyp maturity in colonies</td>
      <td>We defined a model from models established empirically to determine the proportion of mature polyps in a colony as a function of colony planar area using data for eight species (Appendix 2: §7.2.1.1.b)</td>
      <td>Álvarez-Noriega et al., 2016</td>
    </tr>
    <tr>
      <td>Larval competency</td>
      <td>We used a model established empirically to determine time to motility of coral larvae as a function of egg diameter (Appendix 2: §7.2.1.1.d)</td>
      <td>Figueiredo et al., 2013</td>
    </tr>
    <tr>
      <td>Larval retention</td>
      <td>We used models established empirically to determine the proportion of competent larvae remaining in the reef as a function of time to motility and water retention time (Appendix 2: §7.2.1.1.d)</td>
      <td>Figueiredo et al., 2013</td>
    </tr>
    <tr>
      <td>Larval competency loss</td>
      <td>We defined a model from models established empirically to determine the proportion of external competent larvae settling on the focal reef as a function of the distance travelled (Appendix 2: §7.2.1.2.b)</td>
      <td>Connolly and Baird, 2010</td>
    </tr>
    <tr>
      <td>Larval post-settlement survival</td>
      <td>We defined a model using empirical data to determine the proportion of surviving settled larvae as a function of time (Appendix 2: §7.2.1.3.b)</td>
      <td>Ritson-Williams et al., 2016</td>
    </tr>
    <tr>
      <td>Colony dislodgement</td>
      <td>We used models established empirically to determine if a colony is dislodged as a function of colony growth form, planar area and the intensity of the hydrodynamic disturbance (Appendix 2: §7.3.1.2.a)</td>
      <td>Madin and Connolly, 2006</td>
    </tr>
    <tr>
      <td>Survival of dislodged branching colonies</td>
      <td>We defined a model using a model established empirically to determine the proportion of a dislodged branching colony that survives dislodgement (Appendix 2: §7.3.1.2.b)</td>
      <td>Highsmith et al., 1980</td>
    </tr>
    <tr>
      <td>Coral bleaching</td>
      <td>We used the empirically established bleaching-response index to determine species bleaching susceptibility from functional traits (Appendix 2: §7.4.2; Appendix 4)</td>
      <td>Swain et al., 2016b</td>
    </tr>
    <tr>
      <td>Coral competition</td>
      <td>We used species-pair probabilities of interaction outcomes established from mix-effect models and a review of empirical data (Appendix 2: §7.5.2.2.a)</td>
      <td>Precoda et al., 2017</td>
    </tr>
    <tr>
      <td>Coral-algae competition</td>
      <td>We defined probabilities of interaction outcomes using proportions of interaction won and lost between coral species and the different functional group of algae implemented measured experimentally (Appendix 2: §7.5.3)</td>
      <td>Brown et al. (2017) and K. T. Brown, personal communication, October 2017</td>
    </tr>
  </tbody>
</table>

## Materials and methods

### Sources and software

We collected coral-trait data from coraltraits.org (Madin et al., 2016a) and other resources from the peer-reviewed literature (Appendix 1). We systematically verified and corrected coral-species nomenclature using the World Register of Marine Species as a reference. We used R (version 3.5.0, R Development Core Team, 2017) to manipulate datasets, for statistical analyses, and to manage model simulations. We developed the model with the open-source, Java object-oriented programming language Repast Simphony 2.5.0 (North et al., 2013). We launched simulations using the R package rrepast 0.7.0 (García and Rodríguez-Patón, 2016) and rJava 0.9–10 (Urbanek, 2018). We used the R package missForest 1.4 (Stekhoven and Bühlmann, 2012) to impute missing trait data. We included phylogenetic information as a predictor using Huang and Roy (2015) phylogenetic supertrees to improve predictions; we manipulated the supertrees using the R packages ape 5.0 (Paradis and Schliep, 2019) and phytools 0.5–38 (Revell, 2012) (Appendix 1). We defined coral bleaching probabilities using the R packages MuMIn 1.40.0 (Bartón, 2017), betareg 3.1–0 (Cribari-Neto and Zeileis, 2010), lme4 1.1–15 (Bates et al., 2015), and lmtest 0.9–35 (Zeileis and Hothorn, 2002) (Appendix 4). For the global sensitivity analysis, we drew a Latin hypercube sample from the parameter space using the randomLHS function from the R package lhs 0.16 (Carnell, 2018), and we measured the influence of parameters on different response variables by fitting boosted regression trees using the gbm.step function from the R package dismo 1.1–4 (Hijmans et al., 2017).

### Model description

We provide here a brief description of the model following the Overview, Design concepts, and Details protocol (Grimm et al., 2020; Grimm et al., 2010; Grimm et al., 2006). A complete protocol that contains all the details about parameterization and process implementation along with a review of the supporting literature is available in Appendices 2 and 4.

#### Purpose and patterns

The purpose of the model is to predict coral population dynamics as a function of hydrodynamic (i.e. waves and cyclones) and thermal disturbances, grazing pressure, larval connectivity, sedimentation (i.e. sand import and export), interspecific competitive interactions, and benthic community diversity (species richness and functional diversity). Time series defining disturbance regimes, sand cover and the diversity and number of external coral larvae are imposed and need to be defined before launching simulations. The grazing regime is imposed but can also be determined by activating the feedback process linking reef rugosity (created by colonies) to herbivore fish density to grazing pressure. Patterns in species cover, colony size distributions, recruitment rates and rugosity are used to understand the model’s dynamics and its accuracy.

#### Entities, state variables, and scales

The model consists of grid-cell agents each representing 1 cm2, so that the benthic community is represented at a scale of organization smaller than the colony (equivalent to that of a polyp, although polyp size varies among species by several orders of magnitude) (Figure 1). During a simulation, an agent can be temporally part of a coral colony (798 species), a patch of algae (i.e. macroalgae, allopathic macroalgae, Halimeda spp., turf, articulated coralline algae or crustose coralline algae), sand, or bare substratum. Each agent is characterized by 33 variables that describe where the agent is in space (its position is fixed), its species identity (i.e. one of the 798 coral species or six functional groups of algae) and related functional characteristics, its age, the colony’s planar area and identification number, if it is bleached or was grazed recently, et cetera (Appendix 2—table 1). Coral colonies and patches of algae are entities composed of multiple agents sharing the same variable values (except for their spatial coordinates) and changing their state simultaneously during certain processes. For instance, dislodgement is simulated by converting all the agents forming the dislodged colony into barren ground; a turf algae overgrowing a colony is simulated by converting the coral agents constituting the overgrown part into turf, but conserving the information about the colony (i.e. identification number, size, species, growth form).

The size of the reef and the length of a time step are changeable. We defined a 25 m2 reef for our simulations (i.e. 250,000 agents), which is usually the scale at which benthic communities are assessed in detail (e.g. Holbrook et al., 2018; Torda et al., 2018). We defined a 6-month time step because the empirical data we used to calibrate the model were collected biannually. We acknowledge that six months is a coarse time step, potentially preventing the simulation of subtle dynamics, for instance changes triggered by mild disturbances. We opted for this time step considering that (i) corals grow slowly (<180 mm yr−1), and (ii) their reproductive cycles, and (iii) thermal and hydrodynamic disturbance regimes are seasonal. It is, however, possible to define shorter periods (i.e., 3- and 4-month time steps) as time steps in the model.

The model estimates three-dimensional colony surface areas using geometric formulae (Appendix 2—table 5) to determine the number of larvae produced in each colony (Appendix 2: §7.2.1.1), and (optionally) the rugosity of the reef (Appendix 2: §7.1.2.2). The model also accounts for colony and algae heights in overtopping processes (Appendix 2: §7.5.2.2 and §7.5.3.2). Algae have constant heights and colony heights equal to the radius of the colony planar area, assuming the latter is circular (Appendix 2—table 18).

#### Process overview and scheduling

Each time step includes the following consecutive processes: (i) grazing—patches of agents are randomly selected and grazed until a certain proportion of the reef is reached, (ii) coral reproduction—locally and regionally produced larvae attempt to settle, (iii) thermal disturbance, which, if triggered, eventually causes colonies to bleach and/or die; (iv) dislodgement and fragmentation—the effect of waves and cyclones on certain colonies, (v) growth—each living agent, selected in a random order, attempts to convert its neighbouring agents within a certain radius to its own state, (vi) sedimentation—barren ground agents are converted to sand and vice versa until the desired sand cover is reached, (vii) algae invasion—the remaining ungrazed, barren-ground agents are converted into algae agents (Figure 2) (note that the process differs from species invasion). The order at which processes iii, iv, and v happen must be defined beforehand.

During each time step, the model exports response variables: the cover of each benthic group (coral, algae, and sand), the planar area of each colony present per species, the number of recruited coral larvae m−2 species−1, and the reef rugosity (in cases when rugosity-grazing feedback is activated). The first two variables are collected after processes iii, iv, and vii, and the third and fourth variable after process vii. There are six variables imported each time step; their values respectively determine the cover to be grazed, the intensity of waves or cyclone, and of thermal stress, the number of external larvae m−2 entering the reef, the order that reproduction, bleaching, and wave or cyclone events happen, and the cover of sand to be achieved. We present a complete schedule that includes additional model-related processes in Appendix 2: §3.

#### Design concepts

Basic principles: the model combines agent-based, trait-based, and demographic approaches to simulate coral reef community dynamics in imposed environmental scenarios. The model captures fundamental principles in ecology: (i) biodiversity influences ecosystem resilience and (ii) functioning, (iii) disturbance regimes filter species and mediate interspecific competition, (iv) interspecific functional differences (or strategies) mediate competitive exclusion and coexistence, and (v) source-sink dynamics regulate species coexistence in metacommunities.

Emergence: The dynamics of the benthic community emerge from species traits and the imposed disturbance regime (waves, cyclone, thermal stress), larval connectivity, sedimentation, and grazing pressure intensity (which can also emerge from reef rugosity). Cell agents do not make decisions and their behavior results from imposed deterministic or probabilistic rules.

Interactions: Agents on the edge of coral colonies and patches of algae interact with one another when competing for space. The outcome of a coral-coral interaction is determined by its specific pairwise outcome probabilities—the probability of coral-algae interactions are the same for all coral species, and algae-algae interactions result in a stand-off except when competing against crustose coralline algae. Branching and plating species also have the capacity to overtop other colonies and algae depending on their size (Appendix 2: §7.5).

Stochasticity: The model draws success or failure outcomes each time a patch of algae is grazed, a larva attempts to settle and survive the first 6 months, an agent tries to convert another living agent (Appendix 2: §7.1, 7.2, 7.5), and a colony is thermally stressed (i.e. bleaching and bleaching-induced mortality; Appendix 2: §7.4). Each of these random events is based on a probability of success specific to the process and the species involved. During initialization, colonies are created and placed randomly in space; their sizes are drawn from right-skewed frequency distributions (Appendix 2: §5.1). Finally, grazing and larval settlement happen randomly in space.

Collectives: Collective behaviour of agents happens when a colony is (i) dislodged—agents sharing the same colony (i.e. coral and algae agents growing on a colony) are converted to barren ground (Appendix 2: §7.3), (ii) bleaches or dies—the coral agents of the colony are converted to a bleached or dead state, respectively (Appendix 4: §7.1, 7.2), or (iii) reproduces—the number of larvae or gametes produces by a colony depends on certain coral traits and the size and age of the colony (Appendix 2: §7.2).

Observation: Four types of data are collected during a simulation: (i) percentage cover of each taxon, (ii) number of recruits for each coral species m−2, (iii) planar area of each colony species−1, and (iv) optionally, the rugosity created by the coral colonies (Figure 2).

#### Initialization

The initial composition of the benthic community (i.e. the cover of coral species, algae, barren ground, and sand) is defined by the user and is imported from a comma-delimited text file. The space is filled first by creating circular coral colonies randomly in space. The colony diameters are drawn from skewed distributions that we defined using empirical data (E. H. Meesters and R. P. M. Bak, personal communication, May 2017) and as a function of the trait colony maximum diameter. Circular patches of algae (314 cm2) are then created and the remaining agents are converted into barren ground and sand (Appendix 2: §5).

#### Input data

Predefined time series (recorded in the text files) of input data are used to define the environmental context of the reef (Figure 2). At each time step, the model imports values for the corresponding period of the (i) surface grazed (%), (ii) number of external larvae settling, (iii) intensity of waves of cyclones (in dislodgement mechanical threshold, a dimensionless measure of the mechanical threshold imposed by waves and cyclones), (vi) thermal stress intensity (in degree-heating weeks), and (v) sand cover (%).

#### Submodels

##### Grazing

The reef is grazed by randomly selecting circular patches of agents (29 cm2) until a certain percentage cover is reached. The cover to reach can be either exclusively imposed (imported from a file) or it can result from the rugosity that coral colonies create if the rugosity-grazing feedback process is activated. We used the empirically established Bozec et al. (2013) model to determine herbivorous fish density from reef rugosity and data from Williams and Polunin (2001) to estimate grazing pressure from herbivorous fish density (Appendix 2: §7.1).

##### Reproduction and recruitment

Coral larvae locally produced and arriving from the regional pool attempt to settle in the reef at a random location. The number of larvae produced locally for each species depends on species traits (i.e. polyp fecundity, corallite area, growth form, sexual system)—we used geometric formulae from McWilliam et al. (2018b) to calculate colony surface area from planar area—and the distribution of colony planar areas in their population—we used models from Álvarez-Noriega et al. (2016) to determine the proportion of fecund polyps in colonies as a function of planar area. We used models from Figueiredo et al. (2013) to determine the proportion of spawned eggs remaining in the reef from water retention time and egg diameter—species producing larger eggs also produce larvae having a greater time to motility and a higher chance of being exported outside the reef. Species with a brooding mode of larval development release larvae ready to settle and are not affected by water retention time (Appendix 2: §7.2.1.1). The number of external larvae arriving at the reef can either be defined beforehand and imported from a file, or is calculated as a function of the connectivity imposed—we used the models of Connolly and Baird (2010) to determine the proportion of alive and competent larvae as a function of distance travelled (Appendix 2: §7.2.1.2). Larvae have a chance of settling successfully on barren ground, crustose coralline algae, and dead coral agents. We used data from Ritson-Williams et al. (2016) to define the proportion of settled larvae surviving the duration represented by a time step (Appendix 2: §7.2.1.3). Algae recruit at the end of a time step by filling up the remaining available space (i.e. ungrazed barren ground and dead coral agents) (Appendix 2: §7.2.2).

##### Wave and cyclone damage

We modelled colony dislodgment using colony shape factor from Madin and Connolly (2006), which is compared for each colony to the intensity of the disturbance (expressed as dislodgement mechanical threshold). We implemented branching-colony fragmentation by modifying the relationship between fragment size and survival established by Highsmith et al. (1980). We defined our own models to simulate the effect on the algae community because no relationships have been established empirically (Appendix 2: §7.3).

##### Bleaching

We first defined a species-specific index of bleaching susceptibility using bleaching-resistance traits and the bleaching response index from Swain et al. (2016b). We then used this index to establish species-specific logistic bleaching responses as a function of the intensity of the thermal stress (in degree heating-week) using data from Eakin et al. (2010). Finally, we defined a bleaching-induced mortality logistic-response model (Appendix 2: §7.4; Appendix 4).

##### Growth and spatial competition

Coral and algae agents on the edge of their colony or patch attempt to convert neighbouring agents within a certain radius. The size of the radius depends on the species growth rate and the state of the neighbouring agents—we simulated the effect of direct competition with a living agent on growth rate by reducing the length of the radius. We used competitive outcome probabilities from Precoda et al. (2017) to simulate between coral interactions (we used the trait aggressiveness if the species were not present in their list; see Appendix 1) (Appendix 2: §7.5.2). Branching and plating colonies can also overtop other colonies and algae. We used empirical estimates of competitive outcome probability to simulate competition between coral and algae (Brown et al., 2017; K. T. Brown, personal communication, October 2017; Appendix 2: §7.5.3). We considered algal functional groups as equal competitors and therefore they cannot overgrow each other, except for crustose coralline algae, which is a weaker competitor (Appendix 2: §7.5.4).

### Model calibration

Here, we provide a short description of the calibration. All details are presented in Appendix 3.

#### Study sites and related data

We used data collected between November 2001 and July 2011 in three sites located in Martinique in the Caribbean: Fond Boucher (14° 39′ 21.07″ N, 61° 09′ 38.98″ W), Pointe Borgnesse (14° 26′ 48.74″ N, 60° 54′ 12.72″ W), and Ilet à Rats (14° 40′ 58.04″ N, 60° 54′ 1.18″ W). The data were collected biannually (once per dry and wet seasons) by the Observatoire du Milieu Marin Martiniquais (OMMM) for the program Initiative Française pour les REcifs COralliens (IFRECOR). These data describe the benthic, macroinvertebrate, and fish communities at the species or genus levels, as well as sand cover for each site and at each sampling time (Appendix 3—figure 1, 2). We downloaded values of degree-heating weeks for the corresponding location from the US National Oceanic and Atmospheric Administration data server ERDDAP (Environmental Research Division's Data Access Program; coastwatch.pfeg.noaa.gov/erddap) (Appendix 3—figure 3). We identified cyclone tracks using the National Oceanic and Atmospheric Administration Historical Hurricane Tracks website (coast.noaa.gov/hurricanes).

#### Definition of the environmental context

We modelled thermal stress by inputting at each time step the maximum degree-heating week value found for the corresponding period. We represented the intensity of hydrodynamic regimes by inputting values of the dislodgement mechanical threshold (Madin and Connolly, 2006). We imposed a constant value in the absence of cyclone and a lower value when Hurricane Dean affected the reefs in August 2007 (its intensity changed from Category 1 to 2 while passing over Martinique). We chose threshold values arbitrarily considering wave exposure and cyclone intensity. Because of this uncertainty, we defined three different hydrodynamic regimes that we included in the calibration procedure for each site (Appendix 3—figure 5).

To estimate the percentage of the reef grazed at each time step, we first defined models predicting grazing intensity (i.e. percentage cover maintained in a cropped state) as a function of herbivorous fish and urchin density (we did not activate the rugosity-grazing feedback process). We defined these models using the empirical data from Williams and Polunin (2001) and Sammarco (1980) for fish and urchins, respectively (Appendix 3—figure 6). We then used these models and the population densities of Acanthuridae spp., Scaridae spp., and sea urchins measured in the three sites to predict their respective grazing regimes. Finally, we defined three additional similar regimes of different intensities, which we included in the calibration procedure (Appendix 3—figure 8).

The model adjusts the amount of sand cover (i.e. by removing or adding sand patches) at each time step according to the observed cover measured in each site (Appendix 3—figure 4). Having no information about larval connectivity at the three sites, we set the number of larvae m−2to 700 during each reproductive time period (i.e. once a year). This number corresponds to our estimate of competent larvae arriving on a hypothetical reef 20 km from an upstream reef having a 50% coral cover (Appendix 2: §7.2.1.2). The number is realistic considering that the distance separating the three sites from other coral communities is lower, but the average coral cover in the French West Indies is on average <40% (Wilkinson, 2008).

#### General procedure

We calibrated the model for each site independently. We selected 12 parameters, for which we defined between two to five potential values (Appendix 3—table 1). We defined an algorithm to explore the parameter space optimally. The algorithm first selects the centroid, the most extreme values, and the values situated at mid-distance between the centroid and the extremes. A simulation with each parameter value is launched and replicated five times. We measured the fit between the empirical and simulated cover time series using an objective function. The objective function measures the performance of a given run by calculating the Euclidian distance between the empirical and simulated cover time series (averaged over five replicates), averaged over all the taxa (Appendix 3: §3.2). Performance is thus a positive value, with smaller values indicating higher performance (lower difference between simulated and empirical values). The algorithm then selects the 10 runs providing the best performance and generates for each of them the five closest (using Gower’s distance metric; Gower, 1971) and untested parameter combinations. The algorithm then launches these new simulations and repeats the procedure once more.

To compare the performance of model runs to a null expectation, we generated a null distribution of performance values for each empirical dataset by randomizing cover values within each row and calculating the distance from the original datasets.

### Hierarchically structured validation

Models are often validated by comparing outputs of a single level of organization (i.e. individual, population, community) to equivalent empirical datasets (individual species coverages in our case), but this approach only examines lower dimensionality for more complex models. Following the recommendation of Kubicek et al. (2015), and aligned with the approach of pattern-oriented modeling (Grimm et al., 2005), we used a hierarchical approach to assess whether the different processes implemented in our model—starting from the those occurring at the lowest scales, to those affecting the entire system—produce ecologically realistic patterns by comparing them to expectations formulated a priori. We based several of the expectations using the classification of life-history strategies of Grime (1977) into competitive, stress-tolerant and ruderal (CSR) (or weedy) functional groups—﻿a classification which was adapted to corals (Darling et al., 2012). This ‘CSR’ classification is independent from the effect, resistance and recovery trait classification that Carturan et al. (2018) adapted to corals, and which we used to select the traits to implement in the model.

We assessed the following processes of our model: (i) we expected colony lateral growth to equal the species growth rate in absence of spatial interaction and to decrease as space becomes saturated by colonies; (ii) recruitment rate should increase as a population grows from low initial cover, and then decrease as space saturates; for competition under different (iii) disturbance-regime intensities—we expected the competitive species to dominate the community under low-disturbance regimes, and ruderal or stress-tolerant species otherwise; (iv) larval connectivity—we expected species with higher colony fecundity or brooding mode of larval development to dominate the community under low connectivity, and the competitive ones otherwise; (v) grazing—under low grazing pressure, the benthic community should be dominated by algae, and by corals otherwise. In procedures iii, iv, and v, we varied the intensity of one factor at time while maintaining the other factors at intermediate values. This design generated factor combinations that are not realistic (e.g. grazing pressure and larval connectivity usually decrease after a strong disturbance), but is more rigorous because it prevented us from subjectively defining time series of grazing and larval connectivity that would yield more realistic population dynamics. We did not activate the rugosity-grazing feedback process in the analysis.

Because we expected the community dynamics to depend on species-specific trait differences, we did procedures iii, iv, and v with two different communities, each composed of a competitive, a ruderal, and a stress-tolerant species, originating from the Eastern Pacific and Western Atlantic, respectively. Note that our goal was not to use suites of species that accurately reflect the taxonomic composition of particular reefs or species pools, but rather to select species based on their functional trait attributes. Although we refer to species by name, the names themselves therefore matter less than their functionality. It is well known that reefs with different biogeographic or evolutionary histories host species that are functionally similar (McWilliam et al., 2018b). All details are in Appendix 5.

### Global sensitivity analysis

Our goal was to estimate the sensitivity of the predicted dynamics of the model to parameter variation during a process of recovery after a strong pulse disturbance. We constructed a global sensitivity analysis for 10 of the calibrated parameters and six additional parameters with high uncertainty (Appendix 6—table 1). For each parameter, we defined a range around the value(s) calibrated (for the 10 parameters considered in the calibration) or the value used in the simulations (for the six additional parameters). These parameters are all continuous but vary in their type (i.e. probabilities, ratio, heights, sub-model coefficients). We defined their respective ranges considering parameter uncertainty, realistic boundaries, and what values might improve the model performance based on model calibration and hierarchically structured validation. We did the procedure for each site independently because certain parameters were calibrated on different values between sites and because the coral communities differ.

We simulated our model for 10 years with a bleaching event of an intensity of 12 degree-heating weeks occurring after 4 years. We consequently assessed model sensitivity 6 years after the disturbance, a time when the communities in most runs were still recovering. We kept the following processes constant: grazing (50%; we did not activate the rugosity-grazing feedback process), wave hydrodynamic regime (dislodgement mechanical threshold = 120, which is equivalent to strong wave regimes that colonies experience at the reef crest), and larval input from the regional pool (700 larvae m−2). We defined the same initial benthic composition as the one observed in the Caribbean sites.

We defined five response variables that represent the ecological state of the community at the end of the simulation: (i) total coral cover, (ii) difference of total coral cover at year 10 and just after the bleaching event, (iii) Pielou’s evenness, (iv) coral species richness (only the species with ≥1% cover), and (v) number of recruits m−2.

We estimated the relative importance of the parameters selected on each response variable following the efficient protocol of Prowse et al. (2016). For each site, we sampled 1000 combinations of parameter values from a continuous parameter space using Latin hypercube sampling and uniform-sampling distributions. We launched each combination once (no replicates). We then fitted boosted regression trees on the input parameter values for each response variable—the procedure provides the respective influence of each predictor (i.e. model parameter) on the variation of the response variable in question. We ensured the sampling was sufficient by comparing the influence of the parameters obtained with n = 1000 samples with values obtained with subsamples (n = 100, 250, 500 and 750); sampling is estimated to be sufficient when the influence of the parameters converge to similar values as sample size increases. All the details of the procedure are in Appendix 6.

## Results

### Model calibration

Model performance (the Euclidian distance between the empirical and simulated cover time series averaged over all taxa) varies between 28 and 10 (lower values = better performance), and were all lower than the lower 95% confidence bound of the random distribution (Appendix 3—figure 9). This shows that, despite the model’s complexity and parameter uncertainty, the model outputs population dynamics closer to the empirical data compared to random. The best performance values converged toward 10 among the three sites (i.e. minimum ± standard error: 10.93 ± 3.677, 10.89 ± 2.872, 10.39 ± 3.119 for Fond Boucher, Pointe Borgnesse and Ilet à Rats, respectively).

With the combination of parameter estimates yielding the best fit, the model produces time series of total coral cover similar to the empirical ones for each site (Figure 3; Appendix 3—figure 14; Appendix 3—figure 15). The difference between the simulated and real total coral cover does not exceed 15, 20, and 11% for Fond Boucher, Pointe Borgnesse and Ilet à Rats, respectively. Results at the species level are more variable, but the cover difference of individual coral populations never exceeds 8%. For some species, the simulated cover closely predicts the empirical data—for instance, O. faveolata and O. annularis at Ilet à Rats (Figure 3) and A. agaricites and S. siderea at Fond Boucher (Appendix 3—figure 14). The model failed to predict the population dynamics of some other species accurately; for instance, in the simulated reefs, M. mirabilis, M. decactis and P. furcata became the dominant species, while the cover of P. atreoides and M. meandrites approached zero at Fond Boucher; M. mirabilis outcompeted O. annularis, O. faveolata, O. franksi and P. astreoides at Pointe Borgnesse (Appendix 3—figure 14; Appendix 3—figure 15), while the P. astreoides’s population decreased at Ilet à Rats (Figure 3).

![Figure 3.](https://cdn.elifesciences.org/articles/55993/elife-55993-fig3-v2.jpg)

**Figure 3.:** Solid lines in the simulated time series are the percentage cover means (averaged over five replicates) and the shaded areas show the standard error. The right panels display the cover difference between simulated and empirical time series.

The simulated cover of algae also closely mimics the empirical data for most algal groups (Figure 3; Appendix 3—figure 14; Appendix 3—figure 15). The difference of percentage cover is the highest for turf and reaches a maximum of 29, 22% and 24% for Fond Boucher, Pointe Borgnesse and Ilet à Rats, respectively. These percentages are high compared to other groups or taxa, but this can be explained partially by the high variance in algal turf cover observed at the reefs. Turf cover generally fluctuates by >20%, a pattern that our model was able to reproduce at all three sites (Figure 3; Appendix 3—figure 14; Appendix 3—figure 15). Notably, crustose coralline algae are systematically less abundant in the simulated reefs compared to the observed data, a phenomenon we attempted to correct in the calibration procedure (Appendix 3: §3.3). Finally, the model could not reproduce the high cover of Halimeda spp. observed at Ilet à Rats (Figure 3) compared to the other sites. See Appendix 3 for more detailed results and discussion regarding the between-site comparison.

### Hierarchically structured validation

The hierarchically structured validation shows that the model produces ecologically realistic population dynamics under different environmental conditions. Here, we provide a summary of the results, but a more-complete description and explanation are available in Appendix 5.

#### Growth

Coral colonies grew ipso facto at their species-specific growth rate at low population density. However, as space filled up, colonies began constraining each other spatially and their growth rates decreased until eventual stasis (Appendix 5—figure 4).

#### Recruitment

For a single coral population, the different patterns of recruitment observed among three functionally distinct species (Appendix 5—figure 6) results from the interaction of several factors: (i) individual colony fecundity determined by its planar area, species-specific polyp fecundity, corallite area (polyp size), growth form, sexual system, and mode of larval development; (ii) the distribution of colony size in the population, which depends on maximum colony diameter; and (iii) the amount of surface available for larval settlement. Weedy (Agaricia tenuifolia) and stress-tolerant species (Echinophyllia orpheensis) produced bell-shape recruitment patterns (Appendix 5—figure 8). Recruitment rate was initially low because populations were composed of small, low-fecundity colonies, but the rate increased as colonies grew and became more fertile (Appendix 5—figure 8). Recruitment subsequently decreased as space became saturated. In contrast, recruitment rate for competitive species (Acropora gemmifera) was initially high and only decreased as cover occupancy increased. This pattern is essentially due to a higher vegetative growth rate associated with a population initially composed of fewer but larger, more fecund colonies (Appendix 5—figure 8).

#### Disturbance intensity

In both the Western Atlantic and Eastern Pacific communities (we compared the two functionally distinct coral communities in the rest of the analysis), the competitive species dominated the coral community under low wave exposure (Appendix 5—figure 10, 11, 14). The success of the competitive species was due mainly to two interacting processes—with a higher vegetative growth rate, competitive species (i) overcame free space before other species, and (ii) enhanced recruitment by achieving large colony size rapidly. Higher wave exposure reduced the cover of competitive species because colonies were dislodged at a certain colony size, which reduced recruitment rate and provided other species with more available space to grow and recruit.

In the Western Atlantic community, increased availability of space favoured the weedy species (Madracis pharencis) over the stress-tolerant species (Orbicella annularis), principally because of the former’s brooding mode of larval development (twice a year), faster growth rate, and high wave-resistance of its growth form (digitate). In contrast, species coexisted in the Eastern Pacific community under the highest-intensity disturbances (Appendix 5—figure 14). Both the competitive (Pocillopora elegans) and stress-tolerant species (Porites lutea) recruited more than weedy species (P. damicornis) due to their spawning mode of reproduction; spawning species received three times more larvae from the regional pool (Appendix 2: §7.2.1.2). However, the weedy species recruited twice as frequently and is slightly more aggressive than the other two species. The stress-tolerant species has a massive growth form, which conferred higher resistance to waves compared to the other two branching species. Nonetheless, this advantage barely compensated for its slower growth rate and lower colony fecundity.

Population(s) recovered to pre-disturbance cover after only one year, regardless of the intensity of the event. This recovery is faster than most dynamics observed in real reef systems and arises because we imposed a constant and high number of larvae (7000 m−2) coming from the regional pool. In reality, larval supplies are reduced because a strong bleaching disturbance would also affect the surrounding reefs (Hughes et al., 2019). Another reason for this outcome was that recruitment preceded growth in the model (Figure 2), which inflated the former process because more space was available for settlement.

#### Larval connectivity

Low larval connectivity influenced the two coral communities differently (Appendix 5: §5). In the Western Atlantic, the weedy species thrived under zero to moderate larval input (0, 66, 700 larvae m−2) while the other two species went locally extinct (Appendix 5—figure 17). The weedy species produced ready-to-settle larvae twice a year, while the other two species reproduced annually and only a portion of their larvae were able to settle because of their time to motility (Appendix 2: §7.2.1.1.d). In contrast, the stress-tolerant species dominated in the Eastern Pacific community (Appendix 5—figure 18) due to its higher wave-resistance compared to the other two branching species.

Under the highest larval connectivity (7000 and 35,000 larvae m−2), the competitive species dominated in both communities, principally because of their higher growth rates, spawning mode of reproduction, and their capacity to overtop smaller colonies.

#### Grazing

Population dynamics were similar between the two communities (Appendix 5—figure 20, 25). The total coral cover corresponded approximately to the imposed percentage of reef grazed, and the remaining ungrazed part of the reef was occupied by algae (also, ungrazed coral agents potentially exist). We observed no hysteresis because we did not implement feedback processes. Turf dominated the algae community in all simulated grazing regimes, despite having the highest palatability among algae (Appendix 2—table 3). The success of turf was due to its much higher growth rate compared to other algae (Appendix 2—table 19).

Coral recruitment rates at the steady state were the highest under medium grazing pressure (50%) because under lower and higher grazing intensities, space was saturated by turf and coral colonies, respectively. Under the lowest grazing pressure, most of the colonies were ≤100 cm2 in surface area (Appendix 5—figure 22) and coral populations were rescued by external larval input. At intermediate pressures (30% and 50%), the competitive species dominated the coral community mainly because of their higher external larval input compared to the brooding (weedy) species, and their higher growth rate than the stress-tolerant species. Having a high growth rate was particularly important under low grazing pressure because this trait compensated better for the cover lost in competition with turf, which wins all its interactions with corals in the model (Appendix 2—table 19).

Under higher grazing pressures (70% and 90%), there were more coral-coral and fewer coral-algae interactions, which changed coral species dominance. The Western Atlantic community was dominated by the weedy species, followed by the stress-tolerant species and the competitive species was competitively excluded, mainly because of its lower aggressiveness and highest vulnerability to waves (Appendix 5—figure 10). In the Eastern Pacific community, the stress-tolerant species dominated the coral community and slowly outcompeted the other two species mainly because of its much higher wave resistance (Appendix 5—figure 27).

### Global sensitivity analysis

The parameters that had the most important effects on the response variables (i.e. total coral cover, Pielou’s evenness, difference cover, coral species richness and the number of coral recruits m−2, all measured 10.5 years after the disturbance) were growth rate reduction interaction (the reduction of lateral growth rate of an organism overgrowing another one) and otherProportions (coefficient controlling the number of larvae produced locally), followed by probabilities for larvae to settle on different substrata, and the probabilities of algal grazing. The remaining 10 parameters did not have an important influence on any of the five response variables (Appendix 6—figure 1).

Globally, all the influential parameters affected the response variables according to expectations. For instance, increasing growth-rate reduction when organisms interact (mostly turf over corals) reduced the competitive advantage of the dominant taxa, which increased coral richness, total coral cover (due to reduced competitiveness of algae), and consequently enhanced the difference in coral cover and the number of coral recruits (Appendix 6—figure 1). Increasing otherProportions increased the number of larvae produced by each coral population, which positively affected coral cover, cover difference and the number of coral recruits. The parameter was negatively correlated with richness and evenness because higher values disproportionately benefitted species capable of higher recruitment (e.g. brooder; Appendix 6—figure 3).

In general, the parameters influenced the response variables in consistent ways among sites (Appendix 6—figure 1). Differences were mainly due to different ranges of values tested for particular parameters. For instance, probability of grazing allopathic macroalgae had a stronger effect at Pointe Borgnesse compared to the other two sites because its range included smaller values, implying lower palatability, higher abundance (Appendix 6—table 1, Appendix 6—figure 4), and a larger effect.

Ten of the parameters had a negligible effect on the response variables, because the processes they contributed to did not occur in these simulations. For instance, probability of algae to cover crustose coralline algae did not have an effect because crustose coralline algae was not present in high enough abundance (Appendix 6—figure 4), and height of big algae and height of turf did not have an effect because most of the branching colonies did not reach sizes large enough to overtop these algae (Appendix 6—figure 5).

## Discussion

Our primary goal was to develop a model that captured the spatiotemporal dynamics of community composition in coral reefs as component coral and algal species responded to inter-species competitive interactions and external disturbances. Our trait-based and demographic approaches provided a combination that yielded better predictions and a better understanding of coral ecosystem dynamics relative to single-component models (Edmunds et al., 2014; Salguero‐Gómez et al., 2018; Violle et al., 2007). The spatial structure we imposed—a grid of 1 cm2 agents that collectively comprise a sizeable reef (tens of m2) as inspired by previous models (e.g. Langmead and Sheppard, 2004; Sleeman et al., 2005; Tam and Ang, 2009; Sandin and McNamara, 2012)—yielded emergence, scaling, self-organization, and unpredictability, each of which is a property of complex systems (Parrott, 2002) including coral reefs (Dizon and Yap, 2006; Hatcher, 1997). Operating at such a small spatial grain, processes can be modelled at the appropriate scale (e.g. dislodgement removes entire colonies while spatial competition affects colony edges) (Figure 1) to generate distributions of colony size, and in turn, colony fitness and performance. Overall, the population dynamics resulted from the collective performance of each colony, which implies that at the scale of the community, a given species’ fitness depended on its capacity to persist under a certain environmental context and compete with functionally dissimilar species. As in the real world, macro-scale community dynamics emerged from finer-scale processes and interactions, a phenomenon clearly demonstrated by the hierarchically structured validation (Appendix 5). The model structure can also accommodate the initialization of a specific spatial colony arrangement based on empirical data. This feature is absent in previous models (but see Wakeford et al., 2008), despite the importance of spatial patterns for herbivory (Eynaud et al., 2016) and coral population dynamics (Brito-Millán et al., 2019).

Our model is unique in being designed to simulate the effects of coral species richness and functional diversity on ecosystem dynamics. Most coral models have been developed to describe the effect of external drivers (mainly disturbances) on the state of the coral community (usually total cover) (e.g., Bozec and Mumby, 2015; Kubicek et al., 2019; Kubicek and Reuter, 2016; Madin et al., 2012; Melbourne-Thomas et al., 2011a). In contrast, few models exist that assess the influences of aspects of diversity on community or ecosystem dynamics (e.g. Tam and Ang, 2012; Ortiz et al., 2014; Fabina et al., 2015), but these have represented diversity with limited detail, and consequently have limited capacity to evaluate the effects of identity and diversity on ecosystem functioning (Brandl et al., 2019), or the effects of functional redundancy and response diversity on ecosystem resilience (Mcleod et al., 2019). In contrast, our model represents diversity in detail; we considered eleven functional traits and included their influence over eight ecological processes applied to 798 functionally realistic species. In addition, we ensured that species richness can be varied without affecting computation time. Our model therefore enables exploration of many realistic assemblage scenarios within an easily modified experimental setting.

Our calibrated model was able to reproduce similar total coral-cover dynamics in the three sites (Figure 3; Appendix 3—figure 14; Appendix 3—figure 15). At the population level, results were more varied, with several populations well predicted, others less so. Overall, these results are remarkable considering model complexity, the large number of parameters, and the limited data describing the environmental context and diversity at the three sites. Note that we validated the population dynamics of the species within an imposed environmental context. Specifically, we determined the external larval supply, hydrodynamic, thermal, grazing and sand input regimes before the simulations. In reality, feedback processes emerge and contribute in shaping community dynamics (van de Leemput et al., 2016). Implementing additional feedback processes would have increased model complexity, and we estimated that the empirical data we had were insufficient to validate these. For instance, the model offers the option to activate the feedback process between structural complexity and grazing pressure (Appendix 2: §7.1.2.2), but validating this model with this process requires better population density estimates of the major herbivorous fishes.

A useful model should ideally be calibrated and validated with empirical data at each level of organization (e.g. colony, population, community) (Kubicek et al., 2015). However, empirical data are usually lacking for some or even all of these levels. Coral models have therefore been validated against one or a few community-aggregated variables, and rarely at the species level. Sampling additional data specifically for the model and at the sites used for calibration and benefiting from the opinion of local experts can improve the capacity of the model considerably to reproduce realistic dynamics. For instance Mumby (2006) developed a spatially explicit, mechanistic model to reproduce the total coral and macroalgae cover observed in Jamaican reefs. In two subsequent developments of the model, Ortiz et al. (2014) reproduced accurate recovery rates and final community composition of six coral taxa at 14 reefs in the Great Barrier Reef, and Bozec et al. (2015) reproduced the cover of seven coral species and the rugosity in reefs in Cozumel (Mexico). With a similar model, Kubicek et al. (2012) generated time series of major coral taxa cover at Chumbe Island (Tanzania) similar to real data. Further, Kayal et al. (2018) accurately reproduced colony density distributions of three coral species in four different sites in Moorea, French Polynesia, using integral-projection models.

In contrast with conventional approaches, we developed our model independently of the empirical data on which calibration was based. Instead, our model included the ecological details required for achieving our primary objective. Below we discuss the primary sources of uncertainty in our model calibration and suggest realistic ways for improvement.

Grazing: We estimated average grazing pressure over six months (% of reef grazed) based on a biannual assessment of sea urchin and herbivorous fish (Scaridae spp. and Acanthuridae spp.) populations. Acanthuridae spp. are mobile herbivores (Thibaut et al., 2012), so frequent assessments are necessary to obtain accurate estimates of mean population size. More data collection could improve the accuracy of the modeled processes, has others have done for several fish species (e.g. Bozec et al., 2016; Mumby, 2006).

Hydrodynamic regime: We defined time series of dislodgement mechanical threshold as a function of site exposure and cyclone intensity. Measuring the real dislodgement mechanical threshold over time in each site would improve the precision of the simulations. This would require measuring horizontal water velocity and tensile strength of the substratum (Madin et al., 2013; Madin and Connolly, 2006).

Recruitment: There is high uncertainty in our implementation of recruitment because we did not have estimates of recruitment rates and of the proportion of recruits originating from the local reef versus the regional pool. We therefore fixed the number of external larvae coming into the reef and controlled recruitment rate with one parameter (otherProportions). The sensitivity analysis revealed that the parameter has a strong influence on the model’s predictions. Reducing this uncertainty requires better estimates of recruitment rates, which can be achieved with tile experiments (e.g. Ritson-Williams et al., 2016) or visual assessment of new recruits along transects (e.g. Gilmour et al., 2013; Holbrook et al., 2018). The proportion of locally versus regionally recruited larvae can be estimated with population genetics (e.g. Almany et al., 2017; Johnson et al., 2018) or by modeling larvae plumes (e.g. Golbuu et al., 2012; Wolanski and Kingsford, 2014).

Trait data: The hierarchically structured validation showed that between-species trait differences influenced community dynamics. Considerable gaps in the coral-trait database (Madin et al., 2016a) limited our capacity to estimate traits accurately for many coral species. Collecting reliable trait data is critical to predict coral-community dynamics and ecosystem functioning (Madin et al., 2012). Further precision in the prediction would be gained by measuring traits locally, because traits can vary substantially among populations in different locations (e.g. Diaz-Pulido et al., 2009), and factors such as nutrient concentration affect both algae and corals growth (Wear and Thurber, 2015; Zaneveld et al., 2016).

The third dimension: The model represents flat benthic communities and estimates the height and surface area of colonies using simple geometric formulae. These approximations potentially misrepresent certain processes such as larval production, formation of reef rugosity, overtopping, and their interspecific differences. Recent efforts to quantify physical attributes of the colony from planar areas and growth forms (Zawada et al., 2019) provide potential opportunities to improve our model’s accuracy.

Our model is flexible and can be tailored to represent coral communities around the world, and to explore many different questions pertaining to the links between diversity and ecosystem dynamics. This version of the model focusses primarily on coral diversity and the effect of two disturbance types, but other disturbance types, and additional processes and aspects of reef diversity, could be easily implemented provided sufficient data are available. Examples include functions related to herbivory, algal diversity, disturbance types, and feedback processes, which we elaborate below.

Herbivores differ in their foraging behaviour (reviewed in Appendix 2: §7.1.1), which affects benthic diversity, coral reef recovery, and functioning (Burkepile and Hay, 2010; Cheal et al., 2013; Cheal et al., 2010; Nash et al., 2016; Pratchett et al., 2014). A few models have described aspects of herbivore diversity; for instance, Sandin and McNamara (2012) modelled the effect of spatially differentiated foraging behaviour between fish and urchins on the dynamics of a coral community, and Bozec et al. (2016) modelled the population dynamics of several parrot fish species and their respective species and size-specific contribution to grazing. However, herbivore diversity has generally been neglected in coral-reef models. Accommodating herbivore diversity and its effect on the benthic community in our model is feasible, provided associations between population densities and processes (e.g. grazing, bioerosion) are empirically established for different taxonomic or functional groups (e.g. Appendix 3: §2.3).

Algal diversity is potentially as important as coral and herbivore diversity for reef functioning and recovery (e.g., Roff et al., 2015). Yet, most coral-reef models describe the algal community with no more than three functional groups (macroalgae, crustose coralline algae, turf). Our model is the first to implement six functional groups, which accommodated additional ecological details such as grazing preferences and coral-algae interactions (Appendix 2: §7.1.2 and §7.5.3, respectively). To date, trait-based research on tropical reef algae is modest compared to fishes and corals (Brandl et al., 2019) and an algal-traits database has not yet been created.

We implemented the effects of hydrodynamic variation, thermal disturbances, and changes in grazing pressure, but reefs are also affected by other disturbances, and some of these have been implemented in previous models—including ocean acidification (e.g. Anthony et al., 2011; Madin et al., 2012), predation by Acanthaster planci (e.g. Hogeweg and Hesper, 1990; van der Laan and Bradbury, 1990), disease (e.g. Brandt and McManus, 2009), destructive fishing (e.g. Kubicek et al., 2012), and pollution (e.g., Wolanski et al., 2004; Melbourne-Thomas et al., 2011b; Kennedy et al., 2013). We are currently not able to model the species-specific effects of these disturbances on coral assemblages because it is not clear what traits are relevant, nor how these relate to ecological processes and responses. Such information is necessary to parameterize mechanistic models such as ours, as exemplified by our trait-based model of the response of corals to bleaching (Appendix 4). Nevertheless, our model would benefit from further validation, and is missing important variables (e.g. symbiont diversity) for which data are lacking (Carturan et al., 2018).

Feedback processes affect population dynamics by generating thresholds, hysteresis, and by shaping basins of attraction (Scheffer et al., 2001; Scheffer and Carpenter, 2003). Coral reefs are notorious for feedback processes (Hughes et al., 2010; Mumby and Steneck, 2008), some of which have been implemented in models (e.g. Mumby et al., 2007; Muthukrishnan et al., 2016; Kubicek and Reuter, 2016). van de Leemput et al. (2016) reviewed over 20 different feedback processes observed in reefs and demonstrated with a simple model that the combination of several feedback processes, although weak individually, can have important effects on system dynamics. However, the empirical quantification of these processes remains to be established (van de Leemput et al., 2016).

The model we present here is suitable for simulating the local response of benthic coral reef communities to disturbances over short time periods (<2 decades). Predicting community dynamics over longer periods (e.g. under different climate-change scenarios) requires calibrating the model with longer empirical time series because we cannot guarantee that the actual calibration will yield realistic community dynamics beyond the periods we considered. For testing and demonstration purposes, we implemented the model for small spatial extents. Consequently, the size-class distributions of certain coral species comprising large colonies might not be realistic, and certain influential processes happening at larger scales (e.g. connectivity along environmental gradients and from refuges) are not implemented in our simulations. However, the model can be run for larger spatial extents, but such simulations require substantial computational power due to the high ecological detail and 1 cm2 spatial resolution of the model. Ongoing model development includes improving computational efficiency to accommodate the simulation of larger spatial scales and related processes.

Minimalist models of coral reef systems (e.g. differential equation systems) have generally been developed to simulate the response of state variables to different processes (i.e. pulse and press disturbances, feedback processes) (Weijerman et al., 2015). Our model, while developed for the same objectives, provides the possibility to represent realistic benthic diversity and its effect on community dynamics. Comparing the results of our model to those obtained from minimalist models would help establish the degree to which ecological details are necessary.

### Conclusion

We have constructed a dynamic and customizable model that allows coral species richness and functional diversity to be manipulated independently. The model combines trait-based, demographic, and agent-based approaches to implement many ecological processes that drive coral reef dynamics. Its structure is flexible, and more processes, traits and taxa can be incorporated, provided the data are available. To that end, we highlighted several knowledge gaps that impede the modelling of important details or components of coral reef ecosystems. Our model can be used as a platform for virtual experiments aimed at testing hypotheses about the effects of species identity and diversity on ecosystem functioning, and about the effects of functional redundancy and response diversity on resilience.

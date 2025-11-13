# The NeuroML ecosystem for standardized multi-scale modeling in neuroscience

## Authors

- Ankur Sinha<sup>1</sup> ([ORCID: 0000-0001-7568-7167](https://orcid.org/0000-0001-7568-7167))
- Padraig Gleeson<sup>1</sup> ([ORCID: 0000-0001-5963-8576](https://orcid.org/0000-0001-5963-8576)) †
- Bóris Marin<sup>2</sup>
- Salvador Dura-Bernal<sup>3</sup>
- Sotirios Panagiotou<sup>5</sup>
- Sharon Crook<sup>6</sup>
- Matteo Cantarelli<sup>7</sup> ([ORCID: 0000-0002-0054-226X](https://orcid.org/0000-0002-0054-226X))
- Robert C Cannon<sup>8</sup>
- Andrew P Davison<sup>9</sup> ([ORCID: 0000-0002-4793-7541](https://orcid.org/0000-0002-4793-7541))
- Harsha Gurnani<sup>10</sup>
- Robin Angus Silver<sup>1</sup> ([ORCID: 0000-0002-5480-6638](https://orcid.org/0000-0002-5480-6638)) †

### Affiliations

1. Department of Neuroscience, Physiology and Pharmacology, University College London London United Kingdom ([ROR:02jx3x895](https://ror.org/02jx3x895))
2. Universidade Federal do ABC São Bernardo do Campo Brazil ([ROR:028kg9j04](https://ror.org/028kg9j04))
3. SUNY Downstate Medical Center Brooklyn United States ([ROR:0041qmd21](https://ror.org/0041qmd21))
4. Center for Biomedical Imaging and Neuromodulation, Nathan Kline Institute for Psychiatric Research Orangeburg United States ([ROR:01s434164](https://ror.org/01s434164))
5. Erasmus University Rotterdam Rotterdam Netherlands ([ROR:057w15z03](https://ror.org/057w15z03))
6. Arizona State University Tempe United States ([ROR:03efmqc40](https://ror.org/03efmqc40))
7. MetaCell Ltd Cambridge United States
8. Opus2 International Ltd London United Kingdom
9. CNRS Gif-Sur-Yvette France ([ROR:02feahw73](https://ror.org/02feahw73))
10. University of Washington Seattle United States ([ROR:00cvxb145](https://ror.org/00cvxb145))

† Corresponding author

## Abstract

Data-driven models of neurons and circuits are important for understanding how the properties of membrane conductances, synapses, dendrites, and the anatomical connectivity between neurons generate the complex dynamical behaviors of brain circuits in health and disease. However, the inherent complexity of these biological processes makes the construction and reuse of biologically detailed models challenging. A wide range of tools have been developed to aid their construction and simulation, but differences in design and internal representation act as technical barriers to those who wish to use data-driven models in their research workflows. NeuroML, a model description language for computational neuroscience, was developed to address this fragmentation in modeling tools. Since its inception, NeuroML has evolved into a mature community standard that encompasses a wide range of model types and approaches in computational neuroscience. It has enabled the development of a large ecosystem of interoperable open-source software tools for the creation, visualization, validation, and simulation of data-driven models. Here, we describe how the NeuroML ecosystem can be incorporated into research workflows to simplify the construction, testing, and analysis of standardized models of neural systems, and supports the FAIR (Findability, Accessibility, Interoperability, and Reusability) principles, thus promoting open, transparent and reproducible science.

## Introduction

Development of an in-depth, mechanistic understanding of brain function in health and disease requires different scientific approaches spanning multiple scales, from gene expression to behavior. Although ‘wet’ experimental approaches are essential for characterizing the properties of neural systems and testing hypotheses, theory and modeling are critical for exploring how these complex systems behave across a wider range of conditions, and for generating new experimentally testable, physically plausible hypotheses. Theory and modeling also provide a way to integrate a panoply of experimentally measured parameters, functional properties, and responses to perturbations into a physio-chemically coherent framework that reproduces the properties of the neural system of interest (Einevoll et al., 2019; Yao et al., 2022; Poirazi and Papoutsi, 2020; Gurnani and Silver, 2021; Gleeson et al., 2018; Cayco-Gajic et al., 2017; Billings et al., 2014; Vervaeke et al., 2010; Kriener et al., 2022; Billeh et al., 2020; Markram et al., 2015).

Computational models in neuroscience often focus on different levels of description. For example, a cellular physiologist may construct a complex multi-compartmental model to explain the dynamical behavior of an individual neuron in terms of its morphology, biophysical properties, and ionic conductances (Hay et al., 2011; De Schutter and Bower, 1994; Migliore et al., 2005). In contrast, to relate neural population activity to sensory processing and behavior, a systems neurophysiologist may build a circuit-level model consisting of thousands of much simpler integrate-and-fire neurons (Lapicque, 1907; Potjans and Diesmann, 2014; Brunel, 2000). Domain specific tools have been developed to aid the construction and simulation of models at varying levels of biological detail and scales. An ecosystem of diverse tools is powerful and flexible, but it also creates serious challenges for the research community (Cannon et al., 2007). Each tool typically has its own design, features, Application Programming Interface (API) and syntax, a custom set of utility libraries, and finally, a distinct machine-readable representation of the model’s physiological components. This represents a complex landscape for users to navigate. Additionally, models developed in different simulators cannot be mixed and matched or easily compared, and the translation of a model from one tool-specific implementation to another can be non-trivial and error-prone. This fragmentation in modeling tools and approaches can act as a barrier to neuroscientists who wish to use models in their research, as well as impede how Findable, Accessible, Interoperable, and Reusable (FAIR) models are (Wilkinson et al., 2016).

To counter fragmentation and promote cooperation and interoperability within and across fields, standardization is required. The International Neuroinformatics Co-ordinating Facility (INCF) (Abrams et al., 2022) has highlighted the need for standards to ‘make research outputs machine-readable and computable and are necessary for making research FAIR’ (INCF, 2023). In biology, several community standards have been developed to describe experimental data (e.g. Brain Imaging Data Structure [BIDS; Gorgolewski et al., 2016], Neurodata Without Borders [NWB; Teeters et al., 2015]) and computational models (e.g. Systems Biology Markup Language [SBML; Hucka et al., 2003], CellML [Lloyd et al., 2004], Scalable Open Network Architecture TemplAte [SONATA; Dai et al., 2020], PyNN [Davison et al., 2008] and Neural Open Markup Language [NeuroML; Gleeson et al., 2010]). These standards have enabled open and interoperable ecosystems of software applications, libraries, and databases to emerge, facilitating the sharing of research outputs, an endeavor encouraged by a growing number of funding agencies and scientific journals.

The initial version of the NeuroML standard, version 1 (NeuroMLv1), was originally conceived as a model description format (Goddard et al., 2001) and implemented as a three-layered, declarative, modular, simulator-independent language (Gleeson et al., 2010). NeuroMLv1 could describe detailed neuronal morphologies and their biophysical properties as well as specific instantiations of networks. It enabled the archiving of models in a standardized format and addressed the issue of simulator fragmentation by acting as the common language for model exchange between established simulation environments—NEURON (Hines and Carnevale, 1997; Awile et al., 2022), GENESIS (Bower and Beeman, 1998), and MOOSE (Ray and Bhalla, 2008). While solving a number of long-standing problems in computational neuroscience, NeuroMLv1 had several key limitations. The most restrictive of these was that the dynamical behavior of model elements was not formally described in the standard itself, making it only partially machine readable. Information on the dynamics of elements (i.e. how the state variables should evolve in time) was only provided in the form of human-readable documentation, requiring the developers of each new simulator to re-implement the behavior of these elements in their native format. Additionally, the introduction of new model components required updates to the standard and all supporting simulators, making extension of the language difficult. Finally, the use of Extensible Markup Language (XML) as the primary interface language limited usability—applications would generally have to add their own code to read/write XML files.

To address these limitations, NeuroML was redesigned from the ground up in version 2 (NeuroMLv2) using the Low Entropy Modeling Specification (LEMS) language (Cannon et al., 2014). LEMS was designed to define a wide range of physio-chemical systems, enabling the creation of fully machine-readable, formal definitions of the structure and dynamics of any model components. Modeling elements in NeuroMLv2 (cells, ion channels, synapses) have their mathematical and structural definitions described in LEMS (e.g. the parameters required and how the state variables change with time). Thus, NeuroMLv2 retains all the features of NeuroMLv1—it remains modular, declarative, and continues to support multiple simulation engines—but unlike version 1, it is extensible, and all specifications are fully machine-readable. NeuroMLv2 also moved to Python as its main interface language and provides a comprehensive set of Python libraries to improve usability (Vella et al., 2014), with XML retained as a machine-readable serialization format (i.e. the form in which the model files are saved/shared).

Since its release in 2014, the NeuroMLv2 standard, the software ecosystem, and the community have all steadily grown. An open, community-based governance structure was put in place—an elected Editorial Board, overseen by an independent Scientific Committee, maintains the standard and core software tools—APIs, reference simulators, and utilities. Although these tools were initially focused on enabling the simulation of models on multiple platforms, they have been expanded to support all stages of the model life cycle (Figure 1). Modelers can use these tools to easily create, inspect and visualize, validate, simulate, fit and optimize, share and disseminate NeuroMLv2 models and outputs (Billings et al., 2014; Cayco-Gajic et al., 2017; Gurnani and Silver, 2021; Kriener et al., 2022; Gleeson et al., 2019b). To provide clear, concise, searchable information for both users and developers, the NeuroML documentation has been significantly expanded and re-deployed using the latest modern web technologies (https://docs.neuroml.org). Increased community-wide collaborations have also extended the software ecosystem well beyond the NeuroMLv2 tools developed by the NeuroML team: additional simulators such as Brian (Stimberg et al., 2019), NetPyNE (Dura-Bernal et al., 2019), Arbor (Akar et al., 2019) and EDEN (Panagiotou et al., 2022) all support NeuroMLv2. We have worked to ensure interoperability with other structured formats for model development in neuroscience such as PyNN (Davison et al., 2008) and SONATA (Dai et al., 2020). Platforms for collaboratively developing, visualizing, and sharing NeuroML models (Open Source Brain (OSB) Gleeson et al., 2019b) as well as a searchable database of NeuroML model components NeuroML Database (NeuroML-DB) (Birgiolas et al., 2023) have been developed. These enhancements, driven by an ever-expanding community, have helped NeuroMLv2 grow into a standard that has been officially endorsed by international organizations such as the INCF and COmputational Modeling in Biology NEtwork (COMBINE) (Hucka et al., 2015), and that is now sufficiently mature to be incorporated into a wide range of research workflows.

![Figure 1.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig1-v1.jpg)

In this paper, we provide an overview of the current scope of version 2 of the NeuroML standard, describe the current software ecosystem and community, and outline the extensive resources to assist researchers in incorporate NeuroML into their modeling work. We demonstrate, with examples, that NeuroML supports users at all stages of the model development life cycle (Figure 1) and promotes FAIR principles in computational neuroscience. We highlight the various NeuroML tools and libraries, additional utilities, supported simulation engines, and the related projects that build upon NeuroML for automated model validation, advanced analysis, visualization, and sharing/re-use of models. Finally, we summarize the organizational aspects of NeuroML, its governance structure and its community.

## Results

### NeuroML provides a ready-to-use set of curated model elements

A central aim of the NeuroML initiative is to enable and encourage the use of multi-scale biophysically detailed models of neurons and neuronal circuits in neuroscience research. The initiative takes a range of steps to achieve this aim.

NeuroML provides users with a curated library of model elements that form the NeuroML standard (An index of all the model elements included in version 2.3 of NeuroML, with links to further online documentation, is provided in Tables 1 and 2; Figure 2). The standard is maintained by the NeuroML Editorial Board that has identified a fundamental set of model types to support, to ensure that a significant proportion of commonly used neurobiological modeling entities can be described with the language. This includes (but is not limited to): active membrane conductances (using Hodgkin-Huxley style [Hodgkin and Huxley, 1952] or kinetic scheme-based ionic conductances), multiple synapse and plasticity mechanisms, detailed multi-compartmental neuron models with morphologies and biophysical properties, abstract point neuron models, and networks of such cells spatially arranged in populations, connected by targeted projections, receiving spiking and currently based inputs.

![Figure 2.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig2-v1.jpg)

**Figure 2.:** Elements in NeuroML are formally defined, independent, self-contained building blocks with hierarchical relationships between them. (a) Models of ionic conductances can be defined as a composition of gates, each with specific voltage (and potentially [Ca2+]) dependence that controls the conductance. (b) Morphologically detailed neuronal models specify the 3D structure of the cells, along with passive electrical properties, and reference ion channels that confer membrane conductances. (c) Network models contain populations of these cells connected via synaptic projections. (d) A truncated illustration of the main categories of the NeuroMLv2 standard elements and their hierarchies. The standard includes commonly used model elements/building blocks that have been pre-defined for users: Cells: neuronal models ranging from simple spiking point neurons to biophysically detailed cells with multi-compartmental morphologies and active membrane conductances; Synapses and ionic conductance models: commonly used chemical and electrical synapse models (gap junctions), and multiple representations for ionic conductances; Inputs: to drive cell and network activity, e.g., current or voltage clamp, spiking background inputs; Networks: of populations (containing any of the aforementioned cell types), and projections. The full list of standard NeuroML elements can be found in Tables 1 and 2.

**Table 1.**
 Index of standard NeuroMLv2 ComponentTypes.


<table>
  <thead>
    <tr>
      <th colspan="3">Core components</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>annotation</td>
      <td>bqbiol_encodes</td>
      <td>bqbiol_hasPart</td>
    </tr>
    <tr>
      <td>bqbiol_hasProperty</td>
      <td>bqbiol_hasTaxon</td>
      <td>bqbiol_hasVersion</td>
    </tr>
    <tr>
      <td>bqbiol_is</td>
      <td>bqbiol_isDescribedBy</td>
      <td>bqbiol_isEncodedBy</td>
    </tr>
    <tr>
      <td>bqbiol_isHomologTo</td>
      <td>bqbiol_isPartOf</td>
      <td>bqbiol_isPropertyOf</td>
    </tr>
    <tr>
      <td>bqbiol_isVersionOf</td>
      <td>bqbiol_occursIn</td>
      <td>bqmodel_is</td>
    </tr>
    <tr>
      <td>bqmodel_isDerivedFrom</td>
      <td>bqmodel_isDescribedBy</td>
      <td>rdf_Bag</td>
    </tr>
    <tr>
      <td>rdf_Description</td>
      <td>rdf_li</td>
      <td>rdf_RDF</td>
    </tr>
    <tr>
      <td>property</td>
      <td>point3DWithDiam</td>
      <td>notes</td>
    </tr>
    <tr>
      <td colspan="3">Core dimensions</td>
    </tr>
    <tr>
      <td>area</td>
      <td>capacitance</td>
      <td>charge</td>
    </tr>
    <tr>
      <td>charge_per_mole</td>
      <td>concentration</td>
      <td>conductance</td>
    </tr>
    <tr>
      <td>conductance_per_voltage</td>
      <td>conductanceDensity</td>
      <td>current</td>
    </tr>
    <tr>
      <td>currentDensity</td>
      <td>idealGasConstantDims</td>
      <td>length</td>
    </tr>
    <tr>
      <td>per_time</td>
      <td>per_voltage</td>
      <td>permeability</td>
    </tr>
    <tr>
      <td>resistance</td>
      <td>resistivity</td>
      <td>rho_factor</td>
    </tr>
    <tr>
      <td>specificCapacitance</td>
      <td>substance</td>
      <td>temperature</td>
    </tr>
    <tr>
      <td>time</td>
      <td>voltage</td>
      <td>volume</td>
    </tr>
    <tr>
      <td colspan="3">Abstract cell models</td>
    </tr>
    <tr>
      <td>adExIaFCell</td>
      <td>fitzHughNagumoCell</td>
      <td>hindmarshRose1984Cell</td>
    </tr>
    <tr>
      <td>iafCell</td>
      <td>iafRefCell</td>
      <td>iafTauCell</td>
    </tr>
    <tr>
      <td>iafTauRefCell</td>
      <td>izhikevich2007Cell</td>
      <td>izhikevichCell</td>
    </tr>
    <tr>
      <td>pinskyRinzelCA3Cell</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">ComponentTypes related to biophysically detailed cells</td>
    </tr>
    <tr>
      <td>biophysical Properties</td>
      <td>biophysicalProperties2CaPools</td>
      <td>cell</td>
    </tr>
    <tr>
      <td>cell2CaPools</td>
      <td>concentration Model</td>
      <td>decayingPoolConcentrationModel</td>
    </tr>
    <tr>
      <td>distal</td>
      <td>distalProperties</td>
      <td>fixedFactorConcentrationModel</td>
    </tr>
    <tr>
      <td>fixedFactorConcentrationModelTraub</td>
      <td>from</td>
      <td>include</td>
    </tr>
    <tr>
      <td>inhomogeneousParameter</td>
      <td>inhomogeneousValue</td>
      <td>initMembPotential</td>
    </tr>
    <tr>
      <td>intracellular Properties</td>
      <td>intracellularProperties2CaPools</td>
      <td>member</td>
    </tr>
    <tr>
      <td>membraneProperties</td>
      <td>membraneProperties2CaPools</td>
      <td>morphology</td>
    </tr>
    <tr>
      <td>parent</td>
      <td>path</td>
      <td>pointCellCondBased</td>
    </tr>
    <tr>
      <td>pointCellCondBasedCa</td>
      <td>proximal</td>
      <td>proximalProperties</td>
    </tr>
    <tr>
      <td>segment</td>
      <td>segment Group</td>
      <td>species</td>
    </tr>
    <tr>
      <td>spikeThresh</td>
      <td>subTree</td>
      <td>to</td>
    </tr>
    <tr>
      <td>variable Parameter</td>
      <td>channel Density</td>
      <td>channelDensityGHK</td>
    </tr>
    <tr>
      <td>channelDensityGHK2</td>
      <td>channelDensityNernst</td>
      <td>channelDensityNernstCa2</td>
    </tr>
    <tr>
      <td>channelDensityNonUniform</td>
      <td>channelDensityNonUniformGHK</td>
      <td>channelDensityNonUniformNernst</td>
    </tr>
    <tr>
      <td>channelDensityVShift</td>
      <td>channelPopulation</td>
      <td>channelPopulationNernst</td>
    </tr>
    <tr>
      <td colspan="3">ComponentTypes related to ion channels</td>
    </tr>
    <tr>
      <td>fixedTimeCourse</td>
      <td>forward Transition</td>
      <td>gate</td>
    </tr>
    <tr>
      <td>gateFractional</td>
      <td>gateHHInstantaneous</td>
      <td>gateHHrates</td>
    </tr>
    <tr>
      <td>gateHHratesInf</td>
      <td>gateHHratesTau</td>
      <td>gateHHratesTauInf</td>
    </tr>
    <tr>
      <td>gateHHtauInf</td>
      <td>gateKS</td>
      <td>HHExpLinearRate</td>
    </tr>
    <tr>
      <td>HHExpLinearVariable</td>
      <td>HHExpRate</td>
      <td>HHExpVariable</td>
    </tr>
    <tr>
      <td>HHSigmoidRate</td>
      <td>HHSigmoidVariable</td>
      <td>ionChannel</td>
    </tr>
    <tr>
      <td>ionChannelHH</td>
      <td>ionChannelKS</td>
      <td>ionChannelPassive</td>
    </tr>
    <tr>
      <td>ionChannelVShift</td>
      <td>KSState</td>
      <td>KSTransition</td>
    </tr>
    <tr>
      <td>open State</td>
      <td>q10ConductanceScaling</td>
      <td>q10ExpTemp</td>
    </tr>
    <tr>
      <td>q10Fixed</td>
      <td>reverse Transition</td>
      <td>sub Gate</td>
    </tr>
    <tr>
      <td>tauInfTransition</td>
      <td>vHalfTransition</td>
      <td>closedState</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Index of standard NeuroMLv2 ComponentTypes (continued).


<table>
  <thead>
    <tr>
      <th colspan="3">ComponentTypes related to synapses</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>alphaCurrentSynapse</td>
      <td>alphaSynapse</td>
      <td>blockingPlasticSynapse</td>
    </tr>
    <tr>
      <td>doubleSynapse</td>
      <td>expOneSynapse</td>
      <td>expThreeSynapse</td>
    </tr>
    <tr>
      <td>expTwoSynapse</td>
      <td>gap Junction</td>
      <td>gradedSynapse</td>
    </tr>
    <tr>
      <td>linearGradedSynapse</td>
      <td>silentSynapse</td>
      <td>stdpSynapse</td>
    </tr>
    <tr>
      <td>tsodyksMarkramDepFacMechanism</td>
      <td>tsodyksMarkramDepMechanism</td>
      <td>voltageConcDepBlockMechanism</td>
    </tr>
    <tr>
      <td colspan="3">ComponentTypes related to inputs</td>
    </tr>
    <tr>
      <td>compoundInput</td>
      <td>compoundInputDL</td>
      <td>poissonFiringSynapse</td>
    </tr>
    <tr>
      <td>pulseGenerator</td>
      <td>pulseGeneratorDL</td>
      <td>rampGenerator</td>
    </tr>
    <tr>
      <td>rampGeneratorDL</td>
      <td>sineGenerator</td>
      <td>sineGeneratorDL</td>
    </tr>
    <tr>
      <td>spike</td>
      <td>spikeArray</td>
      <td>spike Generator</td>
    </tr>
    <tr>
      <td>spikeGeneratorPoisson</td>
      <td>spikeGeneratorRandom</td>
      <td>spikeGeneratorRefPoisson</td>
    </tr>
    <tr>
      <td>timedSynapticInput</td>
      <td>transientPoissonFiringSynapse</td>
      <td>voltage Clamp</td>
    </tr>
    <tr>
      <td>voltageClampTriple</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">ComponentTypes related to networks</td>
    </tr>
    <tr>
      <td>connection</td>
      <td>connectionWD</td>
      <td>continuous Connection</td>
    </tr>
    <tr>
      <td>continuousConnectionInstance</td>
      <td>continuousConnectionInstanceW</td>
      <td>continuous Projection</td>
    </tr>
    <tr>
      <td>electrical Connection</td>
      <td>electricalConnectionInstance</td>
      <td>electricalConnectionInstanceW</td>
    </tr>
    <tr>
      <td>electrical Projection</td>
      <td>explicit Connection</td>
      <td>explicitInput</td>
    </tr>
    <tr>
      <td>input</td>
      <td>inputList</td>
      <td>inputW</td>
    </tr>
    <tr>
      <td>instance</td>
      <td>location</td>
      <td>network</td>
    </tr>
    <tr>
      <td>networkWithTemperature</td>
      <td>population</td>
      <td>population List</td>
    </tr>
    <tr>
      <td>projection</td>
      <td>rectangularExtent</td>
      <td>region</td>
    </tr>
    <tr>
      <td>synaptic Connection</td>
      <td>synapticConnectionWD</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">ComponentTypes related to model simulation</td>
    </tr>
    <tr>
      <td>Display</td>
      <td>EventOutputFile</td>
      <td>EventSelection</td>
    </tr>
    <tr>
      <td>Line</td>
      <td>OutputColumn</td>
      <td>OutputFile</td>
    </tr>
    <tr>
      <td>Simulation</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">ComponentTypes related to PyNN</td>
    </tr>
    <tr>
      <td>alphaCondSynapse</td>
      <td>alphaCurrSynapse</td>
      <td>EIF_cond_alpha_isfa_ista</td>
    </tr>
    <tr>
      <td>EIF_cond_exp_isfa_ista</td>
      <td>expCondSynapse</td>
      <td>expCurrSynapse</td>
    </tr>
    <tr>
      <td>HH_cond_exp</td>
      <td>IF_cond_alpha</td>
      <td>IF_cond_exp</td>
    </tr>
    <tr>
      <td>IF_curr_alpha</td>
      <td>IF_curr_exp</td>
      <td>SpikeSourcePoisson</td>
    </tr>
  </tbody>
</table>

The NeuroMLv2 standard consists of two levels that are designed to enable users to easily create their models without worrying about simulator-specific details. The first level defines a formal ‘schema’ for the standard model elements, their attributes/parameters (e.g. an integrate and fire cell model and its necessary attributes: a threshold parameter, a reset parameter, etc.), and the relationships between them (e.g. a network contains populations; a multi-compartmental cell morphology contains segments). This allows the validation of the completeness of the description of individual NeuroML model elements and models, prior to simulation. The second level defines the underlying dynamical behavior of the model elements (e.g. how the time-varying membrane potential of a cell model is to be calculated). Most users do not need to interact with this level (which is enabled by LEMS), which, among other features, enables the automated translation of simulator-independent NeuroML models into simulator-specific code.

Thus, modelers can use the standard NeuroML elements to conveniently build simulator-independent models, while also being able to examine and extend the underlying implementations of models. As a simulator-independent language, NeuroML also promotes interoperability between different computational modeling tools, and as a result, the standard library is complemented by a large, well-maintained ecosystem of software tools that support all stages of the model life cycle—from creation, analysis, simulation, and fitting, to sharing and reuse. Finally, as discussed in later sections, for advanced use cases where the existing NeuroML model building blocks are insufficient, NeuroML also includes a framework for creating and including new model elements.

### NeuroML is a modular, structured language for defining FAIR models

NeuroMLv2 is a modular, structured, hierarchical, simulator-independent format. All NeuroML elements are formally defined, independent, and self-contained with hierarchical relationships between them. An ‘ionic conductance’ model element in NeuroML, for example, can contain zero, one, or more ‘gates’ and be added into a ‘cell’ model element along with a ‘morphology’ element, which can then fit into a ‘population’ of a ‘network’ (Figure 2). To support the range of electrical properties found in biological neurons, ionic conductances with distinct ionic selectivities and dynamics can be generated in NeuroML through the inclusion of different types of gates (e.g. activation, inactivation), their dependence on variables such as voltage and [Ca2+] and their reversal potential. Cell types with different functional and biophysical properties can then be generated by conferring combinations of ionic conductances on their membranes. The conductance density can be adjusted to generate the electrophysiological properties found in real neurons. In practice, many examples of ionic conductances that underlie the electrical behavior of neurons are already available in NeuroMLv2 and can simply be inserted into a cell membrane (Figure 2). Indeed, a model element, once defined in NeuroML, acts as a building block that may be reused any number of times within or across models. Elements such as ionic conductances, cell biophysics, cell morphologies, and cell definitions that incorporate them can be serialized in separate files and ‘included’ in other models (e.g. morphologies https://docs.neuroml.org/Userdocs/ImportingMorphologyFiles.html#neuroml2). Such reuse of model components speeds model construction and prototyping irrespective of the simulation engine used.

The defined structure of each model element and the relationships between them inform users of exactly how model elements are to be created and combined. This encourages the construction of well-structured models, reduces errors and redundancy, and ensures that FAIR principles are firmly embedded in NeuroML models and the ecosystem of tools. As we will see in the following sections, NeuroML’s formal structure also enables features such as model validation prior to simulation, translation into simulation specific formats, and the use of NeuroML as a common language of exchange between different tools.

### NeuroML supports a large ecosystem of software tools that cover all stages of the model life cycle

Model building and the generation of scientific knowledge from simulation and analysis of models is a multi-step, iterative process requiring an array of software tools. NeuroML supports all stages of the model development life cycle (Figure 1), by providing a single model description format that interacts with a myriad of tools throughout the process. Researchers typically assemble ad-hoc sets of scripts, applications, and processes to help them in their investigations. In the absence of standardization, they must work with the specific model formats and APIs that each tool they use requires, and somehow convert model descriptions when using multiple applications in a toolchain. NeuroML addresses this issue by providing a common language for the use and exchange of models and their components between different simulation engines and modeling tools. The NeuroML ecosystem includes a large collection of software tools, both developed and maintained by the main NeuroML contributors (the ‘core NeuroML tools and libraries:’ jNeuroML, pyNeuroML, APIs) and those external applications that have added NeuroML support (Figures 3 and 4a, Tables 3 and 4).

![Figure 3.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig3-v1.jpg)

**Figure 3.:** The inner circle shows the core NeuroML tools and libraries that are maintained by the NeuroML developers. These provide the functionality to read, modify, or create new NeuroML models, as well as to validate, analyze, visualize and simulate the models. The outermost layer shows NeuroML-compliant tools that have been developed independently to allow various interactions with NeuroML models. These complement the core tools by facilitating model creation, validation, visualization, simulation, fitting/optimization, sharing, and reuse. Further information on each of the tools shown here can be found in Tables 3 and 4.

![Figure 4.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig4-v1.jpg)

**Figure 4.:** (a) The core NeuroML software stack consists of Java (blue) and Python (orange) based applications/libraries, and the LEMS model ComponentType definitions (green), wrapped up in a single package, pyNeuroML. Each of these modules can be used independently or the whole stack can be obtained by installing pyNeuroML with the default Python package manager, Pip: pip install pyneuroml. (b) An example of how to create a simple NeuroML model is shown, using the NeuroMLv2 Python API (libNeuroML) to describe a model consisting of a population of 10 integrate and fire point neurons (IafTauCell) in a network. The IafTauCell, Network, Population, and NeuroMLDocument model ComponentTypes are provided by the NeuroMLv2 standard. The underlying dynamics of the model are hidden from the user, being specified in the LEMS ComponentType definitions of the elements (see Methods). The simulator-independent NeuroML model description can be simulated on any of the supported simulation engines. (c) Extensible Markup Language (XML) serialization of the NeuroMLv2 model description shows the correspondence between the Python object model and the XML serialization.

**Table 3.**
 NeuroML software core tools and libraries, with a description of their scope, the main programming language they use (or other interaction means, e.g. Command Line Interface (CLI)), and links for more information.


<table>
  <thead>
    <tr>
      <th>Tool</th>
      <th>Language/interface</th>
      <th>Description</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>pyNeuroML</td>
      <td>Python/CLI</td>
      <td>Recommended Python library for NeuroML; provides pynml, primary command line tool for NeuroML</td>
      <td>https://docs.neuroml.org/Userdocs/Software/pyNeuroML.html</td>
    </tr>
    <tr>
      <td>libNeuroML</td>
      <td>Python</td>
      <td>Python API for NeuroML</td>
      <td>https://docs.neuroml.org/Userdocs/Software/libNeuroML.html</td>
    </tr>
    <tr>
      <td>NeuroMLlite</td>
      <td>Python</td>
      <td>High level library for creating NeuroML network models (beta)</td>
      <td>https://docs.neuroml.org/Userdocs/Software/NeuroMLlite.html</td>
    </tr>
    <tr>
      <td>PyLEMS</td>
      <td>Python/CLI</td>
      <td>Python API and simulator for LEMS</td>
      <td>https://docs.neuroml.org/Userdocs/Software/pyLEMS.html</td>
    </tr>
    <tr>
      <td>jLEMS</td>
      <td>Java/CLI</td>
      <td>Java API for LEMS and reference simulator</td>
      <td>https://docs.neuroml.org/Userdocs/Software/jLEMS.html</td>
    </tr>
    <tr>
      <td>org.neuroml.model</td>
      <td>Java</td>
      <td>Java API for NeuroML, DOI:10.5281/zenodo.5783290</td>
      <td>https://github.com/NeuroML/org.neuroml.model/</td>
    </tr>
    <tr>
      <td>org.neuroml.export</td>
      <td>Java</td>
      <td>Java API for translating NeuroML into different formats such as NEURON, DOI:10.5281/zenodo.1346272</td>
      <td>https://github.com/NeuroML/org.neuroml.export</td>
    </tr>
    <tr>
      <td>org.neuroml.import</td>
      <td>Java</td>
      <td>Java API for importing formats into LEMS and NeuroML, DOI:10.5281/zenodo.5783295</td>
      <td>https://github.com/NeuroML/org.neuroml.import</td>
    </tr>
    <tr>
      <td>jNeuroML</td>
      <td>Java/CLI</td>
      <td>Wraps jLEMS and all export/import packages and provides the jnml tool, DOI:10.5281/zenodo.593108</td>
      <td>https://docs.neuroml.org/Userdocs/Software/jNeuroML.html</td>
    </tr>
    <tr>
      <td>NeuroML-C++</td>
      <td>C++</td>
      <td>C++ API for NeuroML</td>
      <td>https://docs.neuroml.org/Userdocs/Software/NeuroML_API.html</td>
    </tr>
    <tr>
      <td>NeuroML Toolbox</td>
      <td>MATLAB</td>
      <td>MATLAB NeuroML Toolbox</td>
      <td>https://docs.neuroml.org/Userdocs/Software/MatLab.html</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 Tools in the wi main programming language they use (or other interaction means, e.g. through a web browser, Graphical User Interface (GUI) or Command Line Interface (CLI)), and links for more information.


<table>
  <thead>
    <tr>
      <th>Tool</th>
      <th>Language/interface</th>
      <th>Description</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="4">Simulation engines</td>
    </tr>
    <tr>
      <td>NEURON</td>
      <td>Python/Hoc/CLI/GUI</td>
      <td>Empirically-based simulations of neurons and networks of neurons</td>
      <td>https://docs.neuroml.org/Userdocs/Software/Tools/NEURON.html</td>
    </tr>
    <tr>
      <td>NetPyNE</td>
      <td>Python/web</td>
      <td>Package to facilitate the development, parallel simulation, analysis, and optimization of biological neuronal networks using the NEURON simulator. Also has a graphical web interface, NetPyNE-UI</td>
      <td>https://docs.neuroml.org/Userdocs/Software/Tools/NetPyNE.html</td>
    </tr>
    <tr>
      <td>EDEN</td>
      <td>NeuroML</td>
      <td>NeuroML-based neural simulator</td>
      <td>https://docs.neuroml.org/Userdocs/Software/Tools/EDEN.html</td>
    </tr>
    <tr>
      <td>MOOSE</td>
      <td>Python</td>
      <td>The Multiscale Object-Oriented Simulation Environment is the base and numerical core for large, detailed multi-scale simulations that span computational neuroscience and systems biology. Based on a reimplementation of the GENESIS 2 core.</td>
      <td>https://docs.neuroml.org/Userdocs/Software/Tools/MOOSE.html</td>
    </tr>
    <tr>
      <td>PyNN</td>
      <td>Python</td>
      <td>A simulator-independent language for building neuronal network models</td>
      <td>https://docs.neuroml.org/Userdocs/Software/Tools/PyNN.html</td>
    </tr>
    <tr>
      <td>NEST</td>
      <td>Python/SLI</td>
      <td>Simulator for spiking neural network models focusing on dynamics, size, and structure of neural systems</td>
      <td>https://docs.neuroml.org/Userdocs/Software/Tools/NEST.html</td>
    </tr>
    <tr>
      <td>Brian2</td>
      <td>Python</td>
      <td>Easy to learn and use simulator for spiking neural networks</td>
      <td>https://docs.neuroml.org/Userdocs/Software/Tools/Brian.html</td>
    </tr>
    <tr>
      <td>Arbor</td>
      <td>Python</td>
      <td>A multi-compartment neuron simulation library</td>
      <td>https://docs.neuroml.org/Userdocs/Software/Tools/Arbor.html</td>
    </tr>
    <tr>
      <td>N2A</td>
      <td>Java/GUI</td>
      <td>Language and IDE for writing and simulating models</td>
      <td>https://docs.neuroml.org/Userdocs/Software/Tools/N2A.html</td>
    </tr>
    <tr>
      <td colspan="4">Databases</td>
    </tr>
    <tr>
      <td>OSB</td>
      <td>Web</td>
      <td>Resource for sharing and collaboratively developing computational models of neural systems</td>
      <td>https://www.opensourcebrain.org/</td>
    </tr>
    <tr>
      <td>NeuroML-DB</td>
      <td>Web</td>
      <td>NeuroML database of cell and channel models</td>
      <td>https://neuroml-db.org/</td>
    </tr>
    <tr>
      <td colspan="4">Other tools</td>
    </tr>
    <tr>
      <td>OMV</td>
      <td>Python</td>
      <td>Open Source Brain Model Validation framework</td>
      <td>https://github.com/OpenSourceBrain/osb-model-validation</td>
    </tr>
    <tr>
      <td>SciUnit</td>
      <td>Python</td>
      <td>Data driven unit testing framework</td>
      <td>https://github.com/scidash/sciunit</td>
    </tr>
    <tr>
      <td>BluePyOpt</td>
      <td>Python</td>
      <td>Blue Brain Python Optimization Library</td>
      <td>https://bluepyopt.readthedocs.io/</td>
    </tr>
    <tr>
      <td>NeuroTune</td>
      <td>Python</td>
      <td>Package for fitting/optimization of NeuroML models</td>
      <td>https://github.com/NeuralEnsemble/neurotune</td>
    </tr>
    <tr>
      <td>PyElectro</td>
      <td>Python</td>
      <td>Electrophysiology analysis package</td>
      <td>https://github.com/NeuralEnsemble/pyelectro</td>
    </tr>
  </tbody>
</table>

The core NeuroML tools and libraries include APIs in several programming languages—Python, Java, C++, and MATLAB. These tools provide critical functionality to allow users to interact with NeuroML components and build models. Using these, researchers can build models from scratch, or read, modify, analyze, visualize, and simulate existing NeuroML models on supported simulation platforms. Furthermore, developers can also use the core tools, libraries, and APIs to support NeuroML in their own applications.

The simulation platforms e.g. EDEN (Panagiotou et al., 2022), NEURON (Hines and Carnevale, 1997), along with other independently developed tools, form the next layer of the software ecosystem—providing extra functionality such as interactive model construction (e.g. neuroConstruct Gleeson et al., 2007), NetPyNE (Dura-Bernal et al., 2019), additional visualization (e.g. OSB Gleeson et al., 2019b), analysis (e.g. NeuroML-DB Birgiolas et al., 2023), data-driven validation (e.g. SciUnit Gerkin et al., 2019), and archival/sharing (e.g. OSB, NeuroML-DB). Indeed, OSB and NeuroML-DB are prime examples of how advanced neuroinformatics resources can be built on top of standards such as NeuroML.

Table 5 lists interactive, step-by-step guides in the NeuroML documentation, which can be followed to learn the fundamental NeuroML concepts, as well as illustrate how NeuroML-compliant tools can be used to achieve specific tasks across the model development life cycle. In the following sections, we discuss the specific functionality available at each stage of model development.

**Table 5.**
 Step-by-step guides for using NeuroML illustrating the various stages of the model development life cycle.These include Introductory guides aimed at teaching the fundamental NeuroML concepts, Advanced guides illustrating specific modeling workflows, and Walkthrough guides discussing the steps required for converting models to NeuroML. An updated list is available at http://neuroml.org/gettingstarted.


<table>
  <thead>
    <tr>
      <th>Link</th>
      <th>Description</th>
      <th>Model life cycle stages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3">Introductory guides</td>
    </tr>
    <tr>
      <td>Guide 1</td>
      <td>Create and simulate a simple regular spiking Izhikevich neuron in NeuroML</td>
      <td>Create, Validate, Simulate</td>
    </tr>
    <tr>
      <td>Guide 2</td>
      <td>Create a network of two synaptically connected populations of Izhikevich neurons</td>
      <td>Create, Validate, Visualize, Simulate</td>
    </tr>
    <tr>
      <td>Guide 3</td>
      <td>Build and simulate a single compartment Hodgkin-Huxley neuron</td>
      <td>Create, Validate, Visualize, Simulate</td>
    </tr>
    <tr>
      <td>Guide 4</td>
      <td>Create and simulate a multi compartment hippocampal OLM neuron</td>
      <td>Create, Validate, Visualize, Simulate</td>
    </tr>
    <tr>
      <td colspan="3">Advanced guides</td>
    </tr>
    <tr>
      <td>Guide 5</td>
      <td>Create novel NeuroML models from components on NeuroML-DB</td>
      <td>Reuse, Create, Validate, Simulate</td>
    </tr>
    <tr>
      <td>Guide 6</td>
      <td>Optimize/fit NeuroML models to experimental data</td>
      <td>Create, Validate, Simulate, Fit</td>
    </tr>
    <tr>
      <td>Guide 7</td>
      <td>Extend NeuroML by creating a novel model type in LEMS</td>
      <td>Create, Simulate</td>
    </tr>
    <tr>
      <td colspan="3">Walkthroughs</td>
    </tr>
    <tr>
      <td>Guide 8</td>
      <td>Guide to converting cell models to NeuroML and sharing them on Open Source Brain</td>
      <td>Create, Validate, Simulate, Share</td>
    </tr>
    <tr>
      <td>Guide 9</td>
      <td>Conversion of Ray et al., 2020</td>
      <td>Create, Validate, Visualize, Simulate, Share</td>
    </tr>
  </tbody>
</table>

### Creating NeuroML models

The structured declarative elements of NeuroMLv2, when combined with a procedural scripting language such as Python, provide a powerful and yet intuitive ‘building block’ approach to model construction. For this reason, Python is now the recommended language for interacting with NeuroML (Figure 4), although XML remains the primary serialization language for the format (i.e. for saving to disk and depositing in model repositories (Figure 5)). Python has emerged as a key programming language in science, including many areas of neuroscience (Muller et al., 2015). A Python-based NeuroML ecosystem ensures that users can take advantage of Python’s features, and also use packages from the wider Python ecosystem in their work (e.g. Numpy (Harris et al., 2020), Matplotlib Hunter, 2007). pyNeuroML, the Python interface for working with NeuroML, is built on top of the Python NeuroML API, libNeuroML (Vella et al., 2014; Sinha, 2023; Figure 4).

![Figure 5.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig5-v1.jpg)

**Figure 5.:** The Python API can be used to create models which may include elements built from scratch from the NeuroML standard, re-use elements from previously created models, or create new components based on novel model definitions expressed in LEMS (red). The generated model elements are saved in the default XML-based serialization (blue). The NeuroML core tools and libraries (orange) include modules to import model descriptions expressed in the XML serialization, and support multiple options for how simulators can execute these models (green). These include: (1) execution of the NeuroML models by reference simulators; (2) execution by other independently developed simulators that natively support NeuroML, such as EDEN; (3) generation of Python ‘import scripts’ which allow NeuroML models to be imported (and converted to internal formats) by simulators which support this; (4) fully expanding the LEMS description of the models, which can be mapped to generated simulator specific scripts for target simulators; (5) mapping to other standardized formats in neuroscience and systems biology.

As illustrated in Figure 5, Python can be used to combine different NeuroML components into a model. NeuroML supports several pathways for the creation of new models. Modelers may use elements included in the NeuroML standard, re-use user-defined NeuroML model elements from other models, or define completely new model elements using LEMS (Figure 5) (see section on extending NeuroML below). It is common for models to use a combination of these strategies, e.g., Gurnani and Silver, 2021; Kriener et al., 2022; Cayco-Gajic et al., 2017, highlighting the flexibility provided by the modular design of NeuroML. NeuroML APIs support all of these workflows. The Python tools also include many additional higher-level utilities to speed up model construction, such as factory functions, type hints, and convenience functions for building complex multi-compartmental neuron models (Figure 6).

![Figure 6.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig6-v1.jpg)

For the construction of complex 3D circuit models, or for users who are not experienced with Python, a range of NeuroML-compliant online and standalone applications with graphical user interfaces are available. These include NetPyNE’s interactive web interface (Dura-Bernal et al., 2019) (which is available on the latest version of OSB (https://v2.opensourcebrain.org)) and neuroConstruct (Gleeson et al., 2007) which can export models directly into NeuroML and LEMS. These applications can be used to build and simulate new NeuroML models without requiring programming. Thus, users can take advantage of the individual features provided by these applications to generate NeuroML-compliant models and model elements.

### Validating NeuroML models

Ensuring a model is ‘valid’ can have different meanings at different stages of the life cycle—from checking whether the source files are in the correct format, to ensuring the model reproduces a significant feature of its biological counterpart. NeuroML’s hierarchical, well-defined structure allows users to check their model descriptions for correctness at multiple levels (Figure 7), in a manner similar to multi-level testing in software development. Importantly, most of the validation tests in NeuroML are run on the models’ NeuroML descriptions prior to simulation.

![Figure 7.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig7-v1.jpg)

**Figure 7.:** Checks are performed on the model descriptions (blue) before simulation using validation at both the NeuroML and LEMS levels (green). After the models are simulated (yellow), further checks can be run to ensure the output is in line with expected behavior (brown). The OSB Model Validation (OMV) framework can be used to ensure consistent behavior across simulators, and comparisons can be made of model activity to their biological equivalents using SciUnit.

A first level of validation checks the structure of individual model elements against their formal specifications contained in the NeuroML standard. The standard includes information on the parameters of each model element, restrictions on parameter values, their allowed units, their cardinality, and the location of the model element in the model hierarchy—i.e., parent/children relationships. A second level of validation includes a suite of semantic and logical checks. For example, at this level, a model of a multi-compartmental cell can be checked to ensure that all segments referenced in segment groups (e.g. the group of dendritic segments) have been defined, and only defined once with unique identifiers. A list of validation tests currently included in the NeuroML core tools can be found in Table 6. These can be run against NeuroML files at the command line or programmatically in Python (Figure 6).

**Table 6.**
 Listing of validation tests run by NeuroML.


<table>
  <thead>
    <tr>
      <th>Test</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2">Schema tests</td>
    </tr>
    <tr>
      <td>Check names</td>
      <td>Check that names of all elements, attributes, parameters match those provided in the schema</td>
    </tr>
    <tr>
      <td>Check types</td>
      <td>Check that the types of all included elements</td>
    </tr>
    <tr>
      <td>Check values</td>
      <td>Check that values follow given restrictions</td>
    </tr>
    <tr>
      <td>Check inclusion</td>
      <td>Check that required elements are included</td>
    </tr>
    <tr>
      <td>Check cardinality</td>
      <td>Check the number of elements</td>
    </tr>
    <tr>
      <td>Check hierarchy</td>
      <td>Check that child/children elements are included in the correct parent elements</td>
    </tr>
    <tr>
      <td>Check sequence order</td>
      <td>Check that child/children elements are included in the correct order</td>
    </tr>
    <tr>
      <td colspan="2">Additional tests</td>
    </tr>
    <tr>
      <td>Check top level ids</td>
      <td>Check that top level (root) elements have unique ids</td>
    </tr>
    <tr>
      <td>Check Network level ids</td>
      <td>Check that child/children of the Network element have unique ids</td>
    </tr>
    <tr>
      <td>Check Cell Segment ids</td>
      <td>Check that all Segments in a Cell have unique ids</td>
    </tr>
    <tr>
      <td>Check single Segment without parent</td>
      <td>Check that only one Segment is without parents (the soma Segment)</td>
    </tr>
    <tr>
      <td>Check SegmentGroup ids</td>
      <td>Check that all SegmentGroups in a Cell have unique ids</td>
    </tr>
    <tr>
      <td>Check Member segment ids exist</td>
      <td>Check that Segments referred to in SegmentGroup Members exist</td>
    </tr>
    <tr>
      <td>Check SegmentGroup definition</td>
      <td>Check that SegmentGroups being referenced are defined</td>
    </tr>
    <tr>
      <td>Check SegmentGroup definition order</td>
      <td>Check that SegmentGroups are defined before being referenced</td>
    </tr>
    <tr>
      <td>Check included SegmentGroups</td>
      <td>Check that SegmentGroups referenced by Include elements of other SegmentGroups exist</td>
    </tr>
    <tr>
      <td>Check numberInternalDivisions</td>
      <td>Check that SegmentGroups define numberInternalDivisions (used by simulators to discretize un-branched branches into compartments for simulation)</td>
    </tr>
    <tr>
      <td>Check included model files</td>
      <td>Check that model files included by other files exist</td>
    </tr>
    <tr>
      <td>Check Population component</td>
      <td>Check that a component id provided to a Population exists</td>
    </tr>
    <tr>
      <td>Check ion channel exists</td>
      <td>Check that an ion channel used to define a ChannelDensity element exists</td>
    </tr>
    <tr>
      <td>Check concentration model species</td>
      <td>Check that the species used in ConcentrationModel elements are defined</td>
    </tr>
    <tr>
      <td>Check Population size</td>
      <td>Check that the size attribute of a PopulationList matches the number of defined Instances</td>
    </tr>
    <tr>
      <td>Check Projection component</td>
      <td>Check that Populations used in the Projection elements exist</td>
    </tr>
    <tr>
      <td>Check Connection Segment</td>
      <td>Check that the Segment used in Connection elements exist</td>
    </tr>
    <tr>
      <td>Check Connection pre/post cells</td>
      <td>Check that the pre- and post-synaptic cells used in Connection elements exist and are correctly specified</td>
    </tr>
    <tr>
      <td>Check Synapse</td>
      <td>Check that the Synapse component used in a Projection element exists</td>
    </tr>
    <tr>
      <td>Check root id</td>
      <td>Check that the root Segment in a Cell morphology has id 0</td>
    </tr>
  </tbody>
</table>

A key advantage of using the NeuroML2/LEMS framework is that dimensions and units are inbuilt into LEMS descriptions. This enables automated conversions of units, unit checking, together with the validation of equations. Any expressions in models which are dimensionally inconsistent will be highlighted at this stage. Note that LEMS handles unit conversions internally—modelers have flexibility in how they enter the units of parameter values (e.g. specifying conductance density in $S/m^{2}$ or $mS/cm^{2}$) in the NeuroML files, with the underlying LEMS definitions ensuring that a consistent set of dimensions are used in model equations (Cannon et al., 2014). LEMS then takes care of mapping the entered units to the target simulator’s preferred units. This makes model definition, inspection, use, extension, and translation easier and less error-prone.

Once the set of NeuroML files are validated, the model can be simulated, and checks can be made to test whether execution produces consistent results (e.g. firing rate of neurons in a given population) across multiple simulators (or versions of the same simulator). For this, the OSB Model Validation (OMV) framework has been developed (Gleeson et al., 2019b). This framework can automatically check that the output (e.g. spike times) of a NeuroML model running on a given simulator is within an allowed tolerance of the expected value. OMV has been applied to NeuroML models that have been shared on OSB, to test consistent behavior of models as the models themselves, and all supported simulators, are updated. This has proven to be a valuable process for ensuring uniform usage and interpretation of NeuroML across the ecosystem of supporting tools.

A final level of validation concerns checking whether the model elements have emergent features that are in line with experimentally observed behavior of the biological equivalents. NeuronUnit (Gerkin et al., 2019), a SciUnit (Omar et al., 2014) package for data-driven unit testing and validation of neuronal and ion channel models, is also fully NeuroML compliant, and also supports automated validation of NeuroML models shared on NeuroML-DB and OSB.

### Visualizing/analyzing NeuroML models

Multiple visualization, inspection, and analysis tools are available in the NeuroML software ecosystem. Since NeuroML models have a fixed, well-defined structure, NeuroML libraries can extract all information from their descriptions. This information can be used by modelers and their programs/tools to run automated programmatic analyses on models.

pyNeuroML includes a range of ready-made inspection utilities for users (Figure 6) that can be used via Python scripts, interactive Jupyter Notebooks, and command line tools. Examining the structure of cell and network models with 2D and 3D views is important for manual validation and to compare them to their biological counterparts. Graphical views of cell model morphology and the 3-dimensional network layout (Figure 8), population and connectivity matrices/graphs at different levels (Figure 9), and model summaries can all be generated (Figure 10). In addition to these inspection functions, a variety of utilities for the inspection of NeuroML descriptions of electrophysiological properties of membrane conductances and their spatial distribution over the neuronal membrane are also provided (Figure 10).

![Figure 8.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig8-v1.jpg)

**Figure 8.:** (a) Interactive 3-D (VisPy (Campagnola, 2023) based) visualization of an olfactory bulb network with detailed mitral and granule cells (Migliore et al., 2014), generated using pyNeuroML. (b) Visualization of an inhibition stabilized network based on Sadeh et al., 2017 using Open Source Brain (OSB) version 1 (Gleeson et al., 2019b). (c) Visualization of 3D network of simplified multi-compartmental cortical neurons (from Traub et al., 2005, imported as NeuroML Gleeson, 2019a) and simulated spiking activity using NetPyNE’s GUI (Dura-Bernal et al., 2019), which is embedded in OSB version 2.

![Figure 9.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig9-v1.jpg)

**Figure 9.:** Network connectivity schematic (a) and connectivity matrix (b) for a half scale implementation of the human layer 2/3 cortical network model (Yao et al., 2022) generated using pyNeuroML.

![Figure 10.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig10-v1.jpg)

**Figure 10.:** (a) Electrophysiological properties generated by the NeuroML-DB web-based platform (Birgiolas et al., 2023). (Plots show four superimposed voltage traces in the top panel and corresponding current injection traces below). (b) Example plots of steady states of activation (na_channel na_m inf) and inactivation (na_channel na_h inf) variables and their time courses (na_channel na_m tau and na_channel na_h tau) for the Na channel from the classic Hodgkin Huxley model (Hodgkin and Huxley, 1952). (c) The distribution of the peak conductances for the Ih channel over a layer 5 Pyramidal cell (Hay et al., 2011). Both (b) and (c) were generated using the analysis features in pyNeuroML, and similar functionality is also available in OSBv1 (Gleeson et al., 2019b).

The graphical applications included in the NeuroML ecosystem (e.g. neuroConstruct, NeuroML-DB, OSB (v1 [https://v1.opensourcebrain.org] and v2), NetPyNE, and Arbor-GUI) also provide many of their own analysis and visualization functions. OSBv1, for example, supports automated 3D visualization of networks and cell morphologies, network connectivity graphs and metrics, and advanced model inspection features (Gleeson et al., 2019b; Figure 8b). On OSBv2, NetPyNE provides advanced graphical plotting and analysis facilities (Figure 8c). A complete JupyterLab (https://jupyter.org/) interface is also included in OSBv2 for Python scripting, allowing interactive notebooks to be created and shared, mixing scripting and graphical elements, including those generated by pyNeuroML. NeuroML-DB also provides information on electrophysiology, morphology, and the simulation aspects of neuronal models (Birgiolas et al., 2023; Figure 10a). In general, any NeuroML-compliant application can be used to inspect and analyze elements of NeuroML models, each having their own distinct advantages.

### Simulating NeuroML models

Users can simulate NeuroML models using a number of simulation engines without making any changes to their models. This is because the NeuroML/LEMS descriptions of the models are simulator independent and can be translated to simulator specific formats. pyNeuroML facilitates access to all available simulation options, both from the command line and using function calls in Python scripts when using the Python API (Figure 6).

Simulation engines can be classified into five broad categories (Figure 5):

Each simulation engine supports a different set of features that NeuroML users can take advantage of (Table 7). For example, the reference NeuroML and LEMS simulators, jNeuroML, jLEMS, and PyLEMS, can simulate all LEMS models and most NeuroML models. They cannot, however, simulate multi-compartmental models, and users should opt for a simulator that does, e.g., NEURON (Hines and Carnevale, 1997) or EDEN (Panagiotou et al., 2022).

**Table 7.**
 Features supported by NeuroML in different simulation engines.Note: the simulators themselves may support more features, but these have not been mapped onto by the NeuroML tools. Abstract cell models: abstract cell models included in the NeuroML standard (see Table 1). Single compartmental cells: neuronal models that include a single compartment (these engines do not support multi-compartmental cells). Multiple compartmental cells: neuronal models that include multiple compartments. Conductance-based models: models that support ionic conductances. Parallel execution: engines that support parallel execution using MPI/GPUs. Y: full support; N: no support; L: limited support in NeuroML toolchain.


<table>
  <thead>
    <tr>
      <th>Tool</th>
      <th>Abstract cell models</th>
      <th>Single compartment cells</th>
      <th>Multiple compartment cells</th>
      <th>Conductance-based models</th>
      <th>Parallel execution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>jNeuroML/pyNeuroML</td>
      <td>Y</td>
      <td>Y</td>
      <td>N</td>
      <td>Y</td>
      <td>N</td>
    </tr>
    <tr>
      <td>NEURON</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>N</td>
    </tr>
    <tr>
      <td>NetPyNE</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
    </tr>
    <tr>
      <td>EDEN</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
    </tr>
    <tr>
      <td>MOOSE</td>
      <td>Y</td>
      <td>Y</td>
      <td>L</td>
      <td>Y</td>
      <td>N</td>
    </tr>
    <tr>
      <td>PyNN</td>
      <td>Y</td>
      <td>Y</td>
      <td>L</td>
      <td>L</td>
      <td>Y</td>
    </tr>
    <tr>
      <td>NEST</td>
      <td>Y</td>
      <td>Y</td>
      <td>N</td>
      <td>N</td>
      <td>Y</td>
    </tr>
    <tr>
      <td>Brian2</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>Y</td>
      <td>L</td>
    </tr>
    <tr>
      <td>Arbor</td>
      <td>L</td>
      <td>Y</td>
      <td>Y</td>
      <td>L</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>

Another criteria that is relevant when choosing a simulation engine is the efficiency of simulation. Simulation engines implement different computing techniques—e.g., NetPyNE, Arbor, and EDEN support parallel execution on clusters and super computers via MPI—to enable simulation of large-scale models. Thus, for efficient large-scale simulation, users may prefer one of these simulation engines.

The preferred programming language for working with NeuroML is Python (Muller et al., 2015). A Python-based ecosystem ensures that automated simulation of models can easily be carried out either using scripts, or the command line tools. Utilities to enable the execution of simulations on dedicated supercomputing resources, such as the Neuroscience Gateway (NSG) (Sivagnanam, 2013; http://www.nsgportal.org/) are also available within the ecosystem. OSBv1 takes advantage of these to support the submission of NeuroML model simulation jobs using the NEURON simulator on NSG. NetPyNE also includes parallel execution of simulations, batch processing, and parameter exploration features, and its deployment on OSBv2 allows users to easily access these features on a scalable, cloud-based platform. Finally, the JupyterLab environment on OSBv2 contains all of the core NeuroML tools and various simulation engines as pre-installed software packages, ready to use.

### Optimizing NeuroML models

Development of biologically detailed models of brain function requires that components and emergent properties match the behavior of the corresponding biology as closely as possible. Thus, fitting neurons and networks to experimental data is a critical step in the model life cycle (Rossant et al., 2011; Druckmann et al., 2007). pyNeuroML promotes data-driven modeling by providing functions to fit and optimize NeuroML models against experimental data. It includes the NeuroMLTuner module (https://pyneuroml.readthedocs.io/en/development/pyneuroml.tune.html), which builds on the Neurotune package (https://github.com/NeuralEnsemble/neurotune; Vella and Gleeson, 2023) for tuning and optimizing NeuroML models against data using evolutionary computation techniques. This module allows users to select a set of weighted features from their data to calculate the fitness of populations of candidate models. In each generation, the fittest models are found and mutated to create the next generation of models, until a set of models that best exhibit the selected data features are isolated (see Guide 6 in Table 5) (https://docs.neuroml.org/Userdocs/OptimisingNeuroMLModels.html).

The NeuroML ecosystem includes multiple tools that also provide model fitting features. The Blue Brain Python Optimisation Library (BluePyOpt) (Van Geit et al., 2016), an extensible framework for data-driven model parameter optimization, supports exporting optimized models to NeuroML files (https://github.com/BlueBrain/BluePyOpt/blob/master/examples/neuroml/neuroml.ipynb). Similar to pyNeuroML, NetPyNE also uses the inspyred Python package (https://github.com/aarongarrett/inspyred; Sinha and Garrett, 2024) to provide evolutionary computation-based model optimization features (Dura-Bernal et al., 2019).

### Sharing NeuroML models

The NeuroML ecosystem includes the advanced web-based model sharing platforms NeuroML-DB (Birgiolas et al., 2023; https://neuroml-db.org) and OSB (Gleeson et al., 2019b). These resources have been designed specifically for the dissemination of models and model elements standardized in NeuroML. The OSB platform also supports visualization, analysis, simulation, and development of NeuroML models. Researchers can create shared, collaborative NeuroML projects on it and can take advantage of the in-built automated visualization and analysis pipelines to explore and re-use models and their components. Whereas version 1 (OSBv1) focused on providing an interactive 3D interface for running pre-existing NeuroML models (e.g. sourced from linked GitHub repositories) (Gleeson et al., 2019b), OSBv2 provides cloud-based workspaces for researchers to construct NeuroML-based computational models as well as analyze, and compare them to, the experimental data on which they are based, thus facilitating data-driven computational modeling. Table 8 provides a list of stable, well-tested NeuroML compliant models from brain regions including the neocortex, cerebellum, and hippocampus, which have been shared on OSB.

**Table 8.**
 Listing of NeuroML models and example repositories.


<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Description</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3">Neocortex</td>
    </tr>
    <tr>
      <td>Billeh et al., 2020</td>
      <td>Morphologically detailed and point neuron models based on electrophysiological recordings from visual cortex neurons</td>
      <td>https://github.com/OpenSourceBrain/AllenInstituteNeuroML</td>
    </tr>
    <tr>
      <td>Brunel, 2000</td>
      <td>Spiking network illustrating balance between excitation and inhibition</td>
      <td>https://github.com/OpenSourceBrain/Brunel2000</td>
    </tr>
    <tr>
      <td>Hay et al., 2011</td>
      <td>Layer 5 pyramidal cell model constrained by somatic and dendritic recordings</td>
      <td>https://github.com/OpenSourceBrain/L5bPyrCellHayEtAl2011</td>
    </tr>
    <tr>
      <td>Izhikevich, 2004</td>
      <td>Spiking neuron model reproducing wide range of neuronal activity</td>
      <td>https://github.com/OpenSourceBrain/IzhikevichModel</td>
    </tr>
    <tr>
      <td>Markram et al., 2015</td>
      <td>Cell models from Neocortical Microcircuit of Blue Brain Project</td>
      <td>https://github.com/OpenSourceBrain/BlueBrainProjectShowcase</td>
    </tr>
    <tr>
      <td>Pospischil et al., 2008</td>
      <td>HH-based models for different classes of cortical and thalamic neurons</td>
      <td>https://github.com/OpenSourceBrain/PospischilEtAl2008</td>
    </tr>
    <tr>
      <td>Potjans and Diesmann, 2014</td>
      <td>Microcircuit model of sensory cortex with 8 populations across 4 layers</td>
      <td>https://github.com/OpenSourceBrain/PotjansDiesmann2014</td>
    </tr>
    <tr>
      <td>Dura-Bernal et al., 2017</td>
      <td>Model of mouse primary motor cortex (M1)</td>
      <td>https://github.com/OpenSourceBrain/M1NetworkModel</td>
    </tr>
    <tr>
      <td>Sadeh et al., 2017</td>
      <td>Point neuron model of Inhibition Stabilized Network</td>
      <td>https://github.com/OpenSourceBrain/SadehEtAl2017-InhibitionStabilizedNetworks</td>
    </tr>
    <tr>
      <td>Smith et al., 2013</td>
      <td>Layer 2/3 cell model used to investigate dendritic spikes</td>
      <td>https://github.com/OpenSourceBrain/SmithEtAl2013-L23DendriticSpikes</td>
    </tr>
    <tr>
      <td>Traub et al., 2005</td>
      <td>Single column network model containing 14 cell populations from cortex and thalamus</td>
      <td>https://github.com/OpenSourceBrain/Thalamocortical</td>
    </tr>
    <tr>
      <td>Bahl et al., 2012</td>
      <td>A set of reduced models of layer 5 pyramidal neurons</td>
      <td>https://github.com/OpenSourceBrain/BahlEtAl2012_ReducedL5PyrCell</td>
    </tr>
    <tr>
      <td>Wilson and Cowan, 1972</td>
      <td>A classic rate-based model describing the dynamics and interactions between the excitatory and inhibitory populations of neurons</td>
      <td>https://github.com/OpenSourceBrain/WilsonCowan</td>
    </tr>
    <tr>
      <td>Garcia Del Molino et al., 2017</td>
      <td>Rate-based model showing paradoxical response reversal of top-down modulation in cortical circuits with three interneuron types</td>
      <td>https://github.com/OpenSourceBrain/del-Molino2017</td>
    </tr>
    <tr>
      <td>Mejias et al., 2016</td>
      <td>A rate-based model simulating the dynamics of a cortical laminar structure across multiple scales: intralaminar, interlaminar, interareal and whole cortex</td>
      <td>https://github.com/OpenSourceBrain/MejiasEtAl2016</td>
    </tr>
    <tr>
      <td colspan="3">Cerebellum</td>
    </tr>
    <tr>
      <td>Maex and Schutter, 1998</td>
      <td>Cerebellar granule cell</td>
      <td>https://github.com/OpenSourceBrain/GranuleCell</td>
    </tr>
    <tr>
      <td>Cayco-Gajic et al., 2017</td>
      <td>Cerebellar granule cell layer network</td>
      <td>https://github.com/SilverLabUCL/MF-GC-network-backprop-public</td>
    </tr>
    <tr>
      <td>Maex and Schutter, 1998</td>
      <td>3D Cerebellar granule cell layer network</td>
      <td>https://github.com/OpenSourceBrain/GranCellLayer</td>
    </tr>
    <tr>
      <td>Solinas et al., 2007</td>
      <td>Cerebellar Golgi cell model</td>
      <td>https://github.com/OpenSourceBrain/SolinasEtAl-GolgiCell</td>
    </tr>
    <tr>
      <td>Vervaeke et al., 2010</td>
      <td>Electrically connected cerebellar Golgi cell network model</td>
      <td>https://github.com/OpenSourceBrain/VervaekeEtAl-GolgiCellNetwork</td>
    </tr>
    <tr>
      <td colspan="3">Hippocampus</td>
    </tr>
    <tr>
      <td>Bezaire et al., 2016</td>
      <td>Full scale network model of CA1 region of hippocampus</td>
      <td>https://github.com/mbezaire/ca1</td>
    </tr>
    <tr>
      <td>Ferguson et al., 2013</td>
      <td>Parvalbumin-positive interneuron from CA1, based on Izhikevich cell model</td>
      <td>https://github.com/OpenSourceBrain/FergusonEtAl2013-PVFastFiringCell</td>
    </tr>
    <tr>
      <td>Ferguson et al., 2014</td>
      <td>Pyramidal cell from CA1, based on Izhikevich cell model</td>
      <td>https://github.com/OpenSourceBrain/FergusonEtAl2014-CA1PyrCell</td>
    </tr>
    <tr>
      <td>Migliore et al., 2005</td>
      <td>Multi-compartmental model of pyramidal cell from CA1 region of hippocampus</td>
      <td>https://github.com/OpenSourceBrain/CA1PyramidalCell</td>
    </tr>
    <tr>
      <td>Pinsky and Rinzel, 1994</td>
      <td>Simplified model of CA3 pyramidal cell</td>
      <td>https://github.com/OpenSourceBrain/PinskyRinzelModel</td>
    </tr>
    <tr>
      <td>Wang and Buzsáki, 1996</td>
      <td>Hippocampal interneuronal network model exhibiting gamma oscillations</td>
      <td>https://github.com/OpenSourceBrain/WangBuzsaki1996</td>
    </tr>
    <tr>
      <td colspan="3">Olfactory bulb</td>
    </tr>
    <tr>
      <td>Migliore et al., 2014</td>
      <td>Large-scale 3D olfactory bulb network with detailed mitral cells and granule cells</td>
      <td>https://github.com/OpenSourceBrain/MiglioreEtAl14_OlfactoryBulb3D</td>
    </tr>
    <tr>
      <td colspan="3">Invertebrate</td>
    </tr>
    <tr>
      <td>Hodgkin and Huxley, 1952</td>
      <td>Classic investigation of the ionic basis of the action potential</td>
      <td>https://github.com/openworm/hodgkin_huxley_tutorial</td>
    </tr>
    <tr>
      <td>FitzHugh, 1961</td>
      <td>Simplified form of Hodgkin Huxley model</td>
      <td>https://github.com/OpenSourceBrain/FitzHugh-Nagumo</td>
    </tr>
    <tr>
      <td>Prinz et al., 2004</td>
      <td>Pyloric network of the lobster stomatogastric ganglion system</td>
      <td>https://github.com/OpenSourceBrain/PyloricNetwork</td>
    </tr>
    <tr>
      <td>Boyle and Cohen, 2008</td>
      <td>Model of body wall muscle from C. elegans</td>
      <td>https://github.com/openworm/muscle_model</td>
    </tr>
    <tr>
      <td>Gleeson et al., 2018</td>
      <td>A multiscale framework for modeling the nervous system of C. elegans</td>
      <td>https://github.com/openworm/c302</td>
    </tr>
    <tr>
      <td colspan="3">General</td>
    </tr>
    <tr>
      <td>Morris and Lecar, 1981</td>
      <td>Two dimensional reduced neuron model with calcium and potassium conductances</td>
      <td>https://github.com/OpenSourceBrain/MorrisLecarModel</td>
    </tr>
    <tr>
      <td>Hindmarsh and Rose, 1984</td>
      <td>A simplified point cell model which captures complex firing patterns of single neurons, such as periodic and chaotic bursting</td>
      <td>https://github.com/OpenSourceBrain/HindmarshRose1984</td>
    </tr>
    <tr>
      <td colspan="3">Showcases</td>
    </tr>
    <tr>
      <td>NEST Showcase</td>
      <td>Examples of interactions with simulator NEST</td>
      <td>https://github.com/OpenSourceBrain/NESTShowcase</td>
    </tr>
    <tr>
      <td>PyNN Showcase</td>
      <td>Examples of interactions between NeuroML and PyNN</td>
      <td>https://github.com/OpenSourceBrain/PyNNShowcase</td>
    </tr>
    <tr>
      <td>NetPyNE Showcase</td>
      <td>Examples of interactions between NeuroML and NetPyNE</td>
      <td>https://github.com/OpenSourceBrain/NetPyNEShowcase</td>
    </tr>
    <tr>
      <td>SBML Showcase</td>
      <td>Examples of interactions between NeuroML and SBML</td>
      <td>https://github.com/OpenSourceBrain/SBMLShowcase</td>
    </tr>
    <tr>
      <td>Brian Showcase</td>
      <td>Examples of interactions between NeuroML and Brian</td>
      <td>https://github.com/OpenSourceBrain/BrianShowcase</td>
    </tr>
    <tr>
      <td>MOOSE Showcase</td>
      <td>Examples of interactions between NeuroML and MOOSE</td>
      <td>https://github.com/OpenSourceBrain/MOOSEShowcase</td>
    </tr>
    <tr>
      <td>Arbor Showcase</td>
      <td>Examples of interactions between NeuroML and Arbor</td>
      <td>https://github.com/OpenSourceBrain/ArborShowcase</td>
    </tr>
    <tr>
      <td>EDEN Showcase</td>
      <td>Examples of interactions between NeuroML and EDEN</td>
      <td>https://github.com/OpenSourceBrain/EDENShowcase</td>
    </tr>
    <tr>
      <td>The Virtual Brain Showcase</td>
      <td>Examples of interactions between NeuroML and TVB</td>
      <td>https://github.com/OpenSourceBrain/TheVirtualBrainShowcase</td>
    </tr>
    <tr>
      <td>NEURON Showcase</td>
      <td>Examples of interactions between NeuroML and NEURON</td>
      <td>https://github.com/OpenSourceBrain/NEURONShowcase</td>
    </tr>
    <tr>
      <td>neuroConstruct Showcase</td>
      <td>Examples of neuroConstruct projects</td>
      <td>https://github.com/OpenSourceBrain/neuroConstructShowcase</td>
    </tr>
    <tr>
      <td>NeuroMorpho.Org</td>
      <td>Examples of reconstructions from NeuroMorpho.Org</td>
      <td>https://github.com/OpenSourceBrain/NeuroMorpho</td>
    </tr>
    <tr>
      <td>Janelia MouseLight</td>
      <td>Janelia MouseLight project neuronal reconstructions</td>
      <td>https://github.com/OpenSourceBrain/MouseLightShowcase</td>
    </tr>
  </tbody>
</table>

NeuroML-DB aims to promote the uptake of standardized NeuroML models by providing a convenient location for archiving and exploration. It includes advanced database search functions, including ontology-based search (Birgiolas et al., 2015), coupled with pre-computed analyses on models’ electrophysiological and morphological properties, as well as an indication of the relative speed of execution of different models.

NeuroML’s modular nature ensures that models and their components can be easily shared with others through standard code sharing resources. The simplest way of sharing NeuroML models and components is to make their Python descriptions or their XML serializations available through these resources. Indeed, it is straightforward to make Python descriptions or the XML serializations available via different file, code (GitHub, GitLab), model sharing (ModelDB Migliore et al., 2003; McDougal et al., 2017), and archival (Zenodo, Open Science Framework) platforms, just like any other code/data produced in scientific investigations. Complex models with many components, spanning multiple files, such as networks and neuronal models that reference multiple cell and ionic conductance definitions, can also be exported into a COMBINE zip archive (Bergmann et al., 2014), a zip file that includes metadata about its contents. pyNeuroML includes functions to easily create COMBINE archives from NeuroML models and simulations (Figure 6).

OSB is designed so that researchers can share their code on their chosen platform (e.g. GitHub), while retaining full control over write access to their repositories. Afterwards, a page for the model can be created on OSB which lists the latest files present there, with links to OSB visualization/analysis/simulation features which can use the standardized files found in the resource.

NeuroML supports the embedding of structured ontological information in model descriptions (Neal et al., 2019). Models can include NeuroLex (now InterLex) (Larson and Martone, 2013) identifiers for their components (e.g. neuro_lex_id in Figure 6). This links model components to their biological counterparts and makes them more transparent, findable, and reusable. For example, different types of neurons and brain regions have unique ontological ids. A user can use these ids to search for relevant model components on NeuroML-DB. More general information to maintain provenance can also be included in NeuroML models (https://docs.neuroml.org/Userdocs/Provenance.html).

### Reusing NeuroML models

NeuroML models, once openly shared, become community resources that are accessible to all. Researchers can use models shared on NeuroML-DB and OSB without restrictions. Guide 5 in Table 5 provides an example of finding NeuroML-based model components using the API of NeuroML-DB, and creating novel models incorporating these elements.

In addition to these platforms, other experimental data and model dissemination platforms also provide standardized NeuroML versions of relevant models to promote uptake and reuse. For example, NeuroMorpho.org (Ascoli et al., 2007) includes a tool to download NeuroML compliant versions of its cellular reconstructions (https://github.com/NeuroML/Cvapp-NeuroMorpho.org, https://docs.neuroml.org/Userdocs/Software/Tools/SWC.html). NeuroML versions of models released by organizations such as the Blue Brain Project (Markram et al., 2015) (whole cell models as well as ion channel models from Channelpedia Ranjan et al., 2011), the Allen Institute for Brain Science (Billeh et al., 2020), and the OpenWorm project (Gleeson et al., 2018) are also openly available for reuse (Table 8).

NeuroML can also interact with other standards to further promote model re-use. Whereas NeuroML is a declarative standard, PyNN (Davison et al., 2008) is a procedural standard with a Python API for creating network models that can be simulated on multiple simulators. NeuroML models which are within the scope of PyNN can be converted to the PyNN format, and vice-versa. Similarly, NeuroML also interacts with SONATA (Dai et al., 2020) data format by supporting the two way conversion of the network structures of NeuroML models into SONATA. In standards not specific to neuroscience, models from the well established SBML standard (Hucka et al., 2003) can be converted to LEMS (Cannon et al., 2014), for inclusion in neuroscience-related modeling pipelines, and a subset of NeuroML/LEMS models can be exported to SBML, which allows use with simulators and analysis packages compliant to this standard, e.g., Tellurium (Choi et al., 2018). Simulation execution details of NeuroML/LEMS models can also be exported to Simulation Experiment Description Markup Language (SED-ML) (Waltemath et al., 2011), allowing advanced resources such as Biosimulators (Shaikh et al., 2022) (https://biosimulators.org) to feature NeuroML models.

### NeuroML is extensible

While the standard NeuroML elements (Tables 1 and 2) provide a broad range of curated model types for simulation-based investigations, NeuroML can be extended (using LEMS) to incorporate novel model elements and types when they are not (yet) available in the standard.

LEMS is a general purpose model specification language for creating fully machine readable definitions of the structure and behavior of model elements (Cannon et al., 2014). The dynamics of NeuroML elements are described in LEMS. The hierarchical nature of LEMS means that new elements can build on pre-existing elements of the modular NeuroML framework. For example, a novel ionic conductance element can extend the ‘ionChannelHH’ element, which in turn extends ‘baseIonChannel.’ Thus, the new element will be known to the NeuroML elements as depending on an external voltage and producing a conductance, properties that are inherited from ‘baseIonChannel.’ Other elements, such as a cell, can incorporate this new type without needing any other information about its internal workings.

LEMS (and, therefore, NeuroML) element definitions (called ‘ComponentTypes’) specify the dynamical behavior of the model element in terms of a list of yet to be set parameters. Once the generic model behavior is defined, modelers only need to fill in the appropriate values of the required parameters (e.g. conductance density, reversal potential, etc.) to create new instances (called ‘Components’) of the element (see Methods for more details). Users can, therefore create arbitrary, reusable model elements in LEMS, which can be treated the same way as the standard model elements (for an example see Guide 7 in Table 5).

Another major advantage of NeuroML’s use of the LEMS language is its translatability. Since LEMS is fully machine readable, its primitives (e.g. state variables and their dynamics, expressed as ordinary differential equations) can be readily mapped into other languages. As a result, simulator specific code (Blundell et al., 2018) can be generated from NeuroML models and their LEMS extensions (Figure 5), allowing NeuroML to remain simulator-independent while supporting multiple simulation engines.

Newly created elements that may be of interest to the wider research community can be submitted to the NeuroML Editorial Board for inclusion into the standard. The standard, therefore, evolves as new model elements are added and improved versions of the standard and associated software tool chain are regularly released to the community.

### NeuroML is a global open community initiative

NeuroML is a global open community standard that is used and maintained collectively by a diverse set of stakeholders. The NeuroML Scientific Committee (https://docs.neuroml.org/NeuroMLOrg/ScientificCommittee.html) and the elected NeuroML Editorial Board (https://docs.neuroml.org/NeuroMLOrg/Board.html) oversee the standard, the core tools, and the initiative. This ensures that NeuroML supports the myriad of use cases generated by a multi-disciplinary computational modeling community.

NeuroML is an endorsed INCF (Abrams et al., 2022) community standard (Martone and Das, 2019) and is one of the main standards of the international COMBINE initiative (Hucka et al., 2015), which supports the development of other standards in computational biology as well (e.g. SBML (Hucka et al., 2003) and CellML Lloyd et al., 2004). Participation in these organizations guarantees that NeuroML follows current best practices in standardization, and remains linked to and interoperable with other standards wherever possible. The NeuroML community also participates in training and outreach activities such as Google Summer of Code (https://docs.neuroml.org/NeuroMLOrg/OutreachTraining.html), tutorials, and internships under these and other organizations.

The NeuroML community maintains public open communication channels to ensure that all community members can easily participate in troubleshooting, discussions, and development activities. A public mailing list (https://lists.sourceforge.net/lists/listinfo/neuroml-technology) is used for asynchronous communication and announcements while open chat channels on Gitter (now Matrix/Element (#/#NeuroML_community:gitter.im)) provide immediate access to the NeuroML community. All software repositories hosted on GitHub also have issue trackers for software specific queries. A community Code of Conduct (https://docs.neuroml.org/NeuroMLOrg/CoC.html) sets the standards of communication and behavior expected on all community channels.

A crucial aim of NeuroML is to enable Open Science and ensure models in computational neuroscience are FAIR. To this end, all development and discussions related to NeuroML are done publicly. The schema, all core software tools, and relevant resources such as documentation are made freely available under suitable Free/Open Source Software (FOSS) licenses on public platforms. Everyone can, therefore, use, modify, study, and share all NeuroML artifacts without restriction. Users and developers are encouraged to contribute modifications and improvements to the schema and core tools and to participate in the general maintenance and release process.

## Discussion

NeuroMLv2 has matured into a widely adopted community standard for computational neuroscience. Its modular, hierarchical structure can define a wide range of neuronal and circuit model types including simplified representations and those with a high degree of biological detail. The standardized, machine readable format of the NeuroMLv2/LEMS framework provides a flexible, common language for communicating between a wide range of tools and simulators used to create, validate, visualize, analyze, simulate, share, and reuse models. By enabling this interoperability, NeuroMLv2 has spawned a large ecosystem of interacting tools that cover all stages of the model development life cycle, bringing greater coherence to a previously fragmented landscape. Moreover, the modular nature of the model components and hierarchical structure conferred by NeuroMLv2, combined with the flexibility of coding in Python, has created a powerful ‘building block’ approach for constructing standardized models from scratch.

NeuroML has, therefore, evolved from a standardized archiving format into a mature language that supports an ecosystem of tools for the creation and execution of models that support the FAIR principles and promote open, transparent, and reproducible science.

### Evolution of NeuroML and emergence of the NeuroMLv2 tool ecosystem

NeuroML was conceived (Goddard et al., 2001) and developed (Gleeson et al., 2010) as a declarative XML-based framework for defining biophysical models of neurons and networks in a standardized form in order to compare model properties across simulators and to promote transparency and reuse. NeuroML version 1 achieved these aims and was mainly used to archive and visualize existing models (Gleeson et al., 2010). Building on this, the subsequent development of the NeuroMLv2/LEMS framework provided a way to describe models as a hierarchical set of components with dimensional parameters and state variables, so that their structure and dynamics are fully machine readable (Cannon et al., 2014). This enabled models to be losslessly mapped to other representations, greatly promoting interoperability between tools through read-write and automated code generation (Blundell et al., 2018). As NeuroMLv2 matured and became a community standard recognized by the INCF with a formal governance structure, an increasingly wide range of models and modeling tools have been developed or modified to be NeuroMLv2 compliant (Tables 8, 3 and 4). The core tools, maintained directly by the NeuroML developers (Figure 4), provide functionality to read, modify, or create new NeuroML models, as well as to analyze and visualize, and simulate the models. Furthermore, there are now a larger number of tools that have been developed by other members of the community (Figure 3) including a neuronal simulator designed specifically for NeuroMLv2 (Panagiotou et al., 2022). The emergence of an ecosystem of NeuroMLv2 compliant tools enables modelers to build tool chains that span the model life cycle and build and reuse standardized models.

### NeuroML and other standards in computational neuroscience

Several other standards and formats exist to support computational modeling of neuronal systems. Whereas NeuroML is a modular, declarative simulator independent standard for biophysical neuronal modeling, PyNN (Davison et al., 2008) and SONATA (Dai et al., 2020) provide a procedural Python-based simulator independent API and a framework for efficiently handling large-scale network simulations, respectively. Even though there is some overlap in the functionality provided by these standards, they each target distinct use cases and have their own goals and features. The teams developing these standards work in concert to ensure that they remain interoperable with each other, frequently sharing methods and techniques (Dai et al., 2020). This allows researchers to use their standard of choice and easily combine with another if the need arises. PyNN and SONATA are, therefore, integral parts of the wider NeuroML ecosystem.

### Why using NeuroML and Python promotes the construction of FAIR models

The modular and hierarchical structure of NeuroMLv2, when combined with Python, provides a powerful combination of structured declarative elements and flexible procedural approaches that enables a ‘Lego-like’ building block approach for constructing biologically detailed models (Cayco-Gajic et al., 2017; Billings et al., 2014; Kriener et al., 2022; Gurnani and Silver, 2021). This has been advanced by the development of pyNeuroML, which provides a single installable package offering direct access to a range of functionality for handling NeuroML models (Figure 6). Moreover, the web-based documentation of NeuroMLv2, with multiple Python scripts illustrating the usage of the language and associated tools (Table 5), has recently been updated and expanded (https://docs.neuroml.org). This provides a central resource for both new and experienced users of NeuroML supporting its use in model building. As the examples of this resource illustrate, building models using NeuroMLv2 is efficient and intuitive, as the model components are pre-made and how they fit together specified. The structured format allows APIs like libNeuroML to incorporate features such as auto-completion and inline validation of model parameters and structure as scripts are being developed. In addition, automated multi-stage model validation ensures the code, equations and internal structure are validated against the NeuroML schema minimizing human errors and model simulations outputs are within acceptable bounds (Figure 7). The NeuroMLv2 ecosystem also provides convenient ways to visualize and inspect the inner structure of models. pyNeuroML provides Python functions and corresponding command line utilities to view neuronal morphology (Figure 8), neuronal electrophysiology (Figure 10), circuit connectivity and schematics (Figure 9). In addition, custom analysis pipelines and advanced neuroinformatics resources can easily be built using the APIs. For example, loading a NeuroML model of a neuron into OSB enables visualization of the morphology and the spatial distribution of ionic conductance over the membrane as well as inspection of the conductance state variables, while the connectivity and synaptic weight matrices can be automatically displayed for circuit models (Figure 8; Gleeson et al., 2019b). Such features of OSB, which are made possible by the structured format of NeuroMLv2, promote model transparency, reproducibility, and sharing. By enabling the development and sharing of well tested and transparent models the wider NeuroMLv2 ecosystem promotes Open Science.

### Limitations of NeuroML and current work

A limitation of any standardized framework is that there will always be models and model elements that fall outside the current scope of the standard. Although NeuroML suffers from this limitation, the underlying LEMS-based framework provides a flexible route to develop a wide range of new types of physio-chemical models (Cannon et al., 2014). This is relatively straightforward if the new model component, such as a synaptic plasticity mechanism, fits within the existing hierarchical structure of NeuroMLv2 as the new type of synaptic element can build on an existing base synapse type which specifies the relevant input and outputs (e.g. local voltage and synaptic current). For more radical shifts in model types (e.g. neuronal morphologies that grow during learning) that do not fit neatly into the current NeuroMLv2 schema, structural changes to the language would be required. This route is more involved as the pros and cons of changes to the structure of NeuroMLv2 would need to be considered by the Scientific Committee and, if approved, implemented by the Editorial Board.

Whereas the current scope of NeuroMLv2 encompasses models of spiking neurons and networks at different levels of biological detail, plans are in place to extend its scope to include more abstract, rate-based models of neuronal populations (e.g. see Wilson and Cowan, 1972; Mejias et al., 2016 in Table 8). Additionally, work is under way to extend current support for SBML (Hucka et al., 2003) based descriptions of chemical signaling pathways (Cannon et al., 2014), to enable better biochemical descriptions of sub-cellular activity in neurons and synapses.

There is a growing interest in the field for the efficient generation and serialization of large-scale network models, containing numbers of neurons closer to their biological equivalents (Markram et al., 2015; Billeh et al., 2020; Einevoll et al., 2019). While a multitude of applications in the NeuroML ecosystem support large-scale model generation (e.g. NetPyNE, neuroConstruct, PyNN), the default serialization of NeuroML (XML) is inefficient for reading/writing/storing such extensive descriptions. NeuroML does have an internal format for serializing in the binary format HDF5 (see Methods), but has also recently added support for export of models to the SONATA data format (Dai et al., 2020) allowing efficient serialization of large-scale models. Even though individual instances of large-scale models are useful, the ability to generate families of these for multiple simulation runs and more particularly a way to encapsulate, examine and reuse templates for network models, is also required. A prototype package, NeuroMLlite (https://github.com/NeuroML/NeuroMLlite), has been developed which allows these concise network templates to be described and multiple instances of networks to be generated, and facilitates interaction with simulation platforms and efficient serialization formats.

As discoveries and insights in neuroscience inform machine learning and visa versa, there is an increasing need to develop a common framework for describing both biological and artificial neural networks. Model Description Format (MDF) has been developed to address this (Gleeson et al., 2023). This initiative has developed a standardized format, along with a Python API, which allows the specification of artificial neural networks (e.g. Convolutional Neural Networks, Recurrent Neural Networks) and biological neurons using the same underlying entities. Support for mapping MDF to/from NeuroMLv2/LEMS has been included from the start. This work will enable deeper integration of computational neuroscience and ‘brain-inspired’ networks in Artificial Intelligence (AI).

### Conclusion and vision for the future

NeuroMLv2 is already a mature community standard that provides a framework for standardizing biologically detailed neuronal network models. By providing a stable, common framework defining the essential entities required for biologically detailed neuronal modeling, NeuroML has spawned an ecosystem of tools that span all stages of the model development life cycle. In the short term, we envision the functionality of NeuroML to expand further and for new online resources that encourage the construction of FAIR models using pyNeuroML to be taken up by the community. The NeuroML development team are also beginning to explore how to combine NeuroML-based circuit models with musculo-skeletal simulations to enable models of the neural control of behavior. In the longer term, developing seamless interfaces between NeuroML and other domain specific standards will enable the development of more holistic models of the neural control of body systems across a wide range of organisms, as well as greater exchange of models and insights between computational neuroscience and AI.

## Materials and methods

NeuroMLv2 is formally specified by the NeuroMLv2 XML schema, which defines the allowed structure of XML files which comply to the standard, and the LEMS ComponentType definitions, which define the internal state variables of the underlying elements, providing a machine-readable specification of the time evolution of model components. The specification is backed up by a suite of software tools that support the model life cycle and the accompanying usage and development documentation.

We illustrate the key parts of this framework using the HindmarshRose cell model (Hindmarsh and Rose, 1984; Figure 11), which as an abstract point neuron model, serves as an appropriate simple NeuroMLv2 ComponentType.

![Figure 11.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig11-v1.jpg)

**Figure 11.:** (a) XML serialization of the model description containing the main hindmarshRose1984Cell element with a set of parameters which result in regular bursting. A current clamp stimulus is applied using a pulseGenerator, and a population of one cell is added with this in a network. This XML can be validated against the NeuroML Schema. (b) Membrane potentials generated from a simulation of the model in (a). The LEMS simulation file to execute this is shown in Figure 15. The code used in this example is available here: https://github.com/OpenSourceBrain/HindmarshRose1984/tree/master/NeuroML2/examples.

### The NeuroML XML Schema

We begin with the NeuroMLv2 standard. The standard consists of two parts, each serving different functions:

The NeuroMLv2 schema is a language independent data model that constrains the structure of a NeuroMLv2 model description. The NeuroML schema is formally described as an XML Schema document (https://neuroml.org/schema/neuroml2) in the XML Schema Definition (XSD) format, a recommendation of the World Wide Web Consortium (W3C) (https://www.w3.org/TR/xmlschema-1/). An XML document that claims to conform to a particular schema can be validated against the schema. All NeuroMLv2 model descriptions can, therefore, be validated against the NeuroMLv2 schema.

The basic building blocks of an XSD schema are ‘simple’ or ‘complex’ types and their ‘attributes.’ All types are created as ‘extensions’ or ‘restrictions’ of other types. Complex types may contain other types and attributes whereas simple types may not. Figure 12 shows some example types defined in the NeuroMLv2 schema. For example, the Nml2Quantity_none simple type restricts the in-built ‘string’ type using a regular expression ‘pattern’ that limits what string values it can contain. The type is Nml2Quantity_none is to be used for unit-less quantities (e.g. 3, 6.7, –1.1e-5) and the restriction pattern for translates to ‘a string that may start with a hyphen (negative sign), followed by any number of numerical characters (potentially containing a decimal point) and a string containing capital or small ‘e’ (to specify the exponent).’ The restriction pattern for the Nml2Quantity_voltage type is similar, but must be followed by a ‘V’ or ‘mV.’ In this way, the restriction ensures that a value of type ‘Nml2Quantity_voltage’ represents a physical voltage quantity with units ‘V’ (volt) or ‘mV’ (millivolt). Furthermore, a NeuroMLv2 model description that uses a voltage value that does not match this pattern, for example ‘0.5 s,’ will be invalid.

![Figure 12.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig12-v1.jpg)

**Figure 12.:** Top: ‘simple’ types may not include other elements or attributes. Here, the Nml2Quantity_none and Nml2Quantity_voltage types define restrictions on the default string type to limit what strings can be used as valid values for attributes of these types. Bottom: example of a ‘complex’ type, the HindmarshRose cell model (Hindmarsh and Rose, 1984), that can also include other elements of other types, and extend other types.

The example of a complex type in Figure 12 is the HindmarshRose1984Cell type that extends the BaseCellMembPotCap complex type (the base type for any cell producing a membrane potential v with a capacitance parameter C), and defines new ‘required’ (compulsory) attributes. These attributes are of simple types—these are all unit-less quantities apart from v_scaling, which has dimension voltage. Note that inherited attributes are not re-listed in the complex type definition—the compulsory capacitance attribute, C, is inherited here from BaseCellMembPotCap.

The NeuroMLv2 schema serves multiple critical functions. A variety of tools and libraries support the validation of files against XSD schema definitions. Therefore, the NeuroMLv2 schema enables the validation of model descriptions—model structure, parameters, parameter values and their units, cardinality, element positioning in the model hierarchy (level 1 validation in Figure 7)—prior to simulation. XSD schema definitions, as language independent data models, also allow the generation of APIs in different languages. More information on how APIs in different languages are generated using the NeuroMLv2 XSD schema definition is provided in later sections.

The NeuroMLv2 XSD schema is also released and maintained as a versioned artifact, similar to the software packages. The current version is 2.3, and can be found in the NeuroML2 repository on GitHub (https://github.com/NeuroML/NeuroML2/tree/master/Schemas/NeuroML2).

### LEMS ComponentType definitions

The second part of the NeuroMLv2 standard consists of the corresponding LEMS ComponentType definitions. Whereas the XSD Schema describes the structure of a NeuroMLv2 model description, the LEMS ComponentType definitions formally describe the dynamics of the model elements.

LEMS (Cannon et al., 2014) is a domain independent general purpose machine-readable language for describing models and their simulations. A complete description of LEMS is provided in Cannon et al., 2014 and in our documentation (https://docs.neuroml.org/Userdocs/LEMSSchema.html). Here, we limit ourselves to a short summary necessary for understanding the NeuroMLv2 ComponentType definitions.

LEMS allows the definition of new model types called ComponentTypes. These are formal descriptions of how a generic model element of that type behaves (the ‘dynamics’), independent of the specific set of parameters in any instance. To describe the dynamics, such descriptions must list any necessary parameters that are required, as well as the time-varying state variables. The dimensions of these parameters and state variables must be specified, and any expressions involving them must be dimensionally consistent. An instance of such a generic model is termed a Component and can be instantiated from a ComponentType by providing the necessary parameters. One can think of ComponentTypes as user defined data types similar to ‘classes’ in many programming languages and Components as ‘objects’ of these types with particular sets of parameters. Types in LEMS can also extend other types, enabling the construction of a hierarchical library of types. In addition, since LEMS is designed for model simulation, ComponentType definitions also include other simulation-related features such as Exposures, specifying quantities that may be accessed/recorded by users.

For model elements included in the NeuroML standard, there is a one-to-one mapping between types specified in the NeuroML XSD schema and LEMS ComponentTypes, with the same parameters specified in each. The addition of new model elements to the NeuroML standard, therefore, requires the addition of new type definitions to both the XSD schema and the LEMS definitions. New user defined ComponentTypes, nevertheless, can be defined in LEMS and used freely in models, and these do not need to be added to the standard before use. The only limitation here is that new user defined ComponentTypes cannot be validated against the NeuroML schema since their type definitions will not be included there.

Figure 13 shows the ComponentType definition for the HindmarshRose1984Cell model element. Here, the HindmarshRose1984Cell ComponentType extends baseCellMembPotCap and inherits its elements. The ComponentType includes parameters that users must provide when creating a new instance (component): $a, b, c, d, r, v, x1, v_scaling$.

![Figure 13.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig13-v1.jpg)

Other parameters, $x0$, $y0$, and $z0$ are used to initialize the three state variables of the model, $x,y,z$. x is the proxy for the membrane potential of the cell used in the original formulation of the model (Hindmarsh and Rose, 1984) and is here scaled by a factor $v_scaled$ to expose a more physiological value for the membrane potential of the cell in StateVariable $v$. A Constant, $MSEC$, is defined to hold the value of $1 ms$ for use in the ComponentType. Next, an Attachment enables the addition of entities that would provide external inputs to the ComponentType. Here, synapses are Attachments of the type basePointCurrent and provide synaptic current input to this ComponentType.

The Dynamics block lists the mathematical formalism required to simulate the ComponentType. By default, variables defined in the Dynamics block are private, i.e., they are not visible outside the ComponentType. To make these visible to other ComponentTypes and to allow users to record them, they must be connected to Exposures. Exposures for this ComponentType include the three state variables and also the internal derived variables, which while not used by other components, are useful in inspecting the ComponentType and its dynamics. An extra exposure, $spiking$, is added to allow other NeuroML components access to the spiking state of the cell that will be determined in the Dynamics block.

StateVariable definitions are followed by DerivedVariables, variables whose values depend on other variables but are not time derivatives (which are handled separately in TimeDerivative blocks (below)). The total synaptic current, $iSyn$, is a summation of all the synaptic currents, $i$ received by the synapses that may be attached on to this ComponentType. The synapse[*]/i value of the select field tells LEMS to collect all the i exposures from any synapses Attachments, and the add value of the reduce field tells LEMS to sum the multiple values. As noted, $x$ is a scaled version of the membrane potential variable, $v$. This is followed by the three derived variables, $phi$, $chi$, $rho$ where:

$$
phi=y−ax^{3}+bx^{2}
$$



$$
chi=c−dx^{2}−y
$$



$$
rho=s(x−x1)−z
$$

The total membrane potential of the cell, $iMemb$, is calculated as the sum of the capacitive current and the synaptic current:

$$
iMemb=\frac{C(v_scaling(phi−z))}{MSEC}+iSyn
$$

$v,y,z$ are TimeDerivatives, with the ‘value’ representing the rate of change of each variable:

$$
dv/dt=iMemb/C
$$



$$
dy/dt=chi/MSEC
$$



$$
dz/dt=(r\timesrho)/MSEC
$$

The final few blocks set the initial state of the component (OnStart),

$$
v=x0\timesv_scaling
$$



$$
y=y0
$$



$$
z=z0
$$

and define conditional expressions to set the spiking state of the cell:

$$
spiking={1if (v>0)∧(spiking<0.5)0if (v<0)
$$

Both the XSD schema and the LEMS ComponentType definitions enable model validation. However, despite some overlap, they support different types of validation. Whereas the XSD schema allows for the validation of model descriptions (e.g. the XML files), the LEMS ComponentType definitions enable validation of model instances, i.e., the ‘runnable’ instances of models that are constructed once components have been created by instantiating ComponentTypes with the necessary parameters, and various attachments created between source and target components. A model description may be used to create many different model instances for simulation. Indeed, it is common practice to run models that include stochasticity with different seeds for random number generators to verify the robustness of simulation results. Thus, the validation of dimensions and units that LEMS carries out is done only after a runnable instance of a model has been created.

The LEMS ComponentType definitions for NeuroMLv2 are also maintained as versioned files that are updated along with the XSD schema. These can also be seen in the NeuroMLv2 GitHub repository (https://github.com/NeuroML/NeuroML2/tree/master/NeuroML2CoreTypes). An index of the ComponentTypes included in version 2.3 of the NeuroML standard, with links to online documentation, is also provided in Tables 1 and 2.

### NeuroML APIs

The NeuroMLv2 software stack relies on the NeuroML APIs that provide functionality to read, write, validate, and inspect NeuroML models. The APIs are programmatically generated from the machine readable XSD schema, thus ensuring that the class for defining a specific NeuroML element in a given language (e.g. Java) has the correct set of fields with the appropriate type (e.g. float or string) corresponding to the allowed parameters in the corresponding NeuroML element. NeuroMLv2 currently provides APIs in numerous languages—Python (libNeuroML which is generated via generateDS (http://www.davekuhlman.org/generateDS.html)), Java (org.neuroml.model via JAXB XJC (https://javaee.github.io/jaxb-v2/)), C++ (NeuroML_CPP via XSD (https://www.codesynthesis.com/products/xsd/)) and MATLAB (NeuroMLToolbox which accesses the Java API from MATLAB), and APIs for other languages can also be easily generated as required. LEMS is also supported by a similar set of APIs—PyLEMS in Python, and jLEMS in Java—and since a NeuroMLv2 model description is a set of LEMS Components, the LEMS APIs also support them (e.g. the hindmarshRose1984Cell example in Figure 11 could be loaded by jLEMS and treated as a LEMS Component).

Figure 14 shows the use of the NeuroML Python API to describe a model with one HindmarshRose cell. In Python, the instances of ComponentTypes, their Components, are represented as Python objects. The hr0 Python variable stores the created HindmarshRose1984Cell component/object. This is added to a Population pop0 in the Network net. The network also includes a PulseGenerator with amplitude 5 nA as an ExplicitInput that is targeted at the cell in the population. The model description is serialized to XML (Figure 11) and validated. Note that as the standard convention for classes in Python is to use capitalized names, HindmarshRose1984Cell is used in Python but is serialized as <hindmarshRose1984Cell>in the XML. Users can either share the Python script itself or share the XML serialization. Any valid XML serialization can be also loaded into a Python object model and modified.

![Figure 14.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig14-v1.jpg)

**Figure 14.:** This script generates the XML in Figure 11. The code used in this example is available here: https://github.com/OpenSourceBrain/HindmarshRose1984/tree/master/NeuroML2/examples.

XML is the default serialization of NeuroML and all existing APIs can read and write the format (and it should be seen as a minimal requirement for new APIs to support XML). There is, however, an alternative HDF5 (https://www.hdfgroup.org/solutions/hdf5) based serialization of NeuroML files which is supported by both libNeuroML and the Java API, org.neuroml.model (https://docs.neuroml.org/Userdocs/HDF5.html). This format is based on an efficient representation of cell positions and connectivity data as HDF5 data sets which can be serialized in compact binary format and loaded into memory for optimized access (e.g. as numpy arrays in libNeuroML). This reduces the size of the saved files for large-scale networks and speeds up loading/writing models eliminating the need to parse/generate large text files containing XML. Models serialized in this format can be loaded and transformed to simulator code in the same way as XML-based models by the Java and Python APIs.

### Simulating NeuroML models

The model description shown in Figure 11 contains no information about how it is to be simulated, or on the dynamics of each model component. Providing this simulation information and linking in the ComponentType definition requires creating a LEMS file to fully specify the simulation. Figure 15 shows the use of utilities included in the Python pyNeuroML package to describe a LEMS simulation of the HindmarshRose model defined in Figure 11. The LEMSSimulation object includes simulation specific information such as the duration of the simulation, the integration time step, and the seed value. It also allows the specification of files for the storage of data recorded from the simulation. In this example, we record the membrane potential, $v$, of our cell in its population, HRPop0[0]. Similar to the NeuroMLv2 model description, the simulation object can also be serialized to XML for storage and sharing (Figure 15, bottom).

![Figure 15.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig15-v1.jpg)

**Figure 15.:** The code used in this example is available here: https://github.com/OpenSourceBrain/HindmarshRose1984/tree/master/NeuroML2/examples.

As noted previously, NeuroML/LEMS model and simulation descriptions are machine readable and simulator independent and can be simulated by simulation engines using a multitude of strategies (Figure 5).

The first category of tools consists of the reference NeuroML and LEMS simulation engines. These work directly with NeuroML and LEMS as their base descriptions of modeling entities and do not have their own specific formats. They are maintained by the NeuroML Editorial Board—jLEMS, jNeuroML, and PyLEMS (Figure 4). jLEMS serves as the reference implementation for the LEMS language and as such it can simulate any model described in LEMS (not necessarily from neuroscience). When coupled with the LEMS definitions of NeuroML standard entity structure/dynamics, it can simulate most NeuroML models, though it does not currently support multi-compartmental neurons. jNeuroML bundles the NeuroML standard LEMS definitions, jLEMS, and other functionality into a single package for ease of installation/usage. There is also a pure Python implementation of a LEMS interpreter, PyLEMS, which can be used in a similar way to jLEMS. The pyNeuroML package encapsulates all of these tools to give easy access (at both command line and in Python) to all of their functionality (Figure 6).

The second category consists of other simulators which support NeuroML natively. The EDEN simulator is an independently developed tool that was designed from its inception to read NeuroML and LEMS models for efficient, parallel simulation (Panagiotou et al., 2022).

The third category involves simulators which have their own internal formats and include methods to translate NeuroMLv2/LEMS models to their own formats. Examples include NetPyNE (Dura-Bernal et al., 2019), MOOSE (Ray and Bhalla, 2008), and N2A (Rothganger et al., 2014).

The fourth category comprises tools for which the NeuroML tools generate simulator specific scripts. The simulation engines then execute these scripts, similar to how they would execute handwritten user scripts. These include NEURON (Hines and Carnevale, 1997) for which the NeuroML tools generate scripts in Python and the simulator’s hoc and NMODL formats and the Brian simulator (Stimberg et al., 2019) which uses Python scripts.

The final category consists of export options to standardized formats in neuroscience and the wider computational biology field, which enable interaction with simulators and applications supporting those formats. These include the PyNN package (Davison et al., 2008), which can be run in either NEURON, NEST (Gewaltig and Diesmann, 2007) or Brian, the SONATA data format (Dai et al., 2020) and the SBML standard (Hucka et al., 2003) (see Reusing NeuroML models for more details).

Having multiple strategies in place for supporting NeuroML gives more freedom to simulator developers to choose how much they wish to be involved with implementing and supporting NeuroML functionality in their applications, while maximizing the options available for end users.

The primary tool for simulating NeuroML/LEMS models via different engines is jNeuroML, which is included in pyNeuroML. jNeuroML supports all simulator engine categories (Figure 5). It includes jLEMS for simulation of LEMS and single compartmental NeuroML models. It can also pass simulations to the EDEN simulator (Panagiotou et al., 2022) for direct simulation. Using the org.neuroml.export library (https://github.com/NeuroML/org.neuroml.export), jNeuroML can also generate import scripts for simulators (e.g. NetPyNE Dura-Bernal et al., 2019) or convert NeuroML/LEMS models to simulator specific formats (e.g. NEURON Hines and Carnevale, 1997). Supporting a new simulation engine that requires translation of NeuroML/LEMS into another format can be done by adding a new ‘writer’ to the org.neuroml.export library. Finally, jNeuroML also includes the org.neuroml.import (https://github.com/NeuroML/jNeuroML) library that converts from other formats (e.g. SBML Hucka et al., 2003) to LEMS for combination with NeuroML models.

It is important to note though that not all NeuroML models can be exported to/are supported by each of these target simulators (Table 7). This depends on the capabilities of the simulator in question (whether it supports networks, or morphologically detailed cells) and pyNeuroML/jNeuroML will provide feedback if a feature of the model is not supported in a chosen environment.

All NeuroML and LEMS software packages are made available under FOSS licenses. The source code for all NeuroML packages and the standard can be obtained from the NeuroML GitHub organization (https://github.com/NeuroML). The NeuroML Python API (https://github.com/NeuralEnsemble/libNeuroML) was developed in collaboration with the NeuralEnsemble initiative (https://github.com/NeuralEnsemble/), which also maintains other commonly used Python packages such as PyNN (Davison et al., 2008), Neo (Garcia et al., 2014) and Elephant (Denker, 2018). LEMS packages are available from the LEMS GitHub organization (https://github.com/LEMS).

To ensure replication and reproduction of studies, it is important to note the exact versions of software used in studies. For NeuroML and LEMS packages, archives of each release along with citations are published on Zenodo (https://zenodo.org) to enable researchers to cite them in their work (Gleeson, 2021; Gleeson, 2024a; Gleeson et al., 2019b; Gleeson, 2024b; Sinha, 2024).

### Documentation

A standard and its accompanying software ecosystem must be supported by comprehensive documentation if it is to be of use to the research community. The primary NeuroML documentation for users that accompanies this paper has been consolidated into a JupyterBook (Executable Books Community, 2020) at https://docs.neuroml.org. This includes explanations of NeuroML and computational modeling concepts, interactive tutorials with varying levels of complexity, information about tools and what functions they provide to support different stages of the model life cycle. The JupyterBook framework supports ‘executable’ documentation through the inclusion of interactive Jupyter notebooks which may be run in the users’ web browser on free services such as OSBv2, Binder.org (https://mybinder.org/) and Google Colab (https://colab.research.google.com/). Finally, the machine readable nature of the schema and LEMS also enables the automated generation of human readable documentation for the standard and low level APIs (Figure 16) along with their examples (https://docs.neuroml.org/Userdocs/Schemas/Cells.html#hindmarshrose1984cell). In addition, the individual NeuroML software packages each have their own individual documentation (e.g. pyNeuroML (https://pyneuroml.readthedocs.io/en/stable/,) libNeuroML (https://libneuroml.readthedocs.io/en/stable/)).

![Figure 16.](https://cdn.elifesciences.org/articles/95135/elife-95135-fig16-v1.jpg)

**Figure 16.:** More information about the ComponentType can be obtained from the tabs provided.

As with the rest of the NeuroML ecosystem, the documentation is hosted on GitHub (https://github.com/NeuroML/Documentation), licensed under a FOSS license, and community contributions to it are welcomed. A PDF version of the documentation can also be downloaded for offline use (https://docs.neuroml.org/_static/files/neuroml-documentation.pdf).

### Maintenance of the Schema and core software

The NeuroML Scientific Committee (https://docs.neuroml.org/NeuroMLOrg/ScientificCommittee.html) and the elected NeuroML Editorial Board (https://docs.neuroml.org/NeuroMLOrg/Board.html) oversee the standard, the core tools, and the initiative. The Scientific Committee sets the scientific focus of the NeuroML initiative. It ensures that the standard represents the state of the art—that it can encapsulate the latest knowledge in neuronal anatomy and physiology in their corresponding model components. The Scientific Committee also defines the governance structure of the initiative and works with the wider scientific community to gather feedback on NeuroML and promote its use. The Editorial Board manages the day-to-day development and maintenance of LEMS, the NeuroML schema, the core software tools, and critical resources such as the documentation. The Editorial Board works with simulator developers in the extended ecosystem to help make tools NeuroML compliant by testing reference implementations and answering technical queries about NeuroML and the core software tools.

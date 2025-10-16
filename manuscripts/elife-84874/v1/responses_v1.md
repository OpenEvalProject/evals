# Author response - Round 1

Authors:
- M Elise Lauterbur ([ORCID: 0000-0002-7362-3618](https://orcid.org/0000-0002-7362-3618))
- Maria Izabel A Cavassim ([ORCID: 0000-0001-9726-1431](https://orcid.org/0000-0001-9726-1431))
- Ariella L Gladstein ([ORCID: 0000-0001-7735-2336](https://orcid.org/0000-0001-7735-2336))
- Graham Gower ([ORCID: 0000-0002-6197-3872](https://orcid.org/0000-0002-6197-3872))
- Nathaniel S Pope
- Georgia Tsambos ([ORCID: 0000-0001-7001-2275](https://orcid.org/0000-0001-7001-2275))
- Jeffrey Adrion ([ORCID: 0000-0003-1021-6000](https://orcid.org/0000-0003-1021-6000))
- Saurabh Belsare ([ORCID: 0000-0002-8148-1867](https://orcid.org/0000-0002-8148-1867))
- Arjun Biddanda ([ORCID: 0000-0003-1861-1523](https://orcid.org/0000-0003-1861-1523))
- Victoria Caudill ([ORCID: 0000-0002-0577-5513](https://orcid.org/0000-0002-0577-5513))
- Jean Cury
- Ignacio Echevarria
- Benjamin C Haller ([ORCID: 0000-0003-1874-8327](https://orcid.org/0000-0003-1874-8327))
- Ahmed R Hasan ([ORCID: 0000-0003-0002-8399](https://orcid.org/0000-0003-0002-8399))
- Xin Huang
- Leonardo Nicola Martin Iasi
- Ekaterina Noskova ([ORCID: 0000-0003-1168-0497](https://orcid.org/0000-0003-1168-0497))
- Jana Obsteter
- Vitor Antonio Correa Pavinato ([ORCID: 0000-0003-2483-1207](https://orcid.org/0000-0003-2483-1207))
- Alice Pearson
- David Peede
- Manolo F Perez
- Murillo F Rodrigues
- Chris CR Smith
- Jeffrey P Spence ([ORCID: 0000-0002-3199-1447](https://orcid.org/0000-0002-3199-1447))
- Anastasia Teterina
- Silas Tittes ([ORCID: 0000-0003-4697-7434](https://orcid.org/0000-0003-4697-7434))
- Per Unneberg
- Juan Manuel Vazquez ([ORCID: 0000-0001-8341-2390](https://orcid.org/0000-0001-8341-2390))
- Ryan K Waples
- Anthony Wilder Wohns
- Yan Wong ([ORCID: 0000-0002-3536-6411](https://orcid.org/0000-0002-3536-6411))
- Franz Baumdicker
- Reed A Cartwright ([ORCID: 0000-0002-0837-9380](https://orcid.org/0000-0002-0837-9380))
- Gregor Gorjanc
- Ryan N Gutenkunst ([ORCID: 0000-0002-8659-0579](https://orcid.org/0000-0002-8659-0579))
- Jerome Kelleher ([ORCID: 0000-0002-7894-5253](https://orcid.org/0000-0002-7894-5253))
- Andrew D Kern ([ORCID: 0000-0003-4381-4680](https://orcid.org/0000-0003-4381-4680))
- Aaron P Ragsdale
- Peter L Ralph ([ORCID: 0000-0002-9459-6866](https://orcid.org/0000-0002-9459-6866))
- Daniel R Schrider ([ORCID: 0000-0001-5249-4151](https://orcid.org/0000-0001-5249-4151))
- Ilan Gronau ([ORCID: 0000-0001-8536-4062](https://orcid.org/0000-0001-8536-4062))

## Response text

DOI: [10.7554/eLife.84874.3.sa4](https://doi.org/10.7554/eLife.84874.3.sa4)

The following is the authors' response to the original reviews.

We are very glad that the editor and reviewers found our paper of broad interest to the community of population, evolutionary, and ecological genetics. We thank them for their positive feedback and insightful comments and suggestions. We have revised our manuscript to address some of the issues raised by the review. The main change we made was providing a detailed discussion of limitations of simulated genomes, focusing on considerations one needs to make when selecting a demographic model. This can be found in a new section “Limitations of simulated genomes” (pages 9-10). We made a few additional adjustments in other parts of the text based on the reviewers’ suggestions. They are all listed in the detailed point-by-point response to reviewers comments and questions below.

Editor:

It was noted that demographic models (or genomic parameters) that are inferred based on certain aspects of the genomic data (eg., site frequency spectrum, haplotype structure) may not recapitulate other aspects of the data. In other words, any inferred demographic models are expected to reliably reproduce only some aspects of the genetic variation data but not necessarily all. It would be helpful to emphasize this limitation in the manuscript and to include a table summarizing the types of variation that the demographic models for the catalogued species were based on.

This is a very important point, which we addressed in the revision by adding a section entitled “Limitations of simulated genomes”. This section discusses the considerations that one should make when selecting an inferred demographic model to implement in simulation. This includes the samples used in analysis, the method used for inference, as well as various filters. In this section we also point to the documentation page of the stdpopsim catalog, which provides information about each demographic model that can help users decide whether it is appropriate for their needs. We decided not to summarize this information in a succinct table in the manuscript because it is not straightforward to summarize the strengths and potential limitations of each model in a table. Instead, we will expand the summary provided for each demographic model in the documentation page to provide additional information. See response to the second reviewer’s comment on this topic for more details.

2. It will make stdpopsim more user-friendly to include an automated module that can visualize a demographic model given the corresponding parameters (or simulation scripts).

As mentioned in the response to the first reviewer’s comment on this subject, the documentation page of the stdpopsim catalog provides a brief summary for each demographic model, including a graphical representation. See response below for more details.

Reviewer #1:

In the introduction, the authors cite numerous efforts to generate high-quality reference genomes. That's not an issue in itself, but leading with this might send the message to some readers that it is these reference genome efforts that are driving the need for population genomics analysis and simulation tools, which is not really the case - why not instead give some citation attention to actual population genomics projects aiming to address the types of evolutionary questions this paper is concerned with? The reference genome citations would fit better in the section dealing with reference genomes, where they already appear.

Indeed, the desire to answer complex evolutionary questions is the main motivation for sequencing these genomes and also for generating realistic genome simulations. The reason we chose to lead with the genome-sequencing efforts is that high quality genome data is an important prerequisite for obtaining parameters for chromosome-scale simulations. So, with that perspective, these efforts which we cite are the driving force behind expansion of stdpopsim in the near future. Thus, we decided to leave these citations in the introduction. To balance things out, we now start the introduction with a statement about board questions in population genetics. Moreover, after we list the genome sequencing efforts, we added a list of specific types of questions that can be addressed by these newly emerging genomes, with relevant citations. The beginning of the introduction now reads:

“Population genetics allows us to answer questions across scales from deep evolutionary time to ongoing ecological dynamics, and dramatic reductions in sequencing costs enable the generation of unprecedented amounts of genomic data that can be used to address these questions (Ellegren, 2014). Ongoing efforts to systematically sequence life on Earth by initiatives such as the Earth Biogenome (Lewin et al., 2022) and its affiliated project networks, such as Vertebrate Genomes (Rhie et al., 2021), 10,000 Plants (Cheng et al., 2018) and others (Darwin Tree of Life Project Consortium, 2022), are providing the backbone for enormous increases in the amount of population-level genomic data available for model and non-model species. These data are being used, among other things, in inference of population history and demographic parameters (Beichman et al., 2018), studying adaptive introgression (Gower et al., 2021), distinguishing adaptation from drift (e.g. Hsieh et al., 2021), and understanding the implications of deleterious variation in populations of conservation concern (e.g. Robinson et al., 2023).”

Something that would be useful for the stdpopsim resource in general, though not necessarily something for the paper, would be some kind of more human-friendly representation of the demographic models implemented in the curated library. Perhaps I'm not looking in the right place, but as far as I can tell, if I want to study the curated demographic models, I need to go into the Python scripts on the stdpopsim GitHub page (e.g. https://github.com/popsim-consortium/stdpopsim/tree/main/stdpopsim/catalog/BosTau). Here the various parameters and demographic events are hard-coded into the scripts. To understand the model being implemented, one thus needs to go dig into these scripts - something which is not necessarily very accessible to all researchers. Visual representations, such as the one for Anopheles gambiae in Fig 2. in the paper, are more widely accessible. I wonder if such figures could be produced for all the curated models and included in the GitHub folders alongside the scripts, perhaps aided by an existing model visualization software such as POPdemog. Again, I would not suggest that this is necessary for the paper, but if practically feasible I think it would be a useful addition to the resource in the longer term.

This is a very good point. The stdpopsim catalog actually has a documentation page that provides a brief summary for each demographic model, including a graphical representation. This graphical representation is generated using demesdraw applied to the demographic model object implemented in the code. Thus, potential users do not have to dig through the Python code to figure out the details of the demographic model. We used a similar approach to generate the image of the demographic history of A. gambiae for Fig. 2 of the paper. The documentation page is an important part of the stdpopsim catalog, and we now added a link to it in section “Data availability”, and we mention it in key places in the manuscript, such as the caption of Fig 2.

Reviewer #2:

An important update to the stdpopsim software is the capacity for researchers to annotate coding regions of the genome, permitting distributions of fitness effects and linked selection to be modeled. However, though this novel feature expands the breadth of processes that can be evaluated as well as is applicable to all species within the stdpopsim framework, the authors do not provide significant detail regarding this feature, stating that they will provide more details about it in a forthcoming publication. Compared to this feature, the additions of extra species, finite-site substitution models, and non-crossover recombination are more specialized updates to the software.

It would be helpful to provide additional information regarding the coding annotation (and associated distribution of fitness effects and linked selection) that is implemented in the current version of stdpopsim, but will be detailed in a forthcoming paper. This is not to take away from the forthcoming paper, but I believe this is the most important update to the software, and the current manuscript only brushes over it.

We agree that implementation of selection in simulations is a significant addition to stdpopsim. However, our intention in this manuscript is to focus on the separate effort we made in the last two years to expand the utility of stdpopsim to a more diverse set of species. We think the manuscript stands firmly even without discussing in detail the new features that allow modeling selection. The main reason we briefly mention these features in sections “Additions to stdpopsim” and “Basic setup for chromosome-level simulations” is because the released version of stdpopsim contains implemented DFEs for a few species, and we did not want to completely ignore this. We thus added a brief comment at the end of the “Basic setup” section (page 8) mentioning the three model species for which the stdpopsim catalog currently has annotations and implemented DFE models. We think that a more detailed description of how these features and how they should be used is best left to the manuscript that the PopSim community is currently writing (preprint expected later this year).

When it comes to simulating realistic genomic data, the authors clearly lay out that parameters obtained from the literature must be compatible, such as the same recombination and mutation rates used to infer a demographic history should also be used within stdpopsim if employing that demographic history for simulation. This is a highly important point, which is often overlooked. However, it is also important that readers understand that depending on the method used to estimate the demographic history, different demographic models within stdpopsim may not reproduce certain patterns of genetic variation well. The authors do touch on this a bit, providing the example that a constant size demographic history will be unable to capture variation expected from recent size changes (e.g., excess of low-frequency alleles). However, depending on the data used to estimate a demographic history, certain types of variation may be unreliably modeled (Biechman et al. 2017; G3, 7:3605-3620). For example, if a site frequency spectrum method was used to estimate a demographic history, then the simulations under this model from y stdpopsim may not recapitulate the haplotype structure well in the observed species. Similarly, if a method such as PSMC applied to a single diploid genome was used to estimate a demographic history, then the simulations under this model from stdpopsim may not recapitulate the site frequency spectrum well in the observed species. Though the authors indicate that citations are given to each demographic model and model parameter for each species, this may not be sufficient for a novice researcher in this field to understand what forms of genomic variation the models may be capable of reliably producing. A potential worry is that the inclusion of a species within stdpopsim may serve as an endorsement to users regarding the available simulation models (though I understand this is not the case by the authors), and it would be helpful if users and readers were guided on the type of variation the models should be able to reliably reproduce for each species and demographic history available for each species. It would be helpful to include a table with types of observed variation that the current set of 21 species (and associated demographic histories) are likely and unlikely to recapitulate well.

This is a very important point, which we now address in the section “Limitations of simulated genomes”, which we added to the manuscript. In this section, we expand on this topic and discuss various things that will affect the way simulated genomes reflect true sequence variation. This includes the choice of demographic inference method, but also the analyzed samples, and various filters. The main message of this section is that one should consider various things when deciding to implement a demographic model in simulation (or selecting a model among those implemented in stdpopsim). We also cite studies (including Beichman, et al. 2017), which compared different approaches to demography inference. However, we note that the conclusions of these comparisons are not as straightforward as the reviewer suggests. In particular, methods that make use of the site frequency spectrum (such as dadi) should be able to capture some aspects of haplotype structure, because this information is encoded in the demographic history. Furthermore, a demographic history inferred from a single genome (e.g., using PSMC) should do a reasonable job approximating some aspects of the site frequency spectrum. In other words, the aspects of genetic variation not modeled well by a given demographic inference method are not always predicted in a straightforward way. This is why we avoid summarizing this information in a table in the manuscript. The 2nd paragraph of the “Limitations of simulated genomes” section addresses some of these subtle considerations. In particular, we suggest that considering a demographic model for simulation requires some familiarity with the inference method and the way it was applied to data. Regarding the demographic models currently implemented in stdpopsim, we provide some information about each model in the documentation page of the catalog. When selecting a demographic model from the catalog, users should make use of this documentation to guide their decision. This is mentioned in the 3rd paragraph of the “Limitations of simulated genomes” section. Following-up on this issue, we intend to review the documentation and make sure it provides sufficient information for each demographic model. See this GitHub issue.

Reviewer #3:

- p5, 2nd paragraph: I think many Biologists, myself included, will think of horizontal gene transfer mostly as plasmids being transferred among bacteria and adding extra genetic material, not as homologous bacterial recombination. This made me confused about modelling horizontal gene transfer in the same way as gene conversion. It may be helpful for some readers if you specify that you are modelling this particular type of horizontal gene transfer. Some explanation along the lines of what is in Cury et al (2022) would be enough.

This is a good point. We modified the text in that sentence in the 2nd paragraph on page 5 to clarify that we are modeling non-crossover homologous recombination, and not incorporation of exogenous DNA (e.g., via plasmid transfer). The relevant part of the text now says:

“In bacteria and archaea, genetic material can be exchanged through horizontal gene transfer, which can add new genetic material (e.g., via the transfer of plasmids) or replace homologous sequences through homologous recombination (Thomas and Nielsen, 2005; Didelot and Maiden, 2010; Gophna and Altman-Price, 2022). However, the initial version of stdpopsim used crossover recombination to stand in for these processes. Although we cannot currently simulate varying gene content (as would be required to simulate the addition of new genetic material by horizontal gene transfer), the msprime and SLiM simulation engines now allow gene conversion, which has the same effect as non-crossover homologous recombination.

Following (Cury et al., 2022), we use this to include non-crossover homologous recombination in bacterial and archaeal species.”

- p5, 3rd paragraph: When you say gene conversion is turned off by default, you could refer to table 1 and briefly mention the consequence of ignoring gene conversion.

We agree that it is important to note that avoiding to model gene conversion may lead to faulty lengths of shared haplotypes across individuals. This is implied by the statement we make in the beginning of the 3rd paragraph on page 5, where we lay out the motivation for modeling gene conversion in simulation. Following the reviewer’s suggestion, we now added a statement about this in the end of that paragraph:

“Note that ignoring gene conversion may result in a slightly skewed distribution of shared haplotypes between individuals (see Table 1)”

- p7, item 1 and p9, 1st paragraph: I am not sure what you mean by genetic map here, can you define this term? I am not sure if it is synonymous with gene annotations, a recombination map, or something else. The linkage map doesn't seem to make sense to me here.

The term ‘genetic map’ referred to the recombination map whenever it was used in the manuscript. To avoid any confusion, we now removed all mentions of ‘genetic map’, and use ‘recombination map’ instead. The recombination map is relevant in item 1 of page 7 because in species with poor assemblies you will not be able to reliably estimate recombination maps, making chromosome-scale simulations less effective. In the 1st paragraph of page 9, we discuss the issue of lifting over coordinates from one assembly to another, and if you have a recombination map estimated in one assembly, you might need to lift it over to another assembly to apply it in your simulation.

- Table 1, last row, middle column: when you say "simulated population", I think it is a bit ambiguous. You mean "the true population that we are trying to simulate", but could be read as "the population data that was generated by simulation". I would delete the word simulated here.

What we mean here is that the selected effective population size should reflect the observed genetic diversity in real genomic data. We realize that the previous wording was confusing, and changed this to the following:

“Set the effective population size (Ne) to a value that reflects the observed genetic diversity”

- Figure 2, and other places when you refer to mutation and recombination rate (eg p11, last paragraph), can you include the units (e.g. per base pair, per generation)?

Throughout the manuscript, rates are always specified per base per generation. In Figure 2, this is specified in the caption (3rd line). We added units in other places in section “Examples of added species” on pages 12-13, where they were indeed missing.

- p11, "default effective population size": can you use a more descriptive word instead of the default? Maybe the historical average? Also, what is this value used for in the simulations when there is a demographic model specified (as in the case of Anopheles)?

We think that “default effective population size” is the most appropriate term to use here, since we are referring to the parameter in the species model in stdpopsim. It is correct that the value of this parameter should reflect the historical average size in some sense, but it is really unclear what this should be in the case of a species like Bos taurus, which experienced a very dramatic bottleneck in the recent past. We address this subtle, yet important, issue in the sentence preceding this one. If a demographic model is specified in simulation, it overrides the default effective population size, and its value is ignored (which is why we refer to it as ‘default’). We added a short sentence clarifying this in the 2nd paragraph of the “Bos Taurus” section (now page 12).

“Note that the default Ne is only used in simulation if a demographic model is not specified.”

- p8, when you say "Such simulations are useful for a number of purposes, but they cannot be used to model the influence of natural selection on patterns of genetic variation.": You may want to bring up the discussion that many of these neutral parameters taken from the literature could have been estimated assuming genome-wide neutrality, and thus ignoring the effect of background selection. Therefore the parameter values might reflect some effect of background selection that was unaccounted for during their estimation.

This is an important subtle point, which we now address in the section “Limitations of simulated genomes”, which we added to the revised manuscript. In that section, we discuss various limitations of simulations, focusing on inferred demographic models. We address the potential influence of the segments selected for analysis toward the end of 2nd paragraph in that section (page 9):

“... all methods assume that the input sequences are neutrally evolving. This implies that technical choices, such as the specific genomic segments analyzed and various filters, may also influence the inferred model and its ability to model observed genetic variation.”

Interestingly, background selection in itself typically does not have a strong effect on the inferred model. This is something that is examined in the forthcoming publication that presents simulations with natural selection in stdpopsim.

- Why are some concepts written in bold (eg effective population size, demographic model)? Were you planning to make a vocabulary box? I think this is a good idea given that you are aiming for a public that can include people who are not very familiar with some population genetics concepts.

In the “Examples of added species” section, we use boldface fonts to highlight the model parameters that were determined for each species. We added a statement clarifying this in the beginning of this section (page 11), and made sure that all the relevant parameters were consistently highlighted throughout this section. In other sections, we use boldface fonts only for titles. A few cases that did not conform to this rule were removed in the current version. We did not intend on adding a vocabulary box, but considered this when revising the manuscript, due to the reviewer’s suggestion. However, we found it difficult to converge on a small (yet comprehensive) set of terms with accurate and succinct definitions. We think that the important terms are adequately defined within the text of the manuscript, providing sufficient information also for readers who are not expert population geneticists.

- p4, 2nd paragraph: Are these automated scripts that are used to compare models publicly available? If you are suggesting that people use this approach generally when coming up with a simulation model (p8, penultimate paragraph), it would be helpful to have access to these automated scripts.

The scripts are part of the public stdpopsim repository on GitHub, and may be used by anyone. Some components of these scripts are more easy to apply in general, such as comparing a demographic model with one implemented separately by the reviewer. This step, for example, is achieved by application of the Demography.is_equivalent method in msprime. Other parts of the comparison depend on the specific structure of python objects used by stdpopsim, so they are not likely to be useful when implementing simulations outside the framework of stdpopsim.

- p9, 1st paragraph, and p.12 2nd paragraph: instead of adjusting the mutation rate to fit the demographic model (and using an old estimate of the mutation rate), would it be ok to adjust the demographic model to fit the new mutation rate? E.g. with a new mutation rate that is the double of a previous estimate, would it be ok to just divide Ne by 2 such that Ne*mu is constant (in a constant population size model)? I imagine this could get complicated with population size changes.

In principle, this could be done if you were simulating neutrally evolving sequences (without modeling natural selection). Since the coalescence is scale-free, then you can scale down all population sizes and divergence times by a multiplicative factor, and scale up migration rates and the mutation rate by the same factor, and you get the exact same distribution over the output sequences. However, making sure you get the scaling right is tricky and is quite error-prone. Especially considering the fact that you have to do this every time the mutation rate of a species is updated. Moreover, once you start modeling natural selection, this scale-free property no longer holds. Thus, the simple solution we came up with in stdpopsim is to attach to each demographic model the mutation rate used in its inference.

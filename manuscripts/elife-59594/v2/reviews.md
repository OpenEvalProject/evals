# Peer review - Round 1

Editors:
- Mani Ramaswami, Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59594.sa1](https://doi.org/10.7554/eLife.59594.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work reports the generation and characterization of molecularly defined null mutants for all 26 rab genes in Drosophila. Loss of 13 nervous system-enriched Rabs yielded viable and fertile flies without obvious morphological defects. However, all 13 mutants differentially affected development when challenged with different temperatures, or neuronal function when challenged with continuous stimulation. The work shows a synaptic maintenance defect following continuous stimulation for six mutants, including an autophagy-independent role of rab26. This is a highly valuable resource for scientists interested in Rab function.

Decision letter after peer review:

Thank you for submitting your article "Systematic functional analysis of Rab GTPases reveals limits of neuronal robustness in Drosophila" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Mani Ramaswami as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Utpal Banerjee as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Suzanne R Pfeffer (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Kohrs et al. generated a collection of 26 Rab knockouts in Drosophila, to complement their previous systematic Rab expression pattern and localization studies (Chan 2011, PMID22000105; Jin 2012 PMID 22844416, Dunst 2015, PMID 25942626). They make the interesting observation that flies with null mutations in nervous system-enriched Rabs are viable, while null mutants for ubiquitously expressed Rab mutants are lethal. In the first part the paper, they elucidate developmental and broad functional roles of Rabs enriched in the nervous system and, interestingly, identify conditions under which viable rab mutants show strong phenotypes. Together the comprehensive collection of null mutations as well their characterization represent a resource useful and important for Drosophila biologists interested in membrane traffic in general, not on their own, but as a key complement to the existing Rab mutants and RNAi tools, YFP-Rab+YFP RNAi or degron tag collection, and the UAS-CA/DN collection. In contrast, the other "resource" section of the paper describing a RUSH Rab toolkit for studying trafficking of Rabs, which is generated through considerable effort, leads to the clear conclusion that substantial further work is needed before this tools can be gainfully utilized. Finally, through more careful analysis of the Rab26 mutant they provide evidence consistent with Rab26 regulating receptor turnover at cholinergic synapses in the visual system of adult flies.

The scientific advances in this paper (viability and wing size of the mutants at different temperatures, ERG recordings at different ages and light exposures) are largely solid descriptive, despite the more in-depth but still not comprehensive characterization of the Rab26 function. However, with appropriate revisions and additions, it may be acceptable as a "tools and resources" paper.

Essential revisions.

1) The detailed characterization of RUSH system reveals several concerns and caveats with respect to its use that make aspect of the work is too preliminary and untested to be published as a Resource in eLife. This entire section should therefore be removed.

The authors generated an UAS collection of SBP tagged Rabs to study the trafficking of Rabs in neurons via the RUSH system, which enables biotin-dependent release of Rabs from a sequestered location. The biggest concern is that the biotin-free media required to set up the experiment compromises animal health. In addition to this issue, sequestration of the overexpressed Rabs may deplete Rab effectors from their normal locations. Therefore the experiments start from a non-inert condition where there may be significant background phenotypes or developmental compensation, compromising the interpretation of results. Thus, despite the interesting observation of biotin dependent redistribution in one or two cases, the work makes it clear that careful additional experiments will be essential for each RUSH lines, before they can be used to conditionally control respective Rab activity in vivo. At very minimum one would need to know if the RUSH lines rescue corresponding null mutants.

There are also several specific queries and concerns, we mention in case these are useful to the authors to take this forward.

a) The system is not designed in Drosophila to ensure 1:1 expression of the reporter (SBP) and the hook (streptavidin). The UAS constructs are in different chromosomes unlike the bicistronic design used in cultured cells in the original RUSH paper (Boncompain et al., 2012). To address this issue one needs to quantify the level of expression of the reporter and the hook to ensure that the reporter is not expressed at higher levels, leading to unbound reporter in the absence of biotin. One way of doing this is to perform qPCR to measure the abundance of the reporter and the hook.

b) A positive control to show that the RUSH system works properly in Drosophila. For example, a good positive control would be to have an UAS myristoylated SBP. In the absence of biotin, this construct should be restricted to the Golgi. After induction with biotin, the majority should be at the plasma membrane. Another positive control would be to label the SBP-tagged and the endogenous cognate Rab. Before induction, all SBP tagged Rab should not co-localize with the endogenous Rab and vice versa. There is a commercially available Rab7 antibody in DSHB that works that could be used for this proof-of-concept experiment.

c) Another concern related to the RUSH system is that significant changes to the Golgi (hook) are observed., while this compartment appears to be stable before and after induction in the original study (Boncompain et al., 2012). This could be a cell specific phenomenon therefore the authors should ensure that in the wildtype the structure of the Golgi is highly dynamic in these cells as well. They could address this by labeling a Golgi resident protein and perform a similar time-lapse image analysis as reported in the manuscript.

d) Is the construct YFP-Rab-SBP (SBP added at the end of the Rab hypervariable domain as indicated in Figure 5?) or Rab-SBP-YFP as indicated in Supplementary figure 6? and when it is released from the Golgi HOOK how does it get prenylated? Is it able to rescue a phenotype? Can it act if not prenylated? Rabs need to associate with membranes to exert their functions and Rab hypervariable domains contribute to effector binding and Rab localization. Supplementary figure 6 needs compartment labeling to show that a released Rab relocalizes to the correct compartment; release from an aggregate is not sufficient (or useful) if the protein is subsequently non-functional.

2) The sections describing the toolkit of molecularly defined null mutants for all 26 rab genes in Drosophila and their characterization are clear and valuable, but also require several additional clarifications and controls before publication.

a) The authors test the effects of different temperatures on the development of Drosophila in mutants of Rabs enriched in the nervous system. Because mutations are generated via different methods, the genetic backgrounds of those flies should be equalized across all the lines studied (ideally via backcrossing or at least transheterozygotes of independently derived alleles) to exclude unknown variables. The Materials and methods and Results sections do not make it clear if such backcrossing was performed (though the ERG sections indicates that all recordings were performed everything in a w- background). This should be clarified in the manuscript.

b) The authors measure ERG "on" transients to determine if Rab mutants disrupt synaptic transmission. This is a very important experiment, but the dataset for 2 days light appears highly variable. This is an issue, because several Rabs with "not significant" differences seem to have much higher variances, and therefore there may actually be something going on. This high degree of variability is not observed in controls at 2 days light, or in the 0 days or 4 days dark datasets. Could high levels of variability be a result of neuronal death in Rab mutants exposed to 2 days of light? The authors should explore this issue as a source of variability in their dataset by performing something like a TUNEL assay or EM in these Rab mutants, or at least discuss it.

c) Chaoptin staining is used to assess structural differences in the photoreceptor projections in Rab mutants. The representative images used, which are described in the text as having "no phenotype," appear to have decreased Chaoptin staining (e.g. Figure 4A R1-R6 middle panel; control 0 days vs Rab19 0 days and Figure 5—figure supplement 1 Rab3 0 days; most of the Rab mutants after 2 days light such as Rab3 KO and Rab40 KO). These observations should be addressed and discussed in their Results section.

d) In Figure 4, the authors stain for Atg8 and Rab11 to assay for changes in autophagosomes and recycling endosomes, respectively. In RabX1, the authors conclude that there is an increase in Atg8 labeling after exposing adults for 2 days in constant light. The representative figure chosen to represent this increase appears to suggest the opposite. Instead, their appears to be an increase in Atg8 labeling at day 0 but after 2 days of constant light small Atg8 puncta disappear and bigger but lighter blobs appear. To resolve this, the authors should either choose a better representative image or reconsider their interpretation of this data.

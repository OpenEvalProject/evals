# Peer review - Round 1

Editors:
- Gary L Westbrook, Oregon Health and Science University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54812.sa1](https://doi.org/10.7554/eLife.54812.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study reveals structural plasticity of presynaptic terminal bouton sizes and underlying molecular mechanisms for endocannabinoid induced long-term depression of inhibitory synapses (iLTD) in the hippocampus. The results establish that the well-described postsynaptic plasticity-related spine growth/shrinkage can also exist in presynaptic compartments in presynaptic forms of plasticity and provide insights into this relatively less understood aspect of synaptic plasticity.

Decision letter after peer review:

Thank you for submitting your article "CB1 receptor-mediated inhibitory LTD triggers presynaptic remodeling via protein synthesis and ubiquitination" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Gary Westbrook as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Erin M Schuman (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers were positive about the manuscript but had a robust discussion of points that they though required additional input. The summary includes the main points that arose in the discussion. The original reviews follow. Please address both the summary and the reviews in your revised manuscript.

Summary of reviewer discussion:

1) Immunostaining for the CB1 receptor was used as a proxy for terminal size. This could be OK, but the bouton volume data should be checked critically. For example, the shrinkage of the terminal as measured by Bassoon is smaller than that measured by CB1. The authors use an agonist of CB1 throughout the paper – this will certainly change the configuration of the receptor (dimerization, clustering, internalization) that could artificially inflate the shrinkage they claim. This point should be discussed.

2) The MS data needs the tolerance value and stats. The link between the requirement for ubiquitination and protein synthesis is not as strong as it could be. The authors could add experimental data or should at least include a working model in their discussion addressing such questions as: Are both required? Do they operate in parallel or is new synthesis needed for ubiquitination?

3) Drug alone controls are missing for several conditions, particularly CHX and JSK.

4) The conclusions RE Rac and Arp need to be modified because the cellular site of action is not established in this study. The manipulations are pharmacological, and although the narrative and proteomics wants us to think about a pre-terminal action, one could imagine postsynaptic effects as these proteins are well-known for postsynaptic roles. The authors need to modify their conclusions or use tools that exist to cell specifically manipulate these proteins and establish the site of action.

Reviewer #1:

This manuscript explores a functional role for presynaptic protein synthesis in modulating structural plasticity of inhibitory presynaptic boutons during LTD. The authors provide data for protein synthesis dependent shrinkage of CB1+ boutons during endocannabinoid mediated LTD. Using proteomics, they identify 33 upregulated and 27 downregulated proteins during LTD. They narrow in and explore a role for actin remodeling during LTD, focusing on the role of Rac1 and Arp2/3, specifically the downregulation of both, for the manifestation of CB1+ boutons shrinkage. Lastly, they argue that while proteasomal degradation is induced during LTD, only the ubiquitination itself is important for the structural and functional manifestation of LTD.

The data presented on presynaptic structural plasticity are exciting but there are missing key control experiments and validations – as indicated below.

Figure 1:

While the detailed description of the analysis of the boutons was appreciated, the data presented in 1C are not convincing in their present state. The authors provide no controls to ensure that it's not endocytosis/remodeling of the CB1 receptors themselves, which would also result in a decreased CB1 volume. Additional inhibitory presynaptic markers (such as VGAT) should also be assessed and scored. Given the strict cutoffs the authors use in the analysis (ie sphericity value within the Imaris analysis), it could be that they're simply detecting a subset of smaller CB1 puncta resulting from local changes in the receptor pool; while the boutons themselves remain largely unchanged. The use of this CB1 volumetric analysis through the paper is problematic, as in almost all cases the authors do not test the effects of the pharmacological treatment alone (CHX, JSK, CK-666, NSC and ziram). Most if not all of the conclusions could be substantially undercut if these treatments in control conditions show the same change as when paired with WIN treatment. The study of structural plasticity in the postsynapse has largely relied on live cell imaging, so the compartment can be analyzed before, during and post treatment. While challenging, the authors should consider a similar approach, even if only to demonstrate their CB1 volumetric approach is valid. Using either an inhibitory neuron restricted GFP expression or expression of a tagged inhibitory presynaptic protein to allow live imaging of the bouton volume before and after WIN application, the authors could the perform fixation and staining for CB1 receptors and analyze how this compartment changed during the course of the treatments. This would bring their approach more in line with the standard in the field and allow for much more current and compelling analysis for structural plasticity to be performed.

Specific comments:

– Examples (similar as in 1A) should be provided of CB1 boutons with WIN/WIN+CHX treatment.

– CHX treatment alone should be assessed for C.

– CHX and WIN+CHX should be assessed for D.

– Did the authors look at what happens to the corresponding inhibitory postsynaptic compartments? Presumably these also may decrease in size as well.

– For Figure 1—figure supplement 1C, the indicated mean for the WIN group for the graph provided should be checked. Given the large increase in the low volume population seen in the WIN group vs control group; and the similar size of the groups (540 vs 602) it's hard to understand how both means can be right around 1.

Figure 2:

The experimental design (multiplexing of fully medium-heavy and heavy labeled cell cultures) is nice, but there are several potential issues regarding data processing and interpretation.

Protein identification and quantification:

– The accepted parent mass tolerance of 50 PPM is very high and might lead to false identifications. When acquiring the data with an MS1 resolution of 60k on a well-calibrated Orbitrap LTQ instrument, a MS1 mass tolerance of ~5 PPM should be used.

– Why are the SILAC labels (Lys4/Arg6 and Lys8/Arg10) specified as variable modifications instead of “SILAC pairs”? Please describe in more detail how the medium-heavy and heavy counterparts were quantified and how the fold-changes were calculated. Were only peptides species considered that were quantified in the medium heavy and heavy form? Why not using software that provide well-established workflows for SILAC quantification (such as the freeware MaxQuant)?

– From Supplementary file 1, we understand that each ~700 proteins were identified in the forward and the reverse samples. The overlap between the two samples is 391 proteins (main text), indicating that the reproducibility is fairly low between the measurements.

Statistics:

– Please perform proper statistics to identify differentially regulated proteins (e.g. t-test and multiple testing correction). A simple fold-change cut-off (as described in Figure 2C) is not state-of-the-art.

Specific comments:

– The supplementary data should be improved to enable the reader to understand the proteomics data and inspect all quantified proteins. Please include one table that presents the quantitative results for all proteins in all biological replicates (forward and reverse), so that the reader can get a sense for the biological variability. Please include a column with gene names. In Supplementary file 1, why does the table contain proteins from rattus norvegicus, mus musculus and human?

– All mass spec raw data and database search results should be uploaded to the PRIDE repository prior to publication and the PRIDE identifier should be included in the Materials and methods section.

Data interpretation:

– Protein up-regulation is often interpreted as increased protein synthesis and protein down-regulation is often interpreted as increased degradation in the manuscript. However, based on the SILAC-MS data one cannot draw these conclusions. Protein up-regulation could result from more synthesis or less degradation and protein down-regulation could result from less synthesis or more degradation. Based on the presented data there is no evidence for one or the other.

– Based on the proteomics data one cannot distinguish proteins from different subcellular compartment or different cell types. The following statement from the Discussion sections is hence misleading: "[…] why ribosomal proteins would be synthesized locally if ribosomes are exclusively assembled in the nucleolus is unclear."

Figure 3:

The authors refer to JSK as an "actin stabilizing drug", whereas in fact it's a drug that promotes actin polymerization. This fact complicates the data presented in this figure as essential controls (such as JSK treatment alone for 3A) are missing. If JSK treatment alone increases the bouton size, is this really demonstrating that the structural remodeling requires actin depolymerization?

Specific comments:

– 3A, the examples provided with the black background are harder to examine. The authors should use the white background used in Figure 1 and Figure 1—figure supplement 1 examples.

– 3B, what explanation do the authors have for why the +JSK/WIN treated curve stabilizes around 80%?

– Additionally, the authors should test the effect of the Arp2/3 inhibitor and Rac inhibitor with and without WIN treatment on the bouton volume.

Figure 5:

Specific comments

– 5D, examples would be better with white backgrounds.

– Analysis for the effect of ziram alone needs to be done.

Reviewer #2:

In this study by Monday and colleagues, the investigators reveal structural plasticity of presynaptic terminal bouton sizes and underlying molecular mechanisms for iLTD, a form of endocannabinoid induced long-term depression of inhibitory synapses. Their discovery establishes that the well-described post-synaptic phenomenon of spine growth/shrinkage with plasticity can also exist in presynaptic compartments in presynaptic forms of plasticity. This finding is demonstrated by volumetric bouton measurements of CB1+ terminals in hippocampal slices. The remainder of the study involves a series of elegantly and rigorously designed experiments to provide insights to the molecular mechanisms for this structural plasticity. Insights begin with a proteomic analysis performed on cultured hippocampal neurons, and then use pharmacology and Western analysis to test a main hypothesis that changes in the abundance and activity of actin regulators underlie the structural plasticity. The study continues to reveal that despite their hypothesis that proteasomal degradation could drive those shifts, experiments instead support the idea that ubiquitination, in the absence of degradation (assessed by MG-132) appears to underlie the functional differences required for iLTD.

Overall, this study provides an important extension to the Castillo lab's recent work demonstrating the requirement for local protein synthesis for this form of plasticity (Younts et al., 2016). Strengths of this study include the mechanistic depth, general rigor in approaches, and novel insights to a relatively less understood aspect of synaptic plasticity.

I have two major concerns that should be addressed.

1) Boutons simply should not be considered individual n's for statistics. The authors are welcome to argue for what the independent biological unit is. Please also clarify, for a given condition (such as Veh or WIN), were slices from the same animal used for multiple conditions, or were the slices from one animal used for one condition at a time? If the latter, then an animal is the biological unit, with the possibility of using nested data statistical approaches. Alternatively, the mean value/slice could be considered. Issues such as animal health, temperature fluctuations, buffer osmolarity et cetera could otherwise exist and generate 100s of values per slice that are a little bigger or smaller due to technical variables. This is a foundational observation for the study and needs to be robust. As presented, it looks small and only visible when n's are in the 1000s. Likewise, although it was good to consider involvement of other inhibitory synapses (like PV+), a figure showing no significant difference that is potentially grossly underpowered is not so useful (n's of 500).

2) In general, the bioinformatics approach was rigorously and thoroughly presented. It is also nice that the authors further discuss results from other programs. One item to clarify – since the GO analyses are the major data presented: please review and clarify the extent to which the same protein is annotated with multiple functional properties such that it is populating (and driving) multiple terms on those lists.

Reviewer #3:

In this manuscript the authors show that CB1-LTD involves presynaptic structural plasticity: bouton volumes are reduced, which occurs at least partially via actin reorganization.

Mass spec data showed results that may have been expected (downregulation of synaptic proteins), but also some unexpected results were found (upregulation of protein synthesis as well as protein degradation system). Finally, the authors show that activation of the ubiquitination system is required for CB1-LTD, however not by promoting protein degradation by the proteasome.

The manuscript contains an interesting data set and the involvement of the ubiquitination system in CB1-LTD is highly intriguing. However, after reading the manuscript there are many “lose ends”, and it is still not clear what happens during CB1-LTD. Indeed, the authors themselves describe these events as “coordinated engagement of multiple cellular processes”, which does not clarify much. I would like to encourage the authors to try and formulate a more complete hypothesis of the cellular events that underlie CB1-LTD.

I have two major points:

1) It is not easy to link the proteomics findings to changes in the actin cytoskeleton in presynaptic boutons. For instance, the authors show that WIN slightly reduces Arp2c protein levels, but that inactivating Arp2/3 actually enhances CB1-LTD. I am wondering if the explanation given by the authors the most plausible interpretation of the data. Is it known how CB1-LTD is expressed (fewer vesicles? reduced release probability?) and is it possible to link this to specific changes in the actin cytoskeleton?

2) The proteomics data show that multiple processes are activated during CB1-LTD. The manuscript does not provide a model or hypothesis for how these processes are linked. For instance, are ubiquitination and protein synthesis independently regulated by CB1? What is the link between ubiquitination and presynaptic actin remodeling? Would it be possible to link CB1-LTD to a specific E2 or E3 ligase in the presynapse?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your revised article " CB1 receptor-mediated inhibitory LTD triggers presynaptic remodeling via protein synthesis and ubiquitination" to eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Gary Westbrook as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Erin M Schuman (Reviewer #1).

The reviewers have discussed the reviews with one another and the Senior Editor. There are some remaining concerns raised by one of the reviewers and by me that we would like you to address as below. These are concerns about the data presentation as embodied in comment 1 of reviewer 2 in the original review. The issue concerns what constitutes "n" in the bouton counts. We suggest a compromise in which supplemental data are shown by slice for full data transparency. Overall, we suspect that artifact is not the basis of the findings, but the data presentation does not allow that assessment and therefore lowers the rigor and potential reproducibility.

Requested revisions

1) The authors in their rebuttal argue that standard power calculations are "unreasonable" because n of 145 slices would be required. At the most fundamental level, if this were true, this question and conclusion are not appropriate given the constraints of the methodology and one should focus on powerable questions. However, a statistical analysis by a statistician might indicate other analytical approaches. The authors show how close to being powered they may be with the slice means alone (not including nesting) showing significance. If the authors want to show the data as is in the main figure, the authors could address this concern by creating supplemental figures that show bouton size distributions for each slice and also figures with slice means and exact p values.

2) Bassoon puncta were to serve as an independent measure of bouton size to support the CB1 observations. However, the methods describe first making a binary mask of CB1 signal, then using the "and" function to isolate the bassoon pixels that overlap with CB1 pixels. As described, it is almost impossible to reach any other conclusion than reproducing the CB1 measurement results. Please clarify methods substantially to remove this concern.

3) In working to propose a solution for data presentation, the authors raise an important point, supplemental data should include an analysis that addresses whether the plasticity effects preferentially involve a particular size subset, smaller or large.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article " CB1 receptor-mediated inhibitory LTD triggers presynaptic remodeling via protein synthesis and ubiquitination" for consideration by eLife. Your article has been reviewed by one peer reviewer, and the evaluation has been overseen by Gary Westbrook as the Senior Editor. Before final acceptance, please edit the text and Materials and methods to indicate your response to the final reviewer comments as below. I would appreciate it if you indicate in the text where the revisions have been made. The final submission will not go back to the reviewers.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Reviewer #2:

1) The supplementary figures are highly appreciated and allow critical review of the nature of the experimental data and robustness of the conclusions.

2) The authors' response indicating that data was removed to balance slice numbers needs to be clarified. One should not have to remove data. If slices were removed from supplementary figure analyses, what guided those decisions? Do the removed slices remain in the main figure data? I would suggest all the data that were believed to be valid in the original submission be included in the main and supplementary figures. (Or was there a situation of grossly unequal n's in the control/win condition and the authors are trying to make statistical comparisons across similarly sized groups post hoc? In principle, a similar number of interleaved controls should exist for each additional test condition.) Please clarify.

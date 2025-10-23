# Author response - Round 1

Authors:
- Ruud van Zessen ([ORCID: 0000-0001-5634-6922](https://orcid.org/0000-0001-5634-6922))
- Yue Li
- Lucile Marion-Poll ([ORCID: 0000-0003-4652-9797](https://orcid.org/0000-0003-4652-9797))
- Nicolas Hulo ([ORCID: 0000-0003-2640-636X](https://orcid.org/0000-0003-2640-636X))
- Jérôme Flakowski ([ORCID: 0000-0002-6457-3022](https://orcid.org/0000-0002-6457-3022))
- Christian Lüscher ([ORCID: 0000-0001-7917-4596](https://orcid.org/0000-0001-7917-4596))

## Response text

DOI: [10.7554/eLife.66048.sa2](https://doi.org/10.7554/eLife.66048.sa2)

Essential revisions:

1) The support for the main conclusions would be strengthened by the revisions or additions to the statistical analyses:

– Direct comparisons between the relevant conditions (D1 versus D2 neurons, SL327 versus untreated controls), rather than separate tests in each condition that are reported as either significant or non-significant (since the absence of a significant effect isn't evidence for the absence of any effect). In some cases, the data are changing in opposite directions, making it very likely that these direct comparisons will be significant, but in other cases it is less clear.

We thank the reviewers for this constructive suggestion. Direct comparisons between the two populations are indeed a powerful way to make the case of cell type dichotomy. We now directly compare the response to cocaine in D1R and D2R SPNs (Figure 2D), also when SL327 was applied (Figure 6_S1). We find significant differences, thus strengthening our conclusions.

– Analyses that account for the lack of independence between neurons recorded from the same subjects. This can be tricky when examining binary/proportion data (I'm not aware of a standard equivalent to a Fisher's exact test that accounts for lack of independence) – I would suggest calculating the proportion of neurons that are excited or inhibited for each subject individually and then running a mixed or repeated measures ANOVAs to assess whether these proportions are changing over time. For continuous measurements like change in transients, tests like linear mixed models with random effects for subjects could be used to determine whether differences in D1 or D2 activity changes were consistent across subjects.

We agree with the reviewer that non independence of data from the same animal needs to be accounted for in the analysis. We compared the number of transients before and after cocaine injections by calculating the log2(ratio after/before) and found a normal distribution. We then ran a linear mixed model with animals as random effects, as suggested by the reviewers. Finally, we have also quantified the variance per animal by plotting sdev of the calcium transients. These analyses are now presented in Figure S2_S1 and described in the Methods; the results agree with our previous analysis on the proportions.

2) Discussion of the results in the context of the following papers would strengthen the manuscript:

– Ferguson et al., Nat. Neurosci. 2011 Transient neuronal inhibition reveals opposing roles of indirect and direct pathways in sensitization.

– Jiang et al., JNeurosci 2021 Cocaine-Dependent Acquisition of Locomotor Sensitization and Conditioned Place Preference Requires D1 Dopaminergic Signaling through a Cyclic AMP, NCS-Rapgef2, ERK, and Egr-1/Zif268 Pathway – this paper just came out but it would be informative for the authors to include in their discussion.

We agree with the reviewers that these papers provide valuable insights into molecular machinery in circuits of the dorsal striatum underlying locomotor sensitization. We have now added both references to the discussion.

3) The data in Figure 5 are used to conclude that NAc dopamine was stable during cocaine sensitization. Could this be due to a ceiling effect? That is, if the first cocaine injection elicited a maximal sensor response, it would be incorrect to conclude that a second dose does not increase dopamine release. While additional experiments are not requested at this time, this was a significant concern discussed in the review process and a thoughtful discussion of this potential caveat should be included in the Discussion section.

We agree with the reviewers to ensure that the fluorescent signal is not saturated. We therefore performed an additional experiment in a new batch of wildtype animals that we injected with an AAV containing dLight into the NAc. We then monitored dopamine in response to with 20 mg/kg cocaine IP as before, but then followed up with an injection of the D2 antagonist raclopride 0.1 mg/kg IP. The injection was timed to the peak of the cocaine response (see figure 5B). We reasoned that this should relieve the autoinhibition of DA neurons by D2R receptor activity (Wei et al., Cell Discovery 2018), thus further increasing DA levels. We indeed observed a significant enhancement of the dLight fluorescence, confirming that cocaine did not saturate the indicator. These results are presented as a new panel in Figure 5 and are described in the Results section.

4) To what degree can epifluorescence measurements be used to assign calcium activity to individual neurons? The authors cite Zhou et al., (bioRxiv, but it is now published in eLife so this reference should be ipdated) and use constrained nonnegative matrix factorization to assign ROIs for putative somata. There was concern by the reviewers that this isn't enough to evaluate the "isolation quality" (e.g., the morphologies in Figure 1D and Figure 3A look strange). The authors are asked to make it clear to the reader how to access their raw data through GitHUB or a related mechanism which could help to understand the path from raw to processed data.

Indeed, single photon epifluorescence calcium imaging carries the risk of picking up noise from neighboring neurons, and we did carefully consider this in the data processing pipeline. We have now updated the Methods section “Image processing and neuron detection”, giving in depth details on the path from raw to processed data. All the raw data and procedures will be uploaded to Zenodo (CERN, Geneva), for which the link is in the manuscript.

The examples of the fields of view in Fig1D and Figure 3A might “look strange”, but this is only due to an edge distortion typical for GRIN lenses.

In addition, the citation mentioned has been updated.

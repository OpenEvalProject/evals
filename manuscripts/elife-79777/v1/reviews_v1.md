# Peer review - Round 1

Editors:
- Bavesh D Kana, https://ror.org/03rp50x72 University of the Witwatersrand South Africa

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79777.sa0](https://doi.org/10.7554/eLife.79777.sa0)

This work applies hybrid-capture sequencing for coronavirus (CoV) surveillance in bats. Given that bats are a major reservoir for animal-to-human virus spillover events, which have caused several major epidemics/pandemics, this is a very important field of research. The reported hybrid-capture method shows some clear advantages over amplicon-based viral sequencing, which is the established standard in the field. This new approach has clear merits that are well supported by the data presented and is likely to become an important tool in viral surveillance programs that ultimately aim to predict/prevent/prepare for future pandemics. The work will be of interest to microbiologists, particularly those studying viruses or interested in genomics surveillance.


---

# Peer review - Round 1

Editors:
- Bavesh D Kana, https://ror.org/03rp50x72 University of the Witwatersrand South Africa

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79777.sa1](https://doi.org/10.7554/eLife.79777.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Targeted genomic sequencing with probe capture for discovery and surveillance of coronaviruses in bats" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Bavesh Kana as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Ira Deveson (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Please include a simple table of sequencing summary statistics for the study – eg number of sequencing reads overall, on/off target rates, PCR duplicate rates, etc in each library. This is useful for the reader, and some of these basic performance metrics might also help explain the failure to detect expected CoV sequences in some samples.

2. What was the sequence similarity between RdRp contigs obtained via amplicon vs capture sequencing on matched samples? Did capture sequencing always recover the same/similar RdRp sequence, or were there any discordant results? Some text on this would help.

3. The examples of coverage plots in Figure 3 are useful and help to orientate the reader. However, some global summaries of coverage breadth and depth should also be shown, rather than just individual examples. A simple dot plot or bar chart showing the % genome coverage for each of the specimens would be good. And a similar figure showing % coverage for each relevant gene (eg RdRp, spike, etc) would also be informative. The spike generally has poor coverage in the read-depth tracks, it would be good to show this in a clear, simple plot covering all specimens.

4. The hybrid-capture panel design was obviously limited due to the diversity, quality, and completeness of available bat CoV genomes. There are a few open-ended questions on this that could be worth discussing:

Would there be any merit in including known CoV genomes from outside bats on the panel? This might help pick up inter-species transmission events. Please discuss.

Did the authors consider elevating the probe density, or modifying probe sizes, within hypervariable regions, specifically the spike protein? There may well be some technical optimisations that could deliver better performance.

Is it possible to design probes in this region that target imagined (predicted/modelled), but not previously observed, spike-protein sequences? For example, include additional probes that cover a diversity of semi-random spike mutations that could foreseeably occur – an agnostic diversity capture approach.

There is also no reason why other viruses can't be included on the panel. Bats must also carry other informative viruses like influenzas that might be worth looking for. Please discuss.

5. A quantification of the viral load of the samples would be useful to help understand the similarities and differences between the samples post sequencing. For example, SARS-CoV-2 hybrid capture needs a Ct of < 25 to get a reasonable genome whereas ARTIC amplicon sequencing can get similar results at 30. The complexities of working with archival samples and transporting them over long distances limit what can be done.

6. From the methods description of the controls and bioinformatics analysis of the sequencing data, there appears to have been cross-contamination during sample preparation for sequencing. There was then an informatics salvage operation on the data. These salvage operations are fraught with danger, particularly where you have very low levels of RNA and are performing assemblies with very low depths of coverage, which is the case in this work. As the original data, as it came off the sequencer, is not available to the public it is not possible for anyone outside of the study to quantify. This would be a QC fail in SARS-CoV-2 sequencing labs and with a repeat from scratch.

Were NTCs/blanks used for sequencing at the same time as the rest of the samples?

Were there any CoV reads in these NTCs control (before any read scrubbing)?

Many labs have undertaken SARS-CoV-2 work (sequencing, diagnostics, reagent manufacturers) and there is a widespread low level of background contamination. As an indication of background contamination, how many SARS-CoV-2 reads were present in the read data (before any read scrubbing)?

The risk is that the cross-contamination from one overperforming sample can overwhelm an underperforming sample, giving you an erroneous mixed assembly.

Other comments:

1. A positive benefit of amplicon sequencing that should be highlighted is the ability to detect intrahost viral populations.

2. Please check the version of blast used because the version in the text is quite old (possibly just a copy and paste typo).

3. The assembly sizes are small and marginally larger than amplicon sequencing and one can sporadically get different regions of the genome making comparative analysis challenging. This method should really shine on fresh, high viral load samples, so it would be interesting to see it in action, perhaps in the field with sequencing on a MinION. Some comments on this would be useful.

4. The introduction could do a better job of linking back to the literature on the use of hybrid capture for virus sequencing. One paper that comes to mind is https://f1000research.com/articles/4-1062 with the method used for SARS-CoV-2 to great success. There are a lot of papers using hybrid capture for SARS-CoV-2 over the past 2 years demonstrating the relevance of the approach. Please cite the appropriate literature.

Concerns related to how credit has been apportioned to authors, particularly those from DRC.

We acknowledge your earlier correspondence, detailing the roles of authors. It is also acknowledged that some aspects of primary research related to these samples have been published in prior work, with appropriate credit provided to the DRC team. That said, this manuscript makes mention of some primary specimens being shipped to Canada (Specific text: "21 unique specimens were shipped to Canada: 15 as RNA extracts only, 2 as unextracted swabs in transport medium, and 4 as both previously extracted RNA and unextracted swabs in transport medium"). The unextracted swabs would classify as primary specimens. I'm sure you appreciate that collection of such material is a complex process and takes much effort, the current study would not have been possible without these primary specimens. Without knowledge of the intimate workings of your research group, the authorship line up where DRC authors who undertook this collection but do not share primary/senior authorship, emerged as a concern.

We accept your explanation and note your suggestion to include a more detailed author statement. Please do so. That said, there may be merit in discussing this with your team to determine if the author list best reflects the overall intent of the research, including the partnerships created and what appears to be an excellent collaborative relationship between diverse groups, spanning continents. Considerations of joint (sometimes with more than two authors) primary authorship or senior authorship may best reflect the vibrant and collegial nature of these relationships. As a journal, we cannot be prescriptive, the choice is ultimately up to you and your team but I hope this narrative has provided some guidance.

Reviewer #2 (Recommendations for the authors):

The authors need to take a long hard look at how this research was conducted and how it got so far without being addressed. Why are the first 5 authors and last 4 authors all from wealthy countries (primarily Canada), with DRC authors dumped in the middle? It is ethically and morally wrong to undertake this kind of colonial research. You should be building skills and capacity in DRC, not just taking samples thousands of miles away and giving tokenistic authorship to local scientists. These kinds of abusive research practices brought about the Nagoya Protocol.

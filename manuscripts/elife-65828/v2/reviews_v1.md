# Peer review - Round 1

Editors:
- Albert Osterhaus, University of Veterinary Medicine Hannover Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65828.sa1](https://doi.org/10.7554/eLife.65828.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper by Stirrup and colleagues describes a methodology that can be useful for for real-time investigation of COVID-19 outbreaks and SARS-CoV-2 infection prevention by infectious disease control teams in the hospital setting. It combines epidemiological and viral sequencing data – rather than only epidemiological data – to identify and investigate the infection source of hospital onset SARS-CoV-2 infections. The challenge for the use of this methodology is to secure the timely availability of the sequence data and requires close collaboration between methodologists, virologists, infectious disease clinicians and software engineers, to collectively create the appropriate workflows and reporting systems.

Decision letter after peer review:

Thank you for submitting your article "Rapid feedback on hospital onset SARS-CoV-2 infections combining epidemiological and sequencing data" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Albert Osterhaus as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Jos van der Meer as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The method was validated retrospectively with data from two UK city hospital settings and is eventually meant to be used for future use for the identification, prevention and control of healthcare-associated SARS-CoV-2 infections in hospitals.

Indeed, there is an urgent need for tools that can synthesise multiple data streams to provide real time information to healthcare professionals. It is questionable to what extent the tool presented is generalisable to medical facilities outside of the specific data rich settings considered here, or if the tool is useful for prospective analyses.

Concerning the question to what extent the tool presented is generalisable to medical facilities. the papers' claims are largely supported by the data and may be useful for SARS-CoV-2 infection prevention and control teams, provided they effectively have access to, and can implement both elements of the system: evaluation of state-of-the art epidemiological data and of phylogenetic sequence data based on local and hospital SARS-CoV-2 genomes as determined within 24-48 hours by the COVID-19 Genomics (COG) UK initiative. Therefore this study would rather be of interest to specialists working in hospital infection prevention, with more limited further interest.

Concerning the prospective analysis of prospective use cases described in the discussion and given the high burden of SAR-CoV-2 in the UK in late 2020, there should already be ample data available for their inclusion.

As the Discussion section briefly touches on the motivation for using a 2 SNP threshold for identifying "similar" viruses instead of phylogeny-informed approaches, it dismisses the latter saying that they are too intensive to be used outside of research-intensive settings. Although phylogenetic approaches would be more resource intensive, it would seem that the amount of sequencing and shortness of turnaround time required to make this algorithm useful similarly limit its utility to research-intensive settings. With this in mind, the substantially increased information associated with phylogenetic approaches would seem to be worth the increased resource costs particularly since the capabilities and quality of phylogenetic tools has increased substantially since the publication of the 2013 paper cited on line 326. Although extending this particular algorithm to include phylogenetic data is outside the scope of the study, the manuscript is unfairly dismissive of such approaches, especially when a location specific build of nextstrain can be created with a programming burden similar to that of the algorithm described in this study.

Given these considerations, the paper would be acceptable for publication if the following points would be addressed:

1) Analysis of the prospective use cases described in the discussion. This would seem essential for validating the utility of the algorithm.

2) Address specifically the limitations of the study that are related to the overall applicability of the methodology in settings with more limited access to state-of-the art epidemiological and phylogenetic sequence data, the latter based on timely availability of local and hospital SARS-CoV-2 genomes.

3) Although extending this particular algorithm to include phylogenetic data is outside the scope of this study, it should address the value of such approaches, especially when a location specific build of nextstrain can be created with a programming burden similar to that of the algorithm described in this study.

Reviewer #1 (Recommendations for the authors):

The science is based on a practical comparison of the existing PHE system and the newly established SRT, which is based on epidemiological and digested viral sequenced data. The criteria chosen are largely arbitrary but justified by practical considerations. The presentation of data and conclusions is clear. More attention could be paid to the overall applicability of the methodology (with or without modifications) in other geographical or demographic settings with different public health infrastructures and their limitations.

Tables, figures and supplementary material are well designed and informative

Reviewer #3 (Recommendations for the authors):

Foremost, this study could be substantially strengthened through the analysis of the prospective use cases described in the discussion. Given the high burden of SAR-CoV-2 in the UK in late 2020, there should already be ample data available for inclusion. This would seem essential for validating the utility of the algorithm.

It would also be very helpful to include some estimates on the circumstances under which the algorithm is likely to provide useful information. The UK is highly unusual in terms of its virus sequencing efforts. What proportion of test-positive cases need to be sequenced in order for the algorithm to provide reliable estimates of ongoing transmission under different outbreak scenarios? On a related subject, the impact of turnaround time from sample collection to receipt of sequence data should be evaluated. How fast does sequence data need to be able available for the algorithm to provide actionable information?

The Discussion section briefly touches on the motivation for using a 2 SNP threshold for identifying "similar" viruses instead of phylogeny-informed approaches but dismisses the latter saying that they are too intensive to be used outside of research-intensive settings. I agree that phylogenetic approaches would be more resource intensive, but it would seem that the amount of sequencing and shortness of turnaround time required to make this algorithm useful similarly limit its utility to research-intensive settings. With this in mind, the substantially increased information associated with phylogenetic approaches would seem to be worth the increased resource costs particularly since the capabilities and quality of phylogenetic tools has increased substantially since the publication of the 2013 paper cited on line 326. I recognise that extending this particular algorithm to include phylogenetic data is outside the scope of work for this project, but the manuscript is unfairly dismissive of such approaches, especially when a location specific build of nextstrain can created with a programming burden similar to that of the algorithm described in this study.

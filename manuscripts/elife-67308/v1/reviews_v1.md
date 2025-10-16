# Peer review - Round 1

Editors:
- C Brandon Ogbunugafor, Yale University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67308.sa1](https://doi.org/10.7554/eLife.67308.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The reviewers agreed that your manuscript was an impressive piece of work, that provided a rigorous and granular perspective on infection dynamics that integrated data of various kinds: clinical, genomic, and demographic. Using these varied approaches, the study provides strong evidence for the importance of superspreading as a key feature of outbreaks. It is our hope that studies that similarly integrate data of various kinds might become the standard for resolving the particulars of outbreaks.

Decision letter after peer review:

Thank you for submitting your article "Superspreaders drive the largest outbreaks of hospital onset COVID-19 infections" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Sarah E Cobey (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Summary:

This study of COVID-19 outbreaks in a major hospital makes two major contributions. First, it suggests that most hospital-acquired infections do not lead to further spread, and that superspreading events occur infrequently. Second, it advances analytic methods for reconstructing transmission networks by combining data on symptoms, behavior, testing, and viral sequences. This will facilitate analyses of other pathogen outbreaks.

Essential Revisions:

Clarifications on some aspects of the HCWs as outlined by the reviewers. Though their inclusion was a strength and focus on their paper, there are certain aspects that were not immediately clear, that readers could benefit from understanding.

These include, amongst others, questions about the conditions under which the HCWs and patients were tested over time, questions about the immune status of HCWs, and questions about the location function for HCW.

Pay special attention to the detailed questions raised by Reviewer #2. I consider these changes to be essential, and I shared some of those curiosities. Make no mistake, however, the reviewers and reviewing editor agree that this manuscript has very strong potential. It is a compelling study with an impressive mix of data sources and methods.

Reviewer #1:

Illingsworth et al. write a compelling and well motivated manuscript on the importance of superspreading in hospital settings.

It is a very well written and important piece of work with methodological advances beyond the application presented here.

I am not an expert in viral phylogenetics and will not be able to speak to the robustness of the evolutionary analysis performed.

This work is particularly strong in its adaptation of statistical techniques to identify transmission networks in highly sampled environments. Even though this is of great interest for some settings I wonder whether the authors had the ability to test their models predictive performance (i.e., if the authors withheld some data and tried to explain future case trajectories in the hospital). This may well be out of scope for this analysis but would make the results be generalisable beyond one particular setting. It would also provide additional support for the robustness of the method. It is very hard to evaluate whether the transmission networks reconstructed are indeed explained by the model applied here given the large number of parameters and somewhat long time of infectiousness of SARS-CoV-2.

The authors state that the sampling of infections within wards was nearly complete which is a major strength of this paper. Usually there are large biases in genomic sampling. It is remarkable that even asymptomatics here are sampled and sequenced if/when positive. However, there is asymmetry in sampling: within the wards it is high but what could the contribution of visitors have been?

Whereas the authors work is very illustrative I wondered after reading it whether there should be more information about the patients characteristics (age, sex, symptoms etc.).

Overall, I enjoyed reading this work!

Reviewer #2:

This study investigates the spread of SARS-CoV-2 in several wards of a hospital in the spring of 2020, aiming to measure transmissibility among patients and healthcare workers (HCWs). The investigators ambitiously incorporate seemingly all relevant data sources into a unified statistical framework in their attempt to reconstruct transmission networks.

The conclusions of the study appear well supported by the data, assuming a few uncertainties in my reading (discussed elsewhere) are resolved. A strength of the analysis is that transmission events are linked by not only the spatiotemporal proximity of individuals' infections but also the genetic similarity of their viruses, and this is a relatively circumscribed population (i.e., patient movement and HCW shift assignments are well known). This is thus an unusually well resolved transmission network over an extended period.

One of the study's claims appears weakly supported by the current analysis. The authors investigate whether Ct values, a measure of viral load, correlate with superspreading. Since Ct values are well known to vary over the course of an infection, some adjustment should probably be made for time of symptom onset, and asymptomatics potentially excluded. Otherwise there is a risk that any correlation between Ct values and increased transmissibility will be masked by variability in relative sampling times. (Transmissibility should probably not be assigned a binary variable either.) Relatedly, correlations between transmissibility and presence of, e.g., fever, would require a larger analysis, and I suggest the authors qualify their language about "identified risk factors."

An important public health consideration is whether it is appropriate to describe these as superspreading individuals or superspreading events. My impression is that the two are not clearly identifiable here, but the authors seem well positioned to address this ongoing debate directly. Additionally, it seems possible that the statistical breakdown estimated here (80% of cases are caused by 20% of infections) is distorted by the investigators' decision to analyze the wards with the largest outbreaks; if other wards were included, the estimated contribution of superspreading might be lower.

This paper presents a real methodological contribution in showing how diverse data sources can be integrated in a statistically coherent way. This will be invaluable in future outbreak investigations and will (I hope) motivate better surveillance, especially collection of date of symptom onset + sequences. In addition to an unusually clear description of the methods, especially for analyses of this complexity, the authors have commendably made their code publicly available, and it appears to be well documented. Future work will likely relax some of the assumptions here, e.g., by allowing unobserved intermediate infections and potentially allowing greater variation in mutation rates and serial intervals in immunocompromised hosts.

This work appears technically sound, but the following clarifications/checks would be really useful:

1. Under what conditions were HCWs and patients tested in the wards over time? How confident can we be that unobserved infections did not occur? Was there regular screening for asymptomatics (as suggested in the Discussion, lines 268-270)? When were visitors allowed?

2. Did the authors confirm that separate models were justified for the wards? Was there evidence of transmission b/w wards, perhaps involving the same HCWs?

3. In interpreting the transmissibility and susceptibility of HCWs and patients, is there any reason to think that many of the HCWs (especially in the red ward) might already have immunity from prior infection?

4. Are the results affected substantially if we assume that the location function for the HCWs is +/- 0.5 d instead of 1 d? The 1-d assumption could implicate HCWs unnecessarily. Fomite transmission seems hard to justify.

Further clarifications suggested for the text:

5. Please include symptom definitions and whether they varied by case type (HAI, HCW) and also describe the wards a bit more fully, if possible (square footage? patients per room?)

6. It would be really nice to have a time series of infections by ward relative to some arbitrary day 0. I think there should be some way to do this that would not violate privacy.

7. In the Discussion (lines 257-278), the authors recommend masks and hand hygiene. Are there any citations for the latter? If not, I might say something more vague (or mention only the former, with references).

8. I found the description of the network analysis of patient bed movements hard to follow (paragraph starting l. 373). What "network analysis" does FoodChain Lab do exactly? The listed criteria seemed straightforward to apply.

9. Line 431: Separate references and CIs here would help.

10. Line 445: Typo in the lognormal component → "((log(x) -mu)^2)"

11. Lines 658-661: Subscript typo in this criterion?

12. Lines 693, 696: There seems to be a major contradiction between "all possible networks" and all networks meeting the condition where individual i infects n others.

13. Is there any way to add schematics for the later steps of the analysis? I greatly appreciated what the authors already provided.

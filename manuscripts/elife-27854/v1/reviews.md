# Peer review - Round 1

Editors:
- Rumi Chunara, New York University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27854.033](https://doi.org/10.7554/eLife.27854.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Using mobile phones as acoustic sensors for high-throughput surveillance of mosquito ecology" for consideration by eLife. Your article has been favorably evaluated by Prabhat Jha (Senior Editor) and five reviewers, one of whom serve as Guest Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: Scott Ritchie (Reviewer #5).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This work presents an evaluation of the use of common mobile phones for mosquito detection (acoustically), attempts to differentiate species via their acoustic signatures alongside other meta data. Overall this is a very interesting effort that provides an out-of-the-box approach to mosquito and vector surveillance. The reviewers expressed excitement and need for this approach, note that the authors provided technical detail and a convincing case. However there are several things that could be done in order to make a better case for the feasibility of this approach, which are outlined here as essential revisions.

Essential revisions:

A) Differentiating species: Overall the reviewers noted the need to provide more information or demonstration this can accurately be done. Details towards this include:

-Provide more details on meta data required for differentiation (e.g. biting times, geographic prevalence data (and especially in Madagascar), how do you handle multiple counts… (mosquitoes may be in swarms and same one could be counted many times), discussion of why are some distributions not discernible, how many counts needed to generate a distribution that is discernible (e.g. Figure 4B), and/or what total bandwidth (flight time) needed?

-Along the same lines, reviewers concurred that results as presented do not really demonstrate that given a single measurement the species can be differentiated. Reviewers suggested that perhaps the authors could frame the question differently, instead of: given that the mosquito belongs to species A or B, can we work out which? The problem with this is that of course there are multiple possible species a sample could belong to. Presumably a single measurement would not be able to demonstrate which species a sample came from, but if they record the mosquito for long enough, can the species be determined by comparing the distribution of measurements against their reference bank?

-Also reviewers wondered: with the wild caught Anopheles mosquitoes in Madagascar was it not possible to differentiate the species? Much is made earlier in the text of being able to differentiate members of the Anopheles gambiae complex yet this isn't done in the wild. Was this because species were not identified in the field or because they could not be distinguished? Either way this should be highlighted.

-Discussion of how does the inter-species variability relate to the intra-species variability. Comparison of wild caught mosquitoes shows that the inter-quartile range is substantially different (non-overlapping) and varies between different sized individuals in the same population. The magnitude of this variation seems greater than the difference between species the authors say it can differentiate though this is not mentioned. Comparison of the wild and colony mosquitoes is not done and should be discussed.

-One reviewer also noted that the statement that Aedes aegypti and Anopheles gambiae mosquitoes can be differentiated by their biting time is wrong. "To my knowledge though An. gambiae are unlikely to bite in the day both are highly active at dawn and dusk and Aedes can certainly be found biting at night. Without the use of this meta-data these mosquitoes could not be distinguished acoustically and this should be highlighted."

-Inter vs. Intra colony and variability: The Materials and methods shows multiple colony mosquitoes of each species though sometimes these appeared grouped together in Results (e.g. Anopheles arabiensis) though at other times they were separated (e.g. An. quadrimaculatus, Figure 3). Nowhere in the manuscript is inter-colony variation mentioned and it needs to be as it is immensely important. If new calibration datasets are needed for each mosquito sub-population the potential for citizen science is massively diminished. The inter-colony, intra-colony and inter-individual variability all needs to be discussed and ideally separated as currently they are all grouped together making it impossible for the reader to determine the accuracy of the method.

B) Classification details and methods: the reviewers suggest the authors consider advanced methods to improve classification (e.g. machine learning) and provide more details on frequency distributions and measurement requirements to around the classification and classification accuracy. Details:

-Classification accuracy (albeit unblended) could and should be presented more quantitatively for the data presented in Figure 3A – at least at the pairwise level (proportion of individuals correctly classified in a mix of 2 species). A more sophisticated analysis might be to sample potentially collocated species from the data in 3A and present multi (>2) species classification accuracy.

-Machine learning methods should be considered to optimise classification accuracy.

-One reviewer also noted that it was not clear why the higher harmonics/overtones (Figure 1C, 2B) were being thrown away in the analysis presented. Even simple random forest methods trained on relative amplitude/frequency pairs (of course other features could be selected, such as measures of spread across a trace) for the dominant frequency and harmonics might offer considerably greater classification accuracy than just the mean dominant frequency.

C) Experiments: The reviewers suggested some experiments to demonstrate that it is possible to discern relative abundance would be helpful. While time may not permit a systematic field study, we offer the following strongly suggested approach for a blinded test (please note it is not the reviewer's intent for these experiment(s) to take longer than the revision time, if the authors do not think these are feasible in the allotted time period please justify why):

-Replicate experiments where the authors mix (at known proportions) individuals from several vector species in an experimental large cage setting, and then get researched blinded to the species mix to (a) sample wing beat frequencies from multiple (or all) insects, and (b) analyse the results to determined predictive/measurement accuracy. If mixing mosquitoes is too hard, then sequential recordings of a mix of mosquitoes in the same environment and blinded analysis might suffice.

D) Range:

-The reviewers noted that given the limited range as described (5cm), it would be helpful to demonstrate that the approach works (or sensitivity of outcomes) if the orientation or distance between the microphone and mosquito are not ideal.

E) Data and accessibility:

-The authors are encouraged to follow open data norms and provide the raw data that went into the figures in the main manuscript as supplements to the paper.

-As well, in line with the aims of the paper the reviewers agreed that it would be great if the authors can elaborate on how Joe Public can actually get started with this (release data and app).

F) More discussion or real applications in terms of mosquito species and limitations:

-The reviewers note that this approach will work well for anthropophilic mosquitoes, but not as well as animal feeders esp. avian feeders that are not attracted to man.

-As well there is high applicability to ID exotics; the authors are encouraged to augment discussion of the approach's relevance to Aedes and, for example current citizen science program in Europe doing also surveys, or towards surveillance of albos in Australia (PLoS neglected tropical diseases, 11(2), p.e0005286)

-These include hard to catch and measure mosquitoes at night (when they are most active). Will size impact the WBF? Most wild mosquitoes are smaller than lab reared. Will this be a confounder to ID? And what about temperature and age?

-The reviewers noted that this would particularly be an appropriate tool to survey for exotic species, especially where the species of concern is known (e.g., Ae. albopictus). It would also be a great tool to measure populations for rear and release programs such as wolbachia and sterile males. In this instance, we need to know the wild population so that effective numbers can be released. Phones might be a great way to do this.

-Oc. sierrensis should be Aedes sierrensis.

-Also, how did they measure WBF? In a bag, or free flying?

-In several places you mention species-specific wingbeat frequencies. They are not really species specific as there is some overlap. Please remove species-specific.

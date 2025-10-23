# Peer review - Round 1

Editors:
- Marc Lipsitch, Harvard TH Chan School of Public Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53886.sa1](https://doi.org/10.7554/eLife.53886.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper shows the process of horizontal gene transfer within a hospital at an unprecedented level of detail and resolution.

Decision letter after peer review:

Thank you for submitting your article "Comprehensive analysis of horizontal gene transfer among multidrug-resistant bacterial pathogens in a single hospital" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Marc Lipsitch as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Neil Ferguson as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper describes an extensive sequencing project of over 2000 bacterial isolates including the mobile elements from an 18-month period at the University of Pittsburgh hospital. Specifically, authors screened 2173 genomes by using an all-by-all alignment with nucmer to identify shared regions of >5kb and 100% identity. Shared sequences were found in 192 genomes across 11 genera, which were then grouped into 51 clusters of related sequences (ranging from 2-52 genomes in a cluster, with 2-4 genera). Within these clusters, they selected a sample for long-read sequencing, to resolve plasmids, and identified 17 plasmids, with 10 present in >1 sample. They then aligned short reads from all samples to these plasmids, to predict which were present in each. For two patients, authors identified epidemiological links suggesting potential transfer of plasmids within a species, as well as two across-species transfers within the same patients. The identification of plasmid transfer both within and between patients is clinically relevant and highlights the value of incorporating long-read sequencing data in hospital-based surveillance for infection control. Combining these sequencing results with epidemiologic data and enhancing them with hybrid assemblies to understand plasmid transfer, the authors compose a portrait of horizontal gene transfer in a well-defined hospital population that is more extensive than any of which I am aware. As a descriptive study and a data set that will be rich for further analysis, this is a remarkable piece of work which can be made better with some further analysis and improved presentation.

The revisions below are taken from two of the three reviews, which found the manuscript valuable but in need of some revision. For the authors' information, we note a dissenting view from one reviewer, who found the significance of the paper to be less. They wrote: "Notwithstanding the scope of the sampling and numbers of strains examined, there is not much in the way of new information or novel findings. The dissemination of plasmids, mobile elements, antibiotic resistance gene, etc. in hospitals and other settings is a topic of numerous publications, and the degree to which genes can be transferred within and among species, sometimes between distantly related species, is well established." They further noted the uncertainty of the transmission inferences and questioned how generalizable the study would be to other kinds of institutions. These points are noted but the opinion of the reviewing editor is that notwithstanding these caveats, the scale and completeness of the study give it adequate importance to be publishable in eLife, pending revisions.

Essential revisions:

1) At no point in the paper is any justification given for the choices made about the limitation to MDR isolates (or really what that means), the 5000 bp identity requirement, the exclusive focus on inter-genera transfer (while the paper does in fact offer some tantalizing discussion of within-genus transfer), or the very limited information given about clusters after the first 5. Also, the Materials and methods do not describe how the decision to further investigate e.g. epidemiologic links or extent of sequence overlap (pairwise versus fully connected) was made. This manuscript is well-organized but gives a bit of an impression that the sequencing was done, and then some lines of inquiry that seemed inquiry were followed up, until a certain amount of time/effort/results, and a paper was written. This is a perfectly fine thing to do, especially with such interesting material, but it leaves the reader wondering what the full story is. The title says, "comprehensive analysis…among multi-drug resistant pathogens in a single hospital." There is a lot of bioinformatic analysis, but the phrase "comprehensive analysis" would suggest that more things were measured and quantified, and the word comprehensive would suggest that within-genus transfers were also identified and considered. Some specific questions that should be answered if possible are:

– Was there a single definition of an inferred transfer event? Is being in a cluster necessary and sufficient for that inference? Should other definitions be considered?

– Is the inferred amount of HGT between genera high or low or intermediate? Compared to what prior estimates?

– How does the amount of HGT between genera compare to the amount inferred within a genus (perhaps normalized for opportunities to see this)?

– What proportion of inferred events have a plausible path of epidemiologic links?

– What is the impact of the 5kb identity requirement – do you get radically different answers with 3 or 10 as cut-offs?

– What descriptions can be given in quantitative terms of the different patterns of what was conserved within a cluster between C1 and C2, C3? What about all the other clusters?

– What proportion of the inferred events involve mechanisms of horizontal transfer consistent with what we already know (e.g. plasmid transfer, ICE, etc), and which are unexplained by those?

– How do the inferred rates of evolution from the inferred transfer events compare with what we know? The Tn7 comment is tantalizing but is one example – a comprehensive analysis would consider the overall patterns.

– What was the extent of movement of MDR determinants together among inferred events?

Perhaps not all of these can be answered, but to ignore them seems unfortunate in a paper with such a grand title. I don't want to dictate the publication strategy for what will undoubtedly be a series of papers, but a paper in eLife that is called a "Comprehensive Analysis" should not, for example, consider only transfer between genera.

2) Authors state the epidemiology of MGEs in clinical settings requires detailed individual level data, but actually provide nearly no epidemiological data in the current manuscript. I would have expected a table at a minimum outlining the demographics and clinical characteristics of the patients included (N=2173). It would also be helpful to know more about the demographics and clinical characteristics of the patients whose isolates share sequences by cluster (N-192). For example, looking at Figure 1B, I note there are 13 clusters containing Stenotrophomonas – 12 of which are clustered only with Pseudomonas. This would suggest to me that these may be patients with Cystic Fibrosis, as both pathogens are commonly found in the CF lung, but it would be helpful to know this information to better assess the clinical relevance of this work.

3) Authors did long read sequencing on a subset of "representative isolates from the largest clusters" – what do authors mean by “representative” here? Do they just mean they chose a random sample from within each cluster? Please explain.

4) Much of the interpretive material is confusing or questionable.

– The sentence “Taken together, these results indicate that while many of the sequences we identified were shared between related bacterial genera, our approach also identified sequences that were identical in the genomes of distantly related pathogens.” took about four reads before I decided it simply meant there was a lot of sharing among close genera, and some sharing among more distant genera. A more parallel structure to the sentence could clarify (if that is indeed what it means). A reference to Figure 2 could also help.

– Discussion section: "generate biased interpretations of the driving forces": I don't see any interpretation of the driving forces behind HGT (or as I imagine driving forces, behind the success of lineages which have undergone HGT, such as transmissibility or antimicrobial selection pressure or the like) in this paper, and moreover, biased interpretations can be biased only relative to some defined estimand. This seems like unduly vague language, and maybe should be replaced with "incomplete accounts of the extent of HGT" or something similar.

– Discussion paragraph three is somewhat peculiar. It seems to rest on the premise that if an element moves to a new host, it will be selected to change its sequence to adapt to that host, but then undermines that premise with hypotheses 2 and 3. This may be just a matter of wording, but it seems confusing. Maybe sequences are adapted to generic functions (e.g. neutralizing a drug) rather than to the bacterial host. At a minimum the wording should be changed; better would be, instead of giving one example of each, to try to classify the clusters based on these explanations. Again, this is part of the distance between "comprehensive analysis" and the more descriptive tone of the paper.

– "both plasmids…from the same patient were nearly identical to one another, suggesting that they were indeed transferred shortly before the bacteria were isolated" – over what timescale might we expect difference to occur in plasmids and of what magnitude?

– "underscores how quickly MGEs can move" – this makes no sense. MGEs move by for example conjugation which has been measured in the lab as taking minutes. The literal movement is of course fast. I think finding evidence of transfer that is close together in space and time is unremarkable; finding persistence over time is more remarkable.

– Some of the other conclusions seem a bit unsupported by the analyses that are conducted – e.g. "the fact we only observed plasmids in closely related bacterial lineages suggests that they are well-adapted to these lineages, and if they were transmitted to other STs they were likely lost due to instability and/or fitness costs". I would think this could easily be affected by sampling strategy used, with only invasive samples of select species.

– Figure 1D and E just show the proportion of clusters with X gene type or Y AME gene, respectively, but underlying cluster sizes range from 2-52 – shared across all samples. Is there a way authors can standardize by cluster size, as I am not sure a cluster of 2 should have the same weight as a cluster of 52 in these analyses?

– Authors required a minimum of 5kb and 100% identity on nucmer and state these cut-offs were arbitrary (Discussion) – did authors examine any other cut-offs and how do their findings change if these are adjusted?

5) Authors report that they aligned short-reads from all of the isolates to the reference sequences they generated for cluster-containing MGEs (chromosomal or plasmid). They then assessed the coverage (whether this is the% alignment to the reference or depth is unclear – please clarify) to these references to predict whether the respective genome contained the MGE or not. However, I could not find a table showing these results. It would be very helpful to have, for each isolate, the percent of each of these references covered and the median depth of coverage in order to assess the reliability of these results. At a minimum, this should be provided for the plasmid analysis, wherein they found 93 isolates had cluster C1-C5 sequences of 17 plasmids.

6) Transmission analyses – Given the high percent identity between plasmids, the results suggesting transmission of plasmids between patient A and B look quite convincing. However, it would help to have the dates of sample collection for each of these samples. Currently, authors just state patient B's isolate was collected after patient A's. As these are invasive isolates only, it is also is possible that transmission occurred via a colonized intermediary who was not detected due to the study design.

7) A major conclusion authors reach is that some plasmids carrying putative MGEs "were likely inherited vertically as bacteria were transmitted between patients in the hospital." I am a bit surprised not to see any analysis to assess whether the bacterial chromosomes were indeed the same as well as the plasmid given authors have complete Illumina data for these isolates. Authors could easily align reads to a chromosome reference from the respective ST and assess whether this is indeed probable, rather than speculating based on the MGE/plasmid analysis alone.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Systematic detection of horizontal gene transfer across genera among multidrug-resistant bacteria in a single hospital" for further consideration by eLife. Your revised article has been evaluated by Neil Ferguson (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Specifically, we have one remaining concern regarding the 5kb threshold for the cluster analysis. The 5kb threshold (which was used in your original analysis), produced 51 clusters. As requested by reviewers, in the revised manuscript the clustering results with >3kb and >10kb are now shown. However, compared to the 5kb threshold, using a 3kb threshold results in 120 clusters, while using a 10kb threshold results in only 16. Despite finding such a wide range in clustering due to this, this has not been discussed anywhere in the current paper – or the implications this would have on the conclusions. It therefore seems like the results are very sensitive to the threshold used, so this should at least be discussed in the paper as a limitation of this work.

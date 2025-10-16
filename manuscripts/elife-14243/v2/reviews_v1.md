# Peer review - Round 1

Editors:
- Julie Ahringer, University of Cambridge , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.14243.069](https://doi.org/10.7554/eLife.14243.069)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Constitutive H2A.Z turnover at yeast promoters requires the preinitiation complex" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Julie Ahringer, is a member of our Board of Reviewing Editors and the evaluation has been overseen by Jessica Tyler as the Senior Editor. Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The reviewers appreciated that you were addressing an interesting question, but agreed that your data did not support your central conclusion that the transcription machinery has a direct role in H2A.Z disassembly (explained in detail in the individual comments). For example, the multiple effects of Kin28 depletion meant it was not possible to assign phenotypes to a particular pathway, so the role of promoter escape could not be addressed. A significant amount of new work would be needed to make the paper acceptable, which is not compatible with a revision in eLife.

Reviewer #1:

This paper investigates the mechanism of eviction of +1 H2A.Z nucleosomes at promoters. The authors deplete factors that are expected to affect PIC assembly, H2A.Z deposition, or transcription, and then assess for H2A.Z abundance using a semi-quantitative ChIP method. There are some interesting initial findings here but at present they do not allow clear and strong conclusions. Some conclusions drawn are stronger than the data allow, sometimes due to the nature of the perturbation and sometimes due to issues with data analyses.

Explanation of how replicates were treated is not sufficient and there is no assessment of reproducibility of results. These need to be explicitly explained in the methods. The only details I could find were in the Figure 1 legend: “The data in A-D represent the unsmoothed mean of 3 to 5 independent ChIP reactions (technical replicates) from two separate cultures (biological replicates).” The methods should indicate how many replicates were done for each experiment, the concordance between replicates, and how pooling of data was done. The authors need to show that similar results were obtained in independent experiments.

It is not appropriate to use the change of Z/A ratio to measure H2A.Z dynamics. The numerator and denominator are not independent, so linear changes in occupancy result in non-linear changes in the factor. For example, if Z changes from 90% to 80%, (10% change), then the change in Z/A ratio would be 90/10 compared to 80/20. 9/4 = 2.25 fold. Also, this measure is biased, as it is differently sensitive at different levels of H2A.Z occupancy. If the change H2A.Z changed from 50% to 40%, the change in Z/A ratio would only be 1.5, whereas it becomes sensitive again at low H2A.Z levels. This also causes problems in the statistical treatment since Z/A ratio values vary significantly for a similar change in H2A.Z. Instead, the change in H2A.Z should be directly assessed and compared, as the authors eventually do: "We also plotted the change of H2A.Z-over-input, Δ(H2A.Z/input), and found this parameter less sensitive but more unbiased (Figure 1—figure supplement 5C)." The ratio assays should be removed.

The experiment simultaneously depleting TBP and Swc5 is not interpretable, as the result will depend on the relative depletion of the two factors, which is unknown and not controllable. The individual depletions are however, informative.

The Kin28 depletion to assess the impact of promoter escape is problematic because Kin28 loss both reduces the amount of PIC assembly and prevents escape when a PIC is assembled. As the authors don't know the level of PIC assembly defect compared to the promoter escape defect, the experiment is not interpretable. A ChIP of TBP could be helpful here.

Reviewer #2:

This paper makes the interesting observation that depletion of TBP from the nucleus, which precludes assembly of the PIC, results in an increase in H2A.Z at the +1 nucleosome. This persuasively implies an antagonism, and subsequent experiments suggest that the increase in H2A.Z is due to decreased removal rather than increased recruitment (but see below). This isn't too surprising, but it's a nice result. Less convincing is an experiment arguing that depletion of the Kin28 subunit of TFIIH, which supposedly allows PIC assembly but not promoter escape, does not produce the same effect on H2A.Z. The authors want to conclude that some post-PIC, pre-escape step actively targets H2A.Z nucleosomes at +1, but here I found that their models went too far into unsupported speculation (see below).

Major issues:

1) In the third paragraph of the Introduction section, the authors state that it's completely unknown what dissociates H2A.Z. I thought perhaps they were unaware of the paper from Craig Peterson claiming it's Ino80 (Papamichos-Chronakis et al., 2011), but then they cite this paper in the sixth paragraph starting of the Introduction section. Even if they don't find the Papamichos-Chronakis convincing, in my opinion their discussion is overly biased. Is it fair to characterize the Papamichos-Chronakis data for occurring under "certain in vitro conditions", when it's not that different from the Swr1C data? The authors also imply that the Ino80 model lacks in vivo support. It's fine to cite the Jeronimo paper as showing no effect of Ino80 on Htz1 ChIP, but you have to acknowledge that ChIPs in the earlier paper from Papamichos disagree.

2) Sixth paragraph, Introduction section. On a related point, I don't see how H3/H4 turnover argues against specific remodelers taking out H2A.Z. There's no reason complete nucleosome eviction (by Swi/Snf, for example) is mutually exclusive with additional specific removal of the H2A/H2B or H2A.Z/H2B dimers.

3) Figure 2C,D is not completely convincing. While the compiled tag counts on the left suggest the double depletion is less severe than Swc5 alone, the scatter plots at the right make it clear the change is pretty subtle. It's hard to reconcile the numbers from the left panel (sixth paragraph of subsection “PIC assembly is required for genome-wide H2A.Z eviction at promoters from both active and quiescent genes”: 7.5 fold loss of H2A.Z, versus 2.4 fold) with what looks like a more modest difference in the scatter plot. In any case, even with the more severe numbers, the results seem to me to strongly argue that there are probably multiple mechanisms related to clearing H2A.Z, only one of which is transcription.

4) Subsection “H2A.Z eviction occurs at distinct stages of transcription”. The experiment using Kin28 depletion as a method for blocking promoter escape just isn't convincing, especially since this also affects PIC assembly (as noted by the authors). How can we be sure that the difference in H2A.Z response between Kin28-FRB and TBP-FRB isn't due to differences in the kinetics or completeness of nuclear depletion? In the paper from the Robert lab cited for the Kin28 depletion, they actually rested most of their conclusions on chemical inhibition of the kinase rather than the anchor away system. That would be a better way to test the hypothesis in this paper.

5) Subsection “H2A.Z accumulation in the absence of TBP can be used to determine internal and cryptic transcription start sites”. The data for the internal start site in GHD2 looks good, and there is also the CUT in the antisense direction, so it's nice to see the double peak in the Htz1 signal representing internal bidirectional transcription. However, I just don't see the alleged internal start site in HSE1. Also, it's probably worth noting in the text that using H2A.Z as a marker for internal start sites will not tell you which direction transcription is going.

6) First paragraph Discussion section. Perhaps I missed it, but what data shows constitutive turnover of H2A.Z at quiescent genes? Please cite which figure. How is quiescence even defined in yeast, where even "silent" genes may fire occasionally? Did the authors look at truly silenced promoters, for example, those within HMR and HML?

7) Second paragraph Discussion section. There's no justification for invoking recognition of Htz1 by the PIC. It could just be that Htz1 is put at ends of NFRs preferentially, and firing off of the PIC dissociates it. Indeed, the model proposed by the authors where TFIIH-mediated scanning displaces H2A.Z does not require PIC recognition or even direct interaction with +1 nucleosome.

8) Same section as above. Similarly, I can see no basis whatsoever in the data to say that H2A disassembly is transcription independent. I would say authors' model should instead predict that TBP depletion should result in an overall increase in +1 occupancy, independent of whether there's H2A.Z is there or not. Would the authors' normalization scheme obscure overall changes in nucleosome occupancy?

Reviewer #3:

This manuscript investigates the effects of pre-initiation complex (PIC) recruitment on promoter nucleosome dynamics. An elegant conditional depletion approach is used to achieve this. The main observation made is that enrichment of the histone variant H2A.Z increases upon removal of the PIC. This indicates that the PIC normally is involved in a process that depletes H2A.Z from +1 nucleosomes countering the action of the Swr1 complex that normally acts to increase H2A.Z at these locations. This suggests that enrichment of H2A.Z at promoters is normally the result of a dynamic equilibrium between incorporation and removal. The manuscript then proceeds to show that sites of H2A.Z turnover can be used to identify cryptic start sites for transcription. These finding represent important new insights into how chromatin is organised at promoters. Overall the data are of high technical quality and presented clearly.

The interpretation made in the manuscript is that the pre-initiation complex directly acts to displace H2A.Z from promoter nucleosomes. For example the possibility that migration of a bubble of separated DNA at the PIC could drive this is discussed. However, there appear to be alternate explanations that are not mentioned. One is that TBP is required for recruitment of or is co-recruited with another factor that acts to destabilise H2A.Z containing nucleosomes. A second is that an unidentified factor acts with partial redundancy to incorporate H2A.Z, and that this factor is excluded from, promoters when the PIC is present. The authors should consider incorporating discussion of the potential for alternate explanations that do not involve the action of the PIC directly removing H2A.Z.

It would also appear to be quite easy for the authors to look into whether the effects on H2A.Z are more strongly correlated with SAGA or TFIID regulated genes. It would be useful if this could be mentioned in the discussion.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Constitutive H2A.Z turnover at yeast promoters requires the preinitiation complex" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Julie Ahringer, is a member of our Board of Reviewing Editors, and another is Tom Owen-Hughes (Reviewer #3). The evaluation has been overseen by Jessica Tyler as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript provides an important step forward in identifying that engagement of the PIC contributes to H2A.Z cycling at promoters. It clearly illustrates that the steady state levels observed are the result of an equilibrium between directed incorporation and removal. This is likely to be of significant general interest. They also provide evidence that INO80 does not play a role in +1 nucleosome dynamics. This helps to address a topical and somewhat controversial subject. The results advance our understanding of promoter regulation.

Essential revisions:

1) The authors propose a model where the PIC somehow actively removes Htz1, even though there's no precedent for such an enzymatic activity. Depletion of TBP or Pol II doesn't simply reduce PIC assembly; it blocks all subsequent steps, most notably transcription itself. The data in this paper are also consistent with promoter escape, elongation, or termination being involved in removal of Htz1. Statements concluding an active role of the PIC in removal of Htz1 should be toned down, e.g.:

"Impact statement: The transcription machinery disassembles the promoter-proximal H2AZ nucleosome […]";

"These findings suggest that the Pol II transcription machinery plays a more active role than previously through in the remodeling of chromatin structure within promoters";

"We show that the Pol II transcription machinery has a chromatin remodeling activity…".

2) As their model figure shows, this is a cycle. Given the documented affinity of SwrC for the free DNA in the NDR, a much simpler idea is that binding of the PIC blocks SwrC association. Depletion of TBP or Pol II would allow more Swr binding, leading to an increase in Htz1 occupancy. Even on infrequently transcribed genes, there may still be PIC assembly without productive transcription. And Swr1 may continually recycle Htz1 even on non-transcribed genes with an unoccupied NDR. These alternative possible mechanisms for changes in Htz1 occupancy should be discussed.

3) A paper from Randy Morse's lab (Ansari et al. (2014) Mediator, TATA-binding Protein, and RNA Polymerase II Contribute to Low Histone Occupancy at Active Gene. JBC 289, 14981-14995) used TBP depletion or Kin28 inhibition and concluded that the entire +1 nucleosome (rather than only H2AZ) decreased in a "PIC-dependent" manner. This paper should be cited and the differences discussed.

4) Yen et al. 2013 observed that in an Arp5 mutant H2A.Z occupancy is significantly increased at promoters. This paper is not cited. It should be cited and included in the discussion of studies that have looked at the role of Ino80 in H2A.Z turnover. Currently 2 studies provide support for INO80 acting in H2A.Z removal and 2 against. The value of the manuscript would be improved if a plausible explanation for these discrepancies could be identified.

5) The relative profiles of H2A and H2A.Z in no RAP in Figure 1C and D (TBP-FRB and no FRB backgrounds) differ, with lower relative H2A.Z in the no FRB background. The Z/A ratio is higher in TBP-FRB with no RAP than in untagged control with no RAP. This difference is also evident in the correlation diagrams in Figure 1—figure supplement 5, comparing the two no RAP experiments. Can the authors comment on these differences and how they might affect confidence in the observed changes in +RAP conditions? How do these differences relate to the variability in Z/A ratio between replicates? The difference is important, because the authors used the untagged control to determine significantly affected regions in Figure 1F (explained in Figure 1—figure supplement 6).

6) To confirm the qChIP-seq results, the authors tested H2A.Z levels at three nucleosomal regions and two coding regions by qPCR. To increase confidence in this control, the FT fraction should also be assessed, along with levels of H2A in both fractions.

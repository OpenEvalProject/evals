# Peer review - Round 1

Editors:
- Genevieve Konopka, University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69479.sa1](https://doi.org/10.7554/eLife.69479.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study identifies functional enhancers in vivo in the postnatal mouse brain using massively parallel reporter assays. The authors also carry out a number of validation assays to support their findings and show how the approach can be generalizable to other questions.

Decision letter after peer review:

Thank you for submitting your article "Parallel functional testing identifies enhancers active in early postnatal mouse brain" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kathryn Cheah as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Stefan Barakat (Reviewer #1); Joseph D Dougherty (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Please either provide additional experimentation to address these two points or at least discuss why they should be done but you have not provided that data in this manuscript.

1) Additional negative controls.

2) Assessment of CACNA1C variant activity.

Reviewer #1 (Recommendations for the authors):

The authors perform an in vivo screening to identify functional enhancers in early postnatal mouse cortex by means of a massively parallel reporter assay (MPRA). To this end they designed an MPRA library containing 408 human DNA sequences with potential regulatory activity in the brain and choose an AAV vector for delivery of the reporter library. With this approach 41 amplicons with regulatory activity were identified, including the ones located in the disease-associated third intron of CACNA1C. By performing miniMPRA screening of orthologous mouse sequences, the authors confirm the reproducibility of the approach and provide evidence for cross-species conservation of regulatory elements' function. In a series of confirmation experiments the authors validate the activity of a small number of individual amplicons and, also show that the cell type specificity of a small number of investigated enhancers is preserved in this reporter assay. The described methodology might be instrumental for further in vivo studies of regulatory elements.

Strengths:

The study successfully implements a MPRA in an in vivo system and highlights considerations for the experimental design.

Weaknesses:

As also noted by the authors in the discussion, the approach does not yet allow to compare the activity of sequence variants in this assay, which will be crucial for understanding the effects of variants on regulatory function. The number of regions assessed is relatively small, and this might be a bottleneck to apply this approach to study regulatory elements at large scale.

I would like to congratulate Nord and colleagues for an interesting application of STARR-seq in vivo. I think the manuscript is definitively interesting, but sometimes I feel the statements are a bit overrated, and I would suggest that the authors tone down a bit on some of their claims. Also, there could be a few experiments added to further strengthen the quality of the paper.

My specific points, in order of appearance in the manuscript:

– If I understand correctly, the authors start off with 408 regions of interest that they start to clone, but then in line 108 they say that they could upon batch cloning, only verify the presence of 345 of these regions. Why is that? Just failed PCRs for the remaining 63 regions? Is this introducing any bias that should be explained perhaps? Perhaps also good to keep in perspective that 408 regions of interest is rather small, and finding 41 of them as active is not a lot (also given that there were several layers of pre-selection for putative regulatory regions to reach to the 408 regions); Just in general, one might think how many enhancers are required, to put on the label "massively parallel reporter assay"; a question that perhaps also remains unanswered in the manuscript is how likely the author find it that such an approach can be further up-scaled, to investigate the many millions of putative enhancers or GWAS SNPs that are there for human brain?

– In line 94-99, the authors describe the different groups from which their regions of interest were selected. Amongst this, DNaseI hypersensitivity sites were chosen. In line 170, the authors then mention that amongst the region they found active, there was a significant enrichment for loci characterized by DNaseI hypersensitivity. How much of that is explained by the selection bias of selecting those regions in the first place? Same for the putative enhancer group that was used; I assume the reason that these enhancers were putative enhancers in the first place, was their epigenome landscape. So is significant enrichment for H3K4me1/3 then really surprising? The authors should comment on that potential bias, and explain whether their statistics correct for this. Especially given the weight that the authors put on these findings in their conclusive sentence in line 184-186. Some of this information might be in Figure 2C, but is not really clear to me.

– In the section "Confirmation of in vivo P7 cortex MPRA enhancer results" the authors do a couple of validation experiments, to show that their STARR-seq active enhancers show cell type specific enhancer activity. Although important, I feel that the number of enhancers studied in here is very small, so I am not sure that the data will allow to justify broadly extrapolated conclusions from this handful tested sequences. Preferably, the authors should extend this analysis, including more enhancer loci, and perhaps also include experiments in which they test the orientation of the enhancer insertion into the STARR-seq plasmid. E.g., does it affect the activity and cell type specific expression if an enhancer is cloned in the sense or antisense orientation in the STARR-seq cassette? This would also be important to know if one would apply this assay at a larger scale (e.g., testing millions of sequences at ones, in which bulk cloning would probably cause different enhancer orientations in the library). In a way, it doesn't seem so surprising that a reporter assay that has already been validated in many studies (e.g. STARR-seq), seems to behave as a bona fide reporter construct (e.g., if the authors were to clone their validation enhancers in a lacZ reporter, they would probably see the same). So despite being a good control, it is also not such a "special" finding, so I think looking at the sense or antisense orientation might be more impact full?

– In the discussion (line 373-374), the authors say that their assay was not designed to directly compare sequence variants for activity; I don't see why? Would that not be something to include, for example for the CACNA1C locus, to test activity of variants in some of the SNPs in the enhancer regions they found? By including such an experiments, I think the author could increase the impact of their study, and this could be "the icing on the cake", which I feel in the current manuscript is still a bit lacking to some extent.

– Technical question: in line 494-495 the authors describes the STARR-seq library prep. In the original STARR-seq protocol from Stark and colleagues, and also later used by us and others, there is a two-step PCR protocol, with the first set of primers spanning an intron in the STARR-seq plasmid (thereby repressing any potential remaining plasmid DNA contamination) followed by a second round of nested PCR to amplify the amplicons themselves; both PCRs together have <30 cycles. In this paper, the authors use a single set of primers, and amplify both RNA and DNA samples 30x; why is that? Did they modify the original STARR-seq cassette in their adenoviral application, to no longer contain that intron design? What is the reason behind that? Could this be a reason for only a modest number of regions where they find an increased RNA/plasmid ratio? Please explain.

Reviewer #2 (Recommendations for the authors):

Summary: In this paper the authors develop a high throughput assay for in vivo enhancer activity, adapting an MPRA/STARR-seq AAV approach. They use ~900 bp candidate enhancers, selected from the human genome with 4 different strategies for selection, and successfully screen ~300 of these, including some from psychiatric disease loci. They then validate a handful in single construct injections. The major claims are (1 ) that they developed a 'self transcribing regulatory element MPRA strategy' for mouse forebrain. and (2) and validated enhancers that worked in mouse forebrain, including one from an intronic CACNA1C block that is in linkage with disease associated regions.

Major Strengths and Weaknesses: The strengths are that they were able to successfully screen a much larger number of enhancers in a single experiment than prior approaches, and that they included careful first-pass validation of some of these by microscopy in independent animals. The particular approach chosen, PCR cloning of amplicons, also allowed for longer elements to be studied than some of the oligonucleotide based libraries. I also thought the step during validation using co-injection of the test construct with GFP with the positive control in RFP was a very elegant way to control for locus of injection. However, there are some places where the next study building on this one might be I improved; drawbacks to the approach were (1) the lack of a good set of null sequences/negative controls in the MPRA that would have helped define what basal activity looks like. This lack made the analysis steps a bit more challenging, though their relative ranking of most active to least active elements is still likely accurate. (2) As admitted by the authors, the embedding of the enhancers in the UTR can risk conflating posttranscriptional effects of the elements (e.g. Poly A signals, miRNA binding sites) with enhancer effects (though this likely does not explain the activity of their strongest, validated elements). (3) There will be room for improvement in measurement of the enhancer activity by RNA sequencing in the assays, as correlation between biological replicates was not ideal (.54-.842). The noise in the assay can likely be overcome with additional replicates or additional improvements in library delivery or recovery steps. Such improvements might also allow for an increase in the number of elements assessed in parallel.

Likely impact: I think the study demonstrates feasibility for assaying hundreds of assays in parallel for activity in the brain (and similar approaches could be taken for other tissues), and provides a good foundation for future improvements to similar approaches. As it stands, it should be useful for screening more genomic loci for the most active candidate sequences. It also validates a handful of enhancers that do have function, including some in disease associated loci. These validated enhancers are potentially useful tools: understanding the cell types they express would provide some hints as to the cell types important for the disease, and having defined them also provides an opportunity to study the impact of human risk alleles on the function of these specific enhancers.

I have some concerns on the statistical approach I would like to see clarified, but I would say it is likely these are addressable. I also have some suggestions to improve flow and impact.

Concerns:

The MPRA design would have certainly benefited from a larger number of negative controls or blanks to help define which elements had enhancer activity. Something similar to https://www.pnas.org/content/110/29/11952/tab-article-info where they used scrambled sequences to understand what random genomic sequences look like, then defined enhancers based on an activity that was higher than random. That being said, the analysis they conducted does allow them to identify the sequences with the most and least relative activity. So it is probably of use even without this control if it is not feasible to add.

I could use clarification on the statistical approaches though, to be able to fully evaluate them. Use of residuals is not unheard of, but it is a bit unusual and I have a few questions I would like clarified. Specifically:

1) I am confused on the linear model as to why they authors included GC content. If, as per line ~137, no further GC bias arose after cloning, then if the model already accounts for DNA amplicon count, then the remaining effect of GC on RNA might be biological rather than technical. Perhaps high GC content correlates with more enhancer activity or RNA stability? This has certainly been seen in other studies. The authors could rerun the model without the term for GC and see how similar the results are, and see which model better predicts their existing follow up data or some of the genomic enrichment assays.

2) Overall, the authors have 2-4 different statistical approaches to picking the hits from the data they tried. Fortunately, these correspond to each other fairly well. Still, it might be helpful to use some kind of benchmarks (e.g., enrichment for overlap with the epigenomic datasets perhaps?) to determine which ought to be the primary analysis that is presented.

3) Line 539 I could also use a more clear explanation (or reference) to explain how they convert the Z-score of the residual into a p-value.

4) And, when conducting the Wilcoxon rank sum, what are they comparing each enhancer to?

5) In the end, regardless of which statistical method they lead with, they ought to make sure to also correct for multiple testing. It is not clear this was done here.

Suggestions to improve the impact:

The library is actually made of 4 sub-libraries. Are there any differences in activity between the four sub libraries? Is there anything we can learn about the relationship of LD SNPs to function, or the efficicacy of epigenetic marks at predicting function by comparing the 'hit rates' between these 4 libraries?

It is also unclear if they ended up with multiple alleles in the cloning. They cloned from a pool of DNA, so presumably different haplotypes were present. If so, were they powered to look at the allelic effects of in the functional enhancers? Or assess any in follow up?

Finally, it would bolster their second claim a bit if they did some more in depth characterization of the enhancers they validated. Are they expressed only in neurons, or neurons and glia? Are they specific to a subpopulation of neurons (at least excitatory vs. inhibitory?)? Recent comparable AAV/enhancer screens have done more in this regard, and it could be a nice deliverable of this paper if one of these enhancers happens to target a useful subpopulation. Or if it helped us better understand the regulation of some of the psychiatric disease genes. That would improve impact and it seems they have the reagents in hand to do these studies.

Suggestions on writing:

Regarding figure 1B – are the elements with sig negative residuals thought to be repressors? It might be worth discussing. Are they enriched in any particular marks?

It is good the authors discussed some limitations to cloning candidate enhancers into the 3'-UTR position, as they might have some effects on the RNA level via post-transcriptional regulation. Also, sequences containing elements that would have obvious negative consequences (e.g., poly A signals) on the assay might need to be filtered out, especially when looking at repressive sequences.

To my fresh eyes, it sometimes feels experiments are a bit out of order. For example, some of the controls showing the method should work come after the experiment rather than before it. Specifically, it is just a suggestion, but some of the experiments like those establishing that DLX works regardless of whether it is in 3'-UTR of 5' to the promoter, or perhaps the miniMPRA, might make more sense presented before the main MPRA comes up?

I'd like to see a histogram of the count number of the elements in the DNA library. I am just curious about the range between the best and least cloned elements. Presumably the least well cloned elements are also the 25 % that were filtered out? Also, perhaps some scatter plot of DNA read depth vs. coefficient of variation (with color coding of the 25 % filtered out) might make a nice supplement, and provide a benchmark for future improvements to the method.

Reviewer #3 (Recommendations for the authors):

The article 'Parallel functional testing identifies enhancer active in early postnatal mouse brain' uses an adeno-associated virus (AAV) based high throughput approach (massively parallel reporter assay (MPRA)) to test the regulatory capacity of candidate enhancer sequences in early postnatal mouse brain. To ascertain the reproducibility of enhancer activity across MPRA studies, the authors tested four positive enhancers, two negative sequences, and orthologous mouse sequences via miniMPRA. The results these assays suggest that consistent results can be achieved through in vivo MPRA. Finally, the authors dissect regulatory elements within the CACNA1C intron that have been previously associated with disease (schizophrenia), determining that in vivo MPRA could be an efficient tool for assessing neural disease-associated regions. This paper would be of interest to the broad readership of eLife, primarily due to the use of an in vivo AAV-based brain MPRA and characterization of disease-associated regions. However, several point need to be addressed.

– A lot more information is needed about how sequences were chosen for the MPRA. The authors tested 408 sequences from four groups. How many from each group? Was there other filters to get to 408 for each group and if so what were they? Why did they shoot for this number and not more? Are there technical reasons for this? Was there overlap between the four groups and if so what was it? How did the authors choose candidate sequences in the GWAS and SNP groups? For those (GWAS and SNP) how many overlap predictive enhancer marks?

Would also mention the problem of choosing lead SNPs in text, i.e. these may not be causative SNPs, as they are just the SNPs on the genotyping array.

Would add to Figure 1A, some table/Venn diagram or other that shows the numbers of sequences that were tested for each group to make it easier for the reader to understand what was assayed.

Would mention that the fourth group was intended as a 'potential positive control', correct me if I'm wrong here.

No negative controls were tested. This is vital in most MPRAs to compare to in order to assess activity. This needs to be mentioned and discussed in detail.

– SNPs: The sequences were cloned from 'pooled human DNA'. More info on how many individuals these are, ethnicity etc. is needed here, especially as different alleles could have different function. If the applicants have variant data from their sequenced library that would be great to add. This is even more lacking in the individual testing, in particular for the CACNA1C region, where variant might affect activity. Those definitely need to have info on the haplotype actually tested d.

– The R in the correlation between RNA replicates is poor, just a little above 0.5 in some comparisons. It also appears between viral DNA and GC content. The authors need to explain this and also provide potential causes for the reproducibility of individual assays and PCR stochasticity in the library preparation and cDNA.

– Were samples 4-35 included in the subsequent studies or not? If not, what was their performance, considering the influences of the cycles in preparation. How did the authors de-duplicate reads in line 119? Were UMIs used in the experiment and if so, more info on them is needed.

– In the miniMPRA section line 188-200 it is not clear what sequences they chose? How many? What was the criteria for selecting the sequences? A brief explanation of the sequences in the main text will help the reader understand the experimental set up better. Also, more info on stats in the main text comparing between the MPRA is needed.

– Overall only a small N of sequences was tested individually, so I would reduce the tone that the individual assays validated the MPRA and make it more that these individual ones validated.

– More detailed info on the brain expression of the individual constructs is needed.

– For the CACNA1C regions, other than reporting which haplotype was tested, it would significantly improve the manuscript if both the unassociated and associated haplotype were tested to assay whether they lead to alternate function.

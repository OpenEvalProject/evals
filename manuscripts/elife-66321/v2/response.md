# Author response - Round 1

Authors:
- Marzia Munafò ([ORCID: 0000-0002-2689-8432](https://orcid.org/0000-0002-2689-8432))
- Victoria R Lawless ([ORCID: 0000-0003-0406-6552](https://orcid.org/0000-0003-0406-6552))
- Alessandro Passera
- Serena MacMillan
- Susanne Bornelöv ([ORCID: 0000-0001-9276-9981](https://orcid.org/0000-0001-9276-9981))
- Irmgard U Haussmann ([ORCID: 0000-0002-2764-694X](https://orcid.org/0000-0002-2764-694X))
- Matthias Soller ([ORCID: 0000-0003-3844-0258](https://orcid.org/0000-0003-3844-0258))
- Gregory J Hannon ([ORCID: 0000-0003-4021-3898](https://orcid.org/0000-0003-4021-3898))
- Benjamin Czech ([ORCID: 0000-0001-8471-0007](https://orcid.org/0000-0001-8471-0007))

## Response text

DOI: [10.7554/eLife.66321.sa2](https://doi.org/10.7554/eLife.66321.sa2)

Essential revisions:

The three reviewers agree that this is overall a compelling study that provides novel, interesting and important observations. No major new experimentation is required but the data need to be more extensively described and the authors should also discuss alternative models. Detailed suggestions for changes are found in the constructive reviews but it is important that the authors improve the quality of some of their images, provide additional quantitative information and add better statistical analyses.

We thank the reviewers for their positive evaluation of our manuscript. We have revised the text to expand the introduction, discuss alternative models, and provide more explanation of the data. Furthermore, we have added statistical analysis where relevant and clearly described the analysis in both the figure legends and in the Methods section (see Quantification and Statistical analysis). Please, find below our response to each of the points raised by the reviewers and detailed description of the changes made.

Reviewer #1:

[…] 1. Please include a panel of representative images for mutant phenotypes in OSC and ovaries, not simply a single cell or field of view.

We have added additional representative images for OSC and ovary phenotypes and enlarged the panels where possible, see Figure 1—figure supplement 3, Figure 2—figure supplement 3A, Figure 3—figure supplement 2 and Figure 4—figure supplement 1C. Each knockdown/mutant is accompanied by the relative quantification of the size and number of Yb-bodies. We have provided high-resolution files for each figure, which should improve the image quality over the previous version seen by the reviewers (where the figures were embedded in a word document and subsequently exported to PDF, losing quality at each compression). Individual images of each figure panel can be provided upon request.

2. Figure 2A: what is the source of the sense piRNAs whose abundance is unaltered by loss of Yb, Nup54, or Nup58? Do they map to cluster transcripts or elsewhere in the genome?

We have added an additional panel to answer the reviewer’s question (Figure 2—figure supplement 2B). Most sense piRNAs detected upon knockdown of yb, nup54 and nup58 map to genomic TE insertions, predominantly of the gypsy retrotransposon. Since these sense piRNAs are relatively few in the siGFP control and their abundance correlates with the degree of TE up-regulation in the various knockdowns, we conclude that they are most likely derived from processing of re-activated transposon transcripts. The same analysis on antisense piRNAs is shown for comparison.

3. The authors propose that Nup54/58 play a role in export of flam RNA. Given the bias towards loss of 3′ transcript coverage and piRNA abundance, together with both the involvement of the TREX complex in piRNA biogenesis and the role of nuclear pore proteins in transcriptional elongation, isn't it more likely that Nup54/58 promote transcriptional elongation across the entirety of flam or that they prevent premature termination in the 3′ region of the flam gene? The authors should at least discuss these alternative explanations, detailing the evidence supporting or refuting each.

We have added discussion of this potential explanation in the text. Overall, we agree with the reviewer that an effect on transcriptional elongation and/or termination is plausible, however our data are not sufficient to strongly support or refute either explanation. We noticed that knockdown of yb leads to a mild reduction of PRO-seq signal over the entire flam cluster locus, possibly hinting towards a negative effect on transcriptional elongation in cases where this transcription-coupled export axis is disrupted. In conclusion, we believe that our data support the conservative hypothesis of Nup54 and Nup58 involvement in flam processive export, with destabilisation of the transcript upon their absence. Future work will shed light on the mechanisms underlying flam transcription, which is beyond the scope of the present study.

4. Page 18: since the mutant ovaries are small (please show ovary and ovariole images of what exactly this means!), then the cell composition of the controls and mutants will be quite different. Early stage ovaries will have a higher the ratio of follicle cells cytoplasm to nurse cells, since nurse cells will be smaller. Thus, it is not simple to normalize RNA or piRNA sequencing data to permit comparison between the two types of ovaries. This problem is exacerbated by the authors' finding that both TE and mRNA expression changes in nup54MB/9B4. A detailed description of the experimental evidence that explains why the authors' normalization strategy allows such a comparison is essential. Additionally, the authors need to show (e.g., by in situ hybridization) that TE expression is in fact higher in vivo in identical cell types.

We have now provided a brightfield image of ovaries from nup54MB trans-heterozygote mutants. As one can appreciate, the mutant ovary morphology is grossly normal and only slightly smaller in size compared to controls, unlike other piRNA pathway mutants described in the literature. We did not observe any striking changes in the relative abundance of nurse or follicle cells, and therefore have no reason to question our normalisation strategy, which is routinely used in the field. We would like to emphasise that other published piRNA pathway mutants/knockdowns have far more rudimentary ovaries than our nup54MB/9B4, e.g. the piwi mutant and somatic knockdown of piwi in Olivieri et al., 2010. Another example is from our group (Eastwood et al., eLife, 2021), where we showed that germline knockdown of ctp leads to severe atrophy of the ovaries (Figure 1G). The corresponding RNA-seq normalisation has been carried out similarly to the one we used in this study.

Reviewer #2:

[…] General remarks/questions:

The paper is quite dense and sometimes difficult to follow when going back and forth between the multiple figures. It may be worse trying to simplify in order to strengthen the overall message.

We thank the reviewer for the feedback, we have now expanded the text to provide more detailed explanations and to clarify the overall message.

Figure 2 figure supplement 1G: this experiment suggests that flam transcription is affected in siYb, but not in sinup54/58. How could loss of Yb affect flam transcription efficiency?

This result, which is in accordance with previous findings (Murota et al., 2014), might be explained in two possible ways. First, residual flam RNA that is exported via Nup54/58 does not aggregate into discrete foci, due to absence of Yb, and is therefore hardly detectable by RNA-FISH. Second, our PRO-seq data shows a mild reduction in global flam nascent RNA levels upon loss of yb, which is more apparent towards the 3’ end of the locus. Although the molecular mechanism is not readily apparent, this might support the idea that flam transcriptional elongation is somehow dependent on its downstream processing into piRNAs. A minor fraction of flam-derived piRNAs is antisense to the cluster, so we cannot exclude that those might base pair with the nascent flam RNA and contribute to its transcriptional rate. Further investigation of the mechanisms underlying flam cluster definition and transcription will be required to clarify this.

Figure 2 figure supplement 2G: this figure indicates that the Yb bodies and the flam DNA don't show an obvious proximity or correlation (on either side of the NPC). This is unexpected based on the model that Nup54/58 establish a physical connection between Nxf1/Nxt1-bound flam RNAs and their delivery to Yb bodies on the cytoplasmic side of the NPC. This observation is not really discussed in the text and should be clarified since it is somewhat questioning the model presented in Figure 4G.

This observation is in line with previous works (Dennis et al., 2013; 2016). We suggest that the nucleation of Yb-bodies initiates wherever flam transcripts are exported, irrespective of their transcription site.

Figure 2 figure supplement 2H is shown too early since it is linked to Figure 3C.

We thank the reviewer for this slip. Former panel 2H has now been moved to Figure 3—figure supplement 1A.

Figure 3A: the authors should indicate what the red domain in Nup54 corresponds to. Is it the same region lacking in the nup54MB mutant?

The purple box indicates a Nup54-family domain, which is absent in the nup54MB mutant. This information was already included in the legend of Figure 2A and we have now clarified the description of the nup54MB allele also in the main text.

Figure 3 figure supplement 1E: Yb staining shows quite clearly that the nup54MD presents reduced Yb body formation. However, it is not clear why DNA staining reveals larger foci in the nup54MD mutant?

The nup54MB allele is a hypomorph. Some ovarioles of the nup54MB/9B4 trans-heterozygotes seem to have a less organised pattern of follicle cells, which often show slightly larger DNA foci. These ovarioles show the most pronounced decrease in Yb-body assembly, thus suggesting that they are the ones where the effects of the Nup54 mutation are most pronounced. However, this phenotype is not fully penetrant and we have now added a second representative image where the DNA foci are more similar to the control.

Figure 4 and supplements: the mass spec data indicate that Nup54/58 interact with Nxf1 and Yb, consistent with their proposed role in coupling flam RNA export and its addressing to Yb bodies. However, Yb does not efficiently interact with Nup54/58 nor Nxf1 by mass spec. It is unexpected that Yb does not interact with Nxf1, since Nxf1 is expected to transport flam RNAs to the cytoplasmic side of the NPC through interactions with Nup54/Nup58 in order to deliver the transcripts to Yb. co-IP experiments (Figure 4 figure supplement 1D) then show that Yb weakly interacts with both Nup54/Nup58 and Nxt1. Why do the authors think that the weak interaction detected between Yb and Nup54/58 is more functional than the weak interaction between Yb and Nxt1?

When does Yb bind Flam transcripts and wouldn't it be expected that Yb interacts with Nxf1/Nxt1 to take over the flam transcripts? This question should be more clearly addressed in the text or discussion.

Our co-immunoprecipitation experiments detected a weak interaction between Yb and Nxt1, but not between Yb and Nxf1. Since Nxf1 and Nxt1 are usually present as a heterodimer, we did not speculate further about this interaction being functional. We agree with the reviewer that the “handover” of flam transcripts from Nxf1 to Yb is not entirely clear and may involve interactions between Yb and Nxf1/Nxt1 or other adaptor proteins that we have not yet identified. We believe that super-resolution imaging of individual NPCs might clarify the relative position of each component of this export route and shed light onto this point. We have now added a sentence on this to the discussion.

Reviewer #3:

This work examines the role of two nucleoporins in the export of the flam RNA, which is a precursor for piRNA biogenesis necessary for transposon silencing in Drosophila ovaries. There is considerable interest in exploring how nucleoporins function outside of their canonical roles in nuclear transport. Thus, this study is relevant from a fundamental cell biological viewpoint but it also may illuminate how some nups appear to be uniquely required during embryonic development and why nup mutations sometimes result in tissue-specific disease. The paper is impressive in scope and in its use of systems-level, biochemical and cell biological approaches to explore changes to transcription, piRNA biogenesis and biochemical interactions. Further, in general, the data are of high quality although often missing statistical analyses to help evaluate highly variable data. The biggest challenge is that there is so much data crammed into a small number of figures that the paper is very frustrating to navigate. Thus, while it is thoroughly convincing that there is a unique requirement for Nup54 and Nup58 in piRNA biogenesis, specifically from the flam locus, a more deliberate and more detailed description of the data would vastly improve the work. Further, the proposed model may be premature and additional considerations regarding where nups might function in this pathway e.g. in the nucleus or cytoplasm should be more thoroughly considered.

1. There are so many experimental techniques and analyses used in this paper that, when coupled to the often obscure nomenclature of genes and mutant alleles, makes navigating this paper extremely frustrating, particularly for a non-expert. One (of many) example of this is the first figure call out, Figure 1, figure supplement 1, which refers to an 8 panel figure that is essentially not described. The strong suggestion is to expand the text to more fully describe all of the figures to do the work more justice and allow readers access.

We thank the reviewer for this feedback. We have expanded the text to provide more detailed explanations of the data.

2. The strength of the work lies in the remarkable specificity exhibited by loss of function of Nup54/58 to piRNA biogenesis, particularly at the flam locus. However, the model proposed is not fully supported by the data. A key concern is that it is well established that nups can function outside of the NPC, both at genomic loci and also in the cytoplasm but this is not fully considered or ruled out. The suggestion is to be more circumspect with the proposed model and to consider alternative possibilities. The key may lie in the fact that it is the coiled-coil domains of the nups, and not their FG-motifs that appear to be important. Although one could argue that this supports their integration into the NPC, how these domains could connect to Nxf1 without FG-repeats remains difficult to rationalize.

We have adjusted the model description (now referred to as a “tentative model”) and clearly stated what knowledge gaps will need to be filled in order to draw a conclusive picture of flam export. We agree that our data do not fully rule out a possible role of Nup54 and Nup58 outside of the NPC, perhaps within Yb-bodies. However, we believe that in such scenario they should have been detectable in our Yb PL-MS and more cytosolic signal would have emerged via immunofluorescence.

3. Invoking a model that suggests that Yb might act similarly to Dbp5 on the cytosolic filaments is certainly interesting, but the data do not yet support this. A clearer understanding of whether the interaction between Yb and Nup214 is direct would be necessary, further, it should be ruled out that DDX19 is not involved with the export of the flam RNA.

We agree with the reviewer’s comment and we have removed the speculation about Yb acting similarly to Dbp5. Further experiments beyond this study are required to address this question.

Lastly, in general the data is well quantified but better descriptions of the plots and statistics are really needed for interpretation.

We have expanded the figure legends to provide better description of the plots and statistics and have added the exact individual p values to each measurement. All quantifications and statistical analyses are accurately described in the methods section.

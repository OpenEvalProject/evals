# Peer review - Round 1

Editors:
- María Mercedes Zambrano, CorpoGen Colombia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60197.sa1](https://doi.org/10.7554/eLife.60197.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work examines the role of domestication and industrialization on the microbiome by looking at changes in the gut microbiota of humans and wild and domesticated mammals. Despite being fundamentally different processes, the authors conclude that domestication and industrialization have impacted the gut microbiota in related ways.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Effects of domestication on the gut microbiota parallel those of human industrialization" for consideration by eLife. Your article has been reviewed by a Senior Editor, a Reviewing Editor, and three reviewers. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that we cannot pursue the publication of your manuscript in its present form. However, we consider that the work is very interesting and therefore a new version that thoroughly addresses the concerns raised would likely be reviewed again. Although it would be treated as a new submission, we would aim to retain an overlapping set of reviewers.

The work provides exciting and valuable information on the possible effects of domestication and industrialization on the gut microbiome. However, there were several methodological issues raised, such as host genotype determination, control for genetic distance and, in particular, concerns regarding data analyses (diversity metrics, OTU picking, error rates, Permanova, and FDR correction, to name some) that can take a considerable amount of time to perform. There were also misgivings regarding the validity of some of the conclusions based on the data presented. These include group comparisons that do not necessarily agree with the idea that domestication and industrialization similarly impact the gut microbiota, and the effect of host genotype or genetic distance on the microbiota. Please also take into account the comments about differences with respect to previous publications regarding the claim that domestic animals may be useful as models.

Reviewer #1:

This study examines effects of domestication on the gut microbiome of wild animals to the effect of industrialization on the gut microbiota of humans. They report consistent shifts in composition of gut microbiota in domestic animals and in humans from industrialized (but not from traditional) societies. They also perform cross-feeding experiments of wild and domesticated animals (lab mice/wild mice; dogs/wolves) and report that apart from genetics, diet plays a dominant role in shaping (loss of diversity) of the domestic gut microbiota.

I have the following comments:

1) Introduction: "genetic changes under domestication" How did the authors control for differences in genetic distance among the individual domesticated/wild animal pairs? Are the shifts in composition of microbiota during domestication and industrialization still consistent if controlled for genetic distance?

2) Introduction: "Finally, the convergent nature of many ecological shifts experienced by domesticated animals and industrialized human populations suggests that domestic animals may provide a uniquely useful model for studying the microbially-mediated health impacts of rapid environmental change." and Discussion "their translational potential as models for studying the gut microbiota of industrialized populations may be greater than is currently appreciated." This statement is not clear – please clarify in the context of two publications (Nature. 2016;532(7600):512-6 and Science, 708 2019;365(6452):eaaw4361) that appear to state the opposite.

3) The authors describe that diet plays a major role in changing the microbiota of wild animals to those of domestic ones. Diet is a great source of viruses. To which extend is the introduction or loss of viruses (in particular phages) responsible for the shift in gut microbiota?

4) The authors state repeatedly that wild animals more diverse microbiota. Are there uniform changes in taxa? Are some taxa lost, and if so, is this observed in several wild / domestic pairs?

Reviewer #2:

This is an exciting paper with important implications for how diet and environment interact to shape the composition and diversity of the gut microbiome. The results are interesting – particularly the results of the robustly designed diet challenge experiments. Concluding with the host-microbe-environment mismatch puzzle is thought-provoking. I am slightly concerned about how the framing of the study is phrased. I additionally have some questions/suggestions/concerns regarding the methods.

1) The results of this study are super interesting, but the authors need to be sure to make it very clear throughout that they are examining how environmental and dietary shifts associated with domestication may parallel environmental and dietary changes in some human populations (not that some human populations are domesticated and some are wild). The authors are mindful to make this clear most of the time, but it would be good to make it explicit all of the time.

In addition, I would ask that the authors carefully consider how human populations are described – traditional is not the best term, unless it is how those populations self-identify. There are real and very important ecological differences that distinguish the human populations that were sampled. Using language that somehow indicates what those differences are might be more impactful than using industrialized vs. traditional. Or, at the very least, clearly defining those terms early on in the article is necessary. Industrialized vs. non-industrialized or traditional can be read as placing as elevating either group or could be read as saying the populations are "advanced" and "not advanced" (particularly important as this paper will likely generate some media attention).

2) I am wondering if it is better to categorize the genotype/diet experiment as a provenance/diet experiment or something similar. As the authors did not actually look at host genetics in the wild-caught mice, they don't know how genetically distinct they are and there is certainly variation in genetic distance from the lab mice within the group of wild-caught mice.

3) Genetic changes kind of come up unexpectedly and without context the Introduction, which I found unclear. It may be better to focus this paragraph solely on ecological/environmental shifts? I was also a little confused if the authors were indicating the known genetic changes caused by domestication would change something about host physiology that would impact the gut microbiome somehow, or if the effect of divergence in host genetics would cause a simultaneous divergence in gut microbiome composition, or both.

4) Gomez et al., 2019 and Amato et al., 2019 both found that the human gut microbiota is actually closer to that of baboons than chimpanzees. I don't think the authors necessarily need to add baboons to the analysis, but it would be relevant to acknowledge in the discussion that chimps may or may not be the best comparison for humans.

5) Introduction (and elsewhere): I don't think domestic can be used in place of domesticated – the meanings, to me at least, are distinct.

6) Methodological concerns:

- Samples collected in RNAlater are not necessarily comparable to freshly frozen – please note in the methods which species were preserved with each method and describe how you accounted for this difference in preservation.

- Why was closed-reference OTU-picking chosen? Open-reference OTU-picking is the recommended method, unless one is comparing amplicons from different regions of the 16S rRNA gene. I would suggest that analyzing the data using one of the ASV strategies (DADA2 or Deblur) is recommended, but also do not want to force the authors to reanalyze their entire dataset (and the newer ASV methods become less useful when including 454 data).

- Yatsunenko et al., 2012 used 454 sequencing – I am curious how the authors corrected for the differences in sequencing-related error rates between 454 and HiSeq? And why they did not choose to use available human datasets sequenced in a manner comparable to the newly produced dataset in this paper?

- Using the adonis2 function in vegan would allow the authors to use marginal sums of squares in the PERMANOVA analysis – this might allow them to better tease apart which factors are accounting for what proportion of the variance in the dataset.

- A Bonferroni correction is quite conservative for microbiome datasets – FDR correction could be used instead.

- I would like to see an explanation for the choice of method to measure the magnitude of change in β-diversity, as it is one I haven't seen before and measuring change along an axis that does not have an easily interpretable meaning might not be the most informative. Alternatively, comparing pairwise unweighted and weighted UniFrac between domesticated/wild and baseline/treatment and/or performing a Procrustes analysis may be preferred.

Reviewer #3:

Reese et al., compare the microbiota of domestic animals and their closest wild counterparts, including a comparison of humans and chimpanzee microbiotas. They report similar changes to the microbiota from domestication and industrialization. Overall, the data presented is fairly noisy and many of the conclusions seem overstated given slight differences between groups. Even if we set aside the issues with the data, which are not trivial, it is unclear how important the conclusions are. For example, the last sentence of the Abstract:

"We conclude that domestication and industrialization have similarly impacted the gut microbiota, emphasizing the utility of domestic animal models and diets for understanding host-microbial interactions in rapidly changing environments, and the importance of studying non-industrialized human populations for understanding aspects of human health dependent on host-microbial co-evolution."

Not so easy to unravel the point(s) the authors are trying to make. The last passage is already very clear to the field, non-industrialised populations are important to study. The first part suggests that domestic animals and diets are useful in understanding the microbiota in changing environments. It is not clear exactly what this statement is trying to convey and it requires some clarification.

In the Abstract the authors state that "domestication and industrialization have similarly impacted the gut microbiota". A major concern is the data presented in Figure 5B for two reasons. First, the difference between two industrialized human populations appears to be larger than that observed between domestic and wild animals. Second, the shift to the left from industrialized humans to traditional humans is larger than from industrialized humans to chimpanzees. Not only is this problematic from the standpoint of implications about the "wildness" of traditional populations, but also difficult to interpret given the greater similarity in genetics, physiology, lifestyle, and diet between human populations than chimpanzees and humans.

The authors report greater between species variability in wild gut communities than domesticated. However, it does not look like they did this comparison for the human and chimpanzee data. Given published data showing that the between individual variability in the microbiota of industrial individual is larger than that of traditional population microbiota, it would be interesting to see how these data compare to that of chimpanzees given that this is not the result you would expect given the data from the other animal pairs.

It is not clear how α diversity was calculated. Was the data rarefied and if so to how many reads and were the samples sequenced sufficiently deep to ensure an accurate measurement of diversity.

Subsection “Diet vs. genotype effects on domestic gut microbial composition in mice”. "Domestication has profound effects on both ecology and host genotype." Do the authors mean "has had", ie, there is evidence that animals, when domesticated, show genotypic changes, eg, new traits are selected for. Domestication over short time periods may have little effect on genotype.

Subsection “Diet vs. genotype effects on domestic gut microbial composition in mice”. "we found that host genotype explained the largest amount of variation" It is unclear what data the authors are examining to reach this conclusion. The species appears to be Mus musculus for these analyses. Are the authors performing a host genotype (eg, SNP) analysis? Please clarify how differences in host genotype are being determined.

Figure 2.

- It is very difficult to draw conclusions from Figure 2B. Suggest that the authors show centroids or find a better way to represent the data. Some of the colors are too similar as well, so difficult to differentiate. Why are DomG/DomD points moving on the PCA plot? Same with WildG/WildD? Perhaps this data could reveal drift of the microbiome composition in the absence of intervention, which may inform whether their diet shift in the other groups is meaningful.

Figure 4 has many of the same issues described for Figure 2. It's very difficult to interpret these panels with so many points going in different direction and minimal color differences between some of the points.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Effects of domestication on the gut microbiota parallel those of human industrialization" for consideration by eLife. Your article has been reviewed by Detlef Weigel as the Senior Editor, a Reviewing Editor, and three reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The manuscript by Reese et al., explores the effects of mammalian domestication and human industrialization on the gut microbiota and has important implications on how diet and environment interact to shape the composition and diversity of the gut microbiome. They characterize the microbiome via 16S rRNA gene sequence analysis in various mammalian species and show that the microbiome shifts with domestication. Using cross-feeding experiments in mice, wolves and dogs they are able to demonstrate that diet and microbial inoculation can reverse the effects of domestication. Finally, they compare chimpanzees and both industrialized and non-industrialized human populations and show that shifts in microbiome composition are larger when chimpanzees are compared with industrialized populations. Overall the work presents clever experiments aimed at characterizing the effects of domestication on the gut microbiota and comparing these effects with those of human industrialization.

Essential revisions:

1) Reviewers were concerned with the comparisons between domestication and industrialization and the subsequent conclusions. This aspect of the work needs to be improved for clarity and the claims toned down as they are not fully supported by the data presented.

a) The authors should note that domestication, which has taken a long time, and industrialization, a fairly recent change to our ecology, are different processes. Therefore, the direct comparisons in the manuscript do not seem entirely appropriate and should be more carefully addressed. In particular, the data does not provide strong evidence to support the claim that animal domestication and human industrialization result in similar effects on their hosts microbiome, even though this conclusion may be correct, since it makes sense given that many ecological processes are probably affected in similar ways. This conclusion should therefore be toned down to agree with their data.

b) Is there a way to incorporate data from populations that use subsistence strategies involving domestication, but are not Industrialized (the other populations in Jha et al., even)? It could be expected that the agricultural or pastoral but non-Industrialized countries would be somewhat intermediate in their microbiome composition, as they experience the factors of domestication without some of the extreme ecological consequences of Industrialization (antibiotics, highly processed foods, etc.). Is this the case?

c) A more nuanced discussion should occur at some point in the manuscript on the choice and caveats of using highly Industrialized populations in this comparison given that the process being compared is domestication and not industrialization.

2) The revised manuscript has improved but still lacks clarity in many places and uses language that is vague and often misleading, making it difficult to understand what the authors are trying to say. The entire text should therefore be checked and improved to make the language more precise.

a) In the Abstract, for example, it is not clear what shifts the authors refer to, what is meant by microbiomes to be impacted “'similarly”, and what “parallel ecological changes” are. It can be argued that the ecological changes are quite different in industrialized humans and domesticated animals (housing, hygiene, diet, etc.). However, the ecological processes that impacted their microbiomes, and the compositional alterations, might have been similar.

b) This vagueness is also found through the entire manuscript. What are ecological parallels (Introduction)? What is a "suite of shared ecological changes" (Introduction)? Which “evolutionary forces” were studied? What do the authors mean by "individual shifts"? (figure legend of Figure 1C). Compositional shifts in an individual? Was that even assessed?

c) The term “shifts” is used inappropriately throughout the manuscript. For example, what are "shifts between industrialized humans and wild chimpanzees" (Figure 5 legend)? The microbiome does not really shift from a human to a chimpanzee. Do the authors refer to differences between microbiomes in different hosts?

3) The authors should be careful with the way they present their results to avoid biased interpretation and make claims that are clearly supported by their results.

a) It sometimes seems as if the authors have interpreted the findings to fit a preconceived idea of the findings. For example, the authors conclude a "consistent effect of domestication status" (Results), but the samples cluster by host, which has the highest effect sizes. The conclusion is then mainly based on a statistical analysis that showed domesticated samples to be "further right" on an NMDs axis. This is not very convincing, and not very clear in Figure 1C either.

b) Another claim is that in Figure 2, differences between domesticated and wild mice can be overcome by a diet switch, but looking at Figure 2—figure supplement 2, that is simply not the case. It is difficult to see how the data in Figure 5 provides strong evidence that the effects of domestication and industrialization are similar.

4) More clarification is needed for wild and domestic microbiome results and subsequent conclusions

a) The results presented (Results and Figure 1) do not seem to support the conclusion that domestication is shifting all species to the right along NMDS1. The magnitude and direction of shift seems to differ based on host species. While the general trend of all species lumped together is to the right, sheep and pigs don't seem to follow the pattern (and some others don't seem to have a strong shift to the right). What are the effect sizes for the Mann-Whitney U tests here? Also, looking at Figure 1—figure supplement 2A, only the companion species are denoted as having a p<0.05, which seems at odds with the statement in the Results.

This species-dependent direction and strength of shift is not entirely unexpected based on previous work. Shifting host ecology (diet or captivity) has previously been shown to differentially effect host species: Amato et al., 2015 and McKenzie et al., 2017.

The inconsistency in the direction of the shift might not actually negate the broader point, that domestication at times has effects on the gut microbiome that are very similar to the shift we see between industrialized and non-industrialized humans. In fact, it might be instructive to point out what specific species might be good models for the shift we see in humans – what are the specific ecological shifts with domestication in those species and how does that mirror the ecological shift with industrialization in humans?

b) What does it look like when you put the results of the mouse and canid experiments in the same ordination space with your wild/domestic and chimp/human pairs? Is the shift in the expected direction? When looking at the results of the mouse experiment and the canid experiments on their own, we see a shift to the left with experimental domestication (ie, for the Wildh/Domd treatments), but this might be a function of the ordination space?

c) Were any of the animals, either wild or domestic, from the same family, field, pen, etc.? Cohousing results in convergent microbiome profiles across a number of species due to horizontal microbial exchange. If conspecifics were collected from the same living situation or were related, one might expect higher microbiome sharing on those grounds alone. This potential confounder could explain the high similarity between the conspecifics. These details should be added to the Materials and methods. If this is an issue, it should be corrected for in statistical comparisons (if possible).

5) Technical concerns and data presentation

a) Figure 2 and Figure 4 are a difficult to interpret, because the lines used to indicate moving points are obscuring the points themselves in some cases. Would ellipses around the treatment groups in the NMDS plots be more informative than the moving points?

b) For the adonis2 function, to get the marginal sums of squares you need to include “by = "margin"” in the function call. Using adonis2 without specifying “by” is equivalent to using the older adonis function. This should be relatively quick to rerun and will make the effect of host vs. ecology vs. diet easier to parse.

c) The OTU picking strategy can introduce biases when sampling microbes that are better represented in the reference taxonomy since more of the sequences will be classified in one sample versus another. Even though the authors seem to have chosen the best option for this dataset, there very well could be differences given that comparisons are explicitly between Industrialized vs Non-Industrialized populations (there tends to be lower read mapping to closed ref OTUs in non-industrial populations) as well as human-associated vs. wild animals (it would be expected that lab animals and livestock microbiomes have been better characterized back when that GreenGenes taxonomy was created).

Can a Supplementary file be added that lists the proportion of reads classified per sample? Are there differences in the number of reads that classify between the major comparisons in this paper (Industrialized vs. Non-Industrialized, Wild vs. Domestic, etc.)? If there are, then reprocessing of these reads either with an open OTU calling method or ASV method should be implemented.

d) How does microbial load/density vary based on gut passage rates, and could this be influencing your results?

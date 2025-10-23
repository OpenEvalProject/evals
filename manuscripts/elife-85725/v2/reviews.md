# Peer review - Round 1

Editors:
- Detlef Weigel, https://ror.org/0243gzr89 Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85725.sa0](https://doi.org/10.7554/eLife.85725.sa0)

This is an important interdisciplinary effort, with compelling genetic evidence, that informs on the spread of an important crop. The work will be of broad interest to those studying the domestication and dissemination of cultivated plants.


---

# Peer review - Round 1

Editors:
- Detlef Weigel, https://ror.org/0243gzr89 Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85725.sa1](https://doi.org/10.7554/eLife.85725.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "The climatic constrains of the historical global spread of mungbean" for consideration by eLife.

First we would like to apologize for the length of time it took to reach this decision. We had hoped to get input from another archaeologist who had agreed to review but in the end did not submit a review. We had a rather long discussion of the work, plus several of the people involved were on vacation.

Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Jeffrey Ross–Ibarra (Reviewer #1).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will is not acceptable for publication in eLife.

The first two reviewers, both geneticists with experience in plant domestication, were excited about the topic and the interdisciplinary approach taken. But both raised a number of concerns about the methods and approaches used, which would require substantial additional work to address. The third reviewer, an archaeologist, raised real concerns about how well the paper has incorporated existing data into interpretation and analysis.

In the end, given the number of concerns raised on both the genetic and archaeological fronts, I'm sorry to say that we have decided that this work in its current form will not be considered further for publication by eLife. Having said this, there was broad interest in the work and the topic, and we would reconsider, albeit as a new submission, an extensively revised paper, which would likely look very different from the study at hand.

We are sorry about this outcome, but hope that the comments will be helpful for submission elsewhere.

Reviewer #1 (Recommendations for the authors):

The authors provide an ambitious interdisciplinary analysis of the post–domestication spread of mungbean. I believe the authors' general thesis is correct, and the various data they provide are all consistent with their model.

Nonetheless, there are some issues with analysis and interpretation, and in general, the data don't provide definitive evidence that allows claims about drought or the importance of the environment.

All of the evidence and analysis presented are consistent with the authors' proposed SA–SEA–EA–CA model. The f3 results are particularly convincing. I struggle, however, with how the data definitively show environment was more important than human movement. Some text shows, for example, that trading or demic movement between SA and CA was frequent would make clear that mungbean 'could' have moved SA–>CA via humans but didn't. Otherwise, could the SA–SEA–EA–CA model simply reflect historical movements/expansions of people in those directions/times?

On a similar note, the paper claims that drought was the most important factor limiting the mungbean movement. The phenotypic data certainly suggest adaptive differences in traits related to drought and drought differences in phenotype in an experimental setting, but additional evidence would be helpful to convince that drought is the key factor. The authors note the importance of daylength differences, for example – how do we know daylength wasn't the limiting factor (as it seems to have been in the northward spread of maize, for example)?

Methods Recommendations

– It's difficult in some places to know which SNP data set is used where. Are the LD–pruned SNPs used to estimate LD decay? The methods say there are 67K sites (including monomorphic) but there are 41K SNPs. This would imply that 2/3 of the sites are polymorphic. That can't be right so I must be misunderstanding something. Are these monomorphic sites also used for estimating nucleotide diversity (see the issue with VCFtools below)? For fastsimcoal, do you include sites where the derived allele is frequency=0 and where the derived allele is frequency 1?

– It would be good to modify the language of the MaxEnt modeling. While MaxEnt may show that the modern mungbean does not currently grow in conditions similar to those during the Holocene at a certain spot on the map, this is not the same as saying the plant could not have grown there. For example, if we were to model MaxEnt on modern CO2 concentrations, we would come to the conclusion that modern mungbean could not have grown anywhere during the Holocene. I don't think necessarily the methods need to be changed, but it would be good to change the language here to be less definitive.

– Although dominance is less of a concern in inbred species, I believe it is still incorrect to assume that using Vg is equivalent to Va in Qst. The epistatic variance could still be important, for example, and my brief internet search suggests mungbean isn't 100% selfing either. The authors have SNP data for all the individuals phenotyped, so it should be doable to estimate Va using kinship matrices and thus do a correct Qst analysis.

– VCFtools calculates nucleotide diversity assuming every bp in a window has been sequenced. This will lead to incorrect estimates of π and Fst. See https://pubmed.ncbi.nlm.nih.gov/33453139/ for details and one potential fix if you have a vcf with invariant sites, or https://github.com/RILAB/mop for another if you just have bams + variable vcf.

– an NJ tree (Figure 1E) is just a clustering algorithm and shouldn't be interpreted as providing information on the timing or order of evolutionary events. (lines 119–123)

– If the growing season is known and is what is most relevant for the crop (line 190), these should be used for most analyses or a justification for using annual data should be provided

– I can't find the total length of time plants were grown for the drought stress experiment. The text reads as if it were 9 days?

Reviewer #2 (Recommendations for the authors):

The study aims to understand the diffusion of the Mugbean population in Asia using genomic and phenotypic data. The authors used phylogeny, analysis of population structure, model–based inference, quantitative genetics, and niche modeling to understand the diffusion of Mugbean and proposed a scenario where diffusion is strongly constrained by climate, and partially by geographical.

I found the study very interesting with a mix of different methodologies from genomics to niche modeling and quantitative genetics. Few others studies used similar approaches but it is rather unique for the study of diffusion to combine these different approaches and bring up very interesting results. I have several comments on the methods so the results are better supported for the genetic part, for the phenotypic part, I am not sure the author will be able to support their claims, as the method they used might inflate variance in their estimations.

Main comments:

Phylogeny. Phylogeny is not really an appropriate method per see for intra–diversity study, phylogeny analysis could be used but the basic assumptions of the method are often inadequate, so the result should be put in context. A better method to do phylogeny–like inference is the TREEMIX approach based on the relationship of population integrating drift. I suggest the authors add this complementary analysis.

Model inference. Here, I would have liked a statistical comparison of the different scenarios. FastSimcoal allows for estimated probability of models/scenarios and it would be an independent validation to have such a comparison of models.

The inference of the model is dependent on mutation rate (unknown), notably on the time of divergence. The author used 10–8 but it is neither discussed nor justified.

Analysis of structure.

The author led aside from further studying individuals with ancestry lower than 70% in a given group. The analysis of structure could lead to such ancestry because of admixture or isolation by distance. One is secondary contact based on recent (or not) gene flow between genetic groups, the author is related to diffusion across the landscape. A large fraction of individuals in the PCA seems to me more likely related to isolation by distance (between SEA/EA, EA/CA). How this will impact the analysis of correlation by geographical distance if such individuals are not considered? The authors should perform the analysis of the Mantel test with all individuals to assess the impact of their choices.

Quantitative analysis of QST. The author used the genetic variance and not the additive variance. The reasoning behind that is not explained, neither the inflation created by this broad sense QST. Authors have concluded that the "extent to which comparisons between FST and broad–sense QST are appropriate remains unknown" (Pujol et al. 2008).

Reviewer #3 (Recommendations for the authors):

The paper aims to look at the domestication, post–domestication spread, and adaptation of mungbean (Vigna radiata) across Asia through the use of genetic data from landraces and accessions in see and genebanks.

The genetic aspects of this paper are a strength – there is a lot of work that has been done putting together a range of datasets allowing for inter–collection comparison and comparison of collections made by different institutes with their varying goals, sampling strategies, and dates of collecting. Mapping this diversity, think about how drift has occurred and why is something that needs to be done, especially in mungbean (and other tropical pulses of Asian/South Asian origin) as they are often overlooked in literature.

However, the main stated goal of the paper – to look at the domestication, post–domestication, and adaptations to climate change as this crop was moved around – is where it falls short. There is little engagement with the deep archaeological literature on both domestication as a process, post–domestication use and spread of mungbean (and other South Asian crops and those involved in the Silk Routes trade pathways), and the complexity of climate reconstructions and climate change over the stated period of interest/regions of interest. Works by Spengler and d'Alpoim Guedes for example are missed with regards to the Silk Routes debates, and literature by Fuller, Murphy given only short sentences as background for what is a very complex background regarding where and when mungbean is thought to have been domesticated. There is little reflection on the context of the two/three possible origins for mung (south, north, and west South Asia), how this interacts with the Southern Indian Neolithic and Indus regions, and how the changing cultural dynamics may have contributed to the processes of domestication, post–domestication change and the spread of different varieties. Without this background, it is hard to then move into discussing modern genetic data with a view to past patterns, for example with thinking about how climate may have affected change, given that the debates around the 4,2k event are extremely complex within these, let alone thinking pan–Asian and trying to link potentially 'drifted' genetic data today to these deep–time events. This comes across in the timescales given to the genetic data, as without the context of the where and when from archaeology, we see dates such as those given in Figure 2B that suggest domestication for South Asia moving to South East Asia at c.6kya (4000BC), which is when we still think they were under domestication within South Asia. The region is also not pinned down for where in South Asia these specific 'domesticated' mung are coming from to go to South East Asia, and the routes, yet arrows and big circles are added in Figure 2A. This shows the issue of not using that important context from archaeology.

A further issue arises from thinking about the climate data. By conflating vast areas (e.g.: South Asia, Central Asia, etc.), when applying climate modelling there has been an oversimplification, which makes any discussion of mung bean adapting to climate post domestication difficult to sustain. In line 184 for example, there is a suggestion on the role of the 6.2k event in Central Asia (putting aside the above issues of the dating of mung domestication in South Asia before it even reaches Central Asian regions already noted). While there are a few datasets as cited in the paper that show some impacts of wetter climates in some regions of Central Asia for a wetter 6,2k event this is by no means a universal impact, and regional data points are needed. We can see this when looking to the Indus and the impact of the 4.2k event as another example, again a point that needs refining in order to make such claims about mung domestication, let alone post–domestication adaptations.

Overall the thrust of the paper – domestication, post–domestication, and the spread of agriculture – are overshadowing what is actually a far more interesting point, hidden in lines 87–89: this data could be "used this resource to investigate the global history of mungbean after domestication […looking at the …] phenotypic characteristics for local adaptation to distinct environments." This perhaps is where the paper is most interesting, and reframing it in this context would be truly exciting, looking at the diversity of the crop, how it is now adapted to diverse environments, and what this might mean for long–term sustainability in cropping systems.

This paper sadly is losing some very interesting genetics data in complex and poorly explained mung history.

– The lack of engagement with archaeological data and the misunderstanding of the chronology of mung use in the past makes it very difficult to tally the results with the interpretations and discussions. This MAJOR point has been unpacked in more detail above and must be addressed in order to reduce the oversimplification of the background and remove the concerning premise that no one has done much work on ancient mung use (as stated up to l.77). While it has not had as much work as the cereals, there is still work being done on it, looking at its domestication regions, secondary domestication changes and spread across South Asia and then into different parts of Asia.

– Data seems to have been massaged to make it fit with the climate modelling in various regions (for example Figure 2B has mung arriving in Central Asia around 0.2k yet discussions of 6.2k climate events in l.184), and to also make mung seem to be spreading before the domestication event itself. More engagement with the archaeological discussions on mung domestication is needed and discussions of what domestication is as a process (there is a fundamental misunderstanding of the conscious/unconscious action outline in Larson et al. in l.47 – the way it is phrased implies deliberate choice to ensure change rather than recognizing the inherent unconscious and indirect action of human behavior and the entanglement of human–plant–environment interactions).

– Terms like cultivar and variety and landrace are used interchangeably. These must be defined in the paper. How they fit in with notions of domestication and post–domestication agricultural behavior must also be unpacked.

– "how the domesticated forms later expanded to a broader geographical area has also been detailed in several species, including maize (Matsuoka et al., 2002), rice (Huang et al., 2012), tomato (Razifard et al., 2020), chickpea (Varshney et al., 2021), and lettuce (Wei et al., 2021)." – these are unusual choices of case study to make a point as many (maize and rice as key examples) are not accepted as well defined and remain highly controversial. These are genetics papers, and demonstrate the lack of familiarity with the archaeological context of domestication. A quick glance at the literature around them will illustrate that they are poor choices of case studies to make this point as they too are highly controversial.

– "It is also unclear whether the expansion of most crops strictly follows the longitudinal axis of the continents (Diamond, 2005) or whether or why some are able to cross different climatic zones." – again poor knowledge of the archaeological context of these debates, and the reliance on Diamond is concerning as he is not an archaeologist. See works by Lister on barley and Lui on wheat as a good starting point.

– Debate on wild progenitor of mung bean needs to be explored. while sublobator is a likely candidate it should be explained in the paper that there are other possible options, and then why it was chosen here, with citations.

– The figures are difficult to use. This comes back to the conflation of space and time outlined in the public review. There are big circles on the maps covering the dots which I presume are either archaeological sites or accession points of the sampled beans(?! unclear), and then very odd choices of illustrating change over time. The figures are small and hard to see and require very long text in the figures to make them useable.

– Some aspects of basic geography have been overlooked to make climate the most important variable; l.166–7 "Given that geographic barrier might not be the most important factor". I find it hard to believe that both the Himalayas and major flood basins like the Brahmaputra would not be an issue, as would issues of day length when moving things north–south.

– In dealing with issues of climate change and adaptation some discussion of tolerance is needed. there must be a discussion (and a table perhaps) of the different watering, salination, temperature, etc. tolerance of the mung bean(s) under consideration to make the claims justified.

– Within the methods, the sampling strategy was hard to follow. This needs a more careful and clear description of decisions made: exactly where did the accessions come from geographically? how did their spread affect the dataset? Is there geographic clustering, did you compensate for that? how does the sampling potentially bias your data? a map would be useful.

– Fair and open protocols dictate that all methods must be stated: "Genomic DNA was extracted from a single plant per accession using QIAGEN Plant Mini DNA kit according to the manufacturer's instruction with minor modification." If you modified the protocol then you have to outline what you did so it can be reproducible and the data comparable.

– "Climate data for conditions between 1960–1990 were downloaded from the WORLDCLIM 1.4 database" – how was this dataset determined? why 30 years and not more? give citations to explain this decision, and look to other modelling efforts to check comparability.

– "19 bioclimatic variables" – what are these? why were they chosen? a table and explanation are needed.

– "excluding one of the two variables that have a correlation above 0.8 (Supplementary file 4)" – why? explain the reasoning for exclusion.

– Throughout the dataset has relied on "In total, our dataset contains more than one thousand accessions (1092) and covers worldwide diversity of mungbean representing a wide range of variation in seed colour" however at no point is there a discussion of whether these are modern variants of historic landraces and how this was assessed. This has a big impact on any discussion of "ancient" adaptations, and there must be a discussion of how you tested to see if the genetic changes you see are more recent or past changes and how the genetic clock was applied.

As noted in the public review, a far more interesting aspect than trying to tie into domestication/post–domestication and chronological vagaries are the points made in lines 87–89: this data could be "used this resource to investigate the global history of mungbean after domestication […looking at the …] phenotypic characteristics for local adaptation to distinct environments." Thinking about the value of this dataset for the preservation of diversity, and how diversity links to localised adaptations today and to sustainable cropping now is critical, and I suggest this could be the way to reframe things.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Environment as a limiting factor of the historical global spread of mungbean" for further consideration by eLife. Your revised article has been evaluated by Detlef Weigel as Senior and Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined in the comments of Reviewer #1 below.

Reviewer #1:

I found this study to be one of the rare to combine genomic data, climate data, phenotypic data to decipher the diversity of adaptation of plants, and try to build up scenario of their diffusion. Previous recommendations were mainly answered, and I am personally satisfied with this new version of the manuscript. At this stage I recommend acceptance of the paper as soon as the concern is addressed.

Data availability:

I was not able to access the bioproject PRJN809503, is the data already available or not? Neither a biosample I try to access for a check.

Neither I was able to access DRYAD data.

The authors provide a link to fastq data but I could not find a fastq file link in Noble et al. or Breria et al. How did the authors merge the data? If they merged the data based on Table S1 or Noble et al. why did they find more SNPs than Noble et al. with a 10% missing rate? Since some authors are common between these studies a clear path to access to the whole dataset should be available to the community.

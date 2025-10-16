# Peer review - Round 1

Editors:
- Stilianos Louca, https://ror.org/0293rh119 University of Oregon United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78129.sa0](https://doi.org/10.7554/eLife.78129.sa0)

Richter and colleagues present an impressive analysis of metagenomic, OTU and imaging data collected from >100 ocean locations worldwide, with the purpose of elucidating the role of large-scale currents on global-scale marine plankton biogeography. The topic is exciting and timely.


---

# Peer review - Round 1

Editors:
- Stilianos Louca, https://ror.org/0293rh119 University of Oregon United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78129.sa1](https://doi.org/10.7554/eLife.78129.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Genomic evidence for global ocean plankton biogeography shaped by large-scale current systems" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a guest Reviewing Editor with expertise in this field, and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Francisco Rodríguez-Valera (Reviewer #3).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that your work cannot be considered further in its current form for publication by eLife. As you will see in the reviews, the great potential of the paper was generally appreciated, but all reviewers expressed substantial concerns about the methodology and the conclusions that can be drawn from it. It is eLife's policy not to request revisions which we anticipate are likely to take more than two months to complete and thus we are rejecting your submission; however, if you believe that our concerns, outlined below, can be adequately addressed, we encourage you to submit a substantially revised version of your manuscript. If you do decide to re-submit, please include a point-by-point explanation of how these concerns have been addressed.

Richter and colleagues present a large-scale analysis of metagenomic, OTU and imaging data collected from >100 ocean locations worldwide, with the purpose of elucidating the role of large-scale currents on global-scale marine plankton biogeography. The topic is exciting and timely, and should be of broad interest to the fields of marine microbiology, biological oceanography, plankton ecology and physical oceanography. One strong aspect of this study is that it compares community dissimilarities with travel times computed from a global ocean circulation model, rather than simply considering geodesic distances between locations. The data included with this manuscript will also likely be of great value to other research groups. There are, however, substantial concerns regarding the methodology and the conclusions that can be drawn from the work. A specific concern regards the use of 31 bp k-mers for calculating metagenomic dissimilarities and the difficulty of interpreting such dissimilarities biologically, given the many nuances of genome features from viruses to zooplankton. Concerns were also raised regarding the calculation of Tmin based on the surface layer, given that current velocity and direction near the surface and at lower depths of the mixed layer may diverge. Finally, there were questions about the relatively narrow distribution of Tara Oceans samples from similar latitudes and (largely) from the surface, and the fact that different locations were sampled at different seasons (which influence the extent of stratification).

Reviewer #1:

1. One strong aspect of this study is that it compares community dissimilarities with travel times computed from a global ocean circulation model, which arguably makes more sense than simply considering geodesic distances between locations (as most previous studies have done). The data included with this manuscript will also be of great value to other research groups.

2. The authors have shown that travel time correlates strongly with metagenomic community dissimilarities (lines 208-209), but they also found strong correlations between travel time and environmental differences (lines 232-233), and correlations between metagenomic differences and environmental differences (Figure 3 and lines 191-192). They also found that their genomic provinces often matched environmental differences. This begs the question to what extent the genomic provinces are caused by circulation within the provinces (which probably "homogenizes" communities within a province) rather than simply environmental differences between provinces (or environmental homogeneity within provinces). In other words, even if there was no circulation (thus communities are entirely determined by local environmental conditions), would we still expect to see the genomic provinces that the authors found? I would have expected a strong discussion on disentangling environmental selection effects from dispersal effects. The authors do marginally touch upon this issue by calculating partial correlations (Supplemental Figure S9), but they don't discuss this at all in the main text. Their Supplemental Figure S9c actually suggests that correlations between metagenomic dissimilarities and environmental differences (temperature and/or nutrients), when controlling for Tmin, are often stronger than correlations between metagenomic dissimilarities and Tmin (when controlling for temperature and nutrients). This might suggest that for some size classes genomic provinces are mostly caused by environmental homogeneity within basins/provinces, rather than the homogenizing action of currents. As it stands, I find the take-home messages of the paper rather vague and inconclusive from a mechanistic (i.e., rather than descriptive) point of view.

3. The authors calculate metagenomic dissimilarities with Simka based on counts of 31bp-k-mers (instead of, say, species counts or gene ortholog counts). While this is computationally efficient, it makes a biological interpretation of their metagenomic β-diversity hard. The original Simka paper demonstrated that k-mer distances correlate with taxonomic distance matrixes, but they don't seem to examine the relationship between k-mer dissimilarities and function-centric dissimilarities, i.e., dissimilarities in metabolic functions (as inferred by functionally annotating metagenomic reads or contigs). I suspect that k-mer-based distances may not correlate well with function-based dissimilarities.

Recommendations for the authors

I strongly recommend that the authors provide a quantitative and thorough discussion of my point 2 in their main text.

Related to point 3: Why not also perform an analysis in terms of functional (gene-centric) metagenomic dissimilarities? It seems that the authors only considered 100 million reads per sample anyway, so it should be feasible to annotate those and compare KO tables between samples. This would aid in the ecological interpretation of their findings. It would also facilitate comparison to other recent function-focused studies of marine microbial biogeography, such as [Ramírez-Flandes et al. 2019, DOI:10.1073/pnas.1817554116] or [Coles et al. 2017, DOI:10.1126/science.aan5712].

Reviewer #2:

The authors of the Tara Ocean consortium used this unique metagenomics data set of plankton size classes to test whether global biogeographic patterns exist and how these patterns are affected or even structured by global ocean currents. This data set of six size classes including viruses (<0.2 µm), pico- and nanoplankton (prokaryotes, protists), micro- and macroplankton (protists, metazoans) up to a size of 2 mm is really unique for such an effort. It provides a unified basis by using genomic DNA in all size fractions and thus avoids biases related to methodological differences of how the plankton communities of the different size classes were analyzed. By using station- and satellite-based metadata and correlating the metagenomic data of the stations and their dissimilarities to water mass transport derived from the MITgcm global ocean current model, the authors find global biogeographic patterns. Interestingly, these patterns of the different size classes are positively correlated to the minimum travel time of water masses up to 1.5 years, suggesting that biogeographic provinces evolve and presumably persist over this time span. Beyond, other factors become more important, such as temperature or the nutrient regime. The data also show that the scale of the biogeographic patterns is inversely related to the size classes. Further, a hierarchical cluster analysis of the metagenomics data of the different size classes yielded global genomic provinces which grouped together stations of related environmental and biogeochemical properties beyond water masses.

The statistical evaluation is very rigorous and for various correlations multiple and different analyses have been performed. The pairwise dissimilarity analysis of stations was done both for the metagenomics and OTU data yielding basically similar results and thus confirming the validity of the outcome.

Because of the novelty of this analytical approach this study may become seminal for further similar analyses. In order to become a really solid basis for such future analyses I suggest that the authors should consider the following critical points to further improve the study and to revise the manuscript accordingly.

1. I tried to find specifications for sampling of the larger plankton size classes in this manuscript and other Tara Ocean publications. According to the available information metazoans were also collected from Niskin bottles. If this is correct it means that only rather few organisms per sample and depth were collected, assuming a total abundance of <20 animals per liter in oligotrophic regions. So the questions arises how reliable the data on the larger size classes are for individual taxa compared to the smaller size classes where this point is not an issue. Usually zooplankton is collected by net hauls to obtain enough material. However, if net hauls are used they integrate over sections of the water column and it is impossible to sample a particular depth such as DCM. This point may also be an issue for the cluster analysis of the genomic provinces.

2. The cluster analysis of the genomic provinces shows that at quite a few stations the sample near the surface and at the DCM affiliates to different provinces. For the analysis of the water transport the surface layer of the MITgcm model was used. However it is known that current velocity and direction near the surface and at lower depths of the mixed layer may diverge, in particular towards the equatorial currents (Cravatte et al. 2017, J. Phys. Oceanogr. 47: 2305, DOI: 10.1175/JPO-D-17-0043.1; Hu et al. 2020, Sci. Adv. : eaax7727, DOI: 10.1126/sciadv.aax7727). How would the water transport and plankton dispersal change if only the near surface samples were used for this analysis (which would be the correct way for this analysis) or if this analysis were done with the MITgcm model for the depth section of the DCM (which would imply a reduced number of stations and an adjustment of depths because the depth of the DCM was variable)?

3. Stations in oceanic gyres dominate the sampling grid of the Tara Ocean expedition and stations in coastal and equatorial upwelling regions are greatly underrepresented. Therefore, and based on some discussion in the manuscript, the impression emerges that the biogeographic patterns and their relationship to Tmin is mainly true for oceanic gyres. I suggest that the authors should elaborate on this point and may also consider these constraints in their biogeographic analysis.

4. An important outcome of the study are the different scales of the dispersal of the size classes with Tmin. In a previous publication of the Tara Ocean consortium (Sunagawa et al. 2015, Figure 4B) they show a plot of an increasing dissimilarity of the prokaryotic communities with distance up to appr. 5000 km. In this manuscript the authors mention that they calculated correlations of the dissimilarities with distance for the different size classes but do not show any data. The study would greatly benefit when they show these plots for the different size classes which should yield different patterns. The distance of 5000 km may relate to the travel time of 1.5 years over an oceanic gyre.

In addition further recommendations are as follows:

l. 180-183, 195-199 and other places: There are quite a few genomic provinces of the prokaryotic and protest enriched size classes which go far beyond one ocean basin and even occur at one station near the surface and at the DCM. So be more precise in describing these features. Howe would you cope with genomic provinces which encompass similar stations but in corresponding gyres of the northern and southern hemispheres?

l. 181: delete "to" in this part of the sentence:.….tended to be limited to a single ocean basin and [TO] approximately correspond to…

l. 366: must be "….the same number of reads WAS used…."

l. 1019-1024: You hypothesize that the travel time of 1.5 years is equivalent to the time needed for crossing an oceanic gyre. I assume that this must not remain a hypothesis because I am convinced that ground truth data exist which provide such travel times, may be from the Argo floats program.

Reviewer #3:

This is another contribution from the Tara consortium and collaborators, in this case, they try to correlate ocean circulation with plankton biogeography. They have done a number of statistical comparisons using metagenomic data to analyze the effect of a parameter that they call Tmin, the minimal travel time, an estimation of the time that would transfer a water volume from one station to another as deduced from the expected water-mass movement. The problem of this approach (as with previous Tara papers in the view of this reviewer) is the random distribution of Tara stations at similar latitudes and (largely) from the surface and at different seasons. They contemplate the ocean as a two-dimensional system, largely ignoring the third dimension (depth) and the water column stratification that appears at most of these stations seasonally. Surface water movements have been considered without regard to the potentially more important vertical ones that happen when the water column mixes in colder seasons. Thus, their conclusions are flawed by a poor sampling strategy. The authors could have used more structured sampling efforts such as Geotraces, at least to check their overarching conclusions.

A second major flaw of this work is that the main source of information is what they call "metagenomic dissimilarity". It is actually the reciprocal of the ratio of shared (100% identity) 31 nucleotide K-mers between stations out of a pool of several million Illumina reads. This is a quite rough estimate of similarity that does not contemplate the nuances of genome features from virus to zooplankton. For example, the presence of IS or related elements in prokaryotic genomes might bias this parameter strongly, as would the presence of multiple repeats of rRNA genes in eukaryotic cells. The biological significance of metagenomic dissimilarity should be carefully assessed. I do not imply that it cannot be used, but to reach conclusions of such weight ("oceanic genomic provinces") a much more refined sampling strategy and analysis of the data would have been required. For example, why were the myriad of MAGs derived from prokaryotes and viruses at different geographical sites not considered? At least as a control for their claims. Actually, the several reports of nearly identical genomes at different oceanic provinces points towards the opposite. I do not believe the evidence presented here warrants the kind of conclusive statements presented.

In what follows I have identified specific points that would need clarification or modification in case the work had to be published.

Ln 98. There are now many studies on the biogeography of microbes based on metagenomics, including depth profiles and similarities along different transects so this sentence is just wrong.

Ln 102 seascape= metadata

Ln 104 the approach is not consistent (e.g., amplicon sequencing and metagenome similarity)

Ln112 and mixing with deeper layers

Ln118 neighboring (and deeper) water masses

Ln 155 However, some taxa information would have enriched enormously the manuscript

Ln 160 MAG abundance is not a reliable estimate of microbe abundance, often it is the opposite i.e. assembled microbes are not particularly abundant in the environment as exemplified by SAR11 or picocyanobacterial (several references).

Ln 163 explain "significant"

Ln 165 to the end of the paragraph. Extremely subjective i.e., heterogeneous compared to what? A depth profile will show that microbes at a 50 m distance in depth are likely more dissimilar than those located a 500 Km but at the same depth.

Ln 175. Colors are a very subjective representation, different shades of grey or lines of different thickness connecting stations as actually presented in Figure 2 b are easier to interpret.

Ln 187 surface temperature?

Ln 187 temperature or the cognate community?

Ln 190 which size classes?

Ln 194 or those microbial communities vary more sharply with depth and when they upwell (with nutrients) disrupt the water-mass continuity more

Ln 197 and vertical transport?

Ln 219 In any case, it would be interesting to know how dissimilarity correlates with geographic distance as well since Tmin will vary accordingly at shorter distances. It is to be expected that a transect following the Gulf Stream (small Tmin) will show high similarity. This would be a good control of the method of metagenome comparison.

Ln 223 Even more important would be the season and whether the water column is stratified or mixed as would be the case in winter in temperate latitudes (most of Tara samples).

Ln 239 temperature is more correlated with depth and season, particularly at the temperate latitudes.

Figure 2. Many points appear very divergent, can you explain the most extreme cases and label them in the figure?

Ln 332 what happens when the water column is mixed and there is no DCM?

Ln 252 easy enough to pinpoint upwelling areas

Ln 253 There seems to be something wrong with the plots presented in Supplementary Figure 2. If anything, they seem to prove that there is no clear correlation between OTUs and metagenomic dissimilarity what is actually not surprising considering the difficulty when trying to correlate data obtained in so different approaches and with different types of genomes (prokaryotic versus eukaryotic or even multicellular planktonic organisms).

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Genomic evidence for global ocean plankton biogeography shaped by large-scale current systems" for further consideration by eLife. Your revised article has been evaluated by Meredith Schuman (Senior Editor), as well as the previous Reviewing Editor and both previous reviewers.

The reviewers and reviewing editor appreciate the extensive work that the authors put into their revised manuscript and the detailed explanations provided in their response letter. There are still some concerns expressed by some of the reviewers, particularly with regards to (a) the ambiguity of using daily sunshine duration as a proxy for seasonality, (b) the potential inclusion of smaller organisms in larger nominal size fractions (for example host-associated microbes may be included in the 180-2000 fraction, thus distorting your analyses), and (c) the focus on surface currents and the omission of the ocean's 3-dimensional structure and variable stratification. The reviewers and reviewing editor have the following minimum recommendations for addressing these issues:

1. Please indicate in one of your maps what sampling sites had a mixed water column (e.g. less than 5ºC difference from surface to the subsurface DCM sample) and which ones had a stratified water column (e.g. more than 5ºC difference between surface and subsurface).

2. Please acknowledge in your paper (e.g., the introduction and discussion) the potential significance of depth, in particular highlighting the point that in the mesopelagic the relationship between composition of plankton communities and currents may be quite different than at the surface.

3. Please acknowledge (e.g. in the introduction or discussion) that the ocean is a tridimensional system in which the main axis of variation is depth, and that a focus on surface currents is a limitation of this study.

4. Please acknowledge in your paper the caveat that daily sunshine duration does not unambiguously map to seasonal effects (since in Spring and Fall daily sunshine durations coincide), and that ocean biology, chemistry and stratification often differ between Fall and Spring.

5. Please acknowledge in your paper that your size fractions are operational, i.e., not necessarily mapping precisely to organism sizes but instead a priori only mapping to "whatever is captured between two specific filter pore sizes". Please also provide some supporting information regarding the fraction of microbial (and perhaps even viral reads) present in the larger nominal size fractions, so that the readers can judge to what extent this may have been an issue.

6. Please clarify in line 143 why only 18S sequences are mentioned and not 16S and correct if necessary.

7. Please also check in line 142 if 24.2 TB of data were indeed analyzed, or if this is the total number of sequences but not all were actually analyzed.

The review from Reviewer #3 provides some additional details regarding the above revisions, which could help you to formulate your response to the essential revisions. The full reviews from all reviewers are provided for your reference below.

Reviewer #1:

The authors have clearly put a lot of effort into explaining their reasoning and improving the language of the manuscript, although in most cases they did not actually adjust/extend their analyses to address reviewer concerns. Hence, the paper's conclusions still remain in my view largely descriptive rather than mechanistic, for example, the question on the relative effects of the environment vs dispersal on marine microbial biogeography remains largely unaddressed.

That said, overall I think this is an important paper with a strong dataset, and the community should just take it for what it is.

Reviewer #2:

The authors addressed all my concerns and questions satisfactorily and revised the respective parts of the manuscript accordingly.

My impression is that the manuscript gained substantially regarding clarity and limitations of the findings based on all three reviews.

Based on my view of the revised manuscript I recommend its acceptance.

Reviewer #3:

There is no way to separate the "6 organismal size fractions" by filtrations. Take for example the 0.22 to 1.6 fraction, although it will be enriched in bacterial DNA up to 20% will be viral. Or even worse, 5 to 20 will have large amounts of virus and bacteria, even 180-2000 "animal" fraction will have all the microbiomes of planktonic animals that will lead to unpredictable background noise in "metagenomic dissimilarity"

Daily sunshine duration cannot be a proxy for season. In fact, autumn and spring days can have a similar duration but are the opposite in terms of stratification, nutrient availability and community structure (think for example of comparing March 21st with September 21st both close to the equinox but extremely divergent in conditions in temperate latitudes).

The use of eukaryotic (even animal) MAGs is too novel (only a preprint yet) and requires extensive benchmarking before it is used to test such a scheme of dividing the world oceans into "genomic provinces". Something similar would have been much more reliable if applied to prokaryotic MAGs.

Finally, Tara Oceans although very large in terms of Terabases is not a good geographical sampling since it did not have into account depth profiles or season of sampling.

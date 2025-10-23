# Peer review - Round 1

Editors:
- Yaroslav Ispolatov, https://ror.org/02ma57s91 University of Santiago Chile Chile

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94587.sa0](https://doi.org/10.7554/eLife.94587.sa0)

This important theoretical and numerical study deals with a contemporary topic in evolutionary biology, immunology and population genetics. The structure of the models and the analytic framework used are relevant and sound, and the combination of two types of models is a powerful approach that produces compelling evidence to support the hypothesis on the role of heterozygote advantage in maintaining MHC gene polymorphism. The description of the models is easy to follow, and the paper would be of interest to specialists in evolution, immunology, and the general eLife readership.


---

# Peer review - Round 1

Editors:
- Yaroslav Ispolatov, https://ror.org/02ma57s91 University of Santiago Chile Chile

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94587.sa1](https://doi.org/10.7554/eLife.94587.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Heterozygote advantage can explain the extraordinary diversity of immune genes" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife. However, we would like to keep open the possibility for a new submission of a substantially revised manuscript.

The reviewers were somewhat divided in their assessment, but it is clear from the comments and the editorial discussion that your paper contains novel ideas and insights that could be relevant for a wide audience. The conclusion that heterozygote advantage can in principle explain high degrees of diversity at MHC loci is important. However, the reviewers also identified a number of shortcomings in the paper. Specifically:

1) The biological relevance of the assumptions underlying the model is unclear. In particular, it is not clear whether the model assumptions are realistic enough, particularly compared to previous "bitstring" approaches.

2) There are also a number of mathematical assumptions that are questionable, as pointed out in the reviews.

Overall, the scope of the model would need to be considerably expanded in order to address the points raised by the reviewers. If you choose to revise and resubmit, please address all points raised by the reviewers. We would likely send a revised version of the paper to additional reviewers for evaluation.

Reviewer #1:

This is a very interesting theoretical paper addressing the extraordinary amounts of polymorphism found at MHC loci. The paper shows convincingly that heterozygote advantage can generate coexistence of hundreds of different alleles when there is a tradeoff between the protection that a given allele provides against different pathogens. This result is obtained when the number of different pathogens is not small. The paper is well written, the analysis is sound, and even though the paper is purely theoretical, it will be of interest to a wide audience because of the simplicity of the theoretical principle at work, and because of the importance of the topic.

Some comments:

1. It never becomes clear what the significance is of the number of "modules" assumed to make up an allele. This number is assumed to be 10 in the paper, but it would be interesting to know how the model behaves when this number is varied. Presumably, the higher the number of modules, the higher the number of different alleles that can be maintained.

2. A number of recent papers (including ones by the senior author) have studied the effects of the dimension of phenotype space on the amount of diversity that can be maintained. The number of modules mentioned above could probably be interpreted as the dimension of phenotype space (in some sense), and based on that, I think the authors should discuss their results in the context of previous work about high-dimensional phenotype spaces.

3. The number of different pathogens, m, also plays the role of a dimension, in this case the dimension of the external environment. The authors show that as this dimension is increased, the number of alleles that can coexist also increases. Again, this finding should be discussed in the context of the effect of dimension on the amount of diversity.

4. The model assumes that the pathogens are fixed. It would be interesting to know what happens if the pathogens themselves also underwent evolutionary dynamics. I think the authors should at least speculate about the effects of including this complication in the model.

5. Another connection that should be made much clearer is the relationship of the model that the authors are using to Levene type models for the evolution of habitat specialization. There are some clear paralleles between these two modelling approaches, and this should be discussed and put into context. In fact, I think in some abstract sense, the results that the authors are reporting could be directly translated to certain ecological scenarios of habitat specialization, with the prediction that high-dimensional phenotypes and high-dimensional external habitat structure can lead to large amounts of coexisting diversity, simply based on habitat preference.

6. The authors argue (convincingly) that coexistence of different alleles is due to heterozygote advantage. In general, coexistence of the type described here is always due to some form of frequency dependence, in the sense that each of the coexisting alleles has an advantage when rare. It would be good if the authors could make this connection between heterozygote advantage and frequency dependence explicit (with the latter being a more general concept).

7. The authors mention that they assume multiplicativity for the effects of pathogens (Equation1). Does the whole theory break down with additivity? It would be good to include more comments on this.

8. Likewise, the authors assume codominance in Equation 1. What about other dominance modes? E.g. what about multiplicative effects of the two alleles? Presumably, the results would be rather different in this case…

9. l. 98: the indices i and j appear out of the blue at this point, and it is not clear in what sense they characterize an individual.

Reviewer #2:

Review of Heterozygote advantage can explain the extraordinary diversity of immune genes.

First I should say that I focus on the immunological aspects of this paper and am not familiar with the population genetic aspects and leave these to a referee more versed in the area. There are also a number of theoretical immunologists who have worked in the area of immune recognition by MHC who would likely know this area better than myself. In particular I would refer to Borgans and De Boer's work in this area.

I found it hard to follow the biological underpinnings of some of the paper and will try to explain why. My questions are indicated on lines beginning with a ?

The paper tackles the problem of understanding the causes of MHC diversity. Why are there so many alleles at each locus of the MHC. It would be good if the authors gave us an idea of the extent of the number of alleles that are found at each MHC locus, so we can get an idea of the magnitude of the diversity we are trying to explain. The approach, as far as I could tell is as follows:

1. The authors use what looks similar to previous bitstring model to describe the extent to which a given MHC provides protection against a given pathogen. Each MHC is given by an m-dimensional vector m as is each pathogen which is given by p.

2. The efficiency of a given MHC in controlling a given pathogen decreases with increasing euclidian distance between the vectors m and p. I.e. e(p-x)

3. The overall efficiency of a given individual against a pathogen is the sum of the efficiencies of its two MHC alleles at controlling the pathogen.

4. The efficiency of an individual against an ensemble of m pathogen c is the product of the efficiency of that individual for controlling each pathogen.

This is basically equation (i)

5. Selection is a function of c above.

6. They follow the evolutionary dynamics of alleles of MHC in a diploid population of size N.

7. The key results are in Figure 3. The degree of MHC diversity maintained increases with increases in the number of pathogens the degree of pathogen dissimilarity and occurs at intermediate levels of the half saturation constant K.

Comments in order of being encountered in the paper.

1. Why not use the earlier bitstring models rather than a new model. What is the justification of letting the elements of m and p be real numbers (and what determines how large these numbers can be?).

2. Why have c_max or whether the 2 is needed in Equation 1

3. What is the degree of selection that the pathogens chosen impose? Is it biologically reasonable given what we know about MHC?

4. The number of pathogens appears limited to a max of 8 why? How does it scale for more reasonable numbers.

5. Why have models with symmetry in distances between pathogens as in version 1.

6. I don't see the need for recombination … there can be different MHC generated by mutation.

7. Is it necessary to use an idea of generalist – it is supported by a single paper and not potentially yet part of mainstream immunology.

8. From 3 it seems that a key feature is the degree of dissimilarity. A search of the document does not find it being defined? What are biologically plausible values for this parameter?

9. Does the model make any predictions that allow discrimination or rejection of current hypotheses?

Overall I found it hard to follow the paper. To a large extent may be because I am not an expert in population genetics. More problematic was the difficulty I found understanding the details of the connection with immunology and lack of parameterization of biologically reasonable parameter regimes. I would be more convinced about the claims of the authors if the above questions were addressed. Finally I believe that either Jose Borghans or Rob De Boer would be very well suited to review the paper.

Reviewer #3:

There are good reasons to assume that individuals with two different alleles at an MHC locus are better protected against pathogen-induced disease (and, hence, have a higher fitness) than individuals that are homozygous for any of these alleles. Based on this, it has been argued that such heterozygote advantage may explain the high degree of polymorphism found at MHC loci. However, there is a problem with this argument. In principle, an arbitrary large number of alleles can be kept in the population by heterozygote advantage, but this is only possible if (1) all heterozygotes have a similarly high fitness, while (2) all homozygotes have a similarly low fitness. If the fitness effects of MHC alleles are drawn at random, it is unlikely that these conditions are satisfied. For this reason, earlier studies concluded that heterozygote advantage is most likely not the only factor explaining the high degree of MHC diversity. In the present study, the authors demonstrate that, in principle, the heterozygote-advantage hypothesis can be rescued if the current MHC alleles did not 'fall from the air' (i.e. were created by random mutation of large effect size) but instead were shaped by gradual evolution (based on the rare influx of mutations of small effect size). The authors argue that (under suitable conditions) this evolution process has the tendency to shape MHC alleles in such a way that conditions (1) and (2) are satisfied, hence allowing the stable coexistence of many (even hundreds) of MHC alleles.

The study shows that probability calculations, as in earlier studies, have to be taken with care, since the current MHC alleles may not be a random sample from a universe of possibilities but rather the product of diversifying evolution. This insight is interesting and important.

I am less impressed by the model that is used to illustrate their point. Most importantly, fitness (survival) is assumed to be a function of 'condition,' which in turn is defined in a rather specific manner (Equations 1 and 2). To me, it would have been plausible to define survival directly by the product term in Equation 1 (overall survival results from surviving many pathogen-induced challenges), but now this term is plugged into a saturating Michaelis-Menten function. Due to this transformation (which is not motivated well), conditions (1) and (2) are much more easily satisfied. I would like to see the same analysis, but now for the more plausible assumption that condition corresponds to viability. I would also have appreciated if the authors had applied their method to other fitness functions, like the one in De Boer et al. (2004), in order to work out more clearly why the authors arrive at conclusions that contrast with those of earlier studies.

The authors use an adaptive dynamics approach for modelling the fine-tuning of MHC alleles. I wonder whether this kind of approach, which is based on continuously varying traits and very rare mutations of very small effect size is realistic in the context of MHC evolution. Mutations of MHC alleles seem to occur frequently, and even point mutations do often have a large effect. In other words, the genotypic-phenotype mapping is most probably quite intricate, making some baseline assumptions of the model (e.g. Gaussian distribution of effect sizes) questionable. The study would have been more convincing if the authors would have incorporated more realistic assumptions on the action of MHC alleles in their individual-based simulations, rather than just mimicking the assumptions of their analytical model.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Heterozygote advantage can explain the extraordinary diversity of immune genes" for further consideration by eLife. Your revised article has been evaluated by Detlef Weigel (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #2 (Recommendations for the authors):

The MHC genes encode proteins that bind antigenic oligopeptides and present them to receptors on immune cells. Successful presentation of antigens to immune T cells by the MHC is the key stage in the immune response to pathogens. While T cell receptors are variable and can adapt during the process of clonal selection, the MHC repertoire is inherited from parents and does not change during an individual's lifetime. Any pathogen genotype that escapes presentation by the MHC is able to reproduce at a higher rate due to the lack of initiation of an effective immune response. MHC genes are under strong natural selection for efficient binding of pathogen antigens, but surprisingly are often represented by hundreds of alleles (variants) in natural populations of vertebrates. In addition, MHC genes are often characterised by extremely long genealogies. These two features of MHC genes are particularly difficult to reconcile with strong natural selection, which usually results in low genetic polymorphism and often a short coalescence time. The paper by Sijestam and Rueffler investigates the role of one of the key balancing selection forces, the so-called heterozygote advantage, which has been hypothesised to maintain MHC gene polymorphism.

Strengths

The manuscript is clearly written and deals with a current and important topic in evolutionary biology, immunology and population genetics.

The structure of the models presented and the framework used are sound, with one of the models based on a classic theoretical work in the field and predict results that contradict the majority of recent theory on the evolution of MHC gene polymorphism.

The description of the models is easy to follow. The combination of two types of models ('Gaussian model' and 'bit-string model') is a powerful approach to test the hypothesis on the role of heterozygote advantage in maintaining MHC gene polymorphism.

The authors list two key assumptions of their model, which they believe are responsible for the conclusion of the paper. However, only one of these assumptions actually provides fundamental support for the role of heterozygote advantage in maintaining MHC gene polymorphism. Recent models show that the Red Queen process is able to maintain high levels of MHC polymorphism despite the mortality of hosts that respond poorly to infections (see detailed comments).

The work has the potential to shed new light on the long-standing debate about the importance of the Red Queen process vs. heterozygote advantage as a balancing selective force that maintains MHC gene polymorphism, although further analysis is needed to address concerns about some of the model assumptions made.

Weaknesses

There are two fundamental weaknesses in the manuscript, as the models in their current form and without additional analyses do not have sufficient scientific strength to restore the heterozygote advantage as a force capable of maintaining high genetic polymorphism of the MHC. First, because some of the assumptions used to model heterozygous advantage differ from those used in previous studies (suggestions I, II below). Second, because there is no reference to the Red Queen, which a balancing selection force currently receiving considerable attention in studies of MHC polymorphism (suggestion III). I also strongly believe that my concerns about the current limited power of the conclusions presented by the authors can be addressed by adding the suggested analyses. This could be quite a lot of work, but the analyses do not need to be performed in the full parameter space but are mandatory for the paper to be of the highest scientific quality. Here is a short list of the analyses that need to be added (see below for a more detailed description): (I.) In the Gaussian model, add analysis of pathogen peptides evolving by genetic drift by allowing Brownian motion to move the pathogen distribution in allele trait space. (II.) In the bit-string model, add analysis of pathogens evolving by genetic drift. (III.) Add simulations with only the Red Queen process operating (e.g. by simulating haploid hosts co-evolving with pathogens). However, it is necessary that all current assumptions of the bit-string model remain unchanged (including the relationship between infection outcome and host fitness), except for the addition of pathogens co-evolving with hosts.

- The authors do not communicate, or perhaps do so in a way that can be easily overlooked by the reader, the fundamental conceptual challenge associated with testing the role of heterozygote advantage in host-pathogen evolution. By this, I mean that heterozygote advantage can only be modelled or tested in the absence of host-pathogen coevolution, because coevolution generates negative frequency-dependent selection (the Red Queen process). Without this explanation, the fact that pathogens do not evolve in the model may seem ridiculous to the reader. This aspect needs to be clear from the point at which the model is described, or perhaps even from the introduction.

- In this model, pathogens do not reproduce, and I have explained above why authors cannot indeed link pathogen fitness to the host immune response if they want to test heterozygote advantage in the absence of the Red Queen process. However, as I understood from the description, pathogens in the bit-string model consist of random pools of peptides: "In the bit-string model, the m pathogens are each given npep randomly drawn bit-strings", and in the Gaussian model, the centres of the pathogens do not change their position in the allele trait space. The consequence of this assumption would be an evolutionary process that stops far in the future (pathogens are constant over time). Even if I am wrong and pathogens are randomly generated in each generation, this will still be incorrect because the model artificially assumes the maximum possible genetic diversity of pathogen peptides, which combined with the way fitness is calculated (similar to a geometric mean) would only favour a large number of alleles under heterozygote advantage. Furthermore, such an unrealistically high genetic diversity of oligopeptides simulates pathogen populations of much larger effective size than in real populations. A proper model for modelling heterozygote advantage would require modelling pathogens evolving by genetic drift. Even if the authors do not agree with my point, they should include the scenario in which pathogens evolve by genetic drift, as this has been assumed in previous models addressing the question of the role of heterozygote advantage and Red Queen on MHC polymorphism. Pathogens evolving by genetic drift are easily implemented in the bit-string model. In the Gaussian model, I would suggest introducing Brownian motion of pathogen distributions. It is very unrealistic to assume that pathogens would occupy a stationary point in the allelic trait space over so many generations, rather than moving.

- Host fitness is calculated using geometric mean mechanics, which forces the MHC allele (in a hypothetic haploid individual) to be located in the middle of the pathogen distributions located in allele trait space. This is a very strong assumption and differs from other theoretical studies of MHC gene polymorphism (e.g. Borghans et al. 2004, Ejsmond and Radwan 2015). Note, that I do not say that this is an incorrect assumption. Perhaps natural systems differ in the way infections affect host fitness. Anyway, the lack of modelling of other balancing selection forces in the presented work, namely the Red Queen (negative frequency dependence), leaves the reader with a big question mark as to the extent to which the result presented by authors is driven by the specificity of the model or the assumption that immune response and fitness scale in a 'geometric mean'-like manner. Thus, I think the Red Queen process scenario needs to be added, and my suggestion should not be taken as a suggestion of adding an additional analysis beyond the scope of this paper. Each model has its own specificity and it is necessary to know what the levels of polymorphism are when the Red Queen process is simulated. My expectation would be that if fitness is calculated in the way the authors did, the Red Queen process will maintain few alleles. This would be a strong message emerging from this study and the previous literature that heterozygote advantage or the Red Queen process can maintain polymorphism depending on the distribution of fitness effects of infections by different pathogen species.

- The authors should comment on the fact that the MHC gene polymorphism in their model would break down in the presence of several highly virulent pathogen species (narrow distributions in the Gaussian model) and under more realistic assumptions for pathogen classes e.g. helminths, i.e. a large number of antigenic oligopeptides (Figure 5 for v=5).

- The assumption (a) that pathogens are lethal in the absence of an appropriate immune response does not support the role of heterozygote advantage in maintaining MHC gene polymorphism as suggested by the authors. See the model of Ejsmond et al. 2023 ('Adaptive immune response selects for postponed maturation and increased body size'), where hosts with a poor response to pathogens also die, but high MHC gene polymorphism is maintained in particular by the Red Queen process. However, note also that Ejsmond et al. assumed that infections affect fitness proportionally, which is contrary to assumption (b) in the reviewed paper. I would suggest reducing the importance of the first assumption or discussing alternative models that show that the Red Queen process is able to maintain high MHC gene polymorphism despite assumption (a). I believe that the difference in assumption (b) is fundamental to the conclusions derived from this paper and other models.

- Show information about the proportion of hosts in the population dying per generation under main simulated scenarios

- Consider renaming 'allelic trait space' to epitope or agretope space

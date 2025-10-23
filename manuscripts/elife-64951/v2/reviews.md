# Peer review - Round 1

Editors:
- Wenying Shou, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64951.sa1](https://doi.org/10.7554/eLife.64951.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Cell cycle duration acting as a filter that constrains transcription is an idea proposed 30 years ago. Here, authors propose that a very simple model can produce results that qualitatively echo single-cell RNA seq data published by other labs. Overall, this study suggests that the slowing down of the cell cycle during development can act to allow longer genes to be transcribed and more cell types to be generated. Experimental test of this hypothesis are needed for future work.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Control of tissue development by cell cycle dependent transcriptional filtering" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, including Wenying Shou as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: David M Suter (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Although there was some support for your work, the amount of time required for revision will likely exceed two months. It is the policy of eLife that a manuscript requiring substantial revision should be rejected. We do invite you to resubmit if you feel that you have addressed reviewers comments.

Reviewer #1:

Abou Chakra et al. posed the hypothesis that cell cycle transcriptional filtering – the transcribing of long genes only when cell cycle slows down – might help control tissue development and the generation of diverse cell fates. This study is based on simple math modeling and comparing model predictions to single-cell RNA seq data.

From an outsider's point of view, the article is interesting, although very speculative. Thus, I suggest softening your statements throughout. For example, the current title can be changed to "Cell cycle dependent transcription filtering can potentially contribute to tissue development".

Scientifically, I would like to see an analysis of whether transcripts specific to development (e.g. neuronal development) tend to be longer.

Reviewer #2:

This study addresses the important and exciting topic of how the cell cycle duration gates gene expression diversity at the single cell level by limiting the expression of long genes. This work intersects between genetics, gene expression, developmental and evolutionary biology, and should therefore be of broad interest to the readership of eLife. The manuscript is well written and structured, and the findings are interesting. I have some technical and conceptual concerns about the causality links made by the authors.

1. In general the authors should provide more details about the implementation of their method in the manuscript. While Figure 1 is very clear and allows non-specialists to grasp the concept, a more detailed explanation of the model would be useful.

In particular, how is transcription re-initiation modelled ? This is important for the following reason. If a gene takes 10 hours to be transcribed and the cell cycle is 10 hours, only 1 transcript can be made. However, if the cell cycle is longer, the maximum number of transcripts will depend on the distance between successive polymerases (thus depending on initiation rate), and could thus rapidly increase. The number of transcripts generated in 11 hours will thus scale with initiation rate, or inversely with the distance between polymerases on the gene. Also, how does transcriptional bursting affect their modelling ?

2. The authors show that short genes tend to be expressed at higher levels than long genes. They use this data to support that elongation rates * cell cycle duration limits the expression of long genes. In this scenario, one would expect that long genes are more depleted in pol II at the end of the gene, while short genes would not. The authors could look into Pol II footprinting/ChIP-seq datasets to confirm this, and also to exclude that short genes are expressed at higher levels because of their higher initiation rates.

3. The authors mention that cell cycle duration should be broadly correlated with development time. But cell sizes and organism size will also impact this correlation. Why do the authors not consider these parameters ?

4. The authors should provide an analysis of which classes of genes are enriched into different genes length bins. According to their results, more specialised genes, i.e. expressed in terminally differentiated, non-dividing cells should be longer on average.

5. Figure 6A: How can the average cell cycle duration become higher than the max cell cycle duration at the single cell level (shown as color code) ?

6. What is the relative contribution of introns vs exons in long vs short genes ? Could the longer cell cycle of some species allow to accumulate more/longer introns to increase splice isoform diversity/regulatory potential ?

7. Linked to 5., one challenge here is to understand causality links. The cell cycle could be used by organisms to gate cell diversity during development, but longer cell cycles could also allow to accumulate longer genes on evolutionary time scales. The authors should comment on this.

Reviewer #3:

We've known for a very long time that cells in many animal embryos have very fast cell cycles, and that the duration of cell cycle increases as cells differentiate into progeny with specialized function. However, whether cell cycle duration directly impacts cell fate decisions via filtering transcriptional activity is not clear. Certainly it has been proposed on multiple occasions, and the ability of mitosis and DNA replication to interrupt and abort transcription has been demonstrated. This study presents an interesting attempt to address this topic via mathematically modeling the relationship of cell cycle length and the diversity of transcriptome. The authors utilized a simplified model to simulate how cell cycle length, gene length, number of genes and transcription rate affect resulting transcriptomes in cell populations. Not unexpectedly, the simulations show that increasing the length of the cell cycle can increase the proportion of mRNAs from long genes, and also the complexity of the transcriptome and (more interestingly) the diversity of transcriptomes between different cells in a population. The model is clever and the demonstration is useful, if highly over-simplified. Importantly the authors also analyze some real transcriptome data to see if it supports their conclusions. At some levels there is support, but overall the real data from single cell sequence don't align well with their hypothesis and fall short of a compelling experimental validation. Overall we felt the study was interesting in concept and could be a valuable addition to the literature devoted to cell cycle and development, but that it could be much better with comprehensive revisions as discussed below.

1. The simulations in Figure 2A show that increasing cell cycle duration will allow more relative transcription of longer genes. Unfortunately the real data from Xenopus and Danio (Figure 2B, S2) don't appear to show this same trend. The authors should check this more carefully by comparing proportions of transcripts of different lengths at the different developmental times. If there is not change in proportions then the real data may not validate the simulation's predictions. At issue might be the "contamination" of the real data with maternal transcripts. Perhaps the authors should try to remove maternal transcripts and analyze only zygotic transcripts. Furthermore, the timepoints shown for Xenopus in Figure 2B are probably too late and too closely spaced to see a trend. They should compare transcripts for very early and very late in development.

2. I was not convinced by the simulations and arguments about the generation of cell diversity. It seems that this might only occur with very low numbers of transcripts per cell; i.e. when stochastic variation came into effect. This may not be the case for real cells.

3. Figure 6AB really baffled me. Transcriptome diversity seems not to be graphed at all (check the axis labels and key), even though diversity is the point of the figure. Either it is mis-labeled or it needs more explanation. Figure 6C also requires more explanation, both within the figure and in the text (lines 219-227), which is opaque.

4. Figure 5 states that slower cell cycles would increase cell type diversity at the price of fewer progeny number. However, the real data in Figure 6 don't support this idea. Slower cell cycle actually increased differentiated progenies, this suggests that the authors' simulation settings failed to capture a critical aspect of the regulation of transcription.

5. We suggest that the authors also look into the Oikopleura dioica genome (see Danks et al. 2012 "OikoBase: a genomics and developmental transcriptomics resource for the urochordate Oikopleura dioica"). This could be very interesting because this organism develops exceptionally fast (embryogenesis last 4-5 hours before hatching a tadpole), and they have an incredibly compact genome (most introns are no longer than 100 bp). There is also good transcriptome data from Drosophila that could be informative, especially if maternal transcripts could somehow be subtracted out. Overall, the analysis of real transcriptome data is superficial, and much more could be done here, that might support the authors' conclusions much better that what is presented.

6. In the introduction (line 47), the authors should state how they envision the "transcriptional filter" works. By abortion of transcription at M phase? Or during S phase? There is data on both mechanisms and these should be cited and described explicitly. This also comes up in the discussion (line 269). The authors should be aware that the attenuation of transcription during S-phase is limited to interactions with replication forks. In fact there is a great deal of transcription in most S phases.

7. We were uncomfortable with the assumption that appears to be made on lines 86-92 and Figure 2, where the number of transcripts made during a period of time equals: synthesized transcripts=time/time to make one transcript. Does this assumption fail to take into account that multiple RNA transcription bubbles may exist on the same gene once transcription starts, thus speeding up transcript production once the first transcript in finished? If so it is inaccurate.

Reviewer #4:

This manuscript presents a theoretical model that explains potential contribution of cell cycle, as a transcription filter, to organism development. The hypothesis is not entirely new. The main contribution is that the authors defined a math/simulation framework and compared it with some real data (gene size distribution in various organisms and single-cell transcriptomic data obtained from several organisms/processes) for justification. Overall, I do not feel this work adds much new to current understanding. Real data did not strongly validate the proposed model, nor led to refinement in knowledge/hypotheses.

1. Page 4. Algorithms and parameters used in simulation were not described in sufficient detail. For example, how were single-cell RNA-seq data simulated? Was noise considered?

2. Figure 2, the trends between A and B are similar but the actual distributions are not: either mean average transcript count per cell, or the extent of spread look quite different. One could also argue the dissimilarity between the two figures. Does it reveal that the model lacks necessary accuracy? This needs to be further discussed/explained.

3. Figure 3A. The authors should be able to derive analytical solutions for the transcriptome diversity, directly from the model defined in Figure A. Not sure why they need to show these relations indirectly from simulation (Page 5). Perhaps it is the order/logic of the presentation.

4. Figure 3C. Unclear how many cells are there under each condition (when does the simulation stop?) and how do #cell affect the clustering results. Also, #cluster, as a metric is quite misleading (not comparable across conditions) without specifying the total #cell and the clustering algorithms/parameters used.

5. Page 6, the authors stated that "we expect faster developing organisms to have short cell cycles and genes whereas slower developing organisms will have longer cell cycles and genes". This is very rough. Can it be quantified and then supported by the proposed model?

6. Figure 4. How were the 11 genomes selected? Why not select more? Are there genomes that do not follow the trend, i.e., having large genome but relatively shorter genes? Also, it is unclear in what order the organisms are listed. Particularly, Fugu and zebra-fish did not follow the monotonic trend in means. Some distributions do not look statistically significantly different.

7. Figure 6. E15.5 and E17.5 has a slightly reversed trend.

In general, there needs to be more real data used to back up the theoretical models.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Control of tissue development and cell diversity by cell cycle dependent transcriptional filtering" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Wenying Shou as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: David M Suter (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this decision letter to help you prepare a revised submission.

Essential revisions:

The decision has taken a long time because as you will see, the three reviewers have disagreements. Upon further discussions, we have reached an agreement. We feel that although experiments are always desired, there should be a place in science for extracting information from published datasets, despite the varying quality of datasets. We will waive the requirements for experiments, but we do request you to address comments not related to experiments, and be very careful in stressing the limitations of the datasets you used and the conclusions you drew. For example, your model suggests a mechanism, but does not exclude other mechanisms.

Reviewer #1:

1. Figure 4: It may be more meaningful to model stem-cell like behavior where a fast cell always gives birth to a slow and a fast cell, whereas a slow cell always gives rise to two slow cells. I believe that the cell # patterns will look more realistic under this assumption.

2. Figure 7: I am not sold about this figure and the associated text. "Sensory" and "perception" (short genes) seem to be related to neural-development (long genes). Also, the main text said "shortest genes… enriched for genes involved in core processes (e.g…. transcription…), whereas in Figure 7, "transcription" is associated with long genes.

Reviewer #2:

I found the revised version of this manuscript improved, and the authors have adequately addressed most of the points I raised.

Notably, they now describe more in detail their methodology, and also assess how their model behaves when assuming that several RNA Pol II can be present on the same gene. I would suggest to use this as a first assumption rather than "We assume RNA polymerase II re-initiation occurs once a transcript is complete". To me the latter one is not supported by what we know about transcription that occurs in bursts that can generate large number of RNA molecules within minutes. Also see Tantale et al., Nature Communications 2016, who show evidence of RNA Pol II convoys on actively transcribed genes.

Reviewer #3:

In this manuscript the authors use mathematical modeling to address whether cell cycle length determines cell fate using a correlation of gene transcript length. Since a longer cell cycle time, allows transcription of longer genes, it could affect the cell fate of the progeny. If longer transcripts are needed for highly differentiated cells, there would be a need for longer cell cycle times. Since it has been shown in stem cells that lengthening of the G1 phase is correlated with increased differentiation of cells, this hypothesis could make a lot of sense.

Using mathematical modeling is a great approach to answer this question and is definitely one of the strengths of this manuscript. This manuscript is trying to address an important and fundamental question that has been on the minds of scientists for a long time.

The drawback of the manuscript is that validation of the hypothesis is only partially or poorly confirmed by the experimental data. Essentially, the data does not contradict the hypothesis of the authors. This is great but is it good enough? Should the data not univocally prove that the hypothesis is correct? One of the major issues is that the authors use publicly available data, which originates from different organisms, different developmental time points, and have been acquired using different platforms. Therefore, the underlying data may not be solid enough.

Rather than trying to find universal rules that apply to all organisms, tissues, and developmental time points, it may be more useful to stick to one organism. If the authors could prove that their hypothesis is correct even in only one specific cell types, this would be an important step. Sometimes taking a small step can be more important than making a giant leap that is not well supported by the data.

This manuscript is interesting and contains good hypotheses but for sure the authors had to use a number of simplifications. Whether this still allows to generalize the conclusions of this manuscript is up for debate.

I am not a mathematician and therefore I am not able to check the mathematical models that were used. Nevertheless, I will assess if the conclusions make sense in real biology.

My conclusion after reading this manuscript is that of interest but remains speculative. What I mean by this is that the mathematical predictions would need to be verified by experiments. Although the authors use a number of datasets, they are assembled from different organisms and different developmental timepoints. As the authors mention, the data does not contradict their hypotheses. This is ok but maybe not good enough? Should the data not univocally support the mathematical hypotheses in order that the readers will buy them?

Here are the main reasons:

1. Line 128: "in general, cells express more short genes than longer genes over multiple developmental time points." Although there may be a trend, I am not entirely convinced of this statement. There seems to be a lot of noise (variation), which may not support this conclusion.

2. Line 223: "While cell cycle duration measurements are not widely available, we instead ask if organisms with longer genes would also take longer to develop." Although this is understandable, I am not sure that this is a correct surrogate. The duration of development must not necessarily be dependent on cell cycle length. Nevertheless, I agree the cell cycle duration measurements are not widely available.

3. The authors use data from different organisms and from different developmental time points. Of course, the idea is that there are universal rules that apply across species. This would be ideal but is there any proof of that? The unwanted side effect is that it becomes really confusing and the authors may compare apples to oranges.

4. Then there is the issue of splicing and introns. It is not surprising that larger genes contain more introns. To some degree splice isoforms could also explain the differences between stem cells and differentiated cells. Nevertheless, I feel this is a distraction. Therefore, analyzing organisms that contain few introns would be more useful. Budding yeast is such an organism.

5. The pathway analysis of the short and long genes is not thorough enough. In addition, the authors should use random sets of genes (same number) from the intermediate genes, which are the majority of genes.

6. The time it takes to transcribe a gene is not only dependent on its size and a fixed speed. This is an oversimplification.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Control of tissue development and cell diversity by cell cycle dependent transcriptional filtering" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Wenying Shou as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: David M Suter (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Please revise your writing to address Reviewer 1 and 3's critiques.

Reviewer #1:

Authors have mainly addressed my comments.

Figure 9: I wonder whether you can make further statements. For example, if immune cells have short cell cycle, then its enrichment for short genes will make more sense. Also, might olfactory short genes be related to environmental sensing genes which in turn involve signal transduction pathways also used in fast-growing cells?

Figure 5 legend: 220 should be 219.

Reviewer #2:

I am happy to see that the authors successfully integrated RNA Pol II re-initiation in their model, which did not affect their conclusions. The authors have addressed my concerns adequately, and the manuscript should be ready for publication.

Reviewer #3:

The authors have invested efforts to address the issues that were raised by the reviewers. The story of this manuscript has not fundamentally changed (which probably was also not expected) and there remain shortcomings. One aspect that I wish would improve is to use more understatement rather than claiming things that the authors cannot prove.

Here are a few examples, there the manuscript could be improved:

1. Line 128/129: "found that, in general, short genes have a higher expression level than longer genes within a cell." When I was reading this, I had trouble believing it but in Figure 3B, the authors show mRNA expression. This is though not mentioned in the text and the reader can be misled that this also applies to protein expression. It would be desirable that the authors are precise without using generalizations.

2. Line 179: "second child cell" I believe these are usually referred to as "daughter cells".

3. Line 233: "We started by asking if organisms with longer genes would also take longer to develop." I apologize but this question (or hypothesis) does not make a lot of sense to me. There are a million reasons why an organism takes a certain amount of time to develop and this may be also dependent on the environment. Reducing it to the length of the genes is surely only one of many reasons. In their conclusion on line 249, the authors call it "strong relationship", which probably is an association and we all know that associations are weak (remember the one about the amount of chocolate consumption and that chance to win the Nobel prize?).

4. Line 266-278: I am not sure if I get the point here "cell cycle duration and gene expression vary spatially.". Not only spatially but also dependent on age, environment, nutrition, and many more factors.

5. In the discussion, the limitations (some of which are mentioned) should be discussed much more honestly.

6. In several figures (for example Figure 6—figure supplement 2 but there are others), the authors use a representation (word clouds) that are not very helpful. The authors should find a better way to bring across the point that they are trying to make.

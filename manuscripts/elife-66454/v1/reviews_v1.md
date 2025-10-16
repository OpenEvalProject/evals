# Peer review - Round 1

Editors:
- Aleksandra M Walczak, École Normale Supérieure France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66454.sa1](https://doi.org/10.7554/eLife.66454.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper tackles a central question in epigenetics, namely how chromatin-based gene regulatory information can be propagated through cell cycles. They show that incoorporating additional memory elements into a mathematical model, in the form of localized, heritable, protein oligomers recapitulates experimental data.

Decision letter after peer review:

Thank you for submitting your article "Hybrid protein oligomer-histone modification mechanism for PRC2-based epigenetic switching and memory" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Aleksandra Walczak as the Senior and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: Nicole Francis (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Please respond to Reviewer 1's comments.

Reviewer #1:

In this paper, Lovkvist et al. develop a model for epigenetic memory based on regulation of the FLC locus in Arabidopsis by PRC2 and H3K27 methylation. This model captures epigenetic switching and memory, and the processes of nucleation and spreading of histone modifications. The model is fundamentally different from "classical" histone read-write based models (including from this group) in introducing a second memory element, here proposed as a locally formed protein oligomer. This group previously developed a model that could explain the generation and stability of large domains of H3K27me3 (including at the FLC gene) using PRC2 read-write mechanism as the main feature. However, their observation by this team of "metastable" silencing at FLC in mutants (like lhp1) that nucleate H3K27me3 but do not spread it over the locus prompted them to re-evaluate the model. The observed metastable silencing seems to depend on only three highly methylated nucleosomes, too few to maintain silencing in the previous read-write based model. The authors therefore surmised that there must be a mechanism to allow very small chromatin domains (like the nucleation region of FLC) to propagate. They propose two options: 1) precise segregation of parental histones between strands; 2) additional memory elements (proposed as locally formed protein oligomers) at the nucleation site. The first model is implemented and rejected, (see point 1 below) since it does not capture the experimental data. The second idea, the formation of heritable protein oligomers at the nucleation site, is developed into a model that can capture the dynamics of the system and predicts ~17 "memory elements" are required to do so. This model is developed using the simplified lhp1 mutant (which only has H3K27me3 at the nucleation site and shows metastable silencing). The authors use VIN3 as a candidate protein oligomer, although direct evidence for this is lacking, and indeed VIN3 expression is consistent with this function in the early, but not later part of the process The model is then generalized to a wild-type scenario by adding a looping read-write based mechanism to spread H3K27me3. The model also responds to removing the nucleation region by losing silencing and H3K27me3 similar to the effect of deleting a PRE (Polycomb recruiting elements in Drosophila), further supporting its generality to Polycomb regulation in other systems. Finally, the model could be altered to capture the altered FLC regulation dynamics in an Arabidopsis genetic variant.

The key new aspects to the model are the requirement for an additional memory element to capture the observed dynamics, and the specific hypothesis that this element is in the form of heritable protein oligomers. This model may be generalizable to Polycomb regulation in other systems. The ability of the model to predict (meta)stable chromatin states that involve small chromatin domains could also have more general relevance beyond Polycomb function. The complete rejection of balanced segregation of parental histones in the model would need to be reconsidered in light of recent data. Additional explanation of the envisioned mechanism of nucleation of protein oligomers in light of what is known about Polycomb protein recruitment mechanisms would need to be provided. The model also recapitulates H3K27me3 dynamics well but loss of metastable gene silencing less well.

Comments for the authors:

1) The authors consider a model for balanced segregation of histones (Figure SX), but reject this model because it does not fit the experimental data well. However, I do not see why this model should be mutually exclusive with the protein oligomer model-I think it would be appropriate to consider a model with both the protein oligomer and balanced histone segregation. The data from both yeast and mammalian cells indicating that chaperone activities at DNA replication forks promote either leading or lagging strand deposition makes it not only possible but likely that segregation is not random (10.1126/science.aau0294, DOI: 10.1126/science.aat8849, DOI: 10.1016/j.molcel.2018.09.001) Work showing regulated biased segregation in Drosophila germline stem cells (from the Chen group DOI: 10.1038/s41594-019-0269-z) provides additional evidence that this process can be regulated.

2) While I think the author's hypothesis is likely to be correct, and is very exciting, I find that certain features of the model seem highly specific in cases where data ruling out other possibilities does not exist. I don't think the model needs to be changed, but I think acknowledging other possibilities makes the ideas behind the model more general.

– page 7 lines 252-253 why do the protein oligomers segregate randomly? it seems equally possible that they segregate equally, or may not segregate at all but be shared between replicated chromatids prior to sister resolution.

– page 7 line 262-264 is it essential that the new memory elements are required to initially create the nucleation site? couldn't there be a separate mechanism for this?

– page 7 lines 290-292-why is it assumed that the oligomers activate rather than recruit PRC2 (i.e. increase its binding at the nucleation site)

– page 8 line 323-324 "we note that the oligomer size before replication must be more than twice the minimal size needed for a stable oligomer…." can the authors explicitly relate this to the conclusion that ~17 memory elements are needed-this is before replication?

– page 9 lines 349-351 Please explain why VIN3 is specifically found at the nucleation site (e.g. is it recruited by something else?)

– page 11 line 440-441 "the oligomer's only effect on histones is to enhance H3K27me3 in the nucleation region" – Why would this be the case, and is it essential? If looping involves contact between PRC2 at the nucleation site and the distal nucleosomes, it seems quite likely that the effects of the protein oligomer would still occur (unless the oligomer recruits rather than stimulates PRC2).

3) In figure 1C, the "peak" of H3K27me3 is not obvious. From both these data and the supplemental data, it seems like H3K27me3 (when normalized to H3) is similar across the region; without a true negative for comparison, I do not see how these data indicate a 3-nucleosome wide peak (which is fundamental in the model). The published data from Yang et al. (Science 2017) is more obvious.

4) It looks as though the model recapitulates H3K27me3 dynamics at the nucleation region well (Figure 2C), but loss of metastable silencing less well (Figure 2D) (although additional data points would be very helpful here). Do the authors have an explanation for this?

5) The authors invoke a looping mechanism to explain spreading of H3K27me3, but it would be interesting to consider the model of Chory et al. doi: 10.1016/j.molcel.2018.10.028, which also can explain spreading from a nucleation site, but through a distinct mechanism (histone exchange).

6) It would also be interesting to consider (perhaps in the discussion) the model of Pease et al. (DOI:https://doi.org/10.1016/j.celrep.2021.108888), which is somewhat analogous to what is proposed here in requiring a two step mechanism to explain H3K27me3 dynamics and silencing, but invokes chromatin compaction as the "other" element.

7) The usual explanation for the requirement for silencing elements in yeast and PREs in Drosophila is that sequence specific DNA binding proteins that recruit Polycomb proteins continuously recognize these elements, thereby recruiting chromatin modifying enzymes. Here, it is proposed that locally formed protein oligomers serve this function. I think the relationship between recruiting TFs and the stochastic nucleation of protein oligomers could be explained more clearly. Is there still a role for recruiting TFs (or other recruitment mechanisms)? How are the protein oligomers formed at the correct genomic location? Are oligomer forming proteins recruited by TFs (particularly in the case of PREs)?

Reviewer #2:

This manuscript discusses PRC2 based epigenetic switching and memory at the FLC locus in Arabidopsis thaliana. PRC epigenetic memory is linked to H3K27me3 through a read/write maintenance mechanism, epigenetic state switching and memory over many cell cycles. To explain such a persistence, the authors introduce a mathematical model envisaging an extra protein memory storage with oligomeric feedback that persist through replication, in addition to histone modifications.

I find the paper very well written, scientifically sound and very interesting. Additionally, the proposed model describes a generic mechanism that could be widely applicable.

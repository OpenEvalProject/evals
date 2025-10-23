# Peer review - Round 1

Editors:
- Marianne E Bronner, California Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52648.sa1](https://doi.org/10.7554/eLife.52648.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript investigates the transcriptional changes in neural tissue accompanying tail regeneration in Xenopus tropicalis tadpoles. The key findings are that (1) the initial transcriptional response promotes neuronal differentiation, followed within 3 days by an increase in expression of genes associated with cell proliferation; and (2) meis1 and pbx3 emerge as important regulators of the neural regenerative response. This first finding in particular is novel and challenges the fundamental assumption that cell dedifferentiation and proliferation are the initial steps in regeneration. The novelty and potential significance of these observations, together with the overall quality of the work, merit publication in eLife. Moreover, the manuscript is very clearly presented, and the logical flow of the computational analyses is easy to follow.

Decision letter after peer review:

Thank you for sending your article entitled "Chromatin accessibility dynamics and single cell transcriptomics reveal new regulators of neural progenitor regeneration" for peer review at eLife. Your article is being evaluated by three peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Marianne Bronner as the Senior Editor.

All of the reviewers find the manuscript interesting and think that it will be potentially very useful to the community. That said, they also raise substantial concerns that will require major revisions.

Reviewer #1:

The manuscript by Kakebeen et al., is addressing a fundamental question in developmental and regenerative biology. With the realization of human therapies for nervous system regeneration after spinal cord injury, it is important to understand the strategies for regeneration that nature has already solved. The advent of new techniques such as scRNAseq and ATAC-seq have generated opportunities to study changes in cell state and type in complex cell populations, which Kakebeen et al., has made progress with here. Considering the authors are addressing a classic question in regenerative biology using the latest techniques, they’re of great value to the study. Overall, the ATACseq and scRNAseq seem robust, but there are some significant flaws in the design of the study that limit the interpretation that can be made by the readers. These problems are described below.

1) The choice of pax6:GFP as the driver instead of Sox2 is a major drawback of the paper, unless major reinterpretation of the data is performed. The impression made from the Introduction and Results is that the study focuses on all NPCs. Based upon previous literature, this is likely not the case. Pax6 plays a well-established role in determining the dorsal/ventral fate of NSCs in the developing spinal cord across vertebrates, namely the pMN domain, and is expressed in a restricted intermediate dorsal/ventral zone of the vertebrate spinal cord (Pituello, 1997; Reimer et al., 2009). The image in Figure 1B needs to be of higher quality in order to determine the expression pattern of the transgene, but it looks to be and is most likely expressed in a canonical fashion in the intermediate D/V zone of the spinal cord. I would suggest a thinner cryosection and a zoom in on the spinal cord specifically. Pax6 has also been associated with controlling cell cycle exit in neural progenitor cells towards differentiation (Bel-Vialar, Medevielle, and Pituello, 2007; Osumi et al., 2008), which should be kept in mind throughout the study. Also, canonical D/V pax6 expression is maintained in mature axolotl salamander spinal cords and dorsal/ventral position of NSCs mainly remain stable after spinal cord regeneration in the axolotl (McHedlishvili et al., 2007). Considering all interpretation of the manuscript is under the assumption that all NPCs are marked and differentiation is not specific to a D/V region, the interpretation is missing a lot of likely very interesting findings on pax6 function and D/V patterning during spinal cord regeneration. As is, it is difficult to interpret exactly what the cell population the pax6:GFP cells are labeling and what they are differentiating into during regeneration (see next statement).

2) It should be explained why cre/lox lineage tracing was not used in the study. As presented, it is unclear if the cell population that is being sorted is exclusively the NSCs or does it include the neurons they differentiate into. Based upon the gene families that were identified from ATACseq including genes involved in neuritogenesis and growth cone formation, it is likely the authors also sorted differentiated neurons or cells in the process of differentiating. It is known that GFP protein can last for days long after the transgene is not expressed. Use of a Sox2 Cre driver Xenopus mated with a fluorescent cre reporter would have overcome the ambiguity of the cells that are being studied and provide a clear trajectory of NSC to differentiated cell types.

3) The in situ hybridizations in Figure 5 do not support the sequencing data. At stage 41, both genes look to be expressed in all mesodermal tissue such as muscle. In subsection “Gene regulatory network prediction reveals pbx3 and meis1 as candidate

regulators of neuronal regeneration”, it states "Of these, pbx3 was the most restricted to the neural lineage (Supp. 3 E/G)". This is emphasized again in the Discussion. The in situ hybridization shows pbx3 is expressed throughout the mesenchyme of the regenerating tail at 48dpa. It will be important to perform cross sections of tissues to show expression in the expected domains, which will likely be the intermediate DV regions of the spinal cord (see new interpretations of pax6 cells above). I would suggest commercially available FISH such as hybridization chain reaction (molecularinstruments.com) or RNAscope that has higher resolution in the cellular level.

Reviewer #2:

The manuscript by Kakebeen et al., ("Chromatin accessibility dynamics and single cell transcriptomics reveal new regulators of neural progenitor regeneration") investigates the transcriptional changes in neural tissue accompanying tail regeneration in Xenopus tropicalis tadpoles. The key findings are that (1) the initial transcriptional response promotes neuronal differentiation, followed within 3 days by an increase in expression of genes associated with cell proliferation; and (2) meis1 and pbx3 emerge as important regulators of the neural regenerative response. This first finding in particular is novel and challenges the fundamental assumption that cell dedifferentiation and proliferation are the initial steps in regeneration. The novelty and potential significance of these observations, together with the overall quality of the work, merit publication in eLife. Moreover, the manuscript is very clearly presented, and the logical flow of the computational analyses is easy to follow.

I have two points of concern. The first is that, while the authors claim that pbx3 is predicted to be a key transcriptional regulator of the neural regenerative response, the results in Figure 5 indicate that only a very small proportion of neural cells express pbx3. (I found Figure 5E-5F somewhat confusing, and it may be that clarification of the figure legends will address this issue). If my understanding of these results is correct, however, then I suggest the authors revise the text, since, as written, it implies that pbx3 is critical to the entire regenerative response.

The second is in regard to the morpholino oligonucleotide (MO) experiments. The authors use two different MOs for each of the two targets, in lieu of a mispair control. While the pbx3 MOs lead to quite similar results, the meis1 MOs produce somewhat distinct phenotypes (compare Figure 5 C-D, 5W-X). This may be a sample size issue, or it may arise from the apparent greater effectiveness of MO1 vs MO2. Given the ongoing discussion regarding MO use, I would like to see the authors address this point in some way, either experimentally (e.g., a western blot comparing effectiveness of the two MOs in regulating endogenous pbx3 [Abcam has an antibody that works for mammalian species and zebrafish], but other strategies would be suitable) or via discussion in the text, which might also include results of computational comparisons to identify any other predicted targets.

Reviewer #3:

In this manuscript, Kakebeen et al. analyzed chromatin accessibility and single cell transcriptomes from pax6-driven GFP positive cells during Xenopus tail regeneration. The authors utilized transgenic pax6:GFP to sort neural progenitor cells (NPCs) throughout this study. They used deep sequencing, ATACseq, and SCseq to define transcripts, biological processes, and transcription factors that are central to spinal cord regeneration in the regenerating Xenopus tail. The authors concluded that NPCs place an early priority on neuronal differentiation early after injury, and prioritize proliferation at later stages of regeneration. They go on to perform morpholino-based functional analysis on two candidate transcription factors, and concluded that meis1 and pbx3 are required for spinal cord development and regeneration.

Overall, bulk RNA-seq, ATACseq and SCseq offer a powerful combination of tools to infer new insights into the cellular and temporal regulation of endogenous spinal cord regeneration Xenopus. The battery of analyses performed on these datasets is well-executed, revealing an early emphasis (6 hpa) on neuronal differentiation and a later emphasis on neural progenitor replenishment (72 hpa). The authors also use their scRNA-seq dataset to define new markers for neural cell types. However, this hypothesized temporal regulation of NPC injury responses is weakened by the following concerns:

1) The entire study is based on the assumption that pax6 is a general marker for NPCs prior to and during regeneration, and that pax6:GFP recapitulates endogenous pax6 expression throughout the time course of regeneration. While all the conclusions from this study are based on these assumptions, pax6:GFP transgenic animals were poorly characterized (Figure 1 and Figure 1—figure supplement 1).

– Higher magnification images and extensive co-labeling with well-established NPC markers throughout regeneration are critical for this study.

– Confirming that the transgene recapitulates endogenous pax6 expression is also critical for the study. The authors state pax6:GFP is consistent with developmental expression of pax6, but this is assuming regeneration will fully recapitulate development, which is not always the case. An additional concern is the stability of GFP over fine time windows as narrow as 6 hours.

– From the low mag images in Figure 1D, it seems that the transgene is not restricted to the spinal cord. This observation is further supported by scRNA-seq (Figure S3A), which indicates that pax6 is expressed in many cell types beyond NPCs.

2) Even with a full characterization of the transgene, this reviewer is always concerned about drawing conclusions based on a single genetic tool. In this case, it is impossible to rule out the presence of pax6 negative progenitor cells that differentially contribute proliferation versus differentiation at different time points after injury. Further, equally impossible is to rule out technical cell dissociation limitations that may cause differential cell representations in the analysis.

3) The main premise of the study is that NPCs place an early priority on neuronal differentiation before prioritizing proliferation. This is an interesting and potentially relevant observation that warrants experimental support.

– Detailed elucidation of cell proliferation (rostral and caudal to the lesion), migration, and differentiation are recommended in this case.

– These studies would also address the possibility that proliferation is occurring rostral to lesion and that NPCs are recruited into the regenerate where they differentiate into neurons.

– The authors supported their conclusion that NPC proliferation is not abundant until 72 hpa by referencing Love et al., 2011 and their own work (Chang et al., 2017). Chang et al., 2017 does not mention cell proliferation and instead shows an emphasis on immune response at 72 hpa in whole tail. Love et al., 2011 does show an increase in cell proliferation in whole tail at 72 hpa. To support the authors' conclusion that this boost in cell proliferation is indeed happening in the spinal cord, a marker for cell proliferation should be used in the pax6:GFP expressing tadpoles following tail transection.

4) The authors followed up on their SCseq findings by performing functional analyses for meis1 and pbx3. Unfortunately, these studies present a number of major concerns that dampen the excitement about the study.

– The morpholino experiments do not follow recent guidelines for morpholino use. Proper controls are recommended in this case.

– It is unclear how the authors concluded CNS/spinal cord developmental defects based on the severe morpholino phenotypes that were obtained even at the lower doses. These phenotypes are consistent with generic, overall toxicity phenotypes that are common to morpholinos.

– The severe developmental phenotypes caused by meis1 and pbx3 cloud the interpretation of regeneration phenotypes in these morphants.

– Neurofilament stains for uninjured wildtype and morphant animals should be included in Figure 6.

– What is the effect of meis1 and pbx3 morpholinos on cell proliferation in both injured and uninjured tadpoles?

– The authors claim meis1 is required for the neuronal differentiation occurring at early timepoints during spinal cord regeneration. They show that axons in the regenerating tail are disorganized in meis1 morphants, but are these neurons the appropriate neuron type?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Chromatin accessibility dynamics and single cell RNA-Seq reveal new regulators of regeneration in neural progenitors" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Marianne Bronner as the Senior Editor The following individuals involved in review of your submission have agreed to reveal their identity: James R Monaghan (Reviewer #1); Amy Sater (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This revised manuscript has addressed most of the concerns of the reviewers and is fundamentally suitable for publication after some edits in response to the few remaining issues raised by the reviewer. I ask you to address these to the best of your ability with editorial changes.

Revisions:

1) Subsection “Meis1 and Pbx3 are necessary for successful spinal cord and tail

regeneration” first paragraph: please add "antibody" after "anti-neurofilament"

2) The addition of Sox2 antibody staining and its overlap with pax6:GFP is informative. There is a small number of Sox2+ cells that are pax6:GFP negative, which the authors address in the text. However, reviewer 3 has two concerns with this data:

a) Sox2/pax6:GFP co-labelling is performed during tadpole development. This approach assumes pax6:GFP and Sox2 co-expression behave similarly in regeneration as in development, which is not necessarily the case.

b) The authors do not address pax6:GFP+ Sox2- cells. These cells, which are observed by histology and scRNA-seq analysis, could affect data interpretation in Figures 2 and 3.

3) pax6:GFP- Sox2+ NPCs do exist. How are these cells contributing to the differences seen in cell proliferation and differentiation during different stages of regeneration? Perhaps these are the pH3+ cells present at 24 hpa. These pax6:GFP- Sox2+ cells appear to be fewer in number, but their presence should be more clearly acknowledged in the text.

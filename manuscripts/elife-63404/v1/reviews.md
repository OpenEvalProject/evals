# Peer review - Round 1

Editors:
- Robert H Singer, https://ror.org/05cf8a891 Albert Einstein College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63404.sa0](https://doi.org/10.7554/eLife.63404.sa0)

The authors quantitatively assess transcriptional memory in the context of mathematical modeling and testing of the models through single cell approaches. They extend their work to show how single cell data relates to population-level transcription outcomes. The models produced make predictions that the authors successfully test to demonstrate that transcription initiation is not necessary for establishment of memory.


---

# Peer review - Round 1

Editors:
- Robert H Singer, https://ror.org/05cf8a891 Albert Einstein College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63404.sa1](https://doi.org/10.7554/eLife.63404.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Nup98-dependent transcriptional memory is established independently of transcription" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kevin Struhl as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

If it is possible to carry out the suggested experiment on transcriptional inhibition, we urge you to do so.

In this manuscript by Pascual-Garcia et al., the authors use single-cell gene expression analysis to dissect transcriptional memory in the ecdysone response. They explore several different models and the surrounding parameter space in order to fit the data and then arrive at a plausible multi-state model for how Nup98 might be enabling transcriptional re-activation. The overall conclusion is that ecdysone stimulation in the first round 'primes' the re-activation state through a Nup98-dependent process. This priming does not depend on transcriptional activation because treatment with the elongation inhibitor flavopiridol doesn't interfere with the memory response.

All the reviewers find the work interesting and potentially important. However before it can be published, they had several concerns in common. One of them deals with the clarity of the manuscript, in particular the explanation of the modeling and why certain states were chosen, and why so much text deals with the non-working model.. A second concern is that the quality of the FISH on which the approach is based is not optimal. A third concern, as expressed by all reviewers (esp #4) is that the use of the drug flavopiridol does not test the hypothesis that transcription is not necessary for memory because it acts primarily on elongation and not initiation, where chromatin modifications are made. Further data is requested using a drug that acts earlier in the transcription. Finally reviewer #1 questions the conclusion that RNA turnover is not a factor given the time for memory to occur.

The full reviews are below. We feel that the essential experiment would be to determine which component of transcriptional inhibition (initiation, escape) is essential or not for memory.

Reviewer #1:

This is a combined modelling and experimental study probing the nature of the ecdysone induced memory response in S2 cells. This is a very interesting biological problem, and detailed mechanisms- beyond data indicating that protein X or modification Y are required, have proved elusive outside the yeast GAL system. As such, studies probing the causality underlying transcription memory phenomena are welcome.

In the study, the simple models of transcriptional dynamics are discarded, with reference to qPCR and smFISH data and measurements of export and RNA turnover. The researchers fix on a 4 state model that fits the data well, then test 2 predictions of the model- based on the requirement for transcription and the timescale of the memory phenomenon.

The work appears well performed, and for the most part clearly documented, and should certainly be part of the scientific record in close to its current form.

My major reservation is the state of the field. This paper seems largely a model optimisation paper, and the work appears very well carried out. However, there are many different multi-state models around these days, all specific to different genes and systems. From the perspective of understanding transcription dynamics- does this carry us further? From the perspective of memory, it is interesting the transcriptional elongation at the locus is not initially required- but the state change of the cell, or gene, that brings about the memory is no clearer beyond this.

One issue that needs to be addressed before publication relates to the RNA turnover aspect. In the experiment in Figure 2B this analysis is conducted at 4h not 24h (when the initial memory effect was detailed in Figure 1), so is your conclusion about no role for RNA turnover relevant to the memory phenomenon? Especially in the light of Figure 7, where both the experiment and model indicate a longer timescale is required to get the memory effect.

Reviewer #2:

Transcriptional memory is a phenomenon whereby certain inducible genes show stronger/faster induction if they have previously been expressed. This behavior can persist through multiple cell divisions. Such phenomena have been explored in yeast, plants, flies and mammalian cells and several different types of memory have been discovered. In the cases where we have some mechanistic understanding, there are two classes of memory. The regulation of some genes is impacted by the persistence of transcriptional regulators that were previously produced and cytoplasmically inherited (e.g. yeast GAL1). The second class of genes (e.g. yeast INO1 and interferon γ-induced genes in HeLa cells) there are cis-acting changes in transcription factor binding and/or chromatin structure that impact future expression. This latter class of genes shows a physical interaction with the nuclear pore protein Nup98 and memory requires Nup98.

This manuscript explores the transcriptional memory of ecdysone-regulated genes in Drosophila S2 cells, a phenomenon that is Nup98-dependent and correlates with a Nup98-modulated enhancer-promoter loop. The focus of the study is a thorough and quantitative anlalysis of the population dynamics of transcription during the initial induction and memory phases using single molecule RNA FISH. These data are then used to assess three different quantitative models for memory: 1. A two-state model in which memory increases the number of cells that respond to ecdysone, 2. A two-state model in which memory increases the rate of RNA polymerase loading onto the promoter and 3. A four-state model in which these genes exist in an equilibrium between two different expression states (low and high) and this equilibrium is regulated by memory. The authors find that model 3 is the best fit for the observations and, importantly, this model makes two predictions that they could test. First, this model predicts that transcription should not be required for memory. Second, memory should "develop" following the initial induction over some time scale. The authors then test both of these predictions and find that they are true. The former is interesting and rules out that the production of a transcriptional regulator during the first induction is key to this process. The latter is very interesting and surprising and will stimulate additional work to discover its meaning. Overall, the paper is interesting and impactful and worthy of publication in eLife. I have some suggestions for clarifying changes to the manuscript and, if possible, additional experiments that would strengthen the story.

1. The four state model is not well described in the manuscript and the schematic in Figure 5A is confusing. This schematic suggests that there are equilibria between non-memory and memory (which is understandable) and between low-expressing and high-expressing states (also understandable) but that there is also an equilibrium between non-memory and low-expressing and between memory and high-expressing, which does not make sense to me. I think what the authors are trying to convey is that the equilibrium between low-expressing and high-expressing states is influenced by Nup98-dependent memory. If so, then the model should include the following states: non-memory, low-expressing, non-memory high-expressing, memory low-expressing and memory high-expressing. Between each of these states would be an equilibrium and the equilibrium constants for the equilibrium between low and high expressing states would be different for non-memory and memory. I assume that this is how they generated their model. If not, please spend more space to clarify the model and provide an explanation of how the non-memory state is in equilibrium with the low-expressing state, etc.

2. The technical perfection of smRNA FISH is unclear. I doubt it is perfect. Yet, the modeling is highly leveraged on the goal of matching the smRNA FISH data. Some additional controls would strengthen the interpretation. For example, the untreated S2 cells (0h) should be included for the smRNA FISH and modeling. Likewise, knowing how control genes that are not up/down-regulated by ecdysone behave in smRNA FISH would improve the rigor of this approach.

3. Some molecular information about transcription factor occupancy or chromatin changes at the enhancer that is involved in the memory-enhancing loop would greatly strengthen the mechanistic insights of this paper.

Reviewer #3:

In this manuscript by Pascual-Garcia et al., the authors use single-cell gene expression analysis to dissect transcriptional memory in the ecdysone response. They explore several different models and the surrounding parameter space in order to fit the data and then arrive at a plausible multi-state model for how Nup98 might be enabling transcriptional re-activation. The overall conclusion is that ecdysone stimulation in the first round 'primes' the re-activation state through a Nup98-dependent process. This priming does not depend on transcriptional activation because treatment with the elongation inhibitor flavopiridol doesn't interfere with the memory response. Although there is not much biochemical insight, I find this conclusion interesting. Overall, the analysis is fairly rigorous, and I applaud the effort to apply more quantitative models to the field of transcriptional memory.

1. The modeling is a mix of ordinary differential equation analysis and stochastic simulations with the Gillespie algorithm. It is a little unwieldy at times, and I feel the manuscript spends quite a bit of time on a model which doesn't work. Since this non-working model is the authors' invention (and not a standard in the field per se), it seems a bit awkward to present the story this way. Ideally, all the models would be stochastic models from the beginning since the single-cell analysis is the main thrust at the end. Although I find their approach a little ad hoc given the current state of the field, I don't feel strongly enough about it to demand a more rigorous treatment.

2. The persistence of memory in the presence of flavopiridol is a striking result. Would the authors predict a similar result for an inhibitor working upstream of transcriptional pause release? Specifically, the authors mention in the discussion that enhancer-promoter loops may be implicated. One experiment which the authors might consider (which I am not suggesting as necessary for a revision) is whether antagonists or partial agonists can uncouple these two activities of ecdysone. In other words, they have a negative result which emerges as a model prediction but not a positive result.

Reviewer #4:

The authors use a combination of RT-qPCR, smFISH and mathematical modeling to probe the mechanism and contribution of NUP98 to transcriptional memory upon hormone stimulation in Drosophila cells. The authors reveal that the transcriptional memory response is independent of transcription levels immediately after hormone treatment. Furthermore NUP98's role in transcriptional memory relates to its ability to stabilize a slow transition (~20 hrs) of the gene from low-expression to high-expression state. While the results are quite striking and the interpretations are timely in some regards, a few controls and clarifications in the text are necessary before recommending publication in eLife.

1. The authors rely heavily on smFISH to validate their computational modeling. However, the accuracy of quantitation of the smFISH is not evident. The authors should show a histogram of intensities of single diffraction limited spots along with a representative figure of multiple zoomed in panels of the single RNA spots. This is important as the majority of spots, particularly in the transcriptional memory response, are not diffraction limited which complicates both the presentation and analysis of their data.

2. Is there any evidence of E74 being alternatively spliced which may differentially affect FISH probe binding to the mRNAs producing large heterogeneously sized diffuse spots seen in the figure 1D?

3. While the differences are readily apparent in most of the data, the authors do not show any statistical testing in many if not most plots (e.g. violin plots Figure 1E). This should be corrected in a revised manuscript.

4. S2 cells are considered aneuploid. For nascent transcription site analysis, it would be helpful for the readers to see a simple diagram showing the percentage of cells showing 1, 2, 3, 4 etc active TS sites throughout the time course as it was not apparent whether a certain percentage of cells in the population never expressed E74.

5. Figure 7 is one of the most key figures that the authors use to conclude that NUP98 is stabilizing a memory state independent of transcription. Yet they have chosen to use a less informative assay (e.g. RT-qPCR) rather than the most sensitive assay (e.g smFISH) to support their model and conclusions. The authors would make a stronger case for their findings if they employed smFISH to monitor transcript abundance and TS activity after inhibiting transcription.

6. FP primarily only prevents Pol II pause escape and not promoter escape of Pol II. So transcription initiation and Pol II loading at the promoter still occurs in flavopiridol treated cells. This is important because chromatin marks associated with active transcription are likely still being placed in the promoter and enhancer regions of E74 even though a complete transcript is not being produced. The authors should repeat their assays and treat the cells with inhibitors such as triptolide or THZ1 that act earlier in the transcription cycle or better yet use an ecdysone receptor mutant that prevents Pol II recruitment or chromatin modification to the gene in the first place.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Nup98-dependent transcriptional memory is established independently of transcription" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kevin Struhl as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jonathan R Chubb (Reviewer #1); Jason H Brickner (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

All reviewers find that the manuscript is novel and exciting. However reviewer #4 has additional comments that need to be addressed, in particular the observation 1 that triptolide is not required for PIC formation in Drosophila. This issue needs to be addressed in the Discussion along with other issues raised by this reviewer. Please send a response to these comments with the revised manuscript.

Reviewer #1:

This is a much improved manuscript, and deals extensively with the comments raised by myself and the other reviewers. The additional experiments, particularly the more comprehensive RNA turnover work, and the transcription initiation blockade, are a great addition. I think that the overall message is much clearer in the revised paper, with the condensed version of the modelling much more straightforward to read. The overall message, that the transcriptional process is not required for the sensitisation, is now much more clear than I found in the initial submission, and is an important addition to the cellular memory literature.

Reviewer #2:

The authors have responded to my suggestions and, in some cases, added additional data or clarification to the paper. The manuscript is now stronger and publishable in eLife.

Reviewer #4:

The authors take an important step in quantitatively assessing transcriptional memory in the context of mathematical modeling and testing of the models through single cell approaches. Furthermore, the authors extend their work to show how single cell data relates to population-level transcription outcomes. This second approach is highly relevant since transcriptional memory has been traditionally studied at the population-level allowing interpretation of previous studies in the context of single cell data. More importantly, the models produced can make predictions that the authors successfully test to show that transcription initiation is not necessary for establishment of memory. The authors do a good job of addressing the reviewer's critiques. While a clear mechanism for Nup98 establishment of memory is still lacking, I think that this manuscript represents an important step in integrating single cell data into studying memory. There are a few critiques that should still be addressed before final acceptance for publication.

1. While the authors indeed show that transcription initiation is not required for memory, Triptolide treatment does not prevent PIC formation in Drosophila (Krebs et al., 2017, Mol Cell, which the authors cite in the manuscript). PIC assembly actually increases during Triptolide treatment suggesting that key factors and histone marks related to the assembly of the PIC (e.g. H3K4 methylation due to its presumed role in recruiting TFIID) are likely still present and capable of establishing memory in the absence of initiation. The authors should be very clear of this possibility in the discussion.

2. Lines 175-177 the authors are essentially making a statement about transcriptional noise being independent of Nup98. It would be highly beneficial to quantitatively measure transcriptional noise (CV2 or std2/mean2) under the different conditions to validate this statement.

3. I realize that Models 1 and 2 are not viable in the end. However, the wording in Lines 301-306 is misleading creating a potential flaw in these models that seems to be carried throughout the manuscript. The authors invocation of a quantitative assessment of the PIC (e.g. Author's should use the term PIC since RNA Pol II holoenzyme can be confusing) footprint into the model is naive and underestimates the role of a stable TFIID scaffold and TFIIB in re-initiation rates (Zhang et al. Genes and Dev 2016, Yudkovsky et al., Nature 2000). It is highly likely that core promoter accessibility plays a major role in going from an inactive to active state. But core promoter accessibility would likely be a binary effect and not scaleable as the authors seem to intimate in lines 302-304 and let freely fluctuate in their modeling. Model 1 and 2 also assumes that transitions to the inactive states are negligible suggesting that the gene is stuck in the ON state and therefore Nup98 is enhancing Pol II's attempted loading onto a stable PIC scaffold of defined size (e.g. footprint).

4. It would be interesting to see whether the FP and TL treatments change the distributions of transcriptional output during the second induction in single cells compared to those shown in Figure 4.

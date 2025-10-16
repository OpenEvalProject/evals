# Peer review - Round 1

Editors:
- Robert H Singer, Albert Einstein College of Medicine United States

Reviewers:
- Zhe Liu, Howard Hughes Medical Institute, Janelia Research Campus United States

## Review text

DOI: [10.7554/eLife.41769.053](https://doi.org/10.7554/eLife.41769.053)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Live-cell imaging reveals enhancer-dependent Sox2 transcription in the absence of enhancer proximity" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kevin Struhl as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Zhe Liu (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The work provides the first precise measurement of enhancer-promoter distances correlated with transcriptional output. Surprisingly, the proximity of the enhancer and promoter was not correlated with the output. This challenges current dogma that these two elements must come together to initiate transcription. The authors propose an activator hub model where factors are concentrated around the promoter in a large volume.

While the reviewers are positive about the work (one even thinks it is a "landmark"), they have a number of concerns, mainly centering in the accuracy of the distance measurements. Since these distances are critical to the argument and since the conclusion is heterodox, confidence in the measurements are essential. For instance, how was chromatic aberration corrected? They suggest additional controls to verify the measurements. An example would be to show the tagging did not affect the looped interactions by comparing 3C interactions between the experimental and wild type cells. Additional suggestions were to improve the text for clarity and accuracy in interpretation.

Please read through the suggestions for improvements and determine whether you can respond adequately within a few months. If so we will entertain a revised manuscript for review.

Reviewer #1:

This manuscript investigates the long held belief that distal enhancer sites must directly contact the promoter site to activate transcription. This required heroic genetic labeling of the endogenous Sox2 promoter, a Sox2 enhancer locus, as well as the messenger RNA being transcribed. They conclude by many analyses that the position separation between enhancer and promoter is not correlated with gene expression in contrast to the expectation of a direct contact between promoter and enhancers. They propose that recent observation of condensates of transcription factors, and or more complex delay models may be at play in the Sox2 locus investigated. This is an experimental tour de force that will prove important, prompt and guide many future experiments. The manuscript warrants publication in eLife. There are questions on the accuracy of the position measurements that should be addressed as a major concern as that will set a standard for how future measurements may be done; however these should be doable within the time frame allowed by the journal for a revision.

A major issue to be resolved is the question of how accurately the chromatin labeling arrays represent the Sox2 promoter and SCR positions. This becomes apparent when comparing the MS2 signal position to the Sox2 promoter marker position in 3 color imaging. The MS2 signal typically appears to be detected far from the Sox2 promoter signal. This may be due to technical reasons (different filter cube, time delay between Sox2/SCR and MS2 stacks) or represent actual spatial separation between the promoter chromatin label and the Sox2 gene position. This is particularly true since a 14kb separation in the deletion mutant appears to result in a typical separation of ~250nm and never below 100nm. The authors should provide a control for the positional accuracy of their chromatin labels with respect to the target sequence, e.g. co-staining of the actual target locus by DNA FISH or dCas9-based chromatin labeling.

Reviewer #2:

In this paper, Alexander and co-workers address the important topic and enhancer-promoter (E-P) contacts using the Sox2 gene in mESCs as a model. While there was a recent E-P live-cell imaging study in Drosophila from the Gregor group, the Gregor system was a bit artificial and genome organization is very different between mammals and flies. The present study by Alexander is therefore very important: To my knowledge, it is the first live-cell imaging study of E-P contacts in mammals. This is important, because Hi-C, which averages over cell populations and only generates a snapshot cannot readibly report on dynamics. Getting at the dynamics can only be achieved with live-cell imaging, which is what Alexander has now accomplished.

Other highlights include a nice general system for tagging DNA loci (though authors need to put plasmids on AddGene), nice controls (e.g. the other cell lines with similar distances and the 111 kb deletion), comparing mESCs and NPCs and the simultaneous MS2-readout to simultaneously look at transcription.

The findings are also surprising and will be of wide interest. I believe there is a strong possibility that this paper will be looked back upon in a couple of years as a landmark paper in the field and I believe it will be of very wide interest.

Nevertheless, I have a series of serious technical concerns, which should be addressed and I believe that authors should do one important control experiment: verify using a "C"-method that the E-P loop is not disrupted. Finally, given the technical concerns – some of which may not be fully addressable – the authors need to more clearly state the limitations of their work in the main text. Also, many imaging details that are crucial, are missing from the Materials and methods.

Activator hub model

In Figure 6H, authors propose an "activator hub model" where a large hub (maybe 200-400 nm?) activates over long distance. This is an interesting model. If it is true that it is so big, presumably many other genes would be inside of it. Are there other other genes within 1 Mb of Sox2 on the same chromosome? Are they ON or OFF and if some of them are OFF, how do they stay OFF if there is a large hub?

If the hub is a 400 nm cube and mouse ES cells are diploid, they should have 2 of these hubs and around 50k genes (since diploid). Using the typical volume of a nucleus (e.g. 8 μm cube), one gets total hub volume 0.128 μm3 and nuclear volume of 512 μm3, corresponding to 12.5 genes inside of the hubs. Is this realistic? Numbers chosen here are a bit random, but the point is that it seems a bit dangerous to have a large hyper-activating hub in the nucleus (like the LLPS studies the authors reference) since it would be likely to randomly contact genes that should be OFF – especially since chromatin moves around as the authors show. If this hub lasts for 10 minutes, how many random genes will bump into it? The nucleus is a pretty crowded environment. Can the authors discuss this a bit more clearly?

New tools to visualize DNA loci should be on AddGene.

In addition to the biological insight, a big impact of this paper will be the new tools the authors develop to insert TetO and CuO sites in the genome. The 2-step modular approach with attP, PhiC31, Bxb1 etc. is clever and the TetO and CuO plasmids will be generally useful. However, I could not find the AddGene Accession codes for these vectors. In the revised manuscript, the authors should deposit these plasmids to AddGene and include the accession numbers in the manuscript. Moreover, the authors should write a brief protocol on how to use the plasmids and attach it to the manuscript. This will greatly increase the impact of the paper and serve as a big positive contribution to the community.

Key control

It is very nice that authors verify that array insertion does not affect Sox2 expression according to qPCR. This is a really important control. However, the missing and equally important control is the verification that the Sox2-SCR looping interaction is not affected. Authors could argue that since SCR is required for expression, the fact that Sox2 qPCR is the same, suggests that looping level is not affected. But since the authors suggest that E-P loops don't directly affect transcription, this is no longer the case. Therefore, an essential (and straightforward) control experiment to do for the revised manuscript is a 3C-qPCR (or another C-type) experiment comparing Sox2-SCR E-P contacts in WT cells, cells with the arrays but without TetR and CymR and cells with arrays and also TetR and CymR.

Localization Precision

I am somewhat skeptical of the localization precision. It seems a bit weird that the X and Y values are so different. Also 10-15 nm is really high precision. It seems almost too good. I worry that even if the authors tried to use beads at lower light intensity, this could bias the calculation. It is also not clear how well a TetraSpeck bead approximates the unknown distribution of in vivo conformations of e.g. an 8 kb array inside a live cell. Is there any way the authors can use the TetO and CuO readouts to estimate the errors? E.g. in fixed cells?

Distance between Promoter and SCR and CuO and TetO arrays

The distance between the Sox2 E and P is quite high (17 kb). I totally get that it is tricky: if you put the arrays too close, they may interfere with function. If you put them too far away, they may not be good reporters and it is not obvious to me what the best distance would be. But given the wide distribution in Figure 2C yellow line, I believe the authors should emphasize a bit more in the main text that this introduces some uncertainty and is an important caveat.

Timescale of E-P loop and time-scale for MS2 appearance

One key thing I was missing was a discussion of the time-scale of E-P loops. E.g. recently there have been papers arguing that CTCF/cohesin loops are either stable or dynamic and it would be nice if the authors could discuss how their observations relate to this (even if they do not directly observe discrete E-P loops). For example, does the Sox2 loop occur inside a CTCF/Cohesin loop and can the authors compare to some of the CTCF/Cohesin timescales?

Along these lines, the analysis in Figure 6 is very important in that it tries to find a correlation between E-P distance and transcription. But although the result is negative, can the authors really exclude that E-P contact is necessary for Sox2 transcription.

Suppose the following scenario: E-P loops form and last for 10 seconds (but duration highly stochastic, sometimes 1 sec sometimes 100 sec). Soon after they break, Sox2 E and P move apart and the distance increases. The E-P loop even when the true distance is <50 nm, will show a broad distribution of distances similar to yellow line in Figure 2C. After E-P contact, Transcription factors, histone modifying enzymes, mediator, Brd4, p300, TBP, SAGA, TFIID and other factors are recruited but sequentially and with delay between each. This takes an unknown amount of time. Then Pol 2 is recruited. Pol 2 pauses for a bit and then begins transcribing. Since the MS2 reporter is 3', there is a very long delay between Pol 2 initiation and MS2/MCP-readout (the authors should calculate the expected time it takes from initiation to MS2 appearance using the estimated Pol II elongation speed and the length of the Sox2 modified gene and report this duration in the main text). For the sake of argument, let's say this process takes 7 min on average, but because of the many steps, each of which is stochastic, the duration is broadly distributed and heavy tailed such that it can take anywhere from 3 min to 15 min (or something like this).

In this scenario with: 1) very transient E-P contact measured using the very high localization uncertainty shown by the yellow line in Figure 2E; 2) highly stochastic and variable duration for in-between steps and 3) long and somewhat variable delay before MS2 appearance since reporter is 3' and 4) E-P contacts only produce transcription burst say 40% of the time. Would the authors really be able to detect a positive correlation using the analysis in Figure 6?

My sense is that the authors could not, though I would be happy to be persuaded otherwise by a careful quantitative analysis. This does not mean that the author's contribution is not highly valuable, but unless they can exclude this possibility, they should state explicitly in the main text or discussion that they cannot exclude that their analysis fails to detect the underlying E-P inducing Sox2 transcription.

Authors kind of sketch this in 6H top panel, but I found the discussion about these limitations unclear and lacking. It is much better to clearly state the limitations.

Encounter definition

Authors include a very nice control cell line, where 111 kb has been deleted between the pairs. This cell line is "always in encounter" in the sense that the CuO and TetO arrays are about as close as they would be in a bona-fide E-P loop. Looking at Figure 2C, it looks like the mean distance is 250 nm and the range is approximately 0-500 nm. That means that perfect E-P co-localization can nevertheless appear as 500 nm at low probability. But in Figure 4E, authors define encounter as 100 nm. If the mean E-P distance during an encounter is 250 nm (Figure 2C), defining the threshold to be 100 nm seems too restrictive.

Obviously, it is very interesting and informative to consider the probability of an encounter during a time window, but given the much larger mean distance for the control E-P loop cell line, 100 nm is too small. I am not sure how best to deal with this but current Figure 4E seems unfair.

One option would be for the authors to clearly state this limitation in the main text and then re-plot Figure 4E for multiple thresholds – e.g. 100, 150, 200, 250, 300, 350 nm. At the very least, they should also consider thresholds a little bigger than the mean E-P distance in the control cell line (yellow line in Figure 2C).

Information about imaging and the microscope

Technical information about the microscope and imaging protocol is extremely important to evaluate the study, but highly lacking.

What was the pixel size?

What were the emission filters?

How many z-stacks and how long exposure times?

What were the time-gaps between z-stacks? What was the physical distance between the z-stack?

I could not understand – did the authors collect all colors per plane and then move to the next plane or did authors do sequential all planes for each color and then acquire next color?

Authors must report duration of z-stacks?

How did authors correct for chromatic aberrations? Authors mention shifting position, but I could not understand what they did.

How did authors align color channels?

How did authors determine 3D positions? Was it PSF-fitting? If so, what was the PSF-model? Did they enforce symmetric XY PSF or allow asymmetric XY-PSF? Did they do MLE or LS fitting?

What were the settings used in TrackMate? Were gaps allowed?

Etc. Etc. Please provide all details in the Materials and methods since they are important.

Reviewer #3:

Large Picture:

A central model in the current understanding of gene regulation is that direct physical interactions between promoter and enhancer are required for transcriptional activation. It is widely believed that long-distance promoter-enhancer communications are realized in the form of chromatin looping. In this manuscript, the authors devise comprehensive live-cell imaging experiments to test this model using Sox2 locus and Sox2 control region (SCR) – a strong long-distance enhancer required for Sox2 expression. Specifically, by incorporating CuO and TetO arrays into Sox2 locus and SCR respectively, authors established a robust molecular imaging system to precisely quantify the physical distance between Sox2 and SCR in the nucleus of single living ES cells. Surprisingly, authors find no evidence supporting Sox2-SCR interactions in comparison with SCR-control loci pairs. And, consistent with DNA-FISH results on HoxD locus (Genes and Dev. 2014. 28: 2778-2791), authors also showed that upon ES cell differentiation, the genomic region containing Sox2 and SCR compacts as the distance between Sox2 and SCR becomes shorter. Most strikingly, author found no temporal correlation between Sox2 transcription bursting and the proximity of the SCR to Sox2 locus. These emerging results began to challenge the central model regarding DNA looping as the primary mechanism that mediates long-distance enhancer-promoter communications.

I found that the experiments done by authors are very well controlled and the results are timely for the field to move forward in search for alternative mechanisms. I would like to support the publication of the manuscript.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Live-cell imaging reveals enhancer-dependent Sox2 transcription in the absence of enhancer proximity" for further consideration at eLife. Your revised article has been favorably evaluated by Kevin Struhl (Senior Editor), a Reviewing Editor, and three reviewers.

The manuscript is acceptable but there are some remaining issues that need to be addressed. In short, the reviewers would like to see some additional comments regarding the lateral resolution and the inclusion of some of the raw data.

Reviewer #1:

I think given the time frame the authors appropriately addressed the concerns raised.

The authors should provide some of the raw uncorrected video.

Reviewer #2:

We are satisfied with the revisions. This was a valiant effort, and the authors satisfied most of the requests. We believe that manuscript is vastly enriched.

One remaining issue it the claimed lateral resolution. Here the authors use a published method to estimate it that is providing a result that seems out of scale compared to what is typically achieved. I could not pinpoint what is wrong and therefore cannot comment more. Perhaps one way for the authors to explain their number would be to comment and provide their own rational comparing this value to other papers and explain how they improved it so much. Also it would be important to comment on the validity of the tool they use to localize a locus. This is important since other papers might use similar methods and will not necessarily achieve such results.

Because the lateral resolution issue will be a major problem to other labs trying to reproduce the data I would suggest that the authors prepare a set of raw videos that are representative of the dataset and their quantification of it so that others can use it as a benchmarking tool.

Reviewer #3:

This was a strong paper and, in the revision, authors have improved the manuscript more and satisfactorily addressed my concerns. I would support the publication of the paper in eLife.

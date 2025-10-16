# Peer review - Round 1

Editors:
- Vaughn S Cooper, https://ror.org/01an3r305 University of Pittsburgh United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80808.sa0](https://doi.org/10.7554/eLife.80808.sa0)

In this work, the authors present compelling evidence that a toxin-antitoxin system contributes to biofilm dispersal under oxygen limited conditions. This work makes important contributions to two areas of microbial physiology; functional understanding of toxin-antitoxin systems, which have remained largely elusive, and mechanistic regulation or biofilm dispersal, is a critical, but less understood aspect of biofilm physiology.


---

# Peer review - Round 1

Editors:
- Vaughn S Cooper, https://ror.org/01an3r305 University of Pittsburgh United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80808.sa1](https://doi.org/10.7554/eLife.80808.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "eDNA-stimulated cell dispersion from Caulobacter crescentus biofilms upon oxygen limitation is dependent on a toxin- antitoxin system" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The authors attempt to measure parDE expression in different areas of a biofilm with a promoter-lacZ reporter in which activity of the reporter is measured with a substrate that becomes fluorescent when cleaved by the lacZ gene product. This is a clever approach, but it lacks normalization by cell density, a typical feature of assessments of promoter-lacZ fusions. On first pass, the results presented are identical to what one would expect based on differences in cell density alone and I don't believe any conclusions can be drawn about expression of parDE4 across the biofilms grown in static cultures. Given that the authors have already built PparDE4-GFP fusions, it would be quite straightforward to repeat the experiment presented in Figure 8A by comparing PparDE4-GFP signal with a constitutively expressed red fluorescent protein for normalization of cell density. However, the use of stable reporter proteins poses a problem as these would accumulate more in non-growing or slow-growing cells and not necessarily read out cell density. The best solution here therefore would be to measure expression by directly measuring RNA levels (qRT-PCR or RNA-seq) not via stable protein reporters.

2) While the introduction presents background on TA types, and known TA involvement in biofilms, there is no discussion about other known roles of TA function. In particular, post-segregational killing seems like a relevant topic since this is presumably a similar mechanism as what is being observed here (in that case, TA transcription stops due to plasmid loss, while here TA transcription is reduced due to O2-dependent regulation). Several of the points made in the discussion about TA systems/PCD could also be made in the introduction to more clearly set the reader up with the necessary context to appreciate the impact/contribution of this work (e.g. some of the controversy in the PCD/TA literature, the inverse relationship between TA transcription and activity).

3) The choice of media in each experiment is not clear, but as the authors know, has important implications for biofilm formation in terms of baseline fraction of cells which elaborate holdfast and sensitivity to surface stimulation of holdfast synthesis. Furthermore, no rationale is given for media choices. The authors should be explicit in each experiment about the growth conditions including media, or at least state that all physiological experiments are were done in the same medium. The methods section ambiguously states that cells were cultures in either PYE or M2G.

Reviewer #1 (Recommendations for the authors):

Suggested experiments to further support the key conclusion that the ParE toxin is responsible for cell death:

– Make a catalytically inactive toxin variant to see whether cell death requires the toxin activity.

– Measure ParE activity directly e.g. assess whether cells have altered sensitivity to gyrase inhibiting drugs, image cells at higher resolution (possibly with DAPI staining) to determine whether changes to cell morphology is consistent with gyrase inhibition.

Suggested experiments to address whether transcriptional repression of ParDE4 leads to release of the toxin and thus cell death:

– Measure protein levels of toxin and antitoxin by western blot in O2-limited cells to see if there is a change in ratio of toxin and antitoxin

– Shut off parDE transcription either by placing the locus under control of a repressible promoter or using CRISPRi, then measuring growth (or evidence of ParE activity) after repression. In both cases, growth inhibition consistent with ParE activity should now be O2-independent.

Reviewer #2 (Recommendations for the authors):

Given the timing of biofilm formation, in the experiments involving growth in a flow cell, it seems the authors have used defined medium in which wild-type cells have a low propensity for holdfast synthesis and attachment. Though not essential for this publication, I wonder if parDE plays a role in PCD and dispersal when cells are grown in richer, more complex PYE media where attachment is more robust.

I have several questions/comments about the measurements and experimental conditions for the static growth experiments:

The authors claim to quantify "cell death and eDNA release in these biofilms" (line 148) but the measurements of live/dead cells and eDNA are from the planktonic phase not the surface attached cells. I suspect the phenomena that parDE4 contributes to cell death and eDNA release under limited oxygen conditions is not limited to surface attached biofilm conditions, thus I don't question the data, but rather how it is discussed. I recommend the authors focus on "culture conditions" rather than "biofilm condition" in the early part of the paper where they establish that parDE4 contributes to cell death under oxygen limitation. Certainly the culture conditions affect biofilm dynamics, but I suspect these phenotypes do not require the cells to be in a biofilm. If the authors wanted to formally examine this idea, and specifically test if the cells needed to be in a biofilm to 'feel' the effects of parDE4 and low oxygen, they could repeat the static culture experiments in a holdfast null strain. I predict that cell death and eDNA release would be comparable to holdfast competent cells, without the potentially confounding effects of cell attachment.

Figure S1A: Please be more explicit about how the growth measurement were made. Did you measure the same tube over time? Were the cultures mixed prior to measuring OD? If so, how did you maintain the aeration condition? Or did you set up parallel tubes and make terminal measurements at each time point? Growth medium?

Line 36: use of an acronym in abstract without definition

Line 79-80: perhaps emphasize "new-born swarmer" and consider "dissociate" instead of "disperse".

Line 150: 'viability' was not measured. Please rephrase to reflect the experimental measurement.

Please add scale bars to all microscopy images (Figure 2 and 4).

line 189: Similar to other comments above, the authors should rephrase point 1 as they don't measure cell death "in the biofilm". Perhaps instead: "ParD4 has a protective effect against cell lysis that enhances biofilm formation".

The red signal corresponding to dead cells is very difficult to see in Figure 2. From the images as presented, it doesn't seem that 40% of WT cells are dead. Consider showing the channels separately and merged. Also given the difficulty if seeing sparse signal on a black background, consider scaling the images differently (for example from 0=white to max=color, or present the single channels as inverted BW images).

Line 181: activation of TAS is not just about "production" of the proteins. More generally activation comes when there is an imbalance in steady state levels, and reduced stability of antitoxins compared to toxins is an important contributor to these imbalances. The discussion should be enhanced.

The authors should clarify metrics used to quantify microscopy images. It seems that the authors use thresholded areas in a binary fashion that ignores information from signal intensity. But it in these multidimensional structures, areas with thicker cell masses should have higher signal than areas with monolayers of cells. By simply thresholding the images and quantifying area, the authors loose a dimension of the data. Summing intensity in areas where signals overlap seems more informative than simply treating the pixels as binary.

Figure 6D, would be better presented more parallel to 6C such that the Y-axis reflected "relative biofilm formation (∆parDE4 / WT)" rather than "biofilm formation (% of WT)". This would also be more consistent with the language in line 280.

It is not clear why some experiments assess ccoN expression via a promoter reporter and others via transcript abundance by RT-PCR. Nevertheless, the RT-PCR experiments should be labeled as ccoN transcript levels rather than PccoN expression (line 273 and Figure 6B). Also I suspect that ccoN transcript is essentially undetectable under maximal aeration conditions leading to a denominator of practically 0 in the "fold-change". While I have no question about the veracity of the data, I prefer non-normalized (non-ratioed) data whenever possible, especially when one condition is essentially "off". Just my two cents.

Line 306-7: wording is somewhat confusing.

Figure 7 and S3: I have several suggestions for data presentation. Make the data points smaller in the scatter plots to better visualize the density of points near the axis. Consider plotting on a log scale rather than a linear scale to better spread the points with lower intensity and highlight the bulk of the cells rather than the handful of outliers which are what is primarily obvious on the linear scaling.

Please indicate how the threshold was determined to assess if each promoter was on or off for figure 7A. How many cells have "both"? Is "non-labeled" the best description of cells in which neither promoter was sufficiently active to be called "on"? Even "non-fluorescent" seems better than "non-labeled" as label implies staining.

Line 505: the authors report using 10 ug/ml of chloramphenicol to select for plasmids in Caulobacter. This seems extremely high and quite inhibitory even in the presence of a Cm resistance gene. Typically for Caulobacter 1-2 ug/ml chlor is sufficient to maintain a plasmid. Please check if this number is correct.
